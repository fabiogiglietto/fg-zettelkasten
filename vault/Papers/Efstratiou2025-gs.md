---
title: "Rabble-rousers in the new king&#x27;s court: Algorithmic effects on account visibility in pre-X twitter"
aliases: ["Rabble-rousers in the new king&#x27;s court: Algorithmic effects on account visibility in pre-X twitter"]
authors: ["Alexandros Efstratiou", "Kayla Duskin", "Kate Starbird", "Emma Spiro"]
year: 2025
doi: 
bibtex_key: Efstratiou2025-gs
topics: [platform-governance-data-access, political-polarization-partisan-news]
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

This paper audits Twitter's "For You" recommendation algorithm during a narrow but pivotal window in February 2023 — after Musk's acquisition but before the X rebrand — by comparing the algorithmic and reverse-chronological feeds that 806 real users saw simultaneously. The headline finding is that while right-leaning accounts did receive disproportionate algorithmic exposure (replicating prior audits), this apparent ideological bias largely dissolves once one controls for three behavioral factors: posting agitating content, being engaged with by Elon Musk, and verification type. The algorithmic feed was also far more centralized than the chronological one, with Musk himself emerging as the dominant node, and legacy-verified institutional accounts (mainstream news, government) systematically losing visibility. The authors argue that the algorithm rewards controversy-stirring and proximity to the platform owner, undermining "neutral town square" framings of X.

## Key Contributions

- Shifts algorithmic auditing from tweet-level to **account-level** analysis, surfacing network centralization and platform-owner influence effects that tweet-level studies miss.
- Introduces a **counterfactual-feeds design** leveraging real users' paired algorithmic and chronological timelines, an alternative to sockpuppet audits.
- **Mediates the "right-wing amplification" claim**: shows the effect is largely explained by agitating content and Musk interactions rather than political leaning per se.
- Distinguishes algorithmic treatment of **legacy verification vs. Twitter Blue**, illuminating monetization-era incentive shifts.
- Develops and validates an **LLM-based "agitating content" classifier** that captures conflict-stirring rhetoric distinct from toxicity or identity attack.

## Methods

Secondary analysis of Milli et al. (2025)'s dataset of paired algorithmic/chronological feeds from 806 US users (Feb 11–27, 2023). The authors build bipartite participant-account networks, match left- and right-leaning participants on demographics (n=188 per side), and classify account leanings via follower composition with Wilson confidence intervals. Network statistics include bipartite degree centralization, assortativity, and eigenvector centrality. Regressions with robust SEs predict change in in-degree between feeds from verification, leaning, Musk interaction, posting style, and media types. Tweets are annotated by Gemini 2.0 Flash as political (validated against human labels) and as agitating (custom category, F1 ≈0.7). ANOVAs and chi-squared tests probe interactions and follower-based exposure expectations.

## Findings

- Algorithmic feed centralization was roughly double the chronological feed's (0.46 vs 0.24); partisan assortativity dropped (0.06 vs 0.15).
- Musk's in-degree nearly doubled (94 → 179) and his eigenvector centrality rose from 0.27 to 0.52 — he is the principal driver of centralization.
- Algorithmic "winners" were provocateur/influencer accounts (hodgetwins, stillgray, JackPosobiec, catturd2); "losers" were mainstream news and official handles (AP, NYT, BBC, WhiteHouse, CNN).
- Right-leaning accounts gained exposure relative to follow-based expectations across Democratic, Independent, *and* Republican participants (all p<0.001).
- **Musk interaction** was the largest predictor of visibility gain (d ≈0.93; ~4 extra exposures per 1000 users).
- Legacy business (p<0.001) and government (p=0.04) verification predicted losses; Twitter Blue conferred no significant effect.
- Once controls were added, left-leaning accounts lost visibility (p<0.001) while right-leaning showed no independent effect (p=0.92).
- Agitating content was rewarded; political content (net of agitation) was penalized; external links, GIFs, and photos were penalized but videos were not.
- Musk disproportionately engaged right-leaning accounts (99 observed vs 47.84 expected) and more agitating accounts overall.
- Right-leaning accounts — especially Twitter Blue ones — posted more agitating content than left-leaning or neutral accounts, while political-content rates were similar across leanings.

## Connections

This sits squarely in the recent wave of post-acquisition X audits and complements [[Bouchaud2026-lr]] and [[Murtfeldt2025-wu]] on algorithmic amplification dynamics, while extending the counterfactual-feeds approach pioneered in work like [[Bakshy2015-rn]]. Its account-level centralization findings on Musk speak to platform-owner influence themes in [[Rieder2025-ju]] and [[Bak-Coleman2025-pm]], and the disentangling of ideological from behavioral amplification connects to [[Mosleh2024-op]] on partisan asymmetries and to broader engagement-incentive critiques in [[Munger2025-cz]]. The trust-and-safety/governance angle resonates with [[Starbird2025-jj]] and [[Donovan2025-ws]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Efstratiou2025-gs.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-rabble-rousers-in-the-new-kings/id1866587707?i=1000743818386)
