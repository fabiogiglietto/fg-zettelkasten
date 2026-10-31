---
title: "Recommender system in X inadvertently profiles ideological positions of users"
aliases: ["Recommender system in X inadvertently profiles ideological positions of users"]
authors: ["Paul Bouchaud", "Pedro Ramaciotti"]
year: 2026
doi: 
bibtex_key: Bouchaud2026-lr
topics: [platform-governance-data-access, llms-in-content-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2602.02624v2
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-lr.mp3
pdf_available: true
discovery_date: 2026-03-18T06:36:45.219988Z
---

# Recommender system in X inadvertently profiles ideological positions of users

> Bouchaud, P., & Ramaciotti, P. (2026). Recommender system in X inadvertently profiles ideological positions of users. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2602.02624v2)

## Summary

This paper asks whether X's friend-recommendation engine ("Who to Follow") inadvertently learns and acts on users' political orientations, even though it is not explicitly designed to profile ideology. Drawing on a large data-donation campaign in France, the authors reconstruct an approximation of X's 256-dimensional user embedding and show that a single linear direction in that space correlates almost perfectly (ρ=0.887) with users' Left-Right positions, independent of demographic covariates. They argue this constitutes inadvertent political profiling that blurs the legal line between active and passive profiling, and they propose an orthogonal-projection intervention that strips the ideological signal from the embedding while largely preserving recommendation relevance.

## Key Contributions

- First empirical, quantitative measurement of inadvertent political profiling by a large-scale, deployed recommender system at the level of individual ordinary users.
- A reproducible methodology for approximating a closed recommender's embedding from donated exposure data plus public architectural knowledge — portable beyond X.
- Empirical demonstration of the linear representation hypothesis in a production AI system serving hundreds of millions of users.
- A constrained-recommendation procedure that removes sensitive linearly-encoded attributes while preserving relevance, proposed as a candidate compliance tool under GDPR, LGPD, PIPA, nFADP, and the DSA.
- A geometric framework for examining how recommender embeddings jointly encode and separate political and socio-demographic attributes.
- A conceptual intervention in legal debate: AI explainability can make implicit profiling explicit, undermining the active/passive profiling distinction.

## Methods

A browser plug-in collected 2,549,008 "Who to Follow" recommendations from 682 French volunteers (Jan 2023–May 2024), targeting a study population of ~26,500 users, with follower networks, profiles, and recent posts gathered via the API. The authors reconstruct X's embedding through constrained optimization using a TransE scoring function matching X's documented architecture, training a 256-dimensional space via Adagrad gradient descent over a convex combination of "Follow" and "WTF" losses (optimal α=62.6%) with mixed negative sampling. User attributes — Left-Right and anti-elite positions (ideology scaling calibrated against the Chapel Hill Expert Survey), age/gender (M3 model), and topic interests — were inferred and aligned to embedding directions via Canonical Correlation Analysis with permutation tests. An iterative orthogonal projection method (adapted from debiasing work by Bolukbasi et al. and Ravfogel et al.) was used to remove the ideological direction, with before/after comparison of recommendation diversity and topical relevance.

## Findings

- The reconstructed embedding predicts held-out WTF recommendations with AUC-ROC 0.700, Precision@1 0.725, and Precision@3 0.691, far exceeding heuristic baselines.
- CCA directions correlate strongly with attributes: Left-Right (0.887), anti-elite (0.863), news interest (0.848), popularity (0.730), age (0.562), gender (0.384), all p<0.0001.
- Attribute directions are largely orthogonal; only age and news interest align significantly.
- The Left-Right direction correctly orders followers of French parties (La France Insoumise → Renaissance → Rassemblement National).
- Left-Right encoding is not reducible to demographics (Spearman ρ=0.172 with age, −0.275 with gender).
- The embedding inference is robust to training-parameter, negative-sampling, device-coverage-bias, demographic, temporal, and friend-graph variations.
- Removing the Left-Right direction raises ideological diversity of recommendations (Cohen's d=0.477) while preserving topical relevance (topic-distribution cosine similarity = 0.948); it produces the largest change of any attribute removed.

## Connections

This work extends recommender-system audits from item-level diversity toward the internal representations platforms build of users, resonating with broader platform governance and algorithmic-profiling scholarship such as [[Gillespie2010-as]], [[van-Dijck2018-up]], and [[Gonzalez-Bailon2023-uy]]. Its data-donation and embedding-reconstruction approach to a closed system connects to related work by the same author stream, [[Bouchaud2026-np]]. The attention to platform opacity and researcher data access situates it alongside governance-focused contributions like [[Rieder2026-pp]] and [[Rogers2026-zz]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bouchaud2026-lr.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-xs-political-algorithm-profiling/id1866587707?i=1000755979538)
