# Qué subir al enviar el Track 2

Equipo **A3 EMBS ITBA** · fecha límite **24 de octubre de 2026, 18:00 UTC**

**Envía Laura Vargas** (decidido el 23 de octubre). El reto acepta un solo envío por equipo y el panel revisa solo el de la persona designada, así que nadie más debe enviar.

## Los cuatro entregables

| # | Qué | Dónde está |
|---|---|---|
| 1 | **Informe** en PDF | [`A3-EMBS-ITBA_track2_report.pdf`](A3-EMBS-ITBA_track2_report.pdf) — 11 páginas, doble columna IEEE, 7 figuras, 47 referencias |
| 2 | **Formulario de métodos** | [`A3_EMBS_ITBA_methods_description_form.xlsx`](A3_EMBS_ITBA_methods_description_form.xlsx) — hoja "Track 2 methods", 11 preguntas |
| 3 | **Enlace al video** (3 min) | https://www.youtube.com/watch?v=J1OovR5hoWQ |
| 4 | **Enlace al repositorio** | https://github.com/ktalynagb/mva-hackathon-2026 (ya es público) |

## Verificado antes de publicar el repositorio

- Historial de git auditado: no contiene datos del paciente más allá de las dos variantes de *BUB1B*, que son el resultado del trabajo.
- Sin tokens ni credenciales en ningún commit.
- `data/` no está versionado: el VCF y el documento clínico nunca salieron de las computadoras del equipo.
- El pipeline corre completo con `python run_pipeline.py` (8 pasos, 6 min 11 s) y reproduce todos los números del informe.

## Después del cierre

Según los términos de acceso al dataset, cada integrante debe **borrar los datos del paciente** dentro de los 30 días del cierre (aproximadamente el 23 de noviembre de 2026), incluidas las copias en la nube, y notificarlo a `MVAHackathon2026@synapse.org`.
