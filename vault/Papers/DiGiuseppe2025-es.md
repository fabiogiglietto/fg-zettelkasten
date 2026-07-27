---
title: "Scaling open-ended survey responses using LLM-paired comparisons"
aliases: ["Scaling open-ended survey responses using LLM-paired comparisons"]
authors: ["Matthew DiGiuseppe", "Michael E Flynn"]
year: 2025
doi: 10.31235/osf.io/39ajg_v2
bibtex_key: DiGiuseppe2025-es
topics: [survey-methodology-validity, llm-augmented-research-methods]
citation_count: 1
open_access: false
source_url: https://doi.org/10.31235/osf.io/39ajg_v2
podcast_url: 
pdf_available: false
discovery_date: 2025-01-15T00:00:00Z
---

# Scaling open-ended survey responses using LLM-paired comparisons

> DiGiuseppe, M., & Flynn, M. E. (2025). Scaling open-ended survey responses using LLM-paired comparisons. *SocArXiv*. https://doi.org/10.31235/osf.io/39ajg_v2
>
> [View paper](https://doi.org/10.31235/osf.io/39ajg_v2)

## Summary

This paper introduces a methodology that pairs Large Language Models with paired-comparison techniques to convert open-ended survey responses into continuous latent scales of respondent characteristics. The authors argue that closed-ended items constrain the depth and variance of what can be measured, while traditional hand-coding of open-ended text is too labor-intensive to scale. Existing LLM-based coding approaches help, but have their own limitations. By instead having an LLM perform many pairwise judgments between responses and aggregating these into a scale, the method produces measures of latent traits — knowledge, ideology, emotion, policy positions — that retain the richness of free text while remaining quantitatively tractable.

## Key Contributions

- Proposes a novel LLM-paired comparison framework for scaling open-ended survey responses into continuous latent measures.
- Offers an alternative to direct LLM classification or scoring of texts that leverages the relative-judgment strengths of paired comparisons.
- Provides survey researchers a practical tool for measuring latent constructs (knowledge, ideology, affect, policy preferences) from unstructured responses.
- Bridges traditional survey measurement theory with computational text analysis using generative models.

## Methods

- Open-ended survey responses are passed to an LLM, which renders pairwise judgments comparing pairs of responses on a target latent dimension.
- Paired-comparison aggregation (e.g., Bradley-Terry–style scaling) converts these judgments into a continuous latent scale for respondents.
- The approach is benchmarked against existing LLM-based coding strategies, though the abstract leaves the specifics of validation unspecified.

## Findings

- The abstract does not report specific empirical results; the contribution is primarily methodological.
- The framing argues that paired comparisons mitigate known weaknesses of direct LLM scoring of texts and yield more useful latent measures from open-ended responses.

## Connections

This work belongs to a growing methodological literature on using LLMs as measurement instruments in social science, and connects directly to companion work by one of the authors on LLM-based coding ([[DiGiuseppe2026-pu]]). It also relates to broader efforts to validate and benchmark LLM annotation pipelines in computational social science such as [[Le-Mens2025-qz]] and [[Tornberg2025-ir]], and to studies exploring LLMs as proxies for human respondents and judges like [[Hackenburg2025-dj]].
