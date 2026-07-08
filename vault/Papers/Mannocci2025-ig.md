---
title: "Multimodal coordinated online behavior: Trade-offs and strategies"
aliases: ["Multimodal coordinated online behavior: Trade-offs and strategies"]
authors: ["Lorenzo Mannocci", "Stefano Cresci", "Matteo Magnani", "Anna Monreale", "Maurizio Tesconi"]
year: 2025
doi: 
bibtex_key: Mannocci2025-ig
topics: [coordinated-inauthentic-behavior, computational-network-structure-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2507.12108v3
podcast_url: 
pdf_available: true
discovery_date: 2025-07-15T00:00:00Z
---

# Multimodal coordinated online behavior: Trade-offs and strategies

> Mannocci, L., Cresci, S., Magnani, M., Monreale, A., & Tesconi, M. (2025). Multimodal coordinated online behavior: Trade-offs and strategies. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2507.12108v3)

## Summary

This paper systematically compares five ways of operationalizing the detection of *multimodal* coordinated online behavior — i.e., coordination that unfolds simultaneously across multiple action types such as retweets, replies, mentions, hashtags, and URLs. Using a Twitter dataset from the 2019 UK General Election, the authors construct a five-layer multiplex coordination network and evaluate monomodal analysis, independent layers, union flattening (the field's default), multiplex community detection via Generalized Louvain, and intersection flattening. They identify a fundamental trade-off between how strongly modalities are integrated and how inclusive the resulting detection is, and argue that multiplex community detection offers the best balance — preserving monomodal findings, discovering new cross-layer communities, and retaining structurally central actors that flattening tends to discard.

## Key Contributions

- First comparative framework for multimodal coordination detection, making explicit the methodological choices that prior work has left implicit.
- A multiplex community detection pipeline (Generalized Louvain, γ=1, ω=0.1) that lets coordinated communities span layers without collapsing them.
- A comparison methodology based on overlap matrices, Hungarian assignment, and lost/common/gained labeling at both community and node levels.
- Empirical characterization of the integration-vs-inclusiveness trade-off, with practical guidance for method selection.
- Evidence-based critique of the widely used union-flattening approach.

## Methods

The authors build a five-layer multiplex (co-retweet, co-reply, co-mention, co-hashtag, co-URL) over the top 5% most active users per modality, with edges weighted by TF-IDF-cosine similarity over user action vectors within overlapping 6-hour windows. After two-step filtering (common-action counts and median edge-weight thresholds per layer), they apply five operationalizations: MONO (per-layer Louvain), INDI (independent monomodal layers), UNFL in three weighting variants, MULTI (Generalized Louvain on the multiplex), and INTFL (intersection flattening). Comparison uses actor/edge coverage, Pearson degree correlation, NMI, standard structural community metrics, node-level centralities, and Brunner-Munzel tests.

## Findings

- Co-retweet and co-mention layers are the most similar (NMI ≈ 0.38, fully overlapping communities); co-reply is the most distinctive.
- Co-retweet and co-hashtag share some structure but diverge; co-URL is largely structurally separate from other layers.
- Even when modalities yield the same community membership, structural roles differ — particularly between co-retweet and co-URL.
- Union flattening discards more monomodal communities and tends to drop highly central nodes, despite being conceptually more inclusive than MULTI.
- Intersection flattening is extremely restrictive (257 nodes, 27 communities), surfacing only the most tightly coordinated cores.
- MULTI retains nearly all monomodal communities, adds new cross-layer ones, and preserves high-degree/high-eigenvector nodes.
- The three union-flattening weighting strategies behave nearly identically — the flattening operation, not the weighting, drives the loss.

## Connections

This paper extends the conceptual lineage on coordinated behavior detection traceable through work like [[Luceri2025-tr]] and [[Minici2024-tf]] on coordination networks, and the broader methodological discussion in [[Freelon2024-sc]] on inauthentic behavior measurement. Its multi-layer perspective resonates with platform- or signal-spanning approaches such as [[Lai2024-to]] and the cross-modal coordination concerns raised in [[Graham2025-gp]] and [[Kuznetsova2025-nu]]. More broadly, it complements computational-social-science efforts to scrutinize the methodological choices behind coordination claims, as in [[Bouchaud2026-lr]] and [[Schroeder2026-im]].
