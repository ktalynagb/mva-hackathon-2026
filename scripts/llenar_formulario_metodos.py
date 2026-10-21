"""Llena la hoja "Track 2 methods" del formulario oficial del reto.

Parte de la plantilla sin tocar (docs/plantillas/methods_description_form.xlsx)
y escribe las respuestas en las celdas amarillas de la columna B. Las respuestas
salen de docs/informe_final.md; si el informe cambia, se actualizan aquí y se
vuelve a correr. Van en inglés porque el formulario está en inglés.

Los huecos que el equipo tiene que completar quedan como [TO COMPLETE: ...].

Uso:
    python scripts/llenar_formulario_metodos.py
"""
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLA = RAIZ / "docs" / "plantillas" / "methods_description_form.xlsx"
SALIDA = RAIZ / "docs" / "methods_description_form.xlsx"

RESPUESTAS = {
    # Team name
    7: "A3 EMBS ITBA",

    # Approach in detail
    8: (
        "We went from genotype to mechanism to drugs in four steps, all scripted (single entry point: run_pipeline.py).\n"
        "1) Causal variant. Patient WGS VCF (GRCh38). PASS variants in a 321-gene panel (mitosis, kinetochore, centrosome, "
        "cohesin, nuclear envelope/pore, chromatin, DNA repair, cell cycle) were annotated with gnomAD v4 (rare: AF < 1%), "
        "Ensembl VEP on the MANE Select transcript, CADD v1.7, ClinVar and dbNSFP predictors, filtered under a recessive "
        "model and classified with the ACMG/AMP points system. Funnel: 24,604 PASS variants -> 14 rare protein-altering "
        "variants in MANE -> one gene with two variants: BUB1B. A dominant model on 92 PanelApp genes looked for a second diagnosis.\n"
        "2) Mechanism. NMD prediction (50-55 nt rule), AlphaFold structure and residue environment, stability (ThermoMPNN ddG) "
        "and literature verified in PubMed -> loss of function through a shortage of BUBR1 protein.\n"
        "3) Drug long list. From the mechanism we defined four therapeutic lines with the required direction of action: raise "
        "BUBR1 levels, dampen mTORC1, clear senescent cells, and treat the tumour without worsening aneuploidy. Candidates came "
        "from DGIdb v5, Open Targets and a curated list with sources (86 drugs). Exclusion filters: marketing approval checked in "
        "Drugs@FDA (openFDA) and EMA, and removal of drugs that weaken mitosis (HSP90, PLK1, Aurora, MPS1, APC/C inhibitors) -> 73 drugs.\n"
        "4) Scoring and verification. Six weighted criteria scored 0-3 (mechanistic link 25, paediatric safety 20, evidence 15, "
        "fit to the case 15, innovation 15, feasible validation 10; 0-100 scale). Every claim was checked against the primary "
        "paper and the FDA label; this corrected two scores. Patient pharmacogenetics (CYP2B6, CYP2C19, CYP3A5, ABCB1) per CPIC/PharmGKB.\n"
        "Result: two parallel treatments. Cyclophosphamide continues as part of the treatment the patient already receives "
        "for the current rhabdomyosarcoma (standard care, not repurposing). For the remaining manifestations, we propose a "
        "long-term combination of oral sirolimus + arimoclomol + niacin, started alongside tumour treatment and maintained "
        "afterwards (niacin as an explicitly speculative hypothesis). Temsirolimus is kept for relapse, dasatinib for after chemotherapy, "
        "and a MEK inhibitor + temsirolimus only if the tumour shows RAS activation. All candidates can be tested in patient "
        "fibroblasts (BUBR1 Western blot, nocodazole mitotic-arrest assay)."
    ),

    # (required) Generative AI
    9: (
        "• Claude Code (Sonnet and Opus), Anthropic, Claude Pro plan, consumer terms, \"Help improve Claude\" disabled "
        "(K. García).\n"
        "• Claude Code, Anthropic, Claude Pro plan, [TO COMPLETE BY LAURA: data setting, same text as Section II-I of the "
        "report] (L. Vargas).\n"
        "• Gemini through LangChain (notebook 06), Google, [TO COMPLETE: plan and data setting; who used it]. Received only "
        "target names and public database results, no patient data; its draft was not used as the final list.\n"
        "All AI-generated statements were verified against primary sources (PubMed, Drugs@FDA, gnomAD, UniProt)."
    ),

    # Automated or manual
    10: (
        "Hybrid. Candidate generation was automated: scripts/lista_larga_farmacos.py queries DGIdb v5 and Open Targets and "
        "checks approval status in openFDA and the EMA database. The scoring criteria were defined by the team; scoring, the "
        "curated additions and the final selection were manual curation with AI assistance, reviewed by a team member, with "
        "every statement verified against the primary source."
    ),

    # Manual curation in detail
    11: (
        "• Curated list (config/lineas_terapeuticas.json) for mechanisms the databases do not capture (e.g. arimoclomol, "
        "phenylbutyrate, rapalogs, dasatinib), each with its source.\n"
        "• Scoring criteria and 0-3 scales defined by the team from the literature and the challenge's evaluation criteria. "
        "The 55 candidates were scored with AI assistance, each with a written justification and sources "
        "(results/candidatos_farmacos.tsv), and the scores were reviewed by a team member (L. Ogas). Niacin and two MEK "
        "inhibitors (conditional on RAS activation in the tumour) were added by hand.\n"
        "• Biological safety review: for each candidate we asked whether it further weakens mitosis in a patient with a weak "
        "checkpoint. This removed bortezomib (delays mitotic exit, adds neuropathy with vincristine).\n"
        "• Verification against the original paper and FDA label corrected sirolimus (a cited study associated, but did not "
        "treat, BubR1 mice) and arimoclomol (label states mechanism unknown; renal and weight warnings).\n"
        "• Niacin vs nicotinamide: nicotinamide inhibits sirtuins (PMID 12297502), so only niacin fits the SIRT2-BubR1 hypothesis.\n"
        "• All references were cross-checked against PubMed (E-utilities)."
    ),

    # Public vs proprietary
    12: (
        "Only publicly available databases and literature. The patient genome and clinical summary come from the challenge "
        "dataset (SageBio/mva-hackathon-2026-data)."
    ),

    # Public sources in detail
    13: (
        "Drugs and targets: DGIdb v5, Open Targets Platform (including rhabdomyosarcoma trials), Drugs@FDA via openFDA, EMA "
        "medicines database, FDA labels, CPIC and PharmGKB.\n"
        "Variants and genes: gnomAD v4, ClinVar, Ensembl VEP (MANE Select), CADD v1.7, dbNSFP via myvariant.info, ClinGen, "
        "PanelApp, UniProt, AlphaFold DB, AlphaFill.\n"
        "Literature: PubMed, every citation verified (e.g. Suijkerbuijk 2010 PMID 20516114; Sieben 2020 PMID 31738183; "
        "North 2014 PMID 24825348; Mascarenhas 2019 PMID 31513481; Nishitani-Isa 2019 PMID 31184400)."
    ),

    # Proprietary sources
    14: "None.",

    # Mechanism characterisation
    15: (
        "BUB1B compound heterozygote. Allele 1, c.2210T>G p.Leu737Ter: premature stop in exon 17 of 23, predicted NMD "
        "(null allele; ClinVar pathogenic; ACMG likely pathogenic). Allele 2, c.3006T>G p.Asn1002Lys: missense in the "
        "pseudokinase domain, ACMG VUS leaning pathogenic. Buried residue (pLDDT 91) losing 3 hydrogen bonds; ThermoMPNN "
        "ddG +1.5 kcal/mol (predicted destabilising, half of the known MVA variant p.Leu1012Pro), far from the ATP pocket. "
        "In cells, all MVA missense variants studied in this domain lower BUBR1 5-10 fold by misfolding, and restoring the "
        "amount rescues the checkpoint (Suijkerbuijk 2010).\n"
        "Effect: partial loss of function through a shortage of BUBR1 protein, not loss of catalytic activity.\n"
        "Pathway: spindle assembly checkpoint (SAC); BUBR1 is a core component of the mitotic checkpoint complex.\n"
        "Consequence: weak checkpoint -> chromosome mis-segregation -> mosaic aneuploidy -> (a) senescence/premature ageing "
        "with hyperactive mTORC1 in BubR1 mice (growth restriction, muscle atrophy) and (b) chromosomal instability "
        "(rhabdomyosarcoma).\n"
        "Limitations: phase (trans) not proven, no parental samples; allele 2 is a VUS without functional data."
    ),

    # Time / effort
    16: (
        "Five team members over five weeks (17 Sep - 24 Oct 2026), about 8 hours per person per week: approximately "
        "200 person-hours. Full pipeline re-run: 6 min 11 s with cached API queries (Windows 11, Python 3.13); "
        "a clean run without the cache takes considerably longer (about 35,000 variants annotated through public APIs)."
    ),

    # Abstract (<= 500 words)
    17: (
        "We present a reproducible path from a patient's whole genome to repurposable approved drugs for mosaic variegated "
        "aneuploidy (MVA). Starting from the PASS variants of the patient VCF, we screened a 321-gene panel of mitosis, "
        "kinetochore, cohesin, chromatin and DNA-repair genes with population frequency (gnomAD v4), consequence on the MANE "
        "Select transcript (Ensembl VEP), in-silico predictors and ACMG/AMP points. Of 24,604 PASS variants, BUB1B was the "
        "only gene carrying two rare protein-altering variants: p.Leu737Ter (predicted NMD, null allele) and p.Asn1002Lys "
        "(pseudokinase missense, VUS leaning pathogenic). Using MANE annotation removed five false alerts that were severe "
        "only on secondary transcripts.\n"
        "Mechanism: structural modelling (AlphaFold, ThermoMPNN) predicts that p.Asn1002Lys destabilises BUBR1, and published "
        "cell work shows that missense variants in this domain lower BUBR1 levels and that restoring the amount restores the "
        "spindle assembly checkpoint. We therefore frame this case as a quantitative protein deficiency: partial loss of "
        "function leading to a weak checkpoint, mosaic aneuploidy, premature ageing with hyperactive mTORC1, and "
        "rhabdomyosarcoma.\n"
        "Drug repurposing: we derived four therapeutic lines with an explicit direction of action, assembled 86 candidates "
        "from DGIdb, Open Targets and a curated list, kept only drugs with verified FDA or EMA approval, and excluded every "
        "drug that weakens mitosis. Candidates were scored on six weighted criteria and every claim was checked against the "
        "primary paper and FDA label. The proposal separates two treatments: cyclophosphamide continues as part of the "
        "treatment the patient already receives for the current rhabdomyosarcoma, and, for the remaining manifestations "
        "that no current therapy addresses, we propose a long-term combination of oral sirolimus (mTORC1), arimoclomol "
        "(protein folding, to raise BUBR1) and niacin (NAD+-SIRT2-BubR1 axis, an explicitly speculative hypothesis), which "
        "could also indirectly lower the risk of new tumours. Patient pharmacogenetics (CYP2B6 intermediate metaboliser) is "
        "consistent with reduced cyclophosphamide intensity. A dominant-model search found a secondary finding in LZTR1 "
        "(schwannomatosis predisposition) that warrants surveillance. "
        "The mechanism also predicts that antimitotic chemotherapy may behave differently with a weak checkpoint.\n"
        "Strengths: a fully scripted pipeline (one command, about 6 minutes with cache), public data only, MANE-aware "
        "annotation, mechanism-driven filters that exclude harmful drugs, verified references, and a single low-cost "
        "validation experiment shared by all candidates (BUBR1 Western blot and nocodazole arrest in patient fibroblasts).\n"
        "Limitations: no parental samples, so the trans phase is assumed, not proven; allele 2 is a VUS without functional "
        "data; none of the candidates has been tested in MVA, and the niacin hypothesis rests on mouse data with NMN that "
        "lacks independent replication; arimoclomol's mechanism is officially unknown; the pipeline has been run end-to-end "
        "only on Windows and has no automated tests."
    ),
}


def main() -> None:
    respuestas = dict(RESPUESTAS)
    # La fila 9 (uso de IA) la completa cada integrante a mano en el Excel; al regenerar se conserva
    # lo que ya escribieron en lugar de volver a poner los huecos.
    if SALIDA.exists():
        previa = load_workbook(SALIDA)["Track 2 methods"].cell(row=9, column=2).value
        if previa and "TO COMPLETE BY LAURA" not in previa:
            respuestas[9] = previa
    wb = load_workbook(PLANTILLA)
    hoja = wb["Track 2 methods"]
    for fila, texto in respuestas.items():
        celda = hoja.cell(row=fila, column=2)
        celda.value = texto
        celda.alignment = Alignment(wrap_text=True, vertical="top")
    hoja.column_dimensions["B"].width = max(hoja.column_dimensions["B"].width or 0, 110)
    wb.save(SALIDA)
    palabras = len(RESPUESTAS[17].split())
    print(f"Formulario guardado en {SALIDA} (abstract: {palabras} palabras)")


if __name__ == "__main__":
    main()
