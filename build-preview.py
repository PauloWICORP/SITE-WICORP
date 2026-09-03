#!/usr/bin/env python3
"""Gera um HTML unico com CSS e JS embutidos, para visualizacao rapida."""
import re, pathlib, sys

root = pathlib.Path(__file__).parent
src  = root / (sys.argv[1] if len(sys.argv) > 1 else "index.html")
out  = root / (sys.argv[2] if len(sys.argv) > 2 else "preview.html")

html = src.read_text(encoding="utf-8")
css  = (root / "css/style.css").read_text(encoding="utf-8")
js   = (root / "js/main.js").read_text(encoding="utf-8")

html = re.sub(r'<link rel="stylesheet" href="[^"]*style\.css">',
              lambda _: "<style>\n" + css + "\n</style>", html)
html = re.sub(r'<script src="[^"]*main\.js"></script>',
              lambda _: "<script>\n" + js + "\n</script>", html)

out.write_text(html, encoding="utf-8")
print("OK -> %s (%s bytes)" % (out.name, format(len(html), ",")))
