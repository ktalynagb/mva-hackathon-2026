# 05 · Farmacogenética del paciente

**Análisis realizado el 15 de octubre de 2026** · rama `tarea/C7-farmacogenetica`  
Entrada: `scripts/farmacogenetica.py` + VCF del paciente · Genotipos crudos en `data/farmacogenetica/` (no versionado)

> **Aviso de privacidad.** Este documento solo muestra fenotipos de metabolizador  
> (ej. "metabolizador intermedio de CYP2B6"), sin posiciones genómicas ni alelos del VCF.  
> Los genotipos completos están en `data/farmacogenetica/genotipos_farma.json`.

---

## 1. Contexto: ¿por qué revisar esto?

`tbussozungri` propone combinar nab-sirolimus + arimoclomol + ciclofosfamida (ver sección 7 de  
`04_candidatos.md` para la evaluación de esa combinación). Antes de usarlos, conviene saber si el  
paciente tiene variantes en los genes que metabolizan esas drogas que aumenten el riesgo de toxicidad  
o reduzcan la eficacia. Se revisaron las variantes del documento `ANÁLISIS DE FARMACOGENÉTICA PARA MVA.docx` del equipo.

---

## 2. Resultados (solo fenotipos)

### 2.1 Ciclofosfamida — metabolismo y toxicidad

Ciclofosfamida es un profármaco activado principalmente por **CYP2B6** (70–80 % de la dosis)  
y en menor medida por CYP2C19 y CYP3A4. Los metabolizadores intermedios o pobres producen  
menos metabolito activo (4-OH-ciclofosfamida) y potencialmente menos toxicidad, pero también  
menos eficacia. **No existe guía CPIC para ciclofosfamida.**

| Gen | Fenotipo observado | Nivel evidencia | Implicación |
|---|---|---|---|
| **CYP2B6** | Probable **metabolizador intermedio** (*1/*6 ó similar; porta componentes de *9 y *6) | B | Producción de metabolito activo levemente reducida; se sugiere TDM si hay problemas de eficacia o toxicidad inesperada |
| **CYP2C19** | **Metabolizador intermedio** (*1/*2) | B | Contribución menor al metabolismo de ciclofosfamida; impacto clínico incierto |
| **CYP3A4 *22** | Probable WT/WT (no detectado en VCF) | B | Sin reducción de expresión; metabolismo CYP3A4 normal |
| **CYP3A4 *1B** | **Homocigota** (ambos alelos *1B) | C | Evidencia debatida; no cambia la decisión clínica por sí sola |
| **GSTM1** | **No evaluable** (deleción; no visible en VCF de SNV) | B | Limitación del análisis: GSTM1 nulo aumentaría la acumulación de metabolitos alquilantes; no se puede descartar |

**Conclusión para ciclofosfamida:** el fenotipo de metabolizador intermedio de CYP2B6 no  
contraindica su uso, pero refuerza la justificación del protocolo de **intensidad reducida**  
que ya describe Nishitani-Isa 2019 (PMID 31184400) para pacientes con MVA. Monitorear la  
respuesta y la toxicidad más de cerca que en un paciente sin variantes.

---

### 2.2 Sirolimus / nab-sirolimus — metabolismo y exposición

Sirolimus es metabolizado principalmente por **CYP3A4** y por **CYP3A5** cuando está expresado.  
La P-glucoproteína (ABCB1) regula su absorción intestinal. La guía CPIC para tacrolimus  
(análoga) establece recomendaciones según el fenotipo de CYP3A5.

| Gen | Fenotipo observado | Nivel evidencia | Implicación |
|---|---|---|---|
| **CYP3A5** | **No expresor** (*3/*3) | **A** (analogía CPIC tacrolimus) | **CYP3A4 domina el metabolismo de sirolimus. Dosis estándar. Sin ajuste por CYP3A5.** |
| **CYP3A4 *22** | Probable WT/WT | B | Sin reducción de expresión; metabolismo normal de sirolimus |
| **CYP3A4 *1B** | Homocigota variante | C | Posible metabolismo levemente más rápido en algunos estudios (evidencia mixta). No accionable sin TDM |
| **CYP3A4 *1G** | Probable WT/WT | C | Portadores *1G/\*1G tendrían mayor aclaramiento de sirolimus; no aplica aquí |
| **ABCB1** | Haplotipo **heterocigoto** clásico (3435CT + 2677GT/A + 1236CT) | C | Variantes comunes; efecto en absorción de sirolimus debatido; sin acción recomendada |

**Conclusión para sirolimus:** el perfil farmacogenómico no indica ningún ajuste de dosis de  
inicio. El fenotipo CYP3A5 *3/*3 (no expresor) es el más frecuente en poblaciones europeas  
(~85 %) y es el perfil estándar para el que se calcula la dosis de sirolimus oral.  
**Se recomienda monitoreo de niveles (TDM) en los primeros 2 semanas**, como es habitual  
en uso pediátrico, independientemente de la genética.

---

### 2.3 Arimoclomol — sin farmacogenética relevante

No se encontraron estudios de farmacogenética específicos para arimoclomol. La ficha FDA  
(Miplyffa) no menciona variantes genéticas que afecten su metabolismo.  
**El factor limitante es la función renal**, no la genética CYP.  
La creatinina sérica aumenta 10–20 % (inhibe OCT2, sin cambiar el filtrado); vigilar con  
cistatina C en este paciente con nefrocalcinosis (ver sección 2.1 de `04_candidatos.md`).

---

## 3. Limitaciones

1. **GSTM1**: la deleción homocigota (GSTM1 nulo) **no es visible en un VCF de SNV**. Requiere  
   análisis de profundidad de lectura o array específico. No se puede descartar GSTM1 nulo,  
   que aumentaría el estrés oxidativo con ciclofosfamida.

2. **Fase de los alelos CYP2B6**: las variantes de *9 y *6 están en heterocigosis. Sin datos  
   de los padres, no se puede confirmar si están en *cis* (= *1/*6, metabolizador intermedio)  
   o en *trans* (= *9/\*6, metabolizador pobre). La implicación práctica es similar.

3. **CYP3A4 *1B/\*1B en población europea**: el alelo *1B es más frecuente en población  
   africana (~35–40 %) que en europea (~5–10 %). Ver que la orientación de los alelos en el  
   VCF sea correcta antes de reportar homocigota en un informe clínico.

4. **Sin guía CPIC para ciclofosfamida ni para sirolimus directamente**. Las implicaciones de  
   CYP2B6 vienen de estudios observacionales; las de CYP3A5 son por analogía con tacrolimus  
   (nivel A para tacrolimus; nivel B para sirolimus según PharmGKB).

---

## 4. Resumen ejecutivo para el informe

> El paciente es un **metabolizador intermedio de CYP2B6 y CYP2C19**, lo que reduce  
> levemente la activación de ciclofosfamida y refuerza el argumento de usar dosis reducidas  
> (protocolo de Nishitani-Isa 2019). Para sirolimus, el fenotipo **CYP3A5 no expresor**  
> (*3/*3) es el estándar europeo y no requiere ajuste de dosis inicial — sí monitoreo de  
> niveles. Arimoclomol no tiene farmacogenética conocida; el riñón es el órgano centinela.  
> GSTM1 no pudo evaluarse desde el VCF.
