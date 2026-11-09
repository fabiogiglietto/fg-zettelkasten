---
title: "Emergent coordinated behaviors in networked LLM agents: Modeling the strategic dynamics of information operations"
aliases: ["Emergent coordinated behaviors in networked LLM agents: Modeling the strategic dynamics of information operations"]
authors: ["Gian Marco Orlando", "Jinyi Ye", "Valerio La Gatta", "Mahdi Saeedi", "Vincenzo Moscato", "Emilio Ferrara", "Luca Luceri"]
year: 2025
doi: 
bibtex_key: Orlando2025-ul
topics: [generative-ai-disinformation, coordinated-inauthentic-behavior]
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

This paper offers the first systematic study of how coordination *emerges* among generative LLM agents engaged in simulated information operations (IO), rather than being scripted in advance. Using Generative Agent-Based Modeling (GABM), the authors place 10 IO agents and 40 organic agents (half ideologically aligned, half not) on a simulated Twitter/X-like platform and vary how much operational awareness the IO agents have across three regimes: a shared Common Goal, mutual Teammate Awareness, and explicit Collective Decision-Making via periodic deliberation. Their central finding is that as operational structure increases, IO networks grow denser, narratives more homogeneous, amplification more synchronized, and hashtag adoption faster — and, strikingly, that *merely revealing teammate identities* produces coordination nearly equivalent to explicit collective voting. The work argues that distributed mutual awareness is a sufficient affordance for large-scale emergent coordination, with direct implications for platform governance and defense against automated influence campaigns.

## Key Contributions

- First systematic GABM-based study of *emergent* (not predefined) coordination among LLM agents in simulated information operations.
- A structured experimental framework linking real-world IO coordination signals to five testable hypotheses, with operationalized coordination and impact metrics.
- Empirical demonstration that minimal teammate awareness suffices to trigger coordination comparable to explicit collective deliberation.
- Public release of code and an interactive dashboard for exploring evolving social graphs, hashtag diffusion, and agent reasoning.
- Identification of self-organizing agent strategies that mirror tactics documented in real-world IO campaigns.

## Methods

The study uses Generative Agent-Based Modeling with personas, memory modules, and action policies, powered by Llama 3.3 70B via PyAutogen. Simulations ran 50 agents (10 IO, 20 aligned organic, 20 non-aligned organic) initialized from the U.S. 2020 Election Twitter dataset, over 50 iterations with 3 repetitions per configuration. Three regimes were compared — Common Goal, Teammate Awareness, and Collective Decision-Making (deliberation every 5 steps, with an IO Orchestrator consolidating top-5 strategies). Coordination was measured via network density, clustering, reciprocity, Sentence-BERT narrative similarity, RoBERTa sentiment, and TF-IDF co-retweet similarity; impact via hashtag adoption rates, adoption lag, exposure counts, engagement, audience diversity, and cascade size/depth/breadth. Mann-Whitney U tests and qualitative analysis of agent reasoning logs supplemented the quantitative metrics.

## Findings

- Intra-group re-share proportion among IO agents rose from 0.82 (Common Goal) to 0.96 (Teammate Awareness) and 0.94 (Collective Decision-Making) — teammate awareness matched or exceeded deliberation.
- Network density rose 0.74→0.89, clustering 0.86→0.97, reciprocity 0.56→0.68 across regimes.
- Textual similarity among IO posts rose 0.89→0.91 (vs. ~0.62 organic baseline); intra-IO comment sentiment rose 0.68→0.83 (p < 0.001).
- Co-retweet similarity among IO agents grew 0.28→0.35, against a stable 0.11 organic baseline.
- Campaign hashtag prevalence in original posts rose 0.42→0.54; aligned organic agents adopted hashtags almost immediately, while non-aligned agents showed delayed, right-skewed adoption.
- Cascade size grew 3.84→4.56, depth 0.53→0.60, breadth 2.71→3.24; re-shares per IO post rose 0.75→1.19, while audience diversity stayed stable (~0.62).
- Five recurring emergent strategies appeared: amplifying high-performing content, unified messaging, engaging receptive audiences, cross-promoting among peers, and shared language markers.
- Teammate Awareness agents exhibited spontaneous social learning, imitating successful peers as an implicit coordination mechanism.

## Connections

This work sits alongside other agent-based and generative simulation studies of coordinated inauthentic behavior, complementing detection-oriented empirical work on coordination signals such as [[Luceri2025-tr]], [[Minici2024-tf]], and [[Kansaon2025-id]]. Its use of LLM agents to reproduce IO tactics relates to broader investigations of generative-AI–driven influence and manipulation, including [[Triedman2025-uy]] and [[Yang2025-iv]]. It also connects to the Giglietto line of research operationalizing coordinated behavior metrics ([[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2026-9b6a992d]]).
