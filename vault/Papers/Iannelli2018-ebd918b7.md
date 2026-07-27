---
title: "Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"
aliases: ["Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"]
authors: ["Laura Iannelli", "Fabio Giglietto", "Luca Rossi", "Elisabetta Zurovac"]
year: 2018
doi: 10.1177/0894439318816638
bibtex_key: Iannelli2018-ebd918b7
kind: own
topics: [survey-methodology-validity, platform-data-access-and-governance]
citation_count: 88
open_access: true
source_url: https://doi.org/10.1177/0894439318816638
podcast_url: 
pdf_available: true
discovery_date: 
---

# Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations

> Iannelli, L., Giglietto, F., Rossi, L., & Zurovac, E. (2018). Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations. *Social Science Computer Review*. https://doi.org/10.1177/0894439318816638
>
> [View paper](https://doi.org/10.1177/0894439318816638)

## Summary

This paper develops and stress-tests a Facebook ad–based procedure for recruiting online survey respondents in niche, difficult-to-reach populations, using Italian supporters of vaccine and chemtrails conspiracy theories as a test case. The authors exploit recent Facebook marketing features — Pixel conversion tracking, URL parameter passing, and Pixel-derived custom audience exclusion — to build a replicable protocol that also yields a more precise response-rate measure than the click-through rates used in prior work. Across a 53-day campaign they recruited 1,069 valid respondents at €0.46 each with a 3.28% conversion rate, demonstrating clear efficiency. However, when compared to an ITANES CAWI benchmark, the Facebook-recruited sample was not meaningfully more conspiracy-endorsing, leaving the *effectiveness* of interest-based targeting for stigmatized opinions unresolved.

## Key Contributions

- A replicable, technically detailed Facebook ad recruitment protocol integrating Pixel, URL parameters, and custom audience exclusion.
- Introduction of a **conversion rate** metric (valid completions / reach) as a more accurate response-rate proxy than CTR.
- Empirical cost and yield benchmarks (€0.46 per respondent; 3.28% conversion) for future campaigns.
- Extension of Facebook ad–recruitment methodology from health/political domains to controversial-belief targeting.
- Practical design guidance on ad creatives, image rotation, comment moderation, and using brevity/anonymity in place of monetary incentives.

## Methods

Non-probability quota survey (age/gender quotas from ISTAT) targeting Italian Facebook users tagged with "vaccines controversy" and "chemtrails conspiracy" interests, split into 12 age×gender micro-audiences each served four ad creatives. The survey ran on TypeForm PRO under a dedicated domain, launched from a purpose-built Facebook page, with the campaign optimized for conversions. A Facebook Pixel on the thank-you page tracked completions, auto-excluded completers, and populated a custom audience; URL parameters encoding age/gender flagged respondents arriving via social sharing. After removing duplicate-IP and parameterless responses, data were post-stratified and compared to the ITANES 2016 CAWI panel (n=3,027) via Kruskal–Wallis tests and effect-size measures in R.

## Findings

- 53-day campaign: 82,233 impressions, 32,613 unique users reached, 1,140 conversions, 1,069 valid after cleaning.
- 3.28% conversion rate — higher than nearly all CTRs reported in prior Facebook ad-survey studies.
- Total spend of €488, i.e., €0.46 per valid respondent — well below typical panel costs.
- No significant difference in conspiracy-belief distributions between the Facebook sample and the ITANES general-population sample; effect sizes were negligible.
- Some evidence of polarization: 68% of the Facebook sample endorsed no conspiracy theory vs. 53% in ITANES, though comparability transformations complicate this reading.
- Pixel + URL parameter machinery successfully excluded 45 duplicate-IP and 26 socially-shared completions.

## Connections

This paper sits in the methodological strand of computational social science concerned with using platform infrastructures to build samples and link survey data to digital traces, an agenda that intersects with API-access constraints and data-donation approaches explored in [[Bouchaud2026-lr]] and [[Rieder2025-ju]]. Its concern with whether platform-inferred "interests" validly capture ideological or belief-based subpopulations resonates with work on conspiracy and problematic-information audiences such as [[Giglietto2024-cbeb3f70]] and [[Giglietto2022-b30e8b4e]]. Beyond these, connections to other papers in the topic list are thematic rather than substantive.
