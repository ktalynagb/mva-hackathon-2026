# 6. Lista de genes del equipo — modelo dominante (C8)

> **Fecha:** 15 oct 2026 | **Tarea:** C8 | **Script:** `scripts/analisis_genes_equipo.py`  
> **Contexto:** Evaluación de la lista de genes enviada por el equipo (WhatsApp, 9:09 a.m. 15 oct).

---

## 6.1 Genes analizados

De la lista completa del equipo, cuatro genes tienen justificación biológica para un
análisis de **modelo dominante** en este paciente (ver criterio de inclusión en 6.3):

| Gen | Herencia | Enfermedad/rasgo relevante |
|-----|----------|---------------------------|
| **LMNA** | AD (monoalélico) | Emery-Dreifuss tipo 1B, miocardiopatía dilatada familiar, progeria |
| **KMT2D** | AD (monoalélico) | Síndrome Kabuki tipo 1 (microcefalia, talla baja, DI) |
| **KDM6A** | X-linked dominante (mujeres het.) | Síndrome Kabuki tipo 2 |
| **ATM** | Monoalélico: predisposición cáncer / Bialélico: ataxia-telangiectasia | Doble análisis (ver 6.2) |

---

## 6.2 Resultados del embudo dominante

**Script:** `scripts/analisis_genes_equipo.py` → `data/genes_equipo/` (no versionado)

| Paso del embudo | N |
|----------------|---|
| Variantes PASS en los 4 genes | 305 |
| Raras o ausentes de gnomAD (AF < 1%) | 289 |
| Con efecto funcional en algún transcrito | 1 |
| Con efecto funcional en MANE | 1 |
| HET con AF ≤ 1×10⁻⁵ (**umbral dominante**) | **0** |

**Resultado:** ninguna variante pasa el filtro de ultra-rareza (AF ≤ 1×10⁻⁵) requerido
para un diagnóstico dominante grave de inicio pediátrico.

### Detalle por gen

| Gen | Variantes funcionales (MANE) | HET ultra-raras (AF ≤ 1e-5) | Interpretación |
|-----|------------------------------|------------------------------|----------------|
| LMNA | 0 | 0 | Sin variantes candidatas |
| KMT2D | 0 | 0 | Sin variantes candidatas |
| KDM6A | 0 | 0 | Sin variantes candidatas |
| ATM | 1 (missense, AF=0.08%) | 0 | Variante frecuente, no patogénica bajo modelo dominante |

> **Nota privacidad:** la variante encontrada en ATM se documenta solo a nivel de gen/consecuencia/AF
> (no posición ni cambio proteico); el detalle completo está en `data/genes_equipo/`.

### Check bialélico ATM

Solo 1 variante rara funcional en ATM → **patrón bialélico NO detectado**.
El paciente no tiene el fenotipo de ataxia-telangiectasia (ataxia cerebelosa, telangiectasias oculocutáneas,
inmunodeficiencia combinada), por lo que la ausencia de un segundo alelo dañino es consistente.

---

## 6.3 Genes descartados

| Gen | Motivo del descarte |
|-----|---------------------|
| **EZH2** | Síndrome de Weaver = **overgrowth** (macrocefalia, estatura alta). Fenotipo **opuesto** al paciente (microcefalia, restricción del crecimiento). No aplicable. |
| **BRCA1** | Predisposición a cáncer de mama/ovario en **adultos**. No causa fenotipo neonatal ni pediátrico. Sería hallazgo secundario, no causa del cuadro. |
| **BRCA2** | Ídem BRCA1. |
| **PALB2** | Predisposición a cáncer de mama/páncreas (adultos). No aplica como causa primaria. |
| **RAD51C** | Predisposición a cáncer de ovario/mama (adultos). |
| **RAD51D** | Ídem RAD51C. |
| **CHEK2** | Predisposición moderada a cáncer adulto (mama, colon). Sin fenotipo pediátrico dominante. |
| **FANCM** | Anemia de Fanconi biallélica (recesiva). No aplica modelo dominante; habría que analizarlo en modelo recesivo si hay indicación clínica. |
| **LMNB1** | Leucodistrofia por duplicación de LMNB1 (AD), debut adulto. No explica el cuadro actual. |
| **EMD** | Emerinopatía X-linked recesiva (varones), fenotipo principalmente muscular y cardíaco. |
| **NUP155** | Fibrilación auricular familiar (según NORD, patrón recesivo). Sin causa mendeliana dominante con overlap fenotípico. |
| **RANBP2** | Encefalitis aguda necrotizante (AD en contexto de infección febril). No causa del cuadro crónico. |

> **TP53** ya estaba incluido en `config/genes_modelo_dominante.tsv` (paneles de rabdomiosarcoma y
> predisposición a tumores pediátricos) y fue analizado en el modelo dominante anterior (tarea A10).

---

## 6.4 Conclusión

El análisis del modelo dominante para los genes propuestos por el equipo es **negativo**:
ningún gen de la lista tiene una variante ultra-rara (AF ≤ 1×10⁻⁵) con efecto funcional en MANE
que califique como candidata a segundo diagnóstico dominante.

Este resultado es **compatible** con que el MVA por BUB1B (ya confirmado) explica el cuadro principal,
y que no hay un segundo diagnóstico dominante superpuesto en estos genes.

Para el informe:
- EZH2 debe **no mencionarse** o mencionarse explícitamente como descartado.
- BRCA1/2 pueden mencionarse como **hallazgos secundarios no encontrados** (si la política del evento lo requiere).
- KMT2D y LMNA pueden quedar como "evaluados negativamente" en el modelo dominante.

---

## 6.5 Mensaje para el equipo

> **[RESUMEN LISTA DE GENES — C8]**
>
> Corrí el modelo dominante para los genes de la lista. Resultado:
>
> **Se analizaron:** LMNA, KMT2D, KDM6A, ATM.
> **Resultado:** ninguna variante ultra-rara (AF ≤ 1e-5) con efecto funcional. Negativo.
>
> **EZH2 → DESCARTAR.** Síndrome de Weaver = overgrowth (paciente tiene lo opuesto: microcefalia + retraso del crecimiento).
>
> **BRCA1/2, PALB2, RAD51C/D, CHEK2 → hallazgos secundarios** (predisposición oncológica adulta, no causa del cuadro).
> Si quieren, los incluimos como "panel de cáncer hereditario secundario" pero no como causa primaria.
>
> **TP53** ya estaba en el modelo anterior → ya analizado.
>
> **ATM:** solo 1 variante frecuente (AF=0.08%), no patogénica. Tampoco hay patrón bialélico para A-T.
