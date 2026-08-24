---
title: "Political science. Exposure to ideologically diverse news and opinion on Facebook"
aliases: ["Political science. Exposure to ideologically diverse news and opinion on Facebook"]
authors: ["Eytan Bakshy", "Solomon Messing", "Lada A. Adamic"]
year: 2015
doi: 10.1126/science.aaa1160
bibtex_key: Bakshy2015-rn
topics: [political-polarization-and-engagement, platform-policy-and-content-visibility]
citation_count: 2107
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

This paper offers the first large-scale, platform-internal measurement of how ideologically diverse news travels through Facebook to American users with declared political affiliations. Drawing on 10.1 million users over six months, Bakshy, Messing, and Adamic decompose the path from a friend's share to a personal click into distinct stages — friend network composition, News Feed algorithmic ranking, and individual click choice — and quantify how each filters out cross-cutting political content. Their central argument is that while Facebook is ideologically sorted, the strongest filter is users' own networks and click behavior, not the ranking algorithm. The paper thus complicates strong "filter bubble" narratives while documenting meaningful, asymmetric ideological homophily in online news consumption.

## Key Contributions

- First in-platform measurement separating the contributions of *network*, *algorithm*, and *individual choice* to cross-cutting news exposure on a major social platform.
- An "alignment" score for content partisanship derived from the ideological distribution of sharers, validated against canonical partisan outlets.
- Empirical evidence that individual click choices suppress cross-cutting exposure more than algorithmic ranking does — a direct empirical counter to strong filter-bubble claims.
- Documentation of an asymmetry: liberals encounter less cross-cutting content via their networks than conservatives do.
- Publicly released code, classifiers, and aggregate statistics for replication.

## Methods

The authors built a deidentified dataset of 10.1 million U.S. Facebook users who self-reported ideology (July 2014 – January 2015). Roughly 7 million distinct shared URLs were classified as "hard" (politics, national, world) versus "soft" news using an SVM on n-gram text features. Restricting to ~226,000 hard-news URLs shared by at least 20 affiliated users yielded ~3.8 billion potential exposures, 903 million News Feed exposures, and 59 million clicks. Each article received an alignment score equal to the mean ideology of its sharers. They then computed risk ratios for cross-cutting versus consistent content at each pipeline stage — random baseline, friend potential, ranked feed, click — adjusting for News Feed position effects.

## Findings

- Friend networks are partisan but not hermetic: the median liberal has ~20% conservative friends, the median conservative ~18% liberal friends (among affiliated friends).
- Random sharing would yield ~45% cross-cutting exposure for liberals and ~40% for conservatives; actual friend-shared rates fall to 24% and 35% respectively.
- The News Feed algorithm produces only a modest additional reduction: 5% (conservatives) and 8% (liberals).
- Individual click choice produces a larger reduction: 17% (conservatives) and 6% (liberals), even controlling for feed position.
- Users click on only ~7% of available hard-news links, leaving substantial untapped capacity for cross-ideological consumption.
- Network composition is the single largest factor shaping ideological exposure.

## Connections

This paper is a foundational empirical reference for ongoing debates about whether platforms structurally enforce echo chambers. It connects directly to work re-examining cross-platform echo chamber claims and selective exposure, such as [[Rossini2026-jn]], and to research on algorithmic curation and partisan information environments like [[Green2025-ap]] and [[Mosleh2024-op]]. It also provides the methodological and conceptual backdrop for studies of hyperpartisan content circulation and asymmetric polarization, including [[Rothut2026-or]] and [[Knupfer2025-vt]].
