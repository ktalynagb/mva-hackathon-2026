# Video package · Track 2 · Team A3 EMBS ITBA

Material for whoever records and edits the Track 2 video. It replaces an earlier script draft from 8 Oct, whose numbers and drug list were out of date; that draft was removed from the repository once this package superseded it.

## What the rules require

- **Length: 3 minutes.** The video must walk through **our reasoning and the proposed candidates**.
- Upload it to **YouTube or Vimeo**. The link is required in the submission form.
- **Nothing that could identify the patient**: no age, place, dates, or photos. Do not show VCF tables, genomic positions, or genotypes on screen.
- **Secondary finding (*LZTR1*):** the team decided to name it in the report. The video does not need it; the script focuses on the mechanism and the drugs.
- Language: **English**. Add subtitles.

## Images, in order of appearance

All images are in the repository and in English. The video figures (`results/video/`) are 16:9 with large text; regenerate them with `python scripts/figuras_video.py`. The report figures at full width are in `results/en/` (`python scripts/figuras_report_en.py`).

| # | Block | Time | Image |
|---|---|---|---|
| 1 | The problem and the case | 0:00–0:25 | `results/video/video_1_case.png` |
| 2 | How we did it | 0:25–0:45 | `results/video/video_2_method.png` |
| 3 | From 321 genes to one | 0:45–1:05 | `results/en/fig_variant_funnel.png` and `results/en/fig_variants_per_gene.png` |
| 4 | The two variants | 1:05–1:25 | `results/en/fig_bubr1_variants.png` |
| 5 | The mechanism | 1:25–1:55 | **`results/en/fig_checkpoint_normal_vs_patient.png`**, then `results/en/fig_mechanism_pathway.png` |
| 6 | How we chose the drugs | 1:55–2:20 | `results/video/video_3_drug_funnel.png` and `results/video/video_4_candidate_scores.png` |
| 7 | The proposal and how to test it | 2:20–3:00 | `results/video/video_5_proposal.png` |

**Note on the pathway figure (block 5).** It shows the **four therapeutic strategies** with examples of each (for instance "sirolimus, everolimus" and "arimoclomol, phenylbutyrate"), not the final proposal. Use it to explain **where each type of drug acts**; the final choice appears in block 7. The checkpoint figure (normal vs. this patient) is the easiest one to follow for a general audience.

## Script (about 420 words, about 3 minutes read calmly)

**1 · The problem and the case (25 s)**
Before a cell divides, it checks that every chromosome is properly attached. In mosaic variegated aneuploidy, that check fails: cells end up with extra or missing chromosomes, and the risk of childhood cancer soars. Our patient was born premature and small, grows slowly, is losing muscle, has calcium deposits in the kidneys, and developed a rhabdomyosarcoma. There is no treatment aimed at the cause of this disease.

**2 · How we did it (20 s)**
We asked two questions: what is broken, and which approved drug could help? We answered them in five steps, from the whole genome to a proposal, with a single reproducible command and only public data.

**3 · From 321 genes to one (20 s)**
We looked at 321 cell-division genes: more than 24,000 variants. We filtered them by how rare they are in the population and by their effect on the protein in the reference transcript. Only one gene carries two damaging variants: *BUB1B*.

**4 · The two variants (20 s)**
*BUB1B* makes the protein BUBR1. One variant cuts the protein in half, and its messenger is destroyed. The other changes a single amino acid. Its significance is uncertain, but it falls in the same region as the variants of other patients with this disease.

**5 · The mechanism (30 s)**
The key is the amount of protein. In cells from other patients, changes in this region make BUBR1 misfold and break down, and restoring the amount brings the checkpoint back. Our structural model predicts the same for this variant. Our conclusion: a partial loss of function. There is too little BUBR1, the brake on cell division is weak, and that leads to aneuploidy, cellular aging, and cancer.

**6 · How we chose the drugs (25 s)**
From the mechanism come four strategies: raise BUBR1, dampen the mTOR pathway, clear aged cells, and treat the tumor without making the problem worse. We gathered 86 drugs and kept only those approved by the FDA or the EMA. We removed the ones that would lower BUBR1 even further and scored the rest on six criteria, including safety in children.

**7 · The proposal (40 s)**
We propose two treatments in parallel. Cyclophosphamide continues as part of the treatment the patient already receives for the tumor. For the rest of the disease, which no treatment addresses today, we propose a long-term combination of three approved drugs. Oral sirolimus, to dampen the mTOR pathway. Arimoclomol, to help BUBR1 fold. And niacin, through a pathway that regulates BUBR1 in mice; this last one is a speculative hypothesis. None has been tested in this disease, but all three can be checked with one inexpensive experiment: skin cells from the patient, measuring BUBR1 before and after each drug. All the code is on GitHub.

## Recording tips

- Read the script aloud and time it before recording. If it runs over 3:00, shorten block 6.
- Keep each image on screen for at least 15 seconds so it can be read.
- Before uploading, check frame by frame that no VCF data or patient information appears.
- Team name for the title and credits: **A3 EMBS ITBA**.
