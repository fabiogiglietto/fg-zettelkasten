---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [platform-governance-data-access, polarization-hybrid-media]
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

This paper leverages Meta's Privacy-Protected Full URLs Dataset to examine how sharing translates into viewership on Facebook across 130,448 highly circulated URLs shared in the US between 2017 and 2022. The authors show that while shares reliably predict views, this amplification is systematically dampened for content circulating within highly partisan audiences and boosted for content from sources meeting professional journalistic standards. Critically, quarterly re-estimation reveals that these coefficients fluctuate sharply in sync with known Facebook governance interventions—especially the 2020 election "break the glass" measures—supporting the argument that Facebook operates as an active curator whose algorithmic calibrations respond to political crises and reputational pressure, not as a neutral conduit.

## Key Contributions

- Large-scale empirical measurement of the share-to-view amplification relationship using previously inaccessible viewing data.
- Empirically distinguishes structural network homophily from active algorithmic suppression as mechanisms limiting partisan reach, using temporal variation to favor the latter.
- Provides independent quantitative corroboration of Facebook's "break the glass" emergency interventions previously known only through leaks and journalism.
- Extends European amplification frameworks (Trilling et al.) to the US, integrating Political Page Affinity scores and NewsGuard quality ratings.
- Advances a longitudinal methodology for detecting platform governance via temporal discontinuities in amplification coefficients.

## Methods

Using Meta's Facebook Privacy-Protected Full URLs Dataset (v10, Jan 2017–Oct 2022) restricted to US engagement, the authors apply signal-to-noise filters and merge with NewsGuard scores to obtain 130,448 URLs. They estimate four nested privacy-aware linear regressions (via the `lmdp` function in the PrivacyUnbiased R package, with 1000-replication bootstrap variance estimation) predicting views from shares, audience partisan alignment strength, NewsGuard quality, and clicks. The full model is re-estimated quarterly from 2017-Q1 to 2021-Q3 to trace temporal shifts across governance regimes.

## Findings

- Each additional share is associated with ~56 additional views, controlling for clicks.
- A one-SD increase in audience partisan alignment strength corresponds to ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point increase in NewsGuard score corresponds to ~28,700 additional views, independent of sharing.
- Amplification rate ranged from ~71 views/share (2017-Q4, 2019-Q2) down to ~46 in 2020-Q3 during the election and pandemic.
- The partisan penalty intensified sharply in 2020-Q3 (~-2.90M views), aligning with "break the glass" interventions.
- The journalistic quality reward surged from ~31,500 views/quality point (2020-Q2) to >76,900 by mid-2021.
- The click coefficient remained stable (6–7.5 views/click) throughout, contrasting with the volatility of the share and partisanship coefficients.

## Connections

This paper extends a lineage of research using Meta's URLs Dataset and interrogating the platform's role in shaping visibility, most directly building on and partially challenging [[Bakshy2015-rn]]'s framing of algorithmic curation as background structure. It contributes to the platform governance and data access strand represented by [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Bechmann2026-dr]], and speaks to work reassessing partisan amplification and misinformation reach such as [[Allen2025-ot]], [[Pierri2025-hm]], and [[Mosleh2024-op]]. It also complements the author's prior work on coordinated sharing and problematic information ecosystems, including [[Giglietto2022-b30e8b4e]], [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2019-882f1900]], and [[Giglietto2026-855a54cb]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
