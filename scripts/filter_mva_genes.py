"""
Filtra el VCF del paciente MVA para quedarse solo con variantes PASS
en los genes candidatos de MVA (BUB1B, CEP57, TRIP13 y genes SAC relacionados).

Uso:
    python scripts/filter_mva_genes.py

Salida:
    results/variants_mva_genes.tsv   — tabla de variantes filtradas
    results/mva_gene_coords_grch38.json — coordenadas GRCh38 usadas
"""

import gzip
import json
import csv
import requests
from pathlib import Path

VCF = Path("data/raw/WGS_EX2312012_HGWCNDSX7.vcf.gz")
OUT_TSV  = Path("results/variants_mva_genes.tsv")
OUT_JSON = Path("results/mva_gene_coords_grch38.json")
PADDING  = 5000  # bp extra a cada lado del gen

# ── Coordenadas GRCh38 de respaldo (NCBI/Ensembl, sin prefijo 'chr') ─────────
FALLBACK_COORDS = {
    "BUB1B":  ("15", 40_160_984,  40_221_137),  # ENSEMBL GRCh38
    "CEP57":  ("11", 95_789_965,  95_837_070),  # ENSEMBL GRCh38
    "TRIP13": ("5",    892_849,      919_357),  # ENSEMBL GRCh38
    "BUB1":   ("2",  110_143_783, 110_244_769), # NCBI GRCh38
    "MAD1L1": ("7",   1_815_787,   2_233_243),  # ENSEMBL GRCh38
    "MAD2L1": ("4",  120_055_623, 120_067_192), # ENSEMBL GRCh38
}


def fetch_ensembl_coords(gene_name: str) -> tuple[str, int, int] | None:
    url = (
        f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_name}"
        "?content-type=application/json"
    )
    try:
        r = requests.get(url, timeout=10)
        d = r.json()
        return str(d["seq_region_name"]), int(d["start"]), int(d["end"])
    except Exception:
        return None


def get_gene_coords() -> dict[str, tuple[str, int, int]]:
    coords = {}
    for gene in FALLBACK_COORDS:
        result = fetch_ensembl_coords(gene)
        if result:
            coords[gene] = result
            print(f"  {gene}: {result[0]}:{result[1]}-{result[2]}  (Ensembl)")
        else:
            coords[gene] = FALLBACK_COORDS[gene]
            print(f"  {gene}: {FALLBACK_COORDS[gene][0]}:{FALLBACK_COORDS[gene][1]}-{FALLBACK_COORDS[gene][2]}  (fallback)")
    return coords


def build_interval_index(coords: dict) -> dict[str, list]:
    """Construye índice chrom → [(start, end, gene), ...]"""
    index: dict[str, list] = {}
    for gene, (chrom, start, end) in coords.items():
        index.setdefault(chrom, []).append((start - PADDING, end + PADDING, gene))
    return index


def overlaps(pos: int, intervals: list) -> str | None:
    """Devuelve el nombre del gen si pos cae en algún intervalo, None si no."""
    for start, end, gene in intervals:
        if start <= pos <= end:
            return gene
    return None


def parse_genotype(fmt: str, sample: str) -> dict:
    keys = fmt.split(":")
    vals = sample.strip().split(":")
    return dict(zip(keys, vals))


def main():
    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)

    print("Obteniendo coordenadas GRCh38 de genes candidatos MVA...")
    coords = get_gene_coords()
    with open(OUT_JSON, "w") as f:
        json.dump(coords, f, indent=2)

    interval_index = build_interval_index(coords)

    print(f"\nEscaneando VCF: {VCF}")
    hits = []

    with gzip.open(VCF, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.rstrip().split("\t")
            chrom, pos, vid, ref, alt, qual, filt, info, fmt = parts[:9]
            sample = parts[9] if len(parts) > 9 else ""
            pos = int(pos)

            # Solo variantes PASS
            if filt != "PASS":
                continue

            # Solo en intervalos de genes candidatos
            gene = overlaps(pos, interval_index.get(chrom, []))
            if not gene:
                continue

            # Parsear genotipo
            gt_data = parse_genotype(fmt, sample)
            gt  = gt_data.get("GT", ".")
            dp  = gt_data.get("DP", ".")
            gq  = gt_data.get("GQ", ".")
            ad  = gt_data.get("AD", ".")

            # Clasificar tipo de variante
            if len(ref) == 1 and len(alt) == 1:
                var_type = "SNV"
            elif len(ref) > len(alt):
                var_type = "DEL"
            elif len(ref) < len(alt):
                var_type = "INS"
            else:
                var_type = "INDEL"

            # Zygosity
            alleles = gt.replace("|", "/").split("/")
            if alleles[0] == alleles[1] and alleles[0] not in (".", "0"):
                zygosity = "HOM_ALT"
            elif "0" in alleles and len(set(alleles) - {"0"}) == 1:
                zygosity = "HET"
            else:
                zygosity = "OTHER"

            hits.append({
                "gene":     gene,
                "chrom":    chrom,
                "pos":      pos,
                "id":       vid,
                "ref":      ref,
                "alt":      alt,
                "qual":     qual,
                "type":     var_type,
                "zygosity": zygosity,
                "GT":       gt,
                "DP":       dp,
                "GQ":       gq,
                "AD":       ad,
            })

    print(f"\nVariantes PASS en genes candidatos: {len(hits)}")

    # Guardar TSV
    if hits:
        with open(OUT_TSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=hits[0].keys(), delimiter="\t")
            writer.writeheader()
            writer.writerows(hits)
        print(f"Guardado en: {OUT_TSV}")

        # Resumen por gen y zigosidad
        from collections import Counter
        by_gene = Counter(h["gene"] for h in hits)
        by_zyg  = Counter(h["zygosity"] for h in hits)
        print("\nPor gen:")
        for gene, n in by_gene.most_common():
            print(f"  {gene}: {n}")
        print("\nPor zigosidad:")
        for zyg, n in by_zyg.most_common():
            print(f"  {zyg}: {n}")

        hom = [h for h in hits if h["zygosity"] == "HOM_ALT"]
        print(f"\nVariantes HOMOCIGOTAS alternativas: {len(hom)}")
        for h in hom:
            print(f"  {h['gene']}  {h['chrom']}:{h['pos']}  {h['ref']}>{h['alt']}  DP={h['DP']} GQ={h['GQ']}")


if __name__ == "__main__":
    main()
