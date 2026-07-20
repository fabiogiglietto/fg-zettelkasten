---
title: "Evaluating how LLM annotations represent diverse views on contentious topics"
aliases: ["Evaluating how LLM annotations represent diverse views on contentious topics"]
authors: ["Megan A. Brown", "Shubham Atreja", "Libby Hemphill", "Patrick Y. Wu"]
year: 2025
doi: 
bibtex_key: Brown2025-jk
topics: [llm-computational-content-analysis, survey-methodology-validity]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2503.23243v2
podcast_url: 
pdf_available: true
discovery_date: 2025-03-15T00:00:00Z
---

# Evaluating how LLM annotations represent diverse views on contentious topics

> Brown, M. A., Atreja, S., Hemphill, L., & Wu, P. Y. (2025). Evaluating how LLM annotations represent diverse views on contentious topics. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2503.23243v2)

## Summary

This paper asks whether generative LLMs systematically privilege majority demographic perspectives when used to annotate subjective text — a growing practice in computational social science. Across four contentious annotation datasets, three LLMs, and three semantically equivalent prompts per dataset (~75K annotations), the authors regress LLM-human agreement on annotator demographics, label entropy, prompt, and model. They find that demographic biases are small, dataset-specific rather than model-specific, and dwarfed by the effect of item difficulty: when humans disagree, LLMs disagree with humans too. The upshot is that fairness audits of LLM annotation cannot rely on swapping models or prompts and must contextualize bias claims within task difficulty.

## Key Contributions

- First systematic audit of demographic bias in LLM annotations spanning multiple subjective datasets, models, and prompts simultaneously.
- Introduces label entropy (human annotator disagreement) as a co-predictor of LLM-human agreement, separating item difficulty from demographic bias.
- Reframes LLM annotation bias as a dataset-contextual phenomenon rather than a generalized majority-group bias inherited from training data.
- Provides actionable guidance for practitioners: context-specific audits, skepticism toward model-swapping as a mitigation, and integration of difficulty measures into fairness assessments.

## Methods

The authors annotate four datasets (NLPositionality toxicity, POPQUORN offensiveness and politeness, Wikipedia toxicity — the latter stratified to ~2,095 items by entropy) using GPT-4o mini, Llama 3.3 70B Instruct, and Gemini 1.5 Flash with default hyperparameters and three semantically equivalent prompts each. Demographics are recoded into binary majority/minority categories (gender, race, education) for cross-dataset comparability. Logistic regressions predict per-annotation LLM-human agreement from demographics, normalized label entropy, prompt version, and model, with Bonferroni correction and robustness checks omitting entropy. GPT-4o mini is used as a downstream extractor to standardize free-form LLM outputs into discrete labels.

## Findings

- Agreement probabilities by demographic group cluster narrowly between ~0.46 and 0.55 — statistically significant differences are substantively small.
- Direction of demographic bias is consistent across the three LLMs *within* a dataset but flips across datasets: NLPositionality favors minority annotators; POPQUORN Politeness favors college-educated and white annotators; Wikipedia toxicity favors male annotators.
- Label entropy is by far the dominant predictor of (dis)agreement, with effect sizes much larger than demographics, model, or prompt.
- Omitting entropy from regressions leaves demographic coefficients largely unchanged, so difficulty is not masking demographic effects — it is a separate, larger source of disagreement.
- Switching LLMs or prompts produces only marginal shifts in bias and does not consistently mitigate it.

## Connections

This work directly engages debates about whether LLMs can stand in for human coders in computational social science, complementing [[Le-Mens2025-qz]] and [[Tan2024-vl]] on LLM annotation validity and [[Balluff2026-if]] on measurement quality. Its emphasis on dataset-contextual rather than model-intrinsic bias resonates with [[DeVerna2025-dl]] and broader concerns about LLM ideological and demographic skew explored in [[Hackenburg2025-dj]]. The finding that prompt variation has limited effect also speaks to persona-prompting and perspective-aware annotation lines indirectly addressed by [[Tornberg2025-ir]] and [[Tornberg2026-lc]].
