# 04 · Lista corta de candidatos (Hito H4, tarea C5)

**Borrador para revisión** · 8 de octubre de 2026
Entrada: `03_criterios.md` (C1) y los 52 candidatos puntuados de `results/candidatos_farmacos.tsv` (C4). Mecanismo base en `02b_resumen_mecanismo.md` (B4).

## 1. Cómo se eligió

Los 5 candidatos son los de mayor puntaje **sin repetir mecanismo**, cubriendo las 4 líneas terapéuticas de `02b` (la regla del equipo pide al menos 2; estos cubren las 4):

| # | Fármaco | Línea | Puntaje (C4) | Por qué entra y no otro con puntaje parecido |
|---|---|---|---|---|
| 1 | **Sirolimus** | 2 · Frenar mTORC1 | 80,0 | El de mayor puntaje; único con datos experimentales en un modelo de ratón con BubR1 hipomórfico |
| 2 | **Arimoclomol** | 1 · Subir BUBR1 (chaperona) | 73,3 | Mejor puntaje de línea 1; mecanismo de proteostasis vía HSF1/HSP70, distinto al de bortezomib |
| 3 | **Temsirolimus** | 2/4 · mTORC1 + tumor | 70,0 | Único con ensayo clínico propio en rabdomiosarcoma; cubre la línea 4 sin necesitar un fármaco de quimioterapia adicional |
| 4 | **Dasatinib** | 3 · Senolítico | 60,0 | Mejor puntaje de línea 3 (venetoclax: 41,7, menos datos pediátricos) |
| 5 | **Bortezomib** | 1 · Subir BUBR1 (proteasoma) | 60,0 | Segundo mecanismo de línea 1 (ixazomib, mismo mecanismo, puntúa menos: 53,3); es el fármaco que prueba directamente la hipótesis del paper base (MG132, Suijkerbuijk 2010) |

No entran por mayor riesgo pese a puntaje similar: **everolimus** (68,3 — mismo mecanismo que sirolimus/temsirolimus, redundante) y **crizotinib/celecoxib** (60,0 — línea 4, pero dependen de biomarcador no confirmado o de un vínculo mecanístico genérico; ver `03b_lista_larga.md`).

---

## 2. Fichas

### 2.1 Sirolimus — Línea 2 (frenar mTORC1)

| | |
|---|---|
| **Mecanismo** | Inhibe mTORC1 (une FKBP12, bloquea el complejo FKBP12-mTOR). En el MVA, la poca BUBR1 produce aneuploidía en mosaico, y las células con cromosomas de más activan mTORC1, acelerando la senescencia y la atrofia muscular del paciente. |
| **Evidencia** | **La más fuerte de toda la lista:** Sieben 2020 (PMID 31738183) trató un ratón con la variante de MVA p.Leu1012Pro de BubR1 (a 10 residuos de nuestro p.Asn1002Lys) con rapamicina (sirolimus) y frenó el deterioro relacionado con la edad. Es el único candidato con datos *in vivo* en un modelo con la proteína del paciente. |
| **Seguridad pediátrica** | Aprobado en niños pequeños (malformaciones vasculares, trasplante). Perfil de toxicidad bien caracterizado: mucositis, hiperlipidemia, mayor riesgo de infección. |
| **Riesgos / compatibilidad** | Inmunosupresor: requiere vigilancia de infecciones durante la quimioterapia del rabdomiosarcoma (vincristina, actinomicina D, ciclofosfamida). Sin nefro ni cardiotoxicidad relevante — compatible con la nefrocalcinosis del paciente. |
| **Cómo se validaría** | Fibroblastos del paciente tratados con sirolimus: medir fosforilación de S6K/4E-BP1 (confirma inhibición de mTORC1) y marcadores de senescencia (p16, p21) antes/después. |

### 2.2 Arimoclomol — Línea 1 (subir BUBR1, chaperona)

| | |
|---|---|
| **Mecanismo** | Amplifica la respuesta de choque térmico (coinductor de HSF1 → sube HSP70). La hipótesis: si el alelo missense se pliega mal y se degrada, ayudar a plegarlo podría llevar la BUBR1 mutante a niveles más cercanos a lo normal. |
| **Evidencia** | Aprobado para Niemann-Pick C (PMID 36455410), otra enfermedad de proteína mal plegada — pero **nunca probado con BUBR1**. Es extrapolación del mecanismo, no un dato directo (por eso K1 = 1, más bajo que sirolimus). |
| **Seguridad pediátrica** | Aprobada desde los 2 años (FDA NDA 214927, Miplyffa). Buen perfil de tolerancia. |
| **Riesgos / compatibilidad** | Interacciones con la quimioterapia por confirmar; en principio sin toxicidad superpuesta mayor. |
| **Cómo se validaría** | Western blot de BUBR1 en fibroblastos del paciente tratados con arimoclomol — el ensayo más directo y barato de los 5: si la cantidad de proteína sube, confirma la hipótesis de proteostasis. |

### 2.3 Temsirolimus — Líneas 2 y 4 (mTORC1 + tumor)

| | |
|---|---|
| **Mecanismo** | Mismo mecanismo que sirolimus (inhibidor de mTORC1), pero con **datos propios en rabdomiosarcoma**: es el único candidato que a la vez actuaría sobre el mecanismo del MVA y trataría el tumor que amenaza la vida del paciente ahora. |
| **Evidencia** | Mascarenhas 2019 (PMID 31513481): mejor supervivencia en recaída de rabdomiosarcoma (fase II, con quimioterapia). Gupta 2024 (PMID 38936378): sin beneficio adicional en riesgo intermedio (fase III) — la evidencia es real pero mixta según el subtipo. |
| **Seguridad pediátrica** | Usado en ensayos pediátricos de rabdomiosarcoma; perfil de toxicidad de rapálogo IV (mucositis, hiperlipidemia, infección). |
| **Riesgos / compatibilidad** | El ensayo de fase III no mostró beneficio en riesgo intermedio: habría que confirmar en qué grupo de riesgo cae este paciente antes de proponerlo como parte del tratamiento oncológico (no solo como terapia del mecanismo de base). Mismo riesgo inmunosupresor que sirolimus. |
| **Cómo se validaría** | Ya validado clínicamente en rabdomiosarcoma (no requiere ensayo preclínico adicional); para el mecanismo de MVA, mismo ensayo que sirolimus. |

### 2.4 Dasatinib — Línea 3 (senolítico)

| | |
|---|---|
| **Mecanismo** | Inhibidor de SRC/ABL; combinado con quercetina (D+Q) elimina células senescentes. En el MVA, las células aneuploides activan programas de senescencia que contribuirían al envejecimiento precoz (talla baja, atrofia muscular). |
| **Evidencia** | El efecto senolítico de D+Q está bien descrito (PMID 25754370), pero en senescencia *en general*, no en células con BUBR1 bajo específicamente — evidencia indirecta (K1 = 1). |
| **Seguridad pediátrica** | Aprobado desde el año de vida para LMC Ph+ pediátrica (Sprycel). |
| **Riesgos / compatibilidad** | Toxicidad hematológica y efusiones pleurales; mielosupresión aditiva con la quimioterapia estándar — requiere vigilancia. |
| **Cómo se validaría** | Medir marcadores de senescencia (p16, p21, SASP) en fibroblastos del paciente antes y después de dasatinib + quercetina. |

### 2.5 Bortezomib — Línea 1 (subir BUBR1, proteasoma)

| | |
|---|---|
| **Mecanismo** | Inhibe el proteasoma. Suijkerbuijk 2010 mostró con MG132 (inhibidor de proteasoma de laboratorio) que bloquear la degradación sube los niveles de BUBR1 mutante en células — bortezomib es la versión aprobada de ese mismo mecanismo. |
| **Evidencia** | Es el candidato que **prueba más directamente** la hipótesis del paper base, aunque con MG132 y no con bortezomib mismo (K1 = 2, el segundo más alto de la lista después de sirolimus). |
| **Seguridad pediátrica** | Uso pediátrico documentado en ensayos de leucemia (p. ej. AALL07P1); neuropatía periférica y trombocitopenia manejables con ajuste de dosis. |
| **Riesgos / compatibilidad** | **Neuropatía periférica aditiva con vincristina** (ambos son neurotóxicos) — es el riesgo de compatibilidad más relevante de los 5; requeriría vigilancia neurológica estrecha o espaciar las dosis. |
| **Cómo se validaría** | Mismo ensayo que arimoclomol: Western blot de BUBR1 en fibroblastos del paciente tratados con bortezomib. |

---

## 3. Resumen para el informe

| Candidato | Línea | K1 (mecanismo) | K2 (seguridad pediátrica) | Riesgo principal |
|---|---|---|---|---|
| Sirolimus | 2 | 3/3 — único con dato directo en modelo BubR1 | 3/3 | Inmunosupresión durante quimio |
| Arimoclomol | 1 | 1/3 — extrapolado de otra enfermedad | 3/3 | Bajo, por confirmar interacciones |
| Temsirolimus | 2+4 | 2/3 | 2/3 | Beneficio incierto en riesgo intermedio |
| Dasatinib | 3 | 1/3 — senescencia genérica | 3/3 | Mielosupresión aditiva |
| Bortezomib | 1 | 2/3 — mismo mecanismo que MG132 | 2/3 | Neuropatía aditiva con vincristina |

**Ninguno está validado en MVA.** Los 5 son hipótesis razonadas a partir del mecanismo (02b) y datos en otras enfermedades o, en el caso de temsirolimus, en el propio tumor del paciente. El experimento común y barato que destraba la mayoría (sirolimus, arimoclomol, bortezomib, dasatinib) es el mismo: **fibroblastos del paciente, antes/después del fármaco**, midiendo el nivel de BUBR1 (Western blot) y/o el checkpoint mitótico (ensayo con nocodazol).

## 4. Decisiones pendientes para quien revise (💊🧬)

1. ¿Se prioriza sirolimus/temsirolimus (mismo mecanismo, pero temsirolimus con dato clínico propio) o se reemplaza uno por everolimus para cubrir más formas de administración (oral vs. IV)?
2. Bortezomib y vincristina comparten neurotoxicidad: ¿vale la pena incluir ambos candidatos de línea 1 (arimoclomol + bortezomib) o conviene dejar solo uno para no competir por el mismo "cupo" de riesgo?
3. Confirmar en qué grupo de riesgo de rabdomiosarcoma cae el paciente, para saber si el dato de fase III de temsirolimus (sin beneficio en riesgo intermedio) lo descarta como parte del tratamiento oncológico.
4. Validar los puntajes K1/K2 de C4 para estos 5 (revisión 💊 pendiente, regla de C1 sec. 1.5).
