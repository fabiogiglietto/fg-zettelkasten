---
title: "The medium is not the message: Deconfounding text embeddings via linear concept erasure"
aliases: ["The medium is not the message: Deconfounding text embeddings via linear concept erasure"]
authors: ["Yu Fan", "Yang Tian", "Shauli Ravfogel", "Mrinmaya Sachan", "Elliott Ash", "Alexander Hoyle"]
year: 2025
doi: 10.2139/ssrn.5340592
bibtex_key: Fan2025-ut
topics: [llm-and-computational-content-analysis, computational-network-structure-analysis]
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

This paper argues that pretrained text embeddings encode spurious attributes — document source, language, style — that act as *observed confounders* and distort similarity-based analyses when researchers pool heterogeneous corpora. The authors reframe this longstanding concern about corpus-driven structure in unsupervised text analysis as a problem of confounding in embedding dot-product similarity, and propose applying LEACE (a closed-form linear concept erasure method) as a cheap preprocessing step that removes the confounder subspace. They formalize how erasure purges the confounder's contribution from a structural decomposition of similarity, build a benchmark of paired multi-source and multilingual datasets, and show across ten embedding models that erasure substantially improves clustering and retrieval — sometimes dramatically — without harming out-of-distribution performance.

## Key Contributions

- A formal account of how linear concept erasure removes observed-confounder loadings from dot-product document similarity via a structural decomposition.
- A new benchmark of paired category-level (Comparative Agendas Project) and event-level (Super-SCOTUS, SemEval 2022 Task 8, Swiss court summaries) datasets designed to isolate confounder effects on embedding tasks.
- Broad empirical evidence across ten embedding models that LEACE consistently improves clustering and retrieval without degrading OOD MTEB performance.
- A diagnostic linking LEACE's effectiveness to alignment between the confounder and dominant variance (PC1) directions.
- Open-source code and practical guidance recommending erasure as a default step for practitioners pooling documents across sources or languages.

## Methods

- Adapt the closed-form LEACE algorithm to remove subspaces predictive of confounding metadata (source, language) from precomputed embeddings.
- Evaluate ten embedding models (MiniLM, GIST small/base/large, multilingual E5 small/base/large, MPNet, Nomic-v2, MXB-large) varying in size, multilinguality, and instruction tuning.
- Measure clustering with k-means purity and Adjusted Rand Index, and retrieval with Recall@1 / Recall@10 on paired items pooled with distractors.
- Test out-of-distribution effects by applying erasers trained on CAP and legal data to MTEB legal/news retrieval and STS tasks.
- Compare against a PCA baseline (removing PC1), plus bitext-mining experiments on 28 MTEB tasks and qualitative analysis of legal summary pairs.

## Findings

- Erasing source improved purity and ARI across all four CAP source pairings and all ten models.
- Cross-family multilingual gains were dramatic: E5-large Recall@1 rose +0.651 on German–Italian court summaries; overall multilingual Recall@1 improved from 0.175 to 0.826.
- Every SCOTUS model/dataset combination improved with erasure; all ten models improved on SemEval multilingual news after erasing language.
- Erasers trained on one domain left MTEB legal/news/STS performance essentially unchanged — occasionally with small gains.
- PC1 variance in original embeddings correlated strongly with Recall@1 improvement (r = 0.79, p < 0.001).
- The naive PCA baseline gave inconsistent in-domain gains and catastrophically degraded MTEB, unlike LEACE.
- LEACE reached state-of-the-art on three public bitext-mining leaderboard tasks, with no task degrading by more than 0.01 F1.
- Erasure is weaker when confounder categories are very numerous relative to data size, and may fail in some short-query retrieval settings.

## Connections

This paper is largely methodological and stands somewhat apart from the more applied LLM-based content-analysis work under this topic. Its concern with reliable embedding-based measurement for computational social science connects most naturally to work using LLM-derived representations to scale or validate text measurement, such as [[Le-Mens2025-qz]] and [[Tan2024-vl]]; the debiasing framing has no close counterpart among the other listed papers.
