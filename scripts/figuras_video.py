"""Figuras de apoyo para el video de 3 minutos (tarea E4/E6).

Complementan las figuras del informe (figura_1, figura_2 y el embudo de
variantes) con lo que el video tiene que contar y el informe muestra solo en
tablas: el caso, el método completo, el embudo de fármacos, los puntajes y la
propuesta final. Formato 16:9 y letra grande para que se lean en pantalla.

Estilo: misma paleta Okabe-Ito que scripts/figuras_informe.py.
Datos: results/candidatos_farmacos.tsv y los números de docs/informe_final.md.
Uso: python scripts/figuras_video.py  ->  results/video/*.png
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


def video_1_caso():
    """El caso: rasgos clínicos en términos HPO, sin datos identificatorios."""
    fig, ax = lienzo()
    titulo(ax, "El caso: un paciente pediátrico con MVA",
           "Aneuploidía variegada en mosaico: enfermedad rara, recesiva y sin tratamiento dirigido")
    rasgos = [
        ("Rabdomiosarcoma", "HP:0002859", "tumor infantil, ya presente"),
        ("Retraso del crecimiento", "HP:0004322 · HP:0001508", "talla baja y falla de medro"),
        ("Pequeño al nacer y prematuro", "HP:0001518 · HP:0001622", ""),
        ("Atrofia muscular", "HP:0003202", ""),
        ("Nefrocalcinosis", "HP:0000121", "calcio depositado en el riñón"),
        ("Abortos recurrentes en los padres", "HP:0200067", ""),
    ]
    for i, (rasgo, hpo, nota) in enumerate(rasgos):
        col, fila = i % 2, i // 2
        x, y = 0.5 + col * 7.7, 5.6 - fila * 1.9
        caja(ax, x, y, 7.2, 1.5)
        ax.text(x + 0.35, y + 1.0, rasgo, fontsize=18, fontweight="bold", va="center")
        ax.text(x + 0.35, y + 0.45, hpo + (f"  ·  {nota}" if nota else ""), fontsize=13, color=TINTA_2, va="center")
    ax.text(0.5, 0.35, "Pregunta del reto: ¿qué mecanismo explica la enfermedad y qué fármaco ya aprobado podría actuar sobre él?",
            fontsize=15, fontweight="bold", color=TINTA)
    return guardar(fig, "video_1_caso.png")


def video_2_metodo():
    """El método completo en cinco pasos, del VCF a la propuesta."""
    fig, ax = lienzo()
    titulo(ax, "Cómo lo hicimos: del genoma a los fármacos en cinco pasos",
           "Todo el análisis corre con un solo comando (python run_pipeline.py) y solo usa datos públicos")
    pasos = [
        ("1  Genoma", TINTA_2, FONDO_CAJA,
         "VCF de genoma\ncompleto (GRCh38)\n\nPanel de 321 genes\nde la división celular", "24.604\nvariantes"),
        ("2  Variante", TINTA_2, FONDO_CAJA,
         "Frecuencia (gnomAD)\nefecto en MANE (VEP)\nCADD, ClinVar\nclasificación ACMG", "1 gen:\nBUB1B"),
        ("3  Mecanismo", TINTA_2, FONDO_CAJA,
         "ARNm degradado (NMD)\nestructura (AlphaFold)\nestabilidad (ThermoMPNN)\nliteratura verificada", "poca\nBUBR1"),
        ("4  Fármacos", FARMACO, FONDO_VERDE,
         "4 líneas terapéuticas\nDGIdb, Open Targets\naprobación FDA / EMA\n6 criterios con pesos", "86 → 5"),
        ("5  Propuesta", FARMACO, FONDO_VERDE,
         "Esquema continuo\nde 3 fármacos\n\nprueba en fibroblastos\ndel paciente", "3\nfármacos"),
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
    ax.text(0.45, 0.55, "Corrida completa de referencia: 6 min 11 s con las consultas en caché · código en GitHub",
            fontsize=13, color=TINTA_2)
    return guardar(fig, "video_2_metodo.png")


def video_3_embudo_farmacos():
    """Embudo de fármacos con los números de la sección 2.4 del informe."""
    etapas = [
        ("Lista larga\n(DGIdb, Open Targets, curados)", 86, GRIS),
        ("Aprobados en FDA o EMA y que\nno debilitan la mitosis", 73, GRIS),
        ("Candidatos para el MVA\n(los otros 21 son de contexto)", 52, GRIS),
        ("Lista corta\n(mejor puntaje)", 5, ALTERNATIVA),
        ("Esquema continuo propuesto", 3, FARMACO),
    ]
    fig, ax = plt.subplots(figsize=TAM)
    fig.subplots_adjust(left=0.30, right=0.93, top=0.80, bottom=0.16)
    y = list(range(len(etapas)))[::-1]
    ax.barh(y, [e[1] for e in etapas], color=[e[2] for e in etapas], height=0.62, edgecolor="white", linewidth=2)
    ax.set_yticks(y, [e[0] for e in etapas], fontsize=14)
    for yi, (_, n, _) in zip(y, etapas):
        ax.text(n + 1.2, yi, f"{n}", va="center", fontsize=18, fontweight="bold")
    ax.text(3 + 7, 0, "sirolimus oral · arimoclomol · niacina", va="center", fontsize=15, color=TINTA)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Número de fármacos", fontsize=13)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.text(0.02, 0.94, "De 86 fármacos a 3: cómo elegimos", fontsize=24, fontweight="bold", va="top")
    fig.text(0.02, 0.875, "Se descartan los no aprobados y los que bajarían aún más BUBR1 (HSP90, PLK1, Aurora, MPS1, APC/C)",
             fontsize=14, color=TINTA_2, va="top")
    fig.text(0.02, 0.03, "La niacina se agregó a mano como hipótesis especulativa (vía NAD⁺–SIRT2–BubR1). "
             "Fuente: results/candidatos_farmacos.tsv", fontsize=11.5, color=TINTA_2)
    return guardar(fig, "video_3_embudo_farmacos.png")


NOMBRES = {
    "SIROLIMUS": "Sirolimus", "TEMSIROLIMUS": "Temsirolimus", "ARIMOCLOMOL": "Arimoclomol",
    "EVEROLIMUS": "Everolimus", "SODIUM PHENYLBUTYRATE": "Fenilbutirato sódico", "TRAMETINIB": "Trametinib",
    "SELUMETINIB": "Selumetinib", "CELECOXIB": "Celecoxib", "CRIZOTINIB": "Crizotinib", "DASATINIB": "Dasatinib",
    "BORTEZOMIB": "Bortezomib", "NIACIN": "Niacina",
}
FINAL = {"SIROLIMUS", "ARIMOCLOMOL", "NIACIN"}
ALTERNATIVAS = {"TEMSIROLIMUS", "DASATINIB", "TRAMETINIB", "SELUMETINIB"}


def video_4_puntajes():
    """Puntaje de 0 a 100 de los mejores candidatos y qué pasó con cada uno."""
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
    for yi, (f, p) in enumerate(zip(top.farmaco, top.puntaje)):
        ax.text(p + 0.8, yi, f"{p:.1f}".replace(".", ","), va="center", fontsize=13, color=TINTA)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Puntaje (0 a 100)", fontsize=13)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(handles=[Patch(color=FARMACO, label="En el esquema propuesto"),
                       Patch(color=ALTERNATIVA, label="Alternativa o condicional"),
                       Patch(color=GRIS, label="No seleccionado")],
              loc="center left", bbox_to_anchor=(1.0, 0.5), frameon=False, fontsize=13)
    fig.text(0.02, 0.94, "Puntaje de los mejores candidatos", fontsize=24, fontweight="bold", va="top")
    fig.text(0.02, 0.875, "Seis criterios: vínculo con el mecanismo 25 · seguridad en niños 20 · evidencia 15 · "
             "ajuste al caso 15 · innovación 15 · validación 10", fontsize=13.5, color=TINTA_2, va="top")
    fig.text(0.02, 0.03, "Everolimus no se elige porque repite el mecanismo de sirolimus. Bortezomib sale por la revisión "
             "biológica: retrasa la salida de la mitosis. Niacina entra por innovación, no por puntaje.",
             fontsize=11.5, color=TINTA_2)
    return guardar(fig, "video_4_puntajes_candidatos.png")


def video_5_propuesta():
    """Dos tratamientos en paralelo: el estándar para el tumor y la propuesta para el MVA."""
    fig, ax = lienzo()
    titulo(ax, "La propuesta: dos tratamientos en paralelo",
           "El tumor ya tiene tratamiento estándar; la enfermedad de fondo no tiene ninguno")

    caja(ax, 0.4, 2.6, 5.6, 4.6, borde=TINTA_2, lw=2.2)
    ax.text(3.2, 6.65, "Oncología estándar", ha="center", fontsize=19, fontweight="bold")
    ax.text(3.2, 6.05, "trata el rabdomiosarcoma", ha="center", fontsize=14, color=TINTA_2)
    ax.text(3.2, 4.55, "VAC a intensidad reducida\n\nvincristina\nactinomicina D\nciclofosfamida",
            ha="center", va="center", fontsize=14.5, linespacing=1.3)
    ax.text(3.2, 2.95, "Duración acotada · no es reposicionamiento", ha="center", fontsize=12.5, color=TINTA_2)

    caja(ax, 6.5, 2.6, 9.1, 4.6, borde=FARMACO, fondo=FONDO_VERDE, lw=2.6)
    ax.text(11.05, 6.65, "Nuestra propuesta de reposicionamiento", ha="center", fontsize=19, fontweight="bold")
    ax.text(11.05, 6.05, "trata el MVA de fondo · esquema continuo", ha="center", fontsize=14, color=TINTA_2)
    filas = [
        ("Sirolimus oral", "frena mTORC1: envejecimiento precoz,\nmúsculo y crecimiento"),
        ("Arimoclomol", "ayuda al plegamiento:\nmás BUBR1 (la causa)"),
        ("Niacina", "vía NAD⁺–SIRT2: más BUBR1\n(hipótesis especulativa)"),
    ]
    for i, (farm, que) in enumerate(filas):
        yy = 5.15 - i * 0.98
        ax.text(6.9, yy, farm, fontsize=16, fontweight="bold", color=TINTA, va="center")
        ax.text(9.6, yy, que, fontsize=12.5, color=TINTA, va="center", linespacing=1.15)

    caja(ax, 0.4, 0.35, 15.2, 1.85, borde=TINTA_2, fondo="white", lw=1.2)
    ax.text(0.75, 1.62, "Cómo se comprueba:", fontsize=14.5, fontweight="bold", va="center")
    ax.text(4.0, 1.62, "fibroblastos del paciente antes y después de cada fármaco → cantidad de BUBR1 (Western blot)\n"
            "y fuerza del checkpoint mitótico (ensayo con nocodazol)", fontsize=12.5, va="center", linespacing=1.25)
    ax.text(0.75, 0.75, "Además:", fontsize=14.5, fontweight="bold", va="center")
    ax.text(4.0, 0.75, "hemogramas periódicos y resonancia por el hallazgo en LZTR1",
            fontsize=12.5, va="center")
    return guardar(fig, "video_5_propuesta.png")


if __name__ == "__main__":
    for f in (video_1_caso, video_2_metodo, video_3_embudo_farmacos, video_4_puntajes, video_5_propuesta):
        print(f())
