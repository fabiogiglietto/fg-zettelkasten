---
title: "Positioning political texts with large language models by asking and averaging"
aliases: ["Positioning political texts with large language models by asking and averaging"]
authors: ["Gaël Le Mens", "Aina Gallego"]
year: 2025
doi: 10.1017/pan.2024.29
bibtex_key: Le-Mens2025-qz
topics: [llms-in-content-analysis, political-polarization-partisanship]
citation_count: 21
open_access: false
source_url: https://doi.org/10.1017/pan.2024.29
podcast_url: 
pdf_available: false
discovery_date: 2025-01-15T00:00:00Z
---

# Positioning political texts with large language models by asking and averaging

> Mens, G. L., & Gallego, A. (2025). Positioning political texts with large language models by asking and averaging. *Political Analysis*, 1–9. https://doi.org/10.1017/pan.2024.29
>
> [View paper](https://doi.org/10.1017/pan.2024.29)

## Summary

This paper proposes a strikingly simple method for scaling political texts along policy and ideological dimensions: prompt an instruction-tuned LLM (GPT-4, Llama 3, MiXtral, or Aya) to place a short text — a tweet or sentence — on a specified dimension, then average the model's responses across many such texts to estimate the position of a political actor or longer document. Validated against established benchmarks across US Senators' tweets, UK party manifestos, and multilingual EU policy speeches, the "ask and average" approach yields position estimates that correlate strongly with conventional measures, suggesting that off-the-shelf LLMs can serve as competent measurement instruments without bespoke training.

## Key Contributions

- Introduces an "ask and average" prompting methodology for placing political texts on policy/ideological dimensions using off-the-shelf instruction-tuned LLMs.
- Demonstrates the approach generalizes across multiple LLMs, text genres, and 10 languages without supervised fine-tuning or task-specific training data.
- Provides empirical validation against established political positioning benchmarks across three distinct case studies.
- Offers a methodological alternative to traditional scaling techniques (e.g., Wordscores, Wordfish) within the text-as-data tradition.

## Methods

The authors prompt instruction-tuned LLMs to rate where a given short text falls on a specified policy or ideological scale, then aggregate (average) those scores across many texts associated with the same actor or document. The procedure is applied to three corpora: US Senators' tweets, UK party manifestos parsed into sentences, and EU policy speeches in 10 languages. Estimates are validated by correlating them with established benchmark measures of political positioning. Four LLMs (GPT-4, Llama 3, MiXtral, Aya) are compared.

## Findings

- LLM-derived position estimates correlate strongly with benchmark measures across all three case studies.
- The method works robustly across different LLMs, text types, and languages, including in fully multilingual EU speech data.
- Averaging across many short-text judgments produces stable, actor- or document-level estimates from inherently noisy individual ratings.

## Connections

This paper is closely related to broader efforts using LLMs as measurement tools for political and ideological content, including work on ideological scaling and classification such as [[DiGiuseppe2026-pu]], [[DiGiuseppe2025-es]], and [[Tornberg2025-ir]]. It also speaks to the wider methodological agenda on validating LLMs as social-science instruments seen in [[Balluff2026-if]] and [[Tan2024-vl]], and connects to studies probing LLMs' own political dispositions like [[DeVerna2025-dl]].
