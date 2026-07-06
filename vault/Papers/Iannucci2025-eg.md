---
title: "Detecting coordinated activities through temporal, multiplex, and collaborative analysis"
aliases: ["Detecting coordinated activities through temporal, multiplex, and collaborative analysis"]
authors: ["Letizia Iannucci", "Elisa Muratore", "Antonis Matakos", "Mikko Kivelä"]
year: 2025
doi: 
bibtex_key: Iannucci2025-eg
topics: [coordinated-inauthentic-behavior, computational-social-science]
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

This paper introduces a framework for detecting coordinated inauthentic behavior (CIB) on social media that simultaneously addresses two underexploited signals: the *temporal proximity* of co-actions and the *modality* through which coordination occurs. The authors extend Newman's node-normalized collaboration model with an exponential temporal-decay kernel, then layer it into a multiplex network in which hashtag, retweet, mention, and URL co-actions form separate slices linked across users. Per-layer decay parameters are chosen by maximizing Leiden modularity, and multiplex community detection extracts coordinated groups. Validated on synthetic patterns and benchmarked against 12+ baselines on the 26 labeled datasets from Seckin et al. (2025), the multiplex time-aware model attains the best mean rank on weighted precision and the second-best mean rank overall, with notable robustness when adversaries dilute coordination across modalities.

## Key Contributions

- Time-aware extension of Newman's collaboration model using an exponential decay kernel over inter-action time differences.
- Multiplex representation that preserves modalities (hashtag/retweet/mention/URL) rather than collapsing them, providing resilience to cross-modality "dilution" tactics.
- Modularity-driven, per-layer selection of the temporal decay parameter β_a, removing the need to assume a coordination time-scale a priori.
- A new *weighted precision* metric (WP = Σn_k p_k² / Σn_k p_k) that penalizes trivial singleton clusters favored by some prior methods.
- Open-source implementation and a reproducible benchmark of 12+ detection methods across 26 labeled influence operation datasets.

## Methods

The authors build latent collaboration networks where edge weights between users are computed from time-discounted co-action counts, normalized by each user's total activity. They construct one such network per modality and assemble them into a multiplex graph, then apply the Leiden algorithm optimizing multislice weighted modularity (Mucha et al. 2010). A tolerance cutoff Δt_max = −ln(ε)/β_a keeps computational complexity sub-quadratic. Evaluation uses three synthetic coordination regimes (synchronous bursts, alternating bursts, rotating active subsets) and the 26 Seckin et al. labeled datasets, with F1*, precision*, recall*, homogeneity, NMI, and WP as metrics. Baselines include co-hashtag sequences, fixed-window rapid retweets, co-retweet cardinality, text similarity, synchronized-action frameworks, AMDN-HAGE variants, and BLOC.

## Findings

- Perfect detection (F1*, homogeneity, WP = 1.00) on all three synthetic coordination patterns.
- Best mean rank (3.12) on weighted precision and second-best mean rank (5.10) across all six metrics on the 26-dataset benchmark.
- Single time-aware monoplex layers already outperform most single-modality baselines, including fixed-time-window retweet methods.
- Single-modality baselines collapse on campaigns whose primary modality differs (e.g., co-retweet methods fail on hashtag-driven Iran campaigns), whereas the multiplex approach remains stable.
- Some high-precision baselines (Magelinski 2022; Ng & Carley 2022) achieve their scores via trivial singleton clusters — WP exposes this artifact.
- Trade-off observed: multiplex integration can fragment communities that look cohesive in a single layer, raising precision but lowering best-cluster recall.

## Connections

This work belongs to the latent-coordination-network strand of CIB detection and directly engages benchmark efforts and similarity-based detection pipelines such as [[Luceri2025-tr]], [[Minici2024-tf]], and [[Bouchaud2026-lr]], while sharing the multimodal/multilayer impulse with [[Kulichkina2026-zk]] and [[Schroeder2026-im]]. Its critique of fixed time-window and single-modality detectors resonates with methodological discussions in [[Graham2025-gp]], Bastos2025-ya, and [[Freelon2024-sc]], and its benchmark posture parallels reproducibility-oriented work like [[Murtfeldt2025-wu]] and [[Lai2024-to]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iannucci2025-eg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-detecting-coordinated-activities/id1866587707?i=1000743818634)
