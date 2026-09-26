---
title: "Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign"
aliases: ["Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign"]
authors: ["Franziska B. Keller", "David Schoch", "Sebastian Stier", "JungHwan Yang"]
year: 2020
doi: 10.1080/10584609.2019.1661888
bibtex_key: Keller2019-nk
topics: [coordinated-inauthentic-behavior, information-operations-disinformation-narratives]
citation_count: 283
open_access: false
source_url: https://doi.org/10.1080/10584609.2019.1661888
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445419Z
---

# Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign

> Keller, F. B., Schoch, D., Stier, S., & Yang, J. (2020). Political Astroturfing on Twitter: How to Coordinate a Disinformation Campaign. *Political Communication*, 1–25. https://doi.org/10.1080/10584609.2019.1661888
>
> [View paper](https://doi.org/10.1080/10584609.2019.1661888)

## Summary

This paper studies **political astroturfing**—centrally coordinated disinformation campaigns whose participants pose as ordinary, independent citizens—using the rare advantage of offline ground-truth data. Court proceedings against South Korea's National Intelligence Service (NIS) exposed a list of 1,008 Twitter accounts operated by state agents to support conservative candidate Geun-hye Park during the 2012 presidential election. The authors argue that astroturfing is best understood as a species of disinformation not because the content is necessarily false, but because it deceives audiences about the *coordinated origin and independence* of participants. Their central methodological move is to shift attention away from bot detection toward **group-level coordination traces**, which they show are a stronger, harder-to-hide signal. Applying principal-agent theory, they explain why any managed campaign leaves near-universal behavioral fingerprints—and why those same frictions also limit its effectiveness.

## Key Contributions

- Empirical characterization of one of the earliest confirmed coordinated political disinformation campaigns, anchored by court-derived ground truth linking specific accounts to their instigator.
- A theoretically grounded, **relational detection method** based on retweet, co-tweet, and co-retweet networks, argued to transfer across cases because principal-agent problems make coordination hard to conceal.
- Reframes disinformation research from bot detection to coordination detection, and broadens the concept of disinformation to include deception about the *coordinated origin* of otherwise-truthful content.
- Measures campaign influence with multiple metrics rather than anecdote, showing limited impact even under favorable conditions.
- Flags a policy/data problem: platform deletion of implicated accounts undermines ex post study of disinformation.

## Methods

The core is a case study of the NIS operation using a 10% Gardenhose Twitter stream (June–December 2012) of 75 million Korean-language tweets, within which 702 of the known NIS accounts posted ~195,000 tweets. The authors derive expectations from **principal-agent theory** (agent shirking, satisficing, direct supervision) about how coordinated campaigns should differ from organic grassroots activity. They construct three message-coordination networks—retweet, co-tweet (identical non-retweet within one minute), and co-retweet—and analyze temporal activity and account-creation timing (via User IDs). A threshold-based iterative detection strategy (a 50% NIS-retweet threshold plus co-tweet/co-retweet components) identifies additional suspect accounts, validated against account status, activity patterns, and content (keyword rank correlations, top retweeted accounts) relative to random-user, political-keyword, and opinion-leader baselines. Impact is assessed via followers, mentions received, and retweets received.

## Findings

- NIS accounts tweeted mostly during office hours and weekdays, dropped on weekends, and stopped abruptly after exposure on December 11, 2012—patterns opposite to regular users.
- Coordination was pervasive: 48% of NIS tweets were retweets; ~45,000 identical non-retweet tweets were co-tweeted (over half within the same second); only 17% of retweets were unique, and co-retweeting involved almost every agent (725 accounts).
- Network structure revealed a division of labor, with cohesive clusters mapping to individual agents and much traffic circulating within the campaign's own network.
- The method surfaced 834 additional unique suspect accounts sharing NIS temporal patterns, creation times/IDs, and content.
- Validation was strong: under 10% of suspects remained active (vs. 40% of a random sample); 96.5% of known NIS accounts were deactivated or suspended.
- Content skewed heavily political and toward hardline North Korea keywords (τ ≈ 0.61–0.66 between NIS and suspects), negatively correlated with regular users and opinion leaders, and dominated by right-wing pundits.
- Despite mutually inflated follower counts, NIS accounts received fewer mentions than ordinary users; ~40% of the retweets they got came from within the campaign, and there was no evidence of shifting the broader agenda.

## Connections

This paper is a foundational reference for the coordination-over-bots view of inauthentic behavior, connecting to detection work that formalizes coordinated network signatures such as [[Nizzoli2020-cf]], [[Luceri2025-tr]], and [[Minici2024-tf]]. Its grounding of disinformation in state information operations and platform manipulation links it to studies of orchestrated campaigns and their effects, including [[Freelon2020-yp]] and [[Starbird2019-qv]], while its skeptical conclusion about limited real-world impact resonates with broader debates on disinformation spread exemplified by [[Vosoughi2018-at]] and [[Lazer2018-mm]].
