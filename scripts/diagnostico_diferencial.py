"""Diagnostico diferencial (tarea A3): ¿algun otro gen del panel explica el MVA?

Para cada gen de config/genes_candidatos.txt:
  1. Toma las variantes PASS del paciente dentro del gen (VCF en data/raw/).
  2. Las cruza con gnomAD v4 (frecuencia y consecuencia) y, para las ausentes de gnomAD, con Ensembl VEP.
  3. Cuenta variantes raras (AF < 1 % o ausentes de gnomAD) con efecto funcional y evalua si el patron es compatible con
     herencia recesiva: >= 1 homocigota, o >= 2 heterocigotas (fase desconocida).

Salida (results/):
  diagnostico_diferencial_genes.tsv      una fila por gen
  diagnostico_diferencial_variantes.tsv  variantes raras funcionales, solo de genes del panel
Uso:  python scripts/diagnostico_diferencial.py
Requiere el VCF descargado (data/raw/) y conexion a gnomAD y Ensembl.
"""
import csv
import gzip
import json
import time
from collections import defaultdict
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
VCF = next((RAIZ / "data" / "raw").glob("*.vcf.gz"))
GENES = RAIZ / "config" / "genes_candidatos.txt"
CACHE = RAIZ / "data" / "cache"
OUT = RAIZ / "results"
GNOMAD = "https://gnomad.broadinstitute.org/api"
VEP = "https://rest.ensembl.org/vep/human/region"
AF_RARA = 0.01

LOF = {"stop_gained", "frameshift_variant", "splice_acceptor_variant", "splice_donor_variant",
       "start_lost", "stop_lost"}
FUNCIONAL = LOF | {"missense_variant", "inframe_deletion", "inframe_insertion", "protein_altering_variant"}

QUERY = """query($g:String!){ gene(gene_symbol:$g, reference_genome:GRCh38){
  gene_id symbol chrom start stop
  variants(dataset: gnomad_r4){ variant_id consequence
    exome{ac an ac_hom} genome{ac an ac_hom} } } }"""


def leer_genes():
    return [l.split()[0] for l in GENES.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")]


def simbolo_oficial(alias):
    """Simbolo HGNC oficial de un alias (MyGene.info); None si no se resuelve."""
    try:
        r = requests.get("https://mygene.info/v3/query", timeout=60,
                         params={"q": f"symbol:{alias} OR alias:{alias}", "species": "human", "fields": "symbol", "size": 3})
        hits = r.json().get("hits", [])
        return hits[0]["symbol"] if hits else None
    except (requests.RequestException, ValueError, KeyError):
        return None


def gnomad_gen(simbolo):
    """Descarga (con cache) las variantes de gnomAD de un gen. Devuelve (datos, motivo_si_falla)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"gnomad_{simbolo}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8")), None
    motivo = "sin respuesta"
    for intento in range(6):
        try:
            r = requests.post(GNOMAD, json={"query": QUERY, "variables": {"g": simbolo}}, timeout=300)
            j = r.json() if r.status_code == 200 else {}
            if r.status_code == 200 and not j.get("errors") and j["data"]["gene"]:
                f.write_text(json.dumps(j["data"]["gene"]), encoding="utf-8")
                return j["data"]["gene"], None
            msg = (j.get("errors") or [{}])[0].get("message", f"HTTP {r.status_code}")
            motivo = msg
            if "not found" in msg.lower():
                return None, "no encontrado"
        except (requests.RequestException, ValueError) as e:
            motivo = type(e).__name__
        time.sleep(4 * 2 ** intento)
    return None, motivo


QUERY_VAR = """query($id:String!){ variant(variantId:$id, dataset:gnomad_r4){
  variant_id exome{ac an ac_hom} genome{ac an ac_hom} } }"""


def gnomad_variante(clave):
    """Consulta directa de una variante en gnomAD v4 (con cache). None si no esta."""
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / "gnomad_variantes.json"
    cache = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    if clave not in cache:
        for intento in range(5):
            try:
                r = requests.post(GNOMAD, json={"query": QUERY_VAR, "variables": {"id": clave}}, timeout=60)
                if r.status_code == 200:
                    j = r.json()
                    cache[clave] = (j.get("data") or {}).get("variant")
                    break
            except (requests.RequestException, ValueError):
                pass
            time.sleep(3 * 2 ** intento)
        else:
            return None
        f.write_text(json.dumps(cache), encoding="utf-8")
        time.sleep(0.3)
    return cache[clave]


def frecuencia(v):
    """Frecuencia maxima entre exoma y genoma; None si no hay datos."""
    fr = [x["ac"] / x["an"] for x in (v.get("exome"), v.get("genome")) if x and x.get("an")]
    return max(fr) if fr else None


def homocigotos(v):
    return sum(x.get("ac_hom") or 0 for x in (v.get("exome"), v.get("genome")) if x)


def variantes_paciente(regiones):
    """Variantes PASS del paciente dentro de las regiones {simbolo: (chrom, ini, fin)}."""
    por_chrom = defaultdict(list)
    for s, (c, a, b) in regiones.items():
        por_chrom[c].append((a, b, s))
    for lista in por_chrom.values():
        lista.sort()
    salida = defaultdict(list)
    with gzip.open(VCF, "rt", encoding="utf-8", errors="replace") as fh:
        for linea in fh:
            if linea[0] == "#":
                continue
            p = linea.rstrip("\n").split("\t")
            if p[6] != "PASS" or p[0] not in por_chrom:
                continue
            pos = int(p[1])
            gen = next((s for a, b, s in por_chrom[p[0]] if a <= pos <= b), None)
            if gen is None:
                continue
            gt = p[9].split(":")[0].replace("|", "/").split("/")
            if "." in gt or all(x == "0" for x in gt):
                continue
            alts = p[4].split(",")
            fmt = dict(zip(p[8].split(":"), p[9].split(":")))
            for i in sorted({int(x) for x in gt if x != "0"}):
                zig = "HOM" if gt.count(str(i)) == 2 else "HET"
                salida[gen].append({"chrom": p[0], "pos": pos, "ref": p[3], "alt": alts[i - 1], "zig": zig,
                                    "dp": fmt.get("DP"), "gq": fmt.get("GQ")})
    return salida


def vep_lote(variantes):
    """Consecuencia mas severa (Ensembl VEP) para variantes ausentes de gnomAD. {clave: consecuencia}.
    Guarda cache en data/cache/vep.json para no repetir consultas."""
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / "vep.json"
    res = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    claves = [c for c in variantes if c not in res]
    for i in range(0, len(claves), 100):
        lote = claves[i:i + 100]
        cuerpo = {"variants": [f"{c.split('-')[0]} {c.split('-')[1]} . {c.split('-')[2]} {c.split('-')[3]} . . ." for c in lote]}
        for intento in range(4):
            try:
                r = requests.post(VEP, json=cuerpo, headers={"Content-Type": "application/json"}, timeout=180)
                if r.status_code == 200:
                    for e in r.json():
                        ini = e["input"].split()
                        res[f"{ini[0]}-{ini[1]}-{ini[3]}-{ini[4]}"] = e.get("most_severe_consequence")
                    f.write_text(json.dumps(res), encoding="utf-8")
                    break
            except (requests.RequestException, ValueError):
                pass
            time.sleep(5 * 2 ** intento)
        time.sleep(1)
    return {c: res.get(c) for c in variantes}


def main():
    simbolos = leer_genes()
    gen_info, regiones, no_analizados = {}, {}, {}
    for s in simbolos:
        g, motivo = gnomad_gen(s)
        if g is None and motivo == "no encontrado":
            oficial = simbolo_oficial(s)
            if oficial and oficial != s:
                g, motivo = gnomad_gen(oficial)
                if g:
                    print(f"{s} -> {oficial}")
        if g:
            gen_info[s] = g
            regiones[s] = (g["chrom"], g["start"], g["stop"])
        else:
            no_analizados[s] = motivo
            print(f"NO ANALIZADO {s}: {motivo}")
        time.sleep(0.3)
    print(f"{len(regiones)} de {len(simbolos)} genes resueltos; {len(no_analizados)} sin analizar; leyendo el VCF...")
    paciente = variantes_paciente(regiones)

    ausentes = {}
    filas_var = []
    for s, lista in paciente.items():
        indice = {v["variant_id"]: v for v in gen_info[s]["variants"]}
        for v in lista:
            clave = f"{v['chrom']}-{v['pos']}-{v['ref']}-{v['alt']}"
            g = indice.get(clave)
            v["clave"], v["gen"] = clave, s
            if g is None:
                v["af"], v["hom_gnomad"], v["consecuencia"], v["en_gnomad"] = None, 0, None, False
                ausentes[clave] = v
            else:
                v["af"], v["hom_gnomad"] = frecuencia(g), homocigotos(g)
                v["consecuencia"], v["en_gnomad"] = g["consequence"], True
    print(f"{sum(len(l) for l in paciente.values())} variantes del paciente en el panel; "
          f"{len(ausentes)} ausentes de gnomAD -> VEP")
    for k, c in vep_lote(ausentes).items():
        ausentes[k]["consecuencia"] = c
    # La lista por gen de gnomAD omite variantes (p. ej. frecuentes con el alelo alterno mayoritario):
    # las funcionales que "faltan" se consultan una a una antes de llamarlas ausentes.
    for k, v in ausentes.items():
        if v["consecuencia"] in FUNCIONAL:
            d = gnomad_variante(k)
            if d:
                v["af"], v["hom_gnomad"], v["en_gnomad"] = frecuencia(d), homocigotos(d), True

    resumen = []
    for s in simbolos:
        if s in no_analizados:
            resumen.append({"gen": s, "analizado": False, "motivo": no_analizados[s]})
            continue
        lista = paciente.get(s, [])
        raras = [v for v in lista if v["af"] is None or v["af"] < AF_RARA]
        func = [v for v in raras if v["consecuencia"] in FUNCIONAL]
        lof = [v for v in func if v["consecuencia"] in LOF]
        hom = [v for v in func if v["zig"] == "HOM"]
        het = [v for v in func if v["zig"] == "HET"]
        sin_anotar = [v for v in raras if v["consecuencia"] is None]
        compat = bool(hom) or len(het) >= 2
        resumen.append({"gen": s, "analizado": True, "motivo": "", "variantes_pass": len(lista), "raras_o_ausentes": len(raras), "raras_funcionales": len(func),
                        "lof": len(lof), "hom_funcionales": len(hom), "het_funcionales": len(het),
                        "sin_anotar": len(sin_anotar), "patron_recesivo": compat})
        filas_var += [dict(v, gen=s) for v in func]

    OUT.mkdir(exist_ok=True)
    cols = ["gen", "analizado", "motivo", "variantes_pass", "raras_o_ausentes", "raras_funcionales", "lof", "hom_funcionales", "het_funcionales",
            "sin_anotar", "patron_recesivo"]
    with open(OUT / "diagnostico_diferencial_genes.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, cols, delimiter="\t")
        w.writeheader()
        w.writerows(sorted(resumen, key=lambda r: (not r["analizado"], -r.get("lof", 0), -r.get("raras_funcionales", 0), r["gen"])))
    cols_v = ["gen", "chrom", "pos", "ref", "alt", "zig", "consecuencia", "af", "hom_gnomad", "en_gnomad", "dp", "gq"]
    with open(OUT / "diagnostico_diferencial_variantes.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, cols_v, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(filas_var, key=lambda v: (v["gen"], v["pos"])))
    print("Guardado en results/")


if __name__ == "__main__":
    main()
