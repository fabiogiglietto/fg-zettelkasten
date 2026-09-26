---
title: "Coordinated Behavior on Social Media in 2019 UK General Election"
aliases: ["Coordinated Behavior on Social Media in 2019 UK General Election"]
authors: ["Leonardo Nizzoli", "Serena Tardelli", "Marco Avvenuti", "Stefano Cresci", "Maurizio Tesconi"]
year: 2020
doi: 
bibtex_key: Nizzoli2020-cf
topics: [coordinated-inauthentic-behavior, election-campaigns-social-media]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2008.08370v2
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445472Z
---

# Coordinated Behavior on Social Media in 2019 UK General Election

> Nizzoli, L., Tardelli, S., Avvenuti, M., Cresci, S., & Tesconi, M. (2020). Coordinated Behavior on Social Media in 2019 UK General Election. *Proc. AAAI Intl. Conference on Web and Social Media (ICWSM) 2021*.
>
> [View paper](http://arxiv.org/abs/2008.08370v2)

## Summary

This paper introduces a network-based framework for detecting and characterizing coordinated behavior on social media, arguing that coordination should be measured along a continuum rather than reduced to a binary coordinated/uncoordinated label produced by a fixed similarity threshold. Applied to 11M tweets from 1.2M users during the 2019 UK General Election, the method uncovers seven distinct coordinated communities, each with its own characteristic degree of coordination. A central conceptual claim is that coordination and automation are orthogonal: the most strongly coordinated groups were not mainstream party supporters but small activist and antagonist communities, and bot detection alone is insufficient for studying coordinated inauthentic behavior.

## Key Contributions

- A nuanced, non-binary network-based framework that generalizes prior coordination-detection approaches to estimate the *full spectrum* of coordination.
- Two methodological innovations: multiscale backbone filtering (avoiding arbitrary fixed thresholds) and an iterative "coordination-aware" community detection procedure.
- Empirical demonstration that coordination and automation are largely uncorrelated concepts.
- Identification and qualitative interpretation of concrete coordinated communities, including small activist groups typically overlooked.
- A publicly released large-scale Twitter dataset of the 2019 UK GE (11.3M tweets, 1.2M users).

## Methods

The six-step framework proceeds from selecting starting users to studying detected communities. The authors collected tweets via the Streaming API (12 Nov–12 Dec 2019) using a curated list of neutral, Labour-, and Conservative-leaning hashtags plus official party/leader accounts. They focused on "superspreaders" (top 1% by retweets, ~10,782 users), modeling each as a TF-IDF-weighted vector of retweeted tweet IDs and computing cosine similarity. Rather than thresholding, they applied the Serrano et al. multiscale backbone to retain statistically significant edges, then ran Louvain community detection inside an iterative procedure that steadily raises an edge-weight threshold to trace how communities evolve with coordination strength. Political leaning was inferred via label propagation from seed hashtags. Communities were characterized with network measures (density, clustering, assortativity), TF-IDF hashtag clouds, word shift graphs, and Botometer scores plus account suspensions.

## Findings

- Seven coordinated communities emerged: CON (conservatives), LAB (labourists), TVT (tactical voting / anti-Brexit neutrals), SNP, B60 (Backto60 pension activists), ASE (anti-Labour antisemitism-focused conservatives), and LCH (anti-loan-charge activists).
- Network structure mirrored the UK political landscape — a sharply separated conservative cluster and intertwined Labour/neutral clusters reflecting Brexit polarization.
- Large communities (LAB, CON) mixed many weakly-coordinated users with a small strongly-coordinated core, while small activist groups (B60, LCH, ASE) were almost entirely strongly coordinated.
- Community-specific characteristic coordination values differed markedly (e.g., LCH ~0.9, B60 ~0.8, ASE ~0.55).
- Network measures revealed divergent structures: B60 was a cohesive assortative clique, while ASE and LAB were hub-and-spoke star structures.
- Strongly-coordinated users embraced far more specific narratives than peripheral members.
- Automation was essentially uncorrelated with coordination; conservative clusters had more suspensions, while B60's decreasing suspensions suggested authentic grassroots coordination.

## Connections

This paper is a methodological cornerstone in the coordinated-inauthentic-behavior literature, and its continuum-based reframing of coordination and its orthogonality-to-automation argument connect it to a broad line of network-based coordination detection work, including [[Luceri2025-tr]], [[Minici2024-tf]], [[Mannocci2025-ig]], and [[Mannocci2026-kc]]. Its use of coordinated-network analysis for electoral contexts links it to the CooRnet-derived election studies such as [[Giglietto2020-9d8acdd7]], [[Giglietto2020-6278a4aa]], and [[Giglietto2022-0e951ac5]], while its distinction between coordination, bots, and inauthenticity resonates with bot- and disinformation-focused work like [[Grinberg2019-ua]] and [[Starbird2019-qv]].
