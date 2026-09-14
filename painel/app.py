#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Painel de conteudo da Wicorp.

O site publico continua 100% estatico: HTML, CSS e JS, sem nada dinamico.
Este painel e a UNICA parte que roda codigo no servidor. Ele edita o
conteudo.json, processa as imagens enviadas e chama o build.py, que regera
as paginas estaticas. Se o painel cair ou for desligado, o site continua
no ar exatamente como estava — e essa e a ideia.

Rodar:  python3 painel/app.py
Ver:    http://127.0.0.1:8090/admin
"""

import hashlib
import hmac
import json
import os
import pathlib
import re
import secrets
import subprocess
import sys
import time
import unicodedata
from datetime import date, datetime

from flask import (Flask, abort, flash, redirect, render_template, request,
                   send_from_directory, session, url_for)
from PIL import Image, ImageOps

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CONTEUDO = RAIZ / "conteudo.json"
IMAGENS = RAIZ / "img" / "novidades"
CONFIG = pathlib.Path(__file__).resolve().parent / "config.json"

EXT_OK = {".jpg", ".jpeg", ".png", ".webp"}
TAM_MAX = 8 * 1024 * 1024          # 8 MB por imagem
TENTATIVAS_MAX = 5                 # por janela
JANELA = 15 * 60                   # 15 minutos

app = Flask(__name__)
app.config.update(
    MAX_CONTENT_LENGTH=TAM_MAX,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    # Vire para True assim que o painel estiver atras de HTTPS.
    SESSION_COOKIE_SECURE=os.environ.get("PAINEL_HTTPS", "") == "1",
    PERMANENT_SESSION_LIFETIME=8 * 3600,
)

_tentativas = {}                   # ip -> [timestamps]


# ---------------------------------------------------------------- config ---

def cfg_ler():
    if not CONFIG.exists():
        return None
    with open(CONFIG, encoding="utf-8") as f:
        return json.load(f)


def cfg_gravar(d):
    CONFIG.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    os.chmod(CONFIG, 0o600)


def hash_senha(senha, sal=None):
    sal = sal or secrets.token_hex(16)
    h = hashlib.scrypt(senha.encode("utf-8"), salt=sal.encode("utf-8"),
                       n=2 ** 14, r=8, p=1, dklen=32)
    return sal, h.hex()


def senha_confere(senha, sal, esperado):
    _, obtido = hash_senha(senha, sal)
    return hmac.compare_digest(obtido, esperado)


# ------------------------------------------------------------- conteudo ---

def conteudo_ler():
    if not CONTEUDO.exists():
        return {"novidades": [], "artigos": []}
    with open(CONTEUDO, encoding="utf-8") as f:
        d = json.load(f)
    d.setdefault("novidades", [])
    d.setdefault("artigos", [])
    return d


def conteudo_gravar(d):
    """Grava em arquivo temporario e troca — se faltar energia no meio,
    o conteudo.json antigo continua inteiro em vez de virar lixo."""
    tmp = CONTEUDO.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(CONTEUDO)


def slug(txt):
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode()
    txt = re.sub(r"[^a-zA-Z0-9]+", "-", txt).strip("-").lower()
    return (txt or "item")[:60]


def id_livre(base, existentes):
    s, n = base, 2
    while s in existentes:
        s, n = f"{base}-{n}", n + 1
    return s


def situacao(item):
    hoje = date.today().isoformat()
    ini = (item.get("inicio") or "").strip()
    fim = (item.get("fim") or "").strip()
    if ini and hoje < ini:
        return ("agendada", "Agendada")
    if fim and hoje > fim:
        return ("expirada", "Fora do ar")
    return ("no-ar", "No ar")


def paginas_do_site():
    """Lista as paginas do site, para o painel oferecer no seletor de link.

    Assim ninguem precisa decorar caminho de arquivo — e ninguem digita
    errado e publica um card que leva a lugar nenhum.
    """
    nomes = {
        "index.html": "Home",
        "quem-somos.html": "Quem somos",
        "contato.html": "Contato",
        "suporte.html": "Suporte",
        "novidades.html": "Novidades",
        "privacidade.html": "Política de Privacidade",
        "consulta-disponibilidade.html": "Consulta de disponibilidade (CEP)",
        "calculadora-custo-downtime.html": "Calculadora de custo de downtime",
        "blog/index.html": "Blog",
        "solucoes/link-dedicado-empresarial.html": "Solução · Link dedicado",
        "solucoes/link-box-redundancia.html": "Solução · Link.Box",
        "solucoes/pabx-virtual-nuvem.html": "Solução · PABX virtual com IA",
        "solucoes/firewall-sd-wan.html": "Solução · Firewall e SD-WAN",
        "solucoes/infraestrutura-ti.html": "Solução · Infraestrutura e projetos",
    }
    achadas = [(c, n) for c, n in nomes.items() if (RAIZ / c).is_file()]

    # Artigos do blog entram sozinhos conforme forem criados
    blog = RAIZ / "blog"
    if blog.is_dir():
        for arq in sorted(blog.glob("*.html")):
            if arq.name == "index.html":
                continue
            achadas.append((f"blog/{arq.name}", f"Artigo · {arq.stem.replace('-', ' ')}"))
    return achadas


def link_valido(link):
    """Aceita http(s) ou caminho de uma pagina que existe. Rejeita o resto."""
    link = (link or "").strip()
    if not link:
        return True, ""
    baixo = link.lower()
    if baixo.startswith(("http://", "https://")):
        return True, ""
    # Esquema esquisito, caminho absoluto ou subida de pasta: fora.
    if ":" in link.split("/")[0] or link.startswith(("/", "..")):
        return False, "Use uma página do site (pelo seletor) ou um endereço começando com https://"
    alvo = (RAIZ / link.split("#")[0].split("?")[0])
    if alvo.is_file():
        return True, ""
    return False, f"A página “{link}” não existe no site. Escolha uma da lista."


# --------------------------------------------------------------- imagem ---

def salvar_imagem(arquivo, nome_base):
    """Reprocessa a imagem pelo Pillow antes de gravar.

    Isso nao e firula: reabrir e reescrever o arquivo descarta qualquer
    coisa escondida dentro dele. O que chega ao disco e uma imagem nova,
    gerada aqui, nao o arquivo que o navegador mandou.
    """
    ext = pathlib.Path(arquivo.filename or "").suffix.lower()
    if ext not in EXT_OK:
        raise ValueError("Formato não aceito. Use JPG, PNG ou WebP.")

    try:
        im = Image.open(arquivo.stream)
        im.verify()                     # detecta arquivo corrompido ou falso
        arquivo.stream.seek(0)
        im = Image.open(arquivo.stream)
        im = ImageOps.exif_transpose(im).convert("RGB")
    except Exception:
        raise ValueError("Não consegui ler essa imagem. Tente outro arquivo.")

    # Recorte 16/9, que e a proporcao do card
    alvo, (w, h) = 16 / 9, im.size
    if w / h > alvo:
        nw = int(h * alvo)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    elif w / h < alvo:
        nh = int(w / alvo)
        y = int((h - nh) * 0.4)
        im = im.crop((0, y, w, y + nh))

    IMAGENS.mkdir(parents=True, exist_ok=True)
    nome = slug(nome_base) + "-" + secrets.token_hex(3)
    for larg in (1400, 800):
        r = im.resize((larg, round(im.height * larg / im.width)), Image.LANCZOS)
        sufixo = "" if larg == 1400 else f"-{larg}"
        r.save(IMAGENS / f"{nome}{sufixo}.jpg", quality=85, optimize=True, progressive=True)
        r.save(IMAGENS / f"{nome}{sufixo}.webp", quality=83, method=6)
    return f"img/novidades/{nome}.jpg"


def apagar_imagem(caminho):
    if not caminho or not caminho.startswith("img/novidades/"):
        return                          # nunca toca em imagem fora dessa pasta
    base = (RAIZ / caminho).with_suffix("")
    for sufixo in ("", "-800"):
        for ext in (".jpg", ".webp"):
            alvo = pathlib.Path(str(base) + sufixo + ext)
            try:
                if alvo.is_file() and IMAGENS in alvo.parents:
                    alvo.unlink()
            except OSError:
                pass


# ----------------------------------------------------------------- build ---

def rodar_build():
    try:
        p = subprocess.run([sys.executable, "build.py"], cwd=RAIZ,
                           capture_output=True, text=True, timeout=120)
        return p.returncode == 0, (p.stdout + p.stderr)[-1500:]
    except subprocess.TimeoutExpired:
        return False, "O build passou de 2 minutos e foi interrompido."
    except Exception as e:
        return False, str(e)


# ------------------------------------------------------------ seguranca ---

def logado():
    return session.get("ok") is True


def exige_login():
    if not logado():
        return redirect(url_for("login", proxima=request.path))
    return None


def csrf_token():
    if "csrf" not in session:
        session["csrf"] = secrets.token_urlsafe(32)
    return session["csrf"]


def csrf_ok():
    enviado = request.form.get("csrf", "")
    return bool(session.get("csrf")) and hmac.compare_digest(enviado, session["csrf"])


def bloqueado(ip):
    agora = time.time()
    _tentativas[ip] = [t for t in _tentativas.get(ip, []) if agora - t < JANELA]
    return len(_tentativas[ip]) >= TENTATIVAS_MAX


app.jinja_env.globals["csrf_token"] = csrf_token


# ------------------------------------------------------------------ rotas ---

@app.route("/")
def raiz():
    return site_estatico("index.html")


@app.route("/admin/login", methods=["GET", "POST"])
def login():
    c = cfg_ler()
    if not c:
        return render_template("login.html", sem_config=True)

    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "?").split(",")[0].strip()

    if request.method == "POST":
        if bloqueado(ip):
            flash("Muitas tentativas. Espere 15 minutos.", "erro")
            return render_template("login.html")
        if not csrf_ok():
            flash("Sessão expirada. Tente de novo.", "erro")
            return render_template("login.html")

        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")
        if (hmac.compare_digest(usuario, c["usuario"])
                and senha_confere(senha, c["sal"], c["hash"])):
            session.clear()
            session["ok"] = True
            session["usuario"] = usuario
            session.permanent = True
            _tentativas.pop(ip, None)
            destino = request.args.get("proxima") or url_for("lista")
            return redirect(destino if destino.startswith("/admin") else url_for("lista"))

        _tentativas.setdefault(ip, []).append(time.time())
        restam = TENTATIVAS_MAX - len(_tentativas[ip])
        flash(f"Usuário ou senha incorretos. {max(restam, 0)} tentativa(s) restante(s).", "erro")

    return render_template("login.html")


@app.route("/admin/sair")
def sair():
    session.clear()
    return redirect(url_for("login"))


@app.route("/admin")
@app.route("/admin/novidades")
def lista():
    r = exige_login()
    if r:
        return r
    itens = conteudo_ler()["novidades"]
    itens = sorted(itens, key=lambda n: n.get("inicio") or "", reverse=True)
    for i in itens:
        i["_estado"], i["_rotulo"] = situacao(i)
    return render_template("lista.html", itens=itens, hoje=date.today().isoformat())


@app.route("/admin/novidade/nova", methods=["GET", "POST"])
@app.route("/admin/novidade/<item_id>", methods=["GET", "POST"])
def editar(item_id=None):
    r = exige_login()
    if r:
        return r

    dados = conteudo_ler()
    item = next((n for n in dados["novidades"] if n["id"] == item_id), None)
    if item_id and item is None:
        abort(404)

    if request.method == "POST":
        if not csrf_ok():
            flash("Sessão expirada. Faça login de novo.", "erro")
            return redirect(url_for("login"))

        titulo = request.form.get("titulo", "").strip()
        resumo = request.form.get("resumo", "").strip()
        inicio = request.form.get("inicio", "").strip()
        fim = request.form.get("fim", "").strip()

        erros = []
        if not titulo:
            erros.append("O título é obrigatório.")
        if not resumo:
            erros.append("O resumo é obrigatório — é o que aparece no card.")
        if not inicio:
            erros.append("Informe a partir de quando a novidade entra no ar.")
        if inicio and fim and fim < inicio:
            erros.append("A data final não pode ser anterior à inicial.")

        link = request.form.get("link", "").strip()
        ok_link, erro_link = link_valido(link)
        if not ok_link:
            erros.append(erro_link)

        novo = dict(item) if item else {}
        arquivo = request.files.get("imagem")
        if arquivo and arquivo.filename:
            try:
                caminho = salvar_imagem(arquivo, titulo or "novidade")
                if item and item.get("imagem") != caminho:
                    apagar_imagem(item.get("imagem"))
                novo["imagem"] = caminho
            except ValueError as e:
                erros.append(str(e))
        elif not item:
            erros.append("Escolha uma imagem para o card.")

        if erros:
            for e in erros:
                flash(e, "erro")
            novo.update(titulo=titulo, resumo=resumo, inicio=inicio, fim=fim,
                        etiqueta=request.form.get("etiqueta", "").strip(),
                        link=request.form.get("link", "").strip(),
                        link_texto=request.form.get("link_texto", "").strip())
            return render_template("form.html", item=novo, novo=item is None,
                                   paginas=paginas_do_site())

        novo.update(
            titulo=titulo, resumo=resumo, inicio=inicio, fim=fim,
            etiqueta=request.form.get("etiqueta", "").strip() or "Novidade",
            link=request.form.get("link", "").strip(),
            link_texto=request.form.get("link_texto", "").strip() or "Saber mais",
        )

        if item:
            dados["novidades"] = [novo if n["id"] == item_id else n
                                  for n in dados["novidades"]]
            msg = "Novidade atualizada."
        else:
            existentes = {n["id"] for n in dados["novidades"]}
            novo["id"] = id_livre(slug(titulo), existentes)
            novo["criada_em"] = datetime.now().isoformat(timespec="seconds")
            dados["novidades"].append(novo)
            msg = "Novidade criada."

        conteudo_gravar(dados)
        ok, saida = rodar_build()
        flash(msg + (" Site atualizado." if ok else " Mas o build falhou — veja o log."),
              "ok" if ok else "erro")
        if not ok:
            flash(saida, "erro")
        return redirect(url_for("lista"))

    vazio = {"etiqueta": "Novidade", "inicio": date.today().isoformat(),
             "link_texto": "Saber mais"}
    return render_template("form.html", item=item or vazio, novo=item is None,
                           paginas=paginas_do_site())


@app.route("/admin/novidade/<item_id>/remover", methods=["POST"])
def remover(item_id):
    r = exige_login()
    if r:
        return r
    if not csrf_ok():
        abort(400)

    dados = conteudo_ler()
    item = next((n for n in dados["novidades"] if n["id"] == item_id), None)
    if item is None:
        abort(404)

    dados["novidades"] = [n for n in dados["novidades"] if n["id"] != item_id]
    conteudo_gravar(dados)
    apagar_imagem(item.get("imagem"))
    ok, saida = rodar_build()
    flash("Novidade removida." + (" Site atualizado." if ok else " Mas o build falhou."),
          "ok" if ok else "erro")
    return redirect(url_for("lista"))


@app.route("/admin/publicar", methods=["POST"])
def publicar():
    r = exige_login()
    if r:
        return r
    if not csrf_ok():
        abort(400)
    ok, saida = rodar_build()
    flash("Site regerado." if ok else "O build falhou.", "ok" if ok else "erro")
    if not ok:
        flash(saida, "erro")
    return redirect(url_for("lista"))


@app.route("/<path:caminho>")
def site_estatico(caminho):
    """Serve o site estatico quando o painel roda sozinho.

    Em producao quem entrega estes arquivos e o nginx, muito mais rapido —
    esta rota existe para o painel funcionar tambem sem nginx na frente,
    em teste ou na rede interna. Ela so devolve arquivos de dentro da raiz
    do projeto e nunca entra em pastas do painel.
    """
    alvo = (RAIZ / caminho).resolve()
    try:
        alvo.relative_to(RAIZ)
    except ValueError:
        abort(404)                       # tentativa de sair da pasta
    proibidas = {"painel", ".git", "__pycache__"}
    if proibidas & set(alvo.relative_to(RAIZ).parts):
        abort(404)
    if alvo.is_dir():
        alvo = alvo / "index.html"
    if not alvo.is_file() or alvo.suffix in {".py", ".json", ".tmp"}:
        abort(404)
    return send_from_directory(RAIZ, str(alvo.relative_to(RAIZ)))


@app.errorhandler(413)
def grande_demais(_):
    flash("Imagem acima de 8 MB. Reduza o arquivo e tente de novo.", "erro")
    return redirect(url_for("lista"))


# ------------------------------------------------------------- inicializa ---

def main():
    c = cfg_ler()
    if not c:
        print("\nPrimeiro acesso: nenhuma senha cadastrada.")
        print("Rode:  python3 painel/criar-senha.py\n")
        sys.exit(1)
    app.secret_key = c["segredo"]
    porta = int(os.environ.get("PAINEL_PORTA", "8090"))
    # 127.0.0.1 de proposito: quem fala com a internet e o nginx, nao o Flask.
    app.run(host=os.environ.get("PAINEL_HOST", "127.0.0.1"), port=porta)


if __name__ == "__main__":
    main()
else:
    _c = cfg_ler()
    if _c:
        app.secret_key = _c["segredo"]
