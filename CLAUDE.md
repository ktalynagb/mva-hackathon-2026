# Contexto del Proyecto — MVA Hackathon 2026

## Evento
**Rare Disease, Real Kid: MVA Hackathon 2026**  
Organizadores: EMBS ITBA / Sage Bionetworks / Hugging Face  
**Fecha límite de entrega: 24 de octubre de 2026, 23:59 UTC**

## Track
**Track 2 — Reposicionamiento de Fármacos**

## Objetivo
1. Caracterizar el **mecanismo biológico** de la variante genética causante de MVA en el caso clínico real:
   - Tipo de efecto: pérdida o ganancia de función
   - Vía biológica afectada (ej: SAC — Spindle Assembly Checkpoint)
   - Consecuencia celular/fenotípica
2. Proponer **fármacos aprobados (FDA/EMA)** para reposicionamiento basado en ese mecanismo.

## Enfermedad
**Mosaic Variegated Aneuploidy (MVA)**: enfermedad rara pediátrica por inestabilidad cromosómica severa. Genes principalmente involucrados: *BUB1B*, *CEP57*, *TRIP13* (genes del punto de control mitótico SAC).

## Dataset
- **Fuente:** `SageBio/mva-hackathon-2026-data` en Hugging Face (dataset cerrado/gated)
- **Tamaño total:** ~85 GB, 11 archivos
- **Contenido:**
  - VCF genómicos (variantes del paciente)
  - BAM/CRAM de secuenciación cruda (opcionales)
  - Datos fenotípicos en formato HPO (Human Phenotype Ontology)
- **Acceso:** requiere solicitud y aprobación manual en HuggingFace

## Criterios de evaluación
| Criterio | Peso |
|---------|------|
| Rigor científico | 35% |
| Impacto clínico potencial | 25% |
| Innovación | 25% |
| Escalabilidad | 15% |

## Entregables
1. Informe (PDF o Markdown): caracterización mecanismo + candidatos fármacos
2. Código documentado y reproducible (`scripts/` + `notebooks/`)
3. Video pitch de 3 minutos (no sube al repo, se referencia con enlace)
4. Formulario de descripción de métodos (`methods_description_form.xlsx`)

## Estructura del repo
```
data/          ← datos gated, NO versionados (.gitignore cubre todo)
notebooks/     ← exploración y análisis interactivo
scripts/       ← código reproducible
docs/          ← informe final
results/       ← outputs (figuras, tablas de candidatos)
```

## Stack técnico (en construcción)
- Python 3.13 + venv en `.venv/`
- `huggingface_hub[cli]` para acceso al dataset
- `cyvcf2` / `pysam` para parseo de VCF/BAM
- `pandas`, `requests` para análisis y consultas a APIs de fármacos (OpenTargets, DrugBank, ChEMBL)

## Notas de sesiones anteriores
- El repo se inicializó el 2026-09-17.
- El dataset aún puede estar pendiente de aprobación de acceso.
- `gh` CLI está disponible (v2.88.1) — se puede usar para crear el repo remoto en GitHub.
- No usar `py` launcher (no instalado), usar `python` directamente.
