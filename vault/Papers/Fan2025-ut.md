---
title: "The medium is not the message: Deconfounding text embeddings via linear concept erasure"
aliases: ["The medium is not the message: Deconfounding text embeddings via linear concept erasure"]
authors: ["Yu Fan", "Yang Tian", "Shauli Ravfogel", "Mrinmaya Sachan", "Elliott Ash", "Alexander Hoyle"]
year: 2025
doi: 10.2139/ssrn.5340592
bibtex_key: Fan2025-ut
topics: [computational-methods-social-research]
citation_count: 0
open_access: false
source_url: https://doi.org/10.2139/ssrn.5340592
podcast_url: 
pdf_available: true
discovery_date: 2025-07-15T00:00:00Z
---

# The medium is not the message: Deconfounding text embeddings via linear concept erasure

> Fan, Y., Tian, Y., Ravfogel, S., Sachan, M., Ash, E., & Hoyle, A. (2025). The medium is not the message: Deconfounding text embeddings via linear concept erasure. *arXiv [cs.CL]*. https://doi.org/10.2139/ssrn.5340592
>
> [View paper](https://doi.org/10.2139/ssrn.5340592)

## Summary

This paper argues that pretrained sentence embeddings encode "medium" signals — source, language, style — that act as *observed confounders* when researchers use embedding similarity to cluster or retrieve documents pooled from heterogeneous corpora. The authors recast linear concept erasure (LEACE) as a way to subtract these confounder loadings from a structural decomposition of dot-product similarity, and show empirically across ten embedding models and a new paired benchmark that erasure substantially improves clustering and retrieval — sometimes spectacularly — without degrading out-of-distribution performance. The practical claim is that linear erasure should be a default preprocessing step whenever applied analysts pool texts across known sources or languages.

## Key Contributions

- A formal framing of embedding debiasing as removing observed-confounder contributions from similarity estimands.
- A paired benchmark spanning category-level (Comparative Agendas Project) and event-level (Super-SCOTUS, SemEval 2022 Task 8, SwilTra-Bench Swiss court summaries) data designed to isolate confounder effects.
- Broad empirical evaluation of LEACE across ten embedding models, with clustering, retrieval, and OOD-MTEB diagnostics.
- A variance-alignment diagnostic linking erasure gains to PC1: the more confounders dominate top variance directions, the larger the gain.
- Open-source code framing linear erasure as a cheap, principled preprocessing step for applied computational social science.

## Methods

The authors apply the closed-form LEACE algorithm to precomputed embeddings to remove subspaces linearly predictive of metadata confounders (source, language). They evaluate on (i) k-means purity and ARI for clustering, (ii) Recall@1/@10 for paired retrieval against distractor pools, and (iii) MTEB legal retrieval, news retrieval, STS, and bitext mining tasks for OOD effects. A PCA-removal baseline (drop PC1) is included for contrast, and a correlation analysis ties variance-in-PC1 to Recall@1 improvement.

## Findings

- Erasing source improved clustering for every CAP source-pair across all ten models (e.g., GIST-small on Bills–Newspapers: +0.169 purity, +0.157 ARI).
- Language erasure produced very large cross-language retrieval gains on Swiss court summaries (E5-large +0.651 Recall@1 on DE–IT) and on SemEval multilingual news (E5-small +0.236 Recall@1).
- All model/dataset combinations on SCOTUS paired summaries improved with erasure.
- LEACE-trained erasers transferred to MTEB legal/news/STS tasks with no meaningful degradation; on bitext mining, E5-large-instruct + LEACE set new SOTA on three leaderboard tasks.
- PC1 variance share correlated strongly with Recall@1 improvement (r = 0.79).
- Naive PC1 removal gave inconsistent in-domain gains and catastrophically harmed MTEB, unlike LEACE.
- Erasure is weaker when confounder categories are numerous relative to data, and in some short-query retrieval settings.

## Connections

This work is methodological infrastructure for the growing strand of CSS research using embedding similarity to compare or cluster heterogeneous corpora — relevant to applications like cross-platform or cross-source measurement in [[Bouchaud2026-lr]], [[Balluff2026-if]], and Bastos2025-ya, and to embedding-based pipelines for political or legal text such as [[Peters2026-mo]]. It also complements critical methodological work questioning what unsupervised text representations actually capture (e.g., [[Bak-Coleman2026-mk]], [[Munger2025-cz]]), reframing those concerns as a tractable observed-confounding problem rather than a fundamental limit.
