# Bitácora del Proyecto — MVA Hackathon 2026

**Track 2 — Reposicionamiento de Fármacos**  
**Repo:** https://github.com/ktalynagb/mva-hackathon-2026  
**Deadline:** 24 de octubre de 2026, 23:59 UTC  
**Equipo:** Ktalyna · Laura

> Registra qué se hizo, quién lo hizo, qué se decidió y qué sigue.  
> Cada entrada nueva va **arriba**. Formato: `## YYYY-MM-DD — Título`.

---

## 2026-10-02 — Cambio de organización: de roles a tareas

**Quién:** Ktalyna (con Claude Code)  
**Decisión:** el equipo no llegó a un acuerdo sobre los 6 roles fijos. Se trabajará **por tareas**: el plan se dividió en 5 áreas (A variante · B mecanismo · C fármacos · D código · E informe) con tareas pequeñas identificadas por ID, fecha y dependencias. Cada persona toma hasta 2 tareas a la vez.

**Qué cambió:**
- `docs/plan_equipo_roles.md` → `docs/plan_equipo_tareas.md` (tablero de tareas, guía "¿por dónde empiezo?", reglas y checklist)
- Ramas nuevas: `tarea/<ID>-descripcion` (ej. `tarea/B1-marco-biologico`)
- `plan_de_trabajo.md` y README apuntan al nuevo tablero
- Las menciones a R1–R6 en notebooks y entradas anteriores equivalen a: R1/R2 → A · R3 → B · R4 → C · R5 → D · R6 → E

**Pendiente:**
- [ ] Cada integrante toma su primera tarea y se anota en el tablero

---

## 2026-10-01 — ✅ HITO H1 COMPLETADO: variante causante confirmada

**Quién:** Ktalyna (con Claude Code) — ejecución real del pipeline  
**Qué se hizo:**
- Ejecutado el pipeline completo: VCF → gnomAD v4 → CADD v1.7 → ClinVar
- Confirmadas las dos variantes BUB1B con datos reales de APIs públicas

### Resultados confirmados

| Campo | Variante 1 | Variante 2 |
|-------|-----------|-----------|
| **Posición (GRCh38)** | 15:40209701 | 15:40220612 |
| **Cambio VCF** | T>G | T>G |
| **rsID** | rs759242053 | — (sin rsID) |
| **HGVSc** | c.2210T>G | c.3006T>G |
| **HGVSp** | **p.Leu737Ter** | **p.Asn1002Lys** |
| **Consecuencia** | stop_gained | missense_variant |
| **Transcrito canónico** | ENST00000287598 (BUB1B) | ENST00000287598 (BUB1B) |
| **CADD phred** | **36.0** (top 0.025%) | **24.5** (top 0.35%) |
| **ClinVar** | **Pathogenic** (ID 533901) ✅ | no registrada |
| **AF exoma gnomAD v4** | 7.87×10⁻⁵ (0.008%) | **6.84×10⁻⁷ (0.00007%)** |
| **AF genoma gnomAD v4** | 3.29×10⁻⁵ | ausente |
| **Homocigotos gnomAD** | **0** | **0** |
| **Criterios ACMG** | PVS1 | PM2 + PP3 |
| **Interpretación** | **PATOGÉNICA** ✅ | **Prob. Patogénica** ✅ |

### Corrección importante sobre la variante 2

SnpEff (vía myvariant.info) erróneamente clasifica 15:40220612 T>G como "intergenic_region". gnomAD v4 confirma que está en el **transcrito canónico de BUB1B** (ENST00000287598), exón correspondiente a p.Asn1002Lys.

### Archivos generados
- `results/hito_H1_resultados_finales.json` — tabla completa con fuentes

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
| 2 | Identificar variante causante | ✅ **COMPLETADA** — Hito H1 logrado | Ktalyna + Laura |
| 3 | Caracterizar mecanismo biológico | 🔄 En curso (notebook 05 listo) | Área B |
| 4 | Candidatos de reposicionamiento | ⬜ Pendiente | Área C |
| 5 | Informe + entrega | ⬜ Pendiente | Área E |

### Hipótesis actual

La causa del MVA en este paciente es **BUB1B heterocigótica compuesta** — ✅ **CONFIRMADA**:

| Alelo | Posición | HGVSp | CADD | ClinVar |
|-------|----------|-------|------|---------|
| 1 | 15:40209701 | **p.Leu737Ter** (stop → NMD → LOF) | 36.0 | **Pathogenic** |
| 2 | 15:40220612 | **p.Asn1002Lys** (missense pseudo-kinasa) | 24.5 | no registrada |

Ambas son heterocigotas, ultra-raras en gnomAD v4 (7.87×10⁻⁵ y 6.84×10⁻⁷), sin homocigotos.  
→ Haploinsuficiencia compuesta de BUBR1 → SAC disfuncional → missegregación → MVA.

---

## Pendientes globales

- [ ] Fusionar PR #1 y #2 (tarea D1)
- [ ] Laura confirma `config/genes_candidatos.txt` (tarea A6)
- [ ] Cada integrante toma tareas del [tablero](plan_equipo_tareas.md)
- [ ] Completar `methods_description_form.xlsx` antes del 24 oct (tarea E7)
