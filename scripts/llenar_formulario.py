"""llenar_formulario.py — Tarea E7: completa el formulario de metodos del reto.

Toma la plantilla oficial (docs/plantillas/methods_description_form.xlsx, bajada del Space
del reto en E3) y escribe las respuestas de la hoja "Track 2 methods" en la columna B.
La plantilla no se modifica: la salida va a envios/track2/.

Las respuestas estan en ingles porque el formulario y el panel evaluador lo estan
(Sage Bionetworks / Hugging Face). El informe sigue en espanol.

Uso:  python scripts/llenar_formulario.py
"""
import shutil
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[1]
PLANTILLA = RAIZ / "docs" / "plantillas" / "methods_description_form.xlsx"
SALIDA = RAIZ / "envios" / "track2" / "A3_EMBS_ITBA_methods_description_form.xlsx"
HOJA = "Track 2 methods"

# fila del formulario -> respuesta. El texto de cada pregunta esta en la columna A.
RESPUESTAS = {
    7: "A3 EMBS ITBA",

    8: (
        "We went from genome to candidates in four stages, all scripted and reproducible "
        "with a single command (python run_pipeline.py).\n\n"
        "1. VARIANT. We filtered PASS variants from the proband's whole-genome VCF against a "
        "321-gene panel covering mitosis, kinetochore, centrosome, cohesin, nuclear lamina and "
        "pore, chromatin, DNA repair and cell cycle. We kept rare variants (gnomAD v4 AF < 1%) "
        "with a protein-altering consequence in the MANE Select transcript (Ensembl VEP), then "
        "looked for a recessive pattern (homozygous, or two heterozygous variants in the same "
        "gene). BUB1B was the only gene in the panel with two rare functional variants. We "
        "classified them with ACMG/AMP using the points system.\n\n"
        "2. MECHANISM. We characterised each allele separately (NMD prediction by the 50-55 nt "
        "rule; AlphaFold structure, residue burial and hydrogen bonding; ddG with ThermoMPNN) "
        "and converged on a single quantitative statement: this patient has too little BUBR1 "
        "protein rather than defective BUBR1 function. See Q10 for why that distinction drove "
        "every drug decision.\n\n"
        "3. THERAPEUTIC LINES. From the mechanism we derived four directions of action: raise "
        "BUBR1 protein level, inhibit mTORC1 (hyperactive in BubR1-low mice), clear senescent "
        "aneuploid cells, and treat the tumour without worsening aneuploidy. Each line specifies "
        "the direction of effect sought, so a drug can be judged against it.\n\n"
        "4. CANDIDATES. We built a long list of 86 drugs per line from DGIdb v5 and Open Targets "
        "plus a curated list with sources for what the databases miss. We then applied exclusion "
        "filters (approval verified directly in Drugs@FDA/openFDA and the EMA register, not in "
        "the interaction database) and a mechanism-based exclusion: any drug that would further "
        "weaken mitosis was removed, which ruled out all HSP90, PLK1, Aurora, MPS1 and APC/C "
        "inhibitors. Survivors were scored on six weighted criteria (mechanistic link 25, "
        "paediatric safety 20, evidence 15, case compatibility 15, innovation 15, feasible "
        "validation 10). Finally, every drug claim was checked against the primary paper and the "
        "FDA label, which changed two scores (see Q11).\n\n"
        "The proposal deliberately separates two things: the rhabdomyosarcoma is treated by the "
        "standard oncology protocol (reduced-intensity VAC, which includes cyclophosphamide and "
        "is not repurposing), while our contribution is a continuous regimen aimed at the "
        "underlying disease, which nothing currently treats: oral sirolimus, arimoclomol and "
        "niacin. We also report a pharmacogenomic analysis of the patient's CYP2B6, CYP2C19, "
        "CYP3A4, CYP3A5 and ABCB1 variants to inform dosing."
    ),

    9: (
        "Four tools were used. Only the first received any patient-derived data.\n\n"
        "1. Anthropic Claude Code (Sonnet and Opus), Pro plan, consumer terms, "
        "'Help improve Claude' disabled (no training on chats). Used for analysis code, API "
        "queries, literature verification and drafting. Received patient-derived output at "
        "variant level (positions, alleles, read depths); the VCF, raw reads and clinical "
        "document never left the local machine.\n\n"
        "2. Anthropic Claude (web application), free tier, training setting not confirmed by the "
        "user. Used only for literature search on the disease and its described treatments. No "
        "patient data.\n\n"
        "3. Google Gemini (gemini-3.5-flash-lite and gemini-3.8-flash) through the Gemini API "
        "with LangChain, UNPAID tier. Google's unpaid-tier terms state that submitted content and "
        "generated responses are used to 'provide, improve, and develop' their products and that "
        "'human reviewers may read, annotate, and process your API input and output'. We note "
        "this explicitly because those same terms warn against submitting sensitive or personal "
        "information. No patient data was sent: the prompt contained only the disease name, the "
        "BUB1B gene and therapeutic target names (verifiable in notebooks/06). Its output was a "
        "first draft that was discarded; the final drug list comes from "
        "scripts/lista_larga_farmacos.py.\n\n"
        "4. Perplexity, free tier, training setting not confirmed by the user. Used only for "
        "literature search on the disease and its described treatments. No patient data.\n\n"
        "Every AI-generated claim was verified against the primary source. Claims that could not "
        "be verified were removed from the report."
    ),

    10: (
        "Both, in clearly separated roles.\n\n"
        "AUTOMATED: panel filtering and variant annotation (gnomAD v4, Ensembl VEP on MANE "
        "Select, ClinVar, CADD, dbNSFP predictors); long-list construction by querying DGIdb v5 "
        "and the Open Targets Platform per target; and approval checking against Drugs@FDA "
        "(openFDA) and the EMA centralised register. All scripted, cached and reproducible.\n\n"
        "MANUAL / EXPERT CURATION: the six-criterion scoring of each candidate; a curated drug "
        "list for mechanisms the databases do not capture; the biological review of whether each "
        "drug would worsen mitosis; and verification of every factual claim against the primary "
        "literature and the regulatory label. Detail in Q11.\n\n"
        "An LLM was used to draft code and text and to orient literature searches, but not as the "
        "source of the final candidate list. An early LLM-generated drug list (Gemini, notebooks/06) "
        "was discarded precisely because it could not be traced to verifiable sources."
    ),

    11: (
        "Manual curation was the step that changed the result most, in four ways.\n\n"
        "1. CLAIM-BY-CLAIM VERIFICATION. Every statement about a drug was checked against the "
        "original paper in PubMed and against the FDA label. This corrected two scores. "
        "Sirolimus dropped from 80 to 71.7 because the paper we had cited (Sieben 2020, PMID "
        "31738183) only ASSOCIATES sarcopenia with hyperactive mTORC1 in BubR1-mutant mice; it "
        "did not treat them with rapamycin. The rapamycin treatment result is in wild-type mice "
        "(Ham 2020, PMID 32908143). Arimoclomol dropped from 73.3 to 68.3 after reading the FDA "
        "label, which states that its mechanism in Niemann-Pick C is unknown and warns about "
        "weight loss and renal findings, both relevant in a child with failure to thrive and "
        "nephrocalcinosis. Citations that could not be verified in PubMed were deleted.\n\n"
        "2. MECHANISM-BASED EXCLUSION. We asked of each candidate whether, beyond its intended "
        "effect, it would further weaken cell division in a patient whose spindle assembly "
        "checkpoint is already compromised. This excluded HSP90, PLK1, Aurora, MPS1 and APC/C "
        "inhibitors as a class, and flagged bortezomib: by blocking the proteasome it also blocks "
        "cyclin B and securin degradation, delaying mitotic exit, and adds neuropathy on top of "
        "vincristine. It was removed from the short list.\n\n"
        "3. REVERSED JUDGEMENTS AFTER CHALLENGE. When a team member argued for nab-sirolimus on "
        "tumour-accumulation grounds, we re-examined it and found our own write-up was wrong: a "
        "Children's Oncology Group phase 1 with a defined paediatric MTD does exist (PMID "
        "39487711), and tumour accumulation is measured in xenografts. We corrected the document "
        "and reclassified the drug rather than defending the earlier position.\n\n"
        "4. COMPOUND DISAMBIGUATION. Our NAD+/SIRT2 hypothesis requires niacin (nicotinic acid), "
        "not nicotinamide, even though both are vitamin B3 and are often used interchangeably. "
        "Nicotinamide is the product of the sirtuin reaction and its feedback inhibitor, whereas "
        "nicotinic acid had no effect on SIRT1 in the same study (PMID 12297502). Proposing the "
        "inhibitor of the enzyme the hypothesis depends on would have been self-defeating.\n\n"
        "We also ran a dominant-model analysis over 92 PanelApp green genes looking for a second "
        "diagnosis, which found an incidental LZTR1 truncating variant, and extended it to 10 "
        "genes proposed by the team (including BRCA1/2, PALB2, RAD51C/D, CHEK2), all negative."
    ),

    12: (
        "Solely publicly available databases and literature. No external proprietary data source "
        "was used.\n\n"
        "The only access-controlled input is the challenge's own dataset "
        "(SageBio/mva-hackathon-2026-data on Hugging Face): the proband's VCF and clinical "
        "document, used under the challenge access terms. That is the subject of the analysis, "
        "not an external proprietary source. Those files were never uploaded to the repository, "
        "shared outside the team, or sent to any third-party service."
    ),

    13: (
        "VARIANT AND GENE: gnomAD v4 (allele frequencies and gene constraint, LOEUF/pLI), "
        "Ensembl VEP with MANE Select transcripts, ClinVar, CADD v1.7, dbNSFP predictors "
        "(including REVEL), myvariant.info, UniProt (O60566, BUBR1), and PanelApp from Genomics "
        "England for the dominant-model gene panels (nephrocalcinosis, renal tubulopathies, "
        "calcium/parathyroid, CASR, familial rhabdomyosarcoma, childhood solid tumours, sarcoma "
        "susceptibility, monogenic short stature).\n\n"
        "STRUCTURE AND STABILITY: AlphaFold and AlphaFill models, and ThermoMPNN for ddG "
        "predictions across the pseudokinase domain.\n\n"
        "DRUGS AND TARGETS: DGIdb v5 and the Open Targets Platform for drug-target relationships "
        "and rhabdomyosarcoma trial links; Drugs@FDA via openFDA and the EMA register of "
        "centrally authorised medicines for approval status and label text; CPIC and PharmGKB for "
        "pharmacogenomic phenotype assignment.\n\n"
        "LITERATURE: PubMed, with every citation checked for existence and content. Key sources "
        "include Hanks 2004 (PMID 15475955, founding BUB1B-MVA paper), Suijkerbuijk 2010 (PMID "
        "20516114, pseudokinase missense variants reduce BUBR1 protein level), Sieben 2020 (PMID "
        "31738183), Mascarenhas 2019 (PMID 31513481, temsirolimus phase II in relapsed "
        "rhabdomyosarcoma), Defachelles 2021 (PMID 34343032, VIT-0910), Hol 2021 (PMID 34134020, "
        "SIOP-Europe Wilms tumour surveillance) and Nakano 2024 (PMID 39264246)."
    ),

    14: "None.",

    15: (
        "LOSS OF FUNCTION, and specifically loss of protein QUANTITY rather than of catalytic "
        "activity. That distinction is the core of our proposal, because it changes which targets "
        "are worth pursuing.\n\n"
        "GENOTYPE: compound heterozygous BUB1B. Allele 1, p.Leu737Ter, is a premature stop in "
        "exon 17 of 23, more than 55 nt from the last exon-exon junction, so NMD is predicted by "
        "the 50-55 nt rule and the allele is expected to produce no protein (classified likely "
        "pathogenic, 9 points; pathogenic in ClinVar). Allele 2, p.Asn1002Lys, is a missense in "
        "the pseudokinase domain: a buried residue (pLDDT 91) making three hydrogen bonds that "
        "lysine cannot form, with ddG +1.5 kcal/mol (72nd-75th percentile of the domain), about "
        "half that of the known MVA variant p.Leu1012Pro (+3.1). It does not contact the ATP "
        "pocket (29 A away). It remains a VUS leaning pathogenic.\n\n"
        "WHY QUANTITY AND NOT FUNCTION: every MVA missense variant in this domain characterised in "
        "cells reduces BUBR1 abundance five- to ten-fold through misfolding, and restoring normal "
        "levels restores checkpoint function (Suijkerbuijk 2010, PMID 20516114). So a null allele "
        "plus a destabilised hypomorphic allele converge on the same endpoint: too little BUBR1.\n\n"
        "PATHWAY DISRUPTED: the spindle assembly checkpoint (SAC). BUBR1 is a core component of "
        "the mitotic checkpoint complex that inhibits the APC/C until all chromosomes are properly "
        "attached.\n\n"
        "DOWNSTREAM CONSEQUENCE: a weak checkpoint allows chromosome missegregation, producing "
        "mosaic aneuploidy, which branches into (a) senescence and premature ageing, with "
        "hyperactive mTORC1 described in BubR1-low mice, matching the growth restriction, short "
        "stature and muscle atrophy, and (b) chromosomal instability, matching the "
        "rhabdomyosarcoma. The nephrocalcinosis is not explained by this mechanism and we say so: "
        "no renal gene accounted for it under either dominant or recessive models, and prematurity "
        "is the more likely cause (PMID 38296790).\n\n"
        "A clinically relevant corollary we did not find discussed in the MVA literature: "
        "vincristine, present in every rhabdomyosarcoma protocol, kills through SAC-dependent "
        "mitotic arrest, which is precisely what is impaired here. BubR1-haploinsufficient mice "
        "show mitotic slippage (PMID 14744753), but the published evidence runs in both directions "
        "(PMID 17172401), so we raise it as an open question with a concrete experiment rather "
        "than as a claim."
    ),

    16: (
        "Approximately 120 person-hours across five weeks (17 September to 24 October 2026).\n\n"
        "Per-person hours were not logged, so this is an estimate derived from the repository "
        "record rather than a time sheet: 104 commits over 11 active days, 2,254 lines of Python "
        "across 13 analysis scripts, eight report sections, and a dated work log in "
        "docs/bitacora.md. Effort was concentrated unevenly: one contributor accounts for roughly "
        "85% of commits (all of the computational work and the report), with four others "
        "contributing domain review, the gene list and documentation. A substantial share of the "
        "total went not to writing code but to verifying AI-generated claims against primary "
        "sources, which is what produced the corrections described in Q11."
    ),

    17: (
        "BACKGROUND. Mosaic variegated aneuploidy (MVA) is an ultra-rare paediatric chromosome "
        "instability syndrome with no disease-modifying treatment. We analysed a proband with "
        "rhabdomyosarcoma, nephrocalcinosis, severe intrauterine growth restriction and short "
        "stature.\n\n"
        "METHODS. From the whole-genome VCF we filtered PASS variants across a 321-gene mitosis "
        "and genome-stability panel, retaining rare variants (gnomAD v4 AF < 1%) with a "
        "protein-altering consequence in the MANE Select transcript, and tested for recessive "
        "patterns. BUB1B was the only gene with two rare functional variants. We characterised "
        "each allele (NMD by the 50-55 nt rule; AlphaFold burial and hydrogen bonding; ThermoMPNN "
        "ddG), derived four mechanism-based therapeutic directions, built an 86-drug long list "
        "from DGIdb v5, Open Targets and a sourced curated list, verified approval directly in "
        "Drugs@FDA and the EMA register, excluded drugs that would further weaken mitosis, and "
        "scored survivors on six weighted criteria. We additionally ran a dominant model over 92 "
        "PanelApp genes to test for a second diagnosis, and a pharmacogenomic analysis of CYP2B6, "
        "CYP2C19, CYP3A4, CYP3A5 and ABCB1.\n\n"
        "RESULTS. Compound heterozygous BUB1B: p.Leu737Ter (null, NMD predicted) and "
        "p.Asn1002Lys (destabilising pseudokinase missense, ddG +1.5 kcal/mol). Both converge on "
        "reduced BUBR1 ABUNDANCE rather than impaired activity, which reframes MVA as a "
        "protein-quantity disease and redirects the target space. Our proposal separates standard "
        "oncology (reduced-intensity VAC, including cyclophosphamide, which is not repurposing) "
        "from a continuous regimen for the untreated underlying disease: oral sirolimus (mTORC1), "
        "arimoclomol (proteostasis) and niacin (NAD+/SIRT2-mediated BubR1 stabilisation; "
        "explicitly speculative). The dominant model additionally identified an incidental LZTR1 "
        "truncating variant, likely pathogenic for LZTR1-related schwannomatosis, which carries "
        "actionable paediatric surveillance guidance.\n\n"
        "STRENGTHS. The pipeline is reproducible with one command and uses only public APIs; the "
        "reference run completed all eight steps in 6 min 11 s and reproduced every number in the "
        "report. Every drug claim was verified against the primary paper and the regulatory label, "
        "which corrected two of our own scores and reversed one judgement. Mechanistic reasoning "
        "was applied as an exclusion criterion, not only a selection one. We report the highest "
        "clinical-impact finding even though it is not a drug: Wilms tumour risk in BUB1B-MVA is "
        "approximately 50%, and the recommended three-monthly renal ultrasound is already "
        "indicated for this patient's nephrocalcinosis, so surveillance adds no cost.\n\n"
        "LIMITATIONS. Trans phase cannot be established without parental samples and is not "
        "resolvable from this dataset. Allele 2 remains a VUS. No candidate has been tested in "
        "MVA; evidence is preclinical or from other diseases, and arimoclomol's own FDA label "
        "states its mechanism is unknown. Structural and non-coding variants were not assessed. "
        "The nephrocalcinosis is unexplained. The niacin hypothesis rests on a single unreplicated "
        "mouse result obtained with a different NAD+ precursor. All candidates are falsifiable in "
        "one inexpensive experiment: patient fibroblasts before and after treatment, measuring "
        "BUBR1 by Western blot and checkpoint response with nocodazole."
    ),
}


def main():
    wb = openpyxl.load_workbook(PLANTILLA)
    ws = wb[HOJA]

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    for fila, texto in RESPUESTAS.items():
        pregunta = (ws.cell(row=fila, column=1).value or "").split("\n")[0]
        ws.cell(row=fila, column=2).value = texto
        ws.cell(row=fila, column=2).alignment = openpyxl.styles.Alignment(
            wrap_text=True, vertical="top")
        print(f"  B{fila}  {len(texto):5d} car.  <- {pregunta[:62]}")

    ws.column_dimensions["B"].width = 100
    wb.save(SALIDA)
    print(f"\nGuardado: {SALIDA.relative_to(RAIZ)}")
    print(f"Plantilla intacta: {PLANTILLA.relative_to(RAIZ)}")

    faltan = [f for f in range(7, 18) if f not in RESPUESTAS]
    print(f"Filas sin responder: {faltan or 'ninguna'}")


if __name__ == "__main__":
    main()
