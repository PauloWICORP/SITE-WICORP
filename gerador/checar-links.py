#!/usr/bin/env python3
"""Confere se todo link interno do site aponta para um arquivo que existe.

    python gerador/checar-links.py

Lê todos os .html publicados (fora painel/ e docs/), resolve cada href, src
e srcset relativo a partir da pasta da página e lista o que não existe.
Sai com código 1 se achar link quebrado — rode depois de mover ou renomear
qualquer página ou imagem.
"""
import pathlib
import re
import sys
from urllib.parse import unquote

RAIZ = pathlib.Path(__file__).resolve().parent.parent
IGNORAR = ("painel", "docs", ".git", "gerador", ".devcontainer", ".vscode")
EXTERNO = re.compile(r"^(https?:|mailto:|tel:|data:|javascript:|//|#)")


def urls(html):
    for m in re.finditer(r'\b(?:href|src|action|poster)="([^"]*)"', html):
        yield m.group(1)
    for m in re.finditer(r'\bsrcset="([^"]*)"', html):
        for parte in m.group(1).split(","):
            parte = parte.strip()
            if parte:
                yield parte.split()[0]


def main():
    quebrados = 0
    paginas = [p for p in RAIZ.rglob("*.html")
               if not any(x in p.relative_to(RAIZ).parts[:1] for x in IGNORAR)]
    for pg in sorted(paginas):
        html = pg.read_text(encoding="utf-8")
        for u in sorted(set(urls(html))):
            if not u or EXTERNO.match(u) or "{" in u:
                continue
            alvo = unquote(u.split("#")[0].split("?")[0])
            if not alvo:
                continue
            caminho = (RAIZ / alvo.lstrip("/")) if alvo.startswith("/") else (pg.parent / alvo)
            if caminho.is_dir():
                caminho = caminho / "index.html"
            if not caminho.resolve().exists():
                quebrados += 1
                print(f"QUEBRADO  {pg.relative_to(RAIZ).as_posix():45s} -> {u}")
    print(f"\n{len(paginas)} páginas conferidas, {quebrados} link(s) quebrado(s).")
    return 1 if quebrados else 0


if __name__ == "__main__":
    sys.exit(main())
