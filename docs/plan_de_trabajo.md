# Plan de Trabajo — Track 2: Reposicionamiento de Fármacos

**MVA Hackathon 2026 · Deadline: 24 de octubre de 2026, 23:59 UTC**

> **Las cinco fases están completas (estado al 23 de octubre de 2026).** Variante identificada, mecanismo caracterizado, fármacos priorizados, pipeline reproducible, e informe, formulario y video terminados. **La entrega se envió el 23 de octubre de 2026** y el reto la confirmó.
>
> Este documento es el plan original por fases, escrito al arrancar el proyecto; el seguimiento diario pasó después al [tablero por tareas](plan_equipo_tareas.md) y a la [bitácora](bitacora.md). Se conserva, con los estados al día, porque muestra el recorrido completo de principio a fin.

> Quién hace qué está en el **[plan de equipo por tareas](plan_equipo_tareas.md)**. La columna *Tarea* de las tablas de abajo remite a los IDs de ese tablero (A1, B2…).

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

## Fase 2 — Identificar la Variante Causante ✅ Completada (1 oct)

**Objetivo:** de las variantes en BUB1B y CEP57, identificar cuál es patogénica.

| Paso | Notebook | Tarea | Estado |
|-------|----------|-------------|--------|
| Cruzar variantes BUB1B/CEP57 con gnomAD v4 (API GraphQL) | `04_priorizacion_gnomad_variante_causante.ipynb` | A1 | ✅ |
| Filtrar por frecuencia: AF < 0.01 en todas las poblaciones | idem | A1 | ✅ |
| Aplicar criterios funcionales: LOF / missense con CADD ≥ 20 | idem | A1 | ✅ |
| Consultar ClinVar para clasificación existente | idem | A1 | ✅ |
| **Conclusión:** variante causante + patrón de herencia | idem | A1 | ✅ |
| Redacción ACMG formal + diagnóstico diferencial | `docs/secciones/01_variante_causante.md` | A2, A3 | ✅ clasificación con el sistema de puntos; alelo 1 probablemente patogénico (9 pts), alelo 2 VUS inclinada a patogénica |
| Calidad de lectura de las variantes + lollipop plot | notebook 04 · `scripts/figuras_informe.py` | A4, A5 | ✅ GQ 99 y fracción alélica 0,54/0,46 documentadas; figura 1 del informe |

**Resultado confirmado:**
- `15:40209701` → **p.Leu737Ter** (stop_gained · CADD 36 · ClinVar Pathogenic)  
- `15:40220612` → **p.Asn1002Lys** (missense · CADD 24.5 · AF 6.84×10⁻⁷)  
- Patrón: BUB1B heterocigótica compuesta → AR

**Criterios de priorización (orden):**
1. Variante LOF (frameshift, nonsense, splice ±2 pb)
2. Missense con CADD ≥ 20 y AF gnomAD < 0.001
3. Missense con CADD 15-20 y AF gnomAD < 0.01
4. Patrón homocigótico preferido sobre het. compuesta (más fácil de interpretar)

---

## Fase 3 — Caracterizar el Mecanismo Biológico ✅ Completada

**Objetivo:** describir con rigor científico qué hace la variante y cuál es la consecuencia celular.

| Paso | Notebook | Tarea | Estado |
|-------|----------|-------------|--------|
| Gen afectado → proteína → función en el SAC | `05_mecanismo_biologico_bub1b.ipynb` · `docs/secciones/02_marco_biologico.md` | B1 | ✅ |
| Tipo de efecto molecular: LOF / GOF / dominante negativo | idem · `scripts/evidencia_alelo2.py` | B2, B3 | ✅ **pérdida de función por falta de cantidad de proteína**, no de actividad. NMD sigue siendo *predicho* por la regla de los 55 nt, no medido: queda declarado como limitación |
| Consecuencia celular: fallo SAC → missegregación → mosaicismo | idem | B4 | ✅ resumen de una página en `02b_resumen_mecanismo.md` |
| Diagrama de la vía afectada (figura para el informe) | `scripts/figuras_informe.py`, `figuras_report_en.py` | B5 | ✅ figuras 1 y 2 del informe, más 7 en inglés para el PDF |
| Revisión de literatura: casos MVA con misma variante o gen | idem | B1 | ✅ 47 referencias en el informe final, cada una contrastada con PubMed (autor, revista, volumen, páginas) |

**Marco teórico a cubrir:**
- Spindle Assembly Checkpoint (SAC): BUB1B/BUBR1, MAD1/MAD2, MCC
- Cómo la pérdida de función del gen identificado impide el arresto mitótico
- Consecuencia fenotípica: inestabilidad cromosómica → mosaicismo aneuplo → cáncer/malformaciones

---

## Fase 4 — Reposicionamiento de Fármacos ✅ Completada

**Objetivo:** proponer fármacos aprobados (FDA/EMA) con mecanismo relevante para la vía afectada.

| Paso | Script / documento | Tarea | Estado |
|-------|----------|-------------|--------|
| Definir criterios y pesos de priorización | `docs/secciones/03_criterios.md` | C1 | ✅ seis criterios ponderados (0–100) |
| Consultar DGIdb v5 y Open Targets por línea terapéutica | `scripts/lista_larga_farmacos.py` | C3 | ✅ 86 fármacos en la lista larga |
| Comprobar aprobación en Drugs@FDA y en la EMA | idem | C2, C3 | ✅ verificada directamente en las fuentes, no en la base de interacciones |
| Filtrar y rankear: aprobación, seguridad pediátrica, evidencia | `results/candidatos_farmacos.tsv` | C4 | ✅ 55 candidatos puntuados; excluidos por mecanismo los inhibidores de HSP90, PLK1, Aurora y MPS1 |
| Propuesta final | `docs/secciones/04_candidatos.md` | C5, C6 | ✅ **esquema continuo: sirolimus oral + arimoclomol + niacina.** El tumor lo trata la ciclofosfamida del VAC a intensidad reducida (no es reposicionamiento). Niacina va declarada como hipótesis especulativa |

> El cuaderno `06_agente_reposicionamiento_farmacos.ipynb` fue un primer intento con un LLM (Gemini) y **su salida se descartó**, porque no se podía trazar a fuentes verificables. La lista que se entrega sale del script.

**Fuentes a consultar:**
- [OpenTargets Platform](https://platform.opentargets.org/)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [DrugBank](https://go.drugbank.com/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/) (ensayos en curso)
- Literatura: PubMed + Google Scholar (búsqueda por gen + "drug repurposing" o "therapeutic")

---

## Fase 5 — Informe y Entrega ✅ Completada y enviada

| Entregable | Archivo | Estado |
|-----------|---------|--------|
| Informe final (PDF) | [`envios/track2/A3-EMBS-ITBA_track2_report.pdf`](../envios/track2/A3-EMBS-ITBA_track2_report.pdf) | ✅ 11 páginas, doble columna IEEE, 7 figuras, 47 referencias |
| Formulario de métodos | [`envios/track2/A3_EMBS_ITBA_methods_description_form.xlsx`](../envios/track2/A3_EMBS_ITBA_methods_description_form.xlsx) | ✅ las 11 preguntas de la hoja Track 2 |
| Video pitch 3 min | https://www.youtube.com/watch?v=J1OovR5hoWQ | ✅ publicado |
| Código documentado y reproducible | `python run_pipeline.py` | ✅ 8 pasos en 6 min 11 s, reproduce todos los números del informe |
| **Envío** | sitio del reto · Laura Vargas (`LauraVargas091`) | ✅ **confirmado el 23 oct**, envío 1 |

Qué subir y en qué orden: [`envios/track2/LEEME_ENTREGA.md`](../envios/track2/LEEME_ENTREGA.md).

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
