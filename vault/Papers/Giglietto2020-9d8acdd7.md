---
title: "It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"
aliases: ["It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"]
authors: ["Fabio Giglietto", "Nicola Righetti", "Luca Rossi", "Giada Marino"]
year: 2020
doi: 10.1080/1369118X.2020.1739732
bibtex_key: Giglietto2020-9d8acdd7
kind: own
topics: [coordinated-inauthentic-behavior, italian-elections-political-communication]
citation_count: 114
open_access: true
source_url: https://doi.org/10.1080/1369118X.2020.1739732
podcast_url: 
pdf_available: true
discovery_date: 
---

# It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections

## Summary

This paper argues that disinformation research has overinvested in content-veracity and bad-actor detection, and proposes instead an ecological, action-centered framing built around what the authors call *coordinated link sharing behavior* (CLSB) — networks of Facebook pages, groups, and verified profiles that repeatedly share the same URLs in near-simultaneous bursts. Using CrowdTangle data on Italian political news from the six months preceding the 2018 general election and the 2019 European election, the authors develop a reproducible algorithm to detect such networks and show that coordination is strongly associated with the diffusion of problematic information. They further distinguish openly political from deceptively non-political coordinated networks, linking these self-presentations to different content strategies and plausibly different (ideological vs. commercial) motivations.

## Key Contributions

- Reframes Facebook's operational notion of "coordinated inauthentic behavior" within scholarship on online coordination, participatory culture, and cloaked identities.
- Defines and operationalizes *coordinated link sharing behavior* as a measurable, action-based unit of analysis for disinformation research.
- Releases an open-source R algorithm for detecting CLSB from CrowdTangle link-share data, using a data-driven near-simultaneity threshold and a repetition threshold at the 90th percentile.
- Provides empirical evidence from two Italian elections that coordinated networks disproportionately spread content from known problematic domains and overlap with previously flagged disinformation pages.
- Introduces a typology distinguishing ideologically motivated (openly political) from commercially motivated (deceptive non-political) coordinated networks via the relationship between self-presentation and breadth of domains shared.

## Methods

- Two corpora of Italian political news URLs (84,815 in 2018; 164,760 in 2019) compiled from Google News, GDELT, and the Twitter Streaming API.
- CrowdTangle link endpoint used to retrieve all public Facebook/Instagram shares within 7 days of publication.
- Two-step detection algorithm: (1) estimate a near-simultaneous sharing window from the median time for the fastest 10% of URLs to reach 50% of their shares; (2) extract entities that repeatedly co-share within that window above the 90th-percentile frequency threshold.
- Cross-referencing of shared domains against Italian fact-checker blacklists (376 problematic domains) and of entities against Avaaz's list of 87 problematic Facebook pages; Risk Ratios compare coordinated vs. non-coordinated entities.
- Qualitative coding of each coordinated entity's self-presentation (political / non-political / mixed) and computation of a network-level "politicalness" score; Gini coefficient for domain concentration; Spearman correlations; degree centralization and clustering coefficient for network structure.

## Findings

- 24 coordinated networks (82 entities) detected in 2018; 92 networks (606 entities) in 2019.
- Coordinated entities shared problematic domains 1.79× more often in 2018 (95% CI [1.08, 2.96]) and 2.22× more often in 2019 (95% CI [1.35, 3.67]) than non-coordinated entities.
- Coordinated entities were 19.24× (2018) and 23.19× (2019) more likely to appear on the Avaaz problematic-pages list.
- Network composition shifted between elections: in 2018, 44% of networks were fully political, 27% non-political, 29% mixed; in 2019 mixed networks dominated (64%).
- Strong negative correlation between politicalness and domain-sharing concentration (r_s = −0.76 in 2018; r_s = −0.63 in 2019): non-political networks concentrate amplification on a narrow set of (often problematic) domains, while political networks diversify sources.
- Coordinated networks fall into two structural ideal types — highly centralized (star-like) or highly clustered — but neither politicalness nor Gini coefficient predicts which configuration emerges.

## Connections

This paper is a foundational statement in the authors' ongoing program on CLSB, extended methodologically and empirically in [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], [[Giglietto2026-9b6a992d]], and [[Marino2024-2fbc690f]], with [[Giglietto2019-882f1900]] situating it in the broader Italian electoral-disinformation context. Its action-based, network-detection logic anticipates later coordinated-behavior detection work such as [[Luceri2025-tr]], [[Minici2024-tf]], [[Graham2025-gp]], and [[Hurcombe2025-cs]], while the distinction between ideological and commercially motivated coordination resonates with downstream studies of inauthentic amplification dynamics.
