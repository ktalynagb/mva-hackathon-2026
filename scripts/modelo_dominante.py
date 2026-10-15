"""Modelo dominante / diagnóstico dual (tarea A10): ¿alguna variante en UNA sola copia explica parte del cuadro?

El MVA es recesivo y ya está explicado por BUB1B. Esta prueba busca un segundo diagnóstico dominante, sobre todo para
la nefrocalcinosis, que el MVA no explica, y para la predisposición al rabdomiosarcoma.

  1. Genes: paneles de PanelApp de config/paneles_modelo_dominante.json, genes verdes con herencia monoalélica.
     La lista queda en config/genes_modelo_dominante.tsv.
  2. Mismo embudo que el diagnóstico diferencial (scripts/diagnostico_diferencial.py, criterio MANE de A8).
  3. Filtro dominante: heterocigota, funcional en MANE, AF ≤ 1e-5 en gnomAD v4 (o ausente), GQ ≥ 20 y DP ≥ 10.
  4. Las que pasan se anotan con ClinVar, REVEL y CADD (myvariant.info) y la restricción del gen (gnomAD).

Salida con variantes del paciente (no se versiona): data/dominante/
Uso: python scripts/modelo_dominante.py
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
LISTA = RAIZ / "config" / "genes_modelo_dominante.tsv"
SALIDA = RAIZ / "data" / "dominante"
UA = {"User-Agent": "MVAHackathon2026/1.0 (research)"}


def cargar_dd():
    spec = importlib.util.spec_from_file_location("dd", RAIZ / "scripts" / "diagnostico_diferencial.py")
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)
    return dd


def genes_de_paneles(paneles, herencias=("MONOALLELIC", "BOTH MONOALLELIC")):
    """{símbolo: {"paneles": [...], "herencia": ...}} con genes verdes y el modo de herencia pedido."""
    genes = {}
    for p in paneles:
        d = requests.get(f"https://panelapp.genomicsengland.co.uk/api/v1/panels/{p['id']}/", headers=UA, timeout=60).json()
        for g in d["genes"]:
            moi = g.get("mode_of_inheritance") or ""
            if g.get("confidence_level") != "3" or not moi.upper().startswith(herencias):
                continue
            s = g["gene_data"].get("hgnc_symbol") or g["entity_name"]
            e = genes.setdefault(s, {"paneles": [], "herencia": moi})
            e["paneles"].append(f"{d['name']} (v{d['version']})")
        time.sleep(0.5)
    return genes


def anotar(clave):
    """ClinVar, REVEL y CADD de una SNV (myvariant.info, GRCh38)."""
    c, pos, ref, alt = clave.split("-")
    if len(ref) != 1 or len(alt) != 1:
        return {}
    try:
        r = requests.get(f"https://myvariant.info/v1/variant/chr{c}:g.{pos}{ref}>{alt}", timeout=30,
                         params={"assembly": "hg38", "fields": "clinvar.rcv.clinical_significance,dbnsfp.revel.score,dbnsfp.cadd.phred"})
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
    return {"clinvar": "; ".join(sorted({x.get("clinical_significance", "") for x in rcv if x})),
            "revel": primero(revel), "cadd": primero(cadd)}


def restriccion(simbolo):
    """LOEUF y Z de missense del gen (gnomAD v4). Bajo LOEUF = el gen no tolera perder una copia."""
    q = 'query($g:String!){gene(gene_symbol:$g, reference_genome:GRCh38){gnomad_constraint{oe_lof_upper mis_z pli}}}'
    try:
        r = requests.post("https://gnomad.broadinstitute.org/api", json={"query": q, "variables": {"g": simbolo}}, timeout=60)
        return ((r.json().get("data") or {}).get("gene") or {}).get("gnomad_constraint") or {}
    except (requests.RequestException, ValueError):
        return {}


def rinon_recesivo(cfg):
    """Control para la nefrocalcinosis: genes recesivos de los paneles renales con el modelo recesivo de A8."""
    renales = [p for p in cfg["paneles"] if p["id"] in cfg["paneles_renales"]]
    genes = genes_de_paneles(renales, ("BIALLELIC", "BOTH MONOALLELIC"))
    salida = RAIZ / "data" / "rinon_recesivo"
    salida.mkdir(parents=True, exist_ok=True)
    lista = salida / "genes.txt"
    lista.write_text("\n".join(sorted(genes)) + "\n", encoding="utf-8")
    print(f"{len(genes)} genes renales con herencia bialélica")
    dd = cargar_dd()
    dd.GENES, dd.OUT = lista, salida
    sys.argv = ["diagnostico_diferencial.py"]
    dd.main()
    with open(salida / "diagnostico_diferencial_genes.tsv", encoding="utf-8") as f:
        filas = list(csv.DictReader(f, delimiter="\t"))
    recesivos = [r["gen"] for r in filas if r.get("patron_recesivo") == "True"]
    con_variante = [r["gen"] for r in filas if r.get("raras_funcionales") not in ("", "0", None)]
    print(f"genes con una variante rara funcional en MANE: {', '.join(con_variante) or 'ninguno'}")
    print(f"genes con patrón recesivo: {', '.join(recesivos) or 'ninguno'}")


def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    if "--rinon-recesivo" in sys.argv:
        return rinon_recesivo(cfg)
    crit = cfg["criterios"]
    genes = genes_de_paneles(cfg["paneles"])
    with open(LISTA, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["gen", "herencia", "paneles"])
        for s in sorted(genes):
            w.writerow([s, genes[s]["herencia"], " | ".join(genes[s]["paneles"])])
    print(f"{len(genes)} genes con herencia monoalélica en {len(cfg['paneles'])} paneles -> {LISTA.name}")

    SALIDA.mkdir(parents=True, exist_ok=True)
    lista_dd = SALIDA / "genes.txt"
    lista_dd.write_text("\n".join(sorted(genes)) + "\n", encoding="utf-8")
    dd = cargar_dd()
    dd.GENES, dd.OUT = lista_dd, SALIDA
    sys.argv = ["diagnostico_diferencial.py"]
    dd.main()

    with open(SALIDA / "diagnostico_diferencial_genes.tsv", encoding="utf-8") as f:
        por_gen = list(csv.DictReader(f, delimiter="\t"))
    with open(SALIDA / "diagnostico_diferencial_variantes.tsv", encoding="utf-8") as f:
        variantes = list(csv.DictReader(f, delimiter="\t"))

    n = lambda col: sum(int(float(r[col])) for r in por_gen if r.get(col) not in (None, ""))
    het_func = [v for v in variantes if v["zig"] == "HET" and v["cuenta"] == "True"]
    muy_raras = [v for v in het_func if v["af"] in ("", "None") or float(v["af"]) <= crit["af_max"]]
    buenas = [v for v in muy_raras if int(v["gq"] or 0) >= crit["gq_min"] and int(v["dp"] or 0) >= crit["dp_min"]]
    print("\nEMBUDO DOMINANTE")
    print(f"  variantes PASS en los genes:            {n('variantes_pass')}")
    print(f"  raras (AF < 1 %) o ausentes de gnomAD:  {n('raras_o_ausentes')}")
    print(f"  con efecto en algún transcrito:         {n('alertas_cualquier_transcrito')}")
    print(f"  con efecto en el transcrito MANE:       {n('raras_funcionales')}")
    print(f"  heterocigotas:                          {len(het_func)}")
    print(f"  AF <= {crit['af_max']:g} o ausentes:              {len(muy_raras)}")
    print(f"  GQ >= {crit['gq_min']} y DP >= {crit['dp_min']}:                  {len(buenas)}")

    filas = []
    for v in buenas:
        clave = f"{v['chrom']}-{v['pos']}-{v['ref']}-{v['alt']}"
        a, k = anotar(clave), restriccion(v["gen"])
        filas.append({**v, "herencia": genes.get(v["gen"], {}).get("herencia", ""),
                      "paneles": " | ".join(genes.get(v["gen"], {}).get("paneles", [])),
                      **a, "loeuf": k.get("oe_lof_upper"), "mis_z": k.get("mis_z"), "pli": k.get("pli")})
        time.sleep(0.4)
    cols = ["gen", "chrom", "pos", "ref", "alt", "zig", "consecuencia_mane", "hgvsp", "af", "dp", "gq",
            "clinvar", "revel", "cadd", "loeuf", "mis_z", "pli", "herencia", "paneles"]
    with open(SALIDA / "candidatos_dominantes.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    print(f"\n{len(filas)} candidatas dominantes -> data/dominante/candidatos_dominantes.tsv")
    for r in filas:
        print(f"  {r['gen']:10s} {r['consecuencia_mane']:22s} {r['hgvsp'][-22:]:22s} AF={r['af'] or 'ausente':10s} "
              f"ClinVar={r.get('clinvar') or '-'} REVEL={r.get('revel')} CADD={r.get('cadd')} LOEUF={r.get('loeuf')}")


if __name__ == "__main__":
    main()
