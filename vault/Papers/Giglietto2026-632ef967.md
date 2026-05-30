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

This study uses Meta's Privacy-Protected Full URLs Dataset to examine how sharing translates into viewership for 130,448 widely-circulated URLs on Facebook in the US between 2017 and 2022. The authors show that while shares reliably predict views, the relationship is systematically dampened for content shared by partisan audiences and amplified for content from sources adhering to professional journalistic standards. Crucially, by re-estimating these effects quarterly, they show that the partisan penalty and quality reward fluctuate sharply in alignment with Facebook's documented governance interventions—especially the 2020 "break the glass" measures—providing empirical evidence that the platform operates as an active curator rather than a neutral conduit.

## Key Contributions

- Large-scale empirical mapping of the share-to-view amplification relationship using viewing data previously unavailable to researchers.
- Empirical distinction between structural network homophily and active algorithmic suppression as mechanisms limiting partisan reach, with temporal variation favoring the latter.
- Independent quantitative corroboration of Facebook's "break the glass" emergency interventions, previously known mainly through leaks and journalism.
- Extension of European amplification frameworks (Trilling et al., 2022) to the US, incorporating Political Page Affinity and NewsGuard quality scores.
- A longitudinal methodological template for detecting platform governance shifts through temporal discontinuities in amplification coefficients.

## Methods

The authors analyze Meta's Facebook Privacy-Protected Full URLs Dataset (v10) released via Social Science One, covering January 2017 to October 2022. After signal-to-noise filtering and merging with NewsGuard scores, the analytic sample comprises 130,448 URLs. They use privacy-aware linear regression (the `lmdp` function from the PrivacyUnbiased R package) to correct for differential-privacy noise, with bootstrap variance estimation. Four nested models predict views from shares, audience partisan alignment strength (from Political Page Affinity scores), NewsGuard quality, and clicks as a control. Critically, they re-estimate the full model quarterly from 2017-Q1 to 2021-Q3 to capture how coefficients shift across governance regimes.

## Findings

- Each additional share corresponds to roughly 56 additional views after controlling for clicks.
- A one-SD increase in partisan alignment strength is associated with ~2.3–2.4 million fewer views, holding shares and clicks constant.
- A one-point increase on NewsGuard's 100-point scale yields ~28,700 additional views, independent of sharing volume.
- The shares-to-views amplification rate fluctuated substantially: peaking ~71 views/share in 2017-Q4 and 2019-Q2, falling to ~46 in 2020-Q3 during the election and pandemic.
- The partisan penalty intensified sharply in 2020-Q3 (~-2.90 million views), coinciding with reported "break the glass" interventions.
- The journalistic quality reward surged from ~31,500 additional views per quality point in 2020-Q2 to over 76,900 by mid-2021.
- The click coefficient remained stable (6–7.5 views per click) throughout, in striking contrast to the volatility of share and partisanship coefficients.

## Connections

This paper extends a line of work using the Social Science One URLs dataset and methodologically engaging with differential privacy, connecting directly to [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], and the earlier [[Giglietto2022-b30e8b4e]] and [[Giglietto2019-882f1900]] on coordinated sharing and amplification dynamics. It speaks to and partially challenges the Meta-partnered 2020 election studies typified by [[Bakshy2015-rn]]-style platform-research collaborations, by showing that governance interventions cannot be treated as stable background. It also complements work on hyperpartisan reach, algorithmic curation, and platform gatekeeping such as [[Bouchaud2026-lr]], [[Rieder2026-pp]], [[Rieder2025-ju]], and [[Bruns2026-yv]].

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-632ef967.mp3)
