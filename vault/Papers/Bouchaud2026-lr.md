---
title: "Recommender system in X inadvertently profiles ideological positions of users"
aliases: ["Recommender system in X inadvertently profiles ideological positions of users"]
authors: ["Paul Bouchaud", "Pedro Ramaciotti"]
year: 2026
doi: 
bibtex_key: Bouchaud2026-lr
topics: [platform-governance-data-access, political-polarization-partisan-news]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2602.02624v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-lr.mp3
pdf_available: true
discovery_date: 2026-03-18T06:36:45.219988Z
---

# Recommender system in X inadvertently profiles ideological positions of users

> Bouchaud, P., & Ramaciotti, P. (2026). Recommender system in X inadvertently profiles ideological positions of users. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2602.02624v1)

## Summary

This paper asks whether X's friend-recommendation system inadvertently learns and exploits users' political orientations, even though it is not explicitly designed to profile ideology. Using a data donation program that gathered over 2.5 million "Who to Follow" recommendations from 682 French volunteers, the authors reconstruct an approximation of X's 256-dimensional user embedding from publicly documented architectural details. They find a single spatial direction in this embedding that correlates almost perfectly (ρ=0.887) with users' Left-Right ideological positions, independently of demographics. The paper then proposes an iterative orthogonal projection method that removes this linearly-encoded political information while largely preserving recommendation relevance, offering both a diagnostic and a candidate regulatory-compliance tool.

## Key Contributions

- First empirical, quantitative measurement of inadvertent political profiling in a large-scale real-world recommender serving individual regular users.
- A reproducible methodology for approximating a closed recommender's internal embedding from donated exposure data plus public architectural knowledge — applicable beyond X.
- Empirical demonstration of the linear representation hypothesis in a deployed AI system at scale.
- A constrained-recommendation procedure that strips sensitive linearly-encoded attributes while retaining topical relevance, framed as a possible compliance tool for GDPR, LGPD, PIPA, nFADP, and the DSA.
- A conceptual argument that AI explainability undermines the legal distinction between active and passive profiling.

## Methods

The authors ran a browser plug-in data donation campaign collecting 2,549,008 WTF recommendations from 682 volunteers (Jan 2023–May 2024), plus follower networks, profiles, and recent posts for a study population of ~26,500 users. They reconstructed X's embedding via constrained optimization using a TransE scoring function, training a 256-dimensional space with Adagrad and a convex combination of "Follow" and "WTF" losses, using mixed negative-sampling strategies. Validation relied on AUC-ROC (0.700) and Precision@k against heuristic baselines and extensive robustness checks. User attributes (Left-Right and anti-elite position, age, gender, popularity, topic interests) were inferred using ideology scaling calibrated to the Chapel Hill Expert Survey and off-the-shelf demographic and topic classifiers. Canonical Correlation Analysis identified attribute-aligned directions, and an iterative orthogonal projection (adapting debiasing techniques from the ML fairness literature) removed the ideological direction.

## Findings

- The reconstructed embedding predicted held-out recommendations well (AUC-ROC 0.700, Precision@1 0.725), far exceeding baselines.
- CCA directions correlated strongly with attributes: Left-Right (0.887), anti-elite (0.863), news interest (0.848), popularity (0.730), age (0.562), gender (0.384), all p<0.0001.
- Attribute directions were largely orthogonal; only age and news interest showed significant alignment.
- The Left-Right direction correctly ordered followers of French parties (La France Insoumise leftmost through Rassemblement National rightmost).
- The Left-Right encoding was not reducible to demographics (Spearman ρ=0.172 with age, −0.275 with gender).
- Inference was robust to variation in training parameters, negative sampling, simulated device-coverage bias, demographic sub-sampling, temporal splits, and friend-graph evolution.
- Removing the Left-Right direction increased ideological diversity of recommendations (Cohen's d=0.477) while preserving topical relevance (topic-distribution cosine similarity=0.948); it produced the largest change of any attribute removed.

## Connections

This paper is by one of the authors of the closely related audit work [[Bouchaud2026-np]], and shares that project's focus on reconstructing and interrogating platform recommender behavior under the platform-governance and data-access agenda. It extends recommender-audit literature that previously emphasized item-level diversity or the causal effects of algorithmic policies toward analyzing the *internal user representations* these systems learn. The remaining papers under these topics deal largely with news exposure, polarization, and platform data access at the content level rather than embedding-level profiling, so the intellectual overlap beyond the shared methodological lineage is limited.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-lr.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-xs-political-algorithm-profiling/id1866587707?i=1000755979538)
