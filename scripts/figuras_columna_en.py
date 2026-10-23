"""Single-column versions (3.5 in wide) of the figures of the IEEE report.

IEEE places figures inside one column of a two-column page. Shrinking the full-width
figures would leave 4-pt text, so each one is redrawn here at its final size, with
shorter labels and 6-7 pt text. The content is the same as in scripts/figuras_report_en.py
and scripts/figuras_informe.py.

Usage: python scripts/figuras_columna_en.py  ->  results/en/col_*.png
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch, Rectangle

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "results" / "en"

AZUL = "#0072B2"
BERMELLON = "#D55E00"
VERDE = "#009E73"
NARANJA = "#E69F00"
GRIS = "#BDBDBD"
GRIS_OSC = "#7A7A7A"
TINTA = "#1F1F1F"
TINTA_2 = "#555555"
FONDO = "#F2F2F2"
ANCHO = 3.5  # pulgadas: ancho de una columna IEEE

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"],
    "font.size": 6.5,
    "text.color": TINTA,
    "axes.edgecolor": TINTA_2,
    "axes.labelcolor": TINTA_2,
    "axes.linewidth": 0.6,
    "xtick.color": TINTA_2,
    "ytick.color": TINTA,
    "xtick.major.width": 0.6,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6.5,
    "savefig.dpi": 400,
})


def guardar(fig, nombre):
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / nombre
    fig.savefig(ruta, facecolor="white", bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    return ruta


def limpiar(ax):
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)


def caja(ax, x, y, ancho, alto, texto="", borde=TINTA_2, fondo=FONDO, lw=0.7, tam=6, peso="normal", color=TINTA):
    ax.add_patch(FancyBboxPatch((x - ancho / 2, y - alto / 2), ancho, alto,
                                boxstyle="round,pad=0.02,rounding_size=0.12", fc=fondo, ec=borde, lw=lw, zorder=2))
    if texto:
        ax.text(x, y, texto, ha="center", va="center", fontsize=tam, fontweight=peso, color=color,
                linespacing=1.1, zorder=3)


def flecha(ax, a, b, color=TINTA_2, ls="-", lw=0.8, rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=6, color=color, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0, zorder=1))


# Fig. 1 ---------------------------------------------------------------------------------
def embudo():
    pasos = [("All variants in the VCF", 5_012_204), ("Pass quality filters", 4_740_790),
             ("In the 321-gene panel", 24_604), ("Rare or absent in gnomAD*", 23_242),
             ("Alter protein (any transcript)", 19), ("Alter protein (MANE Select)", 14),
             ("Genes, recessive pattern", 1)]
    fig, ax = plt.subplots(figsize=(ANCHO, 1.9))
    y = list(range(len(pasos)))[::-1]
    ax.barh(y, [n for _, n in pasos], color=[AZUL] * 6 + [BERMELLON], height=0.68, edgecolor="white", lw=1)
    ax.set_yticks(y, [p for p, _ in pasos])
    for yi, (_, n) in zip(y, pasos):
        ax.text(n * 1.4, yi, "1 (BUB1B)" if n == 1 else f"{n:,}", va="center", fontsize=5.8,
                fontweight="bold" if n == 1 else "normal", fontstyle="italic" if n == 1 else "normal")
    ax.set_xscale("log")
    ax.set_xlim(0.5, 3e8)
    ax.set_xlabel("Number of variants (log scale)", fontsize=6)
    limpiar(ax)
    fig.text(0.0, -0.13, "*Mostly intronic variants missing from the gene-level gnomAD query; removed at the next step.",
             fontsize=5, color=TINTA_2)
    return guardar(fig, "col_variant_funnel.png")


# Fig. 2 ---------------------------------------------------------------------------------
def variantes_por_gen():
    d = pd.read_csv(RAIZ / "results" / "diagnostico_diferencial_variantes.tsv", sep="\t")
    AUSENTE = 1.5e-7
    d["x"] = d["af"].fillna(AUSENTE)
    cuenta = d[d.cuenta].groupby("gen").size()
    genes = sorted(d.gen.unique(), key=lambda g: (-cuenta.get(g, 0), d[d.gen == g].x.min()))
    y = {g: len(genes) - 1 - i for i, g in enumerate(genes)}

    fig, ax = plt.subplots(figsize=(ANCHO, 3.0))
    ax.axhspan(y["BUB1B"] - 0.45, y["BUB1B"] + 0.45, color="#F3E3D8", lw=0, zorder=0)
    for v in d.itertuples():
        if v.gen == "BUB1B":
            stop = v.consecuencia_mane == "stop_gained"
            ax.plot(v.x, y[v.gen], marker="s" if stop else "o", ms=5, color=BERMELLON if stop else AZUL,
                    mec="white", mew=0.6, zorder=3)
        elif v.cuenta:
            ax.plot(v.x, y[v.gen], marker="o", ms=4, color=GRIS_OSC, mec="white", mew=0.6, zorder=3)
        else:
            ax.plot(v.x, y[v.gen], marker="o", ms=4, mfc="white", mec=GRIS_OSC, mew=0.8, zorder=3)
    for g in genes:
        n = cuenta.get(g, 0)
        ax.text(2.2e-1, y[g], str(n), va="center", ha="center", fontsize=6,
                fontweight="bold" if n == 2 else "normal", color=TINTA if n else TINTA_2)
    ax.text(2.2e-1, len(genes) - 0.3, "counted", ha="center", va="bottom", fontsize=5.5, color=TINTA_2)
    ax.axvline(1e-2, color=TINTA_2, lw=0.6, ls=(0, (3, 2)))
    ax.text(1.15e-2, -0.95, "1% cutoff", fontsize=5.5, color=TINTA_2, va="center")
    ax.set_xscale("log")
    ax.set_xlim(8e-8, 4e-1)
    ax.set_ylim(-1.3, len(genes) - 0.3)
    ax.set_yticks(list(y.values()), list(y), fontstyle="italic", fontsize=6)
    ax.set_xticks([AUSENTE, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2], ["absent", "10⁻⁶", "10⁻⁵", "10⁻⁴", "10⁻³", "10⁻²"])
    ax.minorticks_off()
    ax.set_xlabel("Allele frequency in gnomAD v4 (log scale)", fontsize=6)
    limpiar(ax)
    ley = [Line2D([], [], marker="s", ls="", color=BERMELLON, mec="white", ms=5, label="BUB1B allele 1"),
           Line2D([], [], marker="o", ls="", color=AZUL, mec="white", ms=5, label="BUB1B allele 2"),
           Line2D([], [], marker="o", ls="", color=GRIS_OSC, mec="white", ms=4, label="alters protein in MANE"),
           Line2D([], [], marker="o", ls="", mfc="white", mec=GRIS_OSC, mew=0.8, ms=4, label="secondary transcript only")]
    ax.legend(handles=ley, loc="upper center", bbox_to_anchor=(0.42, -0.2), ncol=2, frameon=False, fontsize=5.5,
              handletextpad=0.3, columnspacing=0.8)
    return guardar(fig, "col_variants_per_gene.png")


# Fig. 3 ---------------------------------------------------------------------------------
def bubr1():
    L = 1050
    fig, ax = plt.subplots(figsize=(ANCHO, 2.9))
    ax.set_xlim(-330, 1100)
    ax.set_ylim(-4.3, 3.4)
    ax.axis("off")
    ax.add_patch(Rectangle((1, -0.07), L - 1, 0.14, color="#D4D4D4", lw=0))
    for nombre, ini, fin in (("TPR", 59, 219), ("Pseudokinase", 766, 1050)):
        ax.add_patch(Rectangle((ini, -0.3), fin - ini, 0.6, fc="#D4D4D4", ec="white", lw=1))
        ax.text((ini + fin) / 2, 0, nombre, ha="center", va="center", fontsize=6)
    motivos = [("KEN1", 27), ("D1", 228), ("KEN2", 305), ("GLEBS", 413), ("BUB1-b", 450), ("D2", 559), ("KARD", 671)]
    for i, (nombre, x) in enumerate(motivos):
        ax.add_patch(Rectangle((x - 5, -0.22), 10, 0.44, fc=GRIS_OSC, ec="white", lw=0.5))
        ax.text(x, -0.48 - 0.42 * (i % 2), nombre, ha="center", va="top", fontsize=4.8, color=TINTA_2)
    ax.text(1, 0.4, "1", fontsize=5, color=TINTA_2, ha="center")
    ax.text(L, 0.4, "1050", fontsize=5, color=TINTA_2, ha="center")

    # (x, color, marca, nombre, detalle, alto del tallo, x del texto, y del nombre)
    for x, color, marca, nombre, detalle, alto, xt, yn in (
            (737, BERMELLON, "s", "p.Leu737Ter", "allele 1 · stop\npredicted NMD", 2.75, 715, 2.95),
            (1002, AZUL, "o", "p.Asn1002Lys", "allele 2 · missense\nΔΔG +1.5 kcal/mol", 1.9, 1095, 3.15)):
        ax.plot([x, x], [0.32, alto], color=color, lw=1.4, solid_capstyle="round", zorder=3)
        ax.plot(x, alto, marker=marca, ms=5, color=color, mec="white", mew=0.8, zorder=4)
        ax.text(xt, yn, nombre, ha="right", va="center", fontsize=6.2, fontweight="bold")
        ax.text(xt, yn - 0.3, detalle, ha="right", va="top", fontsize=5, color=TINTA_2, linespacing=1.05)
        ax.plot([x, x], [-1.25, -4.1], color=color, lw=0.6, ls=(0, (2, 2)), alpha=0.7, zorder=1)
    ax.text(-30, 2.2, "Patient", ha="right", va="center", fontsize=6.2, fontweight="bold")

    filas = {"Missense,\nreduced BUBR1": (-1.85, [("R727C", 727), ("R814H", 814), ("L844F", 844), ("I909T", 909),
                                                    ("L1012P", 1012)], "lleno"),
             "Missense,\nnormal level": (-2.75, [("Y155C", 155), ("R550Q", 550), ("Q921H", 921)], "vacio"),
             "Truncating": (-3.65, [("194X", 194), ("386X", 386), ("731X", 731), ("753X", 753)], "cuadro")}
    ax.text(-30, -1.3, "MVA variants in cells [21]", ha="right", va="center", fontsize=5.3, fontweight="bold")
    for etiqueta, (yy, variantes, tipo) in filas.items():
        ax.plot([1, L], [yy, yy], color="#E3E3E3", lw=0.6, zorder=0)
        ax.text(-30, yy, etiqueta, ha="right", va="center", fontsize=5.2, color=TINTA_2, linespacing=1.0)
        for i, (n, x) in enumerate(variantes):
            if tipo == "cuadro":
                ax.plot(x, yy, marker="s", ms=3.5, color=GRIS_OSC, mec="white", mew=0.5, zorder=3)
            elif tipo == "lleno":
                ax.plot(x, yy, marker="o", ms=4, color=GRIS_OSC, mec="white", mew=0.5, zorder=3)
            else:
                ax.plot(x, yy, marker="o", ms=4, mfc="white", mec=GRIS_OSC, mew=0.8, zorder=3)
            arriba = i % 2 == 0
            dx = 22 if n == "I909T" else 0  # I909T cae muy cerca de R814H
            ax.text(x + dx, yy + (0.16 if arriba else -0.16), n, ha="center", va="bottom" if arriba else "top",
                    fontsize=4.6, color=TINTA_2)
    return guardar(fig, "col_bubr1_variants.png")


# Fig. 4 ---------------------------------------------------------------------------------
def checkpoint():
    fig, ax = plt.subplots(figsize=(ANCHO, 2.9))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.3)
    ax.axis("off")
    filas = [6.9, 5.55, 4.2, 2.85, 1.5]
    normal = ["Unattached\nchromosome", "Enough BUBR1 →\nenough MCC", "APC/C–CDC20\nstays inhibited",
              "Anaphase waits:\ncorrect separation", "Daughter cells with\n46 chromosomes"]
    paciente = ["Unattached\nchromosome", "Low BUBR1 →\ntoo little MCC", "APC/C–CDC20\nreleased too early",
                "Early anaphase:\nmissegregation", "Some cells with 45 or 47\n→ mosaic aneuploidy"]
    for x, textos, col in ((2.45, normal, TINTA_2), (7.55, paciente, BERMELLON)):
        for i, (t, y) in enumerate(zip(textos, filas)):
            afectado = col == BERMELLON and i > 0
            caja(ax, x, y, 4.5, 1.0, t, borde=col if afectado else TINTA_2, fondo="#FBEDE5" if afectado else FONDO,
                 lw=0.9 if afectado else 0.6, tam=6, peso="bold" if i in (1, 4) and afectado else "normal")
            if i < 4:
                flecha(ax, (x, y - 0.5), (x, filas[i + 1] + 0.5), color=col if afectado else TINTA_2)
    ax.text(2.45, 7.85, "Normal checkpoint", ha="center", fontsize=6.8, fontweight="bold")
    ax.text(7.55, 7.85, "This patient", ha="center", fontsize=6.8, fontweight="bold", color=BERMELLON)
    return guardar(fig, "col_checkpoint.png")


# Fig. 5 ---------------------------------------------------------------------------------
def via():
    fig, ax = plt.subplots(figsize=(ANCHO, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0.3, 14)
    ax.axis("off")
    cx = 5.5
    caja(ax, 2.6, 13.1, 4.6, 1.1, "p.Leu737Ter (allele 1)\nNMD: no protein", borde=BERMELLON, lw=1.2, tam=5.8)
    caja(ax, 7.6, 13.1, 4.6, 1.1, "p.Asn1002Lys (allele 2)\nmisfolded, degraded faster", borde=AZUL, lw=1.2, tam=5.8)
    caja(ax, cx, 11.2, 2.8, 0.9, "Low BUBR1", peso="bold", tam=6.8)
    flecha(ax, (2.6, 12.55), (cx - 0.6, 11.65))
    flecha(ax, (7.6, 12.55), (cx + 0.6, 11.65))
    caja(ax, cx, 9.7, 3.2, 0.95, "Weak mitotic checkpoint\n(insufficient MCC)", tam=5.4)
    caja(ax, cx, 8.25, 3.2, 0.95, "Chromosome\nmissegregation", tam=5.8)
    caja(ax, cx, 6.8, 3.2, 0.9, "Mosaic aneuploidy", peso="bold", tam=6.2)
    for a, b in ((10.75, 10.18), (9.22, 8.73), (7.77, 7.25)):
        flecha(ax, (cx, a), (cx, b))
    caja(ax, 2.8, 4.8, 3.9, 1.0, "Cellular senescence\nhigh mTORC1 (mouse)", tam=5.8)
    caja(ax, 7.9, 4.8, 3.3, 1.0, "Chromosomal\ninstability", tam=5.8)
    flecha(ax, (cx - 0.9, 6.35), (3.4, 5.3))
    flecha(ax, (cx + 0.9, 6.35), (7.6, 5.3))
    caja(ax, 2.8, 3.25, 3.9, 1.0, "Growth restriction, short\nstature, muscle atrophy", fondo="white", borde=TINTA, tam=5.6)
    caja(ax, 7.9, 3.25, 3.3, 0.9, "Rhabdomyosarcoma", fondo="white", borde=TINTA, peso="bold", tam=6)
    flecha(ax, (2.8, 4.3), (2.8, 3.75))
    flecha(ax, (7.9, 4.3), (7.9, 3.7))

    terapia = dict(borde=VERDE, fondo="white", lw=1.0, tam=5.4)
    caja(ax, 8.65, 11.2, 2.6, 1.25, "1 Raise BUBR1\n(arimoclomol,\nphenylbutyrate)", **terapia)
    flecha(ax, (7.35, 11.2), (cx + 1.42, 11.2), color=VERDE, ls=(0, (3, 2)))
    caja(ax, 1.75, 7.5, 3.3, 1.5, "2 Dampen mTORC1\n(sirolimus, everolimus)\n3 Senolytics (dasatinib)", **terapia)
    flecha(ax, (1.75, 6.75), (2.1, 5.3), color=VERDE, ls=(0, (3, 2)))
    caja(ax, 7.9, 1.55, 3.6, 1.15, "4 Treat the tumor without\nworsening aneuploidy\n(temsirolimus)", **terapia)
    flecha(ax, (7.9, 2.13), (7.9, 2.8), color=VERDE, ls=(0, (3, 2)))

    aviso = dict(borde=TINTA_2, fondo="white", lw=0.6, tam=5.2)
    caja(ax, 1.75, 11.2, 3.0, 1.0, "✗ HSP90 inhibition\nlowers it further", **aviso)
    caja(ax, 8.75, 9.0, 2.45, 1.25, "⚠ Antimitotics\n(vincristine):\naltered response", **aviso)
    ax.legend(handles=[Line2D([], [], color=TINTA_2, lw=0.8, label="mechanism"),
                       Line2D([], [], color=VERDE, lw=1.0, ls=(0, (3, 2)), label="therapeutic strategy")],
              loc="lower left", bbox_to_anchor=(0.0, 0.0), frameon=False, fontsize=5.5, handlelength=2)
    return guardar(fig, "col_mechanism_pathway.png")


# Fig. 6 ---------------------------------------------------------------------------------
NOMBRES = {"SIROLIMUS": "Sirolimus", "TEMSIROLIMUS": "Temsirolimus", "ARIMOCLOMOL": "Arimoclomol",
           "EVEROLIMUS": "Everolimus", "SODIUM PHENYLBUTYRATE": "Na phenylbutyrate", "TRAMETINIB": "Trametinib",
           "SELUMETINIB": "Selumetinib", "CELECOXIB": "Celecoxib", "CRIZOTINIB": "Crizotinib", "DASATINIB": "Dasatinib",
           "BORTEZOMIB": "Bortezomib", "NIACIN": "Niacin"}
EN_PROPUESTA = {"SIROLIMUS", "ARIMOCLOMOL", "NIACIN"}
ALTERNATIVAS = {"TEMSIROLIMUS", "DASATINIB", "TRAMETINIB", "SELUMETINIB"}


def farmacos():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(ANCHO, 4.1), gridspec_kw={"height_ratios": [1, 2.1]})
    etapas = [("Long list", 86, GRIS), ("Approved, do not weaken mitosis", 73, GRIS),
              ("Repurposing candidates", 52, GRIS), ("Short list", 5, NARANJA), ("Proposed combination", 3, VERDE)]
    yy = list(range(len(etapas)))[::-1]
    ax1.barh(yy, [n for _, n, _ in etapas], color=[c for _, _, c in etapas], height=0.66, edgecolor="white", lw=1)
    ax1.set_yticks(yy, [e for e, _, _ in etapas], fontsize=6)
    for yi, (_, n, _) in zip(yy, etapas):
        ax1.text(n + 1.5, yi, str(n), va="center", fontsize=6, fontweight="bold" if n == 3 else "normal")
    ax1.set_xlim(0, 100)
    ax1.set_xlabel("Number of drugs", fontsize=6)
    ax1.set_title("(a) From 86 drugs to 3", fontsize=6.8, loc="left")

    d = pd.read_csv(RAIZ / "results" / "candidatos_farmacos.tsv", sep="\t")
    d = d[(d.categoria == "candidato") & d.puntaje.notna()]
    top = d.sort_values("puntaje", ascending=False).head(11)
    if "NIACIN" not in set(top.farmaco):
        top = pd.concat([top, d[d.farmaco == "NIACIN"]])
    top = top.iloc[::-1]
    color = [VERDE if f in EN_PROPUESTA else NARANJA if f in ALTERNATIVAS else GRIS for f in top.farmaco]
    ax2.barh(range(len(top)), top.puntaje, color=color, height=0.68, edgecolor="white", lw=1)
    ax2.set_yticks(range(len(top)), [NOMBRES.get(f, f.title()) for f in top.farmaco], fontsize=6)
    for yi, p in enumerate(top.puntaje):
        ax2.text(p + 1, yi, f"{p:.1f}", va="center", fontsize=5.5)
    ax2.set_xlim(0, 100)
    ax2.set_xlabel("Score (0–100)", fontsize=6)
    ax2.set_title("(b) Best-ranked candidates", fontsize=6.8, loc="left")
    ax2.legend(handles=[Patch(color=VERDE, label="in the combination"), Patch(color=NARANJA, label="alternative"),
                        Patch(color=GRIS, label="not selected")],
               loc="upper center", bbox_to_anchor=(0.35, -0.2), ncol=3, fontsize=5.5, frameon=False,
               handlelength=1, columnspacing=0.8)
    for ax in (ax1, ax2):
        limpiar(ax)
    fig.tight_layout(h_pad=1.0)
    return guardar(fig, "col_drug_selection.png")


# Fig. 7 ---------------------------------------------------------------------------------
def propuesta():
    fig, ax = plt.subplots(figsize=(ANCHO, 3.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10.2)
    ax.axis("off")
    caja(ax, 5, 9.0, 9.8, 2.1, borde=TINTA_2, lw=0.8)
    ax.text(5, 9.65, "Standard care · current rhabdomyosarcoma", ha="center", fontsize=6.5, fontweight="bold")
    ax.text(5, 8.65, "Cyclophosphamide continues as part of the treatment the patient\nalready receives "
            "(reduced intensity, as in a published MVA case).\nNot a repurposing proposal.",
            ha="center", va="center", fontsize=5.6, linespacing=1.15)
    caja(ax, 5, 5.0, 9.8, 5.2, borde=VERDE, fondo="#E6F4EF", lw=1.1)
    ax.text(5, 7.15, "Our repurposing proposal · long-term, continuous", ha="center", fontsize=6.5, fontweight="bold")
    for i, (farmaco, que) in enumerate((("Oral sirolimus", "dampens mTORC1: premature aging,\nmuscle atrophy, growth restriction"),
                                        ("Arimoclomol", "supports protein folding:\nmore BUBR1 (the cause)"),
                                        ("Niacin", "NAD⁺–SIRT2 axis: more BUBR1\n(speculative hypothesis)"))):
        y = 6.1 - i * 1.25
        ax.text(0.5, y, farmaco, fontsize=6.3, fontweight="bold", va="center")
        ax.text(3.6, y, que, fontsize=5.6, va="center", linespacing=1.1)
    ax.text(5, 2.75, "Could indirectly lower the risk of new tumors (hypothesis)", ha="center", fontsize=5.3,
            style="italic", color=TINTA_2)
    caja(ax, 5, 1.1, 9.8, 1.9, borde=TINTA_2, fondo="white", lw=0.6)
    ax.text(0.4, 1.55, "Validation:", fontsize=5.8, fontweight="bold", va="center")
    ax.text(2.7, 1.55, "patient fibroblasts ± each drug → BUBR1 level\n(Western blot) and nocodazole arrest",
            fontsize=5.4, va="center", linespacing=1.1)
    ax.text(0.4, 0.55, "Surveillance:", fontsize=5.8, fontweight="bold", va="center")
    ax.text(2.7, 0.55, "periodic blood counts · MRI for the LZTR1 finding", fontsize=5.4, va="center")
    return guardar(fig, "col_proposal.png")


if __name__ == "__main__":
    for f in (embudo, variantes_por_gen, bubr1, checkpoint, via, farmacos, propuesta):
        print(f())
