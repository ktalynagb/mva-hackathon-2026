# Bitácora del Proyecto — MVA Hackathon 2026

**Track 2 — Reposicionamiento de Fármacos**  
**Repo:** https://github.com/ktalynagb/mva-hackathon-2026  
**Deadline:** 24 de octubre de 2026, 23:59 UTC  
**Equipo:** Ktalyna · Laura · Josefina · (completar)

> Registra qué se hizo, quién lo hizo, qué se decidió y qué sigue.  
> Cada entrada nueva va **arriba**. Formato: `## YYYY-MM-DD — Título`.

---

## 2026-10-21 (noche bis) — Corrección de la jefa: esquema continuo y la ciclofosfamida se queda

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C5-esquema-final`  
**Disparador:** la jefa planteó: "por eso dejábamos ciclofosfamida, y hacíamos un tratamiento continuo con sirolimus oral, arimoclomol y niacinamida".

**Se adopta el encuadre, que es mejor que el anterior.** La propuesta ahora separa explícitamente dos tratamientos con objetivos distintos:
- **Oncología estándar:** el rabdomiosarcoma lo trata el **VAC a intensidad reducida**, con ciclofosfamida. No es reposicionamiento ni necesita serlo.
- **Reposicionamiento (nuestro aporte):** esquema **continuo** de sirolimus oral + arimoclomol + niacina, dirigido a la enfermedad de fondo, que es lo que hoy no trata nadie.

**Consecuencia: el rapálogo pasa a ser sirolimus oral, no temsirolimus.** Como el tumor ya está cubierto por la quimioterapia, el rapálogo no necesita efecto antitumoral propio, y conviene el que sirve para tratamiento prolongado: oral, el más barato, con dosificación pediátrica establecida y TDM de rutina, y el de mejor puntaje de la lista (71,7). Esto invierte la decisión que habíamos cerrado horas antes a favor de temsirolimus; el criterio que cambia es quién trata el tumor. Temsirolimus queda documentado como la opción en recaída o si se busca sumar efecto antitumoral propio, y dasatinib como senolítico para después de la quimioterapia.

**Se corrigió la sección 8.1,** que decía "por qué la ciclofosfamida no va como candidata" y podía leerse como que no se usaba. Ahora dice lo correcto: la ciclofosfamida **trata el tumor y se mantiene**; lo que no corresponde es presentarla como propuesta de reposicionamiento, porque tratar un rabdomiosarcoma es exactamente su indicación aprobada.

**Punto técnico que NO se adoptó, con fundamento: niacinamida → se mantiene niacina.** La jefa dijo "niacinamida". Son distintas y para esta hipótesis son opuestas:
- La **nicotinamida (niacinamida)** es el **producto** de la reacción de las sirtuinas y su **inhibidor por retroalimentación**: inhibe de forma no competitiva a Sir2 y SIRT1 *in vitro* (IC50 SIRT1 ≈ 50–180 µM). En el mismo trabajo, el **ácido nicotínico (niacina) no tuvo efecto** sobre SIRT1 (Bitterman 2002, *J Biol Chem* 277(47):45099–107, PMID 12297502).
- Toda nuestra hipótesis depende de que **SIRT2 esté activa** para mantener BubR1 sin acetilar en K668. Dar el inhibidor propio de la enzima es ambiguo: en células la nicotinamida se convierte rápido en NAD⁺ y podría estimular (Hwang 2017, *Cell Mol Life Sci* 74(18):3347–62, PMID 28417163), pero esa indefinición es el problema.
- **Tampoco pasa F1:** la nicotinamida solo figura en multivitamínicos inyectables, no como fármaco aprobado por sí misma. La niacina sí (Niacor, ANDA040378).
- Probablemente sea un uso indistinto de los nombres (las dos son vitamina B3). Queda documentado en la ficha 2.6 y en la conclusión del informe para que el equipo decida con los datos.

Actualizados el Resumen, la Discusión, las secciones 8.1 y 8.4, la decisión 1 de la sección 4 y las referencias.

---

## 2026-10-21 (noche) — Cerrada la decisión sirolimus vs. temsirolimus: el esquema queda en 3 fármacos

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C5-esquema-final`

**Problema detectado al redactar la conclusión:** el informe listaba 5 candidatos incluyendo **sirolimus y temsirolimus juntos**, que son **el mismo mecanismo** (ambos rapálogos, inhiben mTORC1). Proponerlos juntos duplica la vía y suma inmunosupresión sin beneficio. Era la decisión pendiente nº 1 de la sección 4 de `04_candidatos.md`, abierta desde el 8 oct.

**Resuelta: temsirolimus.** Con el rabdomiosarcoma activo, cubre la línea 2 (eje mTORC1 del MVA) y la línea 4 (tumor) con un solo fármaco, y es el único con evidencia clínica en este tumor (fase II, PMID 31513481). **Sirolimus oral pasa a ser la opción de la fase crónica**, una vez resuelto el tumor: oral, más barato, con dosificación pediátrica establecida y TDM de rutina.

**Esquema final: arimoclomol + temsirolimus + dasatinib** (tres frentes, tres fármacos). Fuera quedan bortezomib (la revisión C6 lo cuestiona) y niacina (aparte, como hipótesis especulativa).

**Se agregó la secuenciación, que faltaba.** Los tres no empiezan juntos, porque dos chocan con la quimioterapia:
- **Durante la quimio:** temsirolimus (vigilar infecciones) y arimoclomol (peso con falla de medro; creatinina y cistatina C con nefrocalcinosis).
- **Después de la quimio:** dasatinib, porque su mielosupresión se suma a la del VAC y la senescencia es un problema crónico que puede esperar.

Se actualizaron en consecuencia el Resumen y la Discusión del informe, que seguían hablando de cinco candidatos.

---

## 2026-10-21 (tarde) — Tratamiento del tumor consolidado y vigilancia oncológica

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C9-tumor-vigilancia`

**Aclaración de base:** el rabdomiosarcoma **ya está presente** en el fenotipo del paciente (HP:0002859), no es un riesgo futuro. La pregunta del equipo ("si llega el tumor") partía de una premisa equivocada; la pregunta real es con qué tratarlo.

**Respuesta consolidada (sección 8.4 de `04_candidatos.md`):** **temsirolimus**. Es el único candidato de la lista corta que actúa sobre el tumor y sobre el MVA a la vez, tiene fase II con mejor supervivencia en rabdomiosarcoma en recaída (PMID 31513481) y su mecanismo (freno en G1) no depende del checkpoint mitótico que al paciente le falta. Se agregó una tabla que separa, para cada escenario, qué es reposicionamiento y qué es estándar de cuidado.

**Hueco importante que faltaba: la vigilancia (sección 8.5).** La predisposición tumoral del MVA no termina con el rabdomiosarcoma:
- **Tumor de Wilms: riesgo ~50 %** en MVA por *BUB1B*, el más alto del espectro (TRIP13 ~20 %). SIOP-Europe recomienda **ecografía renal cada 3 meses desde el nacimiento hasta el 7.º cumpleaños** (Hol 2021, *Eur J Cancer* 153:51–63, PMID 34134020).
- MVA1 también reporta MDS, LMA y LLA, sin frecuencia estimada → hemograma periódico (Nakano 2024, *Clin Cancer Res* 30(22):5009–20, PMID 39264246).
- **Discrepancia declarada, no resuelta por nosotros:** SIOP-Europe dice hasta los 7 años; una guía británica más antigua, cada 3–4 meses hasta los 5. La decisión es del equipo tratante.
- **Observación práctica:** la ecografía renal ya está indicada por la nefrocalcinosis, así que vigilar Wilms no agrega estudios ni costo; solo fijar periodicidad y buscar masas.
- **Limitación:** no sabemos la edad actual del paciente (documento clínico anonimizado), así que no podemos decir si la ventana de vigilancia sigue abierta.

Se agregó como paso (0) de los próximos pasos de la Discusión, porque es el de mayor impacto inmediato y no requiere laboratorio.

**No se pudo verificar en texto completo.** PMC, AACR y Atlas of Genetics devolvieron 403 o CAPTCHA. Las citas (autores, revista, volumen, páginas, PMID, DOI) se confirmaron por la API de NCBI; las cifras del protocolo (~50 %, trimestral hasta los 7) provienen de lo que dos búsquedas independientes leyeron de esas fuentes y **convendría confirmarlas en el texto completo antes de la entrega**.

---

## 2026-10-21 — Reproducibilidad del pipeline (D2/D3/D6) y tratamiento del tumor

**Quién:** Ktalyna (con Claude Code) · rama `tarea/E5-reproducibilidad-tumor`

### Merges
- PR #23 (E5 borrador v2) fusionado a master. No quedan PRs abiertos.
- `tarea/E5-niacina-informe` resultó residual: cero commits y cero diferencias contra master. Se puede borrar (el borrado automático quedó bloqueado por el clasificador de seguridad; hay que hacerlo a mano).

### Reproducibilidad
**Bug encontrado y arreglado:** `scripts/modelo_dominante.py` regeneraba `config/genes_modelo_dominante.tsv` desde la API de PanelApp con `open(..., "w")`, lo que **borraba en silencio los 4 genes que C8 había agregado a mano** (ATM, KDM6A, KMT2D, LMNA) en cada corrida limpia. Ahora esos genes viven en `config/genes_dominante_extra.tsv` y el script los reinyecta al regenerar. Verificado: 96 genes = 92 de PanelApp + 4 manuales.

**Hueco cerrado:** `run_pipeline.py` no incluía los tres análisis más nuevos. Se agregaron como pasos: `dominante` (A10), `genes_equipo` (C8) y `farmacogenetica` (C7). El pipeline pasó de 5 a 8 pasos. También se hizo robusto el `insert` del paso opcional `estabilidad`, que estaba fijado a un índice numérico y con el nuevo orden habría caído en el lugar equivocado.

**Segundo bug, más grave, que la corrida completa dejó al descubierto.** El paso `farmacos` regenera `results/candidatos_farmacos.tsv`, que es el archivo que C4 puntuó **editándolo a mano**. La corrida lo dejó con las 86 filas y **cero puntajes**: se perdieron los seis criterios K1–K6, las notas de las correcciones del 14 oct y la fila de **niacina** completa (ninguna fuente la produce, se había agregado a mano), más la línea condicional de MEK. O sea: la puntuación que sostiene toda la lista corta del informe (sirolimus 71,7, temsirolimus 70,0, arimoclomol 68,3, dasatinib 60,0, bortezomib 60,0, niacina 48,3) vivía solo en un archivo generado, y **correr el comando documentado la destruía**. Se restauró desde git y se arregló: `lista_larga_farmacos.py` ahora relee el TSV versionado y devuelve las columnas curadas (`preservar_curacion()`), conservando además las filas que la regeneración no produce. Verificado: regenerar deja 89 filas, 55 puntajes y la nota de arimoclomol intactos; cero celdas cambiadas contra el estado previo.

**Corrida completa verificada (insumo para D6).** 21 oct, Windows 11, Python 3.13.14, caché construido: **8/8 pasos OK en 6 min 11 s** (diagnostico 158 s, dominante 107 s, alelo2 73 s, genes_equipo 13 s, farmacogenetica 10 s, farmacos 6 s, figuras 4 s). Reprodujo **todos** los números del informe: 24.604 variantes PASS → 14 funcionales en MANE; 11.808 → 1 candidata (*LZTR1*, CADD 49, LOEUF 2,72); 874 → 0 candidatas; 86 fármacos → 73 pasan F1/F2; CYP3A5 \*3/\*3. El log confirmó el fix de los genes manuales: "92 genes con herencia monoalélica en 8 paneles **+ 4 manuales**".

### Tratamiento del tumor (sección 8 de `04_candidatos.md`)
El equipo propuso sumar ciclofosfamida. **Se descartó como candidata, con dos motivos:** (1) no es reposicionamiento, es el estándar del rabdomiosarcoma (VAC/IVA), y presentarla como propuesta sería un error de categoría; (2) es el agente que más conviene minimizar acá, por ser alquilante en un niño con inestabilidad cromosómica.

**En su lugar se documentó algo que faltaba:** el checkpoint débil tiene consecuencias sobre la elección de la quimioterapia. La vincristina mata por una vía que **depende del SAC** (detención mitótica prolongada), y en ratones con haploinsuficiencia de BubR1 esa detención se escapa (*mitotic slippage*, Dai 2004, PMID 14744753). **La dirección del efecto no está resuelta** y se declara así: hay evidencia de más resistencia a taxol/nocodazol/vincristina con BubR1 o Mad2 bajados, y de mayor sensibilidad en otras líneas (revisión Yamada 2006, PMID 17172401). Nadie lo estudió en MVA.

**Propuesta resultante:** temsirolimus sigue como candidato de reposicionamiento con efecto tumoral (no depende del SAC, frena en G1); si hubiera recaída, el esquema **VIT** (vincristina + irinotecán + temozolomida) es el estándar del EpSSG tras VIT-0910 (PFS HR 0,64; OS HR 0,59; Defachelles 2021, PMID 34343032) y sus dos componentes añadidos dañan el ADN fuera de la mitosis. El experimento que resolvería la duda no cuesta nada extra: correr el ensayo de nocodazol ya previsto **también con vincristina**.

---

## 2026-10-15 (madrugada bis) — Corrección: nab-sirolimus y el argumento de acumulación tumoral

**Quién:** Ktalyna (con Claude Code) · rama `tarea/E5-informe`  
**Disparador:** `tbussozungri` defendió el nab-sirolimus en el grupo porque "se acumula en tumores y podríamos evitar dosis altas que tengan efecto en las otras células del cuerpo".

**Se verificó y el argumento tenía más respaldo del que le habíamos dado. Dos correcciones:**
1. La sección 7.2 de `04_candidatos.md` decía que el uso pediátrico de nab-sirolimus "no está establecido". **Incompleto:** existe ADVL1514, fase 1 del Children's Oncology Group, con MTD de 15 mg/m²/dosis IV D1+D8 en combinación con temozolomida e irinotecán (Cramer 2024, *Cancer Med* 13(21):e70376, PMID 39487711). La ficha de la FDA sí dice que no se estableció, pero hay datos publicados.
2. Decía "sin ventaja demostrada en un niño". **La acumulación tumoral está medida:** 6,2–68,1 veces más sirolimus en el tumor que con rapálogos orales en xenoinjertos, AUC tumoral semanal 43× el del sirolimus oral (Hou 2019, resumen AACR 348). Nivel de evidencia: ratón, resumen de congreso **del laboratorio desarrollador**, sin PK intratumoral en humanos.

**Por qué la recomendación igual no cambia para la línea 2:**
- La hipótesis mecanística del sirolimus acá es el eje mTORC1 → sarcopenia/crecimiento, que es **sistémico**. La acumulación tumoral no aporta a eso; el argumento aplica a la línea 4 (tumor).
- La DLT del nab-sirolimus es **trombocitopenia**, que se suma al VAC a intensidad reducida (que justamente se eligió para no castigar la médula de un paciente con inestabilidad cromosómica).
- ADVL1514 incluyó **2 rabdomiosarcomas alveolares (6,3 %) y ninguno respondió**; la única respuesta parcial fue un Ewing. Además el alveolar es con fusión, y la línea de RAS supone sin fusión.

**Resultado:** nueva sección 7.2.1 en `04_candidatos.md` con el argumento, su evidencia y sus cuatro límites. Nab-sirolimus pasa de "no aporta" a **alternativa condicional al temsirolimus en la línea del tumor**. Sirolimus oral se mantiene para la línea 2. Nota equivalente agregada en la sección 3.3 de `informe_final.md` y 3 referencias nuevas.

---

## 2026-10-15 (madrugada) — E5: integración farmacogenética en informe_final.md

**Quién:** Ktalyna (con Claude Code) · rama `tarea/E5-informe`  
**Qué se hizo:**
- `docs/informe_final.md`: agregada sección 3.4 con resultados farmacogenómicos (de 05_farmacogenetica.md); actualizado 2.4 métodos para incluir la farmacogenética
- Mergeados PR #22 (C8+A10+E5 borrador) y PR #21 (C7 farmacogenética) → master actualizado

**Estado actual de informe_final.md:** Resumen ✅, Intro ✅, Métodos (2.1–2.4 ✅, 2.5 pendiente D2/D3, 2.6 IA pendiente equipo), Resultados (3.1–3.4 ✅), Discusión ✅, Referencias ✅

---

## 2026-10-15 (noche ter) — C8 ampliado + nota ATM en A10 + borrador E5

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C8-genes-equipo`  
**Qué se hizo:**

**C8 ampliado:**
- `scripts/analisis_genes_equipo.py`: se agregaron BRCA1, BRCA2, PALB2, RAD51C, RAD51D, CHEK2 a los genes a correr
- `docs/secciones/06_genes_equipo.md`: actualizado con resultados de 10 genes (funnel 874 PASS → 0 candidatas dominantes)
- Resultado: panel oncológico hereditario **negativo** — 0 variantes funcionales ultra-raras en BRCA1/2/PALB2/RAD51C/D/CHEK2

**A10 — nota ATM:**
- `docs/secciones/01_variante_causante.md` sección 5c: agregada nota sobre ATM en la lista "Lo demás que apareció y se descartó": 1 missense HET AF=0.08%, demasiado frecuente, sin patrón bialélico; referencia a 06_genes_equipo.md

**E5 — borrador informe_final.md:**
- `docs/informe_final.md`: escritos Resumen (≈180 palabras), Discusión completa (5 párrafos), Referencias compiladas de todas las secciones
- Actualizado bullet 3.1 con resultados de C8 extendido
- **Pendientes para E5:** 2.5 reproducibilidad (espera D2/D3), 2.6 tabla IA incompleta (equipo), 05_farmacogenetica.md (PR #21)

---

## 2026-10-15 (noche bis) — Modelo dominante para lista de genes del equipo (C8)

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C8-genes-equipo`  
**Qué se hizo:**
- `scripts/analisis_genes_equipo.py`: corre el embudo del diagnóstico diferencial para LMNA, KMT2D, KDM6A, ATM; aplica filtro dominante (HET, MANE funcional, AF ≤ 1e-5, GQ ≥ 20, DP ≥ 10)
- `docs/secciones/06_genes_equipo.md`: resultados + tabla de descartes
- `config/genes_modelo_dominante.tsv`: 4 genes agregados manualmente (adición C8)

**Hallazgos:**
- **Resultado: negativo.** 305 variantes PASS → 289 raras → 1 funcional en MANE (missense ATM, AF=0.08%) → 0 ultra-raras (AF ≤ 1e-5)
- Ninguna candidata dominante en LMNA, KMT2D, KDM6A ni ATM
- ATM: 1 variante frecuente (no bialélico → no A-T)
- **EZH2 descartado:** síndrome de Weaver = overgrowth, fenotipo opuesto al paciente
- **BRCA1/2, PALB2, RAD51C/D, CHEK2:** predisposición oncológica adulta, solo serían hallazgos secundarios
- TP53 ya estaba en el modelo dominante anterior (A10)

**Pendiente:** decisión del equipo sobre si mencionar BRCA1/2 como "panel de hallazgos secundarios" en el informe

---
## 2026-10-15 (noche) — Farmacogenética (C7), evaluación del combo propuesto y lista de genes del equipo

**Quién:** Ktalyna (con Claude Code) · rama pendiente `tarea/C7-farmacogenetica`  
**Qué se hizo:**
- `scripts/farmacogenetica.py`: resuelve rsIDs de CYP2B6, CYP2C19, CYP3A4, CYP3A5, ABCB1 a coordenadas GRCh38 (Ensembl, con caché), escanea el VCF una sola vez y reporta fenotipos sin coordenadas. Genotipos crudos en `data/farmacogenetica/genotipos_farma.json` (no versionado)
- `docs/secciones/05_farmacogenetica.md`: resultados del análisis farmacogenómico
- `docs/secciones/04_candidatos.md`: sección 7 con evaluación del combo nab-sirolimus + arimoclomol + ciclofosfamida
- Verificado el paper del DOI 10.1111/ped.13849: es Nishitani-Isa 2019 (PMID 31184400), ya citado en el repo. Trata VAC a intensidad reducida, no el combo propuesto

**Hallazgos farmacogenómicos:**
- ✅ **CYP3A5 \*3/\*3** (no expresor): genotipo estándar para sirolimus; dosis inicial estándar según analogía CPIC tacrolimus; monitorear niveles (TDM) a las 2 semanas
- ⚠️ **CYP2B6 probable metabolizador intermedio** (*1/*6): porta componentes del alelo *6 (rs2279343 y rs3745274, ambos heterocigotos). Refuerza la justificación del protocolo de intensidad reducida para ciclofosfamida. Sin guía CPIC para ciclofosfamida
- ⚠️ **CYP2C19 \*1/\*2** (metabolizador intermedio): impacto clínico incierto para ciclofosfamida; sin guía CPIC
- ℹ️ **GSTM1**: no evaluable desde VCF de SNV (limitación declarada)
- ℹ️ **CYP3A4 *1B** homocigota (nivel C) y ABCB1 haplotipo heterocigoto clásico: no accionables

**Evaluación del combo (sección 7 de `04_candidatos.md`):**
- El paper **no usa nab-sirolimus ni arimoclomol**: usa VAC (vincristina + actinomicina D + ciclofosfamida) a intensidad reducida
- **Nab-sirolimus (Fyarro)**: solo aprobado para adultos con PEComa; sin uso pediátrico establecido; no supera a sirolimus oral para este paciente. Se descarta como alternativa a sirolimus
- **Ciclofosfamida**: no es reposicionamiento; es el tratamiento estándar del rabdomiosarcoma (VAC/IVA)
- **Recomendación:** el combo de reposicionamiento sigue siendo sirolimus + arimoclomol; ciclofosfamida es el contexto oncológico estándar (VAC intensidad reducida)

**Lista de genes del equipo (WhatsApp, 15 oct):**
- Grupos: cáncer hereditario, laminopatías, epigenética, microcefalia/centrosoma, checkpoint mitótico, poro nuclear, ciclo celular
- Ver pendiente en tablero (tarea nueva C8/A11 según corresponda)

**Pendiente:**
- [ ] Rama y PR para `scripts/farmacogenetica.py` + `05_farmacogenetica.md`
- [ ] Verificar la orientación de hebra del alelo CYP3A4 *1B/*1B antes de reportar en el informe clínico
- [ ] Decisión del equipo sobre qué genes de la lista nueva vale la pena correr con `modelo_dominante.py`
- [ ] Decidir si se incluye el análisis de farmacogenética en el informe final (sección nueva)

---

## 2026-10-15 — Embudo real en el notebook 04, modelo dominante (A10) y línea condicional de MEK

**Quién:** Ktalyna (con Claude Code) · rama `tarea/A10-modelo-dominante`
**Qué se hizo:**
- **Notebook 04 rehecho.** Dibujaba un embudo de 19.099 variantes, pero el código miraba 6 genes y consultaba gnomAD solo para *BUB1B*. Además descartaba las homocigotas, usaba el primer transcrito de SnpEff en vez de MANE y deducía la fase *trans* a partir de dos heterocigotas. Ahora aplica el embudo validado de A8 a los 321 genes y muestra cuántas variantes quedan en cada paso (figura `results/figura_embudo_variantes.png`)
- **Modelo dominante** (`scripts/modelo_dominante.py`): 92 genes de 8 paneles de PanelApp en los que una sola copia alterada causa enfermedad, con AF ≤ 1×10⁻⁵, más un control recesivo de 48 genes renales (`--rinon-recesivo`)
- Trametinib y selumetinib agregados al TSV como candidatos condicionales (65 pts); sección 6 de `04_candidatos.md`, sección 5c de `01_variante_causante.md` e informe actualizados

**Hallazgos:**
- ✅ **Embudo:** 5.012.204 variantes → 4.740.790 PASS → 24.604 en los 321 genes → 19 raras con efecto en alguna proteína → 14 en MANE, **ninguna homocigota** → 1 gen con patrón recesivo: *BUB1B*
- 💡 **Hallazgo secundario:** una truncante heterocigota en *LZTR1* (AF 1,4×10⁻⁶, germinal, ClinVar P/LP). No explica el MVA ni la nefrocalcinosis y no causa Noonan (el gen tolera perder una copia y no hay segunda variante). Sí es la causa conocida de la **schwannomatosis por *LZTR1*** (dominante, penetrancia incompleta; PMID 24362817), con vigilancia recomendada en niños (PMID 39937237)
- 💡 **Hipótesis innovadora:** si el rabdomiosarcoma perdió la otra copia de *LZTR1*, la vía RAS estaría activa. Eso abriría el uso de un inhibidor de MEK (trametinib o selumetinib, FDA desde 1 año) junto con temsirolimus (PMID 23684925, 36322002), nunca solo (PMID 35363510). Se comprueba en la biopsia. Hay un solo trabajo que une *LZTR1* con el rabdomiosarcoma
- ✅ **Nefrocalcinosis:** ningún gen renal la explica (92 dominantes y 48 recesivos). Lo más probable es la prematuridad (hasta 40 % de los prematuros; PMID 38296790)
- ⚠️ La missense de *MAD1L1* que figuraba como patogénica en la tabla subida al repo es benigna en las evaluaciones germinales recientes (el registro patogénico es de 2001, somático y sin criterios)
- ⚠️ **Privacidad:** la tabla `notebooks/candidatos_genomicos_mva_priorizados.csv` (358 variantes del paciente) se movió a `data/equipo/` (PR #19). Sigue en el historial de git: hay que limpiarlo antes de hacer público el repo

**Pendiente:**
- [ ] Decidir si el hallazgo de *LZTR1* se informa como hallazgo secundario en el Track 1 (la posición exacta iría solo al envío, no al repo)
- [ ] Limpiar el historial de git antes de hacer público el repo
- [ ] Revisión 🧬 de la sección 5c y 💊 de la sección 6 de `04_candidatos.md`

---

## 2026-10-14 (noche) — Niacina en el informe y segunda corrección de puntajes

**Quién:** Ktalyna (con Claude Code) · rama `tarea/E5-niacina-informe`
**Qué se hizo:**
- `docs/informe_final.md`: se completaron la sección 2.4 (cómo se priorizaron los fármacos), la 3.3 (tabla de candidatos) y la discusión. Niacina entra como **hipótesis innovadora, marcada como especulativa**, con sus 5 límites
- Ficha 2.6 de niacina en `docs/secciones/04_candidatos.md`; PDF de revisión actualizado

**Hallazgos:**
- ⚠️ **Arimoclomol: la ficha de la FDA dice que su mecanismo en Niemann-Pick C "es desconocido"** y que solo se aprobó junto con miglustat, desde los 2 años. Baja de peso es efecto frecuente (≥ 15 %) y el paciente tiene falla de medro; sube la creatinina 10–20 % sin afectar el filtrado (inhibe OCT2); ratas jóvenes tuvieron dilatación de la pelvis renal. K4 2 → 1: **73,3 → 68,3**. Sirolimus (71,7) vuelve al primer lugar
- ⚠️ Niacina: el rescate de 2014 (North) **no tuvo réplica independiente**; el mismo grupo mostró en 2023 que SIRT2 extra no alarga la vida de ratones normales (PMID 38009412), y en 2014 otro grupo vio que SIRT2 desacetila BubR1 en K250 sin cambiar su cantidad total (PMID 25285631). La ficha de la FDA de niacina: seguridad pediátrica no establecida
- ✅ PubMed (14 oct): 0 trabajos unen NAD⁺, SIRT2, NMN o niacina con el MVA, y ninguno une arimoclomol o HSP70 con BUBR1
- Error mío anterior corregido: escribí que niacina era "el único fármaco aprobado con datos *in vivo* de que sube BubR1". Los datos son de NMN (no aprobado); la niacina misma no se probó

**Pendiente:**
- [ ] Reunión 15 oct: ¿bortezomib sale de la lista corta?
- [ ] Revisión 🧬 de la sección 3.3 del informe

---

## 2026-10-14 (tarde) — Revisión biológica de la lista corta (C6) y corrección de sirolimus

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C6-revision-biologica`
**Qué se hizo:**
- Se verificó en PubMed la evidencia de cada candidato de la lista corta
- Sección 5 nueva en `docs/secciones/04_candidatos.md`: ¿cada fármaco empeora la mitosis?
- Niacina agregada a `results/candidatos_farmacos.tsv` como candidato de línea 1 (53 candidatos); PDF de revisión actualizado

**Hallazgos:**
- ⚠️ **Corrección:** Sieben 2020 (PMID 31738183) **no trató ratones BubR1 con rapamicina**; solo asocia la sarcopenia con mTORC1 hiperactivo. La rapamicina frena la sarcopenia en ratones salvajes (Ham 2020, PMID 32908143). Sirolimus: K1 3 → 2, 80 → 71,7 pts. **Arimoclomol pasa al primer lugar**
- ✅ Ningún candidato debilita el checkpoint mitótico. **Bortezomib** sí agrega estrés mitótico: al frenar el proteasoma retrasa la degradación de ciclina B y securina, que permite salir de la mitosis; además suma neuropatía a la vincristina
- 💡 **Niacina (vitamina B3, FDA):** NMN, otro precursor de NAD⁺, sube BubR1 en ratones vía SIRT2, y SIRT2 alarga la vida de ratones BubR1<sup>H/H</sup> (North 2014, PMID 24825348). Es el único fármaco aprobado con datos *in vivo* de que aumenta BubR1. Con la matriz puntúa 48,3 (sin datos clínicos, riesgo con el tumor activo)

**Pendiente:**
- [ ] Decidir en la reunión del 15 oct: ¿bortezomib o niacina como segundo candidato de línea 1?
- [ ] Revisión 🧬 de la sección 5

---

## 2026-10-14 — A6 cerrada: 31 genes de la lista original que faltaban

**Quién:** Laura (con Claude Code)
**Qué se hizo:**
- Se encontró la lista original de 201 genes: es `results/genes_candidatos_grch38.tsv`, salida de `resolve_genes.py` del 30 sep en la PC de Laura. No llegó al repo porque `results/*.tsv` está en `.gitignore`, y `resolve_genes.py` la sobrescribe en cada corrida. Ahora está versionada en `config/lista_original_laura_201.tsv`
- Se comparó con `config/genes_candidatos.txt` por nombre original y por símbolo oficial
- Los genes que faltaban se agregaron al panel en un bloque "A6" (panel: 290 → **321** símbolos)
- Diagnóstico diferencial solo sobre esos genes, con el script de A8 sin modificar (`notebooks/03b_a6_genes_faltantes_lista_laura.ipynb`, Colab con runtime local; resultados en `data/a6/`, no versionados)

**Hallazgos:**
- ⚠️ Faltaban **31 genes, no ~11**: la cuenta de 197 − 186 suponía que los 186 del repo eran un subconjunto de la lista de Laura, y no lo eran (el repo tenía genes que ella no tenía y viceversa)
- ⚠️ Entre los que faltaban había **tres de los seis genes de MVA con número en OMIM**: ***CENATAC*** (MVA4), ***SLF2*** (MVA5) y ***SMC5*** (MVA6)
- ✅ **Ninguno de los 31 explica el MVA**: 30 analizados (*IL40* no está en gnomAD v4), 0 con patrón recesivo, 0 pérdidas de función. *CENATAC*, *SMC5* y *SLF2*: 0 variantes raras funcionales. Única alerta: una missense heterocigota en *MINAR1*, frecuente (AF 0,49 %, 23 homocigotos en gnomAD)
- 10 de los 31 son ARN no codificantes o pseudogenes, que el método no puede evaluar (anotado como limitación en la sección 5 de `01_variante_causante.md`)

**Revisión (Ktalyna con Claude Code, 14 oct):**
- Corregida la numeración de MVA: MVA3 es *TRIP13* (OMIM 617598) y *CENATAC* es MVA4 (OMIM 620153). El error venía de una nota de revisión equivocada del 5 oct en `scripts/unir_grupos_genes.py` y `config/genes_candidatos_anotados.csv`, que decía que el MVA 3 era CENATAC; corregida en ambos
- Se borró la salida de la celda que mostraba la posición de la variante de *MINAR1*: el repo será público y la convención es no publicar genotipos del paciente fuera de *BUB1B*
- El marcador del Track 1 confirma la hipótesis: los 24 primeros tienen 100 puntos de rango y F-max 1,000, casi todos con el par de *BUB1B*

---

## 2026-10-09 — Envío al Track 1 preparado (A7)

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- `envios/track1/Ktalyna_bub1b-mane-panel.csv` (una fila: el par de *BUB1B*, EPCR 0,85) y `envios/track1/Ktalyna_track1_report.md` (informe en inglés para el jurado)
- Se leyó el código público del Space (`tabs/submit_track1.py`, `evaluation.py`) y el CSV se validó con su propio lector
- Fila de Ktalyna completada en la tabla de uso de IA (sección 2.6 de `informe_final.md`)

**Hallazgos:**
- ⚠️ El sitio **solo acepta `proband_id = PROBAND01`**. La fila preparada el 2 oct usaba el nombre de la muestra del VCF y habría dado error (los errores no gastan cupo, pero conviene no probar a ciegas)
- Cada integrante tiene su propio cupo de 6 envíos; para que se agrupen en el marcador, todos deben usar exactamente el mismo nombre de equipo

**Pendiente:**
- [ ] Iniciar sesión en HF en el sitio y enviar
- [ ] Decidir nombre de equipo (se envía con el usuario si no hay uno)

---

## 2026-10-09 — Conciliación de la lista de genes (A6, parcial)

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- Se abrió el Colab de Laura: **no contiene la lista de 201 genes**; lee la copia de `config/genes_candidatos.txt` que tiene en su PC
- Se revisó el historial de git, las ramas y el PR #5: ninguna versión del repo tuvo nunca los 201. La primera (1 oct) ya tenía 186 únicos
- Los 4 símbolos sin coordenadas se buscaron en HGNC como símbolo, alias, símbolo previo y con comodín
- Se quitó el duplicado de *CENPJ* (estaba en cinetocoro y en centrosoma; se deja en centrosoma)

**Hallazgos:**
- ✅ MOXN1, RASRL1 y UPP2-AS1 **no existen** en HGNC (UPP2-IT1 es una entrada retirada). TLX1-AS no existe; lo más cercano es *TLX1NB*, un ARN no codificante que el pipeline no evalúa. Ninguno puede esconder una variante causal
- ⚠️ La corrida de Laura tuvo 197 genes con coordenadas (195 con variantes); el repo tiene 186 antes del bloque de los grupos. **Faltan ~11 genes** que solo están en su copia local. Algunos pueden haber entrado después con los CSV de los grupos (el panel actual tiene 290)

**Pendiente:**
- [ ] Laura comparte su `config/genes_candidatos.txt` local; se comparan y, si aparecen genes nuevos, se corre el diagnóstico diferencial solo sobre ellos

---

## 2026-10-09 — Formulario de métodos bajado y mapeado (E3)

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- El formulario **no estaba en el dataset de Hugging Face** (confirmado el 2 oct); estaba en el repo del **Space** del reto (`SageBio/rare-disease-real-kid-mva-hackathon-2026`, pestaña "Submit - Track 2" → "Methods description template (Excel)"), en `static/templates/methods_description_form.xlsx`
- Copiado a `docs/plantillas/methods_description_form.xlsx` (es un formulario público del reto, sin datos del paciente)
- `docs/mapa_formulario.md`: cada pregunta de las 2 hojas (Track 1 y Track 2) enlazada a dónde está la respuesta en el repo y qué tarea la generó

**Hallazgos:**
- De las 11 preguntas de Track 2, 9 ya tienen respuesta lista en algún documento del repo
- 2 quedan abiertas: "Team name" y la fila de IA generativa dependen de E1 (quién envía); "tiempo/esfuerzo dedicado" nadie lo registró, el equipo lo tiene que estimar a mano

**Pendiente:**
- [ ] E1: designar quién envía, para poder cerrar las preguntas que dependen de eso
- [ ] Llenar el `.xlsx` en sí queda para E7 (24 oct)

---

## 2026-10-08 (noche, 4) — Lista corta de fármacos, Hito H4 (C5)

**Quién:** Ktalyna (con Claude Code) · borrador, pendiente de revisión 💊🧬
**Qué se hizo:**
- `docs/secciones/04_candidatos.md`: 5 candidatos elegidos del ranking de C4, sin repetir mecanismo, cubriendo las 4 líneas de `02b_resumen_mecanismo.md` (la regla pedía al menos 2)
- Cada uno con ficha: mecanismo, evidencia, seguridad pediátrica, riesgos de compatibilidad y cómo se validaría

**Elegidos:** sirolimus (línea 2, 80 pts — único con dato experimental en modelo de ratón BubR1 *[corregido 14 oct: no hay tal dato; 71,7 pts]*), arimoclomol (línea 1, 73,3 — chaperona), temsirolimus (líneas 2+4, 70 — único con ensayo clínico propio en rabdomiosarcoma), dasatinib (línea 3, 60 — senolítico), bortezomib (línea 1, 60 — proteasoma, prueba el mecanismo del paper base con MG132)

**Hallazgos:**
- Dos riesgos de compatibilidad a resolver antes del informe final: bortezomib + vincristina comparten neurotoxicidad (ambas en el protocolo estándar); el beneficio de temsirolimus depende del grupo de riesgo del rabdomiosarcoma (sin beneficio en riesgo intermedio, PMID 38936378)
- El ensayo de validación es el mismo para 4 de los 5 candidatos: fibroblastos del paciente, nivel de BUBR1 (Western blot) y checkpoint con nocodazol, antes/después del fármaco

**Pendiente:**
- [ ] Revisión 💊🧬 de la lista (sección 4 de `04_candidatos.md` tiene las decisiones abiertas)
- [ ] E5: integrar esta sección al borrador completo del informe (21 oct)

---

## 2026-10-08 (noche, 3) — Conclusión del análisis de variantes no-PASS (A9)

**Quién:** Ktalyna (con Claude Code) · borrador, pendiente de confirmación de Josefina
**Qué se hizo:**
- Se redactó la conclusión del notebook `02b_sensibilidad_nonpass_genes_mva.ipynb` (subido por Josefina el 7 oct), analizando las 6 variantes NO-PASS por `QUAL`, `QD`, `MQ`, profundidad y soporte de lecturas
- Se agregó el resumen a la sección 5 de `docs/secciones/01_variante_causante.md`

**Hallazgos:**
- Las 2 variantes de *MAD1L1* descartadas solo por `MQ40` (mapeo ambiguo) tienen QUAL y soporte de lecturas altos y rsID en dbSNP: parecen reales, solo mal etiquetadas por el filtro técnico
- Las otras 4 (3 en *MAD1L1*, 1 en *BUB1B*) fallan por `QD2`/`LowQual` con poco soporte de lecturas alternativas: compatibles con artefactos de baja profundidad
- La variante NO-PASS de *BUB1B* (15:40180642) es la de menor calidad del lote (QUAL 19,78, DP 13): no hay motivo para tratarla como un tercer evento genético
- Ninguna cambia el diagnóstico: *MAD1L1* no tiene patrón recesivo entre sus variantes PASS

**Pendiente:**
- [ ] Josefina confirma la conclusión y la firma en el notebook (cierra A9)

---

## 2026-10-08 (noche, 2) — Puntuación de la lista larga de fármacos (C4)

**Quién:** Ktalyna (con Claude Code) · sin rama (edición directa de `results/candidatos_farmacos.tsv`, borrador)
**Qué se hizo:**
- Se puntuaron los 52 candidatos de `results/candidatos_farmacos.tsv` con la matriz de C1 (K1–K6, `puntaje` = Σ peso×nota/3)
- Para línea 4 (tumor), `k3` se mapeó directo desde `fase_rms` de Open Targets (fase 3 → 3, fase 2 → 2, fase 1 → 1) y se marcaron bajo en `k1` los antimitóticos (PRECAUCIÓN): mismo tipo de estrés que ya debilita el SAC del paciente
- `quien_puntua` = "Claude (borrador IA)": falta la revisión 💊 de los 10 primeros que pide la regla de C1 (sección 1.5)

**Hallazgos:**
- Top 4, todos con datos mecanísticos directos (no solo razonamiento): **sirolimus (80)** — único con datos experimentales en el ratón BubR1 hipomórfico (Sieben 2020/PMID 31738183) *[corregido 14 oct: Sieben 2020 no trató con rapamicina, solo asocia sarcopenia y mTORC1; 71,7 pts]* —, **arimoclomol (73,3)**, **temsirolimus (70)** — único con ensayo clínico propio en rabdomiosarcoma — y **everolimus (68,3)**
- El top 10 ya cubre 3 de las 4 líneas (1, 2 y 3: dasatinib 60, bortezomib 60), condición que pide C5 para la lista corta
- ⚠️ Pendiente de decisión (sigue abierta desde C1 sec. 6): la edad exacta del paciente para `k2`; se asumió "niño pequeño" por el fenotipo (prematuro, RCIU severo, talla baja) sin abrir el documento clínico
- ⚠️ Candidatos con alerta renal fuerte por la nefrocalcinosis del paciente (k4 bajo): cisplatino, metotrexato, pemetrexed, nitrato de galio, carfilzomib, varios TKI multiquinasa (cabozantinib, lenvatinib, regorafenib, sorafenib)

**Pendiente:**
- [ ] Revisión 💊 de los 10 primeros puntajes (dos personas, discutir si difieren >1 punto en un criterio)
- [ ] C5: armar la lista corta (3–5, ≥2 líneas) con ficha de cada uno — Hito H4, 17 oct

---

## 2026-10-08 (noche) — Diagnóstico diferencial con MANE (A8) y pipeline de un comando (D2, D3, D5)

**Quién:** Ktalyna (con Claude Code) · ramas `tarea/A8-mane` y `tarea/D2-D3-D5-pipeline`
**Qué se hizo:**
- `scripts/diagnostico_diferencial.py` vuelve a anotar con VEP, en el transcrito **MANE Select**, cada variante rara que parece funcional. Esa consecuencia es la que decide
- Barrido completo de los 290 genes (panel original + grupos del equipo) con el VCF local
- Se quitó EB1 del panel: el buscador de alias lo resolvía como *ANKS1B*; EB1 es *MAPRE1*, que ya estaba
- `run_pipeline.py` corre todo el análisis con un comando; `requirements-lock.txt` fija las versiones; el README explica cómo usarlo con otro paciente (PR #12)

**Hallazgos:**
- 18 alertas en algún transcrito → **13 en MANE**. Se reproducen las 3 falsas alarmas que Laura encontró a mano (ARID1B, SMARCA4, SYNE2) y aparecen 2 más en el panel original (ANAPC2 y el sitio de empalme de SMC1B)
- ✅ *BUB1B* sigue siendo el único gen con patrón recesivo; sus dos variantes mantienen el efecto en MANE

**Pendiente:**
- [ ] D3: clonación limpia en otra máquina

---

## 2026-10-08 (noche) — Figuras 1 y 2 del informe (A5, B5)

**Quién:** Ktalyna (con Claude Code) · rama `tarea/A5-B5-figuras`
**Qué se hizo:**
- `scripts/figuras_informe.py` genera las dos figuras con la guía de estilo del informe (paleta Okabe-Ito validada para daltonismo; alelo 1 bermellón, alelo 2 azul, fármacos verde)
- **Figura 1** (`results/figura_1_bubr1_variantes.png`): BUBR1 con dominios, las 2 variantes del paciente y las 12 variantes de MVA de Suijkerbuijk 2010, agrupadas por efecto sobre la cantidad de proteína
- **Figura 2** (`results/figura_2_via_mecanismo.png`): la vía del genotipo al fenotipo, con el punto de acción de cada línea terapéutica y las dos advertencias (HSP90, antimitóticos)
- Ambas enlazadas en `docs/informe_final.md` con su pie de figura

**Pendiente:**
- [ ] Revisión 🧬 de la figura 2 (Hito H3, 14 oct)

---

## 2026-10-08 (tarde) — Lista larga de fármacos (C3)

**Quién:** Ktalyna (con Claude Code) · rama `tarea/C3-lista-larga`
**Qué se hizo:**
- Se fusionaron los PR #6 a #9 y se borraron las ramas ya fusionadas
- `scripts/lista_larga_farmacos.py` une DGIdb v5, Open Targets y una lista curada por línea terapéutica, comprueba la aprobación en Drugs@FDA y en la EMA y aplica los filtros F1 y F2 de C1
- Resultado en `results/candidatos_farmacos.tsv` (con excepción en `.gitignore`: no contiene datos del paciente) y resumen en `docs/secciones/03b_lista_larga.md`

**Hallazgos:**
- 86 fármacos: **52 candidatos** (líneas 1–3: 14; tumor: 38), 21 de contexto y 13 excluidos
- ✅ Ninguno de los 162 inhibidores de HSP90, PLK1, Aurora, MPS1, APC/C, BUB1 o CDK1 está aprobado: las dianas que empeorarían el checkpoint no tienen fármacos aprobados
- ⚠️ Open Targets ya no tiene el campo `knownDrugs` (ahora `drugAndClinicalCandidates`) y no liga los rapalógos a MTOR; se curaron a mano
- ⚠️ openFDA no trae `generic_name` en muchos registros; se busca también por principio activo

**Pendiente:**
- [ ] C4: puntuar los 52 candidatos con la matriz (perfil 💊). Avisos en la sección 3 de `03b_lista_larga.md`

---

## 2026-10-08 — Cierre de B1, H2 en revisión, matriz de fármacos y borrador del informe

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- Se fusionó el PR #5 de Laura (104 genes nuevos)
- **B1** (PR #6): Suijkerbuijk 2010 y Sieben 2020 leídos en texto completo; guías ACMG verificadas en PubMed
- **B4 / Hito H2** (PR #6): `docs/secciones/02b_resumen_mecanismo.md`, una página para el área C
- **C1** (PR #7): `docs/secciones/03_criterios.md`, matriz con filtros de exclusión y 6 criterios ponderados
- **E2 y E4** (PR #8): `docs/informe_final.md` con el borrador de variante y mecanismo ya integrado, guía de estilo, tabla de uso de IA y `docs/guion_pitch.md`
- Tablero actualizado: estados de A2, A3, B2, B3 y D1; tareas nuevas A8 (barrido con MANE) y A9 (conclusión del notebook 02b); estado 👀 para tareas en revisión

**Hallazgos:**
- ✅ **En el MVA bialélico falta proteína, no función.** Todos los missense del dominio quinasa estudiados bajan BUBR1 de 5 a 10 veces por mal plegamiento, y llevarlos a niveles normales restaura el checkpoint (Suijkerbuijk 2010). p.Asn1002Lys está en ese dominio
- ✅ **Caso publicado casi idéntico al nuestro:** truncamiento en el codón 753 (c.2211insGTTA, el nucleótido contiguo a nuestro c.2210) + p.Leu1012Pro. Ese paciente murió a los 3,6 meses
- ✅ La pérdida total de BUBR1 es letal en el embrión de ratón (Wang 2004): ya no es una hipótesis sin fuente
- ⚠️ **HSP90 deja de ser diana:** inhibirla baja aún más la BUBR1 mutante. Estaba propuesta en el notebook 05 y en el cuaderno 06
- ⚠️ El formulario de métodos no está en el dataset de Hugging Face: E3 queda bloqueada

**Decisiones:**
- Las tareas en PR abierto pasan a 👀 y no cuentan para el máximo de 2 en curso
- La lista corta de fármacos debe cubrir al menos dos líneas terapéuticas distintas

**Pendiente:**
- [ ] Revisión 🧬 del PR #6 y revisión 💊 de los PR #6 y #7
- [ ] Bajar `methods_description_form.xlsx` del sitio del reto (E3)
- [ ] Decidir el idioma del informe y del video
- [ ] Cada persona completa su fila en la tabla de uso de IA (sección 2.6 del informe)
- [ ] Asignar responsables del área C (C2 a C6) y de E1 y A7, que están vencidas

---

## 2026-10-07 — Análisis de sensibilidad de variantes no-PASS

**Quién:** Josefina · subido directo a `master`
**Qué se hizo:**
- `notebooks/02b_sensibilidad_nonpass_genes_mva.ipynb`: revisa las variantes que el filtro de calidad descartó en los 6 genes principales

**Hallazgos:**
- 6 variantes no-PASS: 5 en *MAD1L1* y 1 en *BUB1B* (deleción de 1 pb, QUAL 19,8). Todas con baja calidad de mapeo o de lectura (filtros QD2, MQ40, LowQual)

**Pendiente:**
- [ ] Josefina: escribir la conclusión en el notebook (tarea A9)

---

## 2026-10-06 — Diagnóstico diferencial de los 104 genes nuevos

**Quién:** Laura (con Claude Code) · rama `tarea/A3-genes-nuevos`
**Qué se hizo:**
- Se corrió `python scripts/diagnostico_diferencial.py --solo-nuevos` con el VCF local (Colab conectado a un entorno local). Los 104 genes se resolvieron en gnomAD y no quedaron variantes sin anotar
- Se volvieron a anotar las 7 variantes raras funcionales con Ensembl VEP en el transcrito MANE Select
- Resumen en la sección 5b de `docs/secciones/01_variante_causante.md`

**Hallazgos:**
- ✅ Ningún gen nuevo explica el MVA: *BUB1B* sigue siendo el único con dos variantes dañinas
- ⚠️ *SYNE2* salió con patrón recesivo, pero es una falsa alarma: una de sus 2 variantes es intrónica en MANE
- ⚠️ 3 de las 7 alertas (*ARID1B* stop, *SMARCA4* missense, *SYNE2* stop_lost) solo eran graves en transcritos secundarios. El script usa la consecuencia más severa en cualquier transcrito

**Pendiente:**
- [ ] Usar la consecuencia en MANE dentro de `scripts/diagnostico_diferencial.py` y repetir el barrido de los 187 genes
- [ ] Análisis de sensibilidad de variantes no-PASS (sigue sin hacerse)

---

## 2026-10-06 — Cuaderno 06 de fármacos (adelanto de una compañera que se retira)

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- Una compañera que dejó el equipo subió `notebooks/06_agente_reposicionamiento_farmacos.ipynb` (agente LangChain + Gemini) con una lista inicial de fármacos para 6 blancos. Ya está en `master`
- Se revisó el cuaderno y se anotó el estado en el Área C de `docs/plan_equipo_tareas.md`

**Hallazgos (revisión del cuaderno):**
- ⚠️ La lista **no es validable tal como está**: varios fármacos no están aprobados por FDA/EMA, y bajo Hsp90 y p53 hay fármacos que no actúan sobre esos blancos
- La extracción de DGIdb falló en la ejecución guardada (API v2) y el filtro FDA/EMA es solo una instrucción del prompt
- Quedan sin responsable las tareas C1 a C6; la lista corta (H4) vence el **17 de octubre**

**Pendiente:**
- [ ] Paso de verificación: rehacer C3 con DGIdb v5 y Open Targets, comprobar la aprobación FDA/EMA contra una fuente y puntuar con la matriz de C1
- [ ] Asignar responsable del Área C
- [ ] Preguntarle por privado qué celda produjo la lista del mensaje y si DGIdb funcionó alguna vez

---

## 2026-10-05 — Genes de los grupos del equipo: CSV corregidos y lista ampliada

**Quién:** Ktalyna (con Claude Code)
**Qué se hizo:**
- Los 8 CSV del equipo (166 genes) se guardaron sin tocar en `config/grupos_genes/originales/` y se unificaron con `scripts/unir_grupos_genes.py` en `config/genes_candidatos_anotados.csv`
- `config/genes_candidatos.txt` pasa de 188 a 292 símbolos (104 nuevos, en un bloque entre marcas AUTO; el script se puede volver a correr)
- `scripts/diagnostico_diferencial.py` acepta `--solo-nuevos` para analizar solo esos genes
- Se fusionó `tarea/B3-bolsillo-atp` (p.Asn1002Lys no toca el bolsillo de ATP)

**Hallazgos:**
- ⚠️ Las columnas `hgnc_id`, `ensembl_id` y `ncbi_gene_id` están corruptas en 7 de 8 archivos (p. ej. `ENSG00000162571` en 72 de 95 filas) y se descartaron. En el archivo de reparación de ADN faltan 2 columnas. Las coordenadas salen de `scripts/resolve_genes.py` por símbolo
- Errores de contenido marcados en `nota_revision` (el texto original no se modificó): PCNT/Taybi-Linder, NIN/pseudoacondroplasia, SAS6 ("cartílago") y símbolos desactualizados (CCDC155, H3F3A/B, H2AFZ, MRE11A, NTF2, NUP53, NUP96). *Corrección 14 oct: también se había marcado TRIP13 "MVA 3" como error, pero era correcto (OMIM 617598).*
- HGS, ARRB1 y ARRB2 no son del ciclo celular: baja prioridad

**Pendiente:**
- [ ] Probar los 104 genes nuevos igual que BUB1B: `python scripts/diagnostico_diferencial.py --solo-nuevos` (necesita el VCF en `data/raw/` y red; escribe `results/diagnostico_diferencial_nuevos_*.tsv` sin pisar el análisis del panel). Esta sesión no tenía ni VCF ni red
- [ ] Verificar en OMIM las filas con nota "verificar" antes de citarlas
- [ ] Repetir con red el cálculo del bolsillo de ATP (AlphaFold/AlphaFill estaban bloqueados); el resultado vigente es el de la rama B3
- [ ] Análisis de sensibilidad de variantes no-PASS (todo el pipeline descarta lo que no sea PASS)

---

## 2026-10-02 — Tareas A2 y B2: clasificación ACMG y NMD (corrige la lectura del H1)

**Quién:** Ktalyna (con Claude Code) · rama `tarea/A2-B2-variante-acmg-nmd`  
**Qué se hizo:**
- `docs/secciones/01_variante_causante.md`: tabla ACMG con puntajes, calidad de llamadas, NMD, limitaciones y qué lo confirmaría
- NMD de p.Leu737Ter: PTC en c.2210 (exón 17/23), última unión exón-exón a 747 nt → NMD predicho (sin datos de ARN)
- Calidad de lectura (A4): fracción alt 0,54 y 0,46, GQ 99, sin señal de mosaicismo; sin etiquetas de fase en el VCF

**Evidencia adicional del alelo 2 (B3, parte de B1):** `scripts/evidencia_alelo2.py` → `results/evidencia_alelo2.json`
- ClinVar (2501 registros): p.Asn1002Lys ya figura como VUS (c.3006T>A); sin cambios patogénicos de aminoácido cerca → sin PM1/PM5
- AlphaFold: pLDDT 91, la Asn forma 3 enlaces de hidrógeno que la lisina perdería; residuo conservado en 7/7 vertebrados
- Sin artículos con este cambio; sigue siendo VUS, inclinada a patogénica

**¿p.Asn1002Lys toca el bolsillo de ATP? (2 oct)** → fila nueva en la tabla de hipótesis de `01_variante_causante.md`, `scripts/evidencia_alelo2.py`
- No: a 28,6–29,8 Å del nucleótido (4 posiciones colocadas por homología con AlphaFill), sin contacto con ninguno de los 30 residuos del bolsillo
- Un efecto directo sobre la unión de ATP es muy improbable; uno indirecto por menor estabilidad global no se descarta

**Cálculo de estabilidad de p.Asn1002Lys con ThermoMPNN (2 oct)** → `scripts/estabilidad_alelo2.py`, `results/estabilidad_alelo2.json`
- ΔΔG de N1002K = +1,5 kcal/mol (desestabiliza de forma moderada); la variante conocida de MVA1 p.Leu1012Pro da +3,1
- Todas las sustituciones en 1002 desestabilizan; resultado igual con la proteína completa y con el dominio (Spearman 0,95)
- Controles superados (numeración, identidad, signo). Encaja con un alelo hipomórfico; la degradación rápida no queda demostrada
- No cambia la clasificación ACMG (la herramienta no está calibrada para PP3)

**Hipótesis del equipo sobre p.Asn1002Lys puestas a prueba (2 oct)** → sección "Hipótesis del equipo" de `01_variante_causante.md`
- Glicosilación: descartada (N-A-N-D no es el motivo N-X-S/T)
- N1002 mayormente enterrado, en el extremo de una hélice, con 3 enlaces H que la lisina perdería; a 29 Å del bolsillo de ATP
- Hallazgo: UniProt anota la variante MVA1 p.Leu1012Pro como heterocigota compuesta con una mutación sin sentido (mismo tipo de genotipo del paciente), a 12 Å de N1002 y totalmente enterrada
- Estabilidad/degradación: plausible, falta calcular ΔΔG

**Revisión exhaustiva del dataset y del sitio del reto en Hugging Face (2 oct)**
- El dataset tiene una sola rama, sin versiones ocultas ni PR; son 13 archivos y todos son del paciente (VCF, FASTQ, documento clínico). No hay datos de los padres, y la organización no tiene otros datasets públicos
- La fase de las dos variantes no se puede resolver con lo disponible (variante intermedia a 6,8 y 4,1 kb)
- Requisitos de entrega del Track 2 leídos del sitio oficial: un solo envío por equipo, repo público al terminar, video en YouTube o Vimeo, y declaración de IA con proveedor, plan y configuración de datos. Añadidos al tablero
- El Track 1 del sitio puntúa la pareja de variantes al instante contra la respuesta validada: añadida la tarea A7

**Tarea A3: diagnóstico diferencial** → sección 5 de `docs/secciones/01_variante_causante.md`, `scripts/diagnostico_diferencial.py`
- 187 genes del panel (se añadió MAD2L1BP, MVA descrito en 2023): solo 11 variantes raras funcionales, todas heterocigotas. BUB1B es el único gen con LOF + otra variante rara funcional
- CEP57, TRIP13, MAD2L1BP, BUB1, BUB3, MAD2L1, CDC20 y ESPL1: sin variantes raras funcionales
- No evaluado: variantes estructurales/CNV y no codificantes (un caso publicado de MVA tuvo una variante reguladora de BUB1B)
- Error corregido en el proceso: la primera versión marcó 31 variantes comunes como "ausentes de gnomAD" (la lista por gen de gnomAD omite algunas); ahora se consulta cada variante funcional directamente

**Tarea B1 (borrador): marco biológico** → `docs/secciones/02_marco_biologico.md`
- Coordenadas de dominios verificadas (UniProt y Zhang 2026): GLEBS 408–418, KARD 669–674, pseudoquinasa 766–1050; la tabla del notebook 05 estaba mal y la figura 02a se regeneró
- Tabla de literatura reemplazada por 18 citas verificadas en PubMed. Se eliminaron 5 que no existían o no decían lo afirmado (Malureanu 2009, Elowe 2012, Rivero 2016, Simonetti 2019, Holland y Cleveland 2012)
- Hallazgo: Sieben 2020 modela en ratón la variante de MVA BUBR1 p.Leu1012Pro, a 10 residuos de p.Asn1002 (contexto, no evidencia ACMG); la sarcopenia se asocia a mTORC1, que conecta con la atrofia muscular del paciente

**Correcciones al trabajo anterior:**
- Alelo 2 p.Asn1002Lys: era "probablemente patogénica (PM2+PP3)"; con puntos ACMG es **VUS** (REVEL 0,472 indeterminado, BayesDel tolerado)
- Alelo 1: ClinVar Pathogenic es de un único remitente; con criterios propios son 9 puntos (probablemente patogénica)
- El diagnóstico BUB1B bialélico es **muy probable, no confirmado**: falta fase *trans* (sin padres) y datos funcionales
- Notebook 05: exón 21 → 17, c.2210T>A → T>G, "313 aa" → 314, quitados PM1/PP2 sin respaldo, y marcados como **sin verificar** los límites de dominios (UniProt: dominio quinasa 766–1050, p.Leu737 queda antes) y la tabla de literatura (de memoria)
- El PDF del H1 que circuló tenía el mapa de dominios con esas coordenadas sin verificar; regenerado

---

## 2026-10-02 — Cambio de organización: de roles a tareas

**Quién:** Ktalyna (con Claude Code)  
**Decisión:** el equipo no llegó a un acuerdo sobre los 6 roles fijos. Se trabajará **por tareas**: el plan se dividió en 5 áreas (A variante · B mecanismo · C fármacos · D código · E informe) con tareas pequeñas identificadas por ID, fecha y dependencias. Cada persona toma hasta 2 tareas a la vez.

**Qué cambió:**
- `docs/plan_equipo_roles.md` → `docs/plan_equipo_tareas.md` (tablero de tareas, guía "¿por dónde empiezo?", reglas y checklist)
- Ramas nuevas: `tarea/<ID>-descripcion` (ej. `tarea/B1-marco-biologico`)
- `plan_de_trabajo.md` y README apuntan al nuevo tablero
- Las menciones a R1–R6 en notebooks y entradas anteriores equivalen a: R1/R2 → A · R3 → B · R4 → C · R5 → D · R6 → E

**Pendiente:**
- [ ] Cada integrante toma su primera tarea y se anota en el tablero

---

## 2026-10-01 — ✅ HITO H1 COMPLETADO: variante causante confirmada

**Quién:** Ktalyna (con Claude Code) — ejecución real del pipeline  
**Qué se hizo:**
- Ejecutado el pipeline completo: VCF → gnomAD v4 → CADD v1.7 → ClinVar
- Confirmadas las dos variantes BUB1B con datos reales de APIs públicas

### Resultados confirmados

| Campo | Variante 1 | Variante 2 |
|-------|-----------|-----------|
| **Posición (GRCh38)** | 15:40209701 | 15:40220612 |
| **Cambio VCF** | T>G | T>G |
| **rsID** | rs759242053 | — (sin rsID) |
| **HGVSc** | c.2210T>G | c.3006T>G |
| **HGVSp** | **p.Leu737Ter** | **p.Asn1002Lys** |
| **Consecuencia** | stop_gained | missense_variant |
| **Transcrito canónico** | ENST00000287598 (BUB1B) | ENST00000287598 (BUB1B) |
| **CADD phred** | **36.0** (top 0.025%) | **24.5** (top 0.35%) |
| **ClinVar** | **Pathogenic** (ID 533901) ✅ | no registrada |
| **AF exoma gnomAD v4** | 7.87×10⁻⁵ (0.008%) | **6.84×10⁻⁷ (0.00007%)** |
| **AF genoma gnomAD v4** | 3.29×10⁻⁵ | ausente |
| **Homocigotos gnomAD** | **0** | **0** |
| **Criterios ACMG** | PVS1 | PM2 + PP3 |
| **Interpretación** | **PATOGÉNICA** ✅ | **Prob. Patogénica** ✅ |

### Corrección importante sobre la variante 2

SnpEff (vía myvariant.info) erróneamente clasifica 15:40220612 T>G como "intergenic_region". gnomAD v4 confirma que está en el **transcrito canónico de BUB1B** (ENST00000287598), exón correspondiente a p.Asn1002Lys.

### Archivos generados
- `results/hito_H1_resultados_finales.json` — tabla completa con fuentes

---

## 2026-10-01 — Notebook 05: mecanismo biológico BUB1B/BUBR1

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Creado `notebooks/05_mecanismo_biologico_bub1b.ipynb` — mecanismo completo para Hitos H2 y H3
- Documenta: estructura BUBR1 (5 dominios), SAC normal, efecto de p.Leu737Ter (NMD/LOF) y p.Asn1002Lys (missense pseudo-kinasa), cascada hasta mosaicismo, fenotipo clínico
- Genera 3 figuras: dominios BUBR1 · SAC normal vs disfuncional · cascada fisiopatológica
- Produce `results/resumen_mecanismo_para_R4.json` (6 targets farmacológicos para R4) y `results/hito_H3_mecanismo_completo.json`

**Targets identificados para R4:**
- APC/C · CDC20 · PLK1 (Volasertib) · Aurora B (Barasertib) · Hsp90 (estabilizador alelo missense) · p53 pathway

**Pendiente (R3):**
- [ ] Revisar y completar secciones de literatura (referencias en celda 7)
- [ ] Confirmar CADD de p.Asn1002Lys (notebook 04) antes de entregar a R4

---

## 2026-10-01 — Notebook 04: priorización gnomAD y variante causante

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Creado `notebooks/04_priorizacion_gnomad_variante_causante.ipynb`
- Pipeline completo: het. BUB1B → gnomAD v4 (GraphQL) → AF < 1% → myvariant.info (CADD/ClinVar) → tabla de priorización → confirmación het. compuesta
- Genera `results/bub1b_variantes_priorizadas.csv`, `results/figura_01_priorizacion_bub1b.png`, `results/hito_H1_variante_causante.json`
- Incluye búsqueda de alternativas en CEP57/TRIP13 para descartar otras causas

**Hipótesis documentada:**
- BUB1B het. compuesta: `15:40209701 p.Leu737Ter` (stop → NMD → LOF) + `15:40220612 p.Asn1002Lys` (missense dominio kinasa)
- Criterios ACMG aplicados en el notebook: PVS1, PM1, PM2, PM3, PP2, PP3

**Pendiente (R2):**
- [ ] Correr el notebook con el VCF real y verificar que gnomAD v4 confirma AF < 1% para ambas variantes
- [ ] Confirmar CADD score para p.Asn1002Lys (≥ 20 refuerza patogenicidad)

---

## 2026-10-01 — Plan de equipo para 6 personas

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Se creó `docs/plan_equipo_roles.md` con 6 roles (R1–R6), el perfil de habilidades de cada uno en %, sus tareas por semana, 7 hitos (H1–H7), una matriz de dueños/revisores y reglas de fidelidad al rol

**Decisiones:**
- Semanas de jueves a miércoles: S1 = variante, S2 = mecanismo, S3 = fármacos + borrador, S4 = entrega
- Congelación del código el **viernes 23 oct a las 12:00 UTC**; entrega interna el **sábado 24 oct a las 18:00 UTC** (6 h de margen)
- A partir de ahora: trabajo en ramas `rN/...` y PR con revisor; nada directo a `master`

**Pendiente:**
- [ ] Las 6 personas eligen rol y se anotan en la sección 7 del plan
- [ ] Cada integrante confirma su propio acceso aprobado en HF

---

## 2026-10-01 — Integración del trabajo de Laura al repo

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Se revisó el Colab de Laura (`Versión actualizada fase 1 - 2.ipynb`)
- Se reconstruyó como `notebooks/03_exploracion_Laura_201_genes.ipynb` y se subió al repo
- Se creó `scripts/resolve_genes.py` (coordenadas via MyGene.info)
- Se creó `config/genes_candidatos.txt` (lista base ~200 genes, pendiente confirmar con Laura)

**Hallazgos / decisiones:**
- ✅ Corrección importante: las homocigotas de BUB1B y CEP57 son polimorfismos comunes (AF > 15% en gnomAD) — **no son la causa**
- ✅ Corrección importante: el "ROH" de MAD1L1 no era tal — hay heterozigotas entremezcladas, 23% homocigotas vs 39% del genoma. Sin evidencia de consanguinidad en ese locus
- ✅ Con 201 genes: 19,099 variantes PASS en 195 genes
- 🔍 Causa probable adelantada por Laura (desde notebook 04 en Colab): **BUB1B het. compuesto — p.Leu737Ter (15:40209701) + p.Asn1002Lys (15:40220612)**

**Pendiente:**
- [ ] Laura: confirmar/reemplazar `config/genes_candidatos.txt` con su lista original de 201 genes
- [ ] Laura: subir notebook 04 al repo (priorización gnomAD + identificación variante)

---

## 2026-09-17 — Exploración inicial + filtrado por 6 genes

**Quién:** Ktalyna (con Claude Code)  
**Qué se hizo:**
- Inicializado el repo en GitHub (`ktalynagb/mva-hackathon-2026`, privado)
- Configurado entorno Python (`.venv/`, `requirements.txt`)
- Autenticación en HuggingFace y verificación de acceso al dataset gated
- Descargados los archivos relevantes para Track 2 (~303 MB):
  - `WGS_EX2312012_HGWCNDSX7.vcf.gz` (300.6 MB)
  - `WGS_EX2312012_HGWCNDSX7.vcf.gz.tbi` (2.2 MB)
  - `Challenge_Clinical_Phenotype_1.docx`
- Invitada Laura (`lauracamilavargas-lang`) como colaboradora admin

**Hallazgos del VCF:**
- 5,012,204 variantes totales · 4,740,790 PASS (94.6%)
- 81.4% SNV · 18.6% INDEL
- Muestra única: `WGS_EX2312012` · Pipeline: Sentieon Haplotyper + GATK VariantFiltration · Referencia: GRCh38 (sin prefijo `chr`)

**Hallazgos del fenotipo (HPO):**

| Característica | HPO | Nota |
|----------------|-----|------|
| Rabdomiosarcoma | HP:0002859 | Evento que inició la investigación |
| Nefrocalcinosis | HP:0000121 | Desde el nacimiento |
| Talla baja | HP:0004322 | |
| Falla de medro | HP:0001508 | |
| Atrofia muscular | HP:0003202 | |
| Prematuridad (32 sem) | HP:0001622 | |
| Pequeño para edad gestacional (~1 kg) | HP:0001518 | RCIU severo |
| Abortos recurrentes (parentales) | HP:0200067 | Señal de herencia |

**Filtrado por 6 genes candidatos (BUB1B, CEP57, TRIP13, BUB1, MAD1L1, MAD2L1):**
- 1,075 variantes PASS
- BUB1B: 16 total · 7 homocigotas · 9 heterocigotas
- CEP57: 7 total · 3 homocigotas · 4 heterocigotas
- TRIP13: 3 total · 0 homocigotas · 3 heterocigotas

**Decisiones:**
- No descargar FASTQ (~79 GB) — innecesarios para Track 2
- Herencia esperada: autosómica recesiva → buscar hom. o het. compuesto

**Archivos creados:**
- `notebooks/01_exploracion_inicial.ipynb`
- `notebooks/02_filtrado_vcf_genes_mva.ipynb`
- `scripts/filter_mva_genes.py`
- `results/mva_gene_coords_grch38.json`
- `docs/plan_de_trabajo.md`

---

## Estado actual del proyecto

### Fases

| Fase | Descripción | Estado | Responsable |
|------|-------------|--------|-------------|
| 1 | Datos y exploración | ✅ Completa | Ktalyna + Laura |
| 2 | Identificar variante causante | ✅ **COMPLETADA** — Hito H1 logrado | Ktalyna + Laura |
| 3 | Caracterizar mecanismo biológico | 🔄 B1 y B4 (H2) en revisión, PR #6; falta B5 (H3, 14 oct) | Área B |
| 4 | Candidatos de reposicionamiento | 🔄 C1 en revisión, PR #7; C2 a C6 sin responsable | Área C |
| 5 | Informe + entrega | 🔄 Plantilla y guion en revisión, PR #8 | Área E |

### Hipótesis actual

La causa del MVA en este paciente es **BUB1B heterocigótica compuesta**, muy probable pero sin confirmación formal: falta demostrar la fase *trans* y el alelo 2 es VUS (ver `secciones/01_variante_causante.md`):

| Alelo | Posición | HGVSp | CADD | ClinVar |
|-------|----------|-------|------|---------|
| 1 | 15:40209701 | **p.Leu737Ter** (stop → NMD → LOF) | 36.0 | **Pathogenic** |
| 2 | 15:40220612 | **p.Asn1002Lys** (missense pseudo-kinasa) | 24.5 | no registrada |

Ambas son heterocigotas, ultra-raras en gnomAD v4 (7.87×10⁻⁵ y 6.84×10⁻⁷), sin homocigotos.  
→ Alelo nulo + alelo hipomórfico inestable → poca BUBR1 → SAC débil → errores de segregación → MVA.

---

## Pendientes globales

- [x] Fusionar PR #1 y #2 (tarea D1)
- [ ] Revisar y fusionar los PR #6, #7 y #8
- [x] Laura confirma `config/genes_candidatos.txt` (tarea A6, 14 oct: 31 genes agregados, ninguno explica el MVA)
- [ ] Cada integrante toma tareas del [tablero](plan_equipo_tareas.md)
- [ ] Completar `methods_description_form.xlsx` antes del 24 oct (tarea E7)
