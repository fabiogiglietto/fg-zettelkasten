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

This paper examines how user sharing on Facebook translates into actual viewership, using Meta's Privacy-Protected Full URLs Dataset covering 130,448 highly circulated URLs shared in the US between 2017 and 2022. The authors show that while shares reliably predict views, this amplification is systematically dampened for content with intensely partisan audiences and boosted for content from outlets meeting professional journalistic standards. Crucially, both effects vary sharply over time in ways that track known Facebook governance interventions — especially the 2020 "break the glass" measures — supporting the argument that Facebook functions as an active algorithmic curator whose calibrations shift with political and regulatory pressure, rather than as a neutral conduit.

## Key Contributions

- Large-scale empirical mapping of the share-to-view amplification relationship using viewing data previously unavailable to researchers.
- Empirical distinction between structural homophily ceilings and active algorithmic suppression as mechanisms limiting partisan content reach, with temporal variation favoring the latter.
- Independent quantitative corroboration of Facebook's "break the glass" emergency interventions, previously documented mainly through leaks and journalism.
- Extension of European amplification frameworks (Trilling et al.) to the US context, integrating Political Page Affinity and NewsGuard quality measures.
- A longitudinal methodology for detecting platform governance via temporal discontinuities in amplification coefficients.

## Methods

The authors draw on Meta's Facebook Privacy-Protected Full URLs Dataset (v10) via Social Science One, restricted to US engagement and filtered using signal-to-noise thresholds, yielding 130,448 URLs after merging with NewsGuard scores. They estimate four nested privacy-aware linear regression models (using the `lmdp` function from PrivacyUnbiased, with 1000 bootstrap replications) predicting views from shares, audience partisan alignment strength (from Political Page Affinity scores), NewsGuard quality, and clicks as a control. To capture temporal dynamics, the full model is re-estimated quarterly from 2017-Q1 to 2021-Q3.

## Findings

- Each additional share is associated with ~56 additional views after controlling for clicks.
- A one-SD increase in audience partisan alignment strength corresponds to ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point increase on NewsGuard's 100-point scale corresponds to ~28,700 additional views, independent of sharing volume.
- Shares-to-views amplification peaked at ~71 views/share in 2017-Q4 and 2019-Q2 and fell to ~46 in 2020-Q3 amid the election and pandemic.
- The partisan penalty intensified sharply in 2020-Q3 (~−2.90 million views), coinciding with "break the glass" interventions.
- The journalistic quality reward surged from ~31,500 to over 76,900 additional views per quality point between 2020-Q2 and mid-2021.
- The click coefficient remained stable (6–7.5 views/click) throughout, contrasting with the volatility of shares and partisanship coefficients.

## Connections

This paper connects directly to other work using the Facebook URLs dataset and probing algorithmic curation, notably [[Bakshy2015-rn]] on exposure to ideologically diverse content, and to the broader debate over Meta-partnered 2020 election studies that the authors partially challenge. It builds on the authors' own prior work on coordinated link sharing and amplification dynamics ([[Giglietto2022-b30e8b4e]], [[Giglietto2019-882f1900]], [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]]) and speaks to the platform-governance literature on algorithmic gatekeeping and data access represented by [[Rieder2026-pp]], [[Rieder2025-ju]], and [[Helmond2026-ll]], as well as adjacent studies of partisan and hyperpartisan circulation such as [[Bouchaud2026-lr]], [[Rossini2026-jn]], and [[Pierri2025-hm]].

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
