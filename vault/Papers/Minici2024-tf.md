---
title: "IOHunter: Graph foundation model to uncover online information operations"
aliases: ["IOHunter: Graph foundation model to uncover online information operations"]
authors: ["Marco Minici", "Luca Luceri", "Francesco Fabbri", "Emilio Ferrara"]
year: 2024
doi: 
bibtex_key: Minici2024-tf
topics: [coordinated-inauthentic-behavior, computational-methods-llms]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2412.14663v2
podcast_url: 
pdf_available: false
discovery_date: 2024-12-15T00:00:00Z
---

# IOHunter: Graph foundation model to uncover online information operations

> Minici, M., Luceri, L., Fabbri, F., & Ferrara, E. (2024). IOHunter: Graph foundation model to uncover online information operations. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2412.14663v2)

## Summary

IOHunter proposes a graph foundation model for detecting drivers of coordinated information operations (IOs) on social media. The authors argue that existing IO-detection pipelines are brittle: they are typically trained per-campaign, depend on scarce labels, and fail to transfer across operations originating from different state actors or platforms. By fusing a language model encoder with graph neural networks over user-interaction graphs, IOHunter learns representations that jointly capture content and relational structure, enabling detection that generalizes across heterogeneous campaigns. Evaluated on six state-sponsored campaigns on X, the model outperforms baselines and remains effective in out-of-distribution and few-shot regimes, positioning foundation-model approaches as a promising direction for IO defense.

## Key Contributions

- Introduces a *graph foundation model* paradigm for IO detection, extending the foundation-model framing from text and vision to graph-structured social data.
- Provides a unified architecture that integrates language-model text embeddings with GNN-based structural representations of user activity.
- Empirically demonstrates cross-campaign generalization across six state-sponsored IO datasets on X.
- Shows that the approach supports few-shot detection, mitigating the chronic label scarcity problem in IO research.

## Methods

- Builds user-interaction graphs from X data covering six state-sponsored IO campaigns originating from different countries.
- Encodes node-level textual signals with a language model and combines them with a GNN backbone to learn driver-level representations.
- Trains and evaluates under three regimes: standard supervised, out-of-distribution (held-out campaigns), and few-shot.
- Benchmarks against prior IO driver-detection baselines using classification metrics.

## Findings

- IOHunter outperforms baselines across the six campaign datasets in supervised settings.
- It generalizes to unseen campaigns, suggesting transferable signatures of coordinated behavior across state actors.
- The joint text + graph representation outperforms either modality on its own.
- Performance remains strong with limited labels, supporting practical few-shot deployment.

## Connections

This work fits within a growing body of machine-learning approaches to coordinated inauthentic behavior detection that move beyond per-campaign classifiers; it relates closely to [[Luceri2025-tr]] and [[Mannocci2025-ig]] on detection methodology, and to [[Gerard2025-br]] and [[Yang2025-iv]] on identifying coordinated actors at scale. Its emphasis on cross-campaign generalization and few-shot transfer connects it conceptually to broader methodological efforts in computational social science such as [[Bouchaud2026-lr]] and [[Kansaon2025-id]] that grapple with measuring coordination across diverse operations.
