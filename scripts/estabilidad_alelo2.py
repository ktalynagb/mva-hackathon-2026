"""Efecto de p.Asn1002Lys en la estabilidad de BUBR1 (ΔΔG) con ThermoMPNN.

ThermoMPNN (Dieckhaus et al. 2024, PNAS 121:e2314853121) predice el cambio de estabilidad ΔΔG (kcal/mol)
de cada sustitucion de aminoacido a partir de la estructura. Convencion: POSITIVO = DESESTABILIZA,
NEGATIVO = ESTABILIZA (se verifica con controles en este script).

Paso 1 (fuera de este script; entorno aparte con PyTorch):
    git clone https://github.com/Kuhlman-Lab/ThermoMPNN.git   # version usada: ver results/estabilidad_alelo2.json
    # descargar el modelo de AlphaFold de O60566 (AF_full.pdb) y su recorte 766-1050 (AF_kinase_766_1050.pdb)
    python analysis/custom_inference.py --pdb AF_full.pdb --chain A --out_dir OUT
    python analysis/custom_inference.py --pdb AF_kinase_766_1050.pdb --chain A --out_dir OUT
Paso 2 (este script):
    python scripts/estabilidad_alelo2.py --dir OUT
Escribe results/estabilidad_alelo2.json. No usa datos del paciente.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from scipy.spatial import cKDTree
from scipy.stats import pearsonr, spearmanr

UNIPROT = "O60566"
DOMINIO = (766, 1050)
OUT = Path(__file__).resolve().parent.parent / "results" / "estabilidad_alelo2.json"
MAX_ASA = {"ALA": 129, "ARG": 274, "ASN": 195, "ASP": 193, "CYS": 167, "GLN": 225, "GLU": 223, "GLY": 104,
           "HIS": 224, "ILE": 197, "LEU": 201, "LYS": 236, "MET": 224, "PHE": 240, "PRO": 159, "SER": 155,
           "THR": 172, "TRP": 285, "TYR": 263, "VAL": 174}


def cargar(csv, offset):
    """Lee una salida de ThermoMPNN. La columna 'position' es el indice 0-based dentro de la secuencia del PDB."""
    df = pd.read_csv(csv)
    df["res"] = df["position"].astype(int) + offset
    df["ddg"] = pd.to_numeric(df["ddG_pred"])
    return df


def rsa_por_residuo():
    info = requests.get(f"https://alphafold.ebi.ac.uk/api/prediction/{UNIPROT}", timeout=60).json()[0]
    atomos = []
    for l in requests.get(info["pdbUrl"], timeout=120).text.splitlines():
        if l.startswith("ATOM"):
            atomos.append((int(l[22:26]), l[76:78].strip() or l[12:16].strip()[0], l[17:20],
                           np.array([float(l[30:38]), float(l[38:46]), float(l[46:54])])))
    X = np.array([a[3] for a in atomos])
    R = np.array([{"C": 1.7, "N": 1.55, "O": 1.52, "S": 1.8}.get(a[1], 1.7) for a in atomos])
    rid = np.array([a[0] for a in atomos])
    aa = {a[0]: a[2] for a in atomos}
    i = np.arange(200) + 0.5
    fi, th = np.arccos(1 - 2 * i / 200), np.pi * (1 + 5 ** 0.5) * i
    esfera = np.c_[np.cos(th) * np.sin(fi), np.sin(th) * np.sin(fi), np.cos(fi)]
    arbol, sasa = cKDTree(X), np.zeros(len(X))
    for k in range(len(X)):
        rr = R[k] + 1.4
        pts = X[k] + rr * esfera
        vec = [j for j in arbol.query_ball_point(X[k], rr + R.max() + 1.4) if j != k]
        libre = (np.linalg.norm(pts[:, None, :] - X[vec][None, :, :], axis=2) >= (R[vec] + 1.4)[None, :]).all(axis=1) \
            if vec else np.ones(200, bool)
        sasa[k] = 4 * np.pi * rr ** 2 * libre.mean()
    return {r: float(sasa[rid == r].sum() / MAX_ASA[aa[r]]) for r in aa}


def main(carpeta):
    carpeta = Path(carpeta)
    seq = requests.get(f"https://rest.uniprot.org/uniprotkb/{UNIPROT}.fasta", timeout=60).text.split("\n", 1)[1].replace("\n", "")
    completo = cargar(carpeta / "ThermoMPNN_inference_AF_full.csv", 1)
    dominio = cargar(carpeta / "ThermoMPNN_inference_AF_kinase_766_1050.csv", DOMINIO[0])

    # Controles de integridad: numeracion, identidad y signo
    for nombre, df in (("completo", completo), ("dominio", dominio)):
        malos = sum(seq[r - 1] != w for r, w in zip(df["res"], df["wildtype"]))
        assert malos == 0, f"{nombre}: {malos} residuos no coinciden con UniProt (numeracion incorrecta)"
        ident = df[df["wildtype"] == df["mutation"]]["ddg"].abs().max()
        assert ident < 1e-6, f"{nombre}: la sustitucion por el mismo aminoacido no da 0"

    sust = completo[(completo["wildtype"] != completo["mutation"]) & (completo["res"] >= DOMINIO[0])].copy()
    rsa = rsa_por_residuo()
    sust["rsa"] = sust["res"].map(rsa)
    por_destino = sust.groupby("mutation")["ddg"].mean().sort_values(ascending=False)
    nucleo = sust[(sust["rsa"] < 0.05) & sust["wildtype"].isin(list("AILMFVW"))]
    expuestos = sust[sust["rsa"] > 0.5]
    controles = {
        "ddg_medio_a_prolina": float(por_destino["P"]), "ddg_medio_a_alanina": float(por_destino["A"]),
        "nucleo_hidrofobico_ddg_medio_a_D_K_P_G": float(nucleo[nucleo["mutation"].isin(list("DKPG"))]["ddg"].mean()),
        "expuestos_ddg_medio": float(expuestos["ddg"].mean()),
        "n_posiciones_nucleo": int(nucleo["res"].nunique()), "n_posiciones_expuestas": int(expuestos["res"].nunique()),
    }
    assert controles["ddg_medio_a_prolina"] > controles["ddg_medio_a_alanina"], "signo invertido: revisar convencion"
    assert controles["nucleo_hidrofobico_ddg_medio_a_D_K_P_G"] > controles["expuestos_ddg_medio"], "signo invertido"

    def resumen(df, res, mut):
        todas = df[(df["wildtype"] != df["mutation"]) & (df["res"] >= DOMINIO[0])]["ddg"].values
        x = float(df[(df["res"] == res) & (df["mutation"] == mut)]["ddg"].iloc[0])
        return {"ddg": round(x, 2), "percentil_en_dominio": round(float(100 * np.mean(todas <= x)), 1)}

    en_1002 = completo[(completo["res"] == 1002) & (completo["wildtype"] != completo["mutation"])].sort_values("ddg", ascending=False)
    m = completo.merge(dominio, on=["res", "mutation"], suffixes=("_c", "_d"))
    m = m[m["wildtype_c"] != m["mutation"]]
    salida = {
        "herramienta": "ThermoMPNN (modelo thermoMPNN_default.pt)", "convencion": "positivo = desestabiliza (kcal/mol)",
        "estructura": "AlphaFold DB AF-O60566-F1",
        "N1002K": {"modelo_completo": resumen(completo, 1002, "K"), "modelo_dominio": resumen(dominio, 1002, "K")},
        "L1012P_MVA1_conocida": {"modelo_completo": resumen(completo, 1012, "P"), "modelo_dominio": resumen(dominio, 1012, "P")},
        "posicion_1002_todas_las_sustituciones": {r.mutation: round(float(r.ddg), 2) for r in en_1002.itertuples()},
        "coherencia_completo_vs_dominio": {"n": int(len(m)), "spearman": round(float(spearmanr(m["ddg_c"], m["ddg_d"])[0]), 3),
                                           "pearson": round(float(pearsonr(m["ddg_c"], m["ddg_d"])[0]), 3),
                                           "diferencia_media_abs": round(float((m["ddg_c"] - m["ddg_d"]).abs().mean()), 2)},
        "controles": {k: (round(v, 2) if isinstance(v, float) else v) for k, v in controles.items()},
        "ddg_medio_por_aminoacido_destino": {k: round(float(v), 2) for k, v in por_destino.items()},
    }
    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Guardado:", OUT)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="carpeta con las dos salidas CSV de ThermoMPNN")
    main(ap.parse_args().dir)
