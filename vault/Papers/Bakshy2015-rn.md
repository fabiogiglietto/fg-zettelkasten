---
title: "Political science. Exposure to ideologically diverse news and opinion on Facebook"
aliases: ["Political science. Exposure to ideologically diverse news and opinion on Facebook"]
authors: ["Eytan Bakshy", "Solomon Messing", "Lada A. Adamic"]
year: 2015
doi: 10.1126/science.aaa1160
bibtex_key: Bakshy2015-rn
topics: [political-polarization-partisan-media, misinformation-exposure-recalibration]
citation_count: 2275
open_access: false
source_url: https://doi.org/10.1126/science.aaa1160
podcast_url: 
pdf_available: true
discovery_date: 2015-06-15T00:00:00Z
---

# Political science. Exposure to ideologically diverse news and opinion on Facebook

> Bakshy, E., Messing, S., & Adamic, L. A. (2015). Political science. Exposure to ideologically diverse news and opinion on Facebook. *Science*, *348*, 1130–1132. https://doi.org/10.1126/science.aaa1160
>
> [View paper](https://doi.org/10.1126/science.aaa1160)

## Summary

This landmark study uses platform-internal data from 10.1 million self-identified U.S. Facebook users to trace how politically diverse news flows from friend networks, through the News Feed algorithm, to individual clicks. Bakshy, Messing, and Adamic decompose ideological exposure into distinct stages and find that although friend networks are homophilous, they still contain substantial cross-cutting ties. Crucially, individual choices about what to click suppress exposure to ideologically discordant content more than Facebook's ranking algorithm does. The paper pushes back on strong "filter bubble" and "echo chamber" narratives while documenting real, asymmetric ideological sorting in social-media news consumption.

## Key Contributions

- First large-scale, platform-internal measurement separating the roles of friend network composition, algorithmic ranking, and individual choice in shaping ideological exposure.
- Introduces an "alignment" (A) measure of content partisanship based on the average ideology of sharers, validated against known partisan outlets.
- Empirically apportions filter-bubble-like effects, concluding that user selection matters more than algorithmic curation.
- Offers an empirical counterweight to strong echo-chamber claims while documenting liberal/conservative asymmetries.
- Releases replication code, classifiers, and aggregate statistics via Harvard Dataverse.

## Methods

The authors built a deidentified dataset of 10.1 million active U.S. Facebook users who self-reported ideology over a six-month window (July 2014–January 2015). They collected ~7 million shared URLs and classified them as "hard" (politics, national, world) versus "soft" (entertainment, sports) using an SVM trained on n-gram text features. Restricting to ~226,000 hard-content URLs shared by at least 20 declared-affiliation users produced ~3.8 billion potential exposures, 903 million News Feed exposures, and 59 million clicks. Exposure was decomposed into four stages — a random baseline, network potential, algorithmically ranked feed exposure, and clicked content — with risk ratios for cross-cutting versus consistent content, adjusting for News Feed position effects.

## Findings

- Friend networks are homophilous but cross-cutting: the median liberal has ~20% conservative friends and the median conservative ~18% liberal friends (among those who report affiliation).
- Under random sharing, liberals would see ~45% cross-cutting content and conservatives ~40%; in practice, liberals' friends share 24% and conservatives' friends share 35%.
- The News Feed algorithm modestly reduces cross-cutting exposure (5% for conservatives, 8% for liberals).
- Individual click choices reduce cross-cutting consumption more (17% for conservatives, 6% for liberals), even controlling for feed position.
- Network composition is the single largest factor shaping ideological exposure; liberals encounter less cross-cutting content than conservatives, indicating asymmetric sorting.
- Users click only ~7% of available hard-content links, leaving headroom for greater cross-ideological consumption.

## Connections

This paper is a foundational empirical reference for the debate over algorithmic versus self-selected polarization, closely related to work re-examining exposure and curation dynamics on platforms such as [[Gonzalez-Bailon2024-rq]] and to studies measuring cross-cutting exposure and its effects like [[Eady2025-vm]]. Its decomposition of network, algorithm, and choice also speaks to broader efforts to recalibrate strong echo-chamber and misinformation-exposure claims, as in [[Budak2024-ef]] and [[Allcott2025-jb]].
