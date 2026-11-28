---
title: "It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"
aliases: ["It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"]
authors: ["Fabio Giglietto", "Nicola Righetti", "Luca Rossi", "Giada Marino"]
year: 2020
doi: 10.1080/1369118X.2020.1739732
bibtex_key: Giglietto2020-9d8acdd7
kind: own
topics: [coordinated-inauthentic-behavior, political-communication-elections]
citation_count: 265
open_access: true
source_url: https://doi.org/10.1080/1369118X.2020.1739732
podcast_url: 
pdf_available: true
discovery_date: 
editorial_notices: [correction]
---

# It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections

> [!note] Corrected
> - Correction (2020-04-21): [10.1080/1369118x.2020.1755558](https://doi.org/10.1080/1369118x.2020.1755558)

> Giglietto, F., Righetti, N., Rossi, L., & Marino, G. (2020). It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections. *Information, Communication & Society*. https://doi.org/10.1080/1369118X.2020.1739732
>
> [View paper](https://doi.org/10.1080/1369118X.2020.1739732)

## Summary

This paper argues that disinformation research should pivot away from detecting content veracity or bad actors and toward detecting *coordinated collective action*. The authors operationalize Facebook's vague operational term "coordinated inauthentic behavior" as **coordinated link sharing behavior (CLSB)** — networks of pages, groups, and verified profiles that repeatedly share the same URLs near-simultaneously. Using CrowdTangle data for Italian political news around the 2018 general election and 2019 European election, they develop a reproducible detection algorithm and show that coordinated networks are far more likely to spread problematic domains and to contain entities previously flagged as disinformation sources. A key distinction they draw is between openly political networks (likely ideologically motivated) and deceptively "non-political" networks (likely commercially motivated), which exhibit measurably different sharing strategies.

## Key Contributions

- Grounds Facebook's operational concept of "coordinated inauthentic behavior" in scholarship on online coordination, participatory culture, and authenticity/cloaked identity.
- Introduces a reproducible algorithm (open-source R implementation) for detecting coordinated link sharing behavior from CrowdTangle data.
- Provides empirical evidence linking coordinated sharing to problematic information across two Italian elections, supporting an action-based detection paradigm.
- Differentiates ideological vs. commercial motivations by relating entity self-presentation to the breadth of domains shared.
- Surfaces structural patterns (centralized vs. clustered networks) as open questions for future work.

## Methods

The authors compiled two datasets of Italian political news stories (N=84,815 in 2018; N=164,760 in 2019) from Google News, GDELT, and the Twitter Streaming API, then collected public Facebook/Instagram shares of those URLs within seven days of publication via the CrowdTangle link endpoint. Their two-step algorithm (1) estimates a "near-simultaneous sharing" time threshold from the median time for the fastest 10% of URLs to reach half their shares, and (2) extracts entities that repeatedly co-share above the 90th percentile of frequency. Shared domains were cross-referenced against blacklists from Italian fact-checkers (376 problematic domains) and entities against an Avaaz list of 87 flagged pages. They used Risk Ratios to compare problematic-content proportions, hand-coded each entity's self-presentation as political/non-political/mixed, and characterized networks via Gini coefficients, degree centralization, and clustering coefficients.

## Findings

- Identified 24 coordinated networks (82 entities) in 2018 and 92 networks (606 entities) in 2019.
- Coordinated entities shared problematic domains 1.79× more often (2018) and 2.22× more often (2019) than non-coordinated entities.
- Coordinated entities were 19.24× (2018) and 23.19× (2019) more likely to appear on the Avaaz list of problematic pages.
- Network composition shifted: in 2018, 44% of networks were entirely political; by 2019 the mixed category dominated (64%).
- A strong negative correlation between politicalness and domain-sharing concentration (r_s = −0.76 in 2018; −0.63 in 2019): openly political networks shared diverse sources, while non-political networks amplified a narrow set of often-problematic domains.
- Networks fell into two structural ideal types — highly centralized (star-like) or highly clustered — but neither politicalness nor sharing concentration explained the configuration.

## Connections

This is a foundational statement of the coordinated link sharing behavior program subsequently extended by the same research group — see [[Giglietto2020-6278a4aa]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], and [[Giglietto2024-cbeb3f70]] — and it connects to related Italian coordination work such as [[Nizzoli2020-cf]] and [[Marino2023-9137f448]]. Its action-based reframing of coordinated inauthentic behavior speaks directly to broader disinformation-detection debates represented by [[Starbird2019-qv]], [[Allcott2017-yz]], and [[Keller2019-nk]].
