---
title: "Exploring temporal dynamics in digital trace data: mining user-sequences for communication research"
aliases: ["Exploring temporal dynamics in digital trace data: mining user-sequences for communication research"]
authors: ["Yangliu Fan", "Jakob Ohme", "Lion Wedel"]
year: 2026
doi: 10.1080/19312458.2026.2664873
bibtex_key: Fan2026-af
topics: [computational-methods-llms, computational-network-structure-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/19312458.2026.2664873
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Fan2026-af.mp3
pdf_available: true
discovery_date: 2026-06-06T11:01:38.221976Z
---

# Exploring temporal dynamics in digital trace data: mining user-sequences for communication research

> Fan, Y., Ohme, J., & Wedel, L. (2026). Exploring temporal dynamics in digital trace data: mining user-sequences for communication research. *Communication Methods and Measures*, 1–28. https://doi.org/10.1080/19312458.2026.2664873
>
> [View paper](https://doi.org/10.1080/19312458.2026.2664873)

## Summary

This paper proposes a methodological reorientation for communication research toward analyzing the fine-grained temporal structure of digital trace data (DTD). The authors argue that the field has long theorized communication as a dynamic process while empirically relying on cross-sectional, time-aggregated measures. To close this gap, they introduce the concept of "user-sequences" — chronologically ordered streams of timestamped user activity — and review six computational approaches for analyzing them: sequence analysis, event history analysis, hidden Markov models, network analysis, process mining, and language-based embedding models. A case study using 1.26 million donated traces from 309 German users across Facebook, Instagram, TikTok, and YouTube illustrates what each method reveals and where each falls short on practical challenges like data volume, complexity, incompleteness, time-window selection, and cross-platform alignment.

## Key Contributions

- Articulates the "user-sequence" framework as a way to preserve hyper-longitudinal information rather than aggregating DTD into static measures.
- Provides an integrated review of six computational methods, mapping them to communication research questions.
- Demonstrates all six methods empirically on a large, donated multi-platform dataset, with code shared via OSF.
- Offers a structured comparison of each method's strengths and weaknesses against six practical DTD challenges (volume, complexity, incompleteness/skewness, time window, alignment, volatility).
- Argues that language-based sequence models are the most promising frontier for causal inference and person-level summarization, while highlighting infrastructural needs for shared training data.

## Methods

The paper combines conceptual framework development with a methodological review and an applied case study. The dataset comprises 1,262,775 timestamped activity traces donated by 309 German participants between May and August 2024, collected via Data Download Package donation as part of a two-wave panel (recruited via Bilendi, oversampling 18–27 year-olds). Implementations include optimal matching with hierarchical clustering and sliding-window n-gram mining for sequence analysis; Kaplan-Meier and Cox proportional hazards models for event history; HMMs selected via AIC/BIC; weighted directed networks with Clauset-Newman-Moore community detection; BPMN process discovery via directly-follows graphs; and 100-dimensional word2vec-style embeddings visualized with t-SNE.

## Findings

- Most donated user-sequences were dominated by a single platform; optimal-matching clustering produced 20 clusters but struggled with extreme variation in sequence lengths.
- Frequent subsequence motifs were dominated by repeated identical actions and within-platform transitions (e.g., Instagram like→share, TikTok watch→favorite), with results sensitive to time-window choice.
- Most sessions ended within two hours; Facebook and Instagram had significantly higher hazards of platform-switching than YouTube, while TikTok was slightly less likely to switch.
- A four-state HMM on daily sequences mapped hidden states onto the four platforms, with high self-transition probabilities.
- Network analysis (modularity Q=0.34) separated activities into a TikTok+YouTube-watching community and a Facebook/Instagram/YouTube-search community, with TikTok highly central.
- Process mining showed within-platform transitions occur much faster than cross-platform ones (Facebook→Instagram ≈3.4 hours; Instagram→Facebook >9 hours) and identified two stylized daily routines, with YouTube typically terminating them.
- Embeddings organized events primarily by platform but also captured semantic local structure, such as geographic similarity among Facebook search queries for nearby Bavarian towns.

## Connections

This paper connects most directly to other work using donated digital trace data and cross-platform behavioral logs to study media use, such as [[Fan2025-ut]], and to broader methodological discussions of how computational approaches can be tailored to communication research questions ([[Bailard2024-pj]]). Its emphasis on temporal motifs and sequence-level behavior also resonates with work on coordinated and patterned online activity such as [[Giglietto2024-cbeb3f70]] and [[Minici2024-tf]], though those focus on coordination detection rather than individual user trajectories. Beyond these, the methodological agenda stands somewhat apart from the topic cluster's more substantive focus on platform content and LLM-based analysis.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Fan2026-af.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-every-tap-swipe-and-scroll-mining/id1866587707?i=1000772571651)
