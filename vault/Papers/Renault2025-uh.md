---
title: "Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"
aliases: ["Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"]
authors: ["Thomas Renault", "Mohsen Mosleh", "David Gertler Rand"]
year: 2025
doi: 10.31234/osf.io/vk5yj_v1
bibtex_key: Renault2025-uh
topics: [information-disorder, platform-governance-apis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31234/osf.io/vk5yj_v1
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes

> Renault, T., Mosleh, M., & Rand, D. G. (2025). Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes. *Proc. Natl. Acad. Sci. U. S. A.*, *122*. https://doi.org/10.31234/osf.io/vk5yj_v1
>
> [View paper](https://doi.org/10.31234/osf.io/vk5yj_v1)

## Summary

This brief report tests whether the well-documented partisan asymmetry in online misinformation sharing — Republicans being flagged more often than Democrats — survives when content moderation shifts from professional fact-checkers to a crowdsourced bridging algorithm. Using 218,382 Community Notes from X between January 2023 and June 2024, the authors show that Republican posts are flagged as misleading 2.3 times more often than Democratic posts among notes that achieved "helpful" status (which requires cross-partisan agreement). They argue this directly undercuts the rationale offered by Musk and Zuckerberg for replacing professional fact-checking with community-based systems on the grounds that fact-checkers are biased against conservatives.

## Key Contributions

- Demonstrates that partisan asymmetry in misinformation flagging persists under a crowdsourced, bridging-algorithm system that structurally requires agreement across ideologically diverse raters.
- Provides a direct empirical response to the political claim that fact-checking bias explains differential sanctioning of Republicans.
- Moves beyond domain-level link quality measures to tweet-level claim evaluation.
- Introduces a triangulated partisanship-inference method combining two follower-based estimators with an LLM-based tiebreaker.
- Maps topical variation in the asymmetry, identifying Health misinformation as showing the largest Republican skew.

## Methods

The authors analyze the full open-source Community Notes corpus (Jan 2023–Jun 2024), restricted to English notes on English tweets, yielding 218,382 notes on 162,228 tweets from 39,140 users. User partisanship is inferred by requiring agreement among at least two of three methods: Mosleh & Rand's follower-based score, Barberá's Bayesian ideal-point estimation, and GPT-4o mini classification of recent tweets. Logistic regression predicts "helpful" status from poster partisanship, controlling for verification, follower count, tweet volume, and topic (classified via Chuai et al. 2024). A base-rate sample of 474,394 random English tweets from X's Pro API benchmarks the partisan composition of the platform.

## Findings

- 60.05% of proposed notes targeted Republican posts versus 39.95% for Democratic posts.
- Notes on Republican tweets reached "helpful" status at higher rates (10.41% vs. 6.78%); regression shows a 63.49% increase in odds of helpful status for Republican-authored tweets.
- Among 19,569 helpful notes, 69.79% targeted Republicans and 30.21% targeted Democrats — a 2.3:1 ratio.
- The asymmetry is robust to using either follower-based partisanship method alone (1.7x and 2.1x).
- Topic-level Republican shares of flagged misinformation: Health 81.9%, Politics 73.3%, Science 68.8%, Other 66.9%, Economy 63.7%.
- Democrats still post more than Republicans in a random tweet sample, ruling out a base-rate explanation, though the Republican share has grown post-acquisition.

## Connections

This paper sits squarely within the empirical literature on partisan asymmetries in misinformation exposure and sharing, most directly extending [[Mosleh2024-op]] and [[Gonzalez-Bailon2024-rq]] by showing the asymmetry holds under a crowdsourced rather than expert-driven evaluation regime. It also speaks to broader debates over platform moderation regimes and fact-checking infrastructure raised by [[Budak2024-ef]], and complements work on the dynamics and limitations of Community Notes-style bridging systems relevant to [[Bollenbacher2026-vz]].
