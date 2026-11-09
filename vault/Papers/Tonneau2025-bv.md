---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2026
doi: 10.1145/3805689.3806484
bibtex_key: Tonneau2025-bv
topics: [platform-governance-data-access, computational-network-structure-analysis]
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

This paper offers the first comparative empirical analysis of how six major social media platforms — YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn — distribute human content moderators across languages. Drawing on transparency reports mandated by the EU's Digital Services Act (DSA), the authors document substantial cross-lingual disparities in both language *coverage* (whether a language has any human moderators at all) and *intensity* (moderators relative to content volume). They find that smaller platforms leave millions of EU users without moderation in their national language, and that languages predominantly spoken in the Global South — Spanish, Portuguese, Arabic — receive consistently fewer moderators per unit of content than English. The paper argues that DSA transparency, while a pivotal advance, remains insufficient for independent scrutiny because platforms do not disclose content volume per language, and calls for more meaningful, globally inclusive reporting requirements.

## Key Contributions

- First comparative empirical analysis of cross-lingual moderator workforce allocation across six major DSA-regulated platforms.
- A novel methodology combining DSA transparency disclosures with independently constructed, calibrated content-volume estimates to normalize moderator counts by language.
- Quantification of the number of EU users left without national-language moderation on specific platforms.
- Empirical grounding that extends prior whistleblower and NGO reports (e.g., Haugen disclosures, Global Witness) on non-English underinvestment.
- Concrete policy recommendations: require platforms to report content volume per language, moderator workload capacity, and harmful-content prevalence, and to extend transparency obligations beyond the EU.

## Methods

The authors collected moderator counts per language from DSA-mandated transparency reports (Summer 2023–Fall 2024), averaging across reporting periods and treating non-reported EU languages as having zero moderators. To normalize by content volume, they built independent language-share estimates: the TwitterDay dataset (375M tweets from one day in 2022) for Twitter/X and a random sample of ~26,000 YouTube videos for YouTube. Language identification used fastText on tweet text and video titles/descriptions, with inference scores calibrated via isotonic regression against native-speaker annotations, and bootstrap resampling (1,000 samples) for confidence intervals. Twitter/X user locations were mapped to countries via the Google Geocoding API, and DSA-reported EU user counts were used to estimate how many users lack national-language moderation, categorized with the UN geoscheme.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages; Twitter/X, LinkedIn, and Snapchat have multiple blind spots, especially in Southern, Eastern, and Northern Europe.
- Roughly 16M EU Twitter/X users (14%), 8M LinkedIn users (16%), and 7M Snapchat users (7%) have no moderators for their national language.
- On Twitter/X, blind-spot languages account for an average 31% of tweets in countries where they are official.
- On Twitter/X, only Bulgarian and German exceed English in moderators-per-content; Portuguese, Arabic, and Spanish each receive only 7–9% of English's allocation.
- On YouTube most covered EU languages receive proportionally *more* moderators than English, with Spanish and Portuguese the exceptions — signaling reduced investment in Latin American user bases.
- Global South languages average 55% of English's per-content allocation on YouTube, falling to 7.5% on Twitter/X.
- Interface support and moderation staffing are misaligned: some UI-supported languages (Greek, Czech, Romanian) lack dedicated moderators, while some moderated languages (Tagalog) lack UI support.

## Connections

This paper is a strong empirical contribution to the DSA-driven platform transparency and data-access literature, offering a critical counterpoint to studies that assess what disclosed data can and cannot reveal — see [[Rieder2025-ju]] and [[Votta2025-xz]] on the affordances and limits of platform transparency reporting. Its focus on labour, inequity, and the governance of moderation extends classic accounts of content moderation as infrastructure such as [[Gillespie2010-as]] and [[Gillespie2022-jx]], while its concern with who platform data and oversight serve resonates with debates on access and accountability in [[Gonzalez-Bailon2023-uy]] and [[Freelon2018-ao]].
