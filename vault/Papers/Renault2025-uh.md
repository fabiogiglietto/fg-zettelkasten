---
title: "Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"
aliases: ["Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"]
authors: ["Thomas Renault", "Mohsen Mosleh", "David Gertler Rand"]
year: 2025
doi: 10.31234/osf.io/vk5yj_v1
bibtex_key: Renault2025-uh
topics: [information-disorder-disinformation, platform-governance-content-curation]
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

This brief report tests whether the well-documented partisan asymmetry in online misinformation sharing survives when content is evaluated by a crowdsourced, cross-partisan bridging system rather than professional fact-checkers. Analyzing 218,382 Community Notes written on X between January 2023 and June 2024, the authors find that posts by Republicans are flagged as misleading about 2.3 times more often than posts by Democrats among notes that reached "helpful" status. Because the Community Notes bridging algorithm requires agreement across users of differing viewpoints, the authors argue that the asymmetry cannot be dismissed as liberal bias among fact-checkers — directly undercutting the rationale offered by Musk and Zuckerberg for replacing professional fact-checking with community moderation.

## Key Contributions

- Demonstrates that partisan asymmetry in misinformation sharing persists under a crowdsourced bridging-algorithm system, not only under professional fact-checking.
- Rebuts the "fact-checkers are biased against conservatives" argument by showing the pattern holds when fact-checkers are removed from the evaluation loop.
- Extends prior work from domain-level quality scores and URL-containing posts to evaluation of specific claims at the tweet level.
- Introduces a triangulated approach to inferring user partisanship (two follower-based methods plus an LLM tiebreaker).
- Documents topical variation, with Health misinformation showing the largest Republican skew.
- Releases code and a dehydrated tweet dataset for replication.

## Methods

The authors analyze the full open-source Community Notes dataset (English notes on English tweets, Jan 2023–Jun 2024), yielding 218,382 notes across 162,228 tweets from 39,140 users. User partisanship is inferred by triangulating a follower-based partisan score, Bayesian ideal-point estimation, and GPT-4o mini classification of recent tweets, retaining users where at least two methods agree. A note's "helpful" status (as determined by the bridging algorithm) serves as a proxy for genuine misleadingness. Logistic regression predicts helpful status from poster partisanship, controlling for verification, follower count, tweet volume, and topic (classified into Politics, Science, Health, Economy, Other). A base-rate check samples 474,394 random English tweets to estimate the platform's partisan composition.

## Findings

- 60.05% of proposed notes targeted Republican posts vs. 39.95% Democratic.
- Notes on Republican tweets reached "helpful" status more often (10.41% vs. 6.78%); being Republican raised the odds of a note being rated helpful by 63.49%.
- Among 19,569 helpful notes, 69.79% targeted Republican posts vs. 30.21% Democratic — a 2.3:1 ratio.
- Robust to each partisanship-inference method alone (1.7x and 2.1x).
- Republican overrepresentation is largest for Health (81.9%), then Politics (73.3%), Science (68.8%), Other (66.9%), and Economy (63.7%).
- Democrats still post more than Republicans in a random sample, ruling out a base-rate explanation.

## Connections

This paper builds directly on work documenting partisan differences in the diffusion and quality of shared news, including [[Mosleh2024-op]] and [[Gonzalez-Bailon2024-rq]]. It complements crowdsourced-moderation and Community Notes research such as [[DeVerna2025-dl]] and [[Allen2025-ot]], and speaks to broader debates over platform content moderation policy engaged by [[Copland2025-em]].
