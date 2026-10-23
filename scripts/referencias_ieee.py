"""Convierte las citas [Autor Año] del informe en inglés a formato IEEE numerado.

1. Lee docs/report_track2_en.md y toma las citas [Autor Año] en orden de aparición.
2. Para cada una busca el PMID en CITAS y baja autor, título, revista, volumen,
   número, páginas, fecha y DOI de PubMed (NCBI E-utilities). Así cada referencia
   queda verificada contra PubMed, no escrita de memoria.
3. Reemplaza cada [Autor Año] por [n] y escribe la lista en la sección References.

Se corre una sola vez, al cerrar el informe: sobre un informe ya numerado no
encuentra citas y no hace nada. Mientras corre usa docs/report_track2_en.autores.md
como copia de la versión con [Autor Año]; esa copia se borra al terminar para que
nadie edite un archivo que ya no es el informe.

Uso: python scripts/referencias_ieee.py
"""
import json
import re
import shutil
import time
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
INFORME = RAIZ / "docs" / "report_track2_en.md"
FUENTE = RAIZ / "docs" / "report_track2_en.autores.md"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

CITAS = {
    "SageBio 2026": None,  # dataset del reto: referencia manual (ver MANUALES)
    "Karczewski 2020": 32461654, "McLaren 2016": 27268795, "Landrum 2018": 29165669,
    "Schubach 2024": 38183205, "Martin 2019": 31676867, "Varadi 2022": 34791371,
    "Hekkelman 2023": 36424442, "Cannon 2024": 37953380, "Buniello 2025": 39657122,
    "Morales 2022": 35388217, "Richards 2015": 25741868, "Tavtigian 2020": 32720330,
    "Abou Tayoun 2018": 30192042, "Pejaver 2022": 36413997, "Ioannidis 2016": 27666373,
    "Cheng 2023": 37733863, "Nagy 1998": 9644970, "Dieckhaus 2024": 38285937,
    "Bitterman 2002": 12297502, "Suijkerbuijk 2010": 20516114, "Piotrowski 2014": 24362817,
    "Perrino 2025": 39937237, "Oh 2024": 38296790, "Wang 2004": 14576056, "Baker 2004": 15208629,
    "Baker 2011": 22048312, "Sieben 2020": 31738183, "Dai 2004": 14744753, "Hanks 2004": 15475955,
    "Ham 2020": 32908143, "Mascarenhas 2019": 31513481, "Gupta 2024": 38936378, "Zhu 2015": 25754370,
    "North 2014": 24825348, "Cramer 2024": 39487711, "Wu 2023": 38009412, "Suematsu 2014": 25285631,
    "Hwang 2017": 28417163, "Nishitani-Isa 2019": 31184400, "Guenther 2013": 23684925,
    "Hebron 2023": 36322002, "Eckstein 2022": 35363510, "Yamada 2006": 17172401,
    "Defachelles 2021": 34343032, "Nakano 2024": 39264246,
}
MANUALES = {
    "SageBio 2026": "Sage Bionetworks, “Rare Disease, Real Kid: MVA Hackathon 2026 dataset,” Hugging Face, "
                    "SageBio/mva-hackathon-2026-data, 2026. [TO REPLACE with the dataset reference given on the "
                    "Hackathon Synapse page, as required by the challenge rules.]",
}
MESES = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]


def paginas(p):
    """'1159-61' -> '1159–1161' (PubMed abrevia el final del rango); 'D1062-D1067' -> 'D1062–D1067'."""
    m = re.fullmatch(r"([A-Za-z]?)(\d+)-([A-Za-z]?)(\d+)", p or "")
    if not m:
        return p
    letra, ini, _, fin = m.groups()
    if len(fin) < len(ini):
        fin = ini[: len(ini) - len(fin)] + fin
    return f"{letra}{ini}–{letra}{fin}"


def autor(nombre):
    """'Suijkerbuijk SJ' -> 'S. J. Suijkerbuijk'."""
    partes = nombre.rsplit(" ", 1)
    if len(partes) == 1:
        return nombre
    apellido, iniciales = partes
    return " ".join(f"{i}." for i in iniciales) + " " + apellido


def formatear(r):
    autores = [a["name"] for a in r["authors"] if a.get("authtype") == "Author"]
    if len(autores) > 6:
        txt_aut = autor(autores[0]) + " et al."
    elif len(autores) == 2:
        txt_aut = autor(autores[0]) + " and " + autor(autores[1])
    elif len(autores) > 2:
        txt_aut = ", ".join(autor(a) for a in autores[:-1]) + ", and " + autor(autores[-1])
    else:
        txt_aut = autor(autores[0])
    titulo = r["title"].rstrip(".")
    partes = [f"{txt_aut}, “{titulo},” *{r['source']}*"]
    if r.get("volume"):
        partes.append(f"vol. {r['volume']}")
    if r.get("issue"):
        partes.append(f"no. {r['issue']}")
    pags = paginas(r.get("pages"))
    if pags:
        partes.append(f"pp. {pags}" if "–" in pags else f"Art. no. {pags}")
    fecha = r["pubdate"].split()
    mes = f"{MESES[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(fecha[1])]} " \
        if len(fecha) > 1 and fecha[1] in ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec") else ""
    partes.append(f"{mes}{fecha[0]}")
    doi = next((i["value"] for i in r["articleids"] if i["idtype"] == "doi"), None)
    texto = ", ".join(partes)
    if doi:
        texto += f", doi: {doi}"
    return texto + f". PMID: {r['uid']}."


def main():
    if not FUENTE.exists():
        shutil.copyfile(INFORME, FUENTE)
    md = FUENTE.read_text(encoding="utf-8")
    cuerpo, _, _ = md.partition("## References")
    patron = re.compile(r"\[([A-Z][A-Za-z\- ]+ \d{4})\]")
    orden = []
    for m in patron.finditer(cuerpo):
        if m.group(1) not in orden:
            orden.append(m.group(1))
    if not orden:
        FUENTE.unlink()
        raise SystemExit("No hay citas [Autor Año]: el informe ya está numerado. Nada que hacer.")
    faltan = [c for c in orden if c not in CITAS]
    if faltan:
        raise SystemExit(f"Citas sin PMID en CITAS: {faltan}")

    pmids = [str(CITAS[c]) for c in orden if CITAS[c]]
    res = requests.get(EUTILS, params={"db": "pubmed", "retmode": "json", "id": ",".join(pmids)},
                       headers={"User-Agent": "mva-hackathon-2026"}, timeout=60).json()["result"]
    time.sleep(0.4)

    numero = {c: i + 1 for i, c in enumerate(orden)}
    lista = []
    for c in orden:
        texto = MANUALES[c] if CITAS[c] is None else formatear(res[str(CITAS[c])])
        lista.append(f"[{numero[c]}] {texto}")

    nuevo = patron.sub(lambda m: f"[{numero[m.group(1)]}]", cuerpo)
    nuevo = nuevo.rstrip() + "\n\n## References\n\n" + "\n\n".join(lista) + "\n"
    INFORME.write_text(nuevo, encoding="utf-8", newline="\n")
    FUENTE.unlink()
    print(f"{len(orden)} referencias numeradas en {INFORME.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
