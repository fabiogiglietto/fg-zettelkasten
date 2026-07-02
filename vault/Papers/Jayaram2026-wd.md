---
title: "Towards automating scientific review with Google&#x27;s Paper Assistant Tool"
aliases: ["Towards automating scientific review with Google&#x27;s Paper Assistant Tool"]
authors: ["Rajesh Jayaram", "Drew Tyler", "David Woodruff", "Corinna Cortes", "Yossi Matias", "Vahab Mirrokni", "Vincent Cohen-Addad"]
year: 2026
doi: 
bibtex_key: Jayaram2026-wd
topics: []
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.28277v1
podcast_url: 
pdf_available: true
discovery_date: 2026-07-02T11:04:44.126112Z
---

# Towards automating scientific review with Google&#x27;s Paper Assistant Tool

> Jayaram, R., Tyler, D., Woodruff, D., Cortes, C., Matias, Y., Mirrokni, V., & Cohen-Addad, V. (2026). Towards automating scientific review with Google&#x27;s Paper Assistant Tool. *arXiv [cs.LG]*.
>
> [View paper](http://arxiv.org/abs/2606.28277v1)

## Summary

This paper introduces the Paper Assistant Tool (PAT), an agentic AI system from Google Research designed to detect mathematical, logical, and experimental errors in computer science and mathematics manuscripts. PAT segments a paper, adaptively allocates inference compute across sections, runs parallel deep-review agents built on Gemini Deep Think, and synthesizes findings while grounding claims through Google Search. The authors argue that orchestrated, inference-scaled pipelines materially outperform single-shot LLM verification, reporting a 34-point improvement over zero-shot Gemini 3.1 Pro on the SPOT proof-error benchmark and describing pilot deployments across more than 4,700 STOC 2026 and ICML 2026 submissions. They also propose a four-level taxonomy for AI roles in peer review to structure community discussion about governance and autonomy.

## Key Contributions

- Design of PAT as a four-stage agentic pipeline (segmentation → adaptive compute budgeting → parallel Deep Review agents → grounded synthesis) specialized for proof and experimental verification.
- Empirical evidence on the SPOT math/CS subset that orchestration beats single-shot and Pass@k baselines while preserving precision.
- Large-scale real-world deployment data from STOC 2026 and ICML 2026 pilots, including quantitative author surveys (n=124 and n=733).
- A four-level taxonomy of AI roles in peer review — Author Tool, Reviewer Tool, Supporting Reviewer, Total Automation — analogous to SAE vehicle autonomy levels.
- A governance discussion covering accountability, deskilling, compute equity, adversarial gaming, and preserving diversity of reviewer opinion.

## Methods

PAT is evaluated on a filtered 26-paper, 29-error subset of the SPOT benchmark (Equation/proof errors in Math and CS), against zero-shot Gemini 3.1 Pro and the reported SPOT SOTA. Grading uses an LLM judge assessing logical equivalence to ground-truth errors, with human audit by the authors. Beyond the benchmark, the system was piloted as a pre-submission tool at STOC 2026 (Nov 2025) and ICML 2026 (Jan 2026), with author feedback collected via mixed quantitative/qualitative surveys. The taxonomy component is a conceptual contribution rather than an empirical one.

## Findings

- PAT achieves 89.7% detection accuracy on the SPOT math/CS proof-error subset vs. 55.2% zero-shot Gemini 3.1 Pro and 21.1% original SOTA.
- Case study: PAT constructed a concrete counterexample in a dual Banach spaces paper where zero-shot models accepted the flawed claim.
- 97% (STOC) and 92.1% (ICML) of surveyed authors said they would use PAT again; ~90% found the feedback helpful.
- 11.6% (STOC) and 35.4% (ICML) reported PAT surfaced substantive theoretical gaps requiring more than an hour to address.
- 31% of ICML respondents ran new experiments in response to PAT's feedback.
- Grounding remains imperfect: only 55.8% (STOC) and 64.8% (ICML) rated feedback as mostly or fully grounded; failure modes include knowledge-cutoff hallucinations, PDF parsing errors, and spurious "proof is incorrect" claims.
- Contextual growth data cited: AI conference submissions rose from ~17k (2020) to an estimated ~74k (2026), with an external estimate that 21% of ICLR 2026 reviews were fully AI-generated.

## Connections

No related papers have been provided under shared topics, so there are no wikilinks to make here. Intellectually, the work sits alongside the SPOT verification benchmark, NeurIPS reviewer-consistency studies, and the broader literature on LLM-assisted mathematical proof checking and agentic inference scaling.
