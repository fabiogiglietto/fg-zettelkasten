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

This paper leverages Meta's Privacy-Protected Full URLs Dataset to examine how user sharing translates into actual viewership on Facebook across 130,448 highly circulated URLs in the US (2017–2022). The authors show that while shares reliably predict views, this amplification is systematically dampened for content with highly partisan audiences and boosted for content from sources adhering to professional journalistic standards. Crucially, by re-estimating their model quarterly, they demonstrate that these effects are highly volatile and shift in alignment with known Facebook governance interventions — most strikingly the 2020 "break the glass" measures. This temporal pattern, they argue, constitutes empirical evidence that Facebook operates as an active algorithmic curator rather than a neutral conduit, and that platform governance must be understood as a dynamic rather than background variable.

## Key Contributions

- Provides large-scale empirical evidence of the share-to-view amplification relationship using viewership data historically unavailable to outside researchers.
- Distinguishes empirically between structural homophily and active algorithmic suppression as mechanisms limiting partisan content reach, using temporal variation to favor the latter.
- Offers independent quantitative corroboration of Facebook's "break the glass" emergency interventions previously documented only through journalism and leaks.
- Extends prior European amplification frameworks to the US context using Political Page Affinity scores and NewsGuard journalistic quality measures.
- Advances a longitudinal methodology for detecting platform governance through temporal discontinuities in amplification coefficients.

## Methods

The authors analyze Meta's Facebook Privacy-Protected Full URLs Dataset (v10) via Social Science One, restricted to US engagement (Jan 2017–Oct 2022). After applying signal-to-noise filters and merging with NewsGuard scores, the analytic sample comprises 130,448 URLs. They use privacy-aware linear regression (the `lmdp` function from the PrivacyUnbiased R package) to correct for differential privacy noise, with bootstrapped variance estimation (1000 replications). Four nested models predict URL views from shares, audience partisan alignment strength, NewsGuard journalistic quality score, and clicks as a control. The full model is then re-estimated quarterly from 2017-Q1 to 2021-Q3 to capture temporal variation across shifting governance regimes.

## Findings

- Each additional share corresponds to ~56 additional views after controlling for clicks.
- A one-SD increase in audience partisan alignment strength is associated with ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point increase on NewsGuard's 100-point scale corresponds to ~28,700 additional views, independent of sharing volume.
- The shares-to-views amplification rate fluctuated substantially, peaking at ~71 views/share in 2017-Q4 and 2019-Q2 and falling to ~46 in 2020-Q3 during the election and pandemic.
- The partisan penalty intensified sharply in 2020-Q3 (~-2.90 million views), coinciding with reported "break the glass" interventions.
- The journalistic quality reward surged from ~31,500 additional views per quality point in 2020-Q2 to over 76,900 by mid-2021, synchronized with the heightened partisan penalty.
- The click coefficient remained stable (6–7.5 views per click) throughout, contrasting with the volatility of shares and partisanship coefficients.

## Connections

This paper builds directly on the authors' own prior work on coordinated link sharing and problematic information on Facebook ([[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2022-b30e8b4e]], [[Giglietto2019-882f1900]]), extending that lineage from sharing dynamics to viewership outcomes. It engages critically with the Meta-partnered 2020 election studies — notably [[Bakshy2015-rn]]'s foundational exposure framework and reanalyses such as [[Bak-Coleman2025-pm]] — by arguing that treating governance interventions as stable background conditions misses their dynamic curatorial role. It also speaks to ongoing debates about algorithmic amplification and platform power exemplified by [[Bouchaud2026-lr]], [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Bruns2026-yv]], and complements work on hyperpartisan reach and quality news visibility such as [[Allen2025-ot]] and [[Pierri2025-hm]].

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
