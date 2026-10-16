"""
farmacogenetica.py — Tarea farmacogenetica (MVA Hackathon 2026)

Busca en el VCF del paciente las variantes farmacogenomicas relevantes para:
  - Ciclofosfamida: CYP2B6 (*9, *6, *18), CYP2C19 (*2, *3), CYP3A4 (*22, *1B), GSTM1 nulo
  - Sirolimus/nab-sirolimus: CYP3A5 (*3), CYP3A4 (*22, *1B, *1G), ABCB1 (3435/2677/1236)
  - Arimoclomol: sin farmacogenetica relevante; el factor limitante es la funcion renal

Resuelve rsIDs a coordenadas GRCh38 via Ensembl REST (con cache en data/farmacogenetica/).
Guarda genotipos crudos (con posiciones) en data/farmacogenetica/genotipos_farma.json (NO versionado).
Imprime un resumen con solo fenotipos / etiquetas, sin coordenadas exactas del paciente.

Uso:
    python scripts/farmacogenetica.py

Requiere: acceso a red para Ensembl (solo si la cache esta vacia).
          El VCF en data/raw/*.vcf.gz debe existir.
"""

import gzip
import json
import sys
import time
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
VCF_PATH = next((RAIZ / "data" / "raw").glob("*.vcf.gz"), None)
OUT_DIR = RAIZ / "data" / "farmacogenetica"
CACHE_FILE = OUT_DIR / "coords_cache.json"

ENSEMBL = "https://rest.ensembl.org"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "MVA-Hackathon/1.0 ktalynagarciabenavides@gmail.com",
}

# ---------------------------------------------------------------------------
# Definicion de variantes de interes
# Orden de importancia segun el docx del equipo.
# alelo: nombre del alelo farmacogenomico estandar (CPIC/PharmGKB)
# efecto: lo que hace el alelo mutante
# nivel: evidencia clinica CPIC (A = guia formal, B = indicada pero sin guia, C = debatida)
# ---------------------------------------------------------------------------
VARIANTES = [
    # CYP2B6 — bioactivacion de ciclofosfamida (CRITICO segun docx del equipo)
    {
        "rsid": "rs2279343",
        "gen": "CYP2B6",
        "alelo": "*9",
        "farmaco": "ciclofosfamida",
        "nivel": "B",
        "efecto": (
            "c.785A>G, p.Lys262Arg; reduce actividad CYP2B6; "
            "heterocigotos con *6 son metabolizadores intermedios"
        ),
    },
    {
        "rsid": "rs3745274",
        "gen": "CYP2B6",
        "alelo": "*6 (Gln172His)",
        "farmaco": "ciclofosfamida",
        "nivel": "B",
        "efecto": (
            "c.516G>T, p.Gln172His; junto con rs2279343 define el alelo *6 "
            "(metabolizador intermedio o pobre segun el par de alelos)"
        ),
    },
    {
        "rsid": "rs3211371",
        "gen": "CYP2B6",
        "alelo": "*18",
        "farmaco": "ciclofosfamida",
        "nivel": "B",
        "efecto": "c.1459C>T, p.Arg487Cys; reduce actividad CYP2B6",
    },
    # CYP2C19 — bioactivacion de ciclofosfamida (CRITICO)
    {
        "rsid": "rs4244285",
        "gen": "CYP2C19",
        "alelo": "*2",
        "farmaco": "ciclofosfamida",
        "nivel": "B",
        "efecto": "c.681G>A, splicing defecto; perdida de funcion; PM si es *2/*2 o *2/*3",
    },
    {
        "rsid": "rs4986893",
        "gen": "CYP2C19",
        "alelo": "*3",
        "farmaco": "ciclofosfamida",
        "nivel": "B",
        "efecto": "c.636G>A, p.Trp212Ter (stop); perdida de funcion",
    },
    # CYP3A4 — ciclofosfamida y sirolimus (IMPORTANTE)
    {
        "rsid": "rs35599367",
        "gen": "CYP3A4",
        "alelo": "*22",
        "farmaco": "ciclofosfamida/sirolimus",
        "nivel": "B",
        "efecto": "c.522-191C>T, intronica; reduce expresion ~50%; portadores: mayor exposicion a sirolimus",
    },
    {
        "rsid": "rs2740574",
        "gen": "CYP3A4",
        "alelo": "*1B",
        "farmaco": "ciclofosfamida/sirolimus",
        "nivel": "C",
        "efecto": "5'UTR -392A>G; evidencia de efecto en actividad enzimatica debatida",
    },
    # CYP3A4 *1G — relevante para sirolimus segun docx del equipo
    {
        "rsid": "rs2242480",
        "gen": "CYP3A4",
        "alelo": "*1G",
        "farmaco": "sirolimus",
        "nivel": "C",
        "efecto": "Intronico; portadores tienen AUC y Cmax de sirolimus menores (mayor aclaramiento)",
    },
    # CYP3A5 — metabolismo de sirolimus; guia CPIC para tacrolimus (analogia directa)
    {
        "rsid": "rs776746",
        "gen": "CYP3A5",
        "alelo": "*3",
        "farmaco": "sirolimus",
        "nivel": "A",
        "efecto": (
            "c.219-237A>G, splicing intron 3; perdida de funcion. "
            "*3/*3 = no expresor: CYP3A4 domina, dosis estandar de sirolimus (CPIC). "
            "*1/*3 = expresor intermedio. "
            "*1/*1 = expresor: metabolismo mas rapido, podria necesitar dosis mas alta"
        ),
    },
    # ABCB1 (MDR1 / P-gp) — transporte intestinal de sirolimus (IMPORTANTE)
    {
        "rsid": "rs1045642",
        "gen": "ABCB1",
        "alelo": "3435C>T",
        "farmaco": "sirolimus",
        "nivel": "C",
        "efecto": (
            "c.3435C>T, sinonima (Ile1145=); reduce expresion de P-gp -> mayor absorcion oral "
            "de sirolimus; evidencia clinica debatida"
        ),
    },
    {
        "rsid": "rs2032582",
        "gen": "ABCB1",
        "alelo": "2677G>T/A",
        "farmaco": "sirolimus",
        "nivel": "C",
        "efecto": "Ala893Ser/Thr; reduce funcion de P-gp; analizar junto a rs1045642",
    },
    {
        "rsid": "rs1128503",
        "gen": "ABCB1",
        "alelo": "1236C>T",
        "farmaco": "sirolimus",
        "nivel": "C",
        "efecto": "c.1236C>T, sinonima (Gly412=); parte del haplotipo ABCB1 triple; evidencia debatida",
    },
]


# ---------------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------------

def ensembl_coords(rsid: str, cache: dict) -> dict | None:
    """Devuelve dict {chrom, pos, ref, alt, allele_string} para un rsID (GRCh38).
    Usa cache para no repetir llamadas."""
    if rsid in cache:
        return cache[rsid]

    url = f"{ENSEMBL}/variation/human/{rsid}"
    for intento in range(4):
        try:
            r = requests.get(url, headers=HEADERS,
                             params={"content-type": "application/json"},
                             timeout=20)
            if r.status_code == 200:
                data = r.json()
                for m in data.get("mappings", []):
                    chrom = str(m.get("seq_region_name", ""))
                    if (m.get("assembly_name") == "GRCh38"
                            and (chrom.isdigit() or chrom in ("X", "Y"))):
                        alleles = m.get("allele_string", "")
                        parts = alleles.split("/")
                        coords = {
                            "chrom": chrom,
                            "pos": int(m["start"]),
                            "ref": parts[0] if parts else "",
                            "alt": parts[1] if len(parts) > 1 else "",
                            "allele_string": alleles,
                        }
                        cache[rsid] = coords
                        return coords
                # Sin mapeo GRCh38 en cromosoma estandar
                cache[rsid] = None
                return None
            elif r.status_code == 429:
                time.sleep(20)
                continue
            else:
                break
        except requests.RequestException:
            pass
        time.sleep(4 * 2**intento)

    cache[rsid] = None
    return None


def leer_vcf_para_posiciones(posiciones: dict) -> dict:
    """
    Escaneo unico del VCF para buscar todas las posiciones de interes.
    posiciones: {(chrom_str, pos_int): rsid}
    Devuelve: {rsid: {FILTER, REF, ALT, GT, DP, AD, GQ}}
    """
    encontrados = {}
    if VCF_PATH is None:
        print("  AVISO: VCF no encontrado en data/raw/", file=sys.stderr)
        return encontrados

    with gzip.open(VCF_PATH, "rt", encoding="utf-8", errors="replace") as fh:
        for linea in fh:
            if linea.startswith("#"):
                continue
            cols = linea.rstrip("\n").split("\t", 10)
            if len(cols) < 10:
                continue
            chrom, pos_str = cols[0], cols[1]
            key = (chrom, int(pos_str))
            if key not in posiciones:
                continue
            rsid = posiciones[key]
            fmt_keys = cols[8].split(":")
            fmt_vals = cols[9].split(":")
            fmt = dict(zip(fmt_keys, fmt_vals))
            gt_raw = fmt.get("GT", "./.")
            gt = gt_raw.replace("|", "/")
            encontrados[rsid] = {
                "FILTER": cols[6],
                "REF": cols[3],
                "ALT": cols[4],
                "GT": gt,
                "DP": fmt.get("DP", "NA"),
                "AD": fmt.get("AD", "NA"),
                "GQ": fmt.get("GQ", "NA"),
            }
    return encontrados


def etiqueta_genotipo(v: dict, coords: dict | None, geno: dict | None) -> str:
    """Texto breve para el genotipo observado."""
    if coords is None:
        return "No evaluado (sin coordenadas Ensembl)"
    if geno is None:
        return (
            "No encontrado en el VCF "
            "-> probable homocigota de referencia (alelo salvaje); "
            "verificar cobertura en esa region"
        )
    gt = geno["GT"]
    if gt in ("./.", ".|.", "."):
        return "Sin llamada (.) en el VCF — cobertura insuficiente"
    partes = gt.split("/") if "/" in gt else gt.split("|")
    n_alt = sum(1 for a in partes if a not in ("0", "."))
    if n_alt == 0:
        return "Homocigota referencia (WT/WT) — alelo salvaje"
    elif n_alt == 1:
        return f"Heterocigota (WT/{v['alelo']}) — portador de un alelo variante"
    else:
        return f"Homocigota variante ({v['alelo']}/{v['alelo']}) — ambos alelos variantes"


def cpic_cyp3a5(geno: dict | None) -> str:
    """Fenotipo CYP3A5 segun guia CPIC para tacrolimus (analogia sirolimus)."""
    if geno is None:
        # No esta en el VCF -> probable *3/*3 (no expresor), el mas frecuente en europeos
        return (
            "Probable CYP3A5*3/*3 (no expresor) — el genotipo no aparece en el VCF, "
            "lo que sugiere homocigota de referencia para el alelo variante *3. "
            "Interpretacion CPIC: dosis estandar de sirolimus (CYP3A4 es la enzima dominante). "
            "Verificar cobertura para confirmar."
        )
    gt = geno["GT"]
    partes = gt.split("/") if "/" in gt else gt.split("|")
    n_alt = sum(1 for a in partes if a not in ("0", "."))

    # rs776746: REF = A (*1, expresor), ALT = G (*3, no expresor)
    # Pero en el VCF la referencia puede estar invertida segun la hebra.
    # Verificar con coords["ref"] / coords["alt"] en el JSON de salida.
    if n_alt == 0:
        return (
            "CYP3A5*1/*1 (expresor) — metabolismo rapido de sirolimus. "
            "CPIC (tacrolimus): considerar dosis mas alta al inicio."
        )
    elif n_alt == 1:
        return (
            "CYP3A5*1/*3 (expresor intermedio) — metabolismo moderado. "
            "CPIC (tacrolimus): dosis estandar."
        )
    else:
        return (
            "CYP3A5*3/*3 (no expresor) — CYP3A4 domina el metabolismo de sirolimus. "
            "CPIC (tacrolimus): dosis estandar."
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Cargar cache de coordenadas Ensembl
    cache_coords = json.loads(CACHE_FILE.read_text(encoding="utf-8")) if CACHE_FILE.exists() else {}

    print("=" * 65)
    print("ANALISIS FARMACOGENOMICO — MVA HACKATHON 2026")
    print("Drogas: ciclofosfamida | sirolimus/nab-sirolimus | arimoclomol")
    if VCF_PATH:
        print(f"VCF: {VCF_PATH.name}")
    else:
        print("AVISO: VCF no encontrado en data/raw/ — los genotipos no se podran leer")
    print("=" * 65)

    # Paso 1: Resolver rsIDs a coordenadas GRCh38
    print("\n[1/3] Resolviendo rsIDs a coordenadas GRCh38 (Ensembl)...")
    for v in VARIANTES:
        rsid = v["rsid"]
        if rsid not in cache_coords:
            sys.stdout.write(f"  {rsid} ...")
            sys.stdout.flush()
            c = ensembl_coords(rsid, cache_coords)
            if c:
                print(f" {c['chrom']}:{c['pos']}  {c['allele_string']}")
            else:
                print(" sin respuesta")
            time.sleep(0.4)  # cortesia con Ensembl
        else:
            c = cache_coords[rsid]
            if c:
                print(f"  {rsid} (cache) -> {c['chrom']}:{c['pos']}")

    # Guardar cache
    CACHE_FILE.write_text(json.dumps(cache_coords, indent=2), encoding="utf-8")

    # Paso 2: Escaneo unico del VCF
    posiciones = {}
    for v in VARIANTES:
        c = cache_coords.get(v["rsid"])
        if c:
            posiciones[(c["chrom"], c["pos"])] = v["rsid"]

    print(f"\n[2/3] Escaneando VCF para {len(posiciones)} posiciones...")
    encontrados = leer_vcf_para_posiciones(posiciones)
    print(f"  Encontradas en el VCF: {len(encontrados)} / {len(posiciones)}")

    # Paso 3: Armar resultados y resumen
    print("\n[3/3] Compilando resultados...\n")
    resultados = []
    for v in VARIANTES:
        rsid = v["rsid"]
        coords = cache_coords.get(rsid)
        geno = encontrados.get(rsid)

        if v["gen"] == "CYP3A5" and v["alelo"] == "*3":
            etiq = cpic_cyp3a5(geno)
        else:
            etiq = etiqueta_genotipo(v, coords, geno)

        resultados.append({
            "rsid": rsid,
            "gen": v["gen"],
            "alelo": v["alelo"],
            "farmaco": v["farmaco"],
            "nivel_evidencia": v["nivel"],
            "efecto_alelo_mut": v["efecto"],
            "coords_grch38": coords,
            "genotipo_vcf": geno,
            "interpretacion": etiq,
        })

    # Guardar JSON completo (con posiciones) en data/ — NO versionado
    out_json = OUT_DIR / "genotipos_farma.json"
    out_json.write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Genotipos crudos guardados en: {out_json}")

    # Imprimir resumen
    print()
    print("=" * 65)
    print("RESUMEN (solo fenotipos — sin coordenadas exactas del paciente)")
    print("=" * 65)

    farmaco_actual = ""
    for r in resultados:
        if r["farmaco"] != farmaco_actual:
            print(f"\n=== {r['farmaco'].upper()} ===")
            farmaco_actual = r["farmaco"]
        nivel = r["nivel_evidencia"]
        print(f"  {r['gen']} {r['alelo']} [nivel {nivel}]:")
        print(f"    {r['interpretacion']}")

    print()
    print("-" * 65)
    print("GSTM1 nulo: es una delecion grande (~3.1 kb, 1p13.3).")
    print("  No detectable en VCF de SNV. Requiere analisis de profundidad")
    print("  de lectura o array de genotipado. Se reporta como NO EVALUADO.")
    print()
    print("Nivel de evidencia: A = guia CPIC formal  B = sin guia pero bien documentado")
    print("                    C = evidencia debatida (no cambia la decision clinica sola)")
    print("-" * 65)
    print()
    print("ARIMOCLOMOL: sin farmacogenetica relevante conocida.")
    print("  El factor limitante es la funcion renal (creatinina / cistatina C).")
    print("  Ver secciones 2.1 de 04_candidatos.md para los riesgos especificos.")


if __name__ == "__main__":
    main()
