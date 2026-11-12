"""Genera office-work.html, la versión para jugar en local, a partir de index.html.

index.html es la fuente: es lo que se publica como artefacto y por eso no lleva <!doctype>,
<html>, <head> ni <body> (los pone la plataforma al publicar). Para abrirlo con doble clic
en el navegador hace falta un documento completo; este script lo envuelve.

Uso (desde la carpeta prototipo/):  python3 -I scripts/empaquetar.py
"""
from pathlib import Path

base = Path(__file__).resolve().parent.parent
fuente = (base / "index.html").read_text(encoding="utf-8")
cabecera = (
    "<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "</head>\n<body>\n"
    "<!-- Archivo generado con scripts/empaquetar.py a partir de index.html. No editar a mano. -->\n"
)
(base / "office-work.html").write_text(cabecera + fuente + "\n</body>\n</html>\n", encoding="utf-8")
print("office-work.html generado")
