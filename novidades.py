#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Area de novidades.

O conteudo vem de conteudo.json, escrito pelo painel em /admin.
Cada item tem um periodo de exibicao: aparece a partir de 'inicio' e sai
depois de 'fim'. Quem decide e o build — mas o navegador tambem confere,
porque entre um build e outro uma data pode virar.
"""

import json
import pathlib
from datetime import date

RAIZ = pathlib.Path(__file__).parent


def carregar():
    arq = RAIZ / "conteudo.json"
    if not arq.exists():
        return {"novidades": [], "artigos": []}
    with open(arq, encoding="utf-8") as f:
        d = json.load(f)
    d.setdefault("novidades", [])
    d.setdefault("artigos", [])
    return d


def no_ar(item, hoje=None):
    """True se o item deve aparecer hoje."""
    hoje = hoje or date.today().isoformat()
    ini = (item.get("inicio") or "").strip()
    fim = (item.get("fim") or "").strip()
    if ini and hoje < ini:
        return False
    if fim and hoje > fim:
        return False
    return True


def ativas(hoje=None):
    itens = [n for n in carregar()["novidades"] if no_ar(n, hoje)]
    # Mais recentes primeiro, pelo inicio da exibicao
    return sorted(itens, key=lambda n: n.get("inicio") or "", reverse=True)


def _fmt(d):
    if not d:
        return ""
    m = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]
    try:
        a, mm, dd = d.split("-")
        return f"{int(dd)} de {m[int(mm) - 1]} de {a}"
    except (ValueError, IndexError):
        return d


def _capa(item, prefix):
    img = (item.get("imagem") or "").strip()
    if not img:
        return ""
    base = img.rsplit(".", 1)[0]
    return f"""<div class="nov__capa">
        <picture>
          <source type="image/webp" srcset="{prefix}{base}-800.webp 800w, {prefix}{base}.webp 1400w" sizes="(max-width:900px) 100vw, 46vw">
          <img src="{prefix}{img}" alt="{item.get('titulo','')}" loading="lazy" decoding="async"
               style="aspect-ratio:16/9;object-fit:cover;width:100%">
        </picture>
      </div>"""


def card(item, prefix=""):
    etiqueta = (item.get("etiqueta") or "Novidade").strip()
    link = (item.get("link") or "").strip()
    link_txt = (item.get("link_texto") or "Saber mais").strip()
    fim = (item.get("fim") or "").strip()

    acao = ""
    if link:
        destino = link if link.startswith("http") else prefix + link
        externo = ' target="_blank" rel="noopener"' if link.startswith("http") else ""
        acao = (f'<a class="nov__cta" href="{destino}"{externo} '
                f'data-label="{link_txt}">{link_txt} '
                f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                f'<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>')

    ate = f'<span class="nov__ate">Até {_fmt(fim)}</span>' if fim else ""

    return f"""
      <article class="nov__card reveal" data-nov data-inicio="{item.get('inicio','')}" data-fim="{fim}">
        {_capa(item, prefix)}
        <div class="nov__corpo">
          <div class="nov__meta">
            <span class="nov__tag">{etiqueta}</span>
            <span class="nov__data">{_fmt(item.get('inicio'))}</span>
            {ate}
          </div>
          <h3>{item.get('titulo','')}</h3>
          <p>{item.get('resumo','')}</p>
          {acao}
        </div>
      </article>"""


def faixa_home(prefix="", limite=2):
    """Faixa curta na home. Some sozinha quando nao ha nada no ar."""
    itens = ativas()[:limite]
    if not itens:
        return ""
    cards = "".join(card(i, prefix) for i in itens)
    return f"""
<section class="section section--alt sec-tex" id="novidades" data-nov-secao>
  <div class="wrap">
    <div class="nov__head reveal">
      <div>
        <span class="eyebrow">Novidades</span>
        <h2 class="display">O que há de novo na Wicorp</h2>
      </div>
      <a href="{prefix}novidades.html" class="btn btn--ghost btn--sm">Ver todas as novidades</a>
    </div>
    <div class="nov">{cards}
    </div>
  </div>
</section>"""


def pagina(prefix=""):
    itens = ativas()
    if itens:
        corpo = f'<div class="nov">{"".join(card(i, prefix) for i in itens)}\n    </div>'
    else:
        corpo = """
    <div class="callout" style="text-align:center">
      <h3>Nada por aqui no momento</h3>
      <p>Quando houver lançamento, evento ou aviso, ele aparece nesta página.
      Enquanto isso, o blog tem conteúdo técnico sobre conectividade, telefonia e segurança.</p>
      <p style="margin-top:18px">
        <a href="blog/index.html" class="btn btn--primary" data-label="Ir para o blog">Ir para o blog</a>
      </p>
    </div>"""

    return f"""
<main id="main">
<section class="page-hero" style="padding-bottom:44px">
  <div class="wrap">
    <span class="eyebrow">Novidades</span>
    <h1 class="display">O que há de novo <span class="grad-text">na Wicorp</span></h1>
    <p class="lead">
      Lançamentos, avisos de operação e novidades das soluções. O que está
      valendo agora, sem conteúdo velho ocupando espaço.
    </p>
  </div>
</section>

<section class="section" style="padding-top:0" data-nov-secao>
  <div class="wrap">{corpo}
  </div>
</section>
</main>"""
