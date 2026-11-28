---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [news-sharing-social-media, platform-governance-regulation]
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

This study interrogates the gap between what users *share* on Facebook and what they actually *see*, drawing on Meta's Privacy-Protected Full URLs Dataset to analyze 130,448 highly circulated US URLs from 2017 to 2022. The central argument is that Facebook functions not as a neutral conduit but as an active curator: while sharing reliably predicts viewership, that amplification is systematically dampened for content with highly partisan audiences and boosted for content from sources meeting professional journalistic standards. Crucially, by re-estimating its models quarterly, the paper shows these partisan penalties and quality rewards fluctuate sharply in alignment with known platform governance interventions—most notably the 2020 election "break the glass" measures—providing quantitative corroboration of curation decisions previously known mainly through journalistic accounts and leaks.

## Key Contributions

- Large-scale empirical evidence of the share-to-view amplification relationship, using viewing data historically unavailable to researchers.
- Distinguishes structural network effects (homophily ceilings) from active algorithmic suppression by leveraging temporal variation, favoring the latter as the mechanism limiting partisan reach.
- Independent quantitative corroboration of Facebook's "break the glass" emergency interventions.
- Extends a European amplification framework to the US context, incorporating Political Page Affinity and NewsGuard quality measures.
- Advances platform-studies methodology by detecting governance through temporal discontinuities in amplification coefficients.

## Methods

The authors work from Meta's Facebook Privacy-Protected Full URLs Dataset (v10) via Social Science One, covering January 2017–October 2022. Quality filters based on signal-to-noise thresholds reduced ~14.8 million URLs to 236,341, then merging with NewsGuard scores yielded a final 130,448-URL sample. Because the data carries differential-privacy noise, they use privacy-aware linear regression (the `lmdp` function from PrivacyUnbiased) with bootstrap variance estimation (1,000 replications). Four nested models predict views from shares, audience partisan alignment strength, NewsGuard quality score, and clicks as a control. The full model is re-estimated quarterly from 2017-Q1 to 2021-Q3 to trace coefficient variation across shifting governance regimes.

## Findings

- Each additional share is associated with ~56 additional views after controlling for clicks.
- A one-SD increase in audience partisan alignment corresponds to ~2.3–2.4 million *fewer* views, holding shares and clicks constant — a partisan reach penalty.
- A one-point increase on NewsGuard's 100-point scale yields ~28,700 additional views, independent of sharing volume.
- The shares-to-views amplification rate fluctuated from ~71 views/share (2017-Q4, 2019-Q2) down to ~46 in 2020-Q3.
- The partisan penalty intensified sharply in 2020-Q3 (~−2.90 million views), coinciding with "break the glass" interventions.
- The quality reward surged from ~31,500 views/point (2020-Q2) to over 76,900 by mid-2021, synchronized with the heightened partisan penalty.
- The click coefficient stayed stable (6–7.5 views/click) throughout, contrasting with the volatility of shares and partisanship effects.

## Connections

This paper directly engages with and challenges the Meta-partnered 2020 election studies, arguing that treating governance interventions as stable background conditions obscures their dynamic role — making [[Guess2023-ai]] and [[Gonzalez-Bailon2023-uy]] key interlocutors, alongside the foundational curation study [[Bakshy2015-rn]]. Its platform-as-curator framing builds on gatekeeping and governance scholarship such as [[Gillespie2010-as]] and [[Gillespie2022-jx]], while its concern with amplification of low-quality and viral content connects to [[Vosoughi2018-at]]. The authors' own prior work on coordinated sharing and the URLs dataset situates it within a broader research program ([[Giglietto2025-1765bb4f]], [[Giglietto2026-855a54cb]], [[Giglietto2025-ed60bc90]]), and methodologically it shares terrain with other analyses of the Social Science One URLs data ([[Eady2025-vm]], [[Pierri2026-ib]]).

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
