# Bitácora del Proyecto — MVA Hackathon 2026

**Track 2 — Reposicionamiento de Fármacos**  
**Repo:** https://github.com/ktalynagb/mva-hackathon-2026  
**Deadline:** 24 de octubre de 2026, 23:59 UTC  
**Equipo:** Ktalyna · Laura · Josefina · (completar)

> Registra qué se hizo, quién lo hizo, qué se decidió y qué sigue.  
> Cada entrada nueva va **arriba**. Formato: `## YYYY-MM-DD — Título`.

---

## 2026-10-08 (noche) — Figuras 1 y 2 del informe (A5, B5)

**Quién:** Ktalyna (con Claude Code) · rama `tarea/A5-B5-figuras`
**Qué se hizo:**
- `scripts/figuras_informe.py` genera las dos figuras con la guía de estilo del informe (paleta Okabe-Ito validada para daltonismo; alelo 1 bermellón, alelo 2 azul, fármacos verde)
- **Figura 1** (`results/figura_1_bubr1_variantes.png`): BUBR1 con dominios, las 2 variantes del paciente y las 12 variantes de MVA de Suijkerbuijk 2010, agrupadas por efecto sobre la cantidad de proteína
- **Figura 2** (`results/figura_2_via_mecanismo.png`): la vía del genotipo al fenotipo, con el punto de acción de cada línea terapéutica y las dos advertencias (HSP90, antimitóticos)
- Ambas enlazadas en `docs/informe_final.md` con su pie de figura

**Pendiente:**
- [ ] Revisión 🧬 de la figura 2 (Hito H3, 14 oct)

---

## 2026-10-08 (tarde) — Lista larga de fármacos (C3)

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C3-lista-larga`
**Qué se hizo:**
- Se fusionaron los PR #6 a #9 y se borraron las ramas ya fusionadas
- `scripts/lista_larga_farmacos.py` une DGIdb v5, Open Targets y una lista curada por línea terapéutica, comprueba la aprobación en Drugs@FDA y en la EMA y aplica los filtros F1 y F2 de C1
- Resultado en `results/candidatos_farmacos.tsv` (con excepción en `.gitignore`: no contiene datos del paciente) y resumen en `docs/secciones/03b_lista_larga.md`

**Hallazgos:**
- 86 fármacos: **52 candidatos** (líneas 1–3: 14; tumor: 38), 21 de contexto y 13 excluidos
- ✅ Ninguno de los 162 inhibidores de HSP90, PLK1, Aurora, MPS1, APC/C, BUB1 o CDK1 está aprobado: las dianas que empeorarían el checkpoint no tienen fármacos aprobados
- ⚠️ Open Targets ya no tiene el campo `knownDrugs` (ahora `drugAndClinicalCandidates`) y no liga los rapalógos a MTOR; se curaron a mano
- ⚠️ openFDA no trae `generic_name` en muchos registros; se busca también por principio activo

**Pendiente:**
- [ ] C4: puntuar los 52 candidatos con la matriz (perfil 💊). Avisos en la sección 3 de `03b_lista_larga.md`

---

## 2026-10-08 — Cierre de B1, H2 en revisión, matriz de fármacos y borrador del informe

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- Se fusionó el PR #5 de Laura (104 genes nuevos)
- **B1** (PR #6): Suijkerbuijk 2010 y Sieben 2020 leídos en texto completo; guías ACMG verificadas en PubMed
- **B4 / Hito H2** (PR #6): `docs/secciones/02b_resumen_mecanismo.md`, una página para el área C
- **C1** (PR #7): `docs/secciones/03_criterios.md`, matriz con filtros de exclusión y 6 criterios ponderados
- **E2 y E4** (PR #8): `docs/informe_final.md` con el borrador de variante y mecanismo ya integrado, guía de estilo, tabla de uso de IA y `docs/guion_pitch.md`
- Tablero actualizado: estados de A2, A3, B2, B3 y D1; tareas nuevas A8 (barrido con MANE) y A9 (conclusión del notebook 02b); estado 👀 para tareas en revisión

**Hallazgos:**
- ✅ **En el MVA bialélico falta proteína, no función.** Todos los missense del dominio quinasa estudiados bajan BUBR1 de 5 a 10 veces por mal plegamiento, y llevarlos a niveles normales restaura el checkpoint (Suijkerbuijk 2010). p.Asn1002Lys está en ese dominio
- ✅ **Caso publicado casi idéntico al nuestro:** truncamiento en el codón 753 (c.2211insGTTA, el nucleótido contiguo a nuestro c.2210) + p.Leu1012Pro. Ese paciente murió a los 3,6 meses
- ✅ La pérdida total de BUBR1 es letal en el embrión de ratón (Wang 2004): ya no es una hipótesis sin fuente
- ⚠️ **HSP90 deja de ser diana:** inhibirla baja aún más la BUBR1 mutante. Estaba propuesta en el notebook 05 y en el cuaderno 06
- ⚠️ El formulario de métodos no está en el dataset de Hugging Face: E3 queda bloqueada

**Decisiones:**
- Las tareas en PR abierto pasan a 👀 y no cuentan para el máximo de 2 en curso
- La lista corta de fármacos debe cubrir al menos dos líneas terapéuticas distintas

**Pendiente:**
- [ ] Revisión 🧬 del PR #6 y revisión 💊 de los PR #6 y #7
- [ ] Bajar `methods_description_form.xlsx` del sitio del reto (E3)
- [ ] Decidir el idioma del informe y del video
- [ ] Cada persona completa su fila en la tabla de uso de IA (sección 2.6 del informe)
- [ ] Asignar responsables del área C (C2 a C6) y de E1 y A7, que están vencidas

---

## 2026-10-07 — Análisis de sensibilidad de variantes no-PASS

**Quién:** Josefina · subido directo a `master`
**Qué se hizo:**
- `notebooks/02b_sensibilidad_nonpass_genes_mva.ipynb`: revisa las variantes que el filtro de calidad descartó en los 6 genes principales

**Hallazgos:**
- 6 variantes no-PASS: 5 en *MAD1L1* y 1 en *BUB1B* (deleción de 1 pb, QUAL 19,8). Todas con baja calidad de mapeo o de lectura (filtros QD2, MQ40, LowQual)

**Pendiente:**
- [ ] Josefina: escribir la conclusión en el notebook (tarea A9)

---

## 2026-10-06 — Diagnóstico diferencial de los 104 genes nuevos

**Quién:** Laura (con Claude Code) · rama `tarea/A3-genes-nuevos`
**Qué se hizo:**
- Se corrió `python scripts/diagnostico_diferencial.py --solo-nuevos` con el VCF local (Colab conectado a un entorno local). Los 104 genes se resolvieron en gnomAD y no quedaron variantes sin anotar
- Se volvieron a anotar las 7 variantes raras funcionales con Ensembl VEP en el transcrito MANE Select
- Resumen en la sección 5b de `docs/secciones/01_variante_causante.md`

**Hallazgos:**
- ✅ Ningún gen nuevo explica el MVA: *BUB1B* sigue siendo el único con dos variantes dañinas
- ⚠️ *SYNE2* salió con patrón recesivo, pero es una falsa alarma: una de sus 2 variantes es intrónica en MANE
- ⚠️ 3 de las 7 alertas (*ARID1B* stop, *SMARCA4* missense, *SYNE2* stop_lost) solo eran graves en transcritos secundarios. El script usa la consecuencia más severa en cualquier transcrito

**Pendiente:**
- [ ] Usar la consecuencia en MANE dentro de `scripts/diagnostico_diferencial.py` y repetir el barrido de los 187 genes
- [ ] Análisis de sensibilidad de variantes no-PASS (sigue sin hacerse)

---

## 2026-10-06 — Cuaderno 06 de fármacos (adelanto de una compañera que se retira)

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- Una compañera que dejó el equipo subió `notebooks/06_agente_reposicionamiento_farmacos.ipynb` (agente LangChain + Gemini) con una lista inicial de fármacos para 6 blancos. Ya está en `master`
- Se revisó el cuaderno y se anotó el estado en el Área C de `docs/plan_equipo_tareas.md`

**Hallazgos (revisión del cuaderno):**
- ⚠️ La lista **no es validable tal como está**: varios fármacos no están aprobados por FDA/EMA, y bajo Hsp90 y p53 hay fármacos que no actúan sobre esos blancos
- La extracción de DGIdb falló en la ejecución guardada (API v2) y el filtro FDA/EMA es solo una instrucción del prompt
- Quedan sin responsable las tareas C1 a C6; la lista corta (H4) vence el **17 de octubre**

**Pendiente:**
- [ ] Paso de verificación: rehacer C3 con DGIdb v5 y Open Targets, comprobar la aprobación FDA/EMA contra una fuente y puntuar con la matriz de C1
- [ ] Asignar responsable del Área C
- [ ] Preguntarle por privado qué celda produjo la lista del mensaje y si DGIdb funcionó alguna vez

---

## 2026-10-05 — Genes de los grupos del equipo: CSV corregidos y lista ampliada

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- Los 8 CSV del equipo (166 genes) se guardaron sin tocar en `config/grupos_genes/originales/` y se unificaron con `scripts/unir_grupos_genes.py` en `config/genes_candidatos_anotados.csv`
- `config/genes_candidatos.txt` pasa de 188 a 292 símbolos (104 nuevos, en un bloque entre marcas AUTO; el script se puede volver a correr)
- `scripts/diagnostico_diferencial.py` acepta `--solo-nuevos` para analizar solo esos genes
- Se fusionó `tarea/B3-bolsillo-atp` (p.Asn1002Lys no toca el bolsillo de ATP)

**Hallazgos:**
- ⚠️ Las columnas `hgnc_id`, `ensembl_id` y `ncbi_gene_id` están corruptas en 7 de 8 archivos (p. ej. `ENSG00000162571` en 72 de 95 filas) y se descartaron. En el archivo de reparación de ADN faltan 2 columnas. Las coordenadas salen de `scripts/resolve_genes.py` por símbolo
- Errores de contenido marcados en `nota_revision` (el texto original no se modificó): PCNT/Taybi-Linder, NIN/pseudoacondroplasia, SAS6 ("cartílago"), TRIP13 "MVA 3" y símbolos desactualizados (CCDC155, H3F3A/B, H2AFZ, MRE11A, NTF2, NUP53, NUP96)
- HGS, ARRB1 y ARRB2 no son del ciclo celular: baja prioridad

**Pendiente:**
- [ ] Probar los 104 genes nuevos igual que BUB1B: `python scripts/diagnostico_diferencial.py --solo-nuevos` (necesita el VCF en `data/raw/` y red; escribe `results/diagnostico_diferencial_nuevos_*.tsv` sin pisar el análisis del panel). Esta sesión no tenía ni VCF ni red
- [ ] Verificar en OMIM las filas con nota "verificar" antes de citarlas
- [ ] Repetir con red el cálculo del bolsillo de ATP (AlphaFold/AlphaFill estaban bloqueados); el resultado vigente es el de la rama B3
- [ ] Análisis de sensibilidad de variantes no-PASS (todo el pipeline descarta lo que no sea PASS)

---

## 2026-10-02 — Tareas A2 y B2: clasificación ACMG y NMD (corrige la lectura del H1)

**Quién:** Ktalyna (con Claude Code) · rama `tarea/A2-B2-variante-acmg-nmd`  
**Qué se hizo:**
- `docs/secciones/01_variante_causante.md`: tabla ACMG con puntajes, calidad de llamadas, NMD, limitaciones y qué lo confirmaría
- NMD de p.Leu737Ter: PTC en c.2210 (exón 17/23), última unión exón-exón a 747 nt → NMD predicho (sin datos de ARN)
- Calidad de lectura (A4): fracción alt 0,54 y 0,46, GQ 99, sin señal de mosaicismo; sin etiquetas de fase en el VCF

**Evidencia adicional del alelo 2 (B3, parte de B1):** `scripts/evidencia_alelo2.py` → `results/evidencia_alelo2.json`
- ClinVar (2501 registros): p.Asn1002Lys ya figura como VUS (c.3006T>A); sin cambios patogénicos de aminoácido cerca → sin PM1/PM5
- AlphaFold: pLDDT 91, la Asn forma 3 enlaces de hidrógeno que la lisina perdería; residuo conservado en 7/7 vertebrados
- Sin artículos con este cambio; sigue siendo VUS, inclinada a patogénica

**¿p.Asn1002Lys toca el bolsillo de ATP? (2 oct)** → fila nueva en la tabla de hipótesis de `01_variante_causante.md`, `scripts/evidencia_alelo2.py`
- No: a 28,6–29,8 Å del nucleótido (4 posiciones colocadas por homología con AlphaFill), sin contacto con ninguno de los 30 residuos del bolsillo
- Un efecto directo sobre la unión de ATP es muy improbable; uno indirecto por menor estabilidad global no se descarta

**Cálculo de estabilidad de p.Asn1002Lys con ThermoMPNN (2 oct)** → `scripts/estabilidad_alelo2.py`, `results/estabilidad_alelo2.json`
- ΔΔG de N1002K = +1,5 kcal/mol (desestabiliza de forma moderada); la variante conocida de MVA1 p.Leu1012Pro da +3,1
- Todas las sustituciones en 1002 desestabilizan; resultado igual con la proteína completa y con el dominio (Spearman 0,95)
- Controles superados (numeración, identidad, signo). Encaja con un alelo hipomórfico; la degradación rápida no queda demostrada
- No cambia la clasificación ACMG (la herramienta no está calibrada para PP3)

**Hipótesis del equipo sobre p.Asn1002Lys puestas a prueba (2 oct)** → sección "Hipótesis del equipo" de `01_variante_causante.md`
- Glicosilación: descartada (N-A-N-D no es el motivo N-X-S/T)
- N1002 mayormente enterrado, en el extremo de una hélice, con 3 enlaces H que la lisina perdería; a 29 Å del bolsillo de ATP
- Hallazgo: UniProt anota la variante MVA1 p.Leu1012Pro como heterocigota compuesta con una mutación sin sentido (mismo tipo de genotipo del paciente), a 12 Å de N1002 y totalmente enterrada
- Estabilidad/degradación: plausible, falta calcular ΔΔG

**Revisión exhaustiva del dataset y del sitio del reto en Hugging Face (2 oct)**
- El dataset tiene una sola rama, sin versiones ocultas ni PR; son 13 archivos y todos son del paciente (VCF, FASTQ, documento clínico). No hay datos de los padres, y la organización no tiene otros datasets públicos
- La fase de las dos variantes no se puede resolver con lo disponible (variante intermedia a 6,8 y 4,1 kb)
- Requisitos de entrega del Track 2 leídos del sitio oficial: un solo envío por equipo, repo público al terminar, video en YouTube o Vimeo, y declaración de IA con proveedor, plan y configuración de datos. Añadidos al tablero
- El Track 1 del sitio puntúa la pareja de variantes al instante contra la respuesta validada: añadida la tarea A7

**Tarea A3: diagnóstico diferencial** → sección 5 de `docs/secciones/01_variante_causante.md`, `scripts/diagnostico_diferencial.py`
- 187 genes del panel (se añadió MAD2L1BP, MVA descrito en 2023): solo 11 variantes raras funcionales, todas heterocigotas. BUB1B es el único gen con LOF + otra variante rara funcional
- CEP57, TRIP13, MAD2L1BP, BUB1, BUB3, MAD2L1, CDC20 y ESPL1: sin variantes raras funcionales
- No evaluado: variantes estructurales/CNV y no codificantes (un caso publicado de MVA tuvo una variante reguladora de BUB1B)
- Error corregido en el proceso: la primera versión marcó 31 variantes comunes como "ausentes de gnomAD" (la lista por gen de gnomAD omite algunas); ahora se consulta cada variante funcional directamente

**Tarea B1 (borrador): marco biológico** → `docs/secciones/02_marco_biologico.md`
- Coordenadas de dominios verificadas (UniProt y Zhang 2026): GLEBS 408–418, KARD 669–674, pseudoquinasa 766–1050; la tabla del notebook 05 estaba mal y la figura 02a se regeneró
- Tabla de literatura reemplazada por 18 citas verificadas en PubMed. Se eliminaron 5 que no existían o no decían lo afirmado (Malureanu 2009, Elowe 2012, Rivero 2016, Simonetti 2019, Holland y Cleveland 2012)
- Hallazgo: Sieben 2020 modela en ratón la variante de MVA BUBR1 p.Leu1012Pro, a 10 residuos de p.Asn1002 (contexto, no evidencia ACMG); la sarcopenia se asocia a mTORC1, que conecta con la atrofia muscular del paciente

**Correcciones al trabajo anterior:**
- Alelo 2 p.Asn1002Lys: era "probablemente patogénica (PM2+PP3)"; con puntos ACMG es **VUS** (REVEL 0,472 indeterminado, BayesDel tolerado)
- Alelo 1: ClinVar Pathogenic es de un único remitente; con criterios propios son 9 puntos (probablemente patogénica)
- El diagnóstico BUB1B bialélico es **muy probable, no confirmado**: falta fase *trans* (sin padres) y datos funcionales
- Notebook 05: exón 21 → 17, c.2210T>A → T>G, "313 aa" → 314, quitados PM1/PP2 sin respaldo, y marcados como **sin verificar** los límites de dominios (UniProt: dominio quinasa 766–1050, p.Leu737 queda antes) y la tabla de literatura (de memoria)
- El PDF del H1 que circuló tenía el mapa de dominios con esas coordenadas sin verificar; regenerado

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
| 3 | Caracterizar mecanismo biológico | 🔄 B1 y B4 (H2) en revisión, PR #6; falta B5 (H3, 14 oct) | Área B |
| 4 | Candidatos de reposicionamiento | 🔄 C1 en revisión, PR #7; C2 a C6 sin responsable | Área C |
| 5 | Informe + entrega | 🔄 Plantilla y guion en revisión, PR #8 | Área E |

### Hipótesis actual

La causa del MVA en este paciente es **BUB1B heterocigótica compuesta**, muy probable pero sin confirmación formal: falta demostrar la fase *trans* y el alelo 2 es VUS (ver `secciones/01_variante_causante.md`):

| Alelo | Posición | HGVSp | CADD | ClinVar |
|-------|----------|-------|------|---------|
| 1 | 15:40209701 | **p.Leu737Ter** (stop → NMD → LOF) | 36.0 | **Pathogenic** |
| 2 | 15:40220612 | **p.Asn1002Lys** (missense pseudo-kinasa) | 24.5 | no registrada |

Ambas son heterocigotas, ultra-raras en gnomAD v4 (7.87×10⁻⁵ y 6.84×10⁻⁷), sin homocigotos.  
→ Alelo nulo + alelo hipomórfico inestable → poca BUBR1 → SAC débil → errores de segregación → MVA.

---

## Pendientes globales

- [x] Fusionar PR #1 y #2 (tarea D1)
- [ ] Revisar y fusionar los PR #6, #7 y #8
- [ ] Laura confirma `config/genes_candidatos.txt` (tarea A6)
- [ ] Cada integrante toma tareas del [tablero](plan_equipo_tareas.md)
- [ ] Completar `methods_description_form.xlsx` antes del 24 oct (tarea E7)
