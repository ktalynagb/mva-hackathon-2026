# Plan de Trabajo — Track 2: Reposicionamiento de Fármacos

**MVA Hackathon 2026 · Deadline: 24 de octubre de 2026, 23:59 UTC**

> Quién hace qué y en qué semana está en el **[plan de equipo y roles](plan_equipo_roles.md)**. Los responsables de las tablas de abajo corresponden a esos roles (R1–R6).

---

## Fase 1 — Datos y Exploración ✅ Completada

| Tarea | Notebook / Script | Estado |
|-------|-------------------|--------|
| Configurar repo, entorno Python, acceso HuggingFace | — | ✅ |
| Descargar datos relevantes (~303 MB: VCF + índice + fenotipo) | `scripts/download_data.py` | ✅ |
| Explorar estructura del VCF y fenotipo clínico HPO | `notebooks/01_exploracion_inicial.ipynb` | ✅ |
| Filtrar VCF por genes candidatos MVA | `notebooks/02_filtrado_vcf_genes_mva.ipynb` | ✅ |

**Hallazgos clave:**
- 5,012,204 variantes totales · 4,740,790 pasan filtros de calidad
- Fenotipo: rabdomiosarcoma + nefrocalcinosis + RCIU + prematuridad + abortos recurrentes parentales → diagnóstico MVA
- **BUB1B: 7 variantes homocigotas** (gen #1 en MVA, ~50% de casos)
- **CEP57: 3 variantes homocigotas** (incluyendo 2 inserciones)
- TRIP13: 3 variantes heterocigotas (menos probable como causa primaria)
- MAD1L1: patrón ROH de ~418 kb, consistente con posible consanguinidad parental

---

## Fase 2 — Identificar la Variante Causante ⬜ Pendiente

**Objetivo:** de las variantes en BUB1B y CEP57, identificar cuál es patogénica.

| Tarea | Notebook | Responsable |
|-------|----------|-------------|
| Cruzar variantes BUB1B/CEP57 con gnomAD v4 (API GraphQL) | `03_priorizacion_gnomad.ipynb` | — |
| Filtrar por frecuencia: AF < 0.01 en todas las poblaciones | — | — |
| Aplicar criterios funcionales: LOF / missense con CADD ≥ 20 | — | — |
| Consultar ClinVar para clasificación existente | — | — |
| **Conclusión:** variante causante + patrón de herencia | — | — |

**Criterios de priorización (orden):**
1. Variante LOF (frameshift, nonsense, splice ±2 pb)
2. Missense con CADD ≥ 20 y AF gnomAD < 0.001
3. Missense con CADD 15-20 y AF gnomAD < 0.01
4. Patrón homocigótico preferido sobre het. compuesta (más fácil de interpretar)

---

## Fase 3 — Caracterizar el Mecanismo Biológico ⬜ Pendiente

**Objetivo:** describir con rigor científico qué hace la variante y cuál es la consecuencia celular.

| Tarea | Notebook | Responsable |
|-------|----------|-------------|
| Gen afectado → proteína → función en el SAC | `04_mecanismo_biologico.ipynb` | — |
| Tipo de efecto molecular: LOF / GOF / dominante negativo | — | — |
| Consecuencia celular: fallo SAC → missegregación → mosaicismo | — | — |
| Diagrama de la vía afectada (figura para el informe) | — | — |
| Revisión de literatura: casos MVA con misma variante o gen | — | — |

**Marco teórico a cubrir:**
- Spindle Assembly Checkpoint (SAC): BUB1B/BUBR1, MAD1/MAD2, MCC
- Cómo la pérdida de función del gen identificado impide el arresto mitótico
- Consecuencia fenotípica: inestabilidad cromosómica → mosaicismo aneuplo → cáncer/malformaciones

---

## Fase 4 — Reposicionamiento de Fármacos ⬜ Pendiente

**Objetivo:** proponer fármacos aprobados (FDA/EMA) con mecanismo relevante para la vía afectada.

| Tarea | Notebook | Responsable |
|-------|----------|-------------|
| Consultar OpenTargets para el gen identificado | `05_candidatos_farmacos.ipynb` | — |
| Consultar ChEMBL / DrugBank por targets en la vía SAC | — | — |
| Filtrar por: aprobación FDA/EMA, seguridad pediátrica, evidencia | — | — |
| Rankear candidatos con justificación mecanística | — | — |
| Tabla final: top 3-5 candidatos con dosis, indicación actual, propuesta | — | — |

**Fuentes a consultar:**
- [OpenTargets Platform](https://platform.opentargets.org/)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [DrugBank](https://go.drugbank.com/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/) (ensayos en curso)
- Literatura: PubMed + Google Scholar (búsqueda por gen + "drug repurposing" o "therapeutic")

---

## Fase 5 — Informe y Entrega ⬜ Pendiente

| Entregable | Archivo | Deadline |
|-----------|---------|----------|
| Informe final (PDF/Markdown) | `docs/informe_final.md` → PDF | 24 oct |
| Formulario de métodos | `methods_description_form.xlsx` | 24 oct |
| Video pitch 3 min | enlace externo (referenciado en README) | 24 oct |
| Código documentado y reproducible | notebooks + scripts en este repo | 24 oct |

**Estructura del informe:**
1. Introducción: qué es MVA, relevancia del caso clínico
2. Métodos: pipeline bioinformático, fuentes, herramientas de IA utilizadas
3. Resultados
   - 3.1 Variante identificada y evidencia de patogenicidad
   - 3.2 Mecanismo biológico
   - 3.3 Candidatos de reposicionamiento
4. Discusión: limitaciones, escalabilidad, próximos pasos clínicos
5. Referencias

---

## Criterios de Evaluación (recordatorio)

| Criterio | Peso | Cómo maximizarlo |
|---------|------|-----------------|
| **Rigor científico** | 35% | Evidencia sólida para la variante; citar bases de datos y literatura |
| **Impacto clínico** | 25% | Candidatos con evidencia pediátrica o en enfermedades raras |
| **Innovación** | 25% | Mecanismo no obvio, conexión inesperada entre vía y fármaco |
| **Escalabilidad** | 15% | Pipeline reproducible, bien documentado, generalizable a otros casos MVA |

---

## Notas técnicas

- **Entorno:** Python 3.13 + `.venv/` — ver `requirements.txt`
- **Datos:** `data/raw/` no se versiona (`.gitignore`) — descargar con `scripts/download_data.py`
- **VCF:** GRCh38, sin prefijo `chr`, llamado con Sentieon Haplotyper + GATK VariantFiltration
- **gnomAD:** usar v4 (GRCh38) para frecuencias poblacionales
- **En Windows:** `pysam`/`cyvcf2` no están disponibles — usar `PyVCF3` o parsing manual con `gzip`
