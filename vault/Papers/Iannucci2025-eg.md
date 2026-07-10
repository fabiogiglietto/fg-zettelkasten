---
title: "Detecting coordinated activities through temporal, multiplex, and collaborative analysis"
aliases: ["Detecting coordinated activities through temporal, multiplex, and collaborative analysis"]
authors: ["Letizia Iannucci", "Elisa Muratore", "Antonis Matakos", "Mikko Kivelä"]
year: 2025
doi: 
bibtex_key: Iannucci2025-eg
topics: [coordinated-inauthentic-behavior, computational-network-structure-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2512.19677v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iannucci2025-eg.mp3
pdf_available: true
discovery_date: 2025-12-15T00:00:00Z
---

# Detecting coordinated activities through temporal, multiplex, and collaborative analysis

> Iannucci, L., Muratore, E., Matakos, A., & Kivelä, M. (2025). Detecting coordinated activities through temporal, multiplex, and collaborative analysis. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2512.19677v1)

## Summary

This paper introduces a framework for detecting coordinated inauthentic behavior (CIB) that combines two ideas: a time-aware collaboration model and a multiplex network representation of user activity. The authors extend Newman's node-normalized collaboration model with an exponential decay temporal kernel, so that co-actions closer in time contribute more strongly to inferred coordination, and they represent different coordination modalities (hashtags, retweets, mentions, URLs) as separate layers of a multiplex network rather than aggregating them into one. The core argument is that both *temporal proximity* and *frequency* of co-actions are needed to distinguish deliberate coordination from coincidental synchronicity, and that keeping modalities separate makes detection more robust against dilution tactics. Validated on synthetic simulations and 26 labeled datasets, the multiplex time-aware model achieves the best average rank on weighted precision and second-best across all metrics.

## Key Contributions

- A time-aware extension of Newman's node-normalized collaboration model, weighting co-actions with an exponential temporal decay kernel over time differences.
- A multiplex framework that separates and integrates coordination evidence across modalities without prior knowledge of which modality or time scale is exploited.
- A data-driven, modularity-maximizing procedure for selecting the per-layer temporal decay parameter β_a.
- A new weighted precision metric (WP = Σn_k p_k² / Σn_k p_k) that penalizes trivial/singleton clusters and rewards cohesive identification of coordinated groups.
- A reproducible benchmark of 12+ detection methods across 26 labeled datasets, with open-source code released.

## Methods

The latent collaboration network is built per modality, with edge weights combining Newman's normalization and an exponential decay over the time gap between users' co-actions. A tolerance cutoff (Δt_max = -ln(ε)/β_a) keeps computational complexity sub-quadratic. Each modality forms its own layer of a multiplex network; the decay parameter β_a is chosen per layer by scanning values (0–10, step 0.01) and selecting the one maximizing modularity of the Leiden partition. Community detection uses the Leiden algorithm optimizing multislice weighted modularity. The approach is validated on synthetic simulations of three coordination patterns (synchronous bursts, alternating bursts with inactivity, alternating subsets of active accounts) and benchmarked against baselines including co-hashtag sequences, rapid retweets at fixed windows, co-retweet cardinality, text-similarity methods, synchronized action frameworks, AMDN-HAGE variants, and BLOC, using F1*, precision*, recall*, homogeneity, NMI, and WP.

## Findings

- On synthetic simulations the time-aware multiplex model achieved perfect scores (F1*, homogeneity, WP = 1.00) across all three coordination patterns.
- The 4-layer time-aware multiplex model achieved the best average rank (3.12) on weighted precision and second-best (5.10) across all six metrics on 26 datasets.
- Individual time-aware monoplex layers (retweet, mention, hashtag) outperformed most single-modality baselines, including fixed-window rapid-retweet methods.
- Single-modality methods showed high variance — e.g. co-retweet methods failed on Iran campaigns dominated by text/hashtag coordination — while the multiplex approach stayed robust.
- Some baselines achieved high precision/homogeneity only by producing trivial singleton clusters; WP penalizes this and confirms the multiplex model's practical superiority.
- Multiplex clustering can fragment communities visible in a single layer, raising precision but reducing recall — a trade-off between integration and within-layer cohesion.

## Connections

This paper builds directly on the multiplex/temporal coordination detection tradition and shares its benchmark-and-method framing with [[Luceri2025-tr]] and [[Minici2024-tf]], which similarly develop and evaluate coordination-detection pipelines on labeled information-operations data. It also connects to the Giglietto group's work on coordinated link and content sharing detection ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2026-9b6a992d]]), which likewise reasons about temporal co-action windows across modalities, and to broader network-structural analyses of coordinated behavior such as [[Gerard2025-br]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iannucci2025-eg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-detecting-coordinated-activities/id1866587707?i=1000743818634)
