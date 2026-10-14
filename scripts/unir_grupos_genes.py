"""Unifica los CSV de grupos de genes del equipo en una tabla corregida y amplia genes_candidatos.txt.

Entrada:  config/grupos_genes/originales/*.csv  (tal como los mando el equipo, sin tocar)
Salida:   config/genes_candidatos_anotados.csv  (una fila por gen, sin las columnas de IDs)
          config/genes_candidatos.txt           (bloque entre marcas AUTO; el resto no se toca)

Que se corrige:
  - Se descartan hgnc_id, ensembl_id y ncbi_gene_id: en 7 de los 8 archivos repiten el mismo valor
    en muchas filas (p. ej. ENSG00000162571 en 72 de 95 filas) y no se pueden verificar sin red.
    En el archivo de reparacion de ADN las columnas estan corridas (le faltan 2 columnas).
    Las coordenadas se obtienen por simbolo con scripts/resolve_genes.py.
  - Se agrega la columna nota_revision con errores de contenido detectados (ver NOTAS).
    El texto original de funcion y enfermedad no se modifica.

Uso:  python scripts/unir_grupos_genes.py
"""
import csv
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "config" / "grupos_genes" / "originales"
SALIDA_CSV = RAIZ / "config" / "genes_candidatos_anotados.csv"
LISTA = RAIZ / "config" / "genes_candidatos.txt"
INI, FIN = "# >>> AUTO: grupos del equipo (scripts/unir_grupos_genes.py) >>>", "# <<< AUTO <<<"

COLUMNAS = ["gen", "nombre_completo", "tipo_locus", "cromosoma_banda", "funcion_principal",
            "enfermedades_asociadas"]

# Simbolo del archivo -> simbolo vigente (HGNC). MyGene tambien resuelve alias, pero asi queda explicito.
SIMBOLO_ACTUAL = {"SAS6": "SASS6", "CCDC155": "KASH5", "H3F3A": "H3-3A", "H3F3B": "H3-3B",
                  "H2AFZ": "H2AZ1", "MRE11A": "MRE11", "NTF2": "NUTF2", "NUP53": "NUP35",
                  "NUP96": "NUP98"}

# Revisiones a mano. Son advertencias, no sustituyen el texto original: verificar antes de citar.
NOTAS = {
    "MAD2L1BP": "MVA descrito en 2023 (ver seccion 5 de docs/secciones/01_variante_causante.md); verificar la parte de fallo ovarico.",
    "TRIP13": "Verificado 14 oct: el archivo esta bien, MVA 3 es TRIP13 (OMIM 617598, bialelico, con tumor de Wilms). CENATAC es MVA 4 (OMIM 620153).",
    "SAS6": "Simbolo vigente SASS6. 'Formacion del cartilago del centriolo' es un error: es la rueda de carro (cartwheel).",
    "PCNT": "Taybi-Linder corresponde a RNU4ATAC, no a PCNT; PCNT: MOPD II y Seckel tipo 4.",
    "NIN": "'Displasia seudoacondroplasica' corresponde a COMP; NIN se asocia a un cuadro tipo Seckel. Verificar.",
    "CCDC155": "Simbolo vigente KASH5.",
    "H3F3A": "Simbolo vigente H3-3A.", "H3F3B": "Simbolo vigente H3-3B.", "H2AFZ": "Simbolo vigente H2AZ1.",
    "MRE11A": "Simbolo vigente MRE11.", "NTF2": "Simbolo vigente NUTF2.", "NUP53": "Simbolo vigente NUP35.",
    "NUP96": "No es un gen aparte: NUP96 es un producto de NUP98 (se usa NUP98).",
    "NUP133": "La columna de enfermedades puede estar incompleta (sindrome nefrotico/Galloway-Mowat); verificar.",
    "NUP85": "La columna de enfermedades puede estar incompleta (sindrome nefrotico/Galloway-Mowat); verificar.",
    "NUP160": "La columna de enfermedades puede estar incompleta (sindrome nefrotico); verificar.",
    "HGS": "No es del ciclo celular (trafico endosomal); baja prioridad para MVA.",
    "ARRB1": "No es del ciclo celular (senalizacion GPCR); baja prioridad para MVA.",
    "ARRB2": "No es del ciclo celular (senalizacion GPCR); baja prioridad para MVA.",
}
GENERICA = "La columna de enfermedades es generica en genes sin enfermedad mendeliana: no sirve como evidencia."


def leer(ruta):
    """Lee un CSV del equipo. El archivo de reparacion de ADN trae 7 columnas (sin los 3 IDs reales)."""
    with open(ruta, encoding="utf-8", newline="") as f:
        filas = list(csv.reader(f))[1:]
    return [dict(zip(COLUMNAS, r[:6])) for r in filas if r and r[0].strip()]


def main():
    registros, vistos = [], {}
    for ruta in sorted(ENTRADA.glob("*.csv")):
        grupo = re.sub(r"^(grupo\w+?)_.*", r"\1", ruta.stem)
        for r in leer(ruta):
            if r["gen"] in vistos:
                print(f"  duplicado omitido: {r['gen']} ({grupo}, ya en {vistos[r['gen']]})")
                continue
            vistos[r["gen"]] = grupo
            nota = NOTAS.get(r["gen"], "")
            if not nota and r["enfermedades_asociadas"].startswith("Sin enfermedad"):
                nota = GENERICA
            registros.append({"grupo": ruta.stem, "simbolo_actual": SIMBOLO_ACTUAL.get(r["gen"], r["gen"]),
                              **r, "nota_revision": nota})
    campos = ["grupo", "gen", "simbolo_actual"] + COLUMNAS[1:] + ["nota_revision"]
    with open(SALIDA_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(registros)

    texto = LISTA.read_text(encoding="utf-8")
    existentes = {l.split()[0] for l in texto.split(INI)[0].splitlines() if l.strip() and not l.startswith("#")}
    bloque, nuevos = [INI], 0
    for ruta in sorted(ENTRADA.glob("*.csv")):
        genes = [r for r in registros if r["grupo"] == ruta.stem and r["simbolo_actual"] not in existentes]
        genes = list({r["simbolo_actual"]: r for r in genes}.values())
        if not genes:
            continue
        bloque.append(f"# ── {ruta.stem} ({len(genes)} nuevos) ──")
        for r in genes:
            if r["gen"] != r["simbolo_actual"]:
                bloque.append(f"{r['simbolo_actual']}  # en el archivo: {r['gen']}")
            else:
                bloque.append(r["simbolo_actual"])
            nuevos += 1
            existentes.add(r["simbolo_actual"])
    bloque.append(FIN)
    base = re.sub(re.escape(INI) + r".*?" + re.escape(FIN) + r"\n?", "", texto, flags=re.S).rstrip("\n")
    LISTA.write_text(base + "\n" + "\n".join(bloque) + "\n", encoding="utf-8")
    print(f"{len(registros)} genes unicos en {SALIDA_CSV.name}; {nuevos} nuevos en genes_candidatos.txt")


if __name__ == "__main__":
    main()
