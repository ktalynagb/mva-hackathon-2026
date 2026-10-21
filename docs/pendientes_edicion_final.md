# Pendientes de la edición final · informe en inglés

Archivo: `docs/report_track2_en.md` · PDF de revisión: `docs/report_track2_en_revision.pdf` (los huecos salen en amarillo) · rama `tarea/E6-cierre-entrega` · nada subido a GitHub todavía.

## Avance por bloque

| Bloque | Sección | Estado |
|---|---|---|
| 1 | Abstract + Index Terms | ✅ Aprobado |
| 2 | I. Introduction | ✅ Aprobado |
| 3 | II. Methods A–D | ✅ Aprobado |
| 4 | II. Methods E–I | ✏️ Escrito, falta tu revisión |
| 5 | III.A Causal Variants (Tabla III, Figs. 1–3) | ✏️ Escrito, falta tu revisión |
| 6 | III.B Biological Mechanism (Tabla IV, Figs. 4–5) | ✏️ Escrito, falta tu revisión |
| 7 | III.C–E Candidates, Proposed Treatment, Pharmacogenetics (Tablas V–VII, Figs. 6–7) | ✏️ Escrito, falta tu revisión |
| 8 | IV. Discussion | ✏️ Escrito, falta tu revisión |
| 9 | V. Conclusion | ✏️ Escrito, falta tu revisión |
| 10 | Acknowledgment (texto oficial de las reglas) + 47 referencias IEEE verificadas en PubMed | ✅ Hecho |

## Lo que tiene que llenar alguien del equipo (en amarillo en el PDF)

| # | Qué | Dónde | Quién |
|---|---|---|---|
| 1 | **Tu línea de IA**: configuración de datos, con la fecha en que se apagó "Help improve Claude"; confirmar que nunca se dieron pulgares | Methods I (busca `TO COMPLETE BY LAURA`) | Laura, a mano |
| 2 | ~~Gemini~~ **Resuelto por Ktalyna (PR #28): API nivel gratuito, sin datos del paciente.** Faltan los ajustes de datos de la app de Claude y de Perplexity | Methods I | Quien las usó |
| 3 | ¿Lourdes es parte del equipo? (no está en la lista de 5) | — | Laura |
| 4 | **Horas-persona** totales | Methods H | Equipo |
| 5 | ~~Apellido de Lorena~~ **Resuelto: Lorena Ogas** | Methods F | — |
| 6 | **Cita del dataset**: la referencia exacta que da la página de Synapse del reto (las reglas la exigen) | Referencia [1] | Copiarla de Synapse |

## Lo que hago yo cuando esté todo lleno

- Copiar tu línea de IA, las horas y el apellido al Excel (`scripts/llenar_formulario_metodos.py`). El resto del Excel ya está sincronizado con el informe.
- Generar el PDF final a doble columna IEEE (`python scripts/exportar_informe_pdf.py --final --ieee --entrada docs/report_track2_en.md --salida docs/A3-EMBS-ITBA_track2_report.pdf`) y revisarlo página por página.
- Subir todo en un PR para que Ktalyna lo revise, después de tu visto bueno.

## Para verificar antes de entregar

- (Resuelto 21 oct) Se quitó la vigilancia del tumor de Wilms: no es un dato del caso y no se pudo confirmar en el texto completo.

## Decisiones ya tomadas

- Ciclofosfamida: parte del tratamiento que el paciente ya recibe para el tumor actual. El cóctel (sirolimus oral + arimoclomol + niacina) es continuo, para el resto de las alteraciones, y podría bajar indirectamente el riesgo de tumores nuevos (como hipótesis).
- *LZTR1* se nombra en el informe.
- Puntajes de fármacos: criterios definidos por el equipo; puntuación con asistencia de IA (declarada); revisión de Lorena. La tabla `results/candidatos_farmacos.tsv` ya dice "revisado por Lorena".
- La doble puntuación independiente no se hizo y no se menciona.

## Pendientes fuera del informe

- Notebook 05: agregar una nota de que su lista de "targets" (PLK1, Aurora, HSP90…) fue preliminar y se descartó por peligrosa.
- Notebooks 01 y 02: revisar fechas y tablas con genotipos antes de hacer público el repositorio.
- Repositorio: hacerlo público cuando termine el hackathon.
- Borrado de datos del paciente: dentro de los 30 días posteriores al cierre (~23 nov 2026), incluida la copia en Drive.
- Video: el guion y las figuras del video ya están en inglés (`docs/paquete_video.md`, `results/video/`).
