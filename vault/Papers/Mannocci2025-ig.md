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

This paper tackles a methodological problem in the detection of coordinated online behavior: real coordination is *multimodal* — users may act in concert across retweets, replies, mentions, hashtags, and shared URLs simultaneously — yet most existing detection pipelines either analyze a single action type or naively collapse multiple layers into one flattened network. The authors construct a five-layer multiplex coordination network from a Twitter dataset of the 2019 UK General Election and systematically compare five ways of operationalizing multimodal detection: monomodal analysis, independent layers, union flattening, multiplex community detection, and intersection flattening. Their central argument is that there is an intrinsic trade-off between the strength of multimodal integration and the inclusiveness of detected coordination, and that multiplex community detection (via Generalized Louvain) strikes the best balance — preserving monomodal findings while surfacing additional coordinated structure and retaining the most central nodes.

## Key Contributions

- First comparative framework for evaluating alternative operationalizations of multimodal coordinated behavior detection.
- A multiplex community detection approach (Generalized Louvain) that lets communities span layers rather than collapsing the multiplex.
- A methodology for cross-approach comparison via overlap matrices, Hungarian matching, and lost/common/gained labeling at both community and node levels.
- Empirical characterization of the integration-vs-inclusiveness trade-off, offering practical method-selection guidance.
- Evidence-based critique of the dominant network-flattening practice, favoring multiplex-aware methods.

## Methods

The authors build a multiplex network with five co-action layers (co-retweet, co-reply, co-mention, co-hashtag, co-URL) from the top 5% most active users per modality. Edges are weighted by TF-IDF-weighted cosine similarity over user action vectors within overlapping 6-hour windows, then filtered by thresholds on common-action counts and edge weights. Five operationalizations are implemented — MONO (Louvain per layer), INDI (independent layers), UNFL (union flattening with three weighting variants), MULTI (Generalized Louvain, γ=1, ω=0.1), and INTFL (intersection flattening). Comparison relies on actor/edge coverage, degree correlation, NMI, structural community metrics, and node centrality measures, with Brunner-Munzel tests for distributional comparisons.

## Findings

- Co-retweet and co-mention layers are highly similar (NMI ≈ 0.38, fully overlapping communities), while co-reply is the most distinctive layer.
- Co-retweet and co-hashtag are partly complementary; co-URL shares little structure and has distinct properties — no single modality is a universal signal.
- Even shared communities differ structurally across modalities, so modality affects node roles, not just membership.
- Union flattening loses more communities than the more restrictive MULTI approach and tends to discard highly central nodes.
- Intersection flattening is extremely selective (257 nodes, 27 communities), capturing only the tightest coordination.
- MULTI retains nearly all monomodal communities, adds new ones, and preserves the most central/influential nodes.
- The three union-flattening weighting strategies yield near-identical results — the flattening operation itself matters far more than the weighting choice.

## Connections

This paper advances the network-science tradition of similarity-network coordination detection, extending single-modality and time-windowed co-action approaches such as those developed in [[Luceri2025-tr]], [[Minici2024-tf]], and the Giglietto line of coordinated link-sharing work ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]]) toward an explicitly multiplex formulation. It speaks to broader methodological debates about detecting and characterizing coordinated inauthentic behavior found in [[Ng2026-og]], [[Kansaon2025-id]], and [[Gerard2025-br]], while its critique of network flattening is a genuinely novel contribution to how these coordination networks should be built and interpreted.
