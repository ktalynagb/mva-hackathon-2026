# Bitácora del Proyecto — MVA Hackathon 2026

**Track 2 — Reposicionamiento de Fármacos**  
**Repo:** https://github.com/ktalynagb/mva-hackathon-2026  
**Deadline:** 24 de octubre de 2026, 23:59 UTC  
**Equipo:** Ktalyna · Laura

> Registra qué se hizo, quién lo hizo, qué se decidió y qué sigue.  
> Cada entrada nueva va **arriba**. Formato: `## YYYY-MM-DD — Título`.

---

## 2026-10-01 — Notebook 05: mecanismo biológico BUB1B/BUBR1

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Creado `notebooks/05_mecanismo_biologico_bub1b.ipynb` — mecanismo completo para Hitos H2 y H3
- Documenta: estructura BUBR1 (5 dominios), SAC normal, efecto de p.Leu737Ter (NMD/LOF) y p.Asn1002Lys (missense pseudo-kinasa), cascada hasta mosaicismo, fenotipo clínico
- Genera 3 figuras: dominios BUBR1 · SAC normal vs disfuncional · cascada fisiopatológica
- Produce `results/resumen_mecanismo_para_R4.json` (6 targets farmacológicos para R4) y `results/hito_H3_mecanismo_completo.json`

**Targets identificados para R4:**
- APC/C · CDC20 · PLK1 (Volasertib) · Aurora B (Barasertib) · Hsp90 (estabilizador alelo missense) · p53 pathway

**Pendiente (R3):**
- [ ] Revisar y completar secciones de literatura (referencias en celda 7)
- [ ] Confirmar CADD de p.Asn1002Lys (notebook 04) antes de entregar a R4

---

## 2026-10-01 — Notebook 04: priorización gnomAD y variante causante

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Creado `notebooks/04_priorizacion_gnomad_variante_causante.ipynb`
- Pipeline completo: het. BUB1B → gnomAD v4 (GraphQL) → AF < 1% → myvariant.info (CADD/ClinVar) → tabla de priorización → confirmación het. compuesta
- Genera `results/bub1b_variantes_priorizadas.csv`, `results/figura_01_priorizacion_bub1b.png`, `results/hito_H1_variante_causante.json`
- Incluye búsqueda de alternativas en CEP57/TRIP13 para descartar otras causas

**Hipótesis documentada:**
- BUB1B het. compuesta: `15:40209701 p.Leu737Ter` (stop → NMD → LOF) + `15:40220612 p.Asn1002Lys` (missense dominio kinasa)
- Criterios ACMG aplicados en el notebook: PVS1, PM1, PM2, PM3, PP2, PP3

**Pendiente (R2):**
- [ ] Correr el notebook con el VCF real y verificar que gnomAD v4 confirma AF < 1% para ambas variantes
- [ ] Confirmar CADD score para p.Asn1002Lys (≥ 20 refuerza patogenicidad)

---

## 2026-10-01 — Plan de equipo para 6 personas

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Se creó `docs/plan_equipo_roles.md` con 6 roles (R1–R6), el perfil de habilidades de cada uno en %, sus tareas por semana, 7 hitos (H1–H7), una matriz de dueños/revisores y reglas de fidelidad al rol

**Decisiones:**
- Semanas de jueves a miércoles: S1 = variante, S2 = mecanismo, S3 = fármacos + borrador, S4 = entrega
- Congelación del código el **viernes 23 oct a las 12:00 UTC**; entrega interna el **sábado 24 oct a las 18:00 UTC** (6 h de margen)
- A partir de ahora: trabajo en ramas `rN/...` y PR con revisor; nada directo a `master`

**Pendiente:**
- [ ] Las 6 personas eligen rol y se anotan en la sección 7 del plan
- [ ] Cada integrante confirma su propio acceso aprobado en HF

---

## 2026-10-01 — Integración del trabajo de Laura al repo

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Se revisó el Colab de Laura (`Versión actualizada fase 1 - 2.ipynb`)
- Se reconstruyó como `notebooks/03_exploracion_Laura_201_genes.ipynb` y se subió al repo
- Se creó `scripts/resolve_genes.py` (coordenadas via MyGene.info)
- Se creó `config/genes_candidatos.txt` (lista base ~200 genes, pendiente confirmar con Laura)

**Hallazgos / decisiones:**
- ✅ Corrección importante: las homocigotas de BUB1B y CEP57 son polimorfismos comunes (AF > 15% en gnomAD) — **no son la causa**
- ✅ Corrección importante: el "ROH" de MAD1L1 no era tal — hay heterozigotas entremezcladas, 23% homocigotas vs 39% del genoma. Sin evidencia de consanguinidad en ese locus
- ✅ Con 201 genes: 19,099 variantes PASS en 195 genes
- 🔍 Causa probable adelantada por Laura (desde notebook 04 en Colab): **BUB1B het. compuesto — p.Leu737Ter (15:40209701) + p.Asn1002Lys (15:40220612)**

**Pendiente:**
- [ ] Laura: confirmar/reemplazar `config/genes_candidatos.txt` con su lista original de 201 genes
- [ ] Laura: subir notebook 04 al repo (priorización gnomAD + identificación variante)

---

## 2026-09-17 — Exploración inicial + filtrado por 6 genes

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Inicializado el repo en GitHub (`ktalynagb/mva-hackathon-2026`, privado)
- Configurado entorno Python (`.venv/`, `requirements.txt`)
- Autenticación en HuggingFace y verificación de acceso al dataset gated
- Descargados los archivos relevantes para Track 2 (~303 MB):
  - `WGS_EX2312012_HGWCNDSX7.vcf.gz` (300.6 MB)
  - `WGS_EX2312012_HGWCNDSX7.vcf.gz.tbi` (2.2 MB)
  - `Challenge_Clinical_Phenotype_1.docx`
- Invitada Laura (`lauracamilavargas-lang`) como colaboradora admin

**Hallazgos del VCF:**
- 5,012,204 variantes totales · 4,740,790 PASS (94.6%)
- 81.4% SNV · 18.6% INDEL
- Muestra única: `WGS_EX2312012` · Pipeline: Sentieon Haplotyper + GATK VariantFiltration · Referencia: GRCh38 (sin prefijo `chr`)

**Hallazgos del fenotipo (HPO):**

| Característica | HPO | Nota |
|----------------|-----|------|
| Rabdomiosarcoma | HP:0002859 | Evento que inició la investigación |
| Nefrocalcinosis | HP:0000121 | Desde el nacimiento |
| Talla baja | HP:0004322 | |
| Falla de medro | HP:0001508 | |
| Atrofia muscular | HP:0003202 | |
| Prematuridad (32 sem) | HP:0001622 | |
| Pequeño para edad gestacional (~1 kg) | HP:0001518 | RCIU severo |
| Abortos recurrentes (parentales) | HP:0200067 | Señal de herencia |

**Filtrado por 6 genes candidatos (BUB1B, CEP57, TRIP13, BUB1, MAD1L1, MAD2L1):**
- 1,075 variantes PASS
- BUB1B: 16 total · 7 homocigotas · 9 heterocigotas
- CEP57: 7 total · 3 homocigotas · 4 heterocigotas
- TRIP13: 3 total · 0 homocigotas · 3 heterocigotas

**Decisiones:**
- No descargar FASTQ (~79 GB) — innecesarios para Track 2
- Herencia esperada: autosómica recesiva → buscar hom. o het. compuesto

**Archivos creados:**
- `notebooks/01_exploracion_inicial.ipynb`
- `notebooks/02_filtrado_vcf_genes_mva.ipynb`
- `scripts/filter_mva_genes.py`
- `results/mva_gene_coords_grch38.json`
- `docs/plan_de_trabajo.md`

---

## Estado actual del proyecto

### Fases

| Fase | Descripción | Estado | Responsable |
|------|-------------|--------|-------------|
| 1 | Datos y exploración | ✅ Completa | Ktalyna + Laura |
| 2 | Identificar variante causante | 🔄 En progreso | Laura (nb04 en Colab) |
| 3 | Caracterizar mecanismo biológico | ⬜ Pendiente | — |
| 4 | Candidatos de reposicionamiento | ⬜ Pendiente | — |
| 5 | Informe + entrega | ⬜ Pendiente | — |

### Hipótesis actual

La causa del MVA en este paciente es probablemente una **variante heterocigótica compuesta en BUB1B**:
- Variante 1: `15:40209701` → **p.Leu737Ter** (stop prematuro — pérdida de función)
- Variante 2: `15:40220612` → **p.Asn1002Lys** (missense — por confirmar patogenicidad)

Ambas heterocigotas en *BUB1B* (BUBR1) afectarían el Spindle Assembly Checkpoint → inestabilidad cromosómica → mosaicismo aneuplo → fenotipo MVA.

**Esta hipótesis debe confirmarse en el notebook 04** (frecuencia gnomAD < 1%, impacto funcional, ausencia en ClinVar como benigna).

---

## Pendientes globales

- [ ] Laura sube notebook 04 al repo
- [ ] Laura confirma `config/genes_candidatos.txt`
- [ ] Asignar los 6 roles del [plan de equipo](plan_equipo_roles.md) (Fase 3 = R3, Fase 4 = R4, video = R6)
- [ ] Completar `methods_description_form.xlsx` antes del 24 oct
