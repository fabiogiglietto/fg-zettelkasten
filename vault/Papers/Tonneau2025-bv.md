---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2026
doi: 10.1145/3805689.3806484
bibtex_key: Tonneau2025-bv
topics: [platform-governance-data-access, misinformation-exposure-recalibration]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3805689.3806484
podcast_url: 
pdf_available: true
discovery_date: 2025-08-15T00:00:00Z
---

# Language Disparities in Moderation Workforce Allocation by Social Media Platforms

> Tonneau, M., Liu, D., McGrady, R., Zheng, K., Schroeder, R., Zuckerman, E., & Hale, S. (2026). Language Disparities in Moderation Workforce Allocation by Social Media Platforms. *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency*. https://doi.org/10.1145/3805689.3806484
>
> [View paper](https://doi.org/10.1145/3805689.3806484)

## Summary

This paper offers the first comparative empirical analysis of how six major social media platforms (YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn) distribute human content moderators across languages. Using transparency data mandated by the EU's Digital Services Act (DSA), combined with independently constructed content-volume estimates, the authors document substantial cross-lingual disparities in both language coverage and moderator-to-content ratios. They find that smaller platforms leave millions of EU users without any moderation in their national language, and that languages predominantly spoken in the Global South — Spanish, Portuguese, Arabic — receive consistently fewer moderators per unit of content than English. The paper argues that current DSA reporting, while a pivotal advance, is insufficient for independent scrutiny and calls for globally inclusive transparency requirements.

## Key Contributions

- First comparative empirical study of cross-lingual moderator workforce allocation across six DSA-regulated platforms.
- A novel methodology normalizing self-reported moderator counts against independently constructed, calibrated content-volume estimates per language.
- Quantification of how many EU users lack national-language moderation on specific platforms.
- Empirical grounding for prior anecdotal reports (e.g., Haugen disclosures, Global Witness) on underinvestment in non-English moderation.
- Concrete policy recommendations: mandate reporting of content volume per language, moderator capacity, harmful-content prevalence, and extend transparency beyond the EU.

## Methods

The authors collected per-language moderator counts from DSA transparency reports (Summer 2023–Fall 2024), averaging across reporting periods and treating non-reported EU languages as zero. To normalize by content volume, they used independent datasets — the TwitterDay corpus (375M tweets) and a random sample of ~26,000 YouTube videos — applying fastText language identification calibrated via isotonic regression against native-speaker annotations. Bootstrap resampling (1,000 samples) yielded per-language content estimates with confidence intervals. Twitter/X user locations were geocoded to countries, and DSA-reported user counts were used to estimate populations lacking national-language moderation, categorized via the UN geoscheme.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages; Twitter/X, LinkedIn, and Snapchat have multiple blind spots, especially in Southern, Eastern, and Northern Europe.
- Roughly 16M Twitter/X users (14% of EU base), 8M LinkedIn users (16%), and 7M Snapchat users (7%) have no moderators for their national language.
- Languages subject to Twitter/X blind spots average 31% of tweets in countries where they are official.
- On Twitter/X, Portuguese, Arabic, and Spanish receive only 9%, 7%, and 7% of English's moderator-per-content allocation.
- On YouTube most covered EU languages receive proportionally more moderators than English, except Spanish and Portuguese — signaling reduced investment in Latin American users.
- Global South languages average from 55% of English's allocation on YouTube down to just 7.5% on Twitter/X.
- Interface language support and moderation staffing are mismatched (e.g., Greek, Czech, Romanian supported but unmoderated; Tagalog moderated but unsupported in UI).

## Connections

This paper sits within the platform-governance and DSA data-access strand, using mandated transparency disclosures as an empirical lever much as [[Rieder2025-ju]] and [[Votta2025-xz]] interrogate the limits and promise of DSA-derived data. Its critique of insufficient, non-normalizable transparency reporting speaks directly to broader debates about platform accountability and researcher data access. The focus on linguistic and Global South inequities in moderation complements work on uneven exposure and platform practices across communities, though most other papers in these topics address misinformation dynamics rather than moderation workforce allocation specifically.
