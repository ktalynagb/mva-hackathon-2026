# Revisión del informe final · 21 oct 2026

Revisión de `docs/informe_final.md` con los cambios de Ktalyna hasta el PR #26 (fusionado el 21 oct). Esta hoja va **solo en el PDF de revisión**. En el texto del informe, los huecos aparecen **resaltados en amarillo**.

## A. Lo que falta llenar (bloquea la entrega)

| # | Dónde | Qué falta | Quién |
|---|---|---|---|
| A1 | Encabezado (línea 3) | ~~Nombre del equipo~~ **Resuelto:** A3 EMBS ITBA (informe, Excel y PDF `A3-EMBS-ITBA_track2_report.pdf`) | Hecho |
| A2 | 2.6 Uso de IA | **Fila de Laura**: plan, configuración de datos, para qué se usó y si recibió datos del paciente. La escribe Laura, con la fecha en que apagó "Help improve Claude" | Laura |
| A3 | 2.6 Uso de IA | **Fila de Gemini**: plan, configuración, si recibió datos del paciente y quién lo usó | Quien hizo el cuaderno 06 |
| A4 | 2.6 Uso de IA | Fila `[otra]` vacía y la marca `[PENDIENTE · E8]`: se completan o se borran | Equipo |
| A5 | Repositorio | El repo **sigue privado**. Tiene que ser público cuando empiece la evaluación, después de comprobar que no tenga datos del paciente | Ktalyna (dueña) |

Las notas internas (línea "Estado: borrador v0", recuadro "Cómo se usa este archivo", líneas "Fuente/Tarea" y "Guía de estilo") **no hace falta borrarlas a mano**: `python scripts/exportar_informe_pdf.py --final` las quita al generar el PDF de entrega.

## B. Contradicciones que el equipo tiene que resolver

| # | Dónde | Qué pasa |
|---|---|---|
| B1 | 3.3, "Qué proponemos para el tumor" | Dice **"Temsirolimus es nuestra propuesta para el tumor"** y lo pone en la tabla para sumarlo al tumor actual. La Conclusión de la misma sección (PR #26, el más nuevo) dice que temsirolimus queda **solo para recaída**. Ese bloque viene del PR #25 y no se actualizó. Hay que elegir una postura y dejarla igual en 3.3, en la Discusión y en el párrafo de nab-sirolimus ("para la línea 4, temsirolimus sigue primero") |
| B2 | **Resuelto 21 oct: se nombra *LZTR1* (decisión de Laura).** Resumen, 3.1, 3.3 y Discusión | El hallazgo secundario en ***LZTR1*** aparece con nombre, y el Resumen nombra además BRCA1/2, PALB2, RAD51C/D y CHEK2. La regla del reto (discusión #20) pide **no publicar hallazgos incidentales no relacionados** en el repo público. Decidir si se deja, se anonimiza ("un gen de predisposición a schwannomatosis") o se saca del repo y va solo en el PDF |
| B3 | 3.3, tabla de candidatos | Muestra los 5 de la lista corta, incluido bortezomib, aunque la propuesta final usa 3. Agregué una frase que lo aclara; el equipo decide si la tabla se queda así |

| B4 | 3.3, tratamiento del tumor | **Pregunta enviada al grupo (21 oct):** ¿se menciona el mantenimiento con vinorelbina + ciclofosfamida oral a dosis bajas (RMS 2005, PMID 31562043 y 40053891) para el rabdomiosarcoma de alto riesgo? Y se deja explícito que no se propone ciclofosfamida a largo plazo para prevenir tumores nuevos (alquilante, riesgo de cáncer secundario con inestabilidad cromosómica) |

## C. Rigor científico (lo que el jurado podría objetar)

| # | Dónde | Qué pasa | Estado |
|---|---|---|---|
| C1 | 5. Referencias | **16 de las 32 referencias con PMID tenían mal el autor, la revista o las páginas, y a otras 2 les faltaban datos** (los PMID sí estaban bien). Ejemplos: North 2014 es *EMBO J*, no *Cell*; Sieben 2020 es *JCI* 130:171–88; PMID 38936378 es Gupta 2024 en *Lancet Oncol*, no Hawthorne en *JCO*; PMID 23684925 es Guenther 2013, no Elhossiny 2023 | **Corregido** contra PubMed |
| C2 | Resumen | Dice que p.Asn1002Lys "desestabiliza la proteína por mal plegamiento" como un hecho. Es una **predicción** (ΔΔG y analogía con otras variantes de la región), y el alelo es VUS. Sugerencia: "que se predice desestabilizante" | Pendiente |
| C3 | 4. Discusión | Dice "diagnóstico de MVA1 **con alta confianza**" con el alelo 2 en VUS y la fase sin resolver. Sugerencia: "diagnóstico de MVA1 muy probable" | Pendiente |
| C4 | 3.3, Vigilancia | Las cifras del tumor de Wilms (~50 %, ecografía cada 3 meses hasta los 7 años) **no se confirmaron en el texto completo**: la propia nota de Ktalyna (PR #25) dice que hay que verificarlas | Pendiente |
| C5 | 2.2, paso 5 | Menciona el análisis de sensibilidad con variantes no-PASS (cuaderno 02b), pero en Resultados no aparece su resultado. Se agrega una línea con el resultado o se quita el paso | Pendiente |
| C6 | 1. Introducción | Las viñetas sin redactar se reemplazaron por la **introducción acordada el 20 oct**. La lista de rasgos HPO quedó fuera: si el equipo la quiere, va en una línea al inicio de 3.1 | Hecho |
| C7 | 3.1 | La guía de estilo pide nombrar el transcrito la primera vez | **Agregado** ENST00000287598 (MANE Select, confirmado en Ensembl) |
