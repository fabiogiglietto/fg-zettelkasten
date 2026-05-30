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

This paper interrogates the relationship between Facebook sharing and viewership at scale, asking how partisan audience composition, journalistic quality, and platform governance interventions mediate the translation of shares into views. Drawing on Meta's Privacy-Protected Full URLs Dataset, the authors analyze 130,448 highly circulated US URLs (2017–2022) and show that while shares reliably predict views, content with intensely partisan audiences is systematically suppressed and content from high-quality news sources is systematically amplified — and crucially, that these effects spike sharply during periods of known platform crisis intervention (the 2020 election, COVID-19). The central argument is that Facebook is an active, temporally dynamic curator whose algorithmic calibrations shift in response to political pressure, not a neutral conduit. This complicates recent Meta-partnered election studies that treat platform conditions as stable background.

## Key Contributions

- Large-scale empirical mapping of the share-to-view amplification relationship using viewing data historically unavailable to outside researchers.
- An empirical strategy that distinguishes structural network homophily from active algorithmic suppression by exploiting temporal variation in coefficients.
- Independent quantitative corroboration of Facebook's "break the glass" emergency interventions, previously documented mainly through leaks and journalism.
- Extension of European amplification frameworks to the US, integrating Political Page Affinity and NewsGuard quality scores.
- A longitudinal methodological template for detecting governance through discontinuities in platform amplification dynamics.

## Methods

- Source: Meta's Facebook Privacy-Protected Full URLs Dataset (v10) via Social Science One, Jan 2017–Oct 2022, US engagement only.
- Filtering: signal-to-noise thresholds reduced ~14.8M URLs to 236,341, then merged with NewsGuard scores to yield the analytic sample of 130,448 URLs.
- Privacy-aware linear regression using the `lmdp` function (PrivacyUnbiased R package) to correct for differential-privacy noise, with 1000-replication bootstrap variance estimation.
- Four nested models predicting views from shares, partisan alignment strength, NewsGuard quality, and clicks as control.
- Quarterly re-estimation (2017-Q1 to 2021-Q3) to track governance-linked temporal variation.

## Findings

- Each additional share corresponds to ~56 additional views, net of clicks.
- A one-SD increase in audience partisan alignment is associated with ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point increase on NewsGuard's 100-point scale yields ~28,700 additional views, independent of sharing.
- The shares-to-views rate fluctuated from ~71 views/share (2017-Q4, 2019-Q2) to ~46 in 2020-Q3.
- The partisan penalty intensified sharply to ~-2.90 million views in 2020-Q3, coinciding with "break the glass" measures.
- The quality reward surged from ~31,500 views/point in 2020-Q2 to >76,900 by mid-2021, synchronized with the partisan penalty.
- The click coefficient remained stable (6–7.5 views/click) throughout, highlighting that the volatility is concentrated in shares and partisanship — consistent with active algorithmic curation.

## Connections

This paper directly engages and complicates the Meta-partnered 2020 election studies exemplified by [[Bakshy2015-rn]]-style platform-data collaborations, arguing that treating governance as static obscures dynamic curation. Methodologically and substantively it builds on the authors' prior coordinated-sharing and amplification work ([[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2022-b30e8b4e]], [[Giglietto2019-882f1900]]) and connects to broader platform-governance and data-access debates ([[Rieder2026-pp]], [[Rieder2025-ju]], [[Bruns2026-yv]]), as well as to research on hyperpartisan reach and quality-news visibility ([[Rossini2026-jn]], [[Cazzamatta2026-lo]], [[Bouchaud2026-lr]]).

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
