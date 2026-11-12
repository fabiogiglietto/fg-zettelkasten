---
title: "“I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing"
aliases: ["“I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing"]
authors: ["Anders Olof Larsson"]
year: 2026
doi: 10.1177/20563051261501463
bibtex_key: Larsson2026-nl
topics: [italian-elections-news-ecosystem, political-polarization-partisanship]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1177/20563051261501463
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Larsson2026-nl.mp3
pdf_available: true
discovery_date: 2026-11-12T22:33:53.932410Z
---

# “I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing

> Larsson, A. O. (2026). “I share your sentiment”—A longitudinal study of Facebook post sentiment and sharing. *Social Media + Society*, *12*. https://doi.org/10.1177/20563051261501463
>
> [View paper](https://doi.org/10.1177/20563051261501463)

## Summary

This paper offers a decade-long (2016–2025) longitudinal analysis of how all nine major Norwegian parliamentary parties deploy negative, positive, and neutral sentiment on Facebook, and how that sentiment relates to how widely posts are shared. Working with a near-complete population of almost 39,000 text posts, Larsson combines open-source LLM classification with human annotation to track both the supply side (party sentiment) and demand side (sharing). The core argument is that while positive sentiment remains dominant, negativity has risen—driven more by challenger status than ideology alone—and that although negative posts generally gain more shares, this advantage erodes over time, suggesting strategic adaptation or audience fatigue.

## Key Contributions

- Rare longitudinal evidence on the "emotional turn" in digital political communication, tracking supply (party sentiment) and demand (sharing) over a full decade.
- A replicable method combining locally run open-source LLMs (Gemma 3, gpt-oss-20b) with human annotation for sentiment classification in a non-English (Norwegian) context.
- Nuances the "dark politics" and populist-negativity literatures by showing that challenger status, not ideology per se, best explains negativity.
- Provides a Northern European multiparty, coalition-based case as a contrast to the US- and election-centric online campaigning literature.

## Methods

Longitudinal, full-population design covering Facebook Page posts from all nine major Norwegian parties across three parliamentary elections (2017, 2021, 2025). Data were collected in January 2026 via the Meta Content Library (successor to CrowdTangle), yielding 38,898 text posts after excluding 614 textless ones. Sentiment was classified via a three-step human-plus-machine approach using the Mall R package: Gemma 3 classification, human coding of a 400-post sample (Krippendorff's α = .82), and reclassification with gpt-oss-20b (inter-LLM α = .78). Binary logistic regression tested whether incumbency predicts negativity; negative binomial regression models (year-by-year and overall) modeled shares as a count outcome, with Cramér's V used for sentiment–party and sentiment–year associations.

## Findings

- Negative posts rose over time, plateauing at just over 35% in the final four years; positive posts remained the largest share (sentiment–year association weak, Cramér's V = .12).
- Incumbents had ~74.5% lower odds of using negative sentiment than challengers (OR = 0.255); predicted probability of negativity was ~16.2% for incumbents versus ~43.1% for challengers.
- The Socialist Left Party posted the most negative content (44%), followed by Red (39.1%), Greens (33.5%), and the far-right Progress Party (31.1%); catch-all parties were least negative—negativity is concentrated among small, often left-wing challengers.
- Negative sentiment drove more shares overall, but this effect weakened after 2021, suggesting a dampening or audience-fatigue effect.
- At the party level, negativity paid off in shares for most parties, but the extreme-end Red and Progress parties gained more shares with *positive* sentiment—a mismatch between their strategy and share-maximizing behavior.

## Connections

This study sits alongside other recent work on affective and negative dynamics in political social media; it resonates with research on the moral-emotional drivers of online sharing (e.g., [[Brady2026-ln]]) and with the broader partisan-animosity and polarization literature it extends beyond the US context ([[Iyengar2019-jj]], [[Osmundsen2021-et]]). As a companion piece by the same author on Nordic online campaigning, [[Larsson2026-ro]] is a direct intellectual neighbor, and its two-step-flow/sharing framing connects to [[Bakshy2015-rn]] on social media diffusion of political content.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Larsson2026-nl.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
