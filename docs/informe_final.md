# Reposicionamiento de fármacos para la aneuploidía variegada en mosaico por *BUB1B*: de la variante al mecanismo

**MVA Hackathon 2026 · Track 2** · Equipo: [nombre] · Repositorio: https://github.com/ktalynagb/mva-hackathon-2026
**Estado: borrador v0 (8 oct).** Tareas E2 (plantilla) y E5 (integración, Hito H5, 21 oct). Exportar a PDF como `<usuario>_track2_report.pdf`.

> **Cómo se usa este archivo.** Cada sección dice de qué archivo sale y quién la cierra. Los bloques `[PENDIENTE]` se rellenan cuando la tarea de origen se fusiona. Las secciones de origen pueden ser más largas: aquí va la versión resumida. Antes de exportar, borrar estas notas y las líneas "Fuente/Tarea".

---

## Resumen

[PENDIENTE · E5 · máximo 200 palabras, se escribe al final]
Un paciente pediátrico con rabdomiosarcoma, nefrocalcinosis, restricción grave del crecimiento intrauterino y talla baja porta dos variantes en *BUB1B*: una de parada prematura (p.Leu737Ter) y una missense en la pseudoquinasa (p.Asn1002Lys). Proponemos que el mecanismo es un alelo nulo más un alelo hipomórfico inestable, es decir, **poca BUBR1** y un checkpoint mitótico débil. A partir de ese mecanismo priorizamos fármacos aprobados en [N] líneas terapéuticas: [lista corta].

## 1. Introducción

*Fuente: `docs/secciones/02_marco_biologico.md` (secciones 1 y 3) · Tarea: B1*

- Qué es el MVA: enfermedad recesiva rara con aneuploidías en mosaico, retraso del crecimiento, microcefalia y predisposición a cáncer infantil (Hanks 2004).
- Genes: *BUB1B* (la mayoría de los casos), *CEP57*, *TRIP13* (Sieben 2020).
- El checkpoint mitótico y el papel de BUBR1 en el MCC, en un párrafo.
- El caso: fenotipo en términos HPO (rabdomiosarcoma HP:0002859, nefrocalcinosis HP:0000121, talla baja HP:0004322, falla de medro HP:0001508, atrofia muscular HP:0003202, prematuridad HP:0001622, pequeño para la edad gestacional HP:0001518; abortos recurrentes en los progenitores HP:0200067).
- Pregunta del trabajo: ¿qué mecanismo explica la enfermedad y qué fármacos aprobados podrían actuar sobre él?

## 2. Métodos

*Fuente: notebooks 01–05, `scripts/` · Tareas: A1, A3, B3, C3, E8*

### 2.1 Datos
VCF de genoma completo del paciente (GRCh38; Sentieon Haplotyper + GATK VariantFiltration) y documento clínico, del dataset `SageBio/mva-hackathon-2026-data`. No se usaron las lecturas crudas. Los datos no salen del equipo ni se suben al repositorio.

### 2.2 Identificación de la variante
1. Filtrado de variantes PASS en un panel de 290 genes de mitosis, cinetocoro, centrosoma, cohesina, lámina y poro nuclear, cromatina, reparación de ADN y ciclo celular (`config/genes_candidatos.txt`).
2. Frecuencia en gnomAD v4 (raras: AF < 1 %), consecuencia con Ensembl VEP en el transcrito **MANE Select**, CADD v1.7, ClinVar y predictores de dbNSFP.
3. Patrón recesivo: homocigota o dos heterocigotas en el mismo gen.
4. Clasificación ACMG/AMP con el sistema de puntos (Richards 2015; Tavtigian 2020; Abou Tayoun 2018; Pejaver 2022).
5. Análisis de sensibilidad con las variantes que no pasaron el filtro de calidad (notebook 02b).

### 2.3 Caracterización del mecanismo
- NMD por la regla de 50–55 nt (Nagy y Maquat 1998).
- Estructura: modelo de AlphaFold de BUBR1, entorno del residuo, accesibilidad y nucleótidos colocados por homología (AlphaFill).
- Estabilidad: ΔΔG con ThermoMPNN (Dieckhaus 2024) para todas las sustituciones del dominio.
- Revisión bibliográfica con verificación de cada cita en PubMed.

### 2.4 Priorización de fármacos
[PENDIENTE · C3, C4] Consulta a DGIdb v5 y Open Targets, comprobación de aprobación en Drugs@FDA y en la EMA, y puntuación con la matriz de `docs/secciones/03_criterios.md` (filtros de exclusión + 6 criterios ponderados).

### 2.5 Reproducibilidad
[PENDIENTE · D2, D3] Comando único, versiones fijadas y tiempo de ejecución.

### 2.6 Uso de herramientas de IA
El reto exige declarar **proveedor, plan o nivel y configuración de datos** de cada herramienta. [PENDIENTE · E8: cada persona completa su fila]

| Herramienta | Proveedor | Plan o nivel | Configuración de datos (¿se usan para entrenar?) | Para qué se usó | ¿Recibió datos del paciente? | Quién |
|---|---|---|---|---|---|---|
| Claude Code (Sonnet y Opus) | Anthropic | Pro | Términos de consumidor; "Help improve Claude" desactivado (no se entrena con los chats) | Código de análisis, consultas a APIs, revisión de literatura, redacción de borradores | Sí, salidas a nivel de variante (posiciones, alelos, lecturas); los archivos de datos quedan en la computadora local | Ktalyna |
| Claude Code | Anthropic | [completar] | [completar] | [completar] | [completar] | Laura |
| Gemini (vía LangChain, cuaderno 06) | Google | [completar] | [completar] | Primer borrador de fármacos (descartado como lista final) | [completar] | [completar] |
| [otra] | | | | | | |

Todas las afirmaciones generadas con IA se verificaron contra la fuente primaria (PubMed, Drugs@FDA, gnomAD, UniProt). Las citas que no se pudieron verificar se retiraron (`02_marco_biologico.md`, sección 9).

## 3. Resultados

### 3.1 Variante causante

*Fuente: `docs/secciones/01_variante_causante.md` · Tareas: A1–A4 · Figura: A5 (lollipop)*

| | Alelo 1 | Alelo 2 |
|---|---|---|
| Cambio | c.2210T>G · p.Leu737Ter | c.3006T>G · p.Asn1002Lys |
| Consecuencia | Parada prematura, exón 17 de 23; NMD predicho | Missense en la pseudoquinasa |
| gnomAD v4 | AF 7,9×10⁻⁵, 0 homocigotos | 1 alelo (6,8×10⁻⁷), 0 homocigotos |
| Calidad de la llamada | PASS, fracción alélica 0,54, GQ 99 | PASS, fracción alélica 0,46, GQ 99 |
| ACMG | Probablemente patogénica (9 puntos); ClinVar: patogénica | VUS inclinada a patogénica (1–2 puntos) |

- **Diagnóstico diferencial:** *BUB1B* es el único de los 290 genes del panel con dos variantes raras funcionales en el transcrito MANE. *CEP57*, *TRIP13* y *MAD2L1BP* no tienen ninguna. Anotar en MANE descartó 5 de 18 alertas que solo eran graves en transcritos secundarios; una de ellas daba un falso patrón recesivo en *SYNE2*.
- **Limitación principal:** sin muestras de los padres no se puede demostrar que las variantes estén en alelos distintos (*trans*).
![Figura 1](../results/figura_1_bubr1_variantes.png)

**Figura 1. BUBR1 con las variantes del paciente y las variantes de MVA caracterizadas.** Arriba, las dos variantes del paciente: p.Leu737Ter (bermellón, truncante) y p.Asn1002Lys (azul, missense en la pseudoquinasa). Abajo, variantes de pacientes con MVA estudiadas en células por Suijkerbuijk et al. 2010, separadas según bajen la cantidad de BUBR1 o no. Las líneas punteadas alinean las variantes del paciente con las publicadas: p.Leu737Ter cae entre los truncamientos 731X y 753X, y p.Asn1002Lys junto a L1012P, en la región donde los missense reducen la proteína. Dominios: UniProt O60566 y Zhang et al. 2026. Generada con `scripts/figuras_informe.py`.

### 3.2 Mecanismo biológico

*Fuente: `docs/secciones/02_marco_biologico.md`, `02b_resumen_mecanismo.md` · Tareas: B1–B5 · Figura: B5*

- **Pérdida de función por falta de proteína.** El alelo 1 no produce proteína (NMD). El alelo 2 cae en la pseudoquinasa, donde todos los missense de MVA estudiados reducen BUBR1 de 5 a 10 veces por mal plegamiento, y llevarlos a niveles normales restaura el checkpoint (Suijkerbuijk 2010).
- **Estructura y estabilidad de N1002K:** residuo enterrado (pLDDT 91), con 3 enlaces de hidrógeno que la lisina no puede formar; ΔΔG +1,5 kcal/mol (percentil 72–75 del dominio), la mitad que la variante conocida de MVA p.Leu1012Pro (+3,1). No toca el bolsillo de ATP (a 29 Å).
- **Precedente más cercano:** un paciente con truncamiento en el codón 753 y p.Leu1012Pro (Hanks 2004; modelado por Sieben 2020). Mismo tipo de genotipo y misma región; ese paciente murió a los 3,6 meses.
- **Consecuencia:** checkpoint débil → reparto erróneo de cromosomas → aneuploidía en mosaico → senescencia y envejecimiento precoz (talla baja, atrofia muscular, posible mTORC1) e inestabilidad cromosómica (rabdomiosarcoma).
![Figura 2](../results/figura_2_via_mecanismo.png)

**Figura 2. Del genotipo al fenotipo.** Los dos alelos convergen en poca BUBR1, lo que debilita el checkpoint mitótico y produce aneuploidía en mosaico. De ahí salen dos ramas: senescencia (con mTORC1 hiperactivo en ratón), que explicaría el retraso del crecimiento y la atrofia muscular, e inestabilidad cromosómica, que lleva al rabdomiosarcoma. En verde, el punto de acción de cada línea terapéutica; en recuadros punteados, las dos advertencias. Las etiquetas en cursiva indican el nivel de evidencia de cada paso. La nefrocalcinosis no tiene un mecanismo establecido y no se incluye. Generada con `scripts/figuras_informe.py`.

### 3.3 Candidatos de reposicionamiento

*Fuente: `docs/secciones/04_candidatos.md` · Tareas: C2–C6 · Hito H4, 17 oct*

[PENDIENTE] Tabla de 3 a 5 fármacos: mecanismo, línea terapéutica, aprobación, seguridad pediátrica, evidencia, riesgos, puntaje y experimento de validación.

Líneas en evaluación (`02b`): (1) subir la cantidad de BUBR1 mediante proteostasis, (2) frenar mTORC1, (3) senolíticos, (4) tratar el tumor sin empeorar la aneuploidía. Quedan excluidos los inhibidores de HSP90, PLK1, Aurora y MPS1.

## 4. Discusión

[PENDIENTE · E5]
- **Lo más sólido y lo más débil:** la fase *trans* no está demostrada, el alelo 2 es VUS y la priorización de fármacos se apoya en datos preclínicos.
- **Innovación:** tratar el MVA bialélico como una enfermedad de proteína mal plegada, y evitar las dianas que empeorarían el checkpoint.
- **Impacto clínico:** qué candidato podría probarse primero y cómo (fibroblastos del paciente).
- **Escalabilidad:** el mismo pipeline sirve para otros pacientes con MVA cambiando el VCF y la lista de genes [D5].
- **Próximos pasos:** genotipar a los padres, RT-PCR del alelo 1, Western blot de BUBR1 con y sin MG132, cariotipo.

## 5. Referencias

[PENDIENTE · E5] Reunir las de `01_variante_causante.md` (sección 9), `02_marco_biologico.md` (sección 10) y `04_candidatos.md`. Formato: Autor et al. Año. *Revista* volumen:páginas. PMID.

---

## Guía de estilo (E2)

**Texto**
- Español neutro, frases cortas y voz activa. El nombre del gen en cursiva (*BUB1B*) y la proteína en redonda (BUBR1).
- Variantes en HGVS con el transcrito la primera vez: `ENST00000287598: c.2210T>G (p.Leu737Ter)`.
- Separar siempre lo demostrado de lo predicho y de la hipótesis. Usar "predicho", "compatible con" o "hipótesis" cuando corresponda.
- Nada que pueda identificar al paciente o a su familia: sin fechas, lugares, nombres ni fotos.

**Figuras**
- Paleta apta para daltonismo (Okabe-Ito): azul `#0072B2`, naranja `#E69F00`, verde `#009E73`, bermellón `#D55E00`, gris `#999999`. **Alelo 1 = bermellón, alelo 2 = azul** en todas las figuras.
- Fuente sin serifa (Arial o DejaVu Sans), de 9 a 11 pt en el tamaño final.
- PNG a 300 ppp en `results/figura_<n>_<tema>.png`, generadas por código del repositorio.
- Pie de figura: qué muestra, de dónde salen los datos y qué script la genera.

**Tablas:** como máximo 6 columnas en el PDF; los detalles van en el repositorio.
