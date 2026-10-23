# MVA Hackathon 2026 — Track 2: Reposicionamiento de Fármacos

**Equipo:** A3 EMBS ITBA   
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
├── docs/               # Informe final, plan de trabajo, roles del equipo y bitácora
├── results/            # Salidas del análisis: candidatos, tablas, figuras
├── .gitignore
├── CLAUDE.md           # Contexto del proyecto para sesiones de Claude Code
├── requirements.txt    # Dependencias Python
└── README.md
```

---

## Equipo y organización

- **[Plan de equipo por tareas](docs/plan_equipo_tareas.md)**: tablero de tareas por área (variante, mecanismo, fármacos, código, informe) con fechas e hitos. **Léelo antes de empezar y toma una tarea libre.**
- [Plan de trabajo por fases](docs/plan_de_trabajo.md)
- [Bitácora](docs/bitacora.md): seguimiento de avances y decisiones

---

## Entregables finales

| # | Entregable | Estado |
|---|-----------|--------|
| 1 | Informe PDF/Markdown con mecanismo + candidatos | ✅ [`docs/A3-EMBS-ITBA_track2_report.pdf`](docs/A3-EMBS-ITBA_track2_report.pdf) (11 pág., IEEE) |
| 2 | Código documentado y reproducible | ✅ `python run_pipeline.py` (8 pasos, 6 min 11 s) |
| 3 | Video pitch 3 min | ✅ [YouTube](https://www.youtube.com/watch?v=J1OovR5hoWQ) |
| 4 | Formulario de descripción de métodos | ✅ [`envios/track2/`](envios/track2/) |

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

### 1. Clonar el repositorio

```bash
git clone https://github.com/ktalynagb/mva-hackathon-2026.git
cd mva-hackathon-2026
```

### 2. Crear entorno virtual e instalar dependencias

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
pip install python-docx   # para leer el fenotipo clínico
```

### 3. Autenticarse en Hugging Face

Necesitas una cuenta en [huggingface.co](https://huggingface.co) con acceso aprobado al dataset `SageBio/mva-hackathon-2026-data` (solicitud manual requerida).

```bash
python scripts/hf_login.py
# Pega tu token cuando lo pida (Settings → Access Tokens en hf.co)
```

### 4. Descargar los datos necesarios para Track 2

> Los FASTQs (~79 GB) **no son necesarios** para Track 2. Solo descargamos el VCF + fenotipo (~303 MB).

```bash
python scripts/download_data.py --file README.md
python scripts/download_data.py --file "Challenge_Clinical_Phenotype_1.docx"
python scripts/download_data.py --file "WGS_EX2312012_HGWCNDSX7.vcf.gz.tbi"
python scripts/download_data.py --file "WGS_EX2312012_HGWCNDSX7.vcf.gz"
```

Los archivos quedan en `data/raw/`.

### 5. Exploración inicial

Abre y corre el notebook de exploración:

```bash
jupyter notebook notebooks/01_exploracion_inicial.ipynb
```

Este notebook te lleva por: verificación del entorno → fenotipo clínico HPO → estadísticas del VCF → estrategia de análisis propuesta.

### 6. Correr todo el análisis con un comando

```bash
python run_pipeline.py            # todos los pasos
python run_pipeline.py --listar   # ver los pasos
python run_pipeline.py --solo farmacos,figuras
```

Los ocho pasos corren en orden y el pipeline se detiene en el primero que falle, imprimiendo al final el estado y la duración de cada uno.

| Paso | Script | Salida | Necesita el VCF | Tiempo |
|---|---|---|---|---|
| `genes` | `scripts/unir_grupos_genes.py` | `config/genes_candidatos.txt` | no | < 1 s |
| `diagnostico` | `scripts/diagnostico_diferencial.py` | `results/diagnostico_diferencial_*.tsv` (no se versionan) | **sí** | 158 s |
| `dominante` | `scripts/modelo_dominante.py` | `data/dominante/` (no se versiona) | **sí** | 107 s |
| `genes_equipo` | `scripts/analisis_genes_equipo.py` | `data/genes_equipo/` (no se versiona) | **sí** | 13 s |
| `alelo2` | `scripts/evidencia_alelo2.py` | `results/evidencia_alelo2.json` | no | 73 s |
| `farmacos` | `scripts/lista_larga_farmacos.py` | `results/candidatos_farmacos.tsv` | no | 6 s |
| `farmacogenetica` | `scripts/farmacogenetica.py` | `data/farmacogenetica/` (no se versiona) | **sí** | 10 s |
| `figuras` | `scripts/figuras_informe.py` | `results/figura_1_*.png`, `figura_2_*.png` | no | 4 s |

El cálculo de estabilidad (`scripts/estabilidad_alelo2.py`) usa la salida de ThermoMPNN, que se corre aparte (instrucciones en el propio script). Se agrega con `--thermompnn DIR`.

**Corrida de referencia:** los 8 pasos en **6 min 11 s** (21 oct 2026, Windows 11, Python 3.13.14, con la caché ya construida), reproduciendo todos los números del informe: 24.604 variantes PASS → 14 funcionales en MANE; 11.808 → 1 candidata dominante en *LZTR1*; 874 → 0 en los genes del equipo; 86 fármacos → 73 pasan los filtros de aprobación.

Todos los pasos consultan APIs públicas y guardan una caché local en `data/cache/`, que no se versiona: una clonación limpia la reconstruye desde las APIs y tarda bastante más, pero así se verifica que el pipeline no dependa de estado local. Para la reproducción exacta, instala `requirements-lock.txt`, que fija las versiones con las que se generaron los resultados (Python 3.13).

**Dos archivos guardan curación manual y el pipeline los preserva al regenerar:** `config/genes_modelo_dominante.tsv` reinyecta los genes de `config/genes_dominante_extra.tsv`, y `results/candidatos_farmacos.tsv` conserva la puntuación de los seis criterios y las filas agregadas a mano. Si se editan a mano, los cambios sobreviven a la siguiente corrida.

---

## Escalabilidad: cómo usarlo con otro paciente

| Parte | ¿Sirve para otro paciente? | Qué cambiar |
|---|---|---|
| Diagnóstico diferencial (321 genes de mitosis, cinetocoro, centrosoma, cohesina, reparación y ciclo celular) | **Sí**, sin cambios de código | Poner su VCF (GRCh38) en `data/raw/` y correr `python run_pipeline.py --solo diagnostico`. El panel se edita en `config/genes_candidatos.txt` |
| Clasificación ACMG, NMD y estructura | Parcial: el método es general, pero `evidencia_alelo2.py` está escrito para el residuo 1002 de BUBR1 | Cambiar el residuo y la proteína en el script |
| Lista larga de fármacos | **Sí** para otro paciente con MVA por *BUB1B*: las líneas terapéuticas dependen del mecanismo, no de la variante | Para otro gen (*CEP57*, *TRIP13*), editar las semillas y la dirección de acción en `config/lineas_terapeuticas.json` |
| Priorización (matriz C1) | **Sí**: filtros y criterios no dependen del caso | Solo K2 (edad del paciente) y K4 (órganos afectados) |

Ningún paso sube datos del paciente al repositorio. Las cachés con variantes del paciente quedan en `data/cache/` y `results/cache/`, que están excluidas por `.gitignore`.

---

## Video pitch

**https://www.youtube.com/watch?v=J1OovR5hoWQ**

Guion y figuras en [`docs/paquete_video.md`](docs/paquete_video.md) y `results/video/`.

---

## Licencia

Este repositorio es de uso exclusivo para la participación en el hackathon.
