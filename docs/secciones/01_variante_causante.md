# 01 · Variante causante: evidencia y clasificación ACMG

**Tareas A2 y B2 · borrador para revisión** · Datos al 2 de octubre de 2026
Fuentes: VCF del paciente (GRCh38) · gnomAD v4 · CADD v1.7 · myvariant.info (dbNSFP, ClinVar) · Ensembl (ENST00000287598) · UniProt O60566

## 1. Conclusión en tres líneas

- Alelo 1, **p.Leu737Ter**: variante de pérdida de función con NMD predicho. Clasificación: **Probablemente patogénica** con nuestros criterios (9 puntos) y reportada como **Patogénica** en ClinVar por un solo remitente.
- Alelo 2, **p.Asn1002Lys**: ultra-rara, el residuo está muy conservado y encaja estructuralmente como dañino, pero los predictores discrepan y no hay casos ni datos funcionales. Con criterios ACMG estrictos es una **VUS** (1 a 2 puntos), inclinada a patogénica.
- El diagnóstico **BUB1B bialélico es muy probable pero no está confirmado formalmente**: falta establecer que las dos variantes están en alelos distintos (fase *trans*) y no hay datos funcionales.

> Esto corrige la redacción anterior del Hito H1 ("confirmada", alelo 2 "probablemente patogénica"). Los datos son los mismos; cambia la lectura de cuánto prueban.

## 2. Las dos variantes

| | Alelo 1 | Alelo 2 |
|---|---|---|
| Posición (GRCh38) | 15:40209701 T>G | 15:40220612 T>G |
| rsID | rs759242053 | sin rsID |
| Transcrito | ENST00000287598 (BUB1B-201) | ENST00000287598 |
| HGVS | c.2210T>G · p.Leu737Ter | c.3006T>G · p.Asn1002Lys |
| Consecuencia | stop_gained (TTA→TGA) | missense_variant |
| Exón | 17 de 23 | 23 de 23 (último) |
| Posición en la proteína | codón 737 de 1050, antes del dominio quinasa (766–1050) | dentro del dominio quinasa |
| gnomAD v4 exomas | AF 7,87×10⁻⁵ · 0 homocigotos | AF 6,84×10⁻⁷ (1 alelo) · 0 homocigotos |
| gnomAD v4 genomas | AF 3,29×10⁻⁵ | ausente |
| ClinVar | Pathogenic (ID 533901), MVA1; 1 remitente con criterios. Otro registro: Likely pathogenic | no registrada |

**Calidad de las llamadas** (tarea A4, ya cubierta con el VCF):

| | Filtro | Genotipo | Lecturas ref/alt | Fracción alt | DP | GQ |
|---|---|---|---|---|---|---|
| Alelo 1 | PASS | 0/1 | 21 / 25 | 0,54 | 46 | 99 |
| Alelo 2 | PASS | 0/1 | 15 / 13 | 0,46 | 28 | 99 |

Ambas son llamadas limpias y la fracción alélica es compatible con heterocigosis germinal (≈ 0,5). No hay señal de mosaicismo en estas dos posiciones.

## 3. Clasificación ACMG/AMP

Usamos el sistema de puntos de Tavtigian et al. (2020): muy fuerte = 8, fuerte = 4, moderado = 2, de apoyo = 1. **Patogénica** ≥ 10 · **Probablemente patogénica** 6–9 · **VUS** 0–5. PM2 se aplica como de apoyo (*Supporting*), siguiendo la recomendación de ClinGen SVI.

### Alelo 1 · p.Leu737Ter

| Criterio | Aplica | Puntos | Justificación |
|---|---|---|---|
| PVS1 | Sí | 8 | Codón de stop en el exón 17 de 23. NMD predicho (sección 4). La pérdida de función bialélica de *BUB1B* es un mecanismo establecido de MVA1. |
| PM2_Supporting | Sí | 1 | AF 7,87×10⁻⁵ en gnomAD v4, sin homocigotos. El umbral de 10⁻⁴ para una enfermedad recesiva muy rara es una decisión del equipo. |
| PM3 | No | 0 | Requiere confirmar que está en *trans* con otra variante patogénica. Fase desconocida. |
| PP4 | No sumado | 0 | El fenotipo es muy específico (MVA, rabdomiosarcoma), pero el dataset no incluye cariotipo con aneuploidías en mosaico. Si el equipo lo confirma, +1. |
| **Total** | | **9** | **Probablemente patogénica**. ClinVar la reporta como Patogénica (remitente único, 1 estrella). |

### Alelo 2 · p.Asn1002Lys

| Criterio | Aplica | Puntos | Justificación |
|---|---|---|---|
| PM2_Supporting | Sí | 1 | 1 alelo en gnomAD v4 exomas, ausente en genomas, 0 homocigotos. |
| PP3 | Discutible | 0 a 1 | A favor: CADD 24,5, AlphaMissense 0,92 (patogénica), PolyPhen-2 1,0, SIFT 0,0. En contra: **REVEL 0,472** (zona indeterminada, 0,29–0,64) y BayesDel con AF = 0,049 (tolerada). CADD no está calibrado para PP3 en las recomendaciones de ClinGen (Pejaver et al., 2022). |
| PM1 | No | 0 | Estar en el dominio quinasa no basta; no hay evidencia de un punto caliente. |
| PM3 | No | 0 | Fase desconocida. |
| PS3 | No | 0 | Sin datos funcionales. |
| **Total** | | **1 a 2** | **VUS** |

### Evidencia adicional para el alelo 2

Reproducible con `python scripts/evidencia_alelo2.py` (resultados en `results/evidencia_alelo2.json`).

| Fuente | Hallazgo | Qué implica |
|---|---|---|
| ClinVar (2501 registros de *BUB1B*) | El mismo cambio de aminoácido ya está registrado como **VUS** (p.Asn1002Lys por c.3006T>A; el paciente tiene c.3006T>G), de un remitente. En el único cambio de aminoácido patogénico de todo el gen (p.Gln467His, probablemente patogénico) no hay respaldo cercano. Los 23 cambios de aminoácido en los residuos 996–1008 son VUS o benignos. | No hay base para PM1 ni PM5. PS1 no aplica (el registro previo es VUS). |
| AlphaFold (modelo v6) | pLDDT del residuo = **91,1** (muy alta confianza; media del dominio quinasa 81,9). Mayormente enterrado (accesibilidad relativa 0,13; mediana del dominio 0,16). La cadena lateral de la Asn1002 forma 3 enlaces de hidrógeno con el esqueleto de Trp978 y Val998. A 6,9 Å está Arg999, con carga positiva. | Compatible con un papel estructural: la lisina perdería esos enlaces y añadiría carga positiva junto a Arg999. Es un análisis geométrico aproximado, no una simulación. |
| Conservación (7 vertebrados) | El residuo es **asparagina en las 7 especies** (ratón, rata, vaca, perro, pollo y dos *Xenopus*). El motivo ILNA es idéntico en todas. | Residuo muy conservado; apoya que es importante. Alineamiento simple, a revisar con uno múltiple. |
| PubMed | Ningún artículo describe p.Asn1002Lys. Cercanos: variantes missense heterocigotas W722R y A739S en familias con pérdida gestacional recurrente y separación prematura de cromátidas (PMID 42434306), y un caso de MVA con p.Ser788Cfsx29 (PMID 40555658). Solo leí los resúmenes. | Sin casos publicados (PS4). Los cercanos muestran que variantes de esa región pueden afectar a BUBR1, pero no son el mismo cambio. |

**Efecto en la clasificación.** Conservación, estructura y predictores son el mismo tipo de evidencia (PP3) y no se suman de forma independiente. Todo apunta en la misma dirección, pero ninguna es evidencia fuerte, así que el alelo 2 **sigue como VUS**, ahora con un perfil de "VUS que se inclina a patogénica". Subiría con: fase *trans* demostrada (PM3), un ensayo funcional (PS3) o casos publicados con el mismo cambio (PS4).

### Hipótesis del equipo y su verificación

Aportes del grupo (2 oct) puestos a prueba con datos. Todo sale de `scripts/evidencia_alelo2.py` (UniProt y modelo de AlphaFold).

| Hipótesis | Resultado | Lectura |
|---|---|---|
| Asn → Lys cambia un aminoácido polar y pequeño por uno grande con carga positiva | **Confirmado.** N1002 está mayormente enterrado (accesibilidad relativa 0,13). Queda en el extremo de una hélice (residuos 996–1001; ángulos φ/ψ = −127°/37°) y su cadena lateral forma 3 enlaces de hidrógeno con el esqueleto de Trp978 y Val998, que la lisina no puede reproducir. Cerca hay cargas positivas (Arg999 a 5,4 Å, Lys979 a 9,0 Å); Asp1005 y Glu1006 (a ~9 Å) están expuestos y solo podrían compensar en parte. | Apoya una desestabilización local. Es un análisis geométrico, no una simulación. |
| La asparagina podría ser un sitio de glicosilación | **Descartado.** El contexto es N-A-N-D (no es el motivo N-X-S/T) y UniProt no anota glicosilación en BUBR1; sus motivos N-X-S/T están en otras posiciones (52, 97, 268, 541, 598, 711, 944, 983). | Coincide con lo planteado por el grupo: no importa para este caso. |
| El plegamiento se vuelve inestable y la proteína se degrada antes de tiempo | **Desestabilización moderada confirmada por cálculo; la degradación no se demuestra.** ΔΔG de N1002K = **+1,5 kcal/mol** (positivo = desestabiliza). La variante conocida de MVA1 **p.Leu1012Pro** (UniProt: "heterocigota compuesta con una mutación sin sentido", el mismo tipo de genotipo del paciente) da +3,1 y cae a 12,3 Å de N1002, en la misma región de hélices. Detalle en el cálculo de estabilidad más abajo. | Apoya que el dominio queda menos estable, sin llegar a probar una vida media corta. Falta un experimento (nivel de BUBR1 por Western blot). |
| El dominio pierde estructura y no puede unirse a otras proteínas | **Parcial.** N1002 está a 29 Å del bolsillo de unión a ATP (residuos 772–780 y 795), así que no afecta ese sitio. El efecto vendría de la estabilidad del dominio, no del bolsillo. La pseudoquinasa favorece el reclutamiento de PP2A-B56 (Gama Braga 2020), una pérdida de unión testeable. | La pérdida de unión es una hipótesis, no una conclusión. |
| El dominio quinasa es un andamio al que se unen MAD2 y CDC20 | **No respaldado por la literatura.** MAD2 se une al dominio TPR del extremo N-terminal (residuos 1–220; PDB 6TLJ) y CDC20 a los motivos KEN, ABBA y cajas D de la región N-terminal y central. La pseudoquinasa (766–1050) es un dominio estructurado cuyo papel descrito es sostener su propia conformación y favorecer el reclutamiento de PP2A-B56 y el alineamiento cromosómico (Zhang 2026; Suijkerbuijk 2012; Gama Braga 2020). | Sí actúa como plataforma de interacción, pero con otros socios. El efecto de N1002K sobre MAD2/CDC20 sería indirecto (menos proteína estable), no por perder su sitio de unión. |
| El gen es de copia única: una variante en cada copia basta | **Correcto**, pero la fase no se puede comprobar con este dataset. | Ver sección 7. |

**Efecto en la clasificación.** No cambia: el alelo 2 sigue como VUS inclinada a patogénica. No hay base para PM1 (en la región, ClinVar solo tiene variantes de significado incierto o benignas) ni para PM5 (L1012P es otro residuo). Lo que sí aporta es un precedente de genotipo: un caso de MVA1 con una mutación sin sentido más un missense en esta misma región.

#### Cálculo de estabilidad (ΔΔG) con ThermoMPNN

Se usó ThermoMPNN (Dieckhaus et al. 2024, PNAS 121:e2314853121, PMID 38285937), que predice el cambio de estabilidad de cada sustitución a partir de la estructura. Se corrió sobre el modelo de AlphaFold de la proteína completa y sobre el dominio quinasa (766–1050) por separado. Convención: **positivo = desestabiliza, negativo = estabiliza**. Reproducible con `scripts/estabilidad_alelo2.py` (versión exacta de la herramienta en `results/estabilidad_alelo2.json`).

| Sustitución | ΔΔG (kcal/mol) | Posición entre todas las sustituciones del dominio |
|---|---|---|
| **p.Asn1002Lys** (paciente) | **+1,5** | percentil 72–75 |
| p.Leu1012Pro (variante conocida de MVA1) | +3,1 | percentil 98–99 |

- **Todas las sustituciones en la posición 1002 desestabilizan** (de +0,9 a +2,6): la asparagina es la mejor opción en ese sitio. La lisina queda en un punto intermedio (13.ª de 19, de mayor a menor efecto).
- **La predicción es la misma con la proteína completa y con el dominio** (coincidencia de las dos corridas: Spearman 0,95; N1002K da +1,51 en ambas).
- **Controles del propio cálculo.** La numeración coincide con UniProt en los 21.000 casos; cambiar un residuo por sí mismo da exactamente 0; las sustituciones a prolina desestabilizan más que a alanina (+1,9 frente a +0,9); en residuos hidrofóbicos enterrados (63 posiciones) pasar a D, K, P o G da +2,5, frente a +0,2 en residuos expuestos. Esto confirma el signo y que el modelo se comporta como se espera.

**Lectura.** N1002K desestabiliza el dominio de forma **moderada**, aproximadamente la mitad que p.Leu1012Pro. Un efecto de este tamaño encaja con un alelo **hipomórfico** (pérdida parcial de función), que es justo el papel que se espera del segundo alelo junto a uno nulo. No basta por sí solo para afirmar que la proteína se degrada rápido.

**Limitaciones.**
- Es una predicción sobre un modelo estático de AlphaFold (confianza alta en este residuo, pLDDT 91); la incertidumbre típica de estos predictores es del orden de 1 kcal/mol, comparable al efecto predicho. No lo verifiqué contra datos experimentales en este caso.
- Mide estabilidad termodinámica del dominio aislado, no vida media en la célula, y no captura efectos sobre la unión a otras proteínas (por ejemplo PP2A-B56) ni sobre la proteína completa en contexto.
- No es una herramienta calibrada para el criterio PP3 de ACMG, así que **no cambia la clasificación**: el alelo 2 sigue como VUS inclinada a patogénica.

**Para confirmarlo en el laboratorio:** nivel de BUBR1 por Western blot en células del paciente, con y sin inhibidor del proteasoma (MG132), y una prueba de unión a PP2A-B56.

## 4. NMD de p.Leu737Ter (tarea B2)

Estructura del transcrito ENST00000287598 (Ensembl): 23 exones, CDS de 3153 nt, 1050 aa.

| Dato | Valor |
|---|---|
| Exón del PTC | 17 (c.2144–2284) |
| Posición del PTC | c.2210 |
| Última unión exón-exón | exones 22/23, entre c.2957 y c.2958 |
| Distancia del PTC a esa unión | **747 nt** |
| Regla de referencia | PTC > 50–55 nt antes de la última unión → NMD |
| Excepciones | No está en el primer exón ni cerca del ATG |

**Predicción:** el ARNm del alelo 1 es sustrato de NMD. Si escapara, el producto tendría 736 aa y no tendría el dominio quinasa.

**Límite:** es una predicción por regla. No hay datos de ARN del paciente. Se confirmaría con RT-PCR en fibroblastos o linfocitos, con y sin ciclohexamida.

## 5. Diagnóstico diferencial (tarea A3)

**Pregunta:** ¿algún otro gen del panel podría explicar el MVA del paciente?

**Método** (`python scripts/diagnostico_diferencial.py`):
1. Variantes PASS del paciente dentro de los 187 genes distintos de `config/genes_candidatos.txt` (unas 16.000; algunas se cuentan en más de un gen porque ciertos alias comparten locus).
2. Frecuencia en gnomAD v4 (se conservan las raras: AF < 1 % o ausentes) y consecuencia (gnomAD o Ensembl VEP).
3. Se dejan las variantes funcionales: pérdida de función (stop, cambio de marco, sitio de empalme, pérdida de inicio o de stop), missense y en el marco.
4. Patrón recesivo compatible: al menos 1 homocigota o 2 heterocigotas en el mismo gen.

**Resultado:** solo **11 variantes raras funcionales en 10 genes**, todas heterocigotas. Las posiciones de las variantes de los genes que no son *BUB1B* no se incluyen aquí; el script las regenera en `results/` (los `.tsv` están en `.gitignore`).

| Gen | Consecuencia | AF gnomAD v4 | ¿Recesivo? |
| --- | --- | --- | --- |
| **BUB1B** | stop_gained | 7,9×10⁻⁵ | **Sí, 2 variantes** |
| **BUB1B** | missense | 6,8×10⁻⁷ |  |
| SMC1B | sitio de empalme (aceptor) | 0,73 % (5 homocigotos en gnomAD) | No, solo 1 |
| ANAPC2 | missense | 1,6×10⁻⁴ | No |
| ATM | missense | 8,4×10⁻⁴ (7 homocigotos) | No |
| CENPO | missense | 0,38 % (17 homocigotos) | No |
| MAD1L1 | missense | 0,46 % (23 homocigotos) | No |
| SASS6 | missense | 0,25 % (6 homocigotos) | No |
| SMC4 | missense | 6,6×10⁻⁷ | No |
| TUBB8 | missense | 0,92 % | No |
| TUBGCP6 | missense | 1,1×10⁻⁴ | No |

**Los genes de MVA conocidos quedan descartados en cuanto a variantes codificantes:**
- ***CEP57***: 4 variantes PASS, ninguna rara ni funcional.
- ***TRIP13***: 3 variantes PASS, ninguna rara ni funcional.
- ***MAD2L1BP*** (p31comet, MVA descrito en 2023): 4 variantes PASS, ninguna rara ni funcional.
- *BUB1*, *BUB3*, *MAD2L1*, *CDC20*, *ESPL1*: sin variantes raras funcionales.

**Lectura.** *BUB1B* es el único gen del panel donde una variante de pérdida de función se acompaña de otra variante rara funcional. No hay ninguna variante rara funcional homocigota en los 187 genes, así que tampoco hay una explicación recesiva por homocigosis. Los demás genes tienen a lo sumo una variante heterocigota, que no basta para un modelo recesivo, y la mayoría son frecuentes en gnomAD, con homocigotos sanos.

**Limitaciones de este análisis:**
- Solo variantes PASS en los genes de la lista. Un gen de MVA que no esté en el panel no se evalúa.
- **No se evalúan variantes estructurales ni de número de copias** (por ejemplo, deleciones de un exón en *BUB1B* o *CEP57*) ni variantes no codificantes. Un caso publicado de MVA combinó una variante de cambio de marco con una variante en elementos reguladores de *BUB1B* (Qu 2025, PMID 40555658, solo resumen).
- La consecuencia de las variantes ausentes de gnomAD viene de VEP (la más severa en cualquier transcrito), que puede sobrestimar el efecto en el transcrito canónico.
- Un umbral de AF del 1 % deja pasar variantes demasiado frecuentes para una enfermedad tan rara; aquí no cambió el resultado.

> Una primera versión del barrido marcó 31 variantes comunes como "ausentes de gnomAD" porque la lista de variantes por gen de gnomAD omite algunas. Se corrigió consultando cada variante funcional directamente.

## 6. Interpretación combinada

El paciente es heterocigoto para una variante probablemente patogénica de pérdida de función y para una variante rara de significado incierto en el mismo gen, cuya enfermedad recesiva (MVA1) encaja con el fenotipo. Es un genotipo típico de MVA1 si ambas están en *trans*: un alelo nulo más un alelo hipomórfico, porque la pérdida total en los dos alelos probablemente sería incompatible con la vida (hipótesis a verificar en B1).

Si estuvieran en *cis*, el paciente tendría un alelo normal y no explicaría la enfermedad. Como el cuadro clínico es grave, *trans* es mucho más probable, pero no está demostrado.

**Dato externo.** El código público del reto (página oficial en Hugging Face) describe la respuesta de Track 1 como una "respuesta compuesta heterocigota clínicamente validada" (*clinically validated compound-heterozygous answer key*), validada por el NHS. Esto respalda que el caso es una heterocigosis compuesta, es decir, dos variantes. No dice en qué gen ni cuáles son, así que no confirma nuestras dos variantes.

## 7. Limitaciones

1. **Fase sin resolver, y no resoluble con este dataset.** El dataset de Hugging Face (13 archivos) contiene solo al paciente: su VCF, sus lecturas crudas (FASTQ) y el documento clínico, que de los padres solo menciona abortos recurrentes. Las variantes están a 10,9 kb y los registros del VCF no traen etiquetas de fase (`PGT`/`PID`). Tampoco se puede encadenar la fase con las lecturas crudas: entre ambas hay una sola heterocigota intermedia (15:40216470), a 6,8 kb de la primera y 4,1 kb de la segunda, muy por encima del tamaño de fragmento de lecturas cortas (~0,5 kb). El faseo estadístico no es fiable para variantes tan raras. Argumento indirecto a favor de *trans*: si estuvieran en el mismo cromosoma (*cis*), el paciente tendría una copia normal de *BUB1B* y no se esperaría la enfermedad.
2. **Alelo 2 sin evidencia funcional.** Su clasificación depende de predictores que discrepan.
3. **NMD no medido** (sección 4).
4. **ClinVar del alelo 1** viene de un único remitente. Conviene revisar los detalles del registro 533901.
5. **Variantes estructurales y no codificantes sin evaluar** (sección 5).

## 8. Qué lo confirmaría

- Genotipar a los padres (Sanger o panel dirigido) para establecer la fase.
- RT-PCR del alelo 1 para demostrar el NMD.
- Ensayo funcional de p.Asn1002Lys (estabilidad de BUBR1 y señal del SAC en fibroblastos del paciente).
- Cariotipo o FISH que muestre aneuploidías en mosaico.
- **Evaluación automática del reto (Track 1).** El sitio oficial puntúa al instante una pareja de variantes contra la respuesta clínicamente validada. Fila de envío para nuestra hipótesis principal (coordenadas GRCh38, `proband_id` tal como figura en el dataset):

```
proband_id,chrom_1,pos_1,ref_1,alt_1,chrom_2,pos_2,ref_2,alt_2,epcr,finding_type,notes
WGS_EX2312012,chr15,40209701,T,G,chr15,40220612,T,G,0.85,primary,BUB1B compound het: p.Leu737Ter + p.Asn1002Lys
```

## 9. Referencias

Existencia confirmada en PubMed (falta leer el texto completo): Hanks et al. 2004, *Nat Genet* (PMID 15475955) · Matsuura et al. 2006, *Am J Med Genet A* (PMID 16411201) · Wei et al. 2026, *Front Endocrinol* (PMID 42434306) · Qu et al. 2025, *Zhonghua Yi Xue Yi Chuan Xue Za Zhi* (PMID 40555658).

Citadas de memoria, sin comprobar: Tavtigian et al. 2020, *Hum Mutat* · Pejaver et al. 2022, *Am J Hum Genet* · Richards et al. 2015, *Genet Med* (guía ACMG/AMP) · Abou Tayoun et al. 2018, *Hum Mutat* (PVS1). Comprobar autores, volumen y páginas antes del informe.
