---
title: "Language Disparities in Moderation Workforce Allocation by Social Media Platforms"
aliases: ["Language Disparities in Moderation Workforce Allocation by Social Media Platforms"]
authors: ["Manuel Tonneau", "Diyi Liu", "Ryan McGrady", "Kevin Zheng", "Ralph Schroeder", "Ethan Zuckerman", "Scott Hale"]
year: 2025
doi: 10.31235/osf.io/amfws_v2
bibtex_key: Tonneau2025-bv
topics: [platform-governance-and-data-access, research-methods-and-ethics-in-css]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/amfws_v2
podcast_url: 
pdf_available: true
discovery_date: 2025-08-15T00:00:00Z
---

# Language Disparities in Moderation Workforce Allocation by Social Media Platforms

> Tonneau, M., Liu, D., McGrady, R., Zheng, K., Schroeder, R., Zuckerman, E., & Hale, S. (2025). Language Disparities in Moderation Workforce Allocation by Social Media Platforms. https://doi.org/10.31235/osf.io/amfws_v2
>
> [View paper](https://doi.org/10.31235/osf.io/amfws_v2)

## Summary

This paper offers the first comparative empirical analysis of how six major social media platforms — YouTube, Meta, TikTok, Twitter/X, Snapchat, and LinkedIn — allocate their human content moderators across languages. Leveraging transparency disclosures newly mandated by the EU's Digital Services Act (DSA), the authors document substantial cross-lingual disparities in both language coverage and moderator-to-content ratios. They find that millions of EU users on smaller platforms post in languages with no human moderation at all, and that even where moderators exist, "Global South" languages like Spanish, Portuguese, and Arabic receive proportionally far fewer moderators than English. The paper frames DSA transparency as a pivotal but incomplete step and calls for more meaningful, globally inclusive reporting requirements.

## Key Contributions

- First comparative empirical analysis of cross-lingual moderator workforce allocation across six DSA-regulated platforms.
- Novel methodology combining DSA transparency disclosures with independently constructed, calibrated content-volume estimates to normalize moderator counts by language.
- Quantification of the number of EU users left without national-language moderation on specific platforms.
- Empirical corroboration and nuancing of prior journalistic and whistleblower reports (e.g., Haugen disclosures, Global Witness) on underinvestment in non-English moderation.
- Concrete policy recommendations: require platforms to report content volume per language, moderator workload capacity, and harmful-content prevalence, and extend transparency obligations beyond the EU.

## Methods

The authors collected per-language moderator counts from DSA-mandated transparency reports (Summer 2023–Fall 2024), averaging across reporting periods and treating non-reported EU languages as having zero moderators. To make raw counts interpretable, they normalized by estimated content volume per language using independent representative datasets: the TwitterDay corpus (375M tweets from one day in September 2022) for Twitter/X and a random sample of ~26,000 YouTube videos for YouTube. Language identification relied on fastText applied to tweet text and video titles/descriptions, with inference scores calibrated via isotonic regression against native-speaker annotations. Bootstrap resampling (1,000 samples) yielded confidence intervals on expected post/video counts, and Twitter/X user locations were geocoded to countries to compute country-level language shares and estimate affected user populations.

## Findings

- YouTube, Meta, and TikTok cover nearly all EU official languages, while Twitter/X, LinkedIn, and Snapchat have multiple blind spots, concentrated in Southern, Eastern, and Northern Europe.
- Roughly 16M EU Twitter/X users (14%), 8M LinkedIn users (16%), and 7M Snapchat users (7%) have no moderators for their national language.
- Languages subject to Twitter/X blind spots represent on average 31% of tweets in countries where they are official.
- On Twitter/X, only Bulgarian and German exceed English in moderators-per-content; Italian and Bulgarian have similar counts despite Italian content being 78× more prevalent.
- On Twitter/X, Portuguese, Arabic, and Spanish receive only 9%, 7%, and 7% of English's moderator-per-content allocation respectively.
- On YouTube, most covered EU languages fare better than English; only Spanish and Portuguese receive less, suggesting reduced investment in Latin American user bases.
- Global South languages average 55% of English's allocation on YouTube, falling to just 7.5% on Twitter/X.
- UI language support and moderation investment diverge: Greek, Czech, and Romanian are interface-supported but lack dedicated moderators, while Tagalog has moderators but no interface support.

## Connections

This paper sits squarely within the platform-governance strand of the register, extending debates about platform accountability and the limits of mandated transparency; it complements work probing what DSA and related regimes actually make visible, such as [[Rieder2025-ju]] and [[Ober2026-vd]]. Its methodological reliance on large-scale language-identified Twitter/X samples connects it to data-infrastructure and measurement discussions around platform data access found in [[Freelon2018-ao]] and [[Lazer2018-mm]]. More broadly, its focus on linguistic and Global South inequities in moderation adds an empirical dimension to the governance literature represented here by foundational references like [[Gillespie2010-as]] and [[van-Dijck2018-up]].
