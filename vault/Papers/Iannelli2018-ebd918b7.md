---
title: "Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"
aliases: ["Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"]
authors: ["Laura Iannelli", "Fabio Giglietto", "Luca Rossi", "Elisabetta Zurovac"]
year: 2018
doi: 10.1177/0894439318816638
bibtex_key: Iannelli2018-ebd918b7
kind: own
topics: [computational-social-science-methods]
citation_count: 40
open_access: true
source_url: https://doi.org/10.1177/0894439318816638
podcast_url: 
pdf_available: true
discovery_date: 
---

# Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations

## Summary

This paper proposes and tests a Facebook ad-based recruitment procedure for online surveys targeting niche, hard-to-reach populations, using Italian supporters of vaccine and chemtrails conspiracy theories as a case study. The authors leverage post-2017 Facebook marketing infrastructure — Pixel conversion tracking, URL parameter passing, and custom audience exclusion — to gain tighter control over sample boundaries and to compute a more precise response-rate metric than the click-through rates used in earlier work. They argue the approach is highly efficient (cheap, fast, replicable), but find its effectiveness at recruiting ideologically distinctive respondents inconclusive: Facebook interest-targeted respondents did not endorse conspiracy claims significantly more than a general-population CAWI benchmark.

## Key Contributions

- A technically detailed, replicable protocol for Facebook ad-based survey recruitment integrating Pixel, URL parameters, and custom audience exclusion.
- Introduction of a **conversion rate** metric (valid completions / reach) as a more precise alternative to CTR for evaluating Facebook ad-based surveys.
- Empirical efficiency benchmarks (€0.46/respondent, 3.28% conversion rate, 53-day fielding) for future comparison.
- Extension of Facebook ad-recruitment methodology from health/political-affiliation domains into stigmatized belief domains (conspiracy theories).
- Practical guidance on ad creative design, image rotation, comment moderation, and using brevity as an alternative to monetary incentives.

## Methods

Non-probability quota survey (Italian adults, age/gender quotas from ISTAT) recruited via Facebook ads targeting users tagged with "vaccines controversy" and "chemtrails conspiracy" interests. 12 demographic micro-segments (6 age × 2 gender) each received 4 ad creatives; the campaign was optimized for conversions rather than clicks. The survey was hosted on TypeForm PRO via a dedicated domain, with a Facebook Pixel on the thank-you page tracking completions, auto-excluding completers, and building a custom audience. URL parameters carrying age/gender detected and removed socially-shared completions. After cleaning (45 duplicate IPs, 26 sharing-based responses), 1,069 valid responses were post-stratification weighted and compared against the ITANES 2016 CAWI panel (n=3,027) on three conspiracy-belief items using Kruskal–Wallis tests and effect sizes.

## Findings

- 53-day campaign: 82,233 impressions, 32,613 unique users reached, 1,140 conversions, 1,069 valid responses.
- Conversion rate of 3.28% exceeded nearly all CTRs reported in prior Facebook ad-based survey work.
- Total cost €488 (~€0.46 per valid respondent), well below typical online panel costs.
- Facebook-recruited respondents did **not** significantly differ from the ITANES general-population sample in conspiracy endorsement; effect sizes were negligible.
- Some sign of polarization: 68% of the Facebook sample endorsed no conspiracy theory vs. 53% in ITANES, though comparability transformations complicate interpretation.
- The Pixel + URL parameter setup successfully filtered out duplicate-IP and socially-shared completions.

## Connections

This study sits in the methodological strand of computational social science concerned with combining platform data and survey research, sharing concerns with [[Schulte2026-df]] and [[Hepp2026-oi]] on integrating digital traces into social-scientific inquiry, and complementing work on the affordances and constraints of platform-mediated research after the post-Cambridge-Analytica API contraction (e.g., [[Freelon2024-sc]], [[Rieder2025-ju]]). Its skepticism toward Facebook interest categories as reliable proxies for offline opinions echoes broader concerns about platform-elaborated user attributes raised in audit and measurement work such as [[Ulloa2024-jm]].
