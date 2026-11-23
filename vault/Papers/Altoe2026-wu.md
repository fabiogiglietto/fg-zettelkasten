---
title: "Predicting narrative virality on social media streams for pre-peak misinformation triage"
aliases: ["Predicting narrative virality on social media streams for pre-peak misinformation triage"]
authors: ["Filipe Altoe", "Sérgio Miguel Gonçalves Pinto", "H. Sofia Pinto"]
year: 2026
doi: 10.1145/3799682.3840688
bibtex_key: Altoe2026-wu
topics: [information-disorder, computational-methods-llms]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3799682.3840688
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Altoe2026-wu.mp3
pdf_available: true
discovery_date: 2026-11-08T08:13:08.368928Z
---

# Predicting narrative virality on social media streams for pre-peak misinformation triage

> Altoe, F., Pinto, S. M. G., & Pinto, H. S. (2026). Predicting narrative virality on social media streams for pre-peak misinformation triage. *Proceedings of the 35th ACM International Conference on Information and Knowledge Management*, 127–138. https://doi.org/10.1145/3799682.3840688
>
> [View paper](https://doi.org/10.1145/3799682.3840688)

## Summary

This paper introduces **narrative-level streaming virality prediction** as a new task for misinformation triage, motivated by a crucial timing gap: false narratives peak in virality around 1.5 days, while fact-checkers take a median of ~4.5 days to publish corrections. The authors build an end-to-end streaming pipeline that clusters semantically equivalent posts into evolving narratives, flags anomalous cluster activity, normalizes claims with LLMs, and predicts remaining spread via a novel **Post-Detection Spread Ratio (PSR)** metric—surfacing triage candidates *before* peak spread. The work is explicitly grounded in journalism research on how fact-checkers reason under time and attention constraints, arguing for pre-peak, narrative-centric, human-centered triage support rather than post-level or event-level analysis.

## Key Contributions

- A new task formulation: **narrative-level streaming virality prediction**, with an integrated pipeline (streaming clustering → online anomaly detection → claim normalization → cluster-level spread prediction).
- The **PSR metric**, quantifying the remaining intervention window at detection time and distinguishing detection lead (~23h) from actionable triage lead (~17h).
- State-of-the-art results on two established Automatic Claim Detection tasks (CT2025 claim normalization and CheckThat! 2024 check-worthiness) using *smaller/distilled* models.
- An interpretable **4-Parallel-Heads** classifier decomposing check-worthiness into checkability, verifiability, and harm potential, aligned with journalistic criteria.
- The **first public dataset and baselines** for this task (529 anomalous clusters, 535 claims, 42-feature inputs) drawn from a 1.52M-post US 2020 political Twitter/X stream.
- A frontier-LLM zero-shot ablation and a formative study with six professional fact-checkers validating the modular design.

## Methods

The dataset is built from the US Election 2020 Tweets corpus (1.52M tweets, Oct–Nov 2020), binned hourly with no-lookahead engagement snapshots. Streaming clustering uses multilingual MPNet embeddings with incremental cosine-similarity clustering (τ=0.65). Online anomaly detection uses EXPoSE (selected from the NAB benchmark) over hourly tweet counts and aggregate engagement. Claim normalization relies on Mistral-7B-Instruct with two-stage retrieval verification, topic-aware retrieval, and contrastive few-shot prompting. Virality is formulated as PSR prediction over 42 engineered features from a 6-hour post-detection window, benchmarked across linear, tree, kernel, sequence, Hawkes point-process, and text-based models. Check-worthiness is handled by a fully fine-tuned 4-Parallel-Heads DeBERTa-v3-large under a three-phase multi-task schedule, with auxiliary heads trained on soft labels from a mid-sized Mistral model.

## Findings

- **Anomaly detection:** EXPoSE achieved an NAB score of 79.2, detected 97.9% of events before peak, and gave a +23.0h median lead, dominating changepoint, Skyline, and Z-score baselines.
- **Claim normalization:** Contrastive few-shot Mistral-7B reached METEOR 0.5569, beating the strongest published baseline by 10 points and outperforming larger models; fine-tuning *underperformed* prompting—task-specific prompt design mattered more than model capacity.
- **Virality prediction:** Simple models won—BayesianRidge gave best ranking (ρ=0.551), SVR-RBF best fit (R²=0.336). LSTM/GRU and Hawkes models performed poorly, confirming that early cluster dynamics are approximately linear. **User authority and temporal features dominated; content features barely mattered**—who spreads a claim matters more than what it says early on.
- **Check-worthiness:** The distilled 4-Parallel-Heads classifier hit F1=0.833 on CT2024 (prior SOTA 0.802) and generalized zero-shot (ClaimBuster F1=0.973; CT2023 F1=0.933). Claude Opus zero-shot reached only F1=0.722 at ~$18/1k claims and ~9.9s latency versus <10ms—justifying modular distilled deployment over frontier-LLM inference. 86% of errors were shared across approaches, pointing to representation learning (not feature engineering) as the bottleneck.
- **Human study:** The pipeline surfaced ~500 candidates from ~1.5M posts; six fact-checkers showed 83.3% agreement and rated the report structure as aligned with practice—though they rated virality prediction itself the *least* valuable component.

## Connections

This work builds on classic accounts of how falsehood spreads and the structural challenges of fact-checking [[Lazer2018-mm]], and on research into the collaborative, time-pressured dynamics of online rumor and correction [[Starbird2019-qv]]. Its narrative-clustering and claim-normalization machinery connects to computational text methods for tracking narratives at scale, while its distilled-classifier-beats-frontier-LLM result speaks to ongoing debates over LLM annotation and deployment trade-offs raised across the computational-text-methods literature.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Altoe2026-wu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
