---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2025
doi: 10.31235/osf.io/amfws_v1
bibtex_key: Tonneau2025-bv
topics: [platform-governance-data-access]
citation_count: 1
open_access: false
source_url: https://doi.org/10.31235/osf.io/amfws_v1
podcast_url: 
pdf_available: true
discovery_date: 2025-08-15T00:00:00Z
---

# Language Disparities in Moderation Workforce Allocation by Social Media Platforms

> Tonneau, M., Liu, D., McGrady, R., Zheng, K., Schroeder, R., Zuckerman, E., & Hale, S. (2025). Language Disparities in Moderation Workforce Allocation by Social Media Platforms. https://doi.org/10.31235/osf.io/amfws_v1
>
> [View paper](https://doi.org/10.31235/osf.io/amfws_v1)

## Summary

This paper provides the first comparative empirical analysis of how six major social media platforms (YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn) allocate human content moderators across languages, leveraging transparency disclosures mandated by the EU's Digital Services Act. By combining DSA-reported moderator counts with independently constructed estimates of content volume per language, the authors document substantial cross-lingual disparities: smaller platforms leave millions of EU users without any moderator for their national language, and across platforms, Global South languages (Spanish, Portuguese, Arabic) receive far fewer moderators per unit of content than English — ranging from 55% of English's allocation on YouTube down to just 7.5% on Twitter/X. The authors argue that current DSA transparency requirements, while a meaningful step, remain insufficient for independent accountability and should be strengthened and globalized.

## Key Contributions

- First cross-platform comparative analysis of moderator workforce allocation by language using DSA transparency data.
- A methodology for normalizing platform-disclosed moderator counts against independently estimated, calibrated content-volume-per-language baselines.
- Quantification of EU users left without national-language moderation: ~16M on Twitter/X, ~8M on LinkedIn, ~7M on Snapchat.
- Empirical confirmation and extension of prior anecdotal/whistleblower evidence (e.g., Haugen, Global Witness) of platform underinvestment in non-English moderation.
- Concrete policy recommendations for richer transparency reporting (content volume per language, workload capacity, harmful-content prevalence) and extending such obligations beyond the EU.

## Methods

The authors collected moderator counts per language from DSA transparency reports (Summer 2023–Fall 2024), averaged across reporting periods, and treated unreported EU languages as zero. To normalize by content volume, they used the TwitterDay dataset (375M tweets) for Twitter/X and a random sample of ~26,000 YouTube videos for YouTube, identifying languages via fastText calibrated through isotonic regression against native-speaker annotations. Bootstrap resampling (1,000 iterations) produced confidence intervals. Twitter user locations were mapped to countries via the Google Geocoding API, and DSA-reported EU country-level user counts were combined with the UN geoscheme to estimate users left without national-language moderation.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages with at least some moderators; Twitter/X, LinkedIn, and Snapchat have major blind spots, particularly in Southern, Eastern, and Northern Europe.
- On Twitter/X, only Bulgarian and German receive more moderators than English relative to content volume; Italian and Bulgarian have similar moderator counts despite Italian content being 78× more prevalent.
- On Twitter/X, Portuguese, Arabic, and Spanish receive only 7–9% of English's moderator-per-content allocation.
- YouTube allocates proportionally more moderators to most EU languages than to English, with Spanish and Portuguese as notable exceptions — suggesting underinvestment in Latin American audiences.
- Global South languages average 55% of English's allocation on YouTube but only 7.5% on Twitter/X.
- Mismatches exist between UI language support and moderation investment: Greek, Czech, and Romanian have UI support but no dedicated moderators; Tagalog has moderators but no UI support.
- In countries where they are official, languages subject to Twitter/X moderation blind spots account for an average of 31% of tweets.

## Connections

This paper directly extends platform-governance work that scrutinizes DSA transparency disclosures and their limits, connecting closely to [[Rieder2025-ju]] and [[Rieder2026-pp]] on the affordances and shortcomings of DSA-mandated data, and to [[Bouchaud2026-lr]] on empirical analyses leveraging DSA-era access. Its focus on linguistic inequity in moderation resonates with broader critiques of platform accountability and content governance found in [[Farkas2026-lr]] and [[Cazzamatta2026-lo]], while its policy framing around transparency reform aligns with [[Bak-Coleman2026-mk]] and [[Schiffrin_undated-gi]].
