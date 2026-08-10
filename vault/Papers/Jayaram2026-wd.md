---
title: "Towards automating scientific review with Google&#x27;s Paper Assistant Tool"
aliases: ["Towards automating scientific review with Google&#x27;s Paper Assistant Tool"]
authors: ["Rajesh Jayaram", "Drew Tyler", "David Woodruff", "Corinna Cortes", "Yossi Matias", "Vahab Mirrokni", "Vincent Cohen-Addad"]
year: 2026
doi: 
bibtex_key: Jayaram2026-wd
topics: [llm-augmented-research-methods, llms-for-content-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.28277v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Jayaram2026-wd.mp3
pdf_available: true
discovery_date: 2026-07-02T11:04:44.126112Z
---

# Towards automating scientific review with Google&#x27;s Paper Assistant Tool

> Jayaram, R., Tyler, D., Woodruff, D., Cortes, C., Matias, Y., Mirrokni, V., & Cohen-Addad, V. (2026). Towards automating scientific review with Google&#x27;s Paper Assistant Tool. *arXiv [cs.LG]*.
>
> [View paper](http://arxiv.org/abs/2606.28277v1)

## Summary

This paper introduces the Paper Assistant Tool (PAT), an agentic AI system built at Google Research to perform deep verification of mathematics and computer science manuscripts. PAT segments a paper, adaptively allocates inference compute across sections, dispatches parallel Deep Review agents powered by Gemini Deep Think, and synthesizes their findings while grounding claims through Google Search. The authors argue that orchestrated, inference-scaled pipelines meaningfully outperform single-shot LLM review, report a 34-point gain over zero-shot Gemini 3.1 Pro on the SPOT proof-error benchmark, and describe pilot deployments at STOC 2026 and ICML 2026 covering more than 4,700 submissions. They also propose a four-level taxonomy of AI roles in peer review to structure policy debate about how far such systems should be trusted.

## Key Contributions

- A concrete agentic architecture (segmentation → adaptive compute budgeting → parallel deep-review agents → grounded synthesis) specialized for detecting proof, equation, and experimental errors.
- Benchmark evidence on the SPOT math/CS subset that orchestrated inference scaling substantially outperforms both zero-shot Gemini 3.1 Pro and the prior SPOT SOTA.
- Real-world pilot data from STOC 2026 and ICML 2026, including author surveys reporting perceived helpfulness, groundedness, and downstream actions taken.
- A four-level taxonomy of AI in peer review (Author Tool, Reviewer Tool, Supporting Reviewer, Total Automation), analogous to SAE autonomy levels.
- A governance-oriented discussion of accountability, deskilling, compute equity, adversarial gaming, and reviewer diversity under increasing AI mediation.

## Methods

PAT is designed as a four-stage pipeline: document segmentation, per-section compute budgeting across Light/Medium/High Thinking tiers, parallel Deep Review agents based on Gemini Deep Think, and a synthesis agent that uses Google Search to ground claims. Evaluation used a filtered SPOT subset of 26 papers with 29 equation/proof errors in math and CS, compared against zero-shot Gemini 3.1 Pro and the original SPOT SOTA, with an LLM grader assessing logical equivalence to ground-truth errors and human audit by the authors. Pilot deployments provided pre-submission PAT reviews at STOC 2026 (n=124 surveyed authors) and ICML 2026 (n=733 surveyed authors), yielding both quantitative usefulness ratings and qualitative feedback.

## Findings

- On the SPOT math/CS proof-error subset, PAT reached 89.7% detection accuracy versus 55.2% for zero-shot Gemini 3.1 Pro and 21.1% for the original SPOT SOTA.
- PAT produced concrete counterexamples (e.g., in a dual Banach spaces paper) that zero-shot models missed.
- 97% of STOC and 92.1% of ICML surveyed authors said they would use PAT again; roughly 90% rated feedback as Very or Mostly Helpful.
- 11.6% of STOC and 35.4% of ICML respondents reported PAT surfaced substantive theoretical gaps taking over an hour to address.
- 31% of ICML respondents ran new experiments in response to PAT feedback.
- Only 55.8% (STOC) and 64.8% (ICML) rated the feedback as mostly or fully grounded, indicating residual hallucination.
- Reported failure modes include knowledge-cutoff hallucinations, PDF parsing errors, and false claims that a proof is incorrect.
- Contextual data cited by the authors: submissions to ICLR/ICML/NeurIPS grew from ~17k in 2020 to an estimated ~74k in 2026, and Pangram estimated 21% of ICLR 2026 reviews were fully AI-generated.

## Connections

No related papers have been supplied under shared topics, so there are no wikilinks to make here. Intellectually, the work sits alongside the SPOT verification benchmark it evaluates on, LLM-in-peer-review measurement studies such as the Pangram estimates and NeurIPS consistency experiments, and the broader literature on agentic inference-time scaling and tool-augmented mathematical reasoning.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Jayaram2026-wd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
