# 02 · Marco biológico: BUBR1, el checkpoint mitótico y el MVA

**Tarea B1 · borrador para revisión** · 2 de octubre de 2026
Todas las referencias se comprobaron en PubMed. Marcamos con * las que solo se leyeron en resumen; para el informe final conviene leer el texto completo de las más importantes.

## 1. Idea central en cinco líneas

1. Antes de dividirse, la célula comprueba que cada cromosoma esté bien anclado al huso. Esa vigilancia es el **checkpoint mitótico (SAC)**.
2. BUBR1, la proteína de *BUB1B*, forma parte del complejo que frena la división mientras haya cromosomas mal anclados: el **MCC** (BUBR1, BUB3, MAD2 y CDC20).
3. Si hay poca BUBR1 funcional, el freno falla, la célula se divide antes de tiempo y reparte mal los cromosomas.
4. El resultado es **aneuploidía en mosaico** (MVA): células con cromosomas de más o de menos en distintos tejidos.
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
| Pseudoquinasa | 766–1050 | Pseudoquinasa inusual: no necesita catalizar, pero sus residuos de unión a ATP sostienen su forma. Favorece el reclutamiento de PP2A-B56 |

**¿Dónde se unen MAD2 y CDC20?** En el extremo N-terminal y la región central, no en la pseudoquinasa. MAD2 se une al dominio TPR (los residuos 1–220 bastan en ensayos de unión, y los residuos que lo median quedan antes de la caja KEN1; estructura PDB 6TLJ). CDC20 se une a los motivos KEN, ABBA y cajas D de esa región. Esa zona es en gran parte desordenada, salvo el TPR; la pseudoquinasa es el otro dominio estructurado (Zhang 2026, PMID 42477419). La pseudoquinasa sí es una plataforma de interacción, pero con otros socios (PP2A-B56) y su efecto sobre el MCC sería indirecto.

**Consecuencia para el caso.** p.Leu737Ter corta la proteína antes de la pseudoquinasa, así que un producto truncado conservaría los sitios de unión a MAD2 y CDC20 y perdería PP2A-B56. Con NMD predicho, ese producto no debería existir. En p.Asn1002Lys, el efecto previsto es sobre la estabilidad del dominio y el reclutamiento de PP2A-B56, no sobre la unión directa a MAD2/CDC20.

**Dónde caen las variantes del paciente**
- **p.Leu737Ter** (residuo 737): después de TPR, KEN, cajas D, GLEBS y KARD, y antes de la pseudoquinasa. Un producto truncado conservaría esos elementos y perdería toda la pseudoquinasa. Con NMD predicho (`01_variante_causante.md`, sección 4), lo esperable es que no se produzca proteína de este alelo.
- **p.Asn1002Lys** (residuo 1002): dentro de la pseudoquinasa.

> Corrección: el notebook 05 mostraba una tabla de dominios con coordenadas de memoria (GLEBS 430–480, TPR "×8" 60–400, pseudoquinasa desde 780). No coincidían con las fuentes y se reemplazaron.

## 3. MVA y *BUB1B*

| Hallazgo | Fuente |
|---|---|
| Primeras mutaciones bialélicas de *BUB1B* en MVA: truncantes y missense, en 5 familias, 2 de ellas con rabdomiosarcoma embrionario | Hanks 2004, PMID 15475955 |
| Mutaciones monoalélicas de *BUB1B* en familias con separación prematura de cromátidas y fallo del checkpoint | Matsuura 2006, PMID 16411201 |
| Heterogeneidad clínica y genética del MVA, con subtipos clínicos* | García-Castillo 2008, PMID 18548531 |
| Análisis de *BUB1B* y CGH en cánceres infantiles asociados a MVA* | Hanks 2006, PMID 16182441 |
| Otros genes de MVA: *CEP57* (revisión de casos) y *TRIP13* (tumor de Wilms) | Santos-Simarro 2021, PMID 34500087 · Yost 2017, PMID 28553959 |

**Sobre el genotipo del paciente.** Hanks 2004 describe mutaciones truncantes y missense en *BUB1B*, así que un alelo truncante más uno missense encaja con lo publicado. La idea de que la pérdida total en los dos alelos sería incompatible con la vida **no la hemos podido respaldar con una fuente** y se mantiene solo como hipótesis.

## 4. Un dato directamente útil: BUBR1 p.Leu1012Pro

Sieben et al. 2020 (PMID 31738183)* reproducen en ratón una variante humana de MVA, **BUBR1 p.Leu1012Pro**, y la combinan con un alelo truncante (X753) y con uno hipomórfico (H). Según el resumen:
- Los ratones con truncante + L1002P (equivalente murino) y con H + truncante murieron de forma prematura.
- Los ratones H/L1002P sobrevivieron y tuvieron rasgos de MVA: predisposición al cáncer, enanismo, lipodistrofia, sarcopenia y baja tolerancia al estrés cardíaco.
- Los efectos dependen del alelo concreto, más allá de la cantidad total de BUBR1 y de la aneuploidía; la sarcopenia se asoció a hiperactividad de mTORC1.

Ojo con la numeración: L1002P es la posición en el ratón; en humano es L1012P. No es el residuo N1002 del paciente.

Relevancia para el caso:
1. L1012 está a **10 residuos de N1002**, dentro de la misma pseudoquinasa. Es un cambio missense en esa región con efecto demostrado en un modelo, lo que da contexto a p.Asn1002Lys. **No cuenta como evidencia ACMG** para el alelo 2, porque es otro residuo.
2. La asociación sarcopenia–mTORC1 conecta con la **atrofia muscular** del paciente y con la línea del mTOR para el área de fármacos (C2).

## 5. Modelos de ratón y envejecimiento

- Ratones con BubR1 reducido muestran envejecimiento precoz e infertilidad (Baker 2004, PMID 15208629).
- Eliminar las células senescentes p16-positivas retrasa trastornos asociados al envejecimiento en ratones BubR1 (Baker 2011, PMID 22048312). Es la base de la línea de **senolíticos** que se explorará en el área C. Es evidencia en ratón, con un modelo distinto al del paciente.

## 6. Rabdomiosarcoma y tratamiento

Hay un caso de rabdomiosarcoma en un paciente con MVA/PCS tratado con quimioterapia de intensidad reducida (Nishitani-Isa 2019, PMID 31184400)*. Es un punto a leer completo en el área C: un checkpoint débil podría cambiar la tolerancia o la respuesta a los antimitóticos.

## 7. NMD

La regla clásica indica que un codón de parada a más de 50–55 nt antes de la última unión exón-exón activa el NMD (Nagy y Maquat 1998, PMID 9644970). Lindeboom et al. 2016 (PMID 27618451) estudian sus reglas en cáncer. La aplicación al alelo 1 está en `01_variante_causante.md`, sección 4.

## 8. Afirmaciones del notebook 05 que se retiraron o quedan como hipótesis

| Afirmación | Estado |
|---|---|
| BUBR1 es el "componente catalítico" del MCC | Retirada: es una pseudoquinasa |
| La pseudoquinasa interacciona con p31^comet | Retirada: sin fuente verificada |
| ~50 % de los casos de MVA son *BUB1B* | Sin verificar |
| Progenitores portadores explicarían los abortos recurrentes | Hipótesis; no hay datos de los padres |
| Pérdida total de BUBR1 incompatible con la vida | Hipótesis sin fuente |
| Citas de Malureanu 2009, Elowe 2012, Rivero 2016, Simonetti 2019 y Holland y Cleveland 2012 | Retiradas: no aparecen en PubMed con ese contenido |

## 9. Pendiente para B1

- Leer el texto completo de Hanks 2004, Sieben 2020 y García-Castillo 2008.
- Confirmar la nomenclatura de p.Leu1012Pro y qué variantes de MVA caen en la pseudoquinasa.
- Buscar casos con truncante + missense en la pseudoquinasa y su fenotipo.
