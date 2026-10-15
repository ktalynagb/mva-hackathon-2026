"""analisis_genes_equipo.py — Tarea C8: modelo dominante para la lista de genes del equipo.

Corre el embudo del diagnóstico diferencial (diagnostico_diferencial.py) para los cuatro genes
de la lista del equipo que tienen justificación biológica para un modelo dominante:
  LMNA   — laminopatía dominante (Emery-Dreifuss AD, miocardiopatía dilatada)
  KMT2D  — síndrome Kabuki tipo 1 (AD, microcefalia + talla baja + DI = overlap fenotípico)
  KDM6A  — síndrome Kabuki tipo 2 (X-linked dominante en mujeres)
  ATM    — predisposición a cáncer (monoalélico); ataxia-telangiectasia (bialélico, recesivo)

Los demás genes de la lista del equipo se descartan por razones documentadas abajo.
Salida (no versionada): data/genes_equipo/
"""
import csv
import importlib.util
import json
import sys
import time
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
CONFIG = RAIZ / "config" / "paneles_modelo_dominante.json"
SALIDA = RAIZ / "data" / "genes_equipo"

GENES_A_CORRER = ["LMNA", "KMT2D", "KDM6A", "ATM"]

HERENCIA_NOTA = {
    "LMNA":  "MONOALLELIC, AD — laminopatía (Emery-Dreifuss, DCM, progeria)",
    "KMT2D": "MONOALLELIC, AD — síndrome Kabuki tipo 1",
    "KDM6A": "X-LINKED dominant (mujeres heterocigotas) — síndrome Kabuki tipo 2",
    "ATM":   "MONOALLELIC (predisposición cáncer) / BIALLELIC (ataxia-telangiectasia)",
}

DESCARTES = {
    "EZH2":   "Síndrome de Weaver (overgrowth: macrocefalia, estatura alta). Fenotipo OPUESTO al paciente.",
    "BRCA1":  "Predisposición a cáncer de mama/ovario en adultos. No causa fenotipo neonatal/pediátrico.",
    "BRCA2":  "Ídem BRCA1. Predisposición oncológica adulta.",
    "PALB2":  "Predisposición a cáncer de mama/páncreas en adultos. No aplica como causa primaria.",
    "RAD51C": "Predisposición a cáncer de ovario/mama. Contexto adulto.",
    "RAD51D": "Ídem RAD51C.",
    "CHEK2":  "Predisposición moderada a cáncer adulto. No causa fenotipo pediátrico.",
    "FANCM":  "Anemia de Fanconi biallélica (recesiva). No aplica modelo dominante.",
    "LMNB1":  "Leucodistrofia AD por duplicación de LMNB1; fenotipo principalmente neurológico adulto.",
    "EMD":    "Emerinopatía X-linked recesiva (varones); fenotipo muscular/cardíaco, no el cuadro actual.",
    "NUP155": "Fibrilación auricular familiar (recesiva según NORD). Sin causa dominante relevante aquí.",
    "RANBP2": "Encefalitis aguda necrotizante (AD en contexto febril). No causa del cuadro crónico.",
}


def cargar_dd():
    spec = importlib.util.spec_from_file_location("dd", RAIZ / "scripts" / "diagnostico_diferencial.py")
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)
    return dd


def anotar(clave):
    """ClinVar, REVEL y CADD (myvariant.info, GRCh38). Solo SNV (ref y alt de 1 nt)."""
    c, pos, ref, alt = clave.split("-")
    if len(ref) != 1 or len(alt) != 1:
        return {}
    try:
        r = requests.get(
            f"https://myvariant.info/v1/variant/chr{c}:g.{pos}{ref}>{alt}",
            timeout=30,
            params={"assembly": "hg38",
                    "fields": "clinvar.rcv.clinical_significance,dbnsfp.revel.score,dbnsfp.cadd.phred"},
        )
        if r.status_code != 200:
            return {}
        j = r.json()
    except (requests.RequestException, ValueError):
        return {}
    rcv = (j.get("clinvar") or {}).get("rcv") or []
    rcv = rcv if isinstance(rcv, list) else [rcv]
    revel = ((j.get("dbnsfp") or {}).get("revel") or {}).get("score")
    cadd = ((j.get("dbnsfp") or {}).get("cadd") or {}).get("phred")
    primero = lambda x: max(x) if isinstance(x, list) else x
    return {
        "clinvar": "; ".join(sorted({x.get("clinical_significance", "") for x in rcv if x})),
        "revel": primero(revel),
        "cadd": primero(cadd),
    }


def restriccion(simbolo):
    """LOEUF y Z-score de missense del gen (gnomAD v4 GraphQL)."""
    q = """query($g:String!){
        gene(gene_symbol:$g, reference_genome:GRCh38){
            gnomad_constraint{oe_lof_upper mis_z pli}}}"""
    try:
        r = requests.post(
            "https://gnomad.broadinstitute.org/api",
            json={"query": q, "variables": {"g": simbolo}},
            timeout=60,
        )
        return ((r.json().get("data") or {}).get("gene") or {}).get("gnomad_constraint") or {}
    except (requests.RequestException, ValueError):
        return {}


def main():
    crit = json.loads(CONFIG.read_text(encoding="utf-8"))["criterios"]
    SALIDA.mkdir(parents=True, exist_ok=True)

    lista_genes = SALIDA / "genes.txt"
    lista_genes.write_text("\n".join(GENES_A_CORRER) + "\n", encoding="utf-8")

    print(f"=== C8: análisis dominante para genes del equipo ===")
    print(f"Genes: {', '.join(GENES_A_CORRER)}")
    dd = cargar_dd()
    dd.GENES = lista_genes
    dd.OUT = SALIDA
    sys.argv = ["diagnostico_diferencial.py"]
    dd.main()

    with open(SALIDA / "diagnostico_diferencial_genes.tsv", encoding="utf-8") as f:
        por_gen = list(csv.DictReader(f, delimiter="\t"))
    with open(SALIDA / "diagnostico_diferencial_variantes.tsv", encoding="utf-8") as f:
        variantes = list(csv.DictReader(f, delimiter="\t"))

    # Filtro modelo dominante (mismo criterio que modelo_dominante.py)
    het_func = [v for v in variantes if v["zig"] == "HET" and v["cuenta"] == "True"]
    muy_raras = [v for v in het_func if v["af"] in ("", "None") or float(v["af"]) <= crit["af_max"]]
    buenas = [v for v in muy_raras if int(v["gq"] or 0) >= crit["gq_min"] and int(v["dp"] or 0) >= crit["dp_min"]]

    # Check bialélico ATM: ¿hay ≥2 variantes raras funcionales, o alguna homocigota?
    atm_raras_func = [v for v in variantes if v["gen"] == "ATM" and v["cuenta"] == "True"
                      and (v["af"] in ("", "None") or float(v["af"]) < 0.01)]
    atm_biallelic = len(atm_raras_func) >= 2 or any(v["zig"] == "HOM" for v in atm_raras_func)

    n = lambda col: sum(int(float(r[col])) for r in por_gen
                        if r.get(col) not in (None, "") and r.get("analizado", "True") != "False")
    print("\n--- EMBUDO DOMINANTE (genes del equipo) ---")
    print(f"  variantes PASS en los genes:            {n('variantes_pass')}")
    print(f"  raras (AF < 1%) o ausentes de gnomAD:   {n('raras_o_ausentes')}")
    print(f"  con efecto en algún transcrito:         {n('alertas_cualquier_transcrito')}")
    print(f"  con efecto en transcrito MANE:          {n('raras_funcionales')}")
    print(f"  heterocigotas con efecto MANE:          {len(het_func)}")
    print(f"  AF <= {crit['af_max']:g} o ausentes:             {len(muy_raras)}")
    print(f"  GQ >= {crit['gq_min']} y DP >= {crit['dp_min']}:                  {len(buenas)}")

    print("\n--- CANDIDATAS DOMINANTES ---")
    filas = []
    for v in buenas:
        clave = f"{v['chrom']}-{v['pos']}-{v['ref']}-{v['alt']}"
        a = anotar(clave)
        k = restriccion(v["gen"])
        filas.append({
            **v,
            "herencia_nota": HERENCIA_NOTA.get(v["gen"], ""),
            **a,
            "loeuf": k.get("oe_lof_upper"),
            "mis_z": k.get("mis_z"),
            "pli": k.get("pli"),
        })
        time.sleep(0.4)

    if filas:
        cols = ["gen", "chrom", "pos", "ref", "alt", "zig", "consecuencia_mane", "hgvsp",
                "af", "dp", "gq", "clinvar", "revel", "cadd", "loeuf", "mis_z", "pli", "herencia_nota"]
        with open(SALIDA / "candidatos_genes_equipo.tsv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, cols, delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(filas)
        for r in filas:
            hgvsp = (r.get("hgvsp") or "")[-28:]
            print(f"  {r['gen']:8s} {r['consecuencia_mane']:25s} {hgvsp:28s} "
                  f"AF={r['af'] or 'ausente':12s} ClinVar={r.get('clinvar') or '-'} "
                  f"REVEL={r.get('revel')} CADD={r.get('cadd')} LOEUF={r.get('loeuf')}")
    else:
        print("  -> Ninguna variante pasa el filtro dominante.")
        open(SALIDA / "candidatos_genes_equipo.tsv", "w").close()

    print(f"\n--- ATM CHECK BIALÉLICO ---")
    if atm_biallelic:
        print(f"  ATM: posible patrón bialélico ({len(atm_raras_func)} variantes raras funcionales) → revisar A-T")
    else:
        print(f"  ATM: {len(atm_raras_func)} variante(s) rara(s) funcional(es); patrón bialélico NO detectado")

    print(f"\n--- GENES DESCARTADOS ---")
    for g, motivo in DESCARTES.items():
        print(f"  {g:10s}: {motivo}")

    print(f"\nSalida: {SALIDA}")
    print(f"Candidatas guardadas: {SALIDA}/candidatos_genes_equipo.tsv")


if __name__ == "__main__":
    main()
