---
title: "Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"
aliases: ["Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook"]
authors: ["Fabio Giglietto", "Giada Marino"]
year: 2026
doi: 10.1177/29768624261452529
bibtex_key: Giglietto2026-632ef967
kind: own
topics: [platform-governance-and-data-access, polarization-partisanship-hyperpartisan-media]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1177/29768624261452529
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3
pdf_available: true
discovery_date: 
---

# Beyond the share button: How partisan alignment, journalistic quality, and algorithmic governance shape what millions see on Facebook

## Summary

This paper leverages Meta's Privacy-Protected Full URLs Dataset to examine the relationship between sharing and viewership for 130,448 highly circulated URLs on Facebook in the US between 2017 and 2022. While shares reliably predict views, the authors show that this amplification is significantly dampened for content with strongly partisan audiences and boosted for content from sources meeting professional journalistic standards. Crucially, these effects are not stable: their sharp temporal fluctuations align with documented Facebook governance interventions—most notably the 2020 "break the glass" measures—providing quantitative evidence that the platform operates as an active curator whose algorithmic calibrations shift in response to political crises and reputational pressure, rather than as a neutral conduit.

## Key Contributions

- Empirically distinguishes between structural network homophily and active algorithmic suppression as mechanisms constraining partisan content reach, using temporal variation to support the latter.
- Offers the first large-scale quantitative corroboration of Facebook's "break the glass" interventions, previously known mainly through leaked documents and journalism.
- Extends European-context amplification frameworks to the US, integrating Political Page Affinity scores with NewsGuard quality ratings.
- Advances a longitudinal methodology for detecting platform governance via temporal discontinuities in amplification coefficients.
- Engages critically with the Meta-partnered 2020 election studies by arguing that treating governance interventions as static background conditions obscures their dynamic role.

## Methods

The authors use Meta's Privacy-Protected Full URLs Dataset (v10) via Social Science One, applying signal-to-noise filters and merging with NewsGuard scores to yield a 130,448-URL analytic sample. Because the dataset includes differentially private noise, they use privacy-aware linear regression via the `lmdp` function in the PrivacyUnbiased R package, with bootstrap variance estimation (1000 replications). Four nested models predict URL views from shares, audience partisan alignment strength, NewsGuard journalistic quality score, and clicks (as control). To capture governance dynamics, the full model is re-estimated quarterly from 2017-Q1 to 2021-Q3.

## Findings

- Each additional share corresponds to roughly 56 additional views after controlling for clicks.
- A one-SD increase in audience partisan alignment is associated with ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point increase on the NewsGuard 100-point quality scale corresponds to ~28,700 additional views, independent of sharing volume.
- The shares-to-views amplification rate fluctuated from ~71 views/share in 2017-Q4 and 2019-Q2 down to ~46 in 2020-Q3 (election + pandemic).
- The partisan penalty intensified sharply in 2020-Q3 (~-2.90 million views), coinciding with the "break the glass" period.
- The journalistic quality reward surged from ~31,500 extra views per quality point in 2020-Q2 to over 76,900 by mid-2021.
- The click coefficient remained stable (6–7.5 views per click), contrasting sharply with the volatility of shares and partisanship coefficients.

## Connections

This paper sits at the intersection of platform-governance forensics and partisan-media circulation research. It directly extends the authors' prior work on coordinated link sharing and Facebook amplification ([[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2022-b30e8b4e]], [[Giglietto2019-882f1900]]) and engages with the Meta-partnered 2020 election studies represented by [[Bakshy2015-rn]]-style designs, while pushing back against their static-treatment assumptions. Its evidence of active algorithmic curation resonates with broader work on platform gatekeeping and URL-level reach ([[Rieder2025-ju]], [[Rieder2026-pp]], [[Bouchaud2026-lr]]), and complements ongoing debates about partisan asymmetries and journalistic quality in social media diffusion ([[Allen2025-ot]], [[Mosleh2024-op]], [[Bruns2026-yv]]).

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
