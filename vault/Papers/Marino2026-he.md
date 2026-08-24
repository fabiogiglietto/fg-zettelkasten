---
title: "Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks"
aliases: ["Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks"]
authors: ["Giada Marino", "Bruna Paroni", "Fabio Giglietto"]
year: 2026
doi: 10.1080/1369118x.2026.2696929
bibtex_key: Marino2026-he
topics: [political-polarization-and-engagement, election-campaigns-on-social-media]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/1369118x.2026.2696929
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Marino2026-he.mp3
pdf_available: true
discovery_date: 2026-07-22T09:04:51.944484Z
---

# Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks

> Marino, G., Paroni, B., & Giglietto, F. (2026). Measuring partisan community dynamics: a longitudinal analysis of affective engagement in pro-Bolsonaro Facebook networks. *Information, Communication & Society*, 1–20. https://doi.org/10.1080/1369118x.2026.2696929
>
> [View paper](https://doi.org/10.1080/1369118x.2026.2696929)

## Summary

This paper offers a three-year longitudinal study (2021–2023) of affective engagement inside a hyperpartisan pro-Bolsonaro network of Brazilian Facebook groups and pages, analyzing over 12 million posts. Combining LLM-based content classification, time-series volatility detection, and multinomial regression, the authors challenge the assumption that hyperpartisan communities operate as stable, impermeable echo chambers. Instead they find that emotional reactions and interaction patterns were highly unstable and event-sensitive, with a decisive inflection in 2023 around Lula's inauguration and the January coup attempt — marked by declining emotional intensity, rising internal debate, and weakening opposition responses. The study centers the underexamined Brazilian (Global South) case and argues for longitudinal rather than cross-sectional or event-bound approaches to polarized digital engagement.

## Key Contributions

- First systematic long-term longitudinal analysis of affective engagement in pro-Bolsonaro Facebook communities, distinguishing in-group versus out-group responses.
- Introduces two replicable behavioral indices: the Emotional Polarization Index (EPI) and the Engagement Balance Index (EBI), proxying emotional polarization and amplification-versus-discussion dynamics.
- Demonstrates a replicable pipeline combining fine-tuned LLM political-actor classification with longitudinal volatility tracking, validated for Brazilian Portuguese.
- Enriches echo-chamber and affective polarization theory by showing hyperpartisan communities can fracture, adapt, and respond to external pressure over prolonged crisis cycles.
- Extends digital polarization research beyond its predominantly US-centered literature.

## Methods

- Analyzed 12,156,409 Facebook posts from 53 groups and 4 pages of a pro-Bolsonaro network (identified via VeraAI Alerts), collected through CrowdTangle for January 2021–December 2023.
- Built two post-level indices: EPI = (love − angry)/(love + angry) and EBI = (shares − comments)/(shares + comments), each ranging −1 to +1.
- Used rolling 30-day window volatility detection (flagging days where rolling SD exceeded the 95th percentile), identifying 96 volatile days aggregated into 7 instability periods (mean 13.7 days; 1,161,126 posts).
- Fine-tuned GPT-4o on 2,245 manually coded posts for six political-actor categories (multi-label), applied to 712,287 text-containing posts.
- Ran two sets of multinomial logistic regressions (per instability period) predicting tertile-based EPI and EBI categories from five actor-presence indicators, controlling for engagement and reaction volume.

## Findings

- EPI showed extreme boundary clustering (94.3% at ±1) and high volatility; EBI showed 66% boundary clustering; both shifted markedly over time.
- Of 96 volatile days, 15.6% clustered within 15 days of the January 2023 coup attempt, while three earlier major events produced no volatile days.
- The classifier reached 67.7% exact-match accuracy and 0.85 overall F1; Bolsonaro-related entities appeared in 43.2% of posts, Lula-related in 28.2%.
- Bolsonaro-related content drove strong love-dominated engagement in 2021–2022 (β up to 1.193) that collapsed in 2023 (β = 0.220 by December), alongside significant rises in argumentative, comment-dominated engagement.
- Lula references drove angry responses in early periods (β = 0.732 around his sentence annulment) that faded, while love-reaction suppression weakened through 2023 — suggesting incursions by anti-Bolsonaro users (deliberate brigading, not just accidental cross-cutting exposure).
- Armed-forces references showed the most extreme temporal variability, tied to discrete events, while mainstream media unexpectedly drew positive share-dominated engagement in 2023.

## Connections

This paper builds directly on the authors' methodological lineage in coordinated behavior and Facebook network analysis — see [[Giglietto2023-fa71a001]], [[Giglietto2024-cbeb3f70]], [[Giglietto2020-9d8acdd7]], [[Giglietto2020-6278a4aa]], and [[Marino2024-2fbc690f]] — as well as their earlier work on partisan sharing and echo chambers such as [[Giglietto2019-882f1900]] and [[Iannelli2015-e0818c3e]]. Its challenge to the stable-echo-chamber model and its analysis of cross-cutting versus adversarial exposure connect to broader debates on selective exposure and network structure represented by [[Bakshy2015-rn]] and [[Gonzalez-Bailon2024-rq]], while its Global South / Brazilian focus links to work on political communication beyond the US such as [[Inacio-da-Silva2026-zf]] and [[Rossini2026-jn]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Marino2026-he.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
