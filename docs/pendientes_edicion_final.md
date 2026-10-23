# Edición final del informe en inglés · registro cerrado

> **Registro histórico del cierre del informe. No quedan pendientes de edición.**
>
> Esta hoja se escribió mientras se redactaba el informe en inglés y se conserva como constancia del proceso. Estado al 23 de octubre de 2026:
>
> - El informe está terminado: `docs/report_track2_en.md` y su PDF de entrega `envios/track2/A3-EMBS-ITBA_track2_report.pdf` (11 páginas, doble columna IEEE, 7 figuras, 47 referencias verificadas contra PubMed).
> - El PR #30 se fusionó y la rama `tarea/E6-cierre-entrega` ya no existe: todo está en `master`.
> - El PDF de revisión con los huecos en amarillo se eliminó del repositorio, para que no se confunda con el entregable.
> - El video está publicado: https://www.youtube.com/watch?v=J1OovR5hoWQ
> - El repositorio es público y su historial fue auditado: no contiene datos del paciente más allá de las dos variantes de *BUB1B*.
>
> Lo único que quedaba sin resolver cuando se escribió esta hoja —designar quién envía— se cerró el 23 de octubre: **envía Laura Vargas**.

Archivo: `docs/report_track2_en.md` · PDF de entrega: `envios/track2/A3-EMBS-ITBA_track2_report.pdf`

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

- Informe: `envios/track2/A3-EMBS-ITBA_track2_report.pdf` (doble columna IEEE, 11 páginas). Se regenera con `python scripts/exportar_informe_pdf.py --final --ieee --entrada docs/report_track2_en.md --salida envios/track2/A3-EMBS-ITBA_track2_report.pdf`.
- Formulario: `envios/track2/A3_EMBS_ITBA_methods_description_form.xlsx`, generado con `scripts/llenar_formulario_metodos.py` a partir de la plantilla oficial en `docs/plantillas/`. (La copia duplicada que había en `docs/` se eliminó, y también el script alternativo que escribía en esa misma ruta y podía sobrescribir el entregable.)
- Video: https://www.youtube.com/watch?v=J1OovR5hoWQ
- ~~Falta: fusionar el PR #30, decidir quién envía, grabar y subir el video.~~ **Los tres resueltos (23 oct):** PR #30 fusionado, video publicado y envía Laura Vargas. Lo único que queda es el envío en sí.

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
