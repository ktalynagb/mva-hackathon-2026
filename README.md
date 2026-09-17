# MVA Hackathon 2026 — Track 2: Reposicionamiento de Fármacos

**Equipo:** [nombre del equipo]  
**Evento:** Rare Disease, Real Kid — MVA Hackathon 2026  
**Organizadores:** EMBS ITBA / Sage Bionetworks / Hugging Face  
**Fecha límite:** 24 de octubre de 2026, 23:59 UTC

---

## Descripción del reto

La **Aneuploidy Variegada en Mosaico (MVA)** es una enfermedad rara pediátrica causada por variantes en genes del punto de control del ensamblaje del huso mitótico (SAC), principalmente *BUB1B*, *CEP57* y *TRIP13*. El resultado es inestabilidad cromosómica severa, con células que portan diferentes números de cromosomas.

**Track 2** consiste en:

1. **Caracterizar el mecanismo biológico** de la variante genética identificada en el caso clínico real (pérdida/ganancia de función, vía afectada, consecuencia biológica).
2. **Proponer fármacos ya aprobados** (FDA/EMA) que puedan reposicionarse para actuar sobre ese mecanismo.

### Dataset

`SageBio/mva-hackathon-2026-data` en Hugging Face (dataset cerrado, ~85 GB):
- Archivos VCF (variantes genómicas)
- Archivos BAM/CRAM de secuenciación cruda (opcionales)
- Datos fenotípicos en formato HPO

---

## Estructura del repositorio

```
Hackaton_MVA_/
├── data/               # Datos del dataset (NO versionados — ver .gitignore)
│   └── raw/            # Archivos descargados de HuggingFace (VCF, HPO)
├── notebooks/          # Jupyter notebooks de exploración y análisis
├── scripts/            # Scripts Python reproducibles (análisis, procesamiento)
├── docs/               # Informe final (PDF/Markdown) y documentación
├── results/            # Salidas del análisis: candidatos, tablas, figuras
├── .gitignore
├── CLAUDE.md           # Contexto del proyecto para sesiones de Claude Code
├── requirements.txt    # Dependencias Python
└── README.md
```

---

## Entregables finales

| # | Entregable | Estado |
|---|-----------|--------|
| 1 | Informe PDF/Markdown con mecanismo + candidatos | 🔲 Pendiente |
| 2 | Código documentado y reproducible | 🔲 Pendiente |
| 3 | Video pitch 3 min (referenciado, no subido) | 🔲 Pendiente |
| 4 | Formulario de descripción de métodos | 🔲 Pendiente |

---

## Criterios de evaluación

| Criterio | Peso |
|---------|------|
| Rigor científico | 35% |
| Impacto clínico potencial | 25% |
| Innovación | 25% |
| Escalabilidad | 15% |

---

## Cómo reproducir

> **Sección pendiente de completar** — se actualizará una vez definida la pipeline de análisis.

### Requisitos previos

- Python 3.10+
- Acceso aprobado al dataset `SageBio/mva-hackathon-2026-data` en Hugging Face
- Token de Hugging Face con permisos de lectura

### Instalación

```bash
# Clonar el repositorio
git clone <URL-del-repo>
cd Hackaton_MVA_

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS

# Instalar dependencias
pip install -r requirements.txt

# Autenticarse en Hugging Face
hf auth login
```

### Descarga de datos

```bash
# (Una vez autenticado y con acceso aprobado)
python scripts/download_data.py
```

---

## Video pitch

> [Enlace al video — se agrega antes de la entrega]

---

## Licencia

Este repositorio es de uso exclusivo para la participación en el hackathon.
