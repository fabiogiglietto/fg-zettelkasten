---
title: "Rabble-rousers in the new king&#x27;s court: Algorithmic effects on account visibility in pre-X twitter"
aliases: ["Rabble-rousers in the new king&#x27;s court: Algorithmic effects on account visibility in pre-X twitter"]
authors: ["Alexandros Efstratiou", "Kayla Duskin", "Kate Starbird", "Emma Spiro"]
year: 2025
doi: 
bibtex_key: Efstratiou2025-gs
topics: [political-polarization-partisanship, platform-critique-anniversary-essays]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2512.06129v2
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Efstratiou2025-gs.mp3
pdf_available: true
discovery_date: 2025-12-15T00:00:00Z
---

# Rabble-rousers in the new king&#x27;s court: Algorithmic effects on account visibility in pre-X twitter

> Efstratiou, A., Duskin, K., Starbird, K., & Spiro, E. (2025). Rabble-rousers in the new king&#x27;s court: Algorithmic effects on account visibility in pre-X twitter. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2512.06129v2)

## Summary

This paper conducts an account-level audit of Twitter's recommendation algorithm during the brief post-acquisition, pre-rebrand window of February 2023. Leveraging a dataset of 806 real US users' simultaneously captured algorithmic ("For You") and reverse-chronological feeds, the authors compare how accounts were exposed across the two feed types. They replicate the widely reported finding that right-leaning accounts received disproportionate algorithmic amplification — but show that this apparent political bias largely evaporates once one controls for three behavioral factors: posting agitating content, receiving interactions from Elon Musk, and verification status. The central argument is that algorithmic curation rewards controversy-stirring and proximity to the platform owner rather than political leaning per se, and that Musk himself became the dominant node in the algorithmic feed. This undermines the "neutral digital town square" framing of the platform.

## Key Contributions

- Provides an **account-level** (rather than tweet-level) analysis of algorithmic amplification, capturing network centralization and platform-owner influence.
- Introduces a **"counterfactual feeds"** design using real users' simultaneous algorithmic and chronological feeds, complementing sockpuppet and randomized-experiment audits.
- Disentangles surface-level political-bias claims by showing right-leaning amplification is mediated by behavioral correlates (agitating content, Musk interaction), not leaning itself.
- Documents the distinct algorithmic treatment of **legacy-verified** versus **Twitter Blue** accounts.
- Develops and validates an LLM-based **"agitating content"** annotation, distinct from toxicity or identity attack.
- Supplies empirical evidence bearing on policy debates (e.g., FTC inquiries) about alleged ideological censorship on platforms.

## Methods

Secondary analysis of a dataset (Milli et al. 2025) of paired algorithmic and chronological feeds from 806 CloudResearch Connect participants, collected Feb 11–27, 2023. The authors built bipartite participant–account networks and computed partisan assortativity, degree centralization, in-degree, and eigenvector centrality. To address the politically skewed sample, they used nearest-neighbor demographic matching (188 left- vs 188 right-leaning participants). Account leaning was inferred from the proportion of right-leaning followers with Wilson binomial confidence intervals and robustness checks. Tweets were annotated by Gemini 2.0 Flash as political (F1 ≈ 0.9) and as agitating (F1 ≈ 0.7). Analyses included robust-standard-error regressions predicting in-degree change, two- and three-way ANOVAs with Tukey HSD, and chi-squared comparisons of follow-based expected versus observed exposure.

## Findings

- The algorithmic feed was far more **centralized** (degree centralization 0.46 vs 0.24) and less partisan-assortative (0.06 vs 0.15) than the chronological feed.
- **Elon Musk** dominated the algorithmic feed: his in-degree nearly doubled (94 → 179) and eigenvector centrality rose from 0.27 to 0.52.
- Algorithmic "winners" were provocateur/influencer accounts; "losers" were mainstream news and official accounts (AP, NYT, BBC, Reuters, WhiteHouse, CNN).
- Right-leaning accounts gained exposure relative to follow-based expectations across Democratic, Independent, and Republican participants alike (all p<0.001).
- **Musk interaction** had the largest standardized effect (d ≈ 0.93), ~3.99 additional exposures per 1000 users.
- Business (p<0.001) and government (p=0.04) verification predicted visibility losses; Twitter Blue showed no significant effect.
- Once controls were added, left-leaning accounts lost visibility relative to neutral (p<0.001) while right-leaning showed no effect (p=0.92).
- **Agitating content predicted gains; political content predicted losses.** Musk disproportionately interacted with right-leaning (99 vs 47.84 expected) and more agitating accounts.

## Connections

This work sits squarely in the algorithmic-auditing and amplification literature on Musk-era Twitter/X, and pairs naturally with network-based studies of platform curation such as [[Bouchaud2026-lr]] and [[Bouchaud2026-np]]. Its critique of engagement-driven perverse incentives and platform-owner centrality connects to broader accountability and collective-behavior arguments in [[Bak-Coleman2026-mk]] and [[Bak-Coleman2025-pm]], while its treatment of partisan news amplification and cross-cutting exposure relates to [[Bakshy2015-rn]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Efstratiou2025-gs.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-rabble-rousers-in-the-new-kings/id1866587707?i=1000743818386)
