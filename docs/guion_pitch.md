# Guion del video · versión 1

**Tarea E4 · borrador** · 8 de octubre de 2026 · Duración objetivo: **3:00** (unas 400 palabras habladas)
Se graba en E6 (23 oct) y se sube a YouTube o Vimeo. Las partes entre corchetes dependen de la lista corta (H4, 17 oct).

**Decisión pendiente:** ¿el video va en español, en inglés o en español con subtítulos en inglés? Conviene confirmar en el sitio del reto qué idiomas acepta el jurado.

**Reglas:** ningún dato que identifique al paciente (ni edad exacta, ni lugar, ni fechas). Las figuras son las del informe.

| # | Tiempo | Bloque | En pantalla |
|---|---|---|---|
| 1 | 0:00–0:20 | Problema | Título + niño ilustrado (no foto) |
| 2 | 0:20–0:45 | El caso | Lista de rasgos clínicos (HPO) |
| 3 | 0:45–1:15 | La variante | Figura 1: BUBR1 con las dos variantes |
| 4 | 1:15–1:50 | El mecanismo | Figura 2: la vía |
| 5 | 1:50–2:35 | Los fármacos | Tabla de la lista corta |
| 6 | 2:35–3:00 | Escalabilidad y cierre | Diagrama del pipeline + enlace al repo |

## Texto

**1 · Problema (20 s)**
Antes de dividirse, cada célula comprueba que sus cromosomas estén bien anclados. En la aneuploidía variegada en mosaico, ese control falla: las células del niño terminan con cromosomas de más o de menos, y el riesgo de cáncer infantil se dispara. Es tan rara que no tiene tratamiento.

**2 · El caso (25 s)**
Nuestro paciente nació prematuro y muy pequeño, crece poco, tiene calcificaciones en el riñón, pérdida de músculo y desarrolló un rabdomiosarcoma. Con su genoma completo nos preguntamos dos cosas: qué está roto y qué fármaco ya aprobado podría ayudar.

**3 · La variante (30 s)**
Analizamos casi 300 genes de la división celular. Solo uno tiene dos variantes dañinas: *BUB1B*, que produce la proteína BUBR1. Una corta la proteína por la mitad y su mensajero se destruye. La otra cambia un solo aminoácido en el extremo de la proteína. Descartamos el resto de los genes, incluso tres falsas alarmas.

**4 · El mecanismo (35 s)**
La clave está en la cantidad. Estudios con células de otros pacientes muestran que los cambios en esta región hacen que BUBR1 se pliegue mal y se degrade, y que si se recupera la cantidad, el control vuelve a funcionar. Nuestro cálculo estructural predice que la variante del paciente también desestabiliza la proteína, aunque menos. El caso publicado más parecido tiene casi la misma combinación. Conclusión: poca BUBR1, un freno mitótico débil y, con el tiempo, aneuploidía, envejecimiento celular y cáncer.

**5 · Los fármacos (45 s)**
Por eso buscamos fármacos que trabajen en la dirección correcta, y descartamos los que empeorarían el freno. Puntuamos cada candidato por mecanismo, seguridad en niños, evidencia e innovación. Nuestra lista corta: [fármaco 1, línea, por qué]; [fármaco 2]; [fármaco 3]. Y una advertencia práctica: algunos fármacos que parecen lógicos, como los inhibidores de HSP90, harían caer aún más la proteína.

**6 · Escalabilidad y cierre (25 s)**
Todo es reproducible: de un VCF a una lista de fármacos priorizados, con cada cita verificada. Para otro paciente con esta enfermedad basta cambiar el archivo de entrada. El siguiente paso es el laboratorio: medir BUBR1 en células del paciente con y sin el fármaco. El código está en GitHub.

## Para grabar (E6)
- Una voz o dos, alternando por bloque. Leer en voz alta y cronometrar antes de grabar.
- Subtítulos siempre (ayudan si el jurado no habla el idioma).
- Revisar que la versión final no muestre datos del VCF en pantalla.
