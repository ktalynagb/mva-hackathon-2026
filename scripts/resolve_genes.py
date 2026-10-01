"""
Traduce la lista de genes de config/genes_candidatos.txt a coordenadas GRCh38
usando la API de MyGene.info. Resuelve símbolos desactualizados (ej. ZNF828 → CHAMP1).

Uso:
    python scripts/resolve_genes.py

Salida:
    results/genes_candidatos_grch38.tsv
"""

import requests
import pandas as pd
from pathlib import Path

CONFIG  = Path("config/genes_candidatos.txt")
OUT_TSV = Path("results/genes_candidatos_grch38.tsv")
MYGENE  = "https://mygene.info/v3/querymany"

CATEGORIA_MAP = {
    "BUB1B": "SAC", "BUB1": "SAC", "BUB3": "SAC", "MAD1L1": "SAC", "MAD2L1": "SAC",
    "MAD2L2": "SAC", "CDC20": "SAC", "TRIP13": "SAC", "ESPL1": "SAC", "PTTG1": "SAC",
}


def load_gene_list() -> list[str]:
    genes = []
    for line in CONFIG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        symbol = line.split()[0]
        genes.append(symbol)
    return genes


def query_mygene(symbols: list[str]) -> pd.DataFrame:
    batch_size = 100
    rows = []
    for i in range(0, len(symbols), batch_size):
        batch = symbols[i:i + batch_size]
        resp = requests.post(
            MYGENE,
            data={
                "q":       ",".join(batch),
                "scopes":  "symbol,alias",
                "species": "human",
                "fields":  "symbol,genomic_pos_hg38,name",
                "dotfield": True,
            },
            timeout=30,
        ).json()
        for item in resp:
            query = item.get("query", "")
            if item.get("notfound"):
                print(f"  ⚠️  No encontrado: {query}")
                rows.append({"consulta": query, "simbolo": None, "chrom": None,
                             "start": None, "end": None, "nombre": None})
                continue
            pos = item.get("genomic_pos_hg38")
            if isinstance(pos, list):
                pos = pos[0]
            if not pos:
                print(f"  ⚠️  Sin coordenadas GRCh38: {query}")
                rows.append({"consulta": query, "simbolo": item.get("symbol"),
                             "chrom": None, "start": None, "end": None,
                             "nombre": item.get("name")})
                continue
            rows.append({
                "consulta": query,
                "simbolo":  item.get("symbol", query),
                "chrom":    str(pos["chr"]),
                "start":    int(pos["start"]),
                "end":      int(pos["end"]),
                "nombre":   item.get("name", ""),
            })
    return pd.DataFrame(rows)


def main():
    genes = load_gene_list()
    print(f"Genes en la lista: {len(genes)}")

    df = query_mygene(genes)

    # Agregar categoría
    df["categoria"] = df["consulta"].map(CATEGORIA_MAP).fillna("otro")

    resolved = df[df.chrom.notna()]
    print(f"Resueltos con coordenadas: {len(resolved)} / {len(genes)}")

    OUT_TSV.parent.mkdir(exist_ok=True)
    df.to_csv(OUT_TSV, sep="\t", index=False)
    print(f"Guardado en {OUT_TSV}")

    if len(df[df.chrom.isna()]) > 0:
        print("\nNo resueltos:")
        for _, r in df[df.chrom.isna()].iterrows():
            print(f"  {r['consulta']}")


if __name__ == "__main__":
    main()
