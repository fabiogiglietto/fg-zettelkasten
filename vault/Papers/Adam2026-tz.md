---
title: "How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic"
aliases: ["How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic"]
authors: ["Silke Adam", "Tobias Rohrbach", "Franziska Keller", "Mykola Makhortykh", "Ernesto de León", "Chiara Valli", "Ani Baghumyan", "Maryna Sydorova"]
year: 2026
doi: 10.1093/joc/jqaf033
bibtex_key: Adam2026-tz
topics: [information-disorder, health-information-online]
citation_count: 4
open_access: false
source_url: https://doi.org/10.1093/joc/jqaf033
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Adam2026-tz.mp3
pdf_available: true
discovery_date: 2026-05-16T09:10:27.779284Z
---

# How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic

> Adam, S., Rohrbach, T., Keller, F., Makhortykh, M., de León, E., Valli, C., Baghumyan, A., & Sydorova, M. (2026). How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic. *Journal of Communication*, *76*, 119–133. https://doi.org/10.1093/joc/jqaf033
>
> [View paper](https://doi.org/10.1093/joc/jqaf033)

## Summary

This study combines a two-wave panel survey (Germany and German-speaking Switzerland, March–May 2020) with browser-level web tracking to ask how media exposure and political predispositions jointly shaped emerging COVID-19 conspiracy beliefs at the pandemic's outset. Using BERT classifiers to identify conspiracy-related sentences and their stance (supporting vs. opposing) across 3.5 million tracked documents, the authors test a holistic model integrating alternative media, mainstream media, populism, and political mistrust. They find both direct contagion (from conspiracy-supporting alternative media) and direct mitigation (from conspiracy-opposing mainstream media), but also indirect reinforcement via selective engagement and a backfire pathway in which mainstream debunking *increases* conspiracy belief among populists.

## Key Contributions

- One of the first behaviorally-tracked, real-time studies of conspiracy belief formation during an unfolding global crisis, sidestepping retrospective self-report bias.
- A holistic model marrying Zaller-style information-plus-predispositions theory with selective exposure and motivated reasoning, operationalized at the level of both source and content stance.
- Empirical evidence that mainstream debunking works on average but backfires among populists — clarifying when correction succeeds or fails.
- Released methodological infrastructure: the WebTrack browser plugin and fine-tuned German BERT classifiers for conspiracy detection and stance.
- Demonstrates that even mainstream quality outlets carried substantial conspiracy-supporting content during the early pandemic.

## Methods

Two-wave online panel (N≈1,147) with quota sampling, bracketing a desktop web-tracking phase via a custom Chrome/Firefox plugin capturing full HTML. Sentence-level conspiracy detection and stance classification used fine-tuned German BERT models trained on 12,745 manually coded sentences (α ≥ .80), validated on a 498-sentence gold standard (macro F1 = 0.94 for detection; 0.78–0.82 for stance). URLs were mapped to mainstream quality/tabloid, hyperpartisan alternative conspiracy (HAC), and social media sources. OLS regression and bootstrapped mediation (10,000 iterations) tested direct and indirect effects of populism and political mistrust on T2 conspiracy beliefs through stance-specific exposure.

## Findings

- 7.2% of visited documents on average contained conspiracy-related content (~113 per participant over the tracking window).
- Conspiracy-supporting content outweighed opposing content across all media types, including mainstream outlets.
- Exposure across source types was positively correlated — users encountered conspiracy content across multiple channels rather than via clean single-source filter bubbles.
- **Contagion**: conspiracy-supporting alternative media exposure raised conspiracy beliefs (b=0.14, p<.001).
- **Mitigation**: conspiracy-opposing mainstream media exposure lowered conspiracy beliefs (b=−0.05, p=.001).
- Populism (b=0.38) and political mistrust (b=0.20) directly predicted conspiracy beliefs.
- Populists selectively engaged with supporting alternative media (b=0.76) and avoided opposing mainstream media (b=−0.91); mistrust effects were weaker.
- Significant indirect reinforcement effect via alternative media for both predispositions.
- Backfire pathway: among populists, the mainstream exposure they did receive *increased* rather than reduced conspiracy beliefs.
- 25–30% of respondents saw at least some truth in COVID-19 conspiracies or were uncertain.

## Connections

This paper sits at the intersection of misinformation-correction work and behavioral exposure measurement, complementing platform- and tracking-based studies of misinformation diets such as [[Gonzalez-Bailon2024-rq]] and [[Budak2024-ef]], and the cross-national exposure perspective in [[Humprecht2025-ml]]. Its findings on populism-driven selective exposure and backfire connect to inoculation and correction debates explored in [[van-der-Linden2026-jt]] and [[Spampatti2026-kx]], while its account of alternative-media contagion resonates with work on hyperpartisan and conspiratorial ecosystems like [[Frischlich2025-vn]] and [[Rohrbach2026-rc]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Adam2026-tz.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-debunking-backfires-how-covid/id1866587707?i=1000768904634)
