---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2025
doi: 10.31235/osf.io/amfws_v1
bibtex_key: Tonneau2025-bv
topics: [platform-data-governance, public-perceptions-and-labor-impacts-of-ai]
citation_count: 2
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

This paper offers the first comparative empirical analysis of how six major social media platforms — YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn — allocate human content moderators across languages, leveraging transparency data mandated by the EU's Digital Services Act. The authors document substantial cross-lingual disparities in both language *coverage* (whether any moderators exist) and *intensity* (moderators relative to content volume). They find that smaller platforms leave millions of EU users without moderation in their national language, and that languages predominantly spoken in the Global South — Arabic, Spanish, Portuguese — receive consistently fewer moderators per unit of content than English. The paper argues that current DSA reporting, while a pivotal advance, is insufficient for independent scrutiny, and calls for globally inclusive transparency requirements.

## Key Contributions

- First comparative empirical analysis of cross-lingual moderator workforce allocation across six major DSA-regulated platforms.
- A novel methodology pairing DSA transparency disclosures with independently constructed, calibrated content-volume estimates to normalize moderator counts by language.
- Quantification of the number of EU users left without national-language moderation on specific platforms.
- Empirical evidence that extends and nuances earlier reports (e.g., Haugen disclosures, Global Witness) about underinvestment in non-English moderation.
- Concrete policy recommendations: reporting content volume per language, moderator workload capacity, harmful-content prevalence, and extending transparency obligations beyond the EU.

## Methods

The authors collected per-language moderator counts from DSA-mandated transparency reports (Summer 2023–Fall 2024) for the six platforms, averaging across reporting periods and treating non-reported EU languages as having zero moderators. To normalize counts by content volume, they built independent representative datasets — the TwitterDay corpus (375M tweets from a single day in 2022) and a random sample of ~26,000 YouTube videos. Language identification used fastText, with inference scores calibrated via isotonic regression against native-speaker annotations, and bootstrap resampling (1,000 samples) to estimate per-language counts with confidence intervals. Twitter/X user locations were mapped to countries via the Google Geocoding API, and DSA-reported EU user counts were used to estimate how many users lack moderators for their national language.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages; Twitter/X, LinkedIn, and Snapchat have multiple blind spots, especially in Southern, Eastern, and Northern Europe.
- Roughly 16M EU Twitter/X users (14%), 8M LinkedIn users (16%), and 7M Snapchat users (7%) have no moderators for their national language.
- Languages under Twitter/X blind spots represent, on average, 31% of tweets in countries where they are official.
- On Twitter/X, only Bulgarian and German have more moderators than English relative to content volume; Italian and Bulgarian have similar counts despite Italian content being 78× more prevalent.
- On Twitter/X, Portuguese, Arabic, and Spanish receive just 9%, 7%, and 7% of English's per-content allocation respectively.
- On YouTube, most covered EU languages receive proportionally more moderators than English — only Spanish and Portuguese receive less, signaling reduced investment in Latin American user bases.
- Global South languages average 55% of English's allocation on YouTube down to 7.5% on Twitter/X.
- Interface language support and moderation staffing are mismatched: some UI-supported languages (Greek, Czech, Romanian) lack dedicated moderators, while some moderated languages (Tagalog) lack UI support.

## Connections

This paper sits within the platform-governance-data-access literature that treats DSA transparency reporting as a rich but flawed empirical resource. It connects most directly to critical assessments of DSA transparency data quality and utility, such as [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Votta2025-xz]], and to work on platform accountability and access under the DSA regime like [[Ahuja2025-ku]]. Its focus on linguistic and Global South inequities in moderation complements broader concerns about uneven platform governance across regions and communities.
