---
title: "Recommender system in X inadvertently profiles ideological positions of users"
aliases: ["Recommender system in X inadvertently profiles ideological positions of users"]
authors: ["Paul Bouchaud", "Pedro Ramaciotti"]
year: 2026
doi: 
bibtex_key: Bouchaud2026-lr
topics: [platform-governance-apis, computational-social-science]
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

This paper provides the first empirical demonstration that X's (Twitter's) "Who to Follow" recommender system inadvertently learns and encodes users' political orientations, even though it is not designed to do so. Combining a French data donation program (2.5M recommendations from 682 volunteers, Jan 2023–May 2024) with X's publicly documented architecture, the authors reconstruct an approximation of its 256-dimensional user embedding and show that a single linear direction in this space correlates at ρ=0.887 with users' Left-Right ideology, independently of demographics. They argue this implicit profiling blurs the legal distinction between "active" and "passive" profiling under regimes like the GDPR and DSA, and propose an iterative orthogonal projection method that strips ideological information from recommendations while preserving topical relevance.

## Key Contributions

- First quantitative, individual-level measurement of inadvertent political profiling in a deployed large-scale recommender system.
- A reproducible methodology to approximate a closed recommender's embedding from donated exposure data plus public architectural details.
- Empirical validation of the **linear representation hypothesis** in a production AI system serving hundreds of millions of users.
- A constrained recommendation procedure (orthogonal projection) that removes sensitive linearly-encoded attributes while largely preserving relevance — a candidate compliance tool for GDPR/LGPD/PIPA/nFADP/DSA.
- A geometric framework for analyzing how multiple socio-demographic and political attributes are jointly encoded in recommender embeddings.
- A conceptual challenge to the legal active/passive profiling dichotomy, since explainability methods can render implicit profiling explicit.

## Methods

The authors deploy a browser plug-in collecting WTF recommendations from 682 French volunteers and target a study population of ~26,500 users, retrieving their follower graphs, profiles, and recent posts via the X API. They then reconstruct X's embedding via constrained optimization with a TransE scoring function (256 dims, Adagrad, mixed Follow/WTF loss with α≈62.6%, 3:1 negative sampling combining uniform/prevalence/second-neighborhood strategies). Validation uses AUC-ROC and Precision@k against heuristic baselines, with extensive robustness checks. User attributes are inferred externally: Left-Right and anti-elite scores via ideology scaling calibrated to the Chapel Hill Expert Survey, age/gender via the M3 model, and topic interests via a tweet topic model. Canonical Correlation Analysis identifies attribute-aligned directions, and iterative orthogonal projection (à la Bolukbasi/Ravfogel) is used to scrub ideological encoding.

## Findings

- Reconstructed embedding achieves AUC-ROC 0.700, P@1 0.725, P@3 0.691 on held-out WTF recommendations, far above baselines.
- CCA correlations with attributes: Left-Right 0.887, anti-elite 0.863, news interest 0.848, popularity 0.730, age 0.562, gender 0.384 (all p<0.0001).
- Attribute directions are largely orthogonal; only age and news interest meaningfully overlap.
- The Left-Right axis correctly orders followers of French parties (LFI ≪ Renaissance ≪ RN); anti-elite axis correctly elevates LFI and RN over Renaissance.
- Left-Right encoding is not reducible to demographics (Spearman ρ=0.172 with age, −0.275 with gender).
- The embedding is robust to perturbations in training, negative sampling, device-coverage bias (up to 39% missing data), demographic sub-sampling, and temporal/graph evolution.
- Stripping the Left-Right direction increases ideological diversity of recommendations (Cohen's d=0.477) while preserving topical relevance (cosine 0.948) and news interest matching — and produces the largest change among all attributes tested.

## Connections

This paper sits at the intersection of platform auditing via data donation and the analysis of algorithmic curation, sharing infrastructural concerns with work that leverages donated or scraped exposure data such as [[Ohme2026-nv]] and [[Ulloa2024-jm]]. Its substantive focus on ideological sorting and amplification by recommender systems connects directly to audits of political content distribution like Bartl2025-...—and more concretely to [[Bak-Coleman2025-pm]], [[Luceri2025-tr]], and [[Green2025-ap]] on political bias and influence dynamics on X. The methodological strategy of reconstructing a closed model's internals from external signals also resonates with reverse-engineering efforts on platform algorithms reflected in [[Rieder2025-ju]] and [[Rieder2026-pp]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-lr.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-xs-political-algorithm-profiling/id1866587707?i=1000755979538)
