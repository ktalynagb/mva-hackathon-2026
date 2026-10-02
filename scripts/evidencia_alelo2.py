"""Evidencia adicional para p.Asn1002Lys (BUB1B, UniProt O60566, residuo 1002).

Consulta fuentes publicas y guarda un resumen en results/evidencia_alelo2.json:
  1. ClinVar (NCBI E-utilities): clasificaciones de los cambios de aminoacido de BUB1B.
  2. AlphaFold DB: confianza (pLDDT), vecinos y enlaces de hidrogeno alrededor del residuo.
  3. UniProt: conservacion del residuo en ortologos de vertebrados.
  4. UniProt y AlphaFold: sitios de glicosilacion, variante de MVA1 cercana (L1012P) y
     estructura local (accesibilidad al solvente, estructura secundaria, distancias).
  5. AlphaFill: posicion del ATP/ADP en el modelo (transplantado desde estructuras homologas) y distancia
     al residuo.

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
from scipy.spatial import cKDTree

RESIDUO = 1002
DOMINIO_QUINASA = (766, 1050)
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


MAX_ASA = {"ALA": 129, "ARG": 274, "ASN": 195, "ASP": 193, "CYS": 167, "GLN": 225, "GLU": 223, "GLY": 104,
           "HIS": 224, "ILE": 197, "LEU": 201, "LYS": 236, "MET": 224, "PHE": 240, "PRO": 159, "SER": 155,
           "THR": 172, "TRP": 285, "TYR": 263, "VAL": 174}
RADIOS = {"C": 1.7, "N": 1.55, "O": 1.52, "S": 1.8}


def diedro(p0, p1, p2, p3):
    b0, b1, b2 = p0 - p1, p2 - p1, p3 - p2
    b1 = b1 / np.linalg.norm(b1)
    v, w = b0 - np.dot(b0, b1) * b1, b2 - np.dot(b2, b1) * b1
    return float(np.degrees(np.arctan2(np.dot(np.cross(b1, v), w), np.dot(v, w))))


def uniprot_y_estructura():
    u = get(f"https://rest.uniprot.org/uniprotkb/{UNIPROT}.json").json()
    seq = u["sequence"]["value"]
    rasgos = []
    for f in u["features"]:
        a, b = f["location"]["start"]["value"], f["location"]["end"]["value"]
        if f["type"] in ("Glycosylation", "Modified residue", "Natural variant", "Active site", "Binding site")                 and (f["type"] in ("Glycosylation", "Natural variant") or 985 <= a <= 1020 or f["type"] != "Modified residue"):
            if f["type"] in ("Glycosylation",) or 985 <= a <= 1020 or f["type"] in ("Active site", "Binding site"):
                rasgos.append({"tipo": f["type"], "inicio": a, "fin": b, "descripcion": f.get("description", "")})
    sequones = [m.start() + 1 for m in re.finditer(r"(?=N[^P][ST])", seq)]

    info = get(f"https://alphafold.ebi.ac.uk/api/prediction/{UNIPROT}").json()[0]
    atomos, res = [], {}
    for l in get(info["pdbUrl"]).text.splitlines():
        if l.startswith("ATOM"):
            r, n = int(l[22:26]), l[12:16].strip()
            xyz = np.array([float(l[30:38]), float(l[38:46]), float(l[46:54])])
            atomos.append((r, l[76:78].strip() or n[0], xyz))
            res.setdefault(r, {"aa": l[17:20], "at": {}})["at"][n] = xyz
    X = np.array([a[2] for a in atomos])
    R = np.array([RADIOS.get(a[1], 1.7) for a in atomos])
    rid = np.array([a[0] for a in atomos])
    i = np.arange(200) + 0.5
    fi, th = np.arccos(1 - 2 * i / 200), np.pi * (1 + 5 ** 0.5) * i
    esfera = np.c_[np.cos(th) * np.sin(fi), np.sin(th) * np.sin(fi), np.cos(fi)]
    arbol, sasa = cKDTree(X), np.zeros(len(X))
    for k in range(len(X)):
        rr = R[k] + 1.4
        pts = X[k] + rr * esfera
        vec = [j for j in arbol.query_ball_point(X[k], rr + R.max() + 1.4) if j != k]
        libre = (np.linalg.norm(pts[:, None, :] - X[vec][None, :, :], axis=2) >= (R[vec] + 1.4)[None, :]).all(axis=1)             if vec else np.ones(200, bool)
        sasa[k] = 4 * np.pi * rr ** 2 * libre.mean()
    rsa = lambda r: float(sasa[rid == r].sum() / MAX_ASA[res[r]["aa"]])
    dominio = [rsa(r) for r in range(766, 1051)]

    def fipsi(r):
        a = res
        return (diedro(a[r - 1]["at"]["C"], a[r]["at"]["N"], a[r]["at"]["CA"], a[r]["at"]["C"]),
                diedro(a[r]["at"]["N"], a[r]["at"]["CA"], a[r]["at"]["C"], a[r + 1]["at"]["N"]))

    def clase(fp):
        f, p = fp
        if -110 <= f <= -30 and -80 <= p <= -5:
            return "helice"
        return "hoja" if f < -45 and (p > 90 or p < -150) else "bucle"

    lado = [v for k, v in res[RESIDUO]["at"].items() if k not in ("N", "CA", "C", "O")]
    sitio_atp = list(range(772, 781)) + [795]
    d_atp = min(float(np.linalg.norm(res[r]["at"][k] - s)) for r in sitio_atp for k in res[r]["at"] for s in lado)
    ca = res[RESIDUO]["at"]["CA"]
    cargados = sorted((round(float(np.linalg.norm(res[r]["at"]["CA"] - ca)), 1), r, res[r]["aa"])
                      for r in res if r != RESIDUO and res[r]["aa"] in ("ASP", "GLU", "LYS", "ARG")
                      and np.linalg.norm(res[r]["at"]["CA"] - ca) <= 10)
    d1012 = float(np.linalg.norm(res[1012]["at"]["CA"] - ca))
    return {"uniprot": {"rasgos_relevantes": rasgos, "sequones_N_glicosilacion": sequones,
                        "residuo_es_sequon": (seq[RESIDUO] not in "P" and seq[RESIDUO + 1] in "ST"),
                        "contexto_996_1008": seq[995:1008]},
            "estructura": {"rsa_residuo": rsa(RESIDUO), "rsa_mediana_dominio_quinasa": float(np.median(dominio)),
                           "percentil_rsa": float(100 * np.mean(np.array(dominio) <= rsa(RESIDUO))),
                           "rsa_996_1008": {str(r): round(rsa(r), 2) for r in range(996, 1009)},
                           "fi_psi_residuo": [round(x) for x in fipsi(RESIDUO)],
                           "clase_996_1008": {str(r): clase(fipsi(r)) for r in range(996, 1009)},
                           "distancia_minima_a_sitio_ATP_A": round(d_atp, 1),
                           "cargados_a_10A_CA": cargados,
                           "L1012_MVA1": {"distancia_CA_A": round(d1012, 1), "rsa": round(rsa(1012), 2),
                                          "clase": clase(fipsi(1012))}}}


def bolsillo_atp():
    """Distancia del residuo al bolsillo de ATP, usando los nucleotidos que AlphaFill transplanta al modelo."""
    resumen = get(f"https://alphafill.eu/v1/aff/{UNIPROT}/json").json()
    lineas = get(f"https://alphafill.eu/v1/aff/{UNIPROT}").text.splitlines()
    i = next(k for k, l in enumerate(lineas) if l.startswith("_atom_site.group_PDB"))
    cols = []
    while lineas[i].startswith("_atom_site."):
        cols.append(lineas[i].split(".")[1].strip())
        i += 1
    ix = {c: n for n, c in enumerate(cols)}
    atomos = []
    while i < len(lineas) and not lineas[i].startswith("#"):
        p = lineas[i].split()
        if len(p) >= len(cols):
            atomos.append(p)
        i += 1
    xyz = lambda a: np.array([float(a[ix["Cartn_x"]]), float(a[ix["Cartn_y"]]), float(a[ix["Cartn_z"]])])
    resid = lambda a: int(a[ix["auth_seq_id"]])
    prot = [a for a in atomos if a[ix["group_PDB"]] == "ATOM"]
    objetivo = [a for a in prot if resid(a) == RESIDUO]
    assert objetivo and objetivo[0][ix["label_comp_id"]] == "ASN", "el residuo no es ASN en el modelo de AlphaFill"
    lateral = [xyz(a) for a in objetivo if a[ix["label_atom_id"]] not in ("N", "CA", "C", "O")]
    ca = [xyz(a) for a in objetivo if a[ix["label_atom_id"]] == "CA"][0]
    nucleotidos = {"ADP", "ANP", "ATP", "AMP", "ACP", "AGS", "APC"}
    grupos = {}
    for a in atomos:
        if a[ix["group_PDB"]] == "HETATM" and a[ix["label_comp_id"]] in nucleotidos:
            grupos.setdefault((a[ix["label_comp_id"]], a[ix["label_asym_id"]]), []).append(a)
    colocaciones, pocket = [], set()
    for (comp, asym), L in grupos.items():
        P = np.array([xyz(a) for a in L])
        contacto = {resid(a) for a in prot if np.linalg.norm(P - xyz(a), axis=1).min() <= 4.5}
        pocket |= contacto
        colocaciones.append({"nucleotido": comp,
                             "distancia_min_cadena_lateral_A": round(min(float(np.linalg.norm(P - s_, axis=1).min()) for s_ in lateral), 1),
                             "distancia_CA_a_centro_nucleotido_A": round(float(np.linalg.norm(ca - P.mean(axis=0))), 1),
                             "residuo_en_contacto": RESIDUO in contacto})
    # el modelo base de AlphaFill puede ser una version distinta de AlphaFold: se comprueba que sea equivalente
    v6 = {}
    info = get(f"https://alphafold.ebi.ac.uk/api/prediction/{UNIPROT}").json()[0]
    for l in get(info["pdbUrl"]).text.splitlines():
        if l.startswith("ATOM") and l[12:16].strip() == "CA":
            v6[int(l[22:26])] = np.array([float(l[30:38]), float(l[38:46]), float(l[46:54])])
    v4 = {resid(a): xyz(a) for a in prot if a[ix["label_atom_id"]] == "CA"}
    comunes = [r for r in range(DOMINIO_QUINASA[0], DOMINIO_QUINASA[1] + 1) if r in v4 and r in v6]
    A, B = np.array([v4[r] for r in comunes]), np.array([v6[r] for r in comunes])
    Ac, Bc = A - A.mean(0), B - B.mean(0)
    U, _, Vt = np.linalg.svd(Bc.T @ Ac)
    if np.linalg.det(U @ Vt) < 0:
        U[:, -1] *= -1
    rmsd = float(np.sqrt(((Bc @ (U @ Vt) - Ac) ** 2).sum(1).mean()))
    return {"alphafill": {"version": resumen["alphafill_version"], "modelo_base": resumen["file"].split("/")[-1]},
            "colocaciones_de_nucleotido": colocaciones,
            "residuos_en_contacto_con_el_nucleotido": sorted(pocket),
            "rmsd_CA_dominio_modelo_alphafill_vs_modelo_usado_A": round(rmsd, 2),
            "nota": "posiciones aproximadas: transplantadas por homologia (identidad 25-28 %), con choques estericos"}


if __name__ == "__main__":
    salida = {"residuo": f"p.Asn{RESIDUO}Lys", "uniprot": UNIPROT,
              "clinvar": clinvar(), "alphafold": alphafold(), "conservacion": conservacion(),
              **uniprot_y_estructura(), "bolsillo_atp": bolsillo_atp()}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False, default=float) + "\n", encoding="utf-8")
    print("Guardado:", OUT)
