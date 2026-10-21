"""Support figures for the 3-minute video (tasks E4/E6), in English.

They complement the report figures (results/en/fig_*.png) with what the video has to
tell and the report shows only in tables: the case, the whole method, the drug funnel,
the scores and the final proposal. 16:9 format with large text so they read on screen.

Style: same Okabe-Ito palette as scripts/figuras_informe.py.
Data: results/candidatos_farmacos.tsv and the numbers in docs/report_track2_en.md.
Usage: python scripts/figuras_video.py  ->  results/video/*.png
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "results" / "video"

ALELO1 = "#D55E00"
ALELO2 = "#0072B2"
FARMACO = "#009E73"
ALTERNATIVA = "#E69F00"
GRIS = "#BDBDBD"
TINTA = "#1F1F1F"
TINTA_2 = "#555555"
FONDO_CAJA = "#F2F2F2"
FONDO_VERDE = "#E6F4EF"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"],
    "font.size": 14,
    "text.color": TINTA,
    "axes.edgecolor": TINTA_2,
    "axes.labelcolor": TINTA_2,
    "xtick.color": TINTA_2,
    "ytick.color": TINTA,
    "savefig.dpi": 150,
})

TAM = (13.33, 7.5)  # 16:9 -> 2000 x 1125 px a 150 ppp


def lienzo():
    fig, ax = plt.subplots(figsize=TAM)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    return fig, ax


def caja(ax, x, y, ancho, alto, borde=TINTA_2, fondo=FONDO_CAJA, lw=1.5):
    ax.add_patch(FancyBboxPatch((x, y), ancho, alto, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fondo, ec=borde, lw=lw, zorder=2))


def flecha(ax, a, b, color=TINTA_2, lw=2.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=22, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0, zorder=1))


def titulo(ax, texto, sub=None):
    ax.text(0.3, 8.55, texto, fontsize=24, fontweight="bold", va="top")
    if sub:
        ax.text(0.3, 7.85, sub, fontsize=14, color=TINTA_2, va="top")


def guardar(fig, nombre):
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / nombre
    fig.savefig(ruta, facecolor="white")
    plt.close(fig)
    return ruta


def video_1_case():
    """The case: clinical features as HPO terms, with no identifying data."""
    fig, ax = lienzo()
    titulo(ax, "The case: a pediatric patient with MVA",
           "Mosaic variegated aneuploidy: a rare recessive disease with no targeted treatment")
    rasgos = [
        ("Rhabdomyosarcoma", "HP:0002859", "childhood tumor, already present"),
        ("Growth restriction", "HP:0004322 · HP:0001508", "short stature, failure to thrive"),
        ("Small at birth and premature", "HP:0001518 · HP:0001622", ""),
        ("Muscle atrophy", "HP:0003202", ""),
        ("Nephrocalcinosis", "HP:0000121", "calcium deposits in the kidney"),
        ("Recurrent miscarriage in the parents", "HP:0200067", ""),
    ]
    for i, (rasgo, hpo, nota) in enumerate(rasgos):
        col, fila = i % 2, i // 2
        x, y = 0.5 + col * 7.7, 5.6 - fila * 1.9
        caja(ax, x, y, 7.2, 1.5)
        ax.text(x + 0.35, y + 1.0, rasgo, fontsize=18, fontweight="bold", va="center")
        ax.text(x + 0.35, y + 0.45, hpo + (f"  ·  {nota}" if nota else ""), fontsize=13, color=TINTA_2, va="center")
    ax.text(0.5, 0.35, "Challenge question: which mechanism explains the disease, and which approved drug could act on it?",
            fontsize=15, fontweight="bold", color=TINTA)
    return guardar(fig, "video_1_case.png")


def video_2_method():
    """The whole method in five steps, from the VCF to the proposal."""
    fig, ax = lienzo()
    titulo(ax, "How we did it: from genome to drugs in five steps",
           "The whole analysis runs with one command (python run_pipeline.py) and uses only public data")
    pasos = [
        ("1  Genome", TINTA_2, FONDO_CAJA,
         "Whole-genome\nVCF (GRCh38)\n\n321-gene panel\nof cell division", "24,604\nvariants"),
        ("2  Variant", TINTA_2, FONDO_CAJA,
         "Frequency (gnomAD)\neffect in MANE (VEP)\nCADD, ClinVar\nACMG classification", "1 gene:\nBUB1B"),
        ("3  Mechanism", TINTA_2, FONDO_CAJA,
         "mRNA decay (NMD)\nstructure (AlphaFold)\nstability (ThermoMPNN)\nverified literature", "low\nBUBR1"),
        ("4  Drugs", FARMACO, FONDO_VERDE,
         "4 therapeutic strategies\nDGIdb, Open Targets\nFDA / EMA approval\n6 weighted criteria", "86 → 5"),
        ("5  Proposal", FARMACO, FONDO_VERDE,
         "Continuous\ncombination\nof 3 drugs\n\ntest in patient\nfibroblasts", "3\ndrugs"),
    ]
    ancho, sep, x0 = 2.75, 0.4, 0.45
    for i, (cab, borde, fondo, cuerpo, cifra) in enumerate(pasos):
        x = x0 + i * (ancho + sep)
        caja(ax, x, 1.3, ancho, 5.9, borde=borde, fondo=fondo, lw=2.2)
        ax.text(x + ancho / 2, 6.75, cab, ha="center", fontsize=18, fontweight="bold")
        ax.text(x + ancho / 2, 4.85, cuerpo, ha="center", va="center", fontsize=12, linespacing=1.35)
        ax.text(x + ancho / 2, 2.25, cifra, ha="center", va="center", fontsize=20, fontweight="bold",
                color=borde if borde != TINTA_2 else TINTA, linespacing=1.1)
        if i < len(pasos) - 1:
            flecha(ax, (x + ancho + 0.03, 4.25), (x + ancho + sep - 0.03, 4.25))
    ax.text(0.45, 0.55, "Reference run: 6 min 11 s with cached queries · code on GitHub",
            fontsize=13, color=TINTA_2)
    return guardar(fig, "video_2_method.png")


def video_3_drug_funnel():
    """Drug funnel with the numbers of Section II-E of the report."""
    etapas = [
        ("Long list\n(DGIdb, Open Targets, curated)", 86, GRIS),
        ("Approved by the FDA or EMA\nand do not weaken mitosis", 73, GRIS),
        ("Repurposing candidates\n(the other 21 are context drugs)", 52, GRIS),
        ("Short list\n(best scores)", 5, ALTERNATIVA),
        ("Proposed combination", 3, FARMACO),
    ]
    fig, ax = plt.subplots(figsize=TAM)
    fig.subplots_adjust(left=0.30, right=0.93, top=0.80, bottom=0.16)
    y = list(range(len(etapas)))[::-1]
    ax.barh(y, [e[1] for e in etapas], color=[e[2] for e in etapas], height=0.62, edgecolor="white", linewidth=2)
    ax.set_yticks(y, [e[0] for e in etapas], fontsize=14)
    for yi, (_, n, _) in zip(y, etapas):
        ax.text(n + 1.2, yi, f"{n}", va="center", fontsize=18, fontweight="bold")
    ax.text(3 + 7, 0, "oral sirolimus · arimoclomol · niacin", va="center", fontsize=15, color=TINTA)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Number of drugs", fontsize=13)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.text(0.02, 0.94, "From 86 drugs to 3: how we chose", fontsize=24, fontweight="bold", va="top")
    fig.text(0.02, 0.875, "We removed unapproved drugs and those that would lower BUBR1 further (HSP90, PLK1, Aurora, MPS1, APC/C)",
             fontsize=14, color=TINTA_2, va="top")
    fig.text(0.02, 0.03, "Niacin was added by hand as a speculative hypothesis (NAD⁺–SIRT2–BubR1 axis). "
             "Source: results/candidatos_farmacos.tsv", fontsize=11.5, color=TINTA_2)
    return guardar(fig, "video_3_drug_funnel.png")


NOMBRES = {
    "SIROLIMUS": "Sirolimus", "TEMSIROLIMUS": "Temsirolimus", "ARIMOCLOMOL": "Arimoclomol",
    "EVEROLIMUS": "Everolimus", "SODIUM PHENYLBUTYRATE": "Sodium phenylbutyrate", "TRAMETINIB": "Trametinib",
    "SELUMETINIB": "Selumetinib", "CELECOXIB": "Celecoxib", "CRIZOTINIB": "Crizotinib", "DASATINIB": "Dasatinib",
    "BORTEZOMIB": "Bortezomib", "NIACIN": "Niacin",
}
FINAL = {"SIROLIMUS", "ARIMOCLOMOL", "NIACIN"}
ALTERNATIVAS = {"TEMSIROLIMUS", "DASATINIB", "TRAMETINIB", "SELUMETINIB"}


def video_4_scores():
    """Scores (0-100) of the best candidates and what happened to each one."""
    d = pd.read_csv(RAIZ / "results" / "candidatos_farmacos.tsv", sep="\t")
    d = d[(d.categoria == "candidato") & d.puntaje.notna()]
    top = d.sort_values("puntaje", ascending=False).head(11)
    if "NIACIN" not in set(top.farmaco):
        top = pd.concat([top, d[d.farmaco == "NIACIN"]])
    top = top.iloc[::-1]

    def color(f):
        return FARMACO if f in FINAL else ALTERNATIVA if f in ALTERNATIVAS else GRIS

    fig, ax = plt.subplots(figsize=TAM)
    fig.subplots_adjust(left=0.17, right=0.74, top=0.80, bottom=0.16)
    y = range(len(top))
    ax.barh(y, top.puntaje, color=[color(f) for f in top.farmaco], height=0.66, edgecolor="white", linewidth=2)
    ax.set_yticks(list(y), [NOMBRES.get(f, f.title()) for f in top.farmaco], fontsize=14)
    for yi, p in enumerate(top.puntaje):
        ax.text(p + 0.8, yi, f"{p:.1f}", va="center", fontsize=13, color=TINTA)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Score (0 to 100)", fontsize=13)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(handles=[Patch(color=FARMACO, label="In the proposed combination"),
                       Patch(color=ALTERNATIVA, label="Alternative or conditional"),
                       Patch(color=GRIS, label="Not selected")],
              loc="center left", bbox_to_anchor=(1.0, 0.5), frameon=False, fontsize=13)
    fig.text(0.02, 0.94, "Scores of the best candidates", fontsize=24, fontweight="bold", va="top")
    fig.text(0.02, 0.875, "Six criteria: mechanistic link 25 · pediatric safety 20 · evidence 15 · "
             "fit with the case 15 · innovation 15 · validation 10", fontsize=13.5, color=TINTA_2, va="top")
    fig.text(0.02, 0.03, "Everolimus repeats the mechanism of sirolimus. Bortezomib was removed by the biological review: "
             "it delays exit from mitosis. Niacin enters for innovation, not for its score.",
             fontsize=11.5, color=TINTA_2)
    return guardar(fig, "video_4_candidate_scores.png")


def video_5_proposal():
    """Two treatments in parallel: standard care for the tumor and the proposal for MVA."""
    fig, ax = lienzo()
    titulo(ax, "The proposal: two treatments in parallel",
           "The tumor already has standard treatment; the underlying disease has none")

    caja(ax, 0.4, 2.6, 5.6, 4.6, borde=TINTA_2, lw=2.2)
    ax.text(3.2, 6.65, "Standard care", ha="center", fontsize=19, fontweight="bold")
    ax.text(3.2, 6.05, "current rhabdomyosarcoma", ha="center", fontsize=14, color=TINTA_2)
    ax.text(3.2, 4.55, "Cyclophosphamide continues\nas part of the treatment\nthe patient already receives\n\n"
            "(reduced intensity, as in\na published MVA case)", ha="center", va="center", fontsize=14, linespacing=1.3)
    ax.text(3.2, 2.95, "Not a repurposing proposal", ha="center", fontsize=12.5, color=TINTA_2)

    caja(ax, 6.5, 2.6, 9.1, 4.6, borde=FARMACO, fondo=FONDO_VERDE, lw=2.6)
    ax.text(11.05, 6.65, "Our repurposing proposal", ha="center", fontsize=19, fontweight="bold")
    ax.text(11.05, 6.05, "underlying disease · long-term, continuous", ha="center", fontsize=14, color=TINTA_2)
    filas = [
        ("Oral sirolimus", "dampens mTORC1: premature aging,\nmuscle and growth"),
        ("Arimoclomol", "supports protein folding:\nmore BUBR1 (the cause)"),
        ("Niacin", "NAD⁺–SIRT2 axis: more BUBR1\n(speculative hypothesis)"),
    ]
    for i, (farm, que) in enumerate(filas):
        yy = 5.15 - i * 0.98
        ax.text(6.9, yy, farm, fontsize=16, fontweight="bold", color=TINTA, va="center")
        ax.text(9.6, yy, que, fontsize=12.5, color=TINTA, va="center", linespacing=1.15)

    caja(ax, 0.4, 0.35, 15.2, 1.85, borde=TINTA_2, fondo="white", lw=1.2)
    ax.text(0.75, 1.62, "How to test it:", fontsize=14.5, fontweight="bold", va="center")
    ax.text(4.0, 1.62, "patient fibroblasts before and after each drug → amount of BUBR1 (Western blot)\n"
            "and strength of the mitotic checkpoint (nocodazole assay)", fontsize=12.5, va="center", linespacing=1.25)
    ax.text(0.75, 0.75, "Also:", fontsize=14.5, fontweight="bold", va="center")
    ax.text(4.0, 0.75, "periodic blood counts and MRI for the LZTR1 finding", fontsize=12.5, va="center")
    return guardar(fig, "video_5_proposal.png")


if __name__ == "__main__":
    for f in (video_1_case, video_2_method, video_3_drug_funnel, video_4_scores, video_5_proposal):
        print(f())
