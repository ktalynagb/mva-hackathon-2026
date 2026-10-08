"""Lista larga de farmacos para reposicionamiento (tarea C3).

Une tres fuentes por linea terapeutica (config/lineas_terapeuticas.json):
DGIdb v5, Open Targets y una lista curada con su fuente. Comprueba la
aprobacion en Drugs@FDA (openFDA) y en el listado de autorizaciones
centralizadas de la EMA, aplica los filtros F1 y F2 de
docs/secciones/03_criterios.md y deja las columnas de puntaje vacias para C4.

Uso:  python scripts/lista_larga_farmacos.py [--sin-cache]
Salida: results/candidatos_farmacos.tsv
"""
import argparse
import hashlib
import io
import json
import re
import sys
import time
from pathlib import Path

import pandas as pd
import requests

RAIZ = Path(__file__).resolve().parents[1]
CONFIG = RAIZ / "config" / "lineas_terapeuticas.json"
CACHE = RAIZ / "results" / "cache" / "c3"
SALIDA = RAIZ / "results" / "candidatos_farmacos.tsv"

DGIDB = "https://dgidb.org/api/graphql"
OT = "https://api.platform.opentargets.org/api/v4/graphql"
OPENFDA = "https://api.fda.gov/drug/drugsfda.json"
EMA_XLSX = "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"

SALES = ("HYDROCHLORIDE", "DIHYDROCHLORIDE", "MESYLATE", "MALEATE", "SULFATE", "CITRATE",
         "TARTRATE", "ACETATE", "PHOSPHATE", "BESYLATE", "TOSYLATE", "FUMARATE", "SUCCINATE",
         "HYDROBROMIDE", "MONOHYDRATE", "ANHYDROUS", "HYCLATE", "LACTATE", "MALATE", "S-MALATE",
         "D-MANNITOL", "TROMETHAMINE")
PREFIJOS = ("ANHYDROUS",)

USAR_CACHE = True


def normalizar(nombre):
    n = re.sub(r"\s+", " ", str(nombre).upper().strip())
    partes = n.split(" ")
    while len(partes) > 1 and partes[-1] in SALES:
        partes.pop()
    while len(partes) > 1 and partes[0] in PREFIJOS:
        partes.pop(0)
    return " ".join(partes)


def cacheado(clave, funcion):
    CACHE.mkdir(parents=True, exist_ok=True)
    ruta = CACHE / (hashlib.sha1(clave.encode()).hexdigest() + ".json")
    if USAR_CACHE and ruta.exists():
        return json.loads(ruta.read_text(encoding="utf-8"))
    datos = funcion()
    ruta.write_text(json.dumps(datos), encoding="utf-8")
    return datos


def graphql(url, consulta):
    for intento in range(3):
        r = requests.post(url, json={"query": consulta}, timeout=120)
        if r.status_code == 200:
            j = r.json()
            if "errors" in j:
                raise RuntimeError(f"{url}: {j['errors'][0]['message']}")
            return j["data"]
        time.sleep(2 * (intento + 1))
    r.raise_for_status()


# ── DGIdb ─────────────────────────────────────────────────────────────────────
def dgidb(genes):
    consulta = """{ genes(names: %s) { nodes { name interactions {
        drug { name approved }
        interactionTypes { type }
        sources { sourceDbName } } } } }""" % json.dumps(genes)
    datos = cacheado("dgidb:" + ",".join(sorted(genes)), lambda: graphql(DGIDB, consulta))
    filas = []
    for nodo in datos["genes"]["nodes"]:
        for i in nodo["interactions"]:
            filas.append({
                "gen": nodo["name"],
                "farmaco": normalizar(i["drug"]["name"]),
                "aprobado_dgidb": bool(i["drug"]["approved"]),
                "acciones": sorted({t["type"].lower() for t in i["interactionTypes"] if t["type"]}),
                "fuentes": sorted({s["sourceDbName"] for s in i["sources"]}),
            })
    return filas


# ── Open Targets ──────────────────────────────────────────────────────────────
DRUG_OT = "drug { name maximumClinicalStage mechanismsOfAction { rows { actionType targets { approvedSymbol } } } }"


def mecanismos(drug):
    return (drug.get("mechanismsOfAction") or {}).get("rows") or []


def ot_ensembl(simbolo):
    consulta = '{ search(queryString: "%s", entityNames: ["target"]) { hits { id object { ... on Target { approvedSymbol } } } } }' % simbolo
    datos = cacheado("ot_search:" + simbolo, lambda: graphql(OT, consulta))
    for h in datos["search"]["hits"]:
        if (h.get("object") or {}).get("approvedSymbol") == simbolo:
            return h["id"]
    return None


def ot_diana(simbolo):
    ens = ot_ensembl(simbolo)
    if not ens:
        return []
    consulta = '{ target(ensemblId: "%s") { drugAndClinicalCandidates { rows { %s } } } }' % (ens, DRUG_OT)
    datos = cacheado("ot_target:" + ens, lambda: graphql(OT, consulta))
    filas = []
    for row in datos["target"]["drugAndClinicalCandidates"]["rows"]:
        d = row["drug"]
        if d["maximumClinicalStage"] != "APPROVAL":
            continue
        acciones = {m["actionType"].lower() for m in mecanismos(d)
                    if any(t["approvedSymbol"] == simbolo for t in (m["targets"] or []))}
        filas.append({"gen": simbolo, "farmaco": normalizar(d["name"]), "acciones": sorted(acciones)})
    return filas


def ot_enfermedad(efo):
    consulta = '{ disease(efoId: "%s") { drugAndClinicalCandidates { rows { maxClinicalStage %s } } } }' % (efo, DRUG_OT)
    datos = cacheado("ot_disease:" + efo, lambda: graphql(OT, consulta))
    filas = []
    for row in datos["disease"]["drugAndClinicalCandidates"]["rows"]:
        d = row["drug"]
        if d["maximumClinicalStage"] != "APPROVAL":
            continue
        dianas = sorted({t["approvedSymbol"] for m in mecanismos(d) for t in (m["targets"] or [])})
        acciones = sorted({m["actionType"].lower() for m in mecanismos(d)})
        filas.append({"farmaco": normalizar(d["name"]), "fase_rms": row["maxClinicalStage"],
                      "dianas": dianas, "acciones": acciones})
    return filas


# ── Aprobacion ────────────────────────────────────────────────────────────────
def fda(farmaco):
    def consultar():
        # Muchos registros no traen openfda.generic_name; el principio activo siempre esta
        consulta = f'openfda.generic_name:"{farmaco}" OR products.active_ingredients.name:"{farmaco}"'
        r = requests.get(OPENFDA, params={"search": consulta, "limit": 100}, timeout=60)
        time.sleep(0.3)
        return r.json() if r.status_code == 200 else {}
    datos = cacheado("fda2:" + farmaco, consultar)
    resultados = datos.get("results", [])
    if not resultados:
        return {"fda": "no", "fda_aplicacion": "", "fda_estado": ""}
    estados = {p.get("marketing_status", "") for x in resultados for p in x.get("products", [])}
    vigente = bool(estados & {"Prescription", "Over-the-counter"})
    nda = sorted(x["application_number"] for x in resultados if x["application_number"].startswith(("NDA", "BLA")))
    return {"fda": "sí", "fda_aplicacion": (nda or [resultados[0]["application_number"]])[0],
            "fda_estado": "comercializado" if vigente else "discontinuado"}


def tabla_ema():
    def bajar():
        r = requests.get(EMA_XLSX, headers={"User-Agent": "Mozilla/5.0"}, timeout=120)
        r.raise_for_status()
        crudo = pd.read_excel(io.BytesIO(r.content), header=None)
        fila = crudo.index[crudo.apply(lambda s: s.astype(str).str.fullmatch("Category").any(), axis=1)][0]
        df = pd.read_excel(io.BytesIO(r.content), header=fila)
        df = df[(df["Category"] == "Human") & (df["Medicine status"] == "Authorised")]
        sustancias = {}
        for _, x in df.iterrows():
            for campo in ("International non-proprietary name (INN) / common name", "Active substance"):
                for s in re.split(r"[,;/]", str(x[campo])):
                    if s.strip() and s.strip().lower() != "nan":
                        sustancias.setdefault(normalizar(s), x["Name of medicine"])
        return sustancias
    return cacheado("ema_xlsx", bajar)


# ── Construccion de la lista ──────────────────────────────────────────────────
def main():
    global USAR_CACHE
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-cache", action="store_true", help="vuelve a consultar todas las APIs")
    USAR_CACHE = not ap.parse_args().sin_cache

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    cand = {}

    def agregar(farmaco, linea, diana, accion, origen, nota="", fase_rms=""):
        c = cand.setdefault(farmaco, {"lineas": set(), "dianas": set(), "acciones": set(),
                                      "origenes": set(), "notas": [], "fase_rms": ""})
        c["lineas"].add(linea)
        if diana:
            c["dianas"].add(diana)
        c["acciones"].update(accion)
        c["origenes"].add(origen)
        if nota and nota not in c["notas"]:
            c["notas"].append(nota)
        if fase_rms:
            c["fase_rms"] = fase_rms

    for linea, info in cfg["lineas"].items():
        for grupo in info.get("grupos", []):
            buscadas = set(grupo["accion"])
            for f in dgidb(grupo["genes"]):
                if f["aprobado_dgidb"] and buscadas & set(f["acciones"]):
                    agregar(f["farmaco"], linea, f["gen"], f["acciones"], "DGIdb", grupo["nota"])
            for gen in grupo["genes"]:
                for f in ot_diana(gen):
                    if buscadas & set(f["acciones"]):
                        agregar(f["farmaco"], linea, gen, f["acciones"], "Open Targets", grupo["nota"])
        if "enfermedad_open_targets" in info:
            for f in ot_enfermedad(info["enfermedad_open_targets"]):
                agregar(f["farmaco"], linea, ",".join(f["dianas"][:3]), f["acciones"], "Open Targets (rabdomiosarcoma)",
                        fase_rms=f["fase_rms"])

    for c in cfg["curados"]:
        agregar(normalizar(c["farmaco"]), c["linea"], c["diana"], [], "curado", f"{c['motivo']} [{c['fuente']}]")

    # F2: farmacos aprobados que inhiben dianas excluidas (auditoria sobre DGIdb)
    inhibe_excluida = {}
    for f in dgidb(cfg["excluir_si_inhibe"]):
        if "inhibitor" in f["acciones"] or "antagonist" in f["acciones"]:
            inhibe_excluida.setdefault(f["farmaco"], set()).add(f["gen"])
    ema = tabla_ema()
    # La marca "approved" de DGIdb es incompleta: se audita con la misma comprobacion FDA/EMA
    for i, (farmaco, genes) in enumerate(sorted(inhibe_excluida.items()), 1):
        print(f"\r  auditoria F2 {i}/{len(inhibe_excluida)}", end="", file=sys.stderr)
        if farmaco not in cand and (fda(farmaco)["fda"] == "sí" or farmaco in ema):
            agregar(farmaco, "auditoria_F2", ",".join(sorted(genes)), ["inhibitor"], "DGIdb (auditoría F2)")
    print(file=sys.stderr)
    antimitotico = {f["farmaco"] for f in dgidb(cfg["precaucion_antimitotico"])}
    estandar = {normalizar(x) for x in cfg["estandar_rms"]}
    soporte = {normalizar(x) for x in cfg["soporte"]}

    filas = []
    for i, (farmaco, c) in enumerate(sorted(cand.items()), 1):
        print(f"\r  aprobacion {i}/{len(cand)}", end="", file=sys.stderr)
        ap_fda = fda(farmaco)
        en_ema = farmaco in ema
        f1 = "pasa" if (ap_fda["fda"] == "sí" or en_ema) else "falla"
        excluidas = sorted(inhibe_excluida.get(farmaco, set()))
        # Un antimitotico solo se tolera como tratamiento del tumor; para el sindrome debilita mas la mitosis
        es_antimitotico = farmaco in antimitotico or any(
            g.strip().startswith(("TUBA", "TUBB")) for d in c["dianas"] for g in re.split(r"[,;]", d))
        antimitotico_fuera = es_antimitotico and "4_tumor" not in c["lineas"]
        f2 = "falla" if (excluidas or antimitotico_fuera) else "pasa"
        motivos = []
        if f1 == "falla":
            motivos.append("F1: sin aprobación en Drugs@FDA ni autorización centralizada EMA")
        if excluidas:
            motivos.append("F2: inhibe " + ",".join(excluidas))
        if antimitotico_fuera:
            motivos.append("F2: antimitótico fuera de la línea del tumor")
        notas = list(c["notas"])
        if es_antimitotico and not antimitotico_fuera:
            notas.append("PRECAUCIÓN: antimitótico")
        if ap_fda["fda_estado"] == "discontinuado" and not en_ema:
            notas.append("F4 por revisar: discontinuado en EE. UU.; comprobar si fue por seguridad")
        if farmaco in estandar:
            categoria = "contexto (tratamiento estándar del rabdomiosarcoma)"
        elif farmaco in soporte:
            categoria = "contexto (soporte o trasplante)"
        else:
            categoria = "candidato"
        filas.append({
            "farmaco": farmaco,
            "categoria": categoria,
            "linea": ";".join(sorted(c["lineas"])),
            "diana": ";".join(sorted(c["dianas"])),
            "accion": ";".join(sorted(c["acciones"])),
            "origen": ";".join(sorted(c["origenes"])),
            "fase_rms": c["fase_rms"],
            "fda": ap_fda["fda"], "fda_aplicacion": ap_fda["fda_aplicacion"], "fda_estado": ap_fda["fda_estado"],
            "ema": f"centralizado ({ema[farmaco]})" if en_ema else "no centralizado",
            "f1": f1, "f2": f2, "f3": "", "f4": "",
            "excluido_por": " | ".join(motivos),
            "k1": "", "k2": "", "k3": "", "k4": "", "k5": "", "k6": "", "puntaje": "",
            "fuentes": "", "quien_puntua": "", "notas": " · ".join(notas),
        })
    print(file=sys.stderr)

    df = pd.DataFrame(filas)
    df["_orden"] = (df["excluido_por"] != "").astype(int) * 2 + (df["categoria"] != "candidato").astype(int)
    df = df.sort_values(["_orden", "linea", "farmaco"]).drop(columns="_orden")
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SALIDA, sep="\t", index=False)

    pasan = df[df["excluido_por"] == ""]
    lista_larga = pasan[pasan["categoria"] == "candidato"]
    print(f"{len(df)} fármacos; {len(pasan)} pasan F1 y F2 ({len(lista_larga)} candidatos, "
          f"{len(pasan) - len(lista_larga)} de contexto); {len(df) - len(pasan)} excluidos")
    print(lista_larga.groupby("linea").size().to_string())
    print(f"Guardado en {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
