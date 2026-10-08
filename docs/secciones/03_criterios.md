# 03 · Criterios para priorizar fármacos

**Tarea C1 · borrador para revisión de alguien con perfil 💊** · 8 de octubre de 2026
Sirve para puntuar la lista larga (C3 → C4) y elegir la lista corta (C5, Hito H4, 17 oct). La base biológica está en `02b_resumen_mecanismo.md`.

## 1. Cómo se usa

1. Cada fármaco de la lista larga pasa primero por los **filtros de exclusión** (sección 2). Si falla uno, queda fuera y se anota el motivo.
2. Los que pasan reciben una **nota de 0 a 3 en seis criterios** (sección 3). Cada nota lleva su fuente.
3. **Puntaje = Σ (peso × nota / 3)**, de 0 a 100.
4. La lista corta son los 3 a 5 mejores puntajes, con una condición: **que haya al menos dos líneas terapéuticas distintas** (de las cuatro de `02b`), para no apostar todo a una sola hipótesis.
5. Dos personas puntúan por separado los 10 primeros. Si difieren en más de 1 punto en un criterio, se discute y se anota la decisión.

## 2. Filtros de exclusión

| Filtro | Se excluye si… | Fuente |
|---|---|---|
| F1 · Aprobación | No está aprobado por la FDA **ni** por la EMA para ninguna indicación | Drugs@FDA (API de openFDA) · base de medicamentos de la EMA |
| F2 · Dirección del mecanismo | Baja la cantidad de BUBR1 o debilita aún más la mitosis en células normales: inhibidores de HSP90, PLK1, Aurora, MPS1 o APC/C | `02_marco_biologico.md`, secciones 4 y 7 |
| F3 · Edad | Contraindicado a la edad del paciente | Ficha técnica (DailyMed, EPAR), sección de uso pediátrico |
| F4 · Retirada | Retirado del mercado por seguridad | Drugs@FDA, EMA |

> F2 es lo que más nos separa de una búsqueda genérica: un fármaco "contra la mitosis" o "sobre BUBR1" puede ir en la dirección equivocada. El cuaderno 06 propuso varios de este tipo.

## 3. Criterios, pesos y escalas

| # | Criterio | Peso | Qué pregunta responde |
|---|---|---|---|
| K1 | Solidez del vínculo mecanístico | **25** | ¿Por qué actuaría sobre lo que está roto en este paciente? |
| K2 | Seguridad pediátrica | **20** | ¿Se puede dar a un niño, a su edad, con riesgos conocidos? |
| K3 | Evidencia de eficacia | **15** | ¿Hay datos, y en qué tipo de paciente o modelo? |
| K4 | Compatibilidad con el caso | **15** | ¿Choca con el tratamiento del rabdomiosarcoma o con la fragilidad del paciente? |
| K5 | Innovación | **15** | ¿Es una conexión que aún nadie propuso para el MVA? |
| K6 | Validación factible | **10** | ¿Hay un experimento claro y barato para comprobarlo? |

Los pesos siguen los criterios del reto: el rigor científico (35 %) se refleja en K1 + K3 = 40; el impacto clínico (25 %) en K2 + K4 = 35; la innovación (25 %) en K5 + K6 = 25.

### Escalas (nota de 0 a 3)

| Nota | K1 · Vínculo mecanístico | K2 · Seguridad pediátrica | K3 · Eficacia |
|---|---|---|---|
| **3** | Datos experimentales con BUBR1 o en MVA | Aprobado en pediatría a la edad del paciente | Datos clínicos en MVA o en rabdomiosarcoma |
| **2** | Datos en un modelo de la vía (ratón BubR1, células con SAC débil) | Uso pediátrico documentado (ensayos u otra indicación) | Datos clínicos en otra enfermedad con el mismo mecanismo (p. ej., otra proteína mal plegada) |
| **1** | Razonamiento plausible sin datos propios | Solo adultos, con toxicidad manejable | Solo preclínicos |
| **0** | Vínculo débil o genérico ("antitumoral") | Toxicidad grave esperada en niños | Ninguna |

| Nota | K4 · Compatibilidad | K5 · Innovación | K6 · Validación |
|---|---|---|---|
| **3** | Sin interacciones relevantes con la quimioterapia del rabdomiosarcoma (vincristina, actinomicina D, ciclofosfamida, irinotecán) ni con un niño con falla de medro y nefrocalcinosis | No hay publicaciones que lo relacionen con BUBR1 ni con el MVA | Ensayo directo en células del paciente (nivel de BUBR1 por Western blot, checkpoint con nocodazol) |
| **2** | Interacciones manejables con ajuste de dosis o vigilancia | Relacionado con modelos de BubR1 pero sin propuesta clínica | Ensayo en un modelo celular estándar |
| **1** | Riesgo relevante (p. ej., inmunosupresión durante la quimioterapia) | Propuesto antes para el MVA o para el envejecimiento por BubR1 | Solo validable en modelo animal |
| **0** | Conflicto serio con el tratamiento o con un órgano afectado | Uso obvio ya establecido | Sin forma clara de validarlo |

**K4 incluye los órganos afectados del paciente:** la nefrocalcinosis obliga a revisar la eliminación renal y la nefrotoxicidad; la falla de medro, el efecto sobre el apetito y el peso.

## 4. Columnas del `.tsv` de la lista larga

`results/candidatos_farmacos.tsv` (C3, C4):

```
farmaco  linea  diana  fda  ema  f1  f2  f3  f4  excluido_por
k1  k2  k3  k4  k5  k6  puntaje  fuentes  quien_puntua  notas
```

- `linea`: 1 = subir BUBR1 · 2 = mTORC1 · 3 = senolítico · 4 = tumor · otra (explicar en `notas`).
- `fuentes`: PMID, número de aplicación de la FDA o enlace del EPAR para cada nota distinta de 0.
- El `.tsv` va en `results/`, que el `.gitignore` excluye para tablas. Como no contiene datos del paciente, se sube con `git add -f`, o se guarda en `docs/` si el equipo lo prefiere (decisión pendiente).

## 5. Ejemplo de uso (no es un puntaje final)

| | Arimoclomol | Volasertib |
|---|---|---|
| F1 · Aprobación | ✅ FDA (Miplyffa, NDA 214927, 20 sep 2024). EMA: por verificar | ❌ Sin aprobación FDA ni EMA |
| F2 · Dirección | ✅ Amplifica la respuesta de choque térmico; no debilita la mitosis | ❌ Inhibe PLK1 |
| Resultado | Pasa a puntuar | **Excluido (F1, F2)** |
| K1 | 1 · Plausible: ayuda a plegar proteínas mal plegadas, sin datos con BUBR1 | — |
| K2 | 3 · Aprobado desde los 2 años (suponiendo que el paciente los tenga) | — |
| K3 | 2 · Eficacia clínica en Niemann-Pick C, enfermedad de proteína mal plegada | — |
| K4 | 2 · Interacciones con la quimioterapia por revisar | — |
| K5 | 3 · Sin publicaciones con BUBR1 o MVA | — |
| K6 | 3 · Western blot de BUBR1 en fibroblastos tratados | — |
| **Puntaje** | 25×1/3 + 20×3/3 + 15×2/3 + 15×2/3 + 15×3/3 + 10×3/3 = **73** | — |

## 6. Decisiones que debe tomar quien revise (💊)

1. ¿Los pesos están bien? En especial K2 (20) frente a K1 (25).
2. ¿Aceptamos fármacos aprobados solo por la EMA, o solo por la FDA? El reto dice "FDA/EMA"; propongo que baste con una.
3. ¿Cuál es la edad del paciente para K2? Está en el documento clínico (no copiarla al repo si no hace falta).
4. ¿El `.tsv` va en `results/` (forzando `git add -f`) o en `docs/`?
5. ¿Agregamos la interacción con la radioterapia, también parte del tratamiento del rabdomiosarcoma?
