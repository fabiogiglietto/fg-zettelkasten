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

This opinion piece offers a critical overview of how large language models (LLMs) have been adopted in political communication research, identifying underacknowledged epistemic, environmental, infrastructural, and ethical trade-offs across three application domains: text analysis, synthetic data generation, and experiments/simulations. The authors do not call for rejecting LLMs but for *reflexive*, task-appropriate use — arguing that researchers should adopt a "trade-off mindset" in which the least resource-intensive method capable of handling a task's complexity is preferred. They warn that the field's rapid embrace of commercial LLMs risks compromising reproducibility, scholarly autonomy, and open science, while obscuring substantial environmental costs and demographic biases.

## Key Contributions

- A structured critique of LLM use across three concrete application areas in political communication.
- A "trade-off mindset" framework (with an accompanying conceptual diagram) for selecting text-as-data methods based on task complexity vs. resource cost.
- Foregrounding of corporate dependency, opaque guardrails, environmental footprint, and demographic bias as first-order methodological concerns.
- Concrete recommendations: prefer open-weight models, develop rigorous LLM validation procedures, and pursue community-trained, domain-specific scientific models via international collaboration.
- Application of the "stochastic parrots" framing to clarify the non-epistemic, regurgitative nature of LLM outputs.

## Methods

A conceptual, critical essay synthesizing recent literature on LLMs in social science and political communication, drawing on debates from the COMPTEXT 2025 conference. The argument is organized around three application domains (classification/annotation, synthetic data, experiments/simulations) and supported by a conceptual diagram mapping methods along axes of task complexity and resource cost.

## Findings

- Prompt-based LLM classification is fragile: prompts are hard to optimize, and silent model updates (e.g., the GPT-4 → GPT-5 retirement) break replication.
- For many text analysis tasks, smaller models (encoder-only transformers, SVMs) match LLM performance at far lower cost.
- Multilingual LLM performance skews toward Western languages; quantization further degrades performance on complex tasks and low-resource languages.
- LLM-generated personas produce stereotypical, demographically narrow outputs with limited algorithmic fidelity for non-Western or politically diverse subpopulations.
- Synthetic data shows reduced linguistic variation and regression-to-the-mean, distorting downstream training and inference.
- Commercial guardrails can refuse politically sensitive content (e.g., DeepSeek on Tiananmen/Taiwan; OpenAI's "David Mayer" incident), constraining research validity.
- LLM use carries substantial — and rarely accounted-for — environmental costs (energy, water, carbon, minerals).
- Field deployments of LLM agents (e.g., the Reddit persuasion experiment) reveal that IRBs are ill-equipped to evaluate LLM-related research ethics.

## Connections

This piece sits alongside other critical and validation-oriented work on LLM-based measurement and simulation. It connects directly to concerns about LLM annotation reliability and prompt sensitivity raised in [[Pante2025-pq]] and Bastos2025-ol, and to debates about LLM-generated synthetic survey data and persona simulation in [[Hackenburg2025-dj]] and [[Bak-Coleman2026-mk]]. The ethical critique of field-deployed LLM agents resonates with the broader political-communication and persuasion concerns in [[DeVerna2025-dl]] and [[Allen2025-ot]], while the call for heterodox, reflexive computational social science aligns with [[Tornberg2025-ir]] and [[Munger2025-cz]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-if.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-llms-are-we-sacrificing-rigor-for/id1866587707?i=1000750775663)
