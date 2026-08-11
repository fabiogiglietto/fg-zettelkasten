---
title: "Multi-platform research in the light of technology affordances: networks of the far right in Germany"
aliases: ["Multi-platform research in the light of technology affordances: networks of the far right in Germany"]
authors: ["Azade E. Kakavand", "Nicola Righetti", "Annie Waldherr"]
year: 2026
doi: 10.1080/19331681.2026.2697186
bibtex_key: Kakavand2026-kt
topics: [online-radicalization-and-extremism-on-platforms, cross-national-coordinated-networks]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/19331681.2026.2697186
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kakavand2026-kt.mp3
pdf_available: true
discovery_date: 2026-08-11T08:00:56.893808Z
---

# Multi-platform research in the light of technology affordances: networks of the far right in Germany

> Kakavand, A. E., Righetti, N., & Waldherr, A. (2026). Multi-platform research in the light of technology affordances: networks of the far right in Germany. *Journal of Information Technology & Politics*, 1–20. https://doi.org/10.1080/19331681.2026.2697186
>
> [View paper](https://doi.org/10.1080/19331681.2026.2697186)

## Summary

This study offers a rare five-platform comparative analysis of German far-right networks, examining Facebook, Twitter (X), Instagram, YouTube, and Telegram through the lens of technology affordances. Its central argument is that affordances — connectivity, replicability, and scalability — are not fixed properties of platforms but *relational, sociotechnical outcomes* of the interplay between platform design and user practice. Using platform-specific forms of visible interaction (retweets, forwarded messages, reshares, mentions, subscriptions) as network edges, the authors show that even when the seed set of far-right actors is largely identical across platforms, the resulting network structures differ substantially in size, cohesion, key actors, and modes of circulation. The takeaway is methodological as much as substantive: single-platform studies capture only a fragment of a broader multi-platform communication ecosystem.

## Key Contributions

- A rare five-platform comparative network analysis of the far right, moving beyond single-platform designs.
- A method for empirically *inferring* affordances from network structure, mapping specific measures (HITS hubs/authorities, betweenness) to specific affordances (replicability, scalability, connectivity).
- A grounded, platform-specific characterization of German far-right networking practices, useful for research, civil society, and countermeasures.
- An affordance-based sociotechnical framework treating network structure as a joint outcome of platform features, user practices, and data accessibility.
- A candid account of the methodological challenges of multi-platform research under uneven data access (Twitter API costs, CrowdTangle discontinuation).

## Methods

Exploratory multi-platform network case study of the German-speaking far right over ~6 months in 2022. A seed list of prominent actors (AfD politicians/parties, journalists, alternative media, activists) drawn from prior research, Verfassungsschutz reports, and media coverage was expanded via three rounds of snowball sampling, with a final round retaining only nodes linking back to the sample. Edges were defined by platform-specific connectors — retweets/mentions (Twitter), forwarded messages (Telegram), reshares (Facebook), caption mentions/tags (Instagram), and channel subscriptions (YouTube). Data came from platform APIs (Twitter API v2, CrowdTangle, Google API, Telegram/Telethon), with YouTube captured as a single subscription snapshot. Analysis used Python (NetworkX) and Gephi, focusing on size-robust measures: weakly connected components, reciprocity, clustering, and Louvain modularity, plus HITS and betweenness for node roles.

## Findings

- **Twitter**: by far the largest network (~42K nodes, ~7.7M edges), a single, loosely connected, international broadcast arena with low clustering and reciprocity; authority scores exceed hub scores, signaling the salience of scalability.
- **Telegram**: second largest (~8.4K nodes), higher clustering but low reciprocity; inward-oriented and dominated by fringe/conspiracy channels, with differentiated producer, amplifier, and broker roles.
- **YouTube**: (~5.2K nodes) links disparate thematic genres (politics, weaponry, prepping, conspiracy) with low clustering and connectivity; subscription/recommendation ties may act as gateways to radicalization.
- **Instagram**: (~843 nodes) highest reciprocity, clustering, and modularity — tightly connected but fragmented echo chambers — yet dominated by mainstream actors, with a tightly knit but peripheral AfD cluster.
- **Facebook**: smallest network (~625 nodes), hierarchically dominated by the AfD, with national accounts as content-producing authorities and local accounts as amplifying hubs — an organized party strategy.
- Because seed accounts were largely shared across platforms, structural differences reflect platform-specific tendencies rather than differing actor sets.

## Connections

This paper sits within the study of online radicalization and the transnational networked far right, resonating with work on cross-platform far-right ecosystems and digital extremism such as [[Rothut2026-or]], [[Rothut2026-wt]], [[Askanius2026-de]], and [[Grusauskaite2026-po]]. Its attention to how situated user practices and platform features jointly shape far-right connectivity relates it to broader affordance-oriented and network studies of extremist communication, including [[Marwick2025-ov]] and [[Marwick2025-vx]]. The AfD-centred German focus and party-organized Facebook networking also connect it to research on national far-right movements like [[Schulte2026-df]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kakavand2026-kt.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
