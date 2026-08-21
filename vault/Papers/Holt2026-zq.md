---
title: "What Facebook users flag as false news: A mixed-methods investigation of user-reported links"
aliases: ["What Facebook users flag as false news: A mixed-methods investigation of user-reported links"]
authors: ["Anton Elias Holt"]
year: 2026
doi: 10.1080/21670811.2026.2703607
bibtex_key: Holt2026-zq
topics: [platform-data-access-and-governance, health-misinformation-and-fact-checking]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/21670811.2026.2703607
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Holt2026-zq.mp3
pdf_available: true
discovery_date: 2026-08-20T12:21:52.011920Z
---

# What Facebook users flag as false news: A mixed-methods investigation of user-reported links

> Holt, A. E. (2026). What Facebook users flag as false news: A mixed-methods investigation of user-reported links. *Digital Journalism*, 1–19. https://doi.org/10.1080/21670811.2026.2703607
>
> [View paper](https://doi.org/10.1080/21670811.2026.2703607)

## Summary

This paper investigates what kinds of links Facebook users have historically flagged as "False News," using the question to probe the wisdom of Meta's January 2025 decision to abandon third-party fact-checking in the US in favor of Community Notes and greater reliance on user reports. Drawing on the Meta-created URL Shares dataset, the author compares three samples — user-reported links, links fact-checked as false, and a matched control of unreported/unchecked links — through a mixed-methods design blending NLP, statistics, and qualitative close reading. The central argument is that user reporting behaves less like reliable misinformation detection and more like a "narrow statement of objection": users disproportionately flag polarized political content that contextualizes controversy rather than content that is demonstrably false.

## Key Contributions

- Empirical, URL-level content analysis of what users actually report as false, moving beyond the largely theoretical, experimental, or qualitative prior literature.
- Direct engagement with Meta's 2025 shift toward user-report-driven moderation and Community Notes, supplying evidence relevant to that policy debate.
- A methodological approach treating user reports as a platform-intrinsic signal of "problematic" content within the URL Shares dataset — data previously used only to validate simulated models.
- Non-US-centric evidence via the Brazil case and a controlled mainstream-media comparison via the BBC case.
- Extension of demographic engagement research (notably age effects) to user-reported content specifically.

## Methods

The study uses the Meta URL Shares dataset (URLs shared publicly >100 times, Jan 2017–Nov 2022), filtering differentially-private noisy cells to retain statistically certain interactions (alpha < 0.001). Three samples are built: a Reported Sample (110,224 URLs with 20+ real reports), a Misinformation Sample (28,271 fact-checked-false URLs), and a Control Sample (200,000 unreported/unchecked URLs matched by top-share country). Multilingual texts were translated to English via NLLB-200-3B inside the FORT environment, with language detection triangulated. Analysis combined frequency statistics and Rank Difference Scores (Kessler 2017) with qualitative thematic reading, two critical case studies (2018 Brazil election, BBC.com/news), and interaction-pattern heatmaps normalized per view by age group.

## Findings

- In the 2018 Brazil case, user-reported URLs outnumbered fact-checked false URLs 71:1 (1,568 vs. 22) — high scale, weak precision.
- Reported Brazil links overwhelmingly concerned the two candidates (994 mentioning Bolsonaro, 462 Haddad), electoral fraud claims, WhatsApp smear campaigns, and the contested "gay kit" story — often contextualizing rather than asserting falsehoods.
- Contradictory reported links appeared on the same contested topic (some claiming the "gay kit" was real, others false), indicating politically motivated flagging.
- BBC reported links (239) had a narrower, more political, more negative and sensational focus (Trump, Covid-19, vaccines, Kashmir) than the diverse, neutral, "evergreen" control links (301).
- The Reported and Misinformation samples overlapped only modestly (12.2% of Misinformation, 3.1% of Reported), so reports are not a subset of fact-checked content.
- Older users engaged more heavily with reported URLs (likes, comments, shares-without-clicks, angry reactions); the youngest groups clicked control links more.
- Elevated angry reactions and shares-without-clicks on reported content signal its more political, contested, partisan character.

## Connections

This paper is grounded in the same Meta URL Shares dataset used by [[Allen2025-ot]] for estimating misinformation exposure, and its skepticism about crowd-sourced flagging speaks directly to work evaluating Community Notes and crowd fact-checking such as [[DeVerna2025-dl]] and [[Pierri2025-hm]]. It also fits the broader debate over post-2025 platform moderation and fact-checking regimes explored in [[Cazzamatta2026-lo]] and [[Schulte2026-df]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Holt2026-zq.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
