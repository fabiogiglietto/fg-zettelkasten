---
title: "Emergent coordinated behaviors in networked LLM agents: Modeling the strategic dynamics of information operations"
aliases: ["Emergent coordinated behaviors in networked LLM agents: Modeling the strategic dynamics of information operations"]
authors: ["Gian Marco Orlando", "Jinyi Ye", "Valerio La Gatta", "Mahdi Saeedi", "Vincenzo Moscato", "Emilio Ferrara", "Luca Luceri"]
year: 2025
doi: 
bibtex_key: Orlando2025-ul
topics: [coordinated-inauthentic-behavior, generative-ai-and-media]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2510.25003v1
podcast_url: 
pdf_available: true
discovery_date: 2025-10-15T00:00:00Z
---

# Emergent coordinated behaviors in networked LLM agents: Modeling the strategic dynamics of information operations

> Orlando, G. M., Ye, J., Gatta, V. L., Saeedi, M., Moscato, V., Ferrara, E., & Luceri, L. (2025). Emergent coordinated behaviors in networked LLM agents: Modeling the strategic dynamics of information operations. *arXiv [cs.MA]*.
>
> [View paper](http://arxiv.org/abs/2510.25003v1)

## Summary

This paper presents the first systematic study of how coordination emerges spontaneously among generative LLM agents conducting simulated information operations (IO). Using Generative Agent-Based Modeling on a Twitter/X-like platform, the authors deploy 10 IO agents alongside 40 organic agents (split between ideologically aligned and non-aligned) and vary the *operational awareness* available to the IO agents across three regimes: a shared Common Goal, Teammate Awareness, and Collective Decision-Making via periodic deliberation. The central finding is that merely revealing teammate identities to agents — without any explicit deliberation mechanism — produces coordination outcomes nearly indistinguishable from those of explicit collective decision-making, suggesting that distributed mutual awareness alone is sufficient affordance for large-scale emergent influence behavior.

## Key Contributions

- First GABM-based study examining *emergent* (rather than scripted) coordination among LLM agents in IO scenarios.
- An experimental framework operationalizing five testable hypotheses linking real-world IO signals to coordination and impact metrics.
- Evidence that minimal teammate awareness suffices to trigger coordination comparable to explicit deliberation — a governance-relevant result.
- Public release of code and an interactive dashboard for inspecting evolving social graphs, hashtag diffusion, and agent reasoning traces.
- Identification of five recurring self-organizing strategies (content amplification, unified messaging, audience targeting, peer cross-promotion, shared linguistic markers) that mirror documented real-world IO tactics.

## Methods

The authors simulate 50 agents (10 IO, 20 ideologically aligned organic, 20 non-aligned organic) initialized from the U.S. 2020 Election Twitter dataset, using Llama 3.3 70B via PyAutogen and a persona/memory/action-policy framework adapted from Ferraro et al. (2024). Each of the three operational regimes is run for 50 iterations with 3 repetitions. Coordination is measured via network metrics (density, clustering, reciprocity, intra-group action proportions), narrative convergence (Sentence-BERT cosine similarity, RoBERTa sentiment), and co-retweet TF-IDF similarity. Impact is assessed via hashtag adoption lag and exposure, engagement, audience diversity (1−Gini), and cascade size/depth/breadth. Mann-Whitney U tests support quantitative claims, and qualitative coding of agent reasoning logs surfaces emergent strategies.

## Findings

- Intra-IO re-share proportion rises from 0.82 (Common Goal) → 0.96 (Teammate Awareness) → 0.94 (Collective Decision-Making); intra-IO comments rise from 0.48 → 0.65.
- Network density rises 0.74 → 0.89, clustering 0.86 → 0.97, reciprocity 0.56 → 0.68 across regimes.
- IO narrative similarity climbs to 0.89–0.91 vs. ~0.62 organic baseline; intra-IO comment sentiment alignment rises 0.68 → 0.83 (p < 0.001).
- Co-retweet similarity among IO agents grows 0.28 → 0.35 against a flat 0.11 organic baseline.
- Aligned organic agents adopt promoted hashtags almost immediately after first IO contact, while non-aligned agents show delayed, right-skewed adoption — a clear selective-amplification signature.
- Cascades grow in size (3.84 → 4.56), depth, and breadth; re-shares per IO post rise 0.75 → 1.19 while audience diversity stays stable (~0.62).
- Qualitative logs reveal *spontaneous social learning* in the Teammate Awareness regime — agents imitate successful peers without being instructed to coordinate.

## Connections

This paper sits at the intersection of LLM multi-agent simulation and empirical CIB research. It directly extends LLM-driven IO simulation work such as [[Triedman2025-uy]] and [[Lin2025-xp]], and complements behavioral detection and characterization studies of coordinated networks like [[Minici2024-tf]], [[Luceri2025-tr]], and [[Kulichkina2026-zk]]. The finding that selective amplification varies sharply with ideological alignment also resonates with empirical engagement studies such as [[DeVerna2025-dl]] and [[Gerard2025-br]].
