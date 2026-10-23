"""Exporta docs/informe_final.md a PDF.

Dos modos:
  --revision  (por defecto) antepone docs/revision_informe_pendientes.md y
              resalta en amarillo los huecos ([PENDIENTE], [completar], ...).
  --final     quita las notas internas (estado del borrador, recuadro "Cómo se
              usa", líneas "Fuente/Tarea" y la guía de estilo) para la entrega.

Convierte Markdown -> HTML con la librería `markdown` e imprime a PDF con
Microsoft Edge (o Chrome) en modo headless, así no hace falta LaTeX ni pandoc.

Uso:
    python scripts/exportar_informe_pdf.py --revision
    python scripts/exportar_informe_pdf.py --final --salida docs/<equipo>_track2_report.pdf
"""
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent
INFORME = RAIZ / "docs" / "informe_final.md"
PENDIENTES = RAIZ / "docs" / "revision_informe_pendientes.md"

NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "msedge", "google-chrome", "chromium", "chrome",
]

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: Arial, "DejaVu Sans", sans-serif; font-size: 10pt; line-height: 1.4; color: #111; }
h1 { font-size: 17pt; margin: 0 0 6pt; }
h2 { font-size: 13.5pt; margin: 16pt 0 6pt; border-bottom: 1px solid #999; padding-bottom: 2pt; }
h3 { font-size: 11.5pt; margin: 12pt 0 4pt; }
h4 { font-size: 10.5pt; margin: 10pt 0 4pt; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 8.5pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #bbb; padding: 3pt 4pt; vertical-align: top; text-align: left; }
th { background: #eee; }
img { max-width: 100%; display: block; margin: 6pt auto; page-break-inside: avoid; }
code { font-family: Consolas, monospace; font-size: 8.5pt; background: #f3f3f3; padding: 0 2pt; }
pre { background: #f3f3f3; padding: 6pt; }
blockquote { border-left: 3px solid #bbb; margin: 6pt 0; padding: 2pt 8pt; color: #333; }
mark { background: #ffe94d; padding: 0 2pt; }
.pendientes { page-break-after: always; }
"""

# Formato IEEE a doble columna (--ieee): carta, Times 10 pt, secciones en versalitas.
# Título, autores y resumen van a una columna; figuras y tablas anchas ocupan las dos.
CSS_IEEE = """
@page { size: letter; margin: 0.75in 0.625in 0.9in 0.625in; }
body { font-family: "Times New Roman", Times, serif; font-size: 10pt; line-height: 1.18; color: #000; }
h1 { font-size: 22pt; font-weight: normal; text-align: center; line-height: 1.15; margin: 0 0 8pt; }
h1 + p { text-align: center; font-size: 10pt; margin-bottom: 10pt; }
hr { display: none; }
.cabecera p { font-size: 9pt; text-align: justify; margin: 0 0 6pt; }
.cabecera h1 + p { font-size: 11pt; text-align: center; margin-bottom: 3pt; }
.cabecera h1 + p + p { text-align: center; margin-bottom: 10pt; }
.cols { column-count: 2; column-gap: 0.25in; text-align: justify; hyphens: auto; }
.cols p { margin: 0 0 5pt; text-indent: 0; }
h2 { font-size: 10pt; font-weight: normal; font-variant: small-caps; text-align: center; letter-spacing: 0.3pt;
     margin: 10pt 0 5pt; break-after: avoid; }
h3 { font-size: 10pt; font-weight: normal; font-style: italic; margin: 8pt 0 3pt; break-after: avoid; }
ul, ol { margin: 0 0 5pt; padding-left: 14pt; }
li { margin-bottom: 2pt; }
table { border-collapse: collapse; width: 100%; font-size: 7.5pt; margin: 3pt 0 8pt; text-align: left; }
th, td { border-top: 0.5pt solid #000; border-bottom: 0.5pt solid #000; padding: 2pt 3pt; vertical-align: top; }
th { font-weight: bold; }
tr { break-inside: avoid; }
img { max-width: 100%; display: block; margin: 4pt auto; }
code { font-family: Consolas, "Courier New", monospace; font-size: 7.5pt; }
.cols code { word-break: break-all; }
mark { background: #ffe94d; }
.figura { margin: 4pt 0 8pt; break-inside: avoid; }
.figura img { width: 100%; margin: 0 0 3pt; }
.figura p { font-size: 8pt; text-align: justify; }
.tabla { margin: 4pt 0 8pt; }
.tabla table { font-size: 6.5pt; line-height: 1.12; }
.tabla th, .tabla td { padding: 1.5pt 2pt; }
p.titulo-tabla { font-size: 8pt; text-align: center; font-variant: small-caps; margin: 6pt 0 2pt; break-after: avoid; }
p.pie { font-size: 8pt; }
.refs p { font-size: 8pt; text-align: left; margin-bottom: 3pt; }
"""


def maquetar_ieee(cuerpo: str) -> str:
    """Separa la cabecera (título, autores, resumen) de las dos columnas.

    Figuras y tablas van dentro de la columna, como en IEEE; las figuras de columna se
    dibujan a 3,5 pulgadas con scripts/figuras_columna_en.py para que el texto se lea.
    """
    corte = cuerpo.find("<h2")
    cabecera, resto = cuerpo[:corte], cuerpo[corte:]
    resto = re.sub(r'(<p><img [^>]*></p>\s*<p><strong>Fig\. \d+\.</strong>.*?</p>)',
                   r'<div class="figura">\1</div>', resto, flags=re.S)

    def tabla(m):
        titulo, tabla_html = m.group(1), m.group(2)
        titulo = titulo.replace("<p>", '<p class="titulo-tabla">', 1)
        return f'<div class="tabla">{titulo}{tabla_html}</div>'

    resto = re.sub(r'(<p><strong>TABLE [IVX]+\..*?</p>)\s*(<table>.*?</table>)', tabla, resto, flags=re.S)
    i = resto.find("<h2>References</h2>")
    if i != -1:
        resto = resto[:i] + '<h2>References</h2><div class="refs">' + resto[i + len("<h2>References</h2>"):] + "</div>"
    return f'<div class="cabecera">{cabecera}</div><div class="cols">{resto}</div>'


# Huecos a resaltar en modo revisión.
HUECOS = re.compile(r"\[(?:PENDIENTE[^\]]*|completar|nombre|otra|DECISIÓN[^\]]*|TO (?:COMPLETE|CONFIRM|REPLACE)[^\]]*|surname)\]")


def limpiar_para_entrega(md: str) -> str:
    """Quita las notas internas del borrador."""
    md = md.split("\n## Guía de estilo")[0]
    salida = []
    for linea in md.splitlines():
        if linea.startswith("**Estado:"):
            continue
        if linea.startswith("> **Cómo se usa este archivo"):
            continue
        if re.match(r"^\*(Fuente|Tareas?):", linea):
            continue
        salida.append(linea)
    return "\n".join(salida).rstrip().rstrip("-").rstrip() + "\n"


def a_html(md: str) -> str:
    return markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])


def buscar_navegador() -> str:
    for n in NAVEGADORES:
        ruta = shutil.which(n) or (n if Path(n).exists() else None)
        if ruta:
            return ruta
    sys.exit("No encontré Edge ni Chrome para imprimir el PDF.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    modo = ap.add_mutually_exclusive_group()
    modo.add_argument("--revision", action="store_true", help="PDF con la hoja de pendientes y huecos resaltados (por defecto)")
    modo.add_argument("--final", action="store_true", help="PDF de entrega, sin notas internas")
    ap.add_argument("--salida", type=Path, help="ruta del PDF")
    ap.add_argument("--entrada", type=Path, default=INFORME, help="Markdown a exportar (por defecto docs/informe_final.md)")
    ap.add_argument("--ieee", action="store_true", help="formato IEEE a doble columna (carta, Times)")
    args = ap.parse_args()

    md = args.entrada.read_text(encoding="utf-8")
    if args.final:
        cuerpo = a_html(limpiar_para_entrega(md))
        salida = args.salida or RAIZ / "docs" / "informe_final.pdf"
    else:
        cuerpo = a_html(md)
        cuerpo = HUECOS.sub(lambda m: f"<mark>{m.group(0)}</mark>", cuerpo)
        if PENDIENTES.exists() and args.entrada.resolve() == INFORME:
            hoja = a_html(PENDIENTES.read_text(encoding="utf-8"))
            cuerpo = f'<div class="pendientes">{hoja}</div>' + cuerpo
        salida = args.salida or RAIZ / "docs" / "informe_final_revision.pdf"

    estilo = CSS
    if args.ieee:
        cuerpo = maquetar_ieee(cuerpo)
        estilo = CSS_IEEE
    idioma = "en" if args.entrada.stem.endswith("_en") else "es"
    # Las imágenes se referencian como ../results/...; se resuelven desde docs/.
    base = (RAIZ / "docs").as_uri() + "/"
    html = (f'<!doctype html><html lang="{idioma}"><head><meta charset="utf-8"><base href="{base}">'
            f"<style>{estilo}</style></head><body>{cuerpo}</body></html>")

    with tempfile.TemporaryDirectory() as tmp:
        ruta_html = Path(tmp) / "informe.html"
        ruta_html.write_text(html, encoding="utf-8")
        salida = salida.resolve()
        antes = salida.stat().st_mtime if salida.exists() else None
        # Perfil propio: si el navegador ya está abierto, sin esto la orden se entrega a esa ventana
        # y el PDF no se escribe.
        subprocess.run([buscar_navegador(), "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--user-data-dir={Path(tmp) / 'perfil'}", f"--print-to-pdf={salida}", ruta_html.as_uri()],
                       check=True, capture_output=True)
        # Edge puede devolver el control antes de escribir el PDF: se espera dentro del bloque
        # para que el HTML temporal siga existiendo mientras lo lee.
        listo = lambda: salida.exists() and salida.stat().st_mtime != antes and salida.stat().st_size > 0
        for _ in range(120):
            if listo():
                time.sleep(1)  # que termine de escribir
                break
            time.sleep(0.5)
    if not listo():
        sys.exit(f"El navegador no escribió el PDF: {salida}")
    print(f"PDF generado: {salida}")


if __name__ == "__main__":
    main()
