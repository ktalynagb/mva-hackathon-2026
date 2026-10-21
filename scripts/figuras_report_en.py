"""English figures for the IEEE report (docs/report_track2_en.md), in one command.

- Variant filtering funnel (drawn here).
- BUBR1 with the variants and the mechanism pathway: the same figures as the Spanish
  report, drawn by scripts/figuras_informe.py with English text.

Funnel: Same numbers as Table I of the report and as the
funnel in notebooks/04_priorizacion_gnomad_variante_causante.ipynb (reference run of
21 Oct 2026); they are typed here because the intermediate counts need the patient VCF.

Style: Okabe-Ito palette, as in scripts/figuras_informe.py.
Usage: python scripts/figuras_report_en.py  ->  results/en/*.png
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import figuras_informe

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "results" / "en"

AZUL = "#0072B2"
BERMELLON = "#D55E00"
TINTA = "#1F1F1F"
TINTA_2 = "#555555"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"],
    "font.size": 9,
    "text.color": TINTA,
    "axes.edgecolor": TINTA_2,
    "axes.labelcolor": TINTA_2,
    "xtick.color": TINTA_2,
    "ytick.color": TINTA,
    "savefig.dpi": 300,
})

EMBUDO = [
    ("All variants in the VCF", 5_012_204),
    ("Pass quality filters (PASS)", 4_740_790),
    ("In the 321-gene panel", 24_604),
    ("Rare or absent in gnomAD v4*", 23_242),
    ("Alter the protein (any transcript)", 19),
    ("Alter the protein (MANE Select)", 14),
    ("Genes with a recessive pattern", 1),
]


def figura_embudo():
    fig, ax = plt.subplots(figsize=(6.6, 3.1))
    y = list(range(len(EMBUDO)))[::-1]
    colores = [AZUL] * (len(EMBUDO) - 1) + [BERMELLON]
    ax.barh(y, [n for _, n in EMBUDO], color=colores, height=0.68, edgecolor="white", linewidth=1.5)
    ax.set_yticks(y, [e for e, _ in EMBUDO])
    for yi, (_, n) in zip(y, EMBUDO):
        texto = "1 (BUB1B)" if n == 1 else f"{n:,}"
        ax.text(n * 1.35, yi, texto, va="center", fontsize=8.5,
                fontweight="bold" if n == 1 else "normal", fontstyle="italic" if n == 1 else "normal")
    ax.set_xscale("log")
    ax.set_xlim(0.5, 1e8)
    ax.set_xlabel("Number of variants (log scale)")
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.text(0.01, 0.01, "*Mostly intronic variants missing from the gene-level gnomAD query; removed at the next step.",
             fontsize=7, color=TINTA_2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / "fig_variant_funnel.png"
    fig.savefig(ruta, facecolor="white")
    plt.close(fig)
    return ruta


def figura_genes():
    """Rare protein-altering variants per gene: only BUB1B has two that count in MANE Select.

    Reads results/diagnostico_diferencial_variantes.tsv (written by scripts/diagnostico_diferencial.py;
    not versioned because it holds the patient's positions). The figure shows only gene names,
    gnomAD frequencies and consequences, never positions.
    """
    import pandas as pd

    d = pd.read_csv(RAIZ / "results" / "diagnostico_diferencial_variantes.tsv", sep="\t")
    AUSENTE = 1.5e-7  # posicion en el eje para las variantes ausentes de gnomAD
    d["x"] = d["af"].fillna(AUSENTE)
    cuenta = d[d.cuenta].groupby("gen").size()
    genes = sorted(d.gen.unique(), key=lambda g: (-cuenta.get(g, 0), d[d.gen == g].x.min()))
    y = {g: len(genes) - 1 - i for i, g in enumerate(genes)}

    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    ax.axhspan(y["BUB1B"] - 0.45, y["BUB1B"] + 0.45, color="#F3E3D8", lw=0, zorder=0)
    for v in d.itertuples():
        if v.gen == "BUB1B":
            stop = v.consecuencia_mane == "stop_gained"
            ax.plot(v.x, y[v.gen], marker="s" if stop else "o", ms=8, color=BERMELLON if stop else AZUL,
                    mec="white", mew=1, zorder=3)
        elif v.cuenta:
            ax.plot(v.x, y[v.gen], marker="o", ms=6.5, color="#7A7A7A", mec="white", mew=1, zorder=3)
        else:
            ax.plot(v.x, y[v.gen], marker="o", ms=6.5, mfc="white", mec="#7A7A7A", mew=1.3, zorder=3)
    for g in genes:
        n = cuenta.get(g, 0)
        ax.text(2.2e-1, y[g], f"{n}", va="center", ha="center", fontsize=8.5,
                fontweight="bold" if n == 2 else "normal", color=TINTA if n else TINTA_2)
    ax.text(2.2e-1, len(genes) - 0.2, "count", ha="center", va="bottom", fontsize=7.5, color=TINTA_2)

    ax.axvline(1e-2, color=TINTA_2, lw=0.8, ls=(0, (3, 2)))
    ax.text(1.1e-2, -0.9, "1% cutoff", fontsize=7, color=TINTA_2, va="center")
    ax.set_xscale("log")
    ax.set_xlim(8e-8, 4e-1)
    ax.set_ylim(-1.3, len(genes) - 0.2)
    ax.set_yticks(list(y.values()), [g for g in y], fontstyle="italic")
    ax.set_xticks([AUSENTE, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2], ["absent", "10⁻⁶", "10⁻⁵", "10⁻⁴", "10⁻³", "10⁻²"])
    ax.set_xlabel("Allele frequency in gnomAD v4 (log scale)")
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)
    from matplotlib.lines import Line2D
    leyenda = [
        Line2D([], [], marker="s", ls="", color=BERMELLON, mec="white", ms=7, label="BUB1B allele 1 (stop)"),
        Line2D([], [], marker="o", ls="", color=AZUL, mec="white", ms=7, label="BUB1B allele 2 (missense)"),
        Line2D([], [], marker="o", ls="", color="#7A7A7A", mec="white", ms=6.5, label="alters the protein in MANE"),
        Line2D([], [], marker="o", ls="", mfc="white", mec="#7A7A7A", mew=1.3, ms=6.5,
               label="only in a secondary transcript (removed)"),
    ]
    ax.legend(handles=leyenda, loc="upper center", bbox_to_anchor=(0.45, -0.16), ncol=2, frameon=False, fontsize=7.5)
    fig.tight_layout()
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / "fig_variants_per_gene.png"
    fig.savefig(ruta, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return ruta


def figura_checkpoint():
    """The spindle assembly checkpoint with enough BUBR1 and with too little BUBR1, side by side."""
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.4)
    ax.axis("off")

    def caja(x, y, texto, borde=TINTA_2, fondo="#F2F2F2", peso="normal", lw=1.0):
        ax.add_patch(FancyBboxPatch((x - 2.1, y - 0.42), 4.2, 0.84, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    fc=fondo, ec=borde, lw=lw, zorder=2))
        ax.text(x, y, texto, ha="center", va="center", fontsize=7.8, fontweight=peso, linespacing=1.15, zorder=3)

    def flecha(x, y0, y1, color=TINTA_2):
        ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="-|>", mutation_scale=9, color=color, lw=1.1,
                                     shrinkA=0, shrinkB=0, zorder=1))

    filas = [6.0, 4.75, 3.5, 2.25, 1.0]
    normal = [
        ("A chromosome is not yet attached\nto the spindle", "normal"),
        ("Enough BUBR1 → enough MCC\n(BUBR1 · BUB3 · MAD2 · CDC20)", "normal"),
        ("APC/C–CDC20 stays inhibited\nuntil every chromosome is attached", "normal"),
        ("Anaphase waits:\nsister chromatids separate correctly", "normal"),
        ("Daughter cells with 46 chromosomes", "bold"),
    ]
    paciente = [
        ("A chromosome is not yet attached\nto the spindle", "normal"),
        ("Low BUBR1 → too little MCC\n(allele 1: no protein · allele 2: predicted unstable)", "bold"),
        ("APC/C–CDC20 is released too early", "normal"),
        ("Anaphase starts before all\nchromosomes are attached: missegregation", "normal"),
        ("Some daughter cells with 45 or 47\nchromosomes → mosaic aneuploidy", "bold"),
    ]
    for x, pasos, col in ((2.4, normal, TINTA_2), (7.6, paciente, BERMELLON)):
        for i, ((texto, peso), y) in enumerate(zip(pasos, filas)):
            afectado = col == BERMELLON and i > 0
            caja(x, y, texto, borde=col if afectado else TINTA_2, fondo="#FBEDE5" if afectado else "#F2F2F2",
                 peso=peso, lw=1.4 if afectado else 1.0)
            if i < len(pasos) - 1:
                flecha(x, y - 0.44, filas[i + 1] + 0.44, color=col if afectado else TINTA_2)
    ax.text(2.4, 6.95, "Normal checkpoint", ha="center", fontsize=9.5, fontweight="bold")
    ax.text(7.6, 6.95, "This patient: weak checkpoint", ha="center", fontsize=9.5, fontweight="bold", color=BERMELLON)
    fig.tight_layout()
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / "fig_checkpoint_normal_vs_patient.png"
    fig.savefig(ruta, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return ruta


VERDE = "#009E73"
NARANJA = "#E69F00"
GRIS = "#BDBDBD"

NOMBRES_FARMACOS = {
    "SIROLIMUS": "Sirolimus", "TEMSIROLIMUS": "Temsirolimus", "ARIMOCLOMOL": "Arimoclomol",
    "EVEROLIMUS": "Everolimus", "SODIUM PHENYLBUTYRATE": "Sodium phenylbutyrate", "TRAMETINIB": "Trametinib",
    "SELUMETINIB": "Selumetinib", "CELECOXIB": "Celecoxib", "CRIZOTINIB": "Crizotinib", "DASATINIB": "Dasatinib",
    "BORTEZOMIB": "Bortezomib", "NIACIN": "Niacin",
}
EN_PROPUESTA = {"SIROLIMUS", "ARIMOCLOMOL", "NIACIN"}
ALTERNATIVAS = {"TEMSIROLIMUS", "DASATINIB", "TRAMETINIB", "SELUMETINIB"}


def figura_farmacos():
    """(a) Drug funnel, from the long list to the combination; (b) scores of the best candidates."""
    import pandas as pd
    from matplotlib.patches import Patch

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.6), gridspec_kw={"width_ratios": [1, 1.15]})

    # (a) Embudo: numeros de la seccion II-E y de docs/secciones/03b_lista_larga.md
    etapas = [("Long list", 86, GRIS), ("Approved, do not\nweaken mitosis", 73, GRIS),
              ("Repurposing\ncandidates", 52, GRIS), ("Short list", 5, NARANJA), ("Proposed\ncombination", 3, VERDE)]
    yy = list(range(len(etapas)))[::-1]
    ax1.barh(yy, [n for _, n, _ in etapas], color=[c for _, _, c in etapas], height=0.66, edgecolor="white", lw=1.5)
    ax1.set_yticks(yy, [e for e, _, _ in etapas], fontsize=7.5)
    for yi, (_, n, _) in zip(yy, etapas):
        ax1.text(n + 2, yi, str(n), va="center", fontsize=8, fontweight="bold" if n == 3 else "normal")
    ax1.set_xlim(0, 100)
    ax1.set_xlabel("Number of drugs", fontsize=8)
    ax1.set_title("(a) From 86 drugs to 3", fontsize=9, loc="left")

    # (b) Puntajes
    d = pd.read_csv(RAIZ / "results" / "candidatos_farmacos.tsv", sep="\t")
    d = d[(d.categoria == "candidato") & d.puntaje.notna()]
    top = d.sort_values("puntaje", ascending=False).head(11)
    if "NIACIN" not in set(top.farmaco):
        top = pd.concat([top, d[d.farmaco == "NIACIN"]])
    top = top.iloc[::-1]
    color = [VERDE if f in EN_PROPUESTA else NARANJA if f in ALTERNATIVAS else GRIS for f in top.farmaco]
    ax2.barh(range(len(top)), top.puntaje, color=color, height=0.68, edgecolor="white", lw=1.5)
    ax2.set_yticks(range(len(top)), [NOMBRES_FARMACOS.get(f, f.title()) for f in top.farmaco], fontsize=7.5)
    for yi, p in enumerate(top.puntaje):
        ax2.text(p + 1, yi, f"{p:.1f}", va="center", fontsize=7)
    ax2.set_xlim(0, 100)
    ax2.set_xlabel("Score (0–100)", fontsize=8)
    ax2.set_title("(b) Best-ranked candidates", fontsize=9, loc="left")
    ax2.legend(handles=[Patch(color=VERDE, label="in the combination"),
                        Patch(color=NARANJA, label="alternative or conditional"),
                        Patch(color=GRIS, label="not selected")],
               loc="upper center", bbox_to_anchor=(0.4, -0.18), ncol=3, fontsize=6.5, frameon=False,
               handlelength=1.2, columnspacing=0.8)

    for ax in (ax1, ax2):
        for lado in ("top", "right"):
            ax.spines[lado].set_visible(False)
        ax.tick_params(axis="y", length=0)
        ax.tick_params(axis="x", labelsize=7)
    fig.tight_layout()
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / "fig_drug_selection.png"
    fig.savefig(ruta, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return ruta


def figura_propuesta():
    """Two treatments in parallel: standard care for the current tumor and the continuous combination."""
    from matplotlib.patches import FancyBboxPatch

    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8.6)
    ax.axis("off")

    def caja(x, y, ancho, alto, borde, fondo, lw):
        ax.add_patch(FancyBboxPatch((x, y), ancho, alto, boxstyle="round,pad=0.02,rounding_size=0.15",
                                    fc=fondo, ec=borde, lw=lw, zorder=2))

    caja(0.2, 2.5, 5.6, 5.9, TINTA_2, "#F2F2F2", 1.2)
    ax.text(3.0, 7.75, "Standard care", ha="center", fontsize=10, fontweight="bold")
    ax.text(3.0, 7.15, "current rhabdomyosarcoma", ha="center", fontsize=8, color=TINTA_2)
    ax.text(3.0, 5.1, "Cyclophosphamide continues\nas part of the treatment\nthe patient already receives\n\n"
            "(reduced intensity, as in a\npublished MVA case)", ha="center", va="center", fontsize=8, linespacing=1.3)
    ax.text(3.0, 2.95, "Not a repurposing proposal", ha="center", fontsize=7.5, color=TINTA_2)

    caja(6.3, 2.5, 9.5, 5.9, VERDE, "#E6F4EF", 1.6)
    ax.text(11.05, 7.75, "Our repurposing proposal", ha="center", fontsize=10, fontweight="bold")
    ax.text(11.05, 7.15, "underlying disease · long-term, continuous", ha="center", fontsize=8, color=TINTA_2)
    filas = [("Oral sirolimus", "dampens mTORC1: premature aging,\nmuscle atrophy, growth restriction"),
             ("Arimoclomol", "supports protein folding:\nmore BUBR1 (the cause)"),
             ("Niacin", "NAD⁺–SIRT2 axis: more BUBR1\n(speculative hypothesis)")]
    for i, (farmaco, que) in enumerate(filas):
        y = 6.1 - i * 1.15
        ax.text(6.7, y, farmaco, fontsize=9, fontweight="bold", va="center")
        ax.text(9.5, y, que, fontsize=7.5, va="center", linespacing=1.15)
    ax.text(11.05, 2.85, "Could indirectly lower the risk of new tumors (hypothesis)", ha="center", fontsize=7,
            color=TINTA_2, style="italic")

    caja(0.2, 0.2, 15.6, 1.9, TINTA_2, "white", 0.9)
    ax.text(0.55, 1.5, "Validation:", fontsize=8, fontweight="bold", va="center")
    ax.text(2.6, 1.5, "patient fibroblasts before and after each drug → BUBR1 level (Western blot)\n"
            "and checkpoint strength (mitotic arrest with nocodazole)", fontsize=7.5, va="center", linespacing=1.2)
    ax.text(0.55, 0.75, "Surveillance:", fontsize=8, fontweight="bold", va="center")
    ax.text(2.6, 0.75, "periodic blood counts · MRI for the LZTR1 finding",
            fontsize=7.5, va="center")
    fig.tight_layout()
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / "fig_proposal.png"
    fig.savefig(ruta, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return ruta


if __name__ == "__main__":
    print(figura_embudo())
    print(figura_genes())
    print(figura_checkpoint())
    print(figura_farmacos())
    print(figura_propuesta())
    print(figuras_informe.figura_1("en"))
    print(figuras_informe.figura_2("en"))
