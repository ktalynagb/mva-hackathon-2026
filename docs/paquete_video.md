# Paquete para el video · 21 oct 2026

Material para quien graba y edita el video del Track 2. Reemplaza al guion v1 (`guion_pitch.md`, 8 oct), que tenía números y fármacos desactualizados.

## Qué piden las reglas

- **Duración: 3 minutos.** Tiene que recorrer **el razonamiento y los candidatos propuestos**.
- Se sube a **YouTube o Vimeo**. El enlace va en el formulario de envío y es obligatorio.
- **Nada que identifique al paciente**: ni edad, ni lugar, ni fechas, ni fotos. Tampoco se muestran en pantalla tablas del VCF, posiciones genómicas ni genotipos.
- **No mencionar el hallazgo secundario** (el otro gen de predisposición). La regla de hallazgos incidentales sigue en discusión en el equipo.
- Idioma: **sin decidir** (español, inglés o español con subtítulos en inglés). Subtítulos siempre.

## Imágenes, en orden de aparición

Todas están en el repositorio. Las de `results/video/` están hechas para pantalla (16:9, letra grande). Se regeneran con `python scripts/figuras_video.py`.

| # | Bloque | Tiempo | Imagen |
|---|---|---|---|
| 1 | El problema y el caso | 0:00–0:25 | `results/video/video_1_caso.png` |
| 2 | Cómo lo hicimos | 0:25–0:45 | `results/video/video_2_metodo.png` |
| 3 | De 321 genes a uno | 0:45–1:05 | `results/figura_embudo_variantes.png` |
| 4 | Las dos variantes | 1:05–1:25 | `results/figura_1_bubr1_variantes.png` |
| 5 | El mecanismo | 1:25–1:55 | **`results/figura_2_via_mecanismo.png`** (imagen de referencia del mecanismo) |
| 6 | Cómo elegimos los fármacos | 1:55–2:20 | `results/video/video_3_embudo_farmacos.png` y `results/video/video_4_puntajes_candidatos.png` |
| 7 | La propuesta y cómo se comprueba | 2:20–3:00 | `results/video/video_5_propuesta.png` |

**Ojo con la imagen del mecanismo (bloque 5).** Muestra las **cuatro líneas terapéuticas** con ejemplos de cada una (por ejemplo, "sirolimus, everolimus" y "arimoclomol, fenilbutirato"), no la propuesta final. Sirve para explicar **dónde actúa cada tipo de fármaco**; la elección final se ve en el bloque 7. Si se prefiere que coincida exactamente, hay que actualizarla en `scripts/figuras_informe.py`.

## Guion v2 (unas 420 palabras, unos 3 minutos leído con calma)

**1 · El problema y el caso (25 s)**
Antes de dividirse, cada célula comprueba que sus cromosomas estén bien enganchados. En la aneuploidía variegada en mosaico, ese control falla: las células terminan con cromosomas de más o de menos y el riesgo de cáncer infantil se dispara. Nuestro paciente nació prematuro y pequeño, crece poco, pierde músculo, tiene calcio en los riñones y desarrolló un rabdomiosarcoma. Para esta enfermedad no existe un tratamiento dirigido.

**2 · Cómo lo hicimos (20 s)**
Respondimos dos preguntas: qué está roto y qué fármaco ya aprobado podría ayudar. Lo hicimos en cinco pasos, del genoma completo a una propuesta, con un solo comando reproducible y solo con datos públicos.

**3 · De 321 genes a uno (20 s)**
Revisamos 321 genes de la división celular: más de 24.000 variantes. Filtramos por frecuencia en la población y por efecto sobre la proteína en el transcrito de referencia. Solo un gen tiene dos variantes dañinas: *BUB1B*.

**4 · Las dos variantes (20 s)**
*BUB1B* fabrica la proteína BUBR1. Una variante corta la proteína por la mitad y su mensajero se destruye. La otra cambia un solo aminoácido. Es de significado incierto, pero cae en la misma región que las variantes de otros pacientes con la enfermedad.

**5 · El mecanismo (30 s)**
La clave es la cantidad. En células de otros pacientes, los cambios en esta región hacen que BUBR1 se pliegue mal y se degrade, y si se recupera la cantidad el control vuelve a funcionar. Nuestro modelo estructural predice lo mismo para esta variante. Conclusión: pérdida parcial de función. Hay poca BUBR1, el freno de la división es débil y eso lleva a la aneuploidía, al envejecimiento celular y al cáncer.

**6 · Cómo elegimos los fármacos (25 s)**
Del mecanismo salen cuatro estrategias: subir BUBR1, frenar la vía mTOR, eliminar células envejecidas y tratar el tumor sin empeorar el problema. Reunimos 86 fármacos y dejamos solo los aprobados por la FDA o la EMA. Descartamos los que bajarían aún más BUBR1 y puntuamos el resto con seis criterios, entre ellos la seguridad en niños.

**7 · La propuesta (40 s)**
Proponemos dos tratamientos en paralelo. El tumor lo trata la quimioterapia estándar, a intensidad reducida. Para la enfermedad de fondo, que hoy nadie trata, proponemos un esquema continuo de tres fármacos aprobados. Sirolimus oral, para frenar la vía mTOR. Arimoclomol, para ayudar a que BUBR1 se pliegue. Y niacina, por una vía que regula BUBR1 en ratones; esta última es una hipótesis especulativa. Ninguno está probado en esta enfermedad, pero los tres se pueden comprobar con un mismo experimento barato: células de la piel del paciente, midiendo BUBR1 antes y después del fármaco. Todo el código está en GitHub.

## Para grabar

- Leer el guion en voz alta y cronometrarlo antes de grabar. Si pasa de 3:00, acortar el bloque 6.
- Cada imagen debe estar en pantalla al menos 15 segundos para que se pueda leer.
- Antes de subirlo, revisar cuadro por cuadro que no aparezcan datos del VCF ni del paciente.
- Nombre del equipo para la portada y los créditos: **A3 EMBS ITBA**.
