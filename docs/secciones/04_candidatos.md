# 04 · Lista corta de candidatos (Hito H4, tarea C5)

**Borrador para revisión** · 8 de octubre de 2026 · **corregido el 14 oct** con la revisión biológica (C6, sección 5)
Entrada: `03_criterios.md` (C1) y los candidatos puntuados de `results/candidatos_farmacos.tsv` (C4). Mecanismo base en `02b_resumen_mecanismo.md` (B4).

> **Corrección 14 oct.** El borrador del 8 oct decía que Sieben 2020 había tratado ratones BubR1 con rapamicina. No es así: ese trabajo solo **asocia** la sarcopenia de los ratones BubR1 con mTORC1 hiperactivo (PMID 31738183). El tratamiento con rapamicina que frena la sarcopenia se hizo en ratones salvajes (Ham 2020, PMID 32908143). Sirolimus baja de K1 = 3 a 2 y de 80 a 71,7 puntos. **Segunda corrección (14 oct, ficha FDA):** arimoclomol baja de 73,3 a 68,3 por riesgos en un niño con falla de medro y nefrocalcinosis (sección 2.1). Sirolimus vuelve al primer lugar.

## 1. Cómo se eligió

Los 5 candidatos son los de mayor puntaje **sin repetir mecanismo**, cubriendo las 4 líneas terapéuticas de `02b` (la regla del equipo pide al menos 2):

| # | Fármaco | Línea | Puntaje (C4) | Por qué entra y no otro con puntaje parecido |
|---|---|---|---|---|
| 1 | **Sirolimus** | 2 · Frenar mTORC1 | 71,7 | Mejor puntaje de la lista; vía asociada a la sarcopenia en ratones BubR1 y rapamicina eficaz contra la sarcopenia en ratón salvaje |
| 2 | **Temsirolimus** | 2/4 · mTORC1 + tumor | 70,0 | Único con ensayo clínico propio en rabdomiosarcoma; cubre la línea 4 sin otro fármaco de quimioterapia |
| 3 | **Arimoclomol** | 1 · Subir BUBR1 (chaperona) | 68,3 | Mejor puntaje de línea 1; apunta a la causa (poca proteína), pero su mecanismo en NPC es desconocido y tiene riesgos con la falla de medro y el riñón |
| 4 | **Dasatinib** | 3 · Senolítico | 60,0 | Mejor puntaje de línea 3 (venetoclax: 41,7, menos datos pediátricos) |
| 5 | **Bortezomib** | 1 · Subir BUBR1 (proteasoma) | 60,0 | Segundo mecanismo de línea 1 (ixazomib, mismo mecanismo: 53,3); prueba la hipótesis del paper base (MG132, Suijkerbuijk 2010). **La revisión C6 propone reemplazarlo** (sección 5) |

**Hipótesis innovadora, fuera del top por la matriz:** **niacina** (48,3), ficha 2.6. Va en el informe como hipótesis explícitamente especulativa.

No entran pese a puntaje similar: **everolimus** (68,3, mismo mecanismo que sirolimus y temsirolimus) y **crizotinib/celecoxib** (60,0, línea 4, pero dependen de un biomarcador no confirmado o de un vínculo mecanístico genérico; ver `03b_lista_larga.md`).

---

## 2. Fichas

### 2.1 Arimoclomol — Línea 1 (subir BUBR1, chaperona)

| | |
|---|---|
| **Mecanismo** | Amplifica la respuesta de choque térmico (coinductor de HSF1 → sube HSP70). La hipótesis: si el alelo missense se pliega mal y se degrada, ayudar a plegarlo podría llevar la BUBR1 mutante a niveles más cercanos a lo normal. |
| **Evidencia** | Aprobado para Niemann-Pick C (PMID 36455410), pero **la propia ficha de la FDA dice que su mecanismo en NPC es desconocido**: que sube HSP70 es la explicación más aceptada, no un hecho. No se encontró ningún estudio con BUBR1. Fuentes secundarias reportan que en ELA no mostró eficacia. Es extrapolación (K1 = 1). |
| **Seguridad pediátrica** | Aprobado **solo para NPC, junto con miglustat, desde los 2 años** (FDA NDA 214927, Miplyffa); no se estableció seguridad en menores de 2 años. Usarlo aquí sería fuera de indicación. Efectos frecuentes (≥ 15 %): infección respiratoria alta, diarrea y **baja de peso**. Urticaria y angioedema en 9 % de los pacientes. |
| **Riesgos / compatibilidad** | **Dos alertas para este paciente:** (1) la baja de peso, con falla de medro; (2) sube la creatinina 10–20 % sin cambiar el filtrado (inhibe el transportador OCT2), así que la función renal debe seguirse con cistatina C, y en ratas jóvenes hubo dilatación de la pelvis renal. Con la nefrocalcinosis del paciente exige vigilancia renal. K4 = 1. |
| **Cómo se validaría** | Western blot de BUBR1 en fibroblastos del paciente tratados con arimoclomol: el ensayo más directo y barato. Si la cantidad de proteína sube, confirma la hipótesis de proteostasis. |

### 2.2 Sirolimus — Línea 2 (frenar mTORC1)

| | |
|---|---|
| **Mecanismo** | Inhibe mTORC1 (une FKBP12 y bloquea el complejo FKBP12-mTOR). Objetivo: la atrofia muscular y el envejecimiento precoz, no la falta de BUBR1. |
| **Evidencia** | En ratones con mutaciones de BubR1, la sarcopenia **coincide** con mTORC1 hiperactivo (Sieben 2020, PMID 31738183; correlación en portadores de una mutación, no un tratamiento). En ratones salvajes envejecidos, la rapamicina a largo plazo frena la sarcopenia (Ham 2020, PMID 32908143). **Nadie trató todavía un modelo de BubR1 con rapamicina** (K1 = 2). |
| **Seguridad pediátrica** | Uso en niños pequeños (malformaciones vasculares, trasplante). Toxicidad conocida: mucositis, hiperlipidemia, más infecciones. |
| **Riesgos / compatibilidad** | Inmunosupresor: vigilar infecciones durante la quimioterapia del rabdomiosarcoma (vincristina, actinomicina D, ciclofosfamida). Sin nefro ni cardiotoxicidad relevante, compatible con la nefrocalcinosis. |
| **Cómo se validaría** | Fibroblastos del paciente tratados con sirolimus: fosforilación de S6K/4E-BP1 (confirma la inhibición de mTORC1) y marcadores de senescencia (p16, p21). El paso clave que falta es tratar el ratón BubR1<sup>H/L1002P</sup> de Sieben 2020. |

### 2.3 Temsirolimus — Líneas 2 y 4 (mTORC1 + tumor)

| | |
|---|---|
| **Mecanismo** | Mismo mecanismo que sirolimus, pero con **datos propios en rabdomiosarcoma**: es el único candidato que actuaría a la vez sobre el MVA y sobre el tumor que amenaza la vida del paciente ahora. |
| **Evidencia** | Mascarenhas 2019 (PMID 31513481): mejor supervivencia en recaída de rabdomiosarcoma (fase II, con quimioterapia). Gupta 2024 (PMID 38936378): sin beneficio adicional en riesgo intermedio (fase III). La evidencia es real pero depende del subtipo. |
| **Seguridad pediátrica** | Usado en ensayos pediátricos de rabdomiosarcoma; toxicidad de rapálogo IV (mucositis, hiperlipidemia, infección). |
| **Riesgos / compatibilidad** | Hay que confirmar el grupo de riesgo del tumor antes de proponerlo como parte del tratamiento oncológico. Mismo riesgo inmunosupresor que sirolimus. |
| **Cómo se validaría** | Ya validado clínicamente en rabdomiosarcoma; para el MVA, el mismo ensayo que sirolimus. |

### 2.4 Dasatinib — Línea 3 (senolítico)

| | |
|---|---|
| **Mecanismo** | Inhibidor de SRC/ABL; con quercetina (D+Q) elimina células senescentes. En el MVA, las células aneuploides activan programas de senescencia que contribuirían al envejecimiento precoz. |
| **Evidencia** | Efecto senolítico de D+Q bien descrito (PMID 25754370), pero en senescencia *en general*. En ratones BubR1<sup>H/H</sup>, eliminar las células senescentes por vía genética retrasa el envejecimiento (Baker 2011, citado en `02b`), sin fármaco (K1 = 1). |
| **Seguridad pediátrica** | Aprobado desde el año de vida para LMC Ph+ (Sprycel). |
| **Riesgos / compatibilidad** | Toxicidad hematológica y derrames pleurales; mielosupresión que se suma a la de la quimioterapia. |
| **Cómo se validaría** | Marcadores de senescencia (p16, p21, SASP) en fibroblastos del paciente antes y después de dasatinib + quercetina. |

### 2.5 Bortezomib — Línea 1 (subir BUBR1, proteasoma)

| | |
|---|---|
| **Mecanismo** | Inhibe el proteasoma. Suijkerbuijk 2010 mostró con MG132 (inhibidor de laboratorio) que bloquear la degradación sube la BUBR1 mutante en células; bortezomib es la versión aprobada del mismo mecanismo. |
| **Evidencia** | Prueba la hipótesis del paper base, aunque con MG132 y no con bortezomib (K1 = 2). |
| **Seguridad pediátrica** | Uso pediátrico en ensayos de leucemia (p. ej. AALL07P1); neuropatía periférica y trombocitopenia manejables con ajuste de dosis. |
| **Riesgos / compatibilidad** | **Neuropatía aditiva con vincristina**, y el problema mitótico de la sección 5. |
| **Cómo se validaría** | Western blot de BUBR1 en fibroblastos del paciente tratados con bortezomib. |

### 2.6 Niacina — Línea 1 (subir BUBR1 por NAD⁺ y SIRT2) · **hipótesis innovadora**

| | |
|---|---|
| **Mecanismo** | La niacina (ácido nicotínico, vitamina B3) es precursora de NAD⁺. La enzima SIRT2 necesita NAD⁺ para mantener a BubR1 sin un grupo acetilo en la lisina 668; con ese grupo, BubR1 se marca para destruirse. Más NAD⁺ → más SIRT2 activa → BubR1 se degrada menos. |
| **Evidencia** | North 2014 (PMID 24825348): el precursor **NMN** sube BubR1 en ratones, y sobreexpresar SIRT2 alarga la vida de ratones con poca BubR1 (BubR1<sup>H/H</sup>). **Límites:** se usó NMN (no aprobado) y no niacina; los ratones tenían BubR1 normal o hipomórfica, no el mutante del paciente; y la p.Asn1002Lys se degrada por mal plegamiento, que puede ser independiente de la acetilación de K668. Además: (1) **el rescate de 2014 no tuvo réplica independiente**; el mismo grupo mostró después que SIRT2 extra no alarga la vida de ratones normales (Wu 2023, PMID 38009412), lo que sugiere que el efecto es específico de la poca BubR1, como en este paciente; (2) en células humanas SIRT2 desacetila BubR1 en otra lisina (K250) y quitar SIRT2 no cambió la cantidad total de BubR1 (Suematsu 2014, PMID 25285631). Búsqueda en PubMed (14 oct): 0 trabajos unen NAD⁺, SIRT2, NMN o niacina con el MVA (K1 = 2, K5 = 1). |
| **Seguridad pediátrica** | La ficha de la FDA (Niacor) dice que la seguridad y eficacia en niños **no se han establecido**. A dosis farmacológicas: rubor, molestias digestivas y toxicidad hepática. K2 = 1. |
| **Riesgos / compatibilidad** | Riesgo teórico: subir NAD⁺ podría favorecer el metabolismo de un tumor activo (los inhibidores de la síntesis de NAD⁺ se estudian como antitumorales). La hepatotoxicidad se suma a la de la actinomicina D. K4 = 1. |
| **Cómo se validaría** | El experimento más barato de la lista: Western blot de BUBR1 y de BubR1 acetilado en K668 en fibroblastos del paciente tratados con niacina o NMN. Si no sube, la hipótesis se descarta en una semana. |

---

## 3. Resumen para el informe

| Candidato | Línea | K1 (mecanismo) | K2 (seguridad pediátrica) | Riesgo principal |
|---|---|---|---|---|
| Arimoclomol | 1 | 1/3, extrapolado de otra enfermedad | 3/3 | Bajo, interacciones por confirmar |
| Sirolimus | 2 | 2/3, vía asociada en ratón BubR1; fármaco probado en ratón salvaje | 3/3 | Inmunosupresión durante la quimio |
| Temsirolimus | 2+4 | 2/3 | 2/3 | Beneficio incierto en riesgo intermedio |
| Dasatinib | 3 | 1/3, senescencia genérica | 3/3 | Mielosupresión aditiva |
| Bortezomib | 1 | 2/3, mismo mecanismo que MG132 | 2/3 | Neuropatía con vincristina; frena la salida de la mitosis |

**Ninguno está validado en MVA.** Son hipótesis razonadas a partir del mecanismo (02b) y de datos en otras enfermedades o, en el caso de temsirolimus, en el propio tumor del paciente. El experimento común y barato es el mismo para casi todos: **fibroblastos del paciente antes y después del fármaco**, midiendo el nivel de BUBR1 (Western blot) y el checkpoint mitótico (ensayo con nocodazol).

## 4. Decisiones pendientes para quien revise (💊🧬)

1. ¿Sirolimus y temsirolimus (mismo mecanismo, temsirolimus con dato clínico propio), o uno de ellos reemplazado por everolimus (oral)?
2. **Bortezomib o niacina** como segundo candidato de línea 1 (sección 5).
3. Confirmar el grupo de riesgo del rabdomiosarcoma del paciente, para saber si la fase III de temsirolimus lo descarta como parte del tratamiento oncológico.
4. Validar los puntajes K1/K2 de C4 para estos 5 (regla de C1 sec. 1.5).

---

## 5. Revisión biológica (C6, 14 oct): ¿algún candidato empeora la mitosis?

La pregunta de C6 es si cada fármaco, además de su efecto buscado, **debilita aún más la división celular** de un paciente que ya tiene el checkpoint mitótico débil.

| Fármaco | ¿Empeora la mitosis? | Lectura |
|---|---|---|
| Arimoclomol | No conocido | Sube HSP70; no inhibe HSP90, que es la chaperona que necesita la BUBR1 mutante. Compatible con el objetivo |
| Sirolimus / temsirolimus | No | Frenan el crecimiento celular (fase G1); menos divisiones implica menos ocasiones de repartir mal los cromosomas |
| Dasatinib | No conocido a dosis senolíticas | Elimina células senescentes, muchas de ellas aneuploides: va en la dirección buscada |
| **Bortezomib** | **Sí, de forma indirecta** | Al frenar el proteasoma también frena la degradación de ciclina B y securina, que es lo que permite salir de la mitosis. Por eso los inhibidores del proteasoma detienen células en metafase (es el uso clásico de MG132 en el laboratorio), y bortezomib prolonga la detención mitótica en células de LMA (*Oncotarget*, artículo 15503). No debilita el checkpoint, pero agrega estrés mitótico a todas las células que se dividen, además de la neuropatía con vincristina |

**Propuesta: presentar niacina como hipótesis innovadora, aparte de la lista corta, y cuestionar bortezomib.** Comparación:

| | Bortezomib | Niacina (vitamina B3) |
|---|---|---|
| Cómo subiría BUBR1 | Frena toda la degradación de proteínas (proteasoma) | Sube NAD⁺ → SIRT2 desacetila BubR1 en K668 → BubR1 se degrada menos |
| Evidencia | MG132 en células (Suijkerbuijk 2010) | NMN, otro precursor de NAD⁺, **sube BubR1 en ratones vivos**; SIRT2 alarga la vida de ratones BubR1<sup>H/H</sup> (North 2014, PMID 24825348) |
| Aprobación | FDA, EMA | FDA (Niacor, ANDA040378) |
| Riesgos | Citotóxico, neuropatía, frena la salida de la mitosis | Rubor y hepatotoxicidad a dosis farmacológicas; subir NAD⁺ podría favorecer el metabolismo del tumor |
| Puntaje con la matriz | 60,0 | 48,3 |

Por la matriz, la niacina **puntúa menos**: no tiene datos clínicos, no tiene indicación pediátrica a esas dosis, y su riesgo con el tumor activo baja K4. A favor tiene que apunta a la causa (la cantidad de BubR1), que su vía tiene datos *in vivo* (con NMN, su precursor; **la niacina misma no se probó**) y que no es citotóxico. Dudas abiertas:
- North 2014 usó NMN y ratones salvajes, no niacina ni el mutante. No se sabe si la vía de K668 afecta a la p.Asn1002Lys, que se degrada por mal plegamiento.
- La NMN y el nicotinamida ribósido no están aprobados como fármacos (F1). La nicotinamida solo figura en multivitamínicos inyectables.

**Validación**, la misma que para arimoclomol: Western blot de BUBR1 en fibroblastos del paciente tratados con niacina o NMN. Si sube con los dos mecanismos, se refuerza la línea 1 completa.

---

## 6. Línea condicional: tumor con RAS activado (A10, 15 oct)

Sale del hallazgo secundario en *LZTR1* (`01_variante_causante.md`, sección 5c). *LZTR1* marca a las proteínas RAS para que se degraden. Si el tumor perdió la otra copia, la vía RAS estaría más activa, y el rabdomiosarcoma sin fusión depende de esa vía. **Solo se propone si la biopsia lo confirma:** pérdida de 22q11 o segunda mutación de *LZTR1*, una mutación de la vía RAS o fosfo-ERK alto.

| | Trametinib | Selumetinib |
|---|---|---|
| Aprobación (FDA) | Mekinist, desde 1 año (BRAF V600E: gliomas de bajo grado y tumores sólidos) | Koselugo, desde 1 año (NF1 con neurofibromas plexiformes) |
| Puntaje (C4) | 65,0 | 65,0 |
| Evidencia en rabdomiosarcoma | Preclínica: MEK + anti-IGF1R eficaz en modelos con RAS mutado (PMID 36322002); MEK + PI3K/mTOR letal para las células (PMID 23684925) | Clínica, negativa en monoterapia: ninguna respuesta en el Pediatric MATCH, que incluyó 7 rabdomiosarcomas (PMID 35363510) |

**Nunca en monoterapia.** Las combinaciones con fundamento son con **temsirolimus** (mTOR, ya en la lista corta) o con un **anti-IGF1R** (teprotumumab es el único aprobado; está en la lista larga con 43,3). Riesgos: piel, CK, función cardíaca (FEVI) y ojos. Inhibir MEK frena el ciclo en G1 y no debilita el checkpoint mitótico.

**Por qué es innovador:** une un hallazgo germinal secundario con el tratamiento del tumor. En PubMed hay un solo trabajo que une *LZTR1* con el rabdomiosarcoma.
