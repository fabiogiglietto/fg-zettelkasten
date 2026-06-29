---
title: "Exposure to low-credibility online health content is limited and is concentrated among older adults"
aliases: ["Exposure to low-credibility online health content is limited and is concentrated among older adults"]
authors: ["Benjamin Lyons", "Andy J. King", "Rebecca L. Barter", "Kimberly A. Kaphingst"]
year: 2026
doi: 10.1038/s43587-025-01059-x
bibtex_key: Lyons2026-ca
topics: [health-information-online, information-disorder]
citation_count: 2
open_access: false
source_url: https://doi.org/10.1038/s43587-025-01059-x
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lyons2026-ca.mp3
pdf_available: true
discovery_date: 2026-02-10T06:52:51.874075Z
---

# Exposure to low-credibility online health content is limited and is concentrated among older adults

> Lyons, B., King, A. J., Barter, R. L., & Kaphingst, K. A. (2026). Exposure to low-credibility online health content is limited and is concentrated among older adults. *Nature Aging*, 1–9. https://doi.org/10.1038/s43587-025-01059-x
>
> [View paper](https://doi.org/10.1038/s43587-025-01059-x)

## Summary

This paper combines a US national survey (n=1,059) with roughly four weeks of passive web and YouTube tracking in late 2023 to measure actual exposure to low-credibility online health content. The authors find that such exposure is rare in aggregate — about 3% of web health visits and 10% of YouTube health views — but heavily concentrated, with the top 10% of users accounting for 77% of exposure. Adults aged 60+ are disproportionately exposed, even controlling for overall browsing volume, and exposure correlates with poorer headline discernment, false cancer beliefs, conspiracism, and consumption of dubious political news. Crucially, referrals to low-credibility health sites come overwhelmingly from other low-credibility sites rather than search engines or social media, suggesting habitual cross-domain consumption rather than incidental encounters.

## Key Contributions

- Extends the digital-trace misinformation literature from political news into health, testing whether age-based vulnerability generalizes across domains.
- One of the first studies pairing linked survey data with passive web and YouTube traces specifically for health misinformation.
- Introduces a scalable hybrid pipeline (embeddings + fine-tuned GPT-4o + manual coding) to classify health content and rate credibility, validated against human coders.
- Maps referral pathways into low-credibility health sites, with platform-design implications: search and social are not the main gateways.
- Validates trace-based exposure measures by linking them to survey misperception and discernment outcomes.

## Methods

The authors linked YouGov's Pulse Panel survey data to RealityMine passive metering of 9.7M URLs across devices over ~4 weeks per participant. Health relevance was classified using YouGov tags plus OpenAI text embeddings; 1,155 health domains were hand-coded for credibility (78 flagged as low-credibility, Krippendorff's α = 1.00). YouTube health videos (~3,900) were rated via a hybrid manual + fine-tuned GPT-4o procedure (κ = 0.89–0.97). Survey instruments measured cancer headline discernment, false risk-factor beliefs, conspiracism, ideology, and demographics. Preregistered OLS regressions with robust standard errors and survey weights were supplemented by logistic and negative binomial models, plus temporal referrer-sequence analysis.

## Findings

- 13% of respondents visited any low-credibility health domain in the 4-week window; mean = 0.5 visits, max = 122.
- Exposure concentration: top 1% of users = 37% of all low-credibility exposure; top 10% = 77%.
- Adults 60+ were substantially more likely to be exposed than 18–29 year olds, robust to controls for total health and total web activity.
- Poorer cancer headline discernment and stronger false-risk-factor beliefs predicted greater exposure, with effects strongest among older adults.
- Older conservatives and older heavy consumers of right-leaning partisan news showed the highest exposure.
- Referrals came mainly from other low-credibility sites (especially for 60+), not from search engines or social media.
- On YouTube, absolute low-credibility exposure did not differ by age, but it constituted a larger share of older adults' overall lighter YouTube health diet.
- Dubious political news consumption and low-credibility health web visits independently predicted low-credibility YouTube health exposure, indicating cross-platform clustering.
- A media literacy intervention from a companion experiment produced no significant downstream effects on exposure.

## Connections

This paper directly extends the digital-trace tradition that has documented older adults' heightened engagement with untrustworthy political content into the health domain, complementing platform- and content-focused work on health misinformation ecosystems like [[Rothut2026-or]] and [[Bollenbacher2026-vz]]. Its finding that low-credibility consumption clusters across topics and platforms resonates with cross-domain perspectives on problematic information consumers seen in [[Efstratiou2026-ij]]. The null result for a media literacy treatment also speaks to ongoing debates about intervention efficacy explored in [[Scalco2026-bd]] and [[Song2025-yh]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lyons2026-ca.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-aging-online-health-misinformations/id1866587707?i=1000749136914)
