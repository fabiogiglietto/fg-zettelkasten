---
title: "“Meet the new boss – Same as the old boss”: A longitudinal study of political post sentiment and Facebook engagement"
aliases: ["“Meet the new boss – Same as the old boss”: A longitudinal study of political post sentiment and Facebook engagement"]
authors: ["Anders Olof Larsson"]
year: 2026
doi: 10.5210/fm.v31i1.14448
bibtex_key: Larsson2026-ro
topics: [llms-computational-content-analysis, political-polarization-partisan-news]
citation_count: 0
open_access: false
source_url: https://doi.org/10.5210/fm.v31i1.14448
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Larsson2026-ro.mp3
pdf_available: true
discovery_date: 2026-01-15T00:00:00Z
---

# “Meet the new boss – Same as the old boss”: A longitudinal study of political post sentiment and Facebook engagement

> Larsson, A. O. (2026). “Meet the new boss – Same as the old boss”: A longitudinal study of political post sentiment and Facebook engagement. *First Monday*. https://doi.org/10.5210/fm.v31i1.14448
>
> [View paper](https://doi.org/10.5210/fm.v31i1.14448)

## Summary

This paper tracks a decade (2013–2023) of Facebook activity from Norway's right-wing populist Progress Party and its two successive leaders, Siv Jensen and Sylvi Listhaug, to examine how the sentiment of political posts relates to audience engagement over time. Larsson uses a hybrid pipeline — GPT-4 zero-shot classification of 11,160 Norwegian-language posts, validated against human coders — to categorize posts as negative, positive, or neutral, then compares shares, comments, and likes across sentiment, account, and year. The central argument is twofold: negativity in populist Facebook content has grown (especially after Listhaug's 2021 takeover) and reliably amplifies shares and comments, while likes follow a different, more positivity-driven logic. The title's nod to "the new boss" captures the finding that leadership transitions reshape party-level communication style toward greater negativity.

## Key Contributions

- A rare 10-year longitudinal account of populist Facebook communication outside the Anglo-American context.
- A reproducible hybrid LLM + human coding workflow for sentiment annotation in Norwegian, with strong reliability (α = .91 intracoder, .82 intercoder).
- Empirical disaggregation of engagement types, showing likes diverge from shares and comments in their relation to sentiment.
- Integration of supply-side (party/leader production) and demand-side (audience engagement) analyses in one design.
- Evidence bearing on negative campaigning, permanent campaigning, and political professionalization debates.

## Methods

CrowdTangle was used to harvest 11,160 public posts from the Progress Party page and the personal pages of Jensen and Listhaug (2013–2023). Each post was classified as negative/positive/neutral campaigning by GPT-4 (gpt-4-0314) using a Norwegian-language zero-shot prompt; reliability was tested by re-running the LLM on a 20% sample and by independent human coding of a 5% sample. Engagement (shares, comments, likes) was analyzed with medians, Kruskal-Wallis, and Dunn's tests due to non-normal distributions, accompanied by visual breakdowns across account, sentiment, and year.

## Findings

- Negative content rose markedly over the decade, with Listhaug shifting toward negativity from 2017 and the party page following after her 2021 ascension.
- Negative posts produced the highest median shares across nearly all accounts and years (H2a confirmed).
- Negative posts also produced more comments, with 2021 (election year) as a notable exception (H2b largely confirmed).
- Likes diverged: positive posts dominated likes for Jensen (2020–2023) and Listhaug (2021–2022), suggesting "lightweight" engagement obeys a different affective logic.
- Election years no longer produced clear engagement surges, consistent with a shift toward permanent campaigning.
- Posting volume mirrored leadership status: Listhaug ramped up after 2021, Jensen wound down.

## Connections

This paper sits naturally alongside other work using LLMs as annotation instruments for political and media content — particularly [[Balluff2026-if]] and [[Le-Mens2025-qz]] on validating LLM-based text classification, and [[Tornberg2025-ir]] / [[Tornberg2026-lc]] on LLMs in political and social analysis. Its non-English (Norwegian) application speaks to multilingual evaluation concerns raised in [[Nguyen2026-vm]]. Substantively, the focus on populist negativity and platform dynamics resonates with [[DeVerna2025-dl]] on social media political content, though most other papers in this register address LLM capabilities rather than political communication directly.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Larsson2026-ro.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-meet-the-new-boss-same-as-the-old/id1866587707?i=1000744605209)
