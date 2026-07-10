---
title: "Newer, larger, better? A critique of the unreflective LLM adoption in communication research"
aliases: ["Newer, larger, better? A critique of the unreflective LLM adoption in communication research"]
authors: ["Paul Balluff", "Justin Chun-ting Ho", "Johannes B. Gruber", "Sean Palicki", "Alexis Palmer", "Luca Rossi", "Irina Shklovski", "Chung-hong Chan"]
year: 2026
doi: 10.1080/10584609.2026.2618486
bibtex_key: Balluff2026-if
topics: [llms-computational-content-analysis, information-disorder]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/10584609.2026.2618486
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-if.mp3
pdf_available: true
discovery_date: 2026-02-20T13:52:33.451450Z
---

# Newer, larger, better? A critique of the unreflective LLM adoption in communication research

> Balluff, P., Ho, J. C., Gruber, J. B., Palicki, S., Palmer, A., Rossi, L., Shklovski, I., & Chan, C. (2026). Newer, larger, better? A critique of the unreflective LLM adoption in communication research. *Political Communication*, 1–10. https://doi.org/10.1080/10584609.2026.2618486
>
> [View paper](https://doi.org/10.1080/10584609.2026.2618486)

## Summary

This opinion piece delivers a critical assessment of how large language models are being taken up in political communication research, spanning three main use cases: text analysis, synthetic data generation, and experiments/simulations. The authors argue that the field's rapid adoption of LLMs has been largely unreflective, downplaying serious epistemic, environmental, infrastructural, and ethical trade-offs — reproducibility failures, dependency on opaque corporate products, language and demographic bias, and substantial computational costs. Rather than rejecting LLMs, they advocate a "trade-off mindset": choose the least resource-intensive method capable of handling a task's complexity, prefer open-weight and task-appropriate alternatives, and cultivate community-built, domain-specific scientific models.

## Key Contributions

- A structured critique of LLM use across three application domains in political communication.
- A "trade-off mindset" and accompanying conceptual model (Figure 1) mapping task complexity against resource cost for text-as-data methods.
- Surfacing of overlooked issues — corporate dependency, guardrails, environmental cost, demographic bias — for a communication research audience.
- Concrete recommendations: favour open-weight models, build rigorous validation procedures, and pursue internationally collaborative, specialized scientific models.
- Deployment of the "stochastic parrots" framing to underscore the non-epistemic, regurgitative nature of LLMs.

## Methods

A conceptual, critical essay synthesizing recent social-science and political-communication literature on LLMs, informed by debates from the COMPTEXT 2025 conference panels. It uses a conceptual diagram to illustrate the task-complexity/resource-cost trade-off, and reviews applications in text classification and annotation, synthetic data generation (survey, social media, and training data), and human-machine communication experiments and agent-based simulations.

## Findings

- Prompt-based LLM classification is fragile; provider configuration changes (e.g., GPT-4 retirement for GPT-5) can break replication.
- Multilingual performance is biased toward Western languages, and quantization degrades performance on complex tasks and low-resource languages.
- LLM-generated personas are stereotypical and demographically narrow, with poor algorithmic fidelity for non-Western or politically diverse sub-populations.
- Synthetic data shows reduced variation and regression-to-the-mean in linguistic features, distorting downstream training and conclusions.
- Commercial guardrails refuse politically sensitive content (e.g., DeepSeek on Tiananmen/Taiwan; the "David Mayer" incident), constraining validity.
- LLMs carry rarely-accounted-for environmental costs — energy, water, carbon, mineral extraction.
- Field deployments of LLM agents (e.g., the Reddit persuasion case) reveal that IRBs struggle to evaluate LLM-related research ethics.
- For many text tasks, smaller models (encoder-only transformers, SVMs) perform comparably at far lower cost.

## Connections

This critique speaks directly to work validating and benchmarking LLMs for content analysis and annotation, such as [[Le-Mens2025-qz]], [[Tornberg2025-ir]], and [[Balluff2026-bv]] (a co-authored companion effort), and to studies using LLM agents or synthetic data in experiments and simulations like [[Hackenburg2025-dj]]. Its methodological caution is relevant to the broader information-disorder literature that increasingly relies on automated classification, including [[DeVerna2025-dl]] and [[Pierri2025-hm]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-if.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-llms-are-we-sacrificing-rigor-for/id1866587707?i=1000750775663)
