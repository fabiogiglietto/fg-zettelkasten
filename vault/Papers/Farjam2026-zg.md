---
title: "A practical guide and case study on how to instruct LLMs for automated coding during content analysis"
aliases: ["A practical guide and case study on how to instruct LLMs for automated coding during content analysis"]
authors: ["Mike Farjam", "Hendrik Meyer", "Meike Lohkamp"]
year: 2026
doi: 10.1177/08944393251349541
bibtex_key: Farjam2026-zg
topics: [llm-augmented-research-methods, computational-methods-llms]
citation_count: 15
open_access: false
source_url: https://doi.org/10.1177/08944393251349541
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Farjam2026-zg.mp3
pdf_available: true
discovery_date: 2026-11-01T23:59:54.656717Z
---

# A practical guide and case study on how to instruct LLMs for automated coding during content analysis

> Farjam, M., Meyer, H., & Lohkamp, M. (2026). A practical guide and case study on how to instruct LLMs for automated coding during content analysis. *Social Science Computer Review*, *44*, 488–502. https://doi.org/10.1177/08944393251349541
>
> [View paper](https://doi.org/10.1177/08944393251349541)

## Summary

This paper provides a hands-on methodological guide for using large language models to augment or replace human coders in content analysis, aimed at the practical constraints of typical university researchers. The authors demonstrate their approach by replicating and extending Feldman et al.'s (2015) study of U.S. newspaper climate change coverage, building an agentic workflow that runs locally on consumer-grade hardware using the open-weight Llama 3.1 model. They validate the workflow against human expert coding, scale the analysis tenfold to the full corpus, and extend it to a German-language corpus without translating the coding instructions. The central argument is that LLMs can achieve acceptable reliability for most coding concepts while offering cost-effective, privacy-preserving, multilingual, and transparent coding — though abstract constructs remain stubbornly hard to code.

## Key Contributions

- A concrete, replicable step-by-step framework for integrating LLMs into content analysis workflows.
- A chain-of-thought **Judge agent** that adjudicates conflicting codings by weighing reasoning quality, rather than simple majority/ensemble voting.
- Demonstration that locally deployed, open-weight LLMs on consumer-grade hardware can satisfy researchers' computational, legal, and privacy constraints.
- Empirical evidence for translation-free multilingual coding and for richer per-impact/per-action coding that surpasses binary human-coded schemes.
- Practical recommendations on prompt engineering, train/validation splits to avoid overfitting, and handling proprietary multilingual data.

## Methods

The authors deploy an agentic pipeline built on Llama 3.1–70b (6-bit quantization) running locally on high-end consumer hardware (two Apple M3 Max machines). The pipeline has four roles: a **Human Intermediary** (prompt refinement and validation), an **Instructor agent** (meta-prompting to generate LLM-friendly prompts), a **Classifier agent** (per-document coding with memory reset and chain-of-thought reasoning requiring direct text quotes), and an optional **Judge agent** that resolves conflicts between multiple Classifier runs. Prompt engineering combined meta-prompting, task decomposition, anti-hallucination reminders, and run pooling/adjudication. Validation followed a machine-learning style 80/20 split (513 training / 129 validation articles) assessing Krippendorff's alpha, before scaling to the full 3,274-article U.S. corpus and a comparable 4,863-article German corpus from four ideologically diverse dailies.

## Findings

- A single Classifier yielded reliabilities of roughly 0.60–0.74; adding the Judge agent raised most alphas above 0.7 (e.g., Frame to 0.74 US / 0.80 German; Timing to 0.81).
- The Judge agent improved human–LLM alignment but increased sensitivity, with the LLM identifying coded variables more often than human coders — though substantive results were unchanged.
- Multilingual performance was comparable across English and German using identical, untranslated instructions.
- The abstract "efficacy" construct stayed below the 0.7 threshold in both languages even after three refinement cycles, likely due to conceptual vagueness.
- Reliability gains plateaued after about two prompt-refinement iterations.
- The full analysis required roughly two weeks of continuous computation, illustrating the trade-off between subtask decomposition, repeated runs, and processing time.

## Connections

This paper sits within the methodological debate over automating content analysis and shares concerns about validation, reliability, and human-in-the-loop oversight with work that benchmarks and validates LLM annotation against human coders, such as [[Gilardi2026-hw]], [[DiGiuseppe2026-pu]], [[Balluff2026-if]], and [[Nenno2025-xa]]. Its emphasis on locally deployed open-weight models and reproducible pipelines connects to broader reflections on LLMs as research tools in Bail-style computational communication — most directly to [[Alizadeh2026-es]] and [[Le-Mens2025-qz]] on scaling text classification, while its agentic, reasoning-based adjudication design extends ensemble-style approaches discussed in [[DeVerna2025-dl]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Farjam2026-zg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
