# Plan de Equipo por Tareas — MVA Hackathon 2026 · Track 2

**Entrega: sábado 24 de octubre de 2026, 23:59 UTC** (entrega interna: 24 oct, 18:00 UTC)

No trabajamos con roles fijos. El trabajo está dividido en **5 áreas** y cada área en **tareas pequeñas con un ID** (A1, B2…). Cada persona toma las tareas que puede hacer, las entrega y toma la siguiente.

Documentos relacionados: [plan de trabajo por fases](plan_de_trabajo.md) · [bitácora](bitacora.md) · [README](../README.md)

---

## 1. Cómo funciona

1. **Elige una tarea libre** (⬜) del [tablero](#4-tablero-de-tareas). Revisa que las tareas de la columna *Depende de* estén ✅.
2. **Anótate:** avisa en el canal del equipo ("tomo B1") y escribe tu nombre en la columna *Responsable* con estado 🔄.
3. **Máximo 2 tareas en curso por persona.** Así nadie acapara y todo avanza.
4. **Trabaja en una rama** con el ID de la tarea: `tarea/B1-marco-biologico`. Nada se sube directo a `master`.
5. **Abre un PR** y pide revisión a otra persona. Las tareas de ciencia (🧬 💊) las revisa alguien con ese perfil.
6. **Cierra la tarea:** cuando el PR se fusiona, marca ✅ y agrega una línea en la [bitácora](bitacora.md).
7. **Si te bloqueas más de 24 h, avisa.** Si una tarea 🔄 no avanza en 3 días, vuelve a quedar libre.

**Leyenda de perfil:** 🧬 biología / genética · 💊 farmacología · 💻 código · ✍️ redacción y diseño
**Leyenda de estado:** ⬜ libre · 🔄 en curso · 👀 en revisión (PR abierto; no cuenta para el máximo de 2) · ✅ fusionado

---

## 2. ¿Por dónde empiezo?

| Si tu fuerte es… | Empieza por | Después |
|---|---|---|
| Biología celular, genética, leer papers | **B1** marco biológico | B2, A3, C6 |
| Farmacología, medicina, química farmacéutica | **C1** matriz de priorización | C2, C5 |
| Python, datos, APIs | **D1** fusionar PRs | A4, A5, C3, D2 |
| Escribir, organizar, diseñar | **E2** plantilla del informe | E3, E4, B5 |

No necesitas programar para aportar: más de la mitad de las tareas son de lectura, análisis o redacción.

---

## 3. Calendario e hitos

| Semana | Fechas | Pregunta que respondemos | Áreas activas | Estado |
|---|---|---|---|---|
| **1** | 1 – 7 oct | ¿Qué variante causa el MVA? | A | ✅ Respondida (1 oct) |
| **2** | 8 – 14 oct | ¿Qué le hace esa variante a la proteína, a la célula y al paciente? | B, C (inicio), D, E | 🔄 En curso |
| **3** | 15 – 21 oct | ¿Qué fármacos aprobados actúan sobre ese mecanismo? | C, E | ⬜ |
| **4** | 22 – 24 oct | ¿Está todo reproducible, grabado y enviado? | D, E | ⬜ |

| Hito | Fecha | Qué debe existir | Tarea | Estado |
|---|---|---|---|---|
| **H1** | 7 oct | Variante causante confirmada | A1 | ✅ 1 oct |
| **H2** | lun 12 oct | Resumen de mecanismo de 1 página | B4 | 👀 PR #6 |
| **H3** | mié 14 oct | Mecanismo completo + figura de la vía | B5 | 👀 figura lista (8 oct) |
| **H4** | sáb 17 oct | Lista corta de 3 a 5 fármacos con ficha | C5 | 👀 borrador 8 oct |
| **H5** | mié 21 oct | Borrador completo del informe | E5 | ⬜ |
| **H6** | vie 23 oct, 12:00 UTC | Código congelado + tag `v1.0-entrega` | D6 | ⬜ |
| **H7** | sáb 24 oct, 18:00 UTC | Entrega enviada | E7 | ⬜ |

---

## 4. Tablero de tareas

### Área A — Variante causante 🧬

Ya sabemos la respuesta: **BUB1B heterocigótica compuesta**, p.Leu737Ter + p.Asn1002Lys (ver `results/hito_H1_resultados_finales.json`). Falta documentarla con rigor.

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| A1 | Priorizar variantes con gnomAD, CADD y ClinVar | `notebooks/04_…ipynb` + `results/hito_H1_resultados_finales.json` | 💻🧬 | 7 oct | — | Ktalyna, Laura | ✅ |
| A2 | Redactar la variante causante con tabla ACMG formal. Incluir la limitación: sin muestras de los padres no se confirma que las variantes estén en alelos distintos (fase *trans*) | `docs/secciones/01_variante_causante.md` | 🧬✍️ | 9 oct | A1 | Ktalyna | ✅ PR #3 |
| A3 | Diagnóstico diferencial: por qué no son *CEP57*, *TRIP13* ni los otros genes del panel | sección 5 de `01_variante_causante.md` + `scripts/diagnostico_diferencial.py` | 🧬 | 11 oct | A1 | Ktalyna, Laura | ✅ PR #3 y #5. Solo BUB1B tiene LOF + 2.ª variante rara; CEP57/TRIP13/MAD2L1BP sin variantes raras funcionales. 104 genes nuevos: ninguno explica el MVA; 3 de 7 alertas eran falsas por usar transcritos no MANE (sigue en A8) |
| A4 | Revisar la calidad de lectura de las 2 variantes (AD, DP, GQ). ¿La fracción alélica es ≈ 0,5 o sugiere mosaicismo? | tabla en `01_variante_causante.md` (falta pasarla a una celda del notebook 04) | 💻🧬 | 11 oct | A1 | | 🔄 datos listos (fracción alt 0,54 y 0,46) |
| A5 | *Lollipop plot* de *BUB1B* con las 2 variantes y los dominios | `results/figura_1_bubr1_variantes.png` (`scripts/figuras_informe.py`) | 💻 | 13 oct | A1 | Ktalyna | 👀 incluye las variantes de MVA de Suijkerbuijk 2010 para comparar |
| A6 | Conciliar `config/genes_candidatos.txt` con la lista original de 201 genes | archivo actualizado + `config/lista_original_laura_201.tsv` + `notebooks/03b_a6_genes_faltantes_lista_laura.ipynb` | 💻 | 9 oct | — | Laura · Ktalyna (con Claude) | 👀 14 oct: lista original encontrada (salida de `resolve_genes.py` del 30 sep). Faltaban **31 genes, no ~11**, entre ellos 3 genes de MVA: *CENATAC* (MVA4), *SLF2* (MVA5) y *SMC5* (MVA6). Agregados (panel: 321) y analizados con el método MANE: **ninguno explica el MVA** (0 recesivos, 0 LOF). Los 4 símbolos inexistentes y el duplicado de CENPJ ya estaban cerrados |
| A7 | Enviar la pareja de variantes al **Track 1** del sitio del reto (evaluación automática inmediata, hasta 6 envíos por persona). **Ojo:** el formulario exige también enlace de GitHub e informe (.md o .pdf), y el envío aparece en el marcador público con el nombre de usuario | CSV + informe `<usuario>_track1_report.md` (formato en `01_variante_causante.md`, sección 8) | 🧬 | 7 oct | A2 | Ktalyna (con Claude) | 🔄 archivos listos en `envios/track1/` y validados con el código del sitio; **falta iniciar sesión en HF y enviar**. Ojo: el sitio solo acepta `proband_id = PROBAND01` |
| A8 | Usar la consecuencia en el transcrito **MANE Select** dentro de `scripts/diagnostico_diferencial.py` y repetir el barrido de los 187 genes. Actualizar la tabla de la sección 5 | script + sección 5 de `01_variante_causante.md` | 💻🧬 | 13 oct | A3 | Ktalyna | 👀 290 genes: 18 alertas → 13 en MANE; solo BUB1B con patrón recesivo |
| A9 | Conclusión del análisis de variantes no-PASS (notebook 02b): ¿alguna de las 6 variantes merece revisarse? Escribirla en el notebook, en la sección 5 de `01_variante_causante.md` y en la bitácora | celda de conclusión + 1 párrafo | 🧬 | 12 oct | — | Josefina | 👀 conclusión redactada (Ktalyna con Claude, 8 oct): ninguna de las 6 cambia el diagnóstico; falta que Josefina la confirme y la firme |
| A10 | Modelo dominante / diagnóstico dual: ¿una variante en una sola copia explica parte del cuadro (nefrocalcinosis, predisposición al rabdomiosarcoma)? | `scripts/modelo_dominante.py` + sección 5c de `01_variante_causante.md` + notebook 04 | 💻🧬 | 15 oct | A8 | Ktalyna (con Claude) | 👀 un hallazgo secundario: truncante heterocigota en *LZTR1* (schwannomatosis); nefrocalcinosis sin causa genética (probable prematuridad) |

### Área B — Mecanismo biológico 🧬

Base: `notebooks/05_mecanismo_biologico_bub1b.ipynb` ya tiene las 3 figuras y el borrador. Falta respaldarlo con literatura.

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| B1 | Revisión bibliográfica: dominios de BUBR1, su papel en el SAC y el MCC, ratones hipomórficos de BubR1, genotipos típicos de MVA tipo 1. Con referencias | `docs/secciones/02_marco_biologico.md` | 🧬✍️ | 10 oct | — | Ktalyna | 👀 PR #6: textos completos de Suijkerbuijk 2010 y Sieben 2020; falta revisión 🧬 |
| B2 | Confirmar si p.Leu737Ter activa el NMD (regla de 50–55 nt antes de la última unión exón-exón) | nota con fuente en notebook 05 y sección 4 de `01_variante_causante.md` | 🧬 | 10 oct | — | Ktalyna | ✅ PR #3. NMD predicho (PTC a 747 nt de la última unión) |
| B3 | Ubicar p.Asn1002Lys en la estructura de AlphaFold: confianza (pLDDT), entorno y cambio de carga, y estimar su efecto en la estabilidad | `scripts/evidencia_alelo2.py`, `scripts/estabilidad_alelo2.py` + sección de `01_variante_causante.md` | 🧬💻 | 12 oct | — | Ktalyna | ✅ PR #3 y #4. ΔΔG de N1002K = +1,5 kcal/mol (moderado); no toca el bolsillo de ATP |
| B4 | **(H2)** Resumen del mecanismo en 1 página, escrito para quien elige fármacos | `docs/secciones/02b_resumen_mecanismo.md` | 🧬✍️ | **12 oct** | B1, B2 | Ktalyna | 👀 PR #6: 4 líneas terapéuticas y 2 advertencias; falta revisión 💊 |
| B5 | **(H3)** Pulir la figura de la vía (variante → SAC débil → aneuploidía → fenotipo) con el estilo del informe | `results/figura_2_via_mecanismo.png` (`scripts/figuras_informe.py`) | ✍️🧬 | **14 oct** | B4, E2 | Ktalyna | 👀 con los puntos de acción de las 4 líneas y las 2 advertencias |

### Área C — Fármacos para reposicionamiento 💊

Base: **`docs/secciones/02b_resumen_mecanismo.md` (B4, PR #6)**, que reemplaza el `resumen_mecanismo_para_R4.json` del notebook 05. Propone 4 líneas: subir la cantidad de BUBR1 (proteostasis), frenar mTORC1, senolíticos y tratar el tumor sin empeorar la aneuploidía.

> ⚠️ **Cambio importante (8 oct):** los missense del dominio quinasa de BUBR1 dependen de HSP90 para plegarse, e inhibirla **baja aún más** la proteína (Suijkerbuijk 2010). HSP90 deja de ser diana. También quedan fuera PLK1, Aurora, MPS1 y APC/C: debilitan más la mitosis y no tienen fármacos aprobados.

> **Adelanto (6 oct):** una compañera que dejó el equipo subió `notebooks/06_agente_reposicionamiento_farmacos.ipynb`, un agente LangChain + Gemini con una lista inicial de fármacos para 6 blancos (APC/C, CDC20, PLK1, Aurora B, Hsp90, p53; no incluye mTOR). **Es un borrador, no una lista validada.** Antes de usarla falta un paso de verificación: (1) varios fármacos listados no están aprobados por FDA/EMA (Volasertib, Rigosertib, Barasertib, Dinaciclib); (2) bajo Hsp90 y p53 aparecen fármacos que no actúan sobre ese blanco (Crizotinib, Trametinib, Everolimus, Doxorrubicina); (3) la consulta a DGIdb usa la API v2 y falló en la ejecución guardada, así que el informe no usó datos recuperados; (4) la aprobación FDA/EMA solo es una instrucción del prompt, no se comprueba contra ninguna base. Siguiente paso: rehacer C3 con DGIdb v5 y Open Targets, comprobar la aprobación contra una fuente (openFDA o DrugBank) y puntuar con la matriz de C1.

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| C1 | Definir la matriz de priorización y sus pesos: aprobación FDA/EMA, solidez del mecanismo, seguridad pediátrica, interacción con el tratamiento del rabdomiosarcoma, evidencia existente | `docs/secciones/03_criterios.md` | 💊 | 10 oct | — | Ktalyna (borrador) | 👀 PR #7: 4 filtros + 6 criterios ponderados; necesita revisor 💊 para cerrar 5 decisiones |
| C2 | Paisaje terapéutico: fármacos aprobados sobre mitosis/SAC, senescencia, *readthrough* de codones de stop y mTOR | sección en el mismo archivo | 💊🧬 | 12 oct | — | | ⬜ |
| C3 | Consultar DGIdb y Open Targets por línea terapéutica → lista larga, con aprobación comprobada en FDA/EMA | `scripts/lista_larga_farmacos.py` + `results/candidatos_farmacos.tsv` + `docs/secciones/03b_lista_larga.md` | 💻💊 | 14 oct | — | Ktalyna | 👀 52 candidatos (14 en líneas 1–3, 38 en tumor), 21 de contexto, 13 excluidos |
| C4 | Puntuar la lista larga con la matriz | columna de puntaje en el `.tsv` | 💊 | 15 oct | C1, C3 | Ktalyna (con Claude) | 👀 53 candidatos puntuados (niacina agregada el 14 oct). Corregidos sirolimus (80 → 71,7) y arimoclomol (73,3 → 68,3, ficha FDA). Falta revisión 💊 de los 10 primeros (regla de C1 sec. 1.5) |
| C5 | **(H4)** Lista corta de 3 a 5 fármacos, con ficha: mecanismo, evidencia, seguridad pediátrica, riesgos y cómo se validaría | `docs/secciones/04_candidatos.md` | 💊✍️ | **17 oct** | B4, C4 | Ktalyna (con Claude) | 👀 5 candidatos (sirolimus, arimoclomol, temsirolimus, dasatinib, bortezomib), cubren las 4 líneas; falta revisión 💊🧬 |
| C6 | Revisión biológica de la lista corta: ¿cada fármaco mejora o empeora la aneuploidía? | sección 5 de `docs/secciones/04_candidatos.md` | 🧬 | 18 oct | C5 | Ktalyna (con Claude) | 👀 14 oct: ninguno debilita el checkpoint; bortezomib frena la salida de la mitosis → se propone niacina (sube BubR1 vía NAD⁺/SIRT2). Falta revisión 🧬 y decisión del equipo |
| C7 | Farmacogenética: buscar en el VCF del paciente las variantes de CYP2B6, CYP2C19, CYP3A4, CYP3A5, ABCB1 relevantes para ciclofosfamida y sirolimus; reportar fenotipos de metabolizador | `scripts/farmacogenetica.py` + `docs/secciones/05_farmacogenetica.md` + genotipos en `data/farmacogenetica/` | 💻🧬 | 17 oct | C5 | Ktalyna (con Claude) | 👀 PR #21 |
| C8 | Revisar la lista de genes del equipo (15 oct): BRCA1/2, LMNA, KMT2D, KDM6A, ATM y otros. Modelo dominante para los relevantes; descartar los demás con justificación | `scripts/analisis_genes_equipo.py` + `docs/secciones/06_genes_equipo.md` + adición en `config/genes_modelo_dominante.tsv` | 🧬💻 | 17 oct | A10 | Ktalyna (con Claude) | ✅ mergeado PR #22 — 10 genes, 0 candidatas dominantes; BRCA1/2 negativo; ATM 1 missense frecuente |
| C9 | Cómo tratar el tumor: evaluar si la ciclofosfamida corresponde como candidata y qué implica el checkpoint débil para la quimioterapia antimitótica | sección 8 de `docs/secciones/04_candidatos.md` + subsección en 3.3 del informe | 💊🧬 | 21 oct | C5, B4 | Ktalyna (con Claude) | ✅ mergeado PR #24 — ciclofosfamida descartada (es estándar, no reposicionamiento); temsirolimus se mantiene; VIT si recaída; documentada la duda abierta vincristina/SAC con evidencia en ambos sentidos |
| C10 | Vigilancia oncológica del MVA: qué tumores pueden venir después del rabdomiosarcoma y con qué protocolo | secciones 8.4 y 8.5 de `04_candidatos.md` + informe 3.3 | 🧬✍️ | 21 oct | C9 | Ktalyna (con Claude) | 🔄 PR pendiente — **Wilms ~50 % en MVA por BUB1B**: ecografía renal trimestral hasta los 7 años (SIOP-E, PMID 34134020); hemograma por MDS/LMA/LLA. **Falta confirmar las cifras en texto completo** (PMC y AACR bloquearon el acceso) |

### Área D — Código y reproducibilidad 💻

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| D1 | Revisar y fusionar los PR #1 (notebook 04) y #2 (notebook 05) | PRs fusionados en `master` | 💻 | 5 oct | — | Ktalyna | ✅ fusionados el 1 oct |
| D2 | Punto de entrada único (`run_pipeline.py`); los parámetros viven en `config/` | script + README | 💻 | 12 oct | D1 | Ktalyna | 👀 PR #12 |
| D3 | Fijar versiones y probar una clonación limpia en otra máquina | `requirements-lock.txt` + nota en README | 💻 | 12 oct | D1 | Ktalyna | 👀 PR #12; **falta la clonación limpia en otra máquina** (ideal Linux o macOS) |
| D4 | Tests con pytest para las funciones críticas y caché local de las consultas a APIs | `tests/` pasando | 💻 | 17 oct | D2 | | ⬜ |
| D2b | Agregar al pipeline los análisis que faltaban (A10, C7, C8) y arreglar el borrado silencioso de los genes manuales de C8 al regenerar desde PanelApp | `run_pipeline.py` 8 pasos + `config/genes_dominante_extra.tsv` | 💻 | 21 oct | D2 | Ktalyna (con Claude) | 🔄 PR pendiente; corrida completa medida |
| D5 | Sección "Escalabilidad" del README: cómo correr el pipeline con otro paciente | README actualizado | 💻✍️ | 20 oct | D2 | Ktalyna | 👀 PR #12 |
| D6 | **(H6)** Corrida limpia completa, congelación y tag `v1.0-entrega` | release en GitHub | 💻 | **23 oct 12:00 UTC** | todas las D | | 🔄 corrida completa de los 8 pasos verificada el 21 oct (6 min 11 s, reprodujo todos los números del informe); **falta** el tag y la release |

### Área E — Informe, video y entrega ✍️

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| E1 | Confirmar que cada integrante tiene su **propio** acceso aprobado en Hugging Face y **designar a una sola persona** que envía el Track 2 en nombre del equipo (los envíos duplicados no se revisan) | lista en el canal | ✍️ | 5 oct | — | | ⬜ **vencida** |
| E2 | Plantilla del informe con sus secciones y guía de estilo de figuras (paleta, fuentes) | `docs/informe_final.md` | ✍️ | 9 oct | — | Ktalyna | 👀 PR #8: incluye ya el borrador de variante y mecanismo |
| E3 | Leer `methods_description_form.xlsx` y anotar qué tarea responde cada pregunta | `docs/mapa_formulario.md` | ✍️ | 10 oct | — | Ktalyna (con Claude) | ✅ formulario bajado del Space oficial (estaba en `static/templates/`, no en el dataset de HF); mapa listo, 2 preguntas quedan pendientes de que el equipo las complete (team name/IA dependen de E1; tiempo dedicado nadie lo registró) |
| E4 | Guion del video v1 (3 min: problema · caso · variante · mecanismo · fármacos · escalabilidad) | `docs/paquete_video.md` | ✍️ | 14 oct | — | Ktalyna | ✅ el borrador v1 del 8 oct quedó desactualizado y se reemplazó por el paquete en inglés de Laura (guion + figuras en `results/video/`) |
| E5 | **(H5)** Integrar el borrador completo del informe | `docs/informe_final.md` completo | ✍️ | **21 oct** | A2, B4, C5 | Ktalyna | 🔄 borrador v2 (15 oct madrugada): Resumen, Resultados (3.1–3.4), Discusión y Referencias completos; falta 2.5 reproducibilidad (D2/D3) y tabla IA 2.6 (equipo) |
| E6 | Grabar y editar el video final | enlace al video | ✍️ | 23 oct | E4, C5 | | ✅ https://www.youtube.com/watch?v=J1OovR5hoWQ |
| E7 | **(H7)** Completar el formulario de métodos, exportar el informe a PDF y enviar por el sitio del reto: informe `<usuario>_track2_report.pdf`, enlace al repositorio GitHub y enlace al video (YouTube o Vimeo) | entrega enviada | ✍️ | **24 oct 18:00 UTC** | E5, E6, D6 | | ⬜ |
| E8 | Bitácora semanal y registro de uso de IA. El reto exige, para cada herramienta de IA: **proveedor, plan o nivel, y configuración de datos** (por ejemplo, si se usa para entrenar) | `docs/bitacora.md` + tabla de la sección 2.6 de `informe_final.md` | ✍️ | cada jueves | — | | 🔄 continuo; la tabla de IA está en PR #8 y **cada persona completa su fila** |

---

### Requisitos de entrega del reto (leídos en el sitio oficial, 2 oct)

- **Un solo envío por equipo** al Track 2: hasta 3 intentos, pero el panel revisa solo el último y solo el de la persona designada.
- **Informe** en PDF o Markdown, con el nombre de usuario o del equipo en el archivo (`<usuario>_track2_report.pdf`). Debe incluir el mecanismo de la variante (pérdida o ganancia de función, vía afectada, consecuencia) como base de la propuesta.
- **Repositorio de GitHub**: puede ser privado durante el hackatón, pero **debe hacerse público al terminar**. Por eso nada del paciente puede estar en el repo.
- **Video de 3 minutos** subido a **YouTube o Vimeo** (el enlace es obligatorio).
- **Uso de IA**: en la descripción de métodos, proveedor, plan o nivel y configuración de datos de cada herramienta.
- **Track 1 es opcional** y se puede hacer en paralelo: evalúa la variante de forma automática y entrega la puntuación al instante.

## 5. Reglas del equipo

### Trabajo
- **Una tarea, un responsable.** Puede pedir ayuda, pero responde por el entregable.
- **Si quieres aportar a una tarea ajena,** coméntalo en el canal o en su PR; el responsable decide.
- **Definición de "terminado":** está en `master` vía PR revisado, explica el *por qué* y quedó en la bitácora.
- **Check-in asíncrono** en el canal: *hice / haré / bloqueos*. **Sync semanal los jueves** (30 min).

### Datos y ética (obligatorio por los términos del dataset)
- Cada integrante debe registrarse como participante y tener su **propio** acceso aprobado en Hugging Face. **Nunca compartas los archivos de datos ni tu token.**
- **Nunca subas** al repo `data/`, archivos VCF/BAM/FASTQ, tokens ni información que pueda reidentificar al paciente o su familia. Esto incluye el informe y el video.
- Registra el uso de IA generativa en la bitácora (tarea E8).
- Al terminar el hackathon, cada integrante borra los datos de su equipo y notifica a `MVAHackathon2026@synapse.org`, según los términos de acceso.

---

## 6. Checklist de ingreso

- [ ] Registrada como participante y con **acceso aprobado** a `SageBio/mva-hackathon-2026-data`
- [ ] Invitación al repo de GitHub aceptada y repo clonado
- [ ] Leídos este documento, la [bitácora](bitacora.md) y el [plan de trabajo](plan_de_trabajo.md)
- [ ] Unida al canal del equipo y al sync de los jueves
- [ ] Primera tarea elegida y anotada

---

> **Nota sobre documentos anteriores.** Los notebooks 04 y 05 y la bitácora mencionan roles R1–R6 de un plan anterior. Equivalen a: R1 y R2 → área A · R3 → área B · R4 → área C · R5 → área D · R6 → área E.
