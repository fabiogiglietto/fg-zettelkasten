---
title: "Detection and characterization of coordinated online behavior: A survey"
aliases: ["Detection and characterization of coordinated online behavior: A survey"]
authors: ["Lorenzo Mannocci", "Michele Mazza", "Anna Monreale", "Maurizio Tesconi", "Stefano Cresci"]
year: 2026
doi: 10.1145/3839225
bibtex_key: Mannocci2026-kc
topics: [coordinated-inauthentic-behavior, computational-network-structure-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3839225
podcast_url: 
pdf_available: true
discovery_date: 2026-08-18T15:26:58.028053Z
---

# Detection and characterization of coordinated online behavior: A survey

> Mannocci, L., Mazza, M., Monreale, A., Tesconi, M., & Cresci, S. (2026). Detection and characterization of coordinated online behavior: A survey. *ACM Computing Surveys*. https://doi.org/10.1145/3839225
>
> [View paper](https://doi.org/10.1145/3839225)

## Summary

This survey collects, categorizes, and critically reviews the growing body of research on *coordinated online behavior*—the phenomenon of multiple actors acting in concert on social media to pursue shared goals, spanning the spectrum from benign activism to malicious disinformation. Its central argument is that coordination is a fundamental, *orthogonal* dimension of many online phenomena (bots, trolls, activism, echo chambers) that deserves study beyond the narrow, threat-focused "coordinated inauthentic behavior" (CIB) lens introduced by platforms in 2018. The authors reconcile fragmented industry and academic definitions, propose a new general definition grounded in an actors–actions–intent triad, and offer a conceptual framework organized around four orthogonal dimensions (authenticity, harmfulness, orchestration, time-variance). Building on a PRISMA-guided review of 122 papers, they formalize the analytical study of coordination into two distinct tasks—detection and characterization—and map the methodological landscape.

## Key Contributions

- A reconciliation of platform and academic definitions and a new general definition of coordinated online behavior grounded in the **actors–actions–intent** triad, inherited from decades of offline coordination research.
- A conceptual framework built on three fundamental components and four defining dimensions (**authenticity, harmfulness, orchestration, time-variance**), instantiated as a taxonomy placing bots, trolls, activists, and fandoms across authenticity/harmfulness axes.
- A formal problem definition separating **detection** *f(·)* (from actions) and **characterization** *g(·)* (of actors and intent), with explicit input/output formalisms.
- A systematic categorization and critical comparison of detection methods (network science vs. machine learning) with detailed tabulation of co-actions, similarity functions, filters, and community-detection algorithms across the literature.
- An identification of open challenges (lack of shared definitions and null models, methodological fragmentation, impact estimation) and a research roadmap.

## Methods

A systematic literature review following the PRISMA protocol. The authors searched Scopus (353 records) and Google Scholar (first 1000 results) for English-language publications from 2014–2026. After removing 147 duplicates and screening 1206 records (excluding non-English and out-of-scope work), 83 papers were retained; backward reference searching added 38 more, yielding a final corpus of **122 papers**. Papers were classified by discipline using Scimago Journal Rank, CORE conference rankings, and arXiv categories (revealing a predominance of Computer Science venues). The synthesis reconciles the operational definitions of Meta, Twitter/X, YouTube, Reddit, and TikTok with academic ones, and organizes detection methods into a structured taxonomy.

## Findings

- **Platform definitions are inconsistent and contingency-driven**, producing contradictory treatment of the same campaign (e.g., the Tulsa TikTok ticket-reservation campaign was not treated as CIB by Facebook; Spamouflage was labeled differently by Google, Twitter, and Reddit).
- Academic operational definitions vary along axes of behavioral similarity, synchronicity, and shared intent, and are often shaped by the *detection technique used* rather than by theory; the field lacks a formal, statistically grounded definition with well-defined null models.
- Network science methods build latent, undirected "coordination networks" linking users who never directly interact, using co-actions—**co-retweet/co-sharing (most common)**, co-reply, co-like, co-URL, co-hashtag, co-mention, and platform-specific ones (co-stitch, co-duet, co-follow, co-report).
- Similarity relies mainly on co-action cardinality or (TF-IDF-weighted) cosine similarity; filtering uses fixed thresholds, k-NN graphs, statistical edge validation, and time-window constraints.
- **Time-window choice materially matters**: shorter windows capture highly synchronized (often inauthentic/harmful) coordination, while longer windows capture looser emergent human coordination.
- Community discovery predominantly uses Louvain, Leiden, or modularity clustering; detection output ranges from rich network communities to clusters to least-informative binary labels.

## Connections

As a survey, this paper serves as an anchoring map for the wider corpus on coordinated inauthentic behavior and network-structure analysis, and it explicitly formalizes the co-sharing/coordination-network detection paradigm that many empirical studies operationalize—see [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Giglietto2023-fa71a001]] on coordinated link and content sharing, and [[Minici2024-tf]] and [[Luceri2025-tr]] on network-based detection. Its distinction between detection and characterization, and its non-threat-centric framing spanning authentic-yet-harmful and inauthentic-yet-harmless coordination, situates it alongside work probing the epistemics and impact of coordination such as [[Efstratiou2025-gs]] and [[Mannocci2025-ig]].
