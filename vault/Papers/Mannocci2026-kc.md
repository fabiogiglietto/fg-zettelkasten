---
title: "Detection and characterization of coordinated online behavior: A survey"
aliases: ["Detection and characterization of coordinated online behavior: A survey"]
authors: ["Lorenzo Mannocci", "Michele Mazza", "Anna Monreale", "Maurizio Tesconi", "Stefano Cresci"]
year: 2026
doi: 10.1145/3839225
bibtex_key: Mannocci2026-kc
topics: [coordinated-inauthentic-behavior, information-disorder-theory]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3839225
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Mannocci2026-kc.mp3
pdf_available: true
discovery_date: 2026-08-18T15:26:58.028053Z
---

# Detection and characterization of coordinated online behavior: A survey

> Mannocci, L., Mazza, M., Monreale, A., Tesconi, M., & Cresci, S. (2026). Detection and characterization of coordinated online behavior: A survey. *ACM Computing Surveys*. https://doi.org/10.1145/3839225
>
> [View paper](https://doi.org/10.1145/3839225)

## Summary

This survey collects, categorizes, and critically reviews the research literature on **coordinated online behavior** — the phenomenon of multiple actors acting together on social media to pursue shared goals, spanning benign activism through malicious disinformation. The authors argue that coordination is a fundamental, *orthogonal* dimension of many online phenomena (bots, trolls, activism, echo chambers, disinformation) that deserves study beyond the narrow, threat-focused "coordinated inauthentic behavior" (CIB) lens introduced by platforms. Diagnosing existing industry and academic definitions as fragmented and operationally driven, they propose a new general definition grounded in a triad of **actors, synergic actions, and intent** inherited from decades of offline coordination research, and situate the work at the intersection of computer science and computational social science.

## Key Contributions

- A reconciliation of platform (Meta, Twitter/X, YouTube, Reddit, TikTok) and academic definitions, and a new **general definition** of coordinated online behavior built on the actors–actions–intent triad.
- A comprehensive conceptual framework with three components and **four orthogonal defining dimensions**: authenticity, harmfulness, orchestration, and time-variance — used to place bots, trolls, activists, and fandoms on an authenticity/harmfulness map.
- A formal problem definition that separates **detection** *f(·)* (mapping users and timestamped actions to communities, clusters, or labels) from **characterization** *g(·)* (mapping to indicators).
- A structured taxonomy and critical comparison of detection methods (network science vs. machine learning), with detailed tabulation of co-actions, similarity functions, filters, and community-detection algorithms.
- Identification of open challenges (missing shared definitions and null models, methodological fragmentation, impact estimation) and a research roadmap.

## Methods

A PRISMA-guided systematic literature review searching Scopus (353 records) and Google Scholar (first 1000 results) for English-language work from 2014–2026. After removing 147 duplicates and screening 1206 records, 83 papers were retained; backward reference searching added 38 more, yielding a **final corpus of 122 papers**. Papers were classified by discipline using Scimago Journal Rank, CORE conference ranking, and arXiv categories, revealing a predominance of computer science venues alongside social science and interdisciplinary outlets. The authors then synthesize definitions conceptually and formalize detection and characterization as functions with explicit inputs (users *U*, timestamped action histories *H*) and outputs (communities *P*, clusters *C*, labels *B*, indicators *M*).

## Findings

- **Platform definitions are inconsistent and contingency-driven**, producing contradictory treatment of the same campaign (e.g., the Tulsa TikTok ticket-reservation campaign not treated as CIB; Spamouflage labeled differently by Google, Twitter, and Reddit).
- Academic operational definitions vary along axes of behavioral similarity, synchronicity, and shared intent, and are often shaped by the detection technique rather than theory; the field lacks a **formal, statistically grounded definition with well-defined null models**.
- Network-science methods build latent, undirected "coordination networks" connecting users who never directly interact, via co-actions — **co-retweet/co-sharing is most common**, alongside co-reply, co-like, co-post, co-URL, co-hashtag, co-mention, and platform-specific ones (co-stitch, co-duet, co-follow, co-report).
- Similarity functions rely mainly on co-action cardinality or cosine similarity (often TF-IDF weighted to discount viral content); filtering uses fixed thresholds, k-NN graphs, statistical edge validation, and time-window constraints.
- **Time-window choice is material**: shorter windows capture highly synchronized (often inauthentic/harmful) coordination, while longer windows capture looser, emergent human coordination.
- Community discovery predominantly uses Louvain, Leiden, or modularity clustering; detection output ranges from information-rich network communities down to least-informative binary labels.

## Connections

As a survey, this paper serves as a conceptual anchor for the broader web of empirical coordination studies, including method-focused detection work such as [[Minici2024-tf]], [[Luceri2025-tr]], and [[Mannocci2025-ig]], and campaign case studies like the CooRnet/co-sharing line of work in [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Giglietto2023-fa71a001]]. Its critique of the narrow CIB frame and its authenticity/harmfulness taxonomy connect it to debates over defining and measuring inauthentic versus legitimate collective action found across many papers in these topics, including [[Ferrara2026-io]] and [[Gonzalez-Bailon2024-rq]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Mannocci2026-kc.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
