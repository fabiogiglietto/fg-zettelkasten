---
title: "It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"
aliases: ["It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"]
authors: ["Fabio Giglietto", "Nicola Righetti", "Luca Rossi", "Giada Marino"]
year: 2020
doi: 10.1080/1369118X.2020.1739732
bibtex_key: Giglietto2020-9d8acdd7
kind: own
topics: [coordinated-inauthentic-behavior, election-campaigns-on-social-media]
citation_count: 232
open_access: true
source_url: https://doi.org/10.1080/1369118X.2020.1739732
podcast_url: 
pdf_available: true
discovery_date: 
---

# It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections

> Giglietto, F., Righetti, N., Rossi, L., & Marino, G. (2020). It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections. *Information, Communication & Society*. https://doi.org/10.1080/1369118X.2020.1739732
>
> [View paper](https://doi.org/10.1080/1369118X.2020.1739732)

## Summary

This paper argues that disinformation research should pivot from content-veracity and bad-actor detection toward identifying **coordinated collective action** on platforms. Using CrowdTangle data on Facebook shares of Italian political news during the run-ups to the 2018 general and 2019 European elections, the authors develop a reproducible algorithm to detect entities that repeatedly share the same URLs near-simultaneously. These "coordinated link sharing behavior" (CLSB) networks are shown to be strongly associated with the diffusion of problematic domains and with entities previously flagged as disinformation sources. The paper further distinguishes networks by their self-presentation (openly political vs. deceptively non-political), linking these to different — likely ideological vs. commercial — sharing strategies.

## Key Contributions

- Grounds Facebook's operational label "coordinated inauthentic behavior" in scholarly work on online coordination, participatory culture, and cloaked identities.
- Introduces a reproducible two-step algorithm (open-source R code) for detecting CLSB from CrowdTangle data, based on a data-driven time threshold and repeated co-sharing.
- Provides empirical evidence that coordinated sharing patterns are linked to problematic information across two Italian elections.
- Differentiates ideologically-motivated from commercially-motivated coordinated networks via the interaction of politicalness and domain-sharing breadth.
- Identifies two recurring structural configurations of coordinated networks — highly centralized and highly clustered — as an open puzzle for future work.

## Methods

- Two corpora of Italian political news stories were built from Google News, GDELT, and the Twitter Streaming API for the six months prior to each election (~85k URLs in 2018; ~165k in 2019).
- Public Facebook/Instagram shares within 7 days of publication were harvested via CrowdTangle.
- The CLSB algorithm (1) estimates a "near-simultaneous" sharing window from the median time for the fastest 10% of URLs to reach half their shares, and (2) retains entities that co-share within that window above the 90th percentile of frequency.
- Shared domains and entities were cross-referenced against Italian fact-checker blacklists (376 domains) and an Avaaz list of 87 problematic Facebook pages; Risk Ratios compared coordinated vs. non-coordinated entities.
- Each coordinated entity was qualitatively coded as political / non-political / mixed to yield a network-level "politicalness" score; Gini coefficients captured domain-sharing concentration; Spearman correlations related the two; degree centralization and clustering coefficients characterized network structure.

## Findings

- Identified 24 coordinated networks (82 entities) in 2018 and 92 networks (606 entities) in 2019.
- Coordinated entities shared problematic domains 1.79× more often (2018) and 2.22× more often (2019) than non-coordinated entities.
- Coordinated entities were 19.24× (2018) and 23.19× (2019) more likely to appear on the Avaaz list of problematic Facebook pages.
- Network composition shifted between elections: in 2018, 44% of networks were fully political; in 2019, 64% were of mixed composition.
- Strong negative Spearman correlations between politicalness and domain concentration (r_s = -0.76 in 2018; -0.63 in 2019): non-political networks amplified a narrow band of (often problematic) domains, while political networks drew from broader source repertoires.
- Networks fell into two structural ideal-types (star-like centralized vs. densely clustered), but neither politicalness nor concentration explained which form emerged.

## Connections

This paper is a foundational statement in the author group's programme on coordinated link sharing, extended and refined in [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], and [[Giglietto2026-9b6a992d]], and its methodological lineage traces back to [[Giglietto2019-882f1900]]. The behavior-centered detection approach it advocates connects directly to broader work on coordinated inauthentic behavior detection and network-level manipulation such as [[Graham2026-fb]], [[Graham2025-gp]], [[Luceri2025-tr]], [[Minici2024-tf]], and [[Kim2026-br]].
