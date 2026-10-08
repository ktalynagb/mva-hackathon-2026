"""Figuras del informe (tareas A5 y B5).

Figura 1: BUBR1 con sus dominios, las dos variantes del paciente y las
variantes de MVA caracterizadas por Suijkerbuijk et al. 2010.
Figura 2: la via, de las variantes al fenotipo, con los puntos de entrada
de las cuatro lineas terapeuticas.

Estilo: docs/informe_final.md (guia de estilo). Paleta Okabe-Ito validada
para daltonismo: alelo 1 bermellon, alelo 2 azul, farmacos verde.
Uso: python scripts/figuras_informe.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "results"

ALELO1 = "#D55E00"
ALELO2 = "#0072B2"
FARMACO = "#009E73"
TINTA = "#1F1F1F"
TINTA_2 = "#555555"
GRIS_DOMINIO = "#D4D4D4"
GRIS_MOTIVO = "#8A8A8A"
GRIS_LIT = "#7A7A7A"
FONDO_CAJA = "#F2F2F2"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"],
    "font.size": 9,
    "text.color": TINTA,
    "axes.edgecolor": TINTA_2,
    "savefig.dpi": 300,
})

LONGITUD = 1050
# UniProt O60566 y Zhang 2026 (docs/secciones/02_marco_biologico.md, seccion 2)
DOMINIOS = [("TPR", 59, 219), ("Pseudoquinasa", 766, 1050)]
MOTIVOS = [("KEN1", 26, 28), ("D1", 224, 232), ("KEN2", 304, 306), ("GLEBS", 408, 418),
           ("Unión\nBUB1", 440, 460), ("D2", 555, 563), ("KARD", 669, 674)]
# Suijkerbuijk 2010 (PMID 20516114): fila = clase
LITERATURA = {
    "Missense: BUBR1\nreducida": [("R727C", 727), ("R814H", 814), ("L844F", 844), ("I909T", 909), ("L1012P", 1012)],
    "Missense: nivel\nnormal": [("Y155C", 155), ("R550Q", 550), ("Q921H", 921)],
    "Truncantes": [("194X", 194), ("386X", 386), ("731X", 731), ("753X", 753)],
}


def figura_1():
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    y_prot = 0.0

    ax.add_patch(Rectangle((1, y_prot - 0.07), LONGITUD - 1, 0.14, color=GRIS_DOMINIO, lw=0))
    for nombre, ini, fin in DOMINIOS:
        ax.add_patch(Rectangle((ini, y_prot - 0.28), fin - ini, 0.56, fc=GRIS_DOMINIO, ec="white", lw=1.5))
        ax.text((ini + fin) / 2, y_prot, nombre, ha="center", va="center", fontsize=8.5, color=TINTA)
    for i, (nombre, ini, fin) in enumerate(MOTIVOS):
        ancho = max(fin - ini, 6)
        ax.add_patch(Rectangle(((ini + fin) / 2 - ancho / 2, y_prot - 0.2), ancho, 0.4, fc=GRIS_MOTIVO, ec="white", lw=1))
        y_txt = y_prot - 0.42 - (0.32 if i % 2 else 0)
        ax.text((ini + fin) / 2, y_txt, nombre, ha="center", va="top", fontsize=6.5, color=TINTA_2, linespacing=0.9)

    for x in (1, 1050):
        ax.text(x, y_prot + 0.36, str(x), ha="center", va="bottom", fontsize=6.5, color=TINTA_2)

    # El alelo 1 se rotula a la izquierda y el 2 a la derecha para que los textos no se crucen
    pacientes = [
        (737, ALELO1, "s", "p.Leu737Ter", "alelo 1 · parada prematura\nNMD predicho → sin proteína", "right"),
        (1002, ALELO2, "o", "p.Asn1002Lys", "alelo 2 · missense\nΔΔG +1,5 kcal/mol (inestable)", "left"),
    ]
    for x, color, marca, nombre, detalle, lado in pacientes:
        ax.plot([x, x], [y_prot + 0.3, 1.85], color=color, lw=2, solid_capstyle="round", zorder=3)
        ax.plot(x, 1.85, marker=marca, ms=9, color=color, mec="white", mew=1.5, zorder=4)
        x_txt = x - 16 if lado == "right" else x + 16
        ax.text(x_txt, 2.12, nombre, ha=lado, va="bottom", fontsize=9, fontweight="bold", color=TINTA)
        ax.text(x_txt, 2.08, detalle, ha=lado, va="top", fontsize=7, color=TINTA_2, linespacing=1.1)
        ax.plot([x, x], [-1.05, -3.75], color=color, lw=1, ls=(0, (2, 2)), alpha=0.7, zorder=1)

    filas_y = {k: y for k, y in zip(LITERATURA, (-1.6, -2.45, -3.3))}
    for clase, variantes in LITERATURA.items():
        y = filas_y[clase]
        ax.plot([1, LONGITUD], [y, y], color="#E3E3E3", lw=0.8, zorder=0)
        ax.text(-18, y, clase, ha="right", va="center", fontsize=7, color=TINTA_2, linespacing=1.0)
        for i, (nombre, x) in enumerate(variantes):
            if clase.startswith("Truncantes"):
                ax.plot(x, y, marker="s", ms=6, color=GRIS_LIT, mec="white", mew=1, zorder=3)
            elif "reducida" in clase:
                ax.plot(x, y, marker="o", ms=6.5, color=GRIS_LIT, mec="white", mew=1, zorder=3)
            else:
                ax.plot(x, y, marker="o", ms=6.5, mfc="white", mec=GRIS_LIT, mew=1.4, zorder=3)
            arriba = i % 2 == 0
            ax.text(x, y + (0.17 if arriba else -0.17), nombre, ha="center",
                    va="bottom" if arriba else "top", fontsize=6.5, color=TINTA_2)

    ax.text(-18, -0.98, "Variantes de MVA\nestudiadas en células\n(Suijkerbuijk 2010)", ha="right", va="center",
            fontsize=7, color=TINTA, fontweight="bold", linespacing=1.0)
    ax.text(-18, 1.85, "Paciente", ha="right", va="center", fontsize=8, color=TINTA, fontweight="bold")

    leyenda = [
        Line2D([], [], marker="s", ls="", color=GRIS_LIT, mec="white", ms=6, label="truncante"),
        Line2D([], [], marker="o", ls="", color=GRIS_LIT, mec="white", ms=6.5, label="missense, BUBR1 reducida"),
        Line2D([], [], marker="o", ls="", mfc="white", mec=GRIS_LIT, mew=1.4, ms=6.5, label="missense, nivel normal"),
    ]
    ax.legend(handles=leyenda, loc="lower right", bbox_to_anchor=(1.0, -0.02), frameon=False, fontsize=6.5,
              ncol=3, handletextpad=0.3, columnspacing=1.0)

    ax.set_xlim(-250, 1290)
    ax.set_ylim(-4.0, 3.1)
    ax.axis("off")
    ax.set_title("BUBR1 (1050 aa): variantes del paciente y variantes de MVA caracterizadas",
                 fontsize=10, loc="left", x=0.0, color=TINTA, pad=2)
    fig.tight_layout()
    ruta = SALIDA / "figura_1_bubr1_variantes.png"
    fig.savefig(ruta, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return ruta


def caja(ax, x, y, texto, ancho=1.9, alto=0.62, borde=TINTA_2, fondo=FONDO_CAJA, lw=1.0, peso="normal", tam=8):
    ax.add_patch(FancyBboxPatch((x - ancho / 2, y - alto / 2), ancho, alto,
                                boxstyle="round,pad=0.02,rounding_size=0.08", fc=fondo, ec=borde, lw=lw, zorder=2))
    ax.text(x, y, texto, ha="center", va="center", fontsize=tam, color=TINTA, fontweight=peso, linespacing=1.1, zorder=3)


def flecha(ax, a, b, color=TINTA_2, estilo="-|>", ls="-", lw=1.2, rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=estilo, mutation_scale=10, color=color, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=2, shrinkB=2, zorder=1))


def figura_2():
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.95, 7.9)
    ax.axis("off")

    # Variantes
    caja(ax, 1.25, 6.7, "p.Leu737Ter\n(alelo 1)", ancho=1.9, borde=ALELO1, lw=2, peso="bold")
    caja(ax, 1.25, 5.3, "p.Asn1002Lys\n(alelo 2)", ancho=1.9, borde=ALELO2, lw=2, peso="bold")
    caja(ax, 3.85, 6.7, "ARNm degradado (NMD)\nno hay proteína", ancho=2.4)
    caja(ax, 3.85, 5.3, "Pseudoquinasa mal plegada\nse degrada antes", ancho=2.4)
    flecha(ax, (2.2, 6.7), (2.65, 6.7), color=ALELO1, lw=1.6)
    flecha(ax, (2.2, 5.3), (2.65, 5.3), color=ALELO2, lw=1.6)
    ax.text(3.85, 6.28, "predicho (regla 50–55 nt)", ha="center", va="top", fontsize=6.5, style="italic", color=TINTA_2)
    ax.text(3.85, 4.88, "ΔΔG +1,5 · precedente en células", ha="center", va="top", fontsize=6.5, style="italic", color=TINTA_2)

    # Cadena central
    caja(ax, 6.85, 6.0, "Poca BUBR1", ancho=1.9, peso="bold", tam=9)
    flecha(ax, (5.05, 6.6), (5.9, 6.15))
    flecha(ax, (5.05, 5.4), (5.9, 5.85))
    caja(ax, 9.6, 6.0, "Checkpoint mitótico\ndébil (MCC insuficiente)", ancho=2.5)
    flecha(ax, (7.8, 6.0), (8.35, 6.0))
    caja(ax, 9.6, 4.6, "Errores al repartir\nlos cromosomas", ancho=2.5)
    flecha(ax, (9.6, 5.69), (9.6, 4.91))
    caja(ax, 9.6, 3.2, "Aneuploidía en mosaico", ancho=2.5, peso="bold")
    flecha(ax, (9.6, 4.29), (9.6, 3.51))

    # Ramas al fenotipo
    caja(ax, 6.0, 1.75, "Senescencia celular\nmTORC1 hiperactivo (ratón)", ancho=2.6)
    caja(ax, 10.3, 1.75, "Inestabilidad\ncromosómica", ancho=2.2)
    flecha(ax, (8.9, 2.89), (6.6, 2.06), rad=-0.1)
    flecha(ax, (10.0, 2.89), (10.3, 2.06))
    caja(ax, 6.0, 0.55, "Retraso del crecimiento · talla baja\nfalla de medro · atrofia muscular",
         ancho=3.3, fondo="white", borde=TINTA)
    caja(ax, 10.3, 0.55, "Rabdomiosarcoma", ancho=2.2, fondo="white", borde=TINTA, peso="bold")
    flecha(ax, (6.0, 1.44), (6.0, 0.86))
    flecha(ax, (10.3, 1.44), (10.3, 0.86))

    # Lineas terapeuticas (verde, discontinuas)
    def linea(num, texto, desde, hasta, alinear="center", rad=0.0):
        ax.text(*desde, f"{num}  {texto}", ha=alinear, va="center", fontsize=7.5, color=TINTA,
                bbox=dict(boxstyle="round,pad=0.25,rounding_size=0.15", fc="white", ec=FARMACO, lw=1.3), zorder=4)
        flecha(ax, desde, hasta, color=FARMACO, ls=(0, (3, 2)), lw=1.4, rad=rad)

    linea("1", "Subir la cantidad de BUBR1\n(arimoclomol, fenilbutirato)", (6.85, 7.35), (6.85, 6.33))
    linea("2", "Frenar mTORC1\n(sirolimus, everolimus)", (2.3, 1.75), (4.68, 1.75))
    linea("3", "Senolíticos\n(dasatinib)", (2.3, 2.95), (5.0, 2.08), rad=-0.15)
    linea("4", "Tratar el tumor sin empeorar\nla aneuploidía (temsirolimus)", (10.3, -0.6), (10.3, 0.22))

    # Advertencias
    ax.text(3.85, 4.35, "✗ Inhibir HSP90 la baja aún más", ha="center", va="center", fontsize=7, color=TINTA,
            fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=TINTA_2, lw=0.8, ls="--"))
    ax.text(10.75, 7.15, "⚠ Antimitóticos (vincristina):\nrespuesta alterada", ha="center", va="center", fontsize=7,
            color=TINTA, fontweight="bold", linespacing=1.1,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=TINTA_2, lw=0.8, ls="--"))

    leyenda = [
        Line2D([], [], color=TINTA_2, lw=1.2, label="mecanismo"),
        Line2D([], [], color=FARMACO, lw=1.4, ls=(0, (3, 2)), label="punto de acción de una línea terapéutica"),
    ]
    ax.legend(handles=leyenda, loc="lower left", bbox_to_anchor=(0.0, 0.0), frameon=False, fontsize=7)
    ax.set_title("Del genotipo al fenotipo, y dónde podría actuar cada línea terapéutica",
                 fontsize=10, loc="left", color=TINTA, pad=2)
    fig.tight_layout()
    ruta = SALIDA / "figura_2_via_mecanismo.png"
    fig.savefig(ruta, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return ruta


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for f in (figura_1(), figura_2()):
        print("Guardada", f.relative_to(RAIZ))
