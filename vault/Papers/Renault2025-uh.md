---
title: "Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"
aliases: ["Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes"]
authors: ["Thomas Renault", "Mohsen Mosleh", "David Gertler Rand"]
year: 2025
doi: 10.31234/osf.io/vk5yj_v3
bibtex_key: Renault2025-uh
topics: [information-disorder-misinformation, political-communication-elections]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31234/osf.io/vk5yj_v3
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes

> Renault, T., Mosleh, M., & Rand, D. G. (2025). Republicans are flagged more often than Democrats for sharing misinformation on X’s Community Notes. *Proc. Natl. Acad. Sci. U. S. A.*, *122*. https://doi.org/10.31234/osf.io/vk5yj_v3
>
> [View paper](https://doi.org/10.31234/osf.io/vk5yj_v3)

## Summary

This brief report uses X's Community Notes program as a natural test of whether the well-documented partisan asymmetry in online misinformation sharing survives when content is evaluated by a crowdsourced bridging algorithm rather than professional fact-checkers. Analyzing 218,382 Community Notes written between January 2023 and June 2024, the authors find that posts by Republicans are flagged as misleading 2.3 times more often than posts by Democrats among notes rated "helpful" — a status the bridging algorithm awards only when politically diverse users agree. Because that mechanism requires cross-partisan consensus, the finding directly undercuts the argument advanced by Musk and Zuckerberg that professional fact-checking is biased against conservatives and that community-based moderation would eliminate the differential sanctioning of Republicans.

## Key Contributions

- Demonstrates that partisan asymmetry in misinformation sharing persists under a crowdsourced, bridging-algorithm evaluation system, not merely under professional fact-checking.
- Directly rebuts the political/policy claim that fact-checker bias explains the Republican skew, by removing fact-checkers from the loop.
- Extends prior domain-quality or URL-based approaches to evaluate specific claims at the tweet level.
- Introduces a triangulated partisanship-inference method combining two follower-based scores with an LLM-based tiebreaker.
- Documents topical variation in the asymmetry, with Health misinformation showing the largest Republican skew.
- Releases replication code and a dehydrated tweet dataset.

## Methods

The authors analyze the full open-source Community Notes dataset (English notes on English tweets, Jan 2023–Jun 2024), yielding 218,382 notes on 162,228 tweets from 39,140 users. User partisanship is inferred by triangulating three approaches — a follower-based partisan score, Bayesian ideal-point estimation, and GPT-4o mini classification of users' recent tweets — retaining users only where at least two methods agree. The bridging algorithm's "helpful" status serves as a proxy for a tweet being genuinely misleading, and logistic regression predicts this status from poster partisanship while controlling for verification, follower count, tweet volume, and topic (classified into Politics, Science, Health, Economy, Other). A separate sample of 474,394 random tweets containing "the" is used to estimate the platform's underlying partisan composition.

## Findings

- 60.05% of proposed notes targeted Republican posts vs. 39.95% Democratic.
- Notes on Republican tweets reached "helpful" status more often (10.41% vs. 6.78%); being Republican raised the odds of a helpful note by 63.49% in regression.
- Among 19,569 helpful notes, 69.79% targeted Republicans vs. 30.21% Democrats — a 2.3:1 ratio.
- The asymmetry is robust to either follower-based partisanship method alone (1.7x and 2.1x).
- Republican overrepresentation is largest for Health (81.9%), then Politics (73.3%), Science (68.8%), Other (66.9%), and Economy (63.7%).
- Democrats still post more than Republicans in a random sample, ruling out a base-rate explanation (though the Republican share has grown since Musk's acquisition).

## Connections

This paper builds directly on the partisan-asymmetry literature exemplified by [[Mosleh2024-op]] and [[Gonzalez-Bailon2024-rq]], reframing that debate around crowdsourced rather than professional evaluation. Its focus on Community Notes and bridging-based moderation connects it to work on the effectiveness and biases of crowd-based fact-checking such as [[Pierri2025-hm]] and [[Allcott2025-jb]], and to broader studies of platform moderation and misinformation dynamics like [[DeVerna2025-dl]].
