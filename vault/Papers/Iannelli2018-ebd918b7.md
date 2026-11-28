---
title: "Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"
aliases: ["Facebook Digital Traces for Survey Research: Assessing the Efficiency and Effectiveness of a Facebook Ad–Based Procedure for Recruiting Online Survey Respondents in Niche and Difficult-to-Reach Populations"]
authors: ["Laura Iannelli", "Fabio Giglietto", "Luca Rossi", "Elisabetta Zurovac"]
year: 2018
doi: 10.1177/0894439318816638
bibtex_key: Iannelli2018-ebd918b7
kind: own
topics: [survey-methodology-validity, research-methods-data-access]
citation_count: 85
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

This paper develops and tests a Facebook ad–based procedure for recruiting online survey respondents from niche, hard-to-reach populations, using supporters of conspiracy theories in Italy as a test case. The authors leverage then-recent Facebook marketing features — Pixel conversion tracking, URL parameter passing, and Pixel-based custom audience exclusion — to improve measurement of response rates and control of sample quality. Across a 53-day campaign targeting Italian users interested in vaccine controversies and chemtrails conspiracies, they recruited 1,069 valid respondents at €0.46 each with a 3.28% conversion rate. The procedure proved highly efficient and affordable, but its effectiveness at reaching ideologically distinctive respondents was inconclusive: the Facebook sample did not endorse conspiracy beliefs significantly more than a general-population CAWI benchmark.

## Key Contributions

- A replicable, technically detailed protocol for Facebook ad–based survey recruitment using Pixel conversion tracking, URL parameter passing, and custom audience exclusion.
- Proposes "conversion rate" (valid completions / reach) as a more precise response-rate metric than the click-through rates (CTRs) used in prior work.
- Provides empirical efficiency benchmarks — cost per respondent, conversion rate, time cost — for future campaigns.
- Extends the Facebook ad-recruitment literature from health and political-affiliation targets to the domain of controversial/stigmatized belief (conspiracy theories).
- Offers practical guidance on ad design, image rotation, comment management, and incentive substitution (emphasizing brevity and anonymity).

## Methods

An online non-probability quota survey of Italian adults (age/gender quotas from national statistics) was targeted via Facebook ads to users tagged with "vaccines controversy" and "chemtrails conspiracy" interests (the more generic "moon landing" interest was excluded). The campaign used 12 demographic micro-targets (6 age cohorts × 2 genders), each receiving four ad creatives on a shared template, and was optimized for conversions rather than clicks. The survey was hosted on TypeForm PRO via a dedicated domain, with a Facebook Pixel on the thank-you page to track completions, auto-exclude completers, and build a custom audience; URL parameters carrying age/gender detected respondents arriving via social sharing. After removing duplicate IPs and parameter-less (shared) responses, data were post-stratification weighted and compared against the ITANES 2016 CAWI benchmark (n=3,027) using Kruskal–Wallis tests and effect size measures.

## Findings

- The 53-day campaign (Dec 2017–Jan 2018) generated 82,233 impressions, reached 32,613 unique users, and produced 1,140 conversions, of which 1,069 were valid.
- The 3.28% conversion rate outperformed nearly all CTRs reported in prior Facebook ad–based survey studies (0.04–4.07).
- Total cost was €488, averaging €0.46 per valid respondent — substantially cheaper than typical panel recruitment.
- Kruskal–Wallis tests found no significant difference in conspiracy-belief distributions between the Facebook and ITANES samples, with negligible effect sizes.
- Some evidence of greater polarization: 68% of the Facebook sample endorsed no conspiracy theories vs. 53% in ITANES, though data transformation complicates interpretation.
- The Pixel + URL parameter implementation successfully excluded 45 duplicate-IP and 26 socially-shared completions, enabling cleaner sample boundaries.

## Connections

This paper sits in the methodological strand concerned with research access to platform data amid tightening APIs after Cambridge Analytica, treating Facebook's ad platform as an alternative data-collection pathway; it relates to broader discussions of data access and platform-based research infrastructure such as [[Freelon2018-ao]] and Davies2024-sc. Beyond these, the other papers listed under the shared topics largely address content-level platform data and misinformation rather than survey recruitment methodology, so direct intellectual links are limited.
