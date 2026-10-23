# Mapa del formulario de métodos (tarea E3)

**Entregable de E3** · `methods_description_form.xlsx` bajado del Space oficial del reto (`SageBio/rare-disease-real-kid-mva-hackathon-2026`, carpeta `static/templates/`) el 9 oct — **no estaba en el dataset de Hugging Face**, estaba en el repo del Space. Copia local en [`docs/plantillas/methods_description_form.xlsx`](plantillas/methods_description_form.xlsx) (es un formulario público del reto, no contiene datos del paciente — se puede versionar sin problema).

El archivo tiene 2 hojas, una por track. Para cada pregunta: dónde está la respuesta en el repo y qué tarea la generó. "Responsable" = quien tiene que redactar la respuesta final en el formulario (no necesariamente quien hizo la tarea).

## Hoja "Track 2 methods" (la que nos importa para E7 — entrega 24 oct)

| # | Pregunta | Dónde está la respuesta | Tarea de origen |
|---|---|---|---|
| 1 | Team name | **A3 EMBS ITBA**. Envía **Laura Vargas** (23 oct), con lo que E1 queda cerrada | E1 ✅ |
| 2 | Describí el enfoque en detalle (de variante/mecanismo a fármaco candidato) | `01_variante_causante.md` → `02_marco_biologico.md` → `02b_resumen_mecanismo.md` → `03_criterios.md` → `03b_lista_larga.md` → `04_candidatos.md`: es el recorrido completo del repo, resumido | A2/A3/A8, B1–B4, C1, C3, C5 |
| 3 | **(obligatoria)** Si se usó IA generativa: proveedor, plan y configuración de datos | Sección 2.6 de `informe_final.md`. **Cuatro herramientas:** Claude Code, Claude (app), Gemini y Perplexity. Claude Code está completa; de Gemini está documentado el uso (cuaderno 06) y que **no recibió datos del paciente**, falta el nivel de la API; de Claude app y Perplexity falta todo porque no hay registro en el repo | E8 |
| 4 | ¿Identificación de candidatos automatizada (consulta a base de datos / LLM) o revisión manual/curación experta? | Ambas: `scripts/lista_larga_farmacos.py` consulta DGIdb v5 y Open Targets de forma automática (C3); la puntuación K1–K6 (C4) y la lista curada de `config/lineas_terapeuticas.json` son curación manual asistida por IA | C3, C4 |
| 5 | Describí la revisión manual/curación experta en detalle | `02_marco_biologico.md` (B1, 18 citas verificadas en PubMed); lista `curados` de `config/lineas_terapeuticas.json` (arimoclomol, fenilbutirato, rapálogos, dasatinib); notas de `03b_lista_larga.md` sección 3 (avisos para quien puntúe) y las notas por fármaco de C4 en `results/candidatos_farmacos.tsv` | B1, C3, C4 |
| 6 | ¿Solo datos/literatura públicos, o también fuentes propietarias? | Solo públicos para el mecanismo y los fármacos. El genoma y la clínica del paciente vienen del dataset del propio reto (`SageBio/mva-hackathon-2026-data` en HF, acceso controlado por los términos del reto, no es una fuente propietaria externa) | — |
| 7 | Describí las fuentes públicas usadas | DGIdb v5, Open Targets Platform, Drugs@FDA (openFDA), base de medicamentos de la EMA, PubMed (Suijkerbuijk 2010 PMID 20516114, Sieben 2020 PMID 31738183, Mascarenhas 2019 PMID 31513481, Gupta 2024 PMID 38936378, entre otras), gnomAD v4, ClinVar, Ensembl VEP (transcrito MANE Select), UniProt, AlphaFold/AlphaFill, myvariant.info | A1, A3, A8, B1–B3, C3 |
| 8 | Describí las fuentes propietarias usadas | Ninguna, aparte del dataset del reto (ver pregunta 6) | — |
| 9 | ¿Cómo caracterizaron el mecanismo de la variante (LOF/GOF, vía, consecuencia)? | Resumen corto: *BUB1B* heterocigota compuesta — p.Leu737Ter (alelo nulo, NMD predicho) + p.Asn1002Lys (missense hipomórfico en la pseudoquinasa, ΔΔG +1,5 kcal/mol) → **pérdida de función por falta de cantidad de BUBR1**, no de función → checkpoint mitótico (SAC) débil → aneuploidía en mosaico → senescencia/envejecimiento precoz (mTORC1) + inestabilidad cromosómica (rabdomiosarcoma). Detalle completo en `01_variante_causante.md` y `02_marco_biologico.md`; resumen de una página en `02b_resumen_mecanismo.md` | A2, B1–B4 |
| 10 | Estimación de tiempo o esfuerzo dedicado | **Sin resolver, el equipo lo tiene que estimar.** La bitácora tiene fechas (lanzamiento 17 sep, primer hito 1 oct) pero no horas-persona por integrante | — **pendiente, el equipo debe completarla** |
| 11 | Abstract del método (hasta 500 palabras, fortalezas y limitaciones) | Se escribe al final, cuando `informe_final.md` esté completo (E5); combina el resumen de las preguntas 2 y 9 más las limitaciones ya documentadas en `01_variante_causante.md` sección 5 y `02b_resumen_mecanismo.md` | E5, al cierre |

## Hoja "Track 1 methods" (para A7, si se decide enviar)

Mismo patrón; preguntas equivalentes ya resueltas en el repo salvo: modelo/número de corrida, tiempo/costo estimado y si el enfoque distingue heterocigota compuesta (sí: `scripts/diagnostico_diferencial.py` identifica el par). Fila 1 (team name) y la de IA generativa son las obligatorias. No se detalla fila por fila porque A7 sigue vencida y sin decidir si se envía.

## Estado (23 oct) — cerrado

- [x] **E1**: equipo A3 EMBS ITBA, envía Laura Vargas.
- [x] **Pregunta 10** (tiempo/esfuerzo): estimado por el equipo en 42 horas-persona, con el desglose por integrante.
- [x] **El `.xlsx` está lleno**: las 11 preguntas de la hoja "Track 2 methods", en `envios/track2/A3_EMBS_ITBA_methods_description_form.xlsx`.

Este mapa cumplió su función —dejar asentado de dónde sale cada respuesta— y se conserva como constancia de ese trabajo.
