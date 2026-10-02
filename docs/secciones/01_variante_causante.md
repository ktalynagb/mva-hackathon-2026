# 01 · Variante causante: evidencia y clasificación ACMG

**Tareas A2 y B2 · borrador para revisión** · Datos al 2 de octubre de 2026
Fuentes: VCF del paciente (GRCh38) · gnomAD v4 · CADD v1.7 · myvariant.info (dbNSFP, ClinVar) · Ensembl (ENST00000287598) · UniProt O60566

## 1. Conclusión en tres líneas

- Alelo 1, **p.Leu737Ter**: variante de pérdida de función con NMD predicho. Clasificación: **Probablemente patogénica** con nuestros criterios (9 puntos) y reportada como **Patogénica** en ClinVar por un solo remitente.
- Alelo 2, **p.Asn1002Lys**: ultra-rara, pero la evidencia computacional discrepa. Con criterios ACMG estrictos es una **VUS** (1 a 2 puntos).
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

## 5. Interpretación combinada

El paciente es heterocigoto para una variante probablemente patogénica de pérdida de función y para una variante rara de significado incierto en el mismo gen, cuya enfermedad recesiva (MVA1) encaja con el fenotipo. Es un genotipo típico de MVA1 si ambas están en *trans*: un alelo nulo más un alelo hipomórfico, porque la pérdida total en los dos alelos probablemente sería incompatible con la vida (hipótesis a verificar en B1).

Si estuvieran en *cis*, el paciente tendría un alelo normal y no explicaría la enfermedad. Como el cuadro clínico es grave, *trans* es mucho más probable, pero no está demostrado.

## 6. Limitaciones

1. **Fase sin resolver.** Las variantes están a 10,9 kb. Las lecturas cortas no las abarcan y los registros del VCF no traen etiquetas de fase (`PGT`/`PID`). El dataset no incluye a los padres.
2. **Alelo 2 sin evidencia funcional.** Su clasificación depende de predictores que discrepan.
3. **NMD no medido** (sección 4).
4. **ClinVar del alelo 1** viene de un único remitente. Conviene revisar los detalles del registro 533901.
5. **Diagnóstico diferencial pendiente** (tarea A3): descartar *CEP57*, *TRIP13* y el resto del panel.

## 7. Qué lo confirmaría

- Genotipar a los padres (Sanger o panel dirigido) para establecer la fase.
- RT-PCR del alelo 1 para demostrar el NMD.
- Ensayo funcional de p.Asn1002Lys (estabilidad de BUBR1 y señal del SAC en fibroblastos del paciente).
- Cariotipo o FISH que muestre aneuploidías en mosaico.

## 8. Referencias por verificar (tarea B1)

Hanks et al. 2004, *Nat Genet* · Tavtigian et al. 2020, *Hum Mutat* · Pejaver et al. 2022, *Am J Hum Genet* · Richards et al. 2015, *Genet Med* (guía ACMG/AMP) · Abou Tayoun et al. 2018, *Hum Mutat* (PVS1). Citadas de memoria; comprobar autores, volumen y páginas antes del informe.
