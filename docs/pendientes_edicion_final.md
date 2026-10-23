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

## Huecos del informe

Todos resueltos (22 oct): línea de IA de Laura (la escribió ella), Gemini (API gratuita, uso del equipo), app de Claude y Perplexity (planes gratuitos, configuración no verificada), autores (Ktalyna García, Laura Vargas, Josefina Wohlfeiler, Thomas German y Lorena Ogas), horas (42 horas-persona: García 10, Vargas 10, Wohlfeiler 8, Ogas 8, German 6) y cita del dataset (ficha de Hugging Face).

## Archivos de entrega

- Informe: `docs/A3-EMBS-ITBA_track2_report.pdf` (doble columna IEEE, 11 páginas). Se regenera con `python scripts/exportar_informe_pdf.py --final --ieee --entrada docs/report_track2_en.md --salida docs/A3-EMBS-ITBA_track2_report.pdf`.
- Formulario: `envios/track2/A3_EMBS_ITBA_methods_description_form.xlsx` (copia de `docs/methods_description_form.xlsx`). No correr `scripts/llenar_formulario.py`, que escribe otra versión en esa ruta.
- Falta: fusionar el PR #30, decidir quién envía, grabar y subir el video.

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
