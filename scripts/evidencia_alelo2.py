"""Evidencia adicional para p.Asn1002Lys (BUB1B, UniProt O60566, residuo 1002).

Consulta tres fuentes publicas y guarda un resumen en results/evidencia_alelo2.json:
  1. ClinVar (NCBI E-utilities): clasificaciones de los cambios de aminoacido de BUB1B.
  2. AlphaFold DB: confianza (pLDDT), vecinos y enlaces de hidrogeno alrededor del residuo.
  3. UniProt: conservacion del residuo en ortologos de vertebrados.

Uso:  python scripts/evidencia_alelo2.py
No usa datos del paciente: solo bases publicas.
"""
import json
import re
import tempfile
import time
from pathlib import Path

import numpy as np
import requests

RESIDUO = 1002
UNIPROT = "O60566"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
ORTOLOGOS = {"Bos taurus": 9913, "Gallus gallus": 9031, "Xenopus laevis": 8355,
             "Xenopus tropicalis": 8364, "Rattus norvegicus": 10116,
             "Canis lupus familiaris": 9615, "Mus musculus": 10090}
OUT = Path(__file__).resolve().parent.parent / "results" / "evidencia_alelo2.json"


def get(url, **params):
    for _ in range(3):
        try:
            r = requests.get(url, params=params, timeout=60)
            if r.status_code == 200:
                return r
        except requests.RequestException:
            pass
        time.sleep(2)
    raise RuntimeError(f"fallo al consultar {url}")


def clinvar():
    base = dict(db="clinvar", term="BUB1B[gene]", retmode="json")
    n = int(get(EUTILS + "esearch.fcgi", retmax=0, **base).json()["esearchresult"]["count"])
    ids = []
    for ini in range(0, n, 500):
        ids += get(EUTILS + "esearch.fcgi", retstart=ini, retmax=500, **base).json()["esearchresult"]["idlist"]
    filas = []
    for i in range(0, len(ids), 100):
        s = get(EUTILS + "esummary.fcgi", db="clinvar", id=",".join(ids[i:i + 100]), retmode="json").json()["result"]
        for k in s.get("uids", []):
            g = s[k].get("germline_classification", {})
            filas.append((s[k].get("title", ""), g.get("description"), g.get("review_status")))
    pat = re.compile(r"p\.([A-Za-z]{3})(\d+)([A-Za-z]{3}|=|\*)")
    patogenicos, vecinos = [], []
    for titulo, clase, revision in filas:
        m = pat.search(titulo)
        if not m or m.group(3) in ("Ter", "*"):
            continue
        pos = int(m.group(2))
        if clase and "athogenic" in clase and "onflicting" not in clase and m.group(3) != "=":
            patogenicos.append({"cambio": titulo, "clase": clase, "revision": revision})
        if RESIDUO - 6 <= pos <= RESIDUO + 6 and m.group(3) != "=":
            vecinos.append({"cambio": titulo, "clase": clase})
    return {"registros_totales": n, "cambios_aa_patogenicos_o_prob_patogenicos": patogenicos,
            "cambios_aa_en_ventana_1002_mas_menos_6": vecinos}


def alphafold():
    info = get(f"https://alphafold.ebi.ac.uk/api/prediction/{UNIPROT}").json()[0]
    pdb = get(info["pdbUrl"]).text
    res = {}
    for linea in pdb.splitlines():
        if linea.startswith("ATOM"):
            r = int(linea[22:26])
            e = res.setdefault(r, {"aa": linea[17:20], "atomos": {}, "b": float(linea[60:66])})
            e["atomos"][linea[12:16].strip()] = np.array([float(linea[30:38]), float(linea[38:46]), float(linea[46:54])])

    def cb(r):
        a = res[r]["atomos"]
        return a.get("CB", a["CA"])

    dominio = range(766, 1051)
    vecinos10 = lambda r: sum(1 for q in dominio if q != r and np.linalg.norm(cb(q) - cb(r)) <= 10)
    cuentas = [vecinos10(r) for r in dominio]
    mio = vecinos10(RESIDUO)
    cerca8 = sorted((round(float(np.linalg.norm(cb(r) - cb(RESIDUO))), 1), r, res[r]["aa"])
                    for r in res if r != RESIDUO and np.linalg.norm(cb(r) - cb(RESIDUO)) <= 8)
    puentes = set()
    for r in res:
        if abs(r - RESIDUO) <= 1:
            continue
        for n, p in res[r]["atomos"].items():
            for m, q in res[RESIDUO]["atomos"].items():
                if n[0] in "NO" and m[0] in "NO" and np.linalg.norm(p - q) <= 3.5:
                    puentes.add((r, res[r]["aa"], n, m))
    return {"version_modelo": info.get("latestVersion"),
            "plddt_residuo": res[RESIDUO]["b"],
            "plddt_medio_dominio_quinasa": float(np.mean([res[r]["b"] for r in dominio])),
            "vecinos_cb_10A": mio, "vecinos_cb_10A_media_dominio": float(np.mean(cuentas)),
            "percentil_enterramiento": float(100 * np.mean(np.array(cuentas) <= mio)),
            "residuos_a_8A": cerca8,
            "enlaces_N_O_a_3_5A": [list(map(str, x)) for x in sorted(puentes)]}


def alinear(a, b, hueco=-8):
    n, m = len(a), len(b)
    S = np.zeros((n + 1, m + 1), dtype=np.int32)
    T = np.zeros((n + 1, m + 1), dtype=np.int8)
    S[:, 0] = np.arange(n + 1) * hueco
    S[0, :] = np.arange(m + 1) * hueco
    T[1:, 0], T[0, 1:] = 1, 2
    A, B = np.frombuffer(a.encode(), np.uint8), np.frombuffer(b.encode(), np.uint8)
    for i in range(1, n + 1):
        diag = S[i - 1, :-1] + np.where(B == A[i - 1], 5, -2)
        for j in range(1, m + 1):
            arriba, izq, dg = S[i - 1, j] + hueco, S[i, j - 1] + hueco, diag[j - 1]
            mejor = max(dg, arriba, izq)
            S[i, j], T[i, j] = mejor, 0 if mejor == dg else (1 if mejor == arriba else 2)
    i, j, mapa = n, m, {}
    while i > 0 and j > 0:
        if T[i, j] == 0:
            mapa[i], i, j = j, i - 1, j - 1
        elif T[i, j] == 1:
            i -= 1
        else:
            j -= 1
    return mapa


def conservacion():
    humano = get(f"https://rest.uniprot.org/uniprotkb/{UNIPROT}.fasta").text.split("\n", 1)[1].replace("\n", "")
    filas = []
    for nombre, taxid in ORTOLOGOS.items():
        r = get("https://rest.uniprot.org/uniprotkb/search",
                query=f"(gene:bub1b OR gene:BUB1B OR gene:bubr1) AND organism_id:{taxid}",
                fields="accession,sequence,length", format="json", size=5).json()["results"]
        r = [x for x in r if 950 <= x["sequence"]["length"] <= 1250]
        if not r:
            continue
        seq = r[0]["sequence"]["value"]
        mapa = alinear(humano, seq)
        en = lambda p: seq[mapa[p] - 1] if p in mapa else "-"
        ident = sum(1 for p in range(766, 1051) if en(p) == humano[p - 1]) / 285
        filas.append({"especie": nombre, "acceso": r[0]["primaryAccession"], "residuo": en(RESIDUO),
                      "ventana_996_1008": "".join(en(p) for p in range(996, 1009)),
                      "identidad_dominio_quinasa": round(ident, 2)})
    return {"humano_996_1008": humano[995:1008], "especies": filas,
            "residuo_conservado_en": f"{sum(f['residuo'] == humano[RESIDUO - 1] for f in filas)} de {len(filas)}"}


if __name__ == "__main__":
    salida = {"residuo": f"p.Asn{RESIDUO}Lys", "uniprot": UNIPROT,
              "clinvar": clinvar(), "alphafold": alphafold(), "conservacion": conservacion()}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False, default=float) + "\n", encoding="utf-8")
    print("Guardado:", OUT)
