# Track 1 report: BUB1B compound heterozygosity

**Participant:** Ktalyna (Hugging Face user `Ktalyna`) · **Predictions file:** `Ktalyna_bub1b-mane-panel.csv` · **Code:** https://github.com/ktalynagb/mva-hackathon-2026

## Prediction

| Rank | Gene | Variant 1 (GRCh38) | Variant 2 (GRCh38) | EPCR | Type |
|---|---|---|---|---|---|
| 1 | *BUB1B* (ENST00000287598, MANE Select) | chr15:40209701 T>G · c.2210T>G · **p.Leu737Ter** | chr15:40220612 T>G · c.3006T>G · **p.Asn1002Lys** | 0.85 | primary |

No secondary findings are reported. *BUB1B* is the established gene for MVA type 1 (autosomal recessive), and the case phenotype (severe growth restriction, rhabdomyosarcoma and other features) is consistent with it.

## Approach

1. **Quality:** PASS variants only (4,740,790 of 5,012,204). The 6 non-PASS calls in the 6 core MVA/SAC genes were reviewed separately; none affects the result (low QUAL/QD with weak alternate-read support, or MQ40-only calls at common dbSNP sites).
2. **Gene panel:** 321 genes covering the spindle assembly checkpoint, kinetochore, centrosome, cohesin, nuclear lamina and pore, chromatin, DNA repair and cell cycle. It includes the six MVA genes with an OMIM number (*BUB1B* MVA1, *CEP57* MVA2, *TRIP13* MVA3, *CENATAC* MVA4, *SLF2* MVA5, *SMC5* MVA6) and *MAD2L1BP* (MVA reported in 2023).
3. **Rarity:** gnomAD v4, allele frequency < 1 %, each functional variant queried directly.
4. **Consequence:** Ensembl VEP on the **MANE Select** transcript. Using the most severe consequence on any transcript produced 5 false alarms out of 18 (for example, a stop codon that only exists in a secondary *ARID1B* transcript); with MANE, 13 remain. The last 31 genes added to the panel produced one more alert, a common heterozygous missense in *MINAR1* (AF 0.49 %, 23 homozygotes in gnomAD).
5. **Recessive pattern:** a homozygous variant or two rare functional heterozygous variants in the same gene.
6. **Classification:** ACMG/AMP point system (Richards 2015; Tavtigian 2020), with CADD v1.7, ClinVar and dbNSFP predictors.

## Evidence

| | p.Leu737Ter | p.Asn1002Lys |
|---|---|---|
| gnomAD v4 (exomes) | AF 7.87×10⁻⁵, 0 homozygotes | AF 6.84×10⁻⁷, 0 homozygotes |
| CADD phred | 36.0 | 24.5 |
| ClinVar | Pathogenic (ID 533901, single submitter) | Listed as VUS (c.3006T>A) |
| Effect | Stop in exon 17 of 23; premature stop lies 747 nt upstream of the last exon junction → NMD predicted (null allele) | Pseudokinase domain (aa 766–1050); buried Asn with 3 H-bonds (AlphaFold pLDDT 91), conserved in 7/7 vertebrates; ThermoMPNN ΔΔG +1.5 kcal/mol (MVA variant p.Leu1012Pro: +3.1) |
| ACMG (points) | Likely pathogenic (9) | VUS, leaning pathogenic |
| Read support | Alt fraction 0.54, GQ 99 | Alt fraction 0.46, GQ 99 |

**Mechanism:** one null allele plus one unstable hypomorphic allele, so the patient would have little BUBR1. Kinase-domain missense variants in MVA lower BUBR1 levels through misfolding and degradation rather than loss of function (Suijkerbuijk et al. 2010, PMID 20516114). A nearly identical genotype has been published: a truncation at codon 753 plus p.Leu1012Pro.

**Differential diagnosis:** among the 321 genes, *BUB1B* is the only one with a recessive pattern, and the only one of the six MVA genes with any rare functional variant. *CEP57*, *TRIP13*, *CENATAC*, *SLF2*, *SMC5*, *MAD2L1BP*, *BUB1*, *BUB3*, *MAD2L1*, *CDC20* and *ESPL1* carry none.

## Why EPCR is 0.85 and not higher

- **Phase is unresolved.** There are no parental samples; the variants are 10.9 kb apart, the VCF has no phase tags, and the only intermediate heterozygous site is 6.8 kb and 4.1 kb away, beyond short-read fragment size. *Trans* is supported indirectly: in *cis* the patient would keep one normal copy.
- **Allele 2 has no functional data** and its predictors disagree (REVEL 0.472).
- **Not evaluated:** structural/copy-number variants and non-coding variants (one published MVA case involved a *BUB1B* regulatory variant). For the same reason, the panel's long non-coding RNA genes cannot be assessed by a protein-consequence method.

What would confirm it: parental genotyping (phase), RT-PCR for NMD, BUBR1 levels and checkpoint function in patient fibroblasts.

## Reproducibility and AI use

`python run_pipeline.py` runs the analysis end to end (genes → differential diagnosis → allele 2 evidence); versions are pinned in `requirements-lock.txt`. Patient data are not in the repository.

**AI use:** Anthropic, Claude Code (Claude Sonnet and Opus models), Claude Pro plan, consumer terms with "Help improve Claude" disabled (chats not used for training). Used for analysis code, API queries, literature review and drafting. The scripts ran on the participant's computer; Claude saw variant-level outputs (positions, alleles, read counts), and the data files never left that computer. Every AI-generated claim was checked against the primary source (PubMed, gnomAD, ClinVar, UniProt); citations that could not be verified were removed.
