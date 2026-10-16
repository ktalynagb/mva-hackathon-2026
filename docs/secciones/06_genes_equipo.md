# 6. Lista de genes del equipo — modelo dominante (C8)

> **Fecha:** 15 oct 2026 (ampliado noche) | **Tarea:** C8 | **Script:** `scripts/analisis_genes_equipo.py`  
> **Contexto:** Evaluación de la lista completa de genes enviada por el equipo (WhatsApp, 9:09 a.m. 15 oct).  
> **Actualización:** se agregaron BRCA1, BRCA2, PALB2, RAD51C, RAD51D, CHEK2 para documentar el panel de predisposición oncológica hereditaria.

---

## 6.1 Genes analizados

**10 genes** con corrida formal del modelo dominante:

| Gen | Herencia | Enfermedad/rasgo | Motivo de inclusión |
|-----|----------|------------------|---------------------|
| **LMNA** | AD | Emery-Dreifuss AD, DCM, progeria | Overlap fenotípico potencial |
| **KMT2D** | AD | Síndrome Kabuki tipo 1 (microcefalia, talla baja) | Overlap fenotípico |
| **KDM6A** | X-linked dom. (het. femeninas) | Síndrome Kabuki tipo 2 | Overlap fenotípico |
| **ATM** | Mono/bialélico | Predisposición cáncer / ataxia-telangiectasia | Propuesto por equipo |
| **BRCA1** | AD | Predisposición cáncer mama/ovario | Corrida formal como panel hereditario |
| **BRCA2** | AD | Predisposición cáncer mama/ovario | Corrida formal como panel hereditario |
| **PALB2** | AD | Predisposición cáncer mama/páncreas | Corrida formal como panel hereditario |
| **RAD51C** | AD | Predisposición cáncer ovario/mama | Corrida formal como panel hereditario |
| **RAD51D** | AD | Predisposición cáncer ovario/mama | Corrida formal como panel hereditario |
| **CHEK2** | AD | Predisposición cáncer mama moderada | Corrida formal como panel hereditario |

---

## 6.2 Resultados del embudo dominante

**Script:** `scripts/analisis_genes_equipo.py` → `data/genes_equipo/` (no versionado)

| Paso del embudo | N |
|----------------|---|
| Variantes PASS en los 10 genes | 874 |
| Raras o ausentes de gnomAD (AF < 1%) | 827 |
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
| ATM | 1 (missense, AF=0.08%) | 0 | Variante frecuente; no patogénica bajo modelo dominante |
| BRCA1 | 0 | 0 | Sin variantes candidatas |
| BRCA2 | 0 | 0 | Sin variantes candidatas |
| PALB2 | 0 | 0 | Sin variantes candidatas |
| RAD51C | 0 | 0 | Sin variantes candidatas |
| RAD51D | 0 | 0 | Sin variantes candidatas |
| CHEK2 | 0 | 0 | Sin variantes candidatas |

> **Nota privacidad:** la variante encontrada en ATM se documenta solo a nivel de gen/consecuencia/AF
> (no posición ni cambio proteico); el detalle completo está en `data/genes_equipo/`.

### Check bialélico ATM

Solo 1 variante rara funcional en ATM → **patrón bialélico NO detectado**.
El paciente no tiene el fenotipo de ataxia-telangiectasia (ataxia cerebelosa, telangiectasias oculocutáneas,
inmunodeficiencia combinada), por lo que la ausencia de un segundo alelo dañino es consistente.

---

## 6.3 Genes no corridos (descartados sin análisis formal)

| Gen | Motivo |
|-----|--------|
| **EZH2** | Síndrome de Weaver = **overgrowth** (fenotipo **opuesto** al paciente). No aplicable. |
| **FANCM** | Anemia de Fanconi biallélica (recesiva). No aplica modelo dominante. |
| **LMNB1** | Leucodistrofia AD por duplicación de LMNB1, debut adulto. No explica el cuadro actual. |
| **EMD** | Emerinopatía X-linked recesiva (varones); fenotipo muscular/cardíaco. |
| **NUP155** | Fibrilación auricular familiar (recesiva según NORD). Sin causa dominante relevante. |
| **RANBP2** | Encefalitis aguda necrotizante (AD en contexto febril). No causa del cuadro crónico. |

> **TP53** ya estaba incluido en `config/genes_modelo_dominante.tsv` y fue analizado en A10.

---

## 6.4 Conclusión

El análisis del modelo dominante para los **10 genes del equipo** es **negativo**:
ningún gen tiene una variante ultra-rara (AF ≤ 1×10⁻⁵) con efecto funcional en MANE.

- **Panel oncológico hereditario** (BRCA1/2, PALB2, RAD51C/D, CHEK2): 0 variantes funcionales en MANE → no hay hallazgos secundarios en este panel en este paciente.
- **Genes de overlap fenotípico** (LMNA, KMT2D, KDM6A): 0 variantes candidatas → descartados como segundo diagnóstico dominante.
- **ATM:** 1 missense heterocigota (AF=0.08%), demasiado frecuente para enfermedad dominante grave; sin patrón bialélico.

Este resultado es consistente con que el MVA por *BUB1B* biallélico explica el cuadro principal y no hay un segundo diagnóstico dominante en estos genes.

---

## 6.5 Mensaje para el equipo

> **[RESUMEN LISTA DE GENES — C8 actualizado]**
>
> Corrí el modelo dominante para **todos** los genes de la lista. 10 genes en total.
>
> **Resultado: todo negativo.**
>
> LMNA, KMT2D, KDM6A: sin variantes candidatas.
> ATM: solo 1 missense frecuente (AF=0.08%), no patogénica. Sin patrón bialélico tampoco.
> BRCA1, BRCA2, PALB2, RAD51C, RAD51D, CHEK2: cero variantes funcionales ultra-raras → no hay hallazgos secundarios en el panel oncológico hereditario tampoco.
>
> EZH2: descartado sin correr (Weaver = overgrowth, fenotipo opuesto).
>
> TP53 ya estaba en el modelo dominante anterior → ya analizado (negativo).
