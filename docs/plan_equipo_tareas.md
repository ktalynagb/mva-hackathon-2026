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
| **H2** | lun 12 oct | Resumen de mecanismo de 1 página | B4 | ⬜ |
| **H3** | mié 14 oct | Mecanismo completo + figura de la vía | B5 | ⬜ |
| **H4** | sáb 17 oct | Lista corta de 3 a 5 fármacos con ficha | C5 | ⬜ |
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
| A2 | Redactar la variante causante con tabla ACMG formal. Incluir la limitación: sin muestras de los padres no se confirma que las variantes estén en alelos distintos (fase *trans*) | `docs/secciones/01_variante_causante.md` | 🧬✍️ | 9 oct | A1 | Ktalyna | 🔄 borrador en PR, falta revisión |
| A3 | Diagnóstico diferencial: por qué no son *CEP57*, *TRIP13* ni los otros genes del panel | sección en el mismo archivo | 🧬 | 11 oct | A1 | | ⬜ |
| A4 | Revisar la calidad de lectura de las 2 variantes (AD, DP, GQ). ¿La fracción alélica es ≈ 0,5 o sugiere mosaicismo? | tabla en `01_variante_causante.md` (falta pasarla a una celda del notebook 04) | 💻🧬 | 11 oct | A1 | | 🔄 datos listos (fracción alt 0,54 y 0,46) |
| A5 | *Lollipop plot* de *BUB1B* con las 2 variantes y los dominios | `results/figura_bub1b_lollipop.png` | 💻 | 13 oct | A1 | | ⬜ |
| A6 | Conciliar `config/genes_candidatos.txt` con la lista original de 201 genes | archivo actualizado | 💻 | 9 oct | — | Laura | ⬜ |

### Área B — Mecanismo biológico 🧬

Base: `notebooks/05_mecanismo_biologico_bub1b.ipynb` ya tiene las 3 figuras y el borrador. Falta respaldarlo con literatura.

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| B1 | Revisión bibliográfica: dominios de BUBR1, su papel en el SAC y el MCC, ratones hipomórficos de BubR1, genotipos típicos de MVA tipo 1. Con referencias | `docs/secciones/02_marco_biologico.md` | 🧬✍️ | 10 oct | — | Ktalyna | 🔄 borrador con 18 citas verificadas en PubMed; falta leer textos completos |
| B2 | Confirmar si p.Leu737Ter activa el NMD (regla de 50–55 nt antes de la última unión exón-exón) | nota con fuente en notebook 05 y sección 4 de `01_variante_causante.md` | 🧬 | 10 oct | — | Ktalyna | ✅ NMD predicho (PTC a 747 nt de la última unión); falta revisión |
| B3 | Ubicar p.Asn1002Lys en la estructura de AlphaFold: confianza (pLDDT), entorno y cambio de carga | `scripts/evidencia_alelo2.py` + sección de `01_variante_causante.md` | 🧬💻 | 12 oct | — | Ktalyna | ✅ pLDDT 91, 3 enlaces H que se perderían, conservado en 7/7 especies; falta revisión |
| B4 | **(H2)** Resumen del mecanismo en 1 página, escrito para quien elige fármacos | `docs/secciones/02b_resumen_mecanismo.md` | 🧬✍️ | **12 oct** | B1, B2 | | ⬜ |
| B5 | **(H3)** Pulir la figura de la vía (variante → SAC débil → aneuploidía → fenotipo) con el estilo del informe | `results/figura_02c_…png` final | ✍️🧬 | **14 oct** | B4, E2 | | ⬜ |

### Área C — Fármacos para reposicionamiento 💊

Base: `results/resumen_mecanismo_para_R4.json` ya lista 6 dianas (CDC20/APC/C, PLK1, Aurora B, Hsp90, eje p53, mTOR). Son hipótesis para verificar.

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| C1 | Definir la matriz de priorización y sus pesos: aprobación FDA/EMA, solidez del mecanismo, seguridad pediátrica, interacción con el tratamiento del rabdomiosarcoma, evidencia existente | `docs/secciones/03_criterios.md` | 💊 | 10 oct | — | | ⬜ |
| C2 | Paisaje terapéutico: fármacos aprobados sobre mitosis/SAC, senescencia, *readthrough* de codones de stop y mTOR | sección en el mismo archivo | 💊🧬 | 12 oct | — | | ⬜ |
| C3 | Notebook 06: consultar DGIdb y Open Targets para *BUB1B* y su red → lista larga de 20 a 30 fármacos | `notebooks/06_candidatos_farmacos.ipynb` + `results/candidatos_farmacos.tsv` | 💻💊 | 14 oct | — | | ⬜ |
| C4 | Puntuar la lista larga con la matriz | columna de puntaje en el `.tsv` | 💊 | 15 oct | C1, C3 | | ⬜ |
| C5 | **(H4)** Lista corta de 3 a 5 fármacos, con ficha: mecanismo, evidencia, seguridad pediátrica, riesgos y cómo se validaría | `docs/secciones/04_candidatos.md` | 💊✍️ | **17 oct** | B4, C4 | | ⬜ |
| C6 | Revisión biológica de la lista corta: ¿cada fármaco mejora o empeora la aneuploidía? | comentarios en el PR de C5 | 🧬 | 18 oct | C5 | | ⬜ |

### Área D — Código y reproducibilidad 💻

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| D1 | Revisar y fusionar los PR #1 (notebook 04) y #2 (notebook 05) | PRs fusionados en `master` | 💻 | 5 oct | — | | ⬜ |
| D2 | Punto de entrada único (`run_pipeline.py`) y parámetros en `config/config.yaml` | script + config | 💻 | 12 oct | D1 | | ⬜ |
| D3 | Fijar versiones en `requirements.txt` y probar una clonación limpia en otra máquina | `requirements.txt` + nota en README | 💻 | 12 oct | D1 | | ⬜ |
| D4 | Tests con pytest para las funciones críticas y caché local de las consultas a APIs | `tests/` pasando | 💻 | 17 oct | D2 | | ⬜ |
| D5 | Sección "Escalabilidad" del README: cómo correr el pipeline con otro paciente | README actualizado | 💻✍️ | 20 oct | D2 | | ⬜ |
| D6 | **(H6)** Corrida limpia completa, congelación y tag `v1.0-entrega` | release en GitHub | 💻 | **23 oct 12:00 UTC** | todas las D | | ⬜ |

### Área E — Informe, video y entrega ✍️

| ID | Tarea | Entregable | Perfil | Fecha | Depende de | Responsable | Estado |
|---|---|---|---|---|---|---|---|
| E1 | Confirmar que cada integrante tiene su **propio** acceso aprobado en Hugging Face | lista en el canal | ✍️ | 5 oct | — | | ⬜ |
| E2 | Plantilla del informe con sus secciones y guía de estilo de figuras (paleta, fuentes) | `docs/informe_final.md` | ✍️ | 9 oct | — | | ⬜ |
| E3 | Leer `methods_description_form.xlsx` y anotar qué tarea responde cada pregunta | `docs/mapa_formulario.md` | ✍️ | 10 oct | — | | ⬜ |
| E4 | Guion del video v1 (3 min: problema · caso · variante · mecanismo · fármacos · escalabilidad) | `docs/guion_pitch.md` | ✍️ | 14 oct | — | | ⬜ |
| E5 | **(H5)** Integrar el borrador completo del informe | `docs/informe_final.md` completo | ✍️ | **21 oct** | A2, B4, C5 | | ⬜ |
| E6 | Grabar y editar el video final | enlace al video | ✍️ | 23 oct | E4, C5 | | ⬜ |
| E7 | **(H7)** Completar el formulario de métodos, exportar el informe a PDF y enviar | entrega enviada | ✍️ | **24 oct 18:00 UTC** | E5, E6, D6 | | ⬜ |
| E8 | Bitácora semanal y registro de uso de IA (herramienta y para qué) | `docs/bitacora.md` | ✍️ | cada jueves | — | | 🔄 continuo |

---

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
