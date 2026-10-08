# 02 · Marco biológico: BUBR1, el checkpoint mitótico y el MVA

**Tarea B1 · versión para revisión** · 8 de octubre de 2026
Todas las referencias se comprobaron en PubMed. La tabla de la sección 10 indica cuáles se revisaron en texto completo y cuáles solo en resumen.

## 1. Idea central en cinco líneas

1. Antes de dividirse, la célula comprueba que cada cromosoma esté bien anclado al huso. Esa vigilancia es el **checkpoint mitótico (SAC)**.
2. BUBR1, la proteína de *BUB1B*, forma parte del complejo que frena la división mientras haya cromosomas mal anclados: el **MCC** (BUBR1, BUB3, MAD2 y CDC20).
3. En el MVA por *BUB1B* lo que falla sobre todo es la **cantidad** de BUBR1: el alelo truncante no produce proteína y el missense del dominio quinasa produce una proteína que se pliega mal y se degrada rápido (sección 4).
4. Con poca BUBR1 el freno falla, la célula se divide antes de tiempo y reparte mal los cromosomas: **aneuploidía en mosaico** (MVA).
5. El MVA se asocia a retraso del crecimiento, microcefalia y cáncer infantil, entre ellos el rabdomiosarcoma.

## 2. Estructura de BUBR1 (1050 aa)

Coordenadas de UniProt O60566 y Zhang et al. 2026 (PMID 42477419).

| Elemento | Residuos | Función |
|---|---|---|
| KEN1 y KEN2 | 26–28 · 304–306 | Unión a CDC20; esenciales para la señal del SAC |
| Dominio TPR | 59–219 | Interacciona con MAD2, CDC20 y APC/C; favorece formar el MCC |
| Cajas D | 224–232 · 555–563 | Interacción con CDC20/APC/C |
| GLEBS | 408–418 | Une BUB3 |
| Motivo de unión a BUB1 | 440–460 | Junto con GLEBS lleva BUBR1 al cinetocoro |
| KARD (LxxIxE) | 669–674 | Une la fosfatasa PP2A-B56: estabiliza la unión al microtúbulo y apaga el SAC |
| Pseudoquinasa | 766–1050 | No necesita catalizar; su integridad sostiene la estabilidad de toda la proteína (sección 4) y favorece el reclutamiento de PP2A-B56 |

**¿Dónde se unen MAD2 y CDC20?** En el extremo N-terminal y la región central, no en la pseudoquinasa. MAD2 se une al dominio TPR (los residuos 1–220 bastan en ensayos de unión; estructura PDB 6TLJ). CDC20 se une a los motivos KEN, ABBA y cajas D de esa región. La función inhibidora de BUBR1 reside en los ~450 aminoácidos N-terminales y no requiere el dominio quinasa (Suijkerbuijk 2010, PMID 20516114). La pseudoquinasa sí es una plataforma de interacción, pero con otros socios (PP2A-B56; Gama Braga 2020, PMID 33207204).

**Dónde caen las variantes del paciente**
- **p.Leu737Ter** (residuo 737): después de TPR, KEN, cajas D, GLEBS y KARD, y antes de la pseudoquinasa. Con NMD predicho (`01_variante_causante.md`, sección 4), lo esperable es que este alelo no produzca proteína.
- **p.Asn1002Lys** (residuo 1002): dentro de la pseudoquinasa.

> Corrección: el notebook 05 mostraba una tabla de dominios con coordenadas de memoria (GLEBS 430–480, TPR "×8" 60–400, pseudoquinasa desde 780). No coincidían con las fuentes y se reemplazaron.

## 3. MVA y *BUB1B*

| Hallazgo | Fuente |
|---|---|
| Primeras mutaciones bialélicas de *BUB1B* en MVA, truncantes y missense, en 5 familias; 2 con rabdomiosarcoma embrionario | Hanks 2004, PMID 15475955 |
| La mayoría de los pacientes tienen mutaciones en *BUB1B*. Las bialélicas suelen combinar **una mutación sin sentido con un missense en el dominio quinasa**, el mismo tipo de genotipo de nuestro paciente | Sieben 2020, PMID 31738183 (introducción, texto completo) |
| En las familias bialélicas, una mutación truncante se combina con una sustitución, a menudo en el dominio quinasa | Suijkerbuijk 2010, PMID 20516114 (texto completo) |
| Mutaciones monoalélicas de *BUB1B* + un alelo hipomórfico en familias japonesas con separación prematura de cromátidas (PCS) | Matsuura 2006, PMID 16411201 |
| Ese alelo hipomórfico resultó ser una variante intergénica 44 kb antes de *BUB1B* que reduce su transcripción | Ochiai 2014, PMID 24344301 |
| Una variante homocigota de empalme en *BUB1B* causa MVA con cánceres gastrointestinales en el adulto | Rio Frio 2010, PMID 21190457 |
| Heterogeneidad clínica: los pacientes bialélicos tienen un fenotipo moderado; los monoalélicos, más grave (Dandy-Walker, cataratas, Wilms) | García-Castillo 2008, PMID 18548531* |
| Otros genes de MVA: *CEP57* y *TRIP13* | Santos-Simarro 2021, PMID 34500087 · Yost 2017, PMID 28553959 |

## 4. El dato central: en el MVA bialélico falta proteína, no función

Suijkerbuijk et al. 2010 estudiaron células de pacientes con MVA bialélico y reemplazaron BUBR1 por cada mutante en líneas humanas. Sus hallazgos, leídos en el texto completo:

- Las células de los pacientes tienen el checkpoint débil, fallos de alineamiento cromosómico y **poca BUBR1 total**. Expresar BUBR1 normal corrige el defecto: la causa es BUBR1.
- Las mutaciones caen en dos clases: las que **bajan la cantidad de proteína** y las que dañan una función concreta.
- **Todas las sustituciones en el dominio quinasa o cerca de él** (I909T, L1012P, R814H, R727C, L844F) bajan la proteína entre 5 y 10 veces. El ARNm es normal: la proteína se pliega mal y se degrada más rápido (unas 2 veces más recambio).
- Esas proteínas mutantes **dependen de la chaperona HSP90** para plegarse. Inhibir HSP90 (geldanamicina) baja aún más sus niveles; inhibir el proteasoma (MG132) los recupera en parte.
- **Si se fuerza la expresión de I909T o L1012P hasta niveles normales, el checkpoint se recupera por completo.** El problema de estos mutantes es la cantidad, no la función.
- Las proteínas truncadas no se detectan en las células de los pacientes, lo que concuerda con el NMD.
- Excepción: Q921H, también en el dominio, se comportó como la proteína normal. No todo missense del dominio es dañino.

**Qué implica para nuestro paciente.** p.Asn1002Lys está en el mismo dominio, a 10 residuos de L1012P, y el cálculo de estabilidad predice que lo desestabiliza de forma moderada (ΔΔG +1,5 kcal/mol, frente a +3,1 de L1012P; `01_variante_causante.md`, sección 3). La hipótesis más fuerte es que pertenece a la clase "inestable": el paciente tendría **poca BUBR1, toda procedente del alelo 2**. Es una hipótesis comprobable (Western blot de BUBR1 en células del paciente, con y sin MG132) y **no cuenta como evidencia ACMG** para el alelo 2, porque se trata de otros residuos.

**Qué implica para los fármacos (área C).**
- Una estrategia que **aumente la cantidad de BUBR1 mutante** podría compensar el defecto, según el resultado de sobreexpresión.
- **Los inhibidores de HSP90 serían contraproducentes**: el notebook 05 y el cuaderno 06 proponían HSP90 como diana para "estabilizar" BUBR1, y el dato experimental apunta en sentido contrario. Se retira (sección 9).

## 5. El precedente más cercano a nuestro paciente: X753 / L1012P

Hanks 2004 describió a un paciente con **c.2211insGTTA (proteína truncada en el residuo 753, "X753") + c.3035T>C (p.Leu1012Pro)**. Sieben et al. 2020 lo modelaron en ratón (texto completo):

| | Paciente de Hanks 2004 | Nuestro paciente |
|---|---|---|
| Alelo truncante | c.2211insGTTA, cambio de marco; truncamiento en 753 | c.2210T>G, p.Leu737Ter: **el nucleótido contiguo** |
| Alelo missense | p.Leu1012Pro, pseudoquinasa | p.Asn1002Lys, pseudoquinasa, a 10 residuos |
| ΔΔG predicho del missense | +3,1 kcal/mol | +1,5 kcal/mol |
| Evolución | Murió a los 3,6 meses, con retraso del crecimiento y anomalías en corazón, pulmón, cerebro, ojo, tiroides y eritrocitos | Sobrevivió y desarrolló rabdomiosarcoma |

En ratón, la combinación equivalente (X753/L1002P) muere antes del día embrionario 13,5. **Lectura:** el genotipo de nuestro paciente tiene la misma arquitectura que un caso publicado, y un missense menos desestabilizante encajaría con un cuadro menos letal. Es una comparación de un solo caso y un solo predictor, así que se presenta como hipótesis.

> Nomenclatura (pendiente de la versión anterior, resuelta): **L1012P es la numeración humana** (c.3035T>C); L1002P es la posición equivalente en el ratón.

## 6. Cuánta BUBR1 hace falta: los modelos de ratón

| Nivel de BUBR1 | Genotipo de ratón | Resultado | Fuente |
|---|---|---|---|
| 0 % | BubR1–/– | Letal en el embrión temprano (antes de E8,5) | Wang 2004, PMID 14576056; Baker 2004 (según Sieben 2020) |
| ~5 % | BubR1–/H | Mueren el primer día de vida | Baker 2004, PMID 15208629 (según Sieben 2020) |
| ~10 % | BubR1H/H | Viables, con envejecimiento precoz: enanismo, cataratas, pérdida de grasa, infertilidad, aneuploidía progresiva | Baker 2004 |

**Esto respalda la hipótesis que estaba sin fuente:** la pérdida total de BUBR1 es incompatible con la vida, al menos en ratón. Por eso un paciente viable con un alelo nulo necesita que el otro alelo produzca algo de proteína funcional, que es el papel esperado de p.Asn1002Lys como alelo **hipomórfico**.

**Senescencia y mTORC1:**
- En ratones BubR1H/H, eliminar las células senescentes p16-positivas retrasa los trastornos del envejecimiento (Baker 2011, PMID 22048312). Es la base de la línea de **senolíticos** (área C), con evidencia solo en ratón.
- Los portadores de X753 (un solo alelo) desarrollan sarcopenia con **mTORC1 hiperactivo** en el músculo, y los portadores de L1002P no, aunque ambos tienen niveles similares de BUBR1 (Sieben 2020). Los autores sugieren que mTORC1 impulsa esa sarcopenia y citan que la rapamicina frena el deterioro por edad en ratones. Conecta con la **atrofia muscular** del paciente y con la línea de mTOR, pero el efecto depende del alelo concreto.
- Los portadores heterocigotos de alelos de MVA tienen más aneuploidía y PCS que los ratones normales (Sieben 2020). Encaja con la idea de que los padres portadores podrían tener más embriones aneuploides, sin demostrarla.

## 7. Rabdomiosarcoma y tratamiento

- Con un veneno del huso (STLC), la mitad de las células de pacientes con MVA salen de la mitosis en 68–114 minutos, mientras que las células control quedan detenidas (Suijkerbuijk 2010). **Un checkpoint débil cambia la respuesta a los antimitóticos.** La vincristina, base del tratamiento del rabdomiosarcoma, es un antimitótico; el efecto en el paciente (más toxicidad, menos eficacia o ninguna diferencia) es una pregunta abierta para el área C.
- Hay un caso de rabdomiosarcoma en un paciente con MVA/PCS tratado con quimioterapia de intensidad reducida (Nishitani-Isa 2019, PMID 31184400)*.

## 8. NMD

La regla clásica indica que un codón de parada a más de 50–55 nt antes de la última unión exón-exón activa el NMD (Nagy y Maquat 1998, PMID 9644970). Lindeboom et al. 2016 (PMID 27618451) estudian sus reglas en cáncer. La aplicación al alelo 1 está en `01_variante_causante.md`, sección 4. Que las proteínas truncadas no se detecten en células de pacientes con MVA (Suijkerbuijk 2010) es coherente con esta predicción.

## 9. Afirmaciones del notebook 05: estado final

| Afirmación | Estado |
|---|---|
| BUBR1 es el "componente catalítico" del MCC | Retirada: es una pseudoquinasa y su función inhibidora está en el N-terminal |
| La pseudoquinasa interacciona con p31^comet | Retirada: sin fuente verificada |
| ~50 % de los casos de MVA son *BUB1B* | Reemplazada por "la mayoría de los pacientes" (Sieben 2020); no encontramos una cifra fiable |
| Pérdida total de BUBR1 incompatible con la vida | **Respaldada en ratón** (sección 6) |
| Progenitores portadores explicarían los abortos recurrentes | Hipótesis compatible con los ratones portadores (sección 6) y con familias con pérdida gestacional recurrente y variantes heterocigotas de *BUB1B* (Wei 2026, PMID 42434306); sin datos de los padres |
| HSP90 como diana para "estabilizar" BUBR1 | **Retirada:** inhibir HSP90 baja aún más los mutantes del dominio quinasa (sección 4) |
| Citas de Malureanu 2009, Elowe 2012, Rivero 2016, Simonetti 2019 y Holland y Cleveland 2012 | Retiradas: no aparecen en PubMed con ese contenido |

## 10. Estado de lectura de las referencias

| Referencia | PMID | Lectura |
|---|---|---|
| Suijkerbuijk et al. 2010, *Cancer Res* 70:4891–900 | 20516114 | Texto completo (PMC2887387) |
| Sieben et al. 2020, *J Clin Invest* 130:171–88 | 31738183 | Texto completo (PMC6934189) |
| Wang et al. 2004, *Blood* 103:1278–85 | 14576056 | Resumen |
| Baker et al. 2004, *Nat Genet* 36:744–9 | 15208629 | Resumen y su descripción en Sieben 2020 |
| Baker et al. 2011, *Nature* 479:232–6 | 22048312 | Resumen |
| Hanks et al. 2004, *Nat Genet* 36:1159–61 | 15475955 | Resumen; sus genotipos se confirman en los textos completos de Sieben 2020 y Suijkerbuijk 2010 |
| García-Castillo et al. 2008, *Am J Med Genet A* 146A:1687–95 | 18548531 | Resumen* (sin acceso abierto) |
| Matsuura et al. 2006, *Am J Med Genet A* 140:358–67 | 16411201 | Resumen |
| Ochiai et al. 2014, *PNAS* 111:1461–6 | 24344301 | Resumen |
| Rio Frio et al. 2010, *N Engl J Med* 363:2628–37 | 21190457 | Resumen |
| Gama Braga et al. 2020, *Cell Rep* 33:108397 | 33207204 | Resumen |
| Suijkerbuijk et al. 2012, *Dev Cell* 22:1321–9 | 22698286 | Resumen |
| Nishitani-Isa et al. 2019, *Pediatr Int* 61:613–6 | 31184400 | Resumen* |
| Zhang et al. 2026, *Commun Biol* 9 | 42477419 | Resumen |
| Santos-Simarro et al. 2021, *Eur J Med Genet* 64:104338 | 34500087 | Resumen |
| Yost et al. 2017, *Nat Genet* 49:1148–51 | 28553959 | Resumen |
| Wei et al. 2026, *Front Endocrinol* 17:1838559 | 42434306 | Resumen |
| Nagy y Maquat 1998, *Trends Biochem Sci* 23:198–9 | 9644970 | Resumen |
| Lindeboom et al. 2016, *Nat Genet* 48:1112–8 | 27618451 | Resumen |

\* Sin acceso abierto. Para el informe bastan los datos citados; si alguien del equipo tiene acceso institucional, conviene leer Hanks 2004 (tabla de mutaciones y fenotipos).
