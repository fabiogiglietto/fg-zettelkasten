---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [platform-data-access-governance, political-communication-elections]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1177/29768624261452529
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3
pdf_available: true
discovery_date: 
---

# Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook

> Giglietto, F., & Marino, G. (2026). Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook. *Platforms & Society*. https://doi.org/10.1177/29768624261452529
>
> [View paper](https://doi.org/10.1177/29768624261452529)

## Summary

This paper leverages Meta's Privacy-Protected Full URLs Dataset to examine how sharing translates into viewership on Facebook across 130,448 highly circulated URLs shared in the US between 2017 and 2022. The authors show that while shares reliably predict views, this amplification is systematically dampened for URLs shared by strongly partisan audiences and boosted for URLs from sources meeting professional journalistic standards. Crucially, these effects vary sharply over time — intensifying during the 2020 election and pandemic period — providing empirical fingerprints of Facebook's known "break the glass" governance interventions. The paper argues this temporal volatility is inconsistent with a purely structural (homophily-based) explanation and evidences Facebook's role as an active algorithmic curator rather than a neutral conduit.

## Key Contributions

- Empirically links sharing behavior to actual viewership at scale using data historically inaccessible to researchers.
- Distinguishes structural network homophily from active algorithmic suppression as competing explanations for reduced partisan reach, using temporal variation as the identifying strategy.
- Provides independent quantitative corroboration of Facebook's "break the glass" emergency interventions previously known chiefly through leaks and journalism.
- Extends European amplification frameworks (Trilling et al.) to the US, integrating Political Page Affinity and NewsGuard scores.
- Advances platform studies methodology by demonstrating how longitudinal discontinuities in amplification coefficients can surface otherwise opaque governance decisions.

## Methods

Analysis of Meta's Facebook Privacy-Protected Full URLs Dataset (v10), filtered via signal-to-noise thresholds and merged with NewsGuard quality scores to yield 130,448 URLs. The authors fit four nested privacy-aware linear regressions (using the `lmdp` function from PrivacyUnbiased, with 1000-replication bootstrap variance estimation) predicting views from shares, audience partisan alignment strength, NewsGuard quality, and clicks. Models are re-estimated quarterly from 2017-Q1 to 2021-Q3 to trace temporal variation in coefficients across governance regimes.

## Findings

- Each additional share corresponds to ~56 additional views, controlling for clicks.
- A one-SD increase in audience partisan alignment strength is associated with ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point increase on NewsGuard's 100-point scale yields ~28,700 additional views, independent of sharing volume.
- The shares-to-views amplification rate ranged from ~71 views/share (2017-Q4, 2019-Q2) down to ~46 (2020-Q3).
- The partisan penalty intensified dramatically in 2020-Q3 (~-2.90 million views), aligning with reported "break the glass" measures.
- The journalistic quality reward surged from ~31,500 to over 76,900 views per quality point between 2020-Q2 and mid-2021.
- The click coefficient stayed stable (6–7.5 views/click), highlighting the volatility of shares and partisanship coefficients as distinctive.

## Connections

This work extends the author's earlier programmatic research on coordinated sharing and platform amplification ([[Giglietto2019-882f1900]], [[Giglietto2022-b30e8b4e]], [[Giglietto2025-1765bb4f]], [[Giglietto2026-855a54cb]]) into the domain of view-level exposure, and directly engages the Meta-partnered 2020 election studies exemplified by [[Bakshy2015-rn]] by arguing that treating governance as static background obscures its dynamic effects. It sits alongside methodologically kindred efforts to reverse-engineer platform curation and audience exposure such as [[Bouchaud2026-lr]], [[Bouchaud2026-np]], [[Rieder2025-ju]], and [[Rieder2026-pp]], and complements adjacent work on news quality, partisan asymmetries, and algorithmic gatekeeping including [[Allen2025-ot]], [[Gaisbauer2025-by]], and [[Bechmann2026-dr]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
