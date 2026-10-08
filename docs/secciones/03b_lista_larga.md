# 03b · Lista larga de fármacos (tarea C3)

**Borrador para revisión** · 8 de octubre de 2026
Tabla completa: `results/candidatos_farmacos.tsv`. Se regenera con `python scripts/lista_larga_farmacos.py` (unos 2 minutos; usa la caché de `results/cache/c3/`, y `--sin-cache` vuelve a consultar todo). Parámetros en `config/lineas_terapeuticas.json`.

## 1. Método

1. **Semillas por línea terapéutica** (las cuatro de `02b_resumen_mecanismo.md`), cada una con la **dirección buscada**: por ejemplo, *activar* HSF1/HSP70 o *inhibir* mTOR. Un fármaco que actúa en la dirección contraria no entra.
2. **Tres fuentes:**
   - **DGIdb v5**: interacciones fármaco–gen de las semillas, solo fármacos marcados como aprobados.
   - **Open Targets**: fármacos aprobados sobre las mismas dianas, más todos los fármacos aprobados con ensayos en **rabdomiosarcoma** (MONDO_0005212), con la fase máxima alcanzada en esa enfermedad.
   - **Lista curada** con fuente para los casos que las bases no capturan: arimoclomol, fenilbutirato sódico, rapalógos (la diana figura como el complejo FKBP12–mTOR) y dasatinib como senolítico.
3. **Aprobación (F1)** comprobada contra la fuente regulatoria, no contra la base de interacciones: Drugs@FDA (openFDA, por nombre genérico o principio activo) y el listado de autorizaciones **centralizadas** de la EMA.
4. **Dirección del mecanismo (F2):**
   - Auditoría de los 162 inhibidores que DGIdb asocia a HSP90, PLK1, Aurora A/B, MPS1, CDC20, APC/C, BUB1 y CDK1, con la misma comprobación de aprobación.
   - Un antimitótico (por la lista de DGIdb o porque su diana es la tubulina) queda excluido si no pertenece a la línea del tumor; dentro de ella se marca "PRECAUCIÓN".
5. **Contexto:** se separan el tratamiento estándar del rabdomiosarcoma y los fármacos de soporte o de trasplante. No son reposicionamiento, pero sirven para K4 (compatibilidad).

## 2. Resultado

**86 fármacos: 52 candidatos para puntuar, 21 de contexto y 13 excluidos.**

| Línea | Candidatos | Fármacos |
|---|---|---|
| 1 · Subir BUBR1 | 5 | **Arimoclomol**, **fenilbutirato sódico**; inhibidores del proteasoma bortezomib, carfilzomib e ixazomib |
| 2 · Frenar mTORC1 | 7 | **Sirolimus**, **everolimus**, **temsirolimus**, metformina (las cuatro también con ensayos en rabdomiosarcoma); alpelisib, copanlisib, infigratinib |
| 3 · Senolíticos | 2 | **Dasatinib**, venetoclax |
| 4 · Tumor | 38 | Antiangiogénicos y multiquinasa (bevacizumab, cabozantinib, pazopanib, regorafenib, sorafenib, lenvatinib), inmunoterapia (nivolumab, ipilimumab, atezolizumab), quimioterapia (gemcitabina, docetaxel, carboplatino, trabectedina…), olaparib, ribociclib, teprotumumab (anti-IGF1R), entre otros |

**Excluidos (13):**
- **F1, 12:** navitoclax, ridaforolimus, sapanisertib, perhexilina (aprobada fuera de EE. UU. y la UE), trofosfamida, entre otros.
- **F2, 1:** paclitaxel unido a albúmina, que DGIdb asociaba a BCL2 como "senolítico".

**Hallazgo de la auditoría F2:** ninguno de los 162 inhibidores de HSP90, PLK1, Aurora, MPS1, APC/C, BUB1 o CDK1 está aprobado por la FDA ni tiene autorización centralizada de la EMA. Las dianas que empeorarían el checkpoint no tienen fármacos aprobados; lo que se excluye por F2 son fármacos aprobados para otra cosa que debilitan la mitosis.

## 3. Avisos para quien puntúe (C4)

- **Ruido de las bases que hay que juzgar:** alpelisib (inhibe PI3Kα, y su vínculo con mTOR es indirecto), infigratinib (inhibe FGFR; el vínculo con mTOR es dudoso), el ácido valproico con diana ALDH5A1 (su efecto relevante es inhibir HDAC). Bajar K1 si el vínculo es débil.
- **F4 por revisar:** copanlisib, infigratinib y nitrato de galio figuran como discontinuados en EE. UU. Comprobar si fue por seguridad o por razones comerciales.
- **EMA "no centralizado" no significa "no aprobado en Europa"**: muchos fármacos antiguos (vincristina, cisplatino, metotrexato) tienen autorizaciones nacionales.
- **Inhibidores del proteasoma:** la lógica (subir la BUBR1 mutante, como MG132 en células) es sólida, pero son citotóxicos. Probablemente K2 y K4 bajos.
- **La línea 4 es amplia (38):** conviene puntuar primero los que tienen fase 2 o 3 en rabdomiosarcoma y los que unen dos líneas (temsirolimus, sirolimus, everolimus).
- La columna `fase_rms` es la fase máxima de los ensayos en rabdomiosarcoma según Open Targets; no implica un resultado positivo.

## 4. Limitaciones

- DGIdb y Open Targets dependen de sus fuentes: hay asociaciones fármaco–diana dudosas (sección 3) y huecos (los rapalógos no aparecen ligados a MTOR en Open Targets).
- La aprobación pediátrica y la edad mínima (F3) no se comprueban de forma automática; se revisan en la ficha técnica al puntuar K2.
- Los fármacos sin diana molecular única (quimioterapia clásica, chaperonas químicas) solo entran por la lista de rabdomiosarcoma o por curación manual.
