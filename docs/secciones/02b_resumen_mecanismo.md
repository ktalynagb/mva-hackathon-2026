# 02b · Resumen del mecanismo para elegir fármacos (Hito H2)

**Tarea B4 · versión para revisión** · 8 de octubre de 2026 · Para el área C
Base: `01_variante_causante.md` y `02_marco_biologico.md`, donde están las fuentes. Este resumen reemplaza la sección 6 del notebook 05 y su `resumen_mecanismo_para_R4.json`, que tenían errores (ver el final).

## Qué está roto

| | Alelo 1 · p.Leu737Ter | Alelo 2 · p.Asn1002Lys |
|---|---|---|
| Qué produce | Nada: el ARNm se degrada por NMD (predicho) | Una BUBR1 completa con un cambio en la pseudoquinasa |
| Efecto esperado | Alelo nulo | Proteína **menos estable**: se pliega peor y se degrada antes (ΔΔG +1,5; precedente de otros missense del mismo dominio) |
| Seguridad | Probablemente patogénica | VUS inclinada a patogénica |

**En una frase:** el paciente tendría **poca BUBR1**, toda del alelo 2, y probablemente funcional en lo que queda. La enfermedad es un problema de **cantidad** de proteína, no de una función perdida.

## La cadena causal

```
poca BUBR1  →  checkpoint mitótico débil  →  errores al repartir cromosomas  →  aneuploidía en mosaico
                                                                                  ├─ células senescentes → envejecimiento precoz, talla baja, atrofia muscular (mTORC1)
                                                                                  └─ inestabilidad cromosómica → cáncer (rabdomiosarcoma)
```

## Qué puede hacer un fármaco: cuatro líneas y dos advertencias

Los fármacos son **ejemplos para que el área C los verifique** con la matriz de C1 (`03_criterios.md`). La columna "Aprobado" se comprobó en Drugs@FDA el 8 oct.

| Línea | Lógica | Evidencia que la respalda | Ejemplos (aprobado FDA) | Nivel |
|---|---|---|---|---|
| **1. Subir la cantidad de BUBR1** (proteostasis) | Si el mutante del dominio quinasa se lleva a niveles normales, el checkpoint se recupera | Suijkerbuijk 2010, en células: sobreexpresión de I909T y L1012P | Arimoclomol (amplifica la respuesta de choque térmico; Niemann-Pick C, ≥ 2 años) · fenilbutirato sódico (chaperona química; trastornos del ciclo de la urea) | Hipótesis **innovadora**: nadie lo ha probado con BUBR1 |
| **2. Frenar mTORC1** | La atrofia muscular de los ratones portadores de un alelo truncante se asocia a mTORC1 hiperactivo | Sieben 2020, en ratón; dependiente del alelo | Sirolimus · everolimus · temsirolimus | Mecanismo plausible; ojo: son inmunosupresores |
| **3. Eliminar células senescentes** (senolíticos) | Quitar las células senescentes retrasa el envejecimiento precoz en ratones con poca BubR1 | Baker 2011, por eliminación genética, no con un fármaco | Dasatinib (Ph+ LMC/LLA, también pediátrico desde 1 año) | Evidencia indirecta |
| **4. Tratar el tumor sin empeorar la aneuploidía** | El rabdomiosarcoma es lo que amenaza la vida | Temsirolimus + quimio: mejor supervivencia en recaída (fase II, Mascarenhas 2019, PMID 31513481), sin beneficio en riesgo intermedio (fase III, Gupta 2024, PMID 38936378) | Temsirolimus (une las líneas 2 y 4) | Datos clínicos en rabdomiosarcoma, no en MVA |

**Advertencias para cualquier candidato**
- ❌ **No inhibir HSP90.** Los mutantes del dominio quinasa dependen de HSP90 para plegarse; inhibirla baja todavía más la BUBR1 (Suijkerbuijk 2010).
- ⚠️ **Cuidado con los antimitóticos.** Las células con MVA salen antes de la mitosis frente a venenos del huso. La vincristina es la base del tratamiento del rabdomiosarcoma: conviene discutir intensidad y vigilancia (hay un caso tratado con quimioterapia de intensidad reducida, Nishitani-Isa 2019). Fármacos que debiliten aún más la mitosis en células normales (inhibidores de PLK1, Aurora o MPS1) son de riesgo, y además no están aprobados.

**Descartados por ahora:** *readthrough* de codones de stop (ataluren no tiene aprobación de la FDA, y el ARNm del alelo 1 se degradaría igual por NMD); inhibidores de APC/C o CDC20 (solo herramientas de laboratorio).

## Errores del notebook 05 que este resumen corrige

| Decía | Corrección |
|---|---|
| "Moduladores de Hsp90 podrían estabilizar el alelo missense", con geldanamicina y 17-AAG | Son inhibidores de HSP90: **bajan** la BUBR1 mutante |
| Volasertib "aprobado en Europa para LMA" | No está aprobado (ni FDA ni EMA) |
| "Potenciar Aurora B" con barasertib | Barasertib **inhibe** Aurora B y no está aprobado |
| Inhibidores de APC/C y CDC20 como dianas | Sin fármacos aprobados |
| Efecto molecular: "haploinsuficiencia compuesta" | Alelo nulo + alelo hipomórfico inestable |

## Qué necesita el área C de aquí

1. Puntuar las cuatro líneas con la matriz de C1 y buscar más ejemplos en DGIdb y Open Targets (C3).
2. Para la línea 1: buscar si arimoclomol o el fenilbutirato se han probado con otras proteínas mal plegadas por un missense; eso define su solidez.
3. Para el informe: una frase sobre cómo se validaría cada candidato (por ejemplo, nivel de BUBR1 y checkpoint en fibroblastos del paciente tratados con el fármaco).
