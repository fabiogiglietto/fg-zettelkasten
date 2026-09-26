---
title: "Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?"
aliases: ["Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?"]
authors: ["Pablo Barberá", "John Jost", "Jonathan Nagler", "Joshua Tucker", "Richard Bonneau"]
year: 2015
doi: 10.7910/dvn/f9ichh
bibtex_key: Barbera2015-fw
topics: [political-polarization-partisanship, election-campaigns-social-media]
citation_count: 1
open_access: true
source_url: https://doi.org/10.7910/dvn/f9ichh
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445453Z
---

# Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?

> Barberá, P., Jost, J., Nagler, J., Tucker, J., & Bonneau, R. (2015). Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?. *Harvard Dataverse*, *26*, 1531–1542. https://doi.org/10.7910/dvn/f9ichh
>
> [View paper](https://doi.org/10.7910/dvn/f9ichh)

## Summary

This paper asks whether online political communication on Twitter operates as an ideological "echo chamber" or something closer to a "national conversation" that crosses partisan lines. Drawing on nearly 150 million tweets across 12 political and nonpolitical events from 2012–2014, the authors estimate the ideological positions of 3.8 million Twitter users from their follower networks and analyze how retweeting patterns vary by topic and over time. Their central argument is that online ideological segregation is not a fixed property of social media but is highly contingent: political issues produce echo-chamber-like homophily, while many nonpolitical events cut across ideological lines. They further document a persistent asymmetry — liberals engage in more cross-ideological sharing than conservatives.

## Key Contributions

- A scalable, **text-free method** for estimating individual ideology from network follow structure, using correspondence analysis as a tractable approximation to Bayesian latent-space models across millions of users.
- Large-scale behavioral evidence that online ideological segregation is **topic- and time-contingent**, challenging blanket echo-chamber characterizations.
- Documentation of a robust **ideological asymmetry** in cross-cutting dissemination favoring liberals, tied to psychological theories of ideological difference.
- Demonstration of the value of unobtrusive "big data" from naturally occurring settings, avoiding the self-selected partisan samples of prior work; data and materials shared openly.

## Methods

The authors built a latent ideological space from users following at least 10 of an initial set of political accounts (president, parties, members of Congress), expanded it with accounts popular among liberals and conservatives, and projected all users onto a standardized scale. They collected ~150 million tweets via the Streaming API using topic-specific keyword lists for 12 events (e.g., the 2012 election, government shutdown, marriage equality, Boston Marathon bombing, Super Bowl, Winter Olympics), filtering out bots and inactive accounts. Retweeting behavior was analyzed with three polarization metrics — share of same-ideology retweets, ideological homogeneity of detected retweet communities, and average extremity of retweeted content — and Poisson regression tested for liberal–conservative asymmetry. Ideology estimates were validated against statewide survey ideology (r = .87), roll-call ideal points (r = .95), and matched voter registration (78% correct classification).

## Findings

- Political topics (2012 election, government shutdown, State of the Union) showed strong retweeting homophily; e.g., 38% of election retweets occurred among extreme conservatives and 28% among extreme liberals, though each group was only 16% of the sample.
- Nonpolitical topics (Boston Marathon bombing, Super Bowl, Winter Olympics) crossed ideological boundaries with low homophily and heterogeneous clusters.
- The Newtown shooting shifted from national conversation to echo chamber as discussion moved from tragedy to gun-control policy; Syria showed the reverse trajectory.
- Highly polarized topics drew their most-shared content from ideologically extreme authors; nonpolitical content was more often retweeted from moderate sources.
- Across all political topics, liberals were significantly more likely than conservatives to retweet across ideological lines; the asymmetry was smaller and sometimes non-significant for nonpolitical topics.

## Connections

This is a foundational computational contribution to the echo-chamber debate, and its network-based ideology estimation method extends the same authors' earlier follower-network work, closely related to [[Barbera2015-je]]. Its topic-contingent, "more than an echo chamber" thesis speaks directly to work qualifying echo-chamber and selective-exposure claims such as [[Bakshy2015-rn]], [[Guess2020-rr]], [[Flaxman2016-lm]], and [[Del-Vicario2016-uj]], and to the recent large-scale platform studies [[Gonzalez-Bailon2023-uy]] and [[Nyhan2023-gb]]. The documented liberal–conservative asymmetry connects to research on partisan sharing dynamics including [[Osmundsen2021-et]], [[Bail2018-fk]], and [[Freelon2020-yp]], as well as broader accounts of affective polarization like [[Iyengar2019-jj]].
