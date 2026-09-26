---
title: "Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data"
aliases: ["Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data"]
authors: ["Pablo Barberá"]
year: 2015
doi: 10.1093/pan/mpu011
bibtex_key: Barbera2015-je
topics: [political-polarization-partisanship, election-campaigns-social-media]
citation_count: 634
open_access: false
source_url: https://doi.org/10.1093/pan/mpu011
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445423Z
---

# Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data

> Barberá, P. (2015). Birds of the Same Feather Tweet Together: Bayesian Ideal Point Estimation Using Twitter Data. *Political Analysis*, *23*, 76–91. https://doi.org/10.1093/pan/mpu011
>
> [View paper](https://doi.org/10.1093/pan/mpu011)

## Summary

Barberá introduces a Bayesian Spatial Following model that recovers ideological positions (ideal points) for both political elites and ordinary citizens from the structure of Twitter following networks. The core intuition is homophilic: people preferentially follow accounts whose politics they share, so the decision to follow a political account functions as a costly signal about one's latent ideology — analogous to a legislator's roll-call vote or a donor's campaign contribution. By modeling follow probability as a function of latent ideological distance, the method scales hundreds of thousands of users onto a common continuous dimension with standard errors, requiring no roll-call, survey, or contribution data. Validated across the US and five European countries and applied to the 2012 US presidential campaign, the paper offers a scalable, low-cost, cross-national measure of ideology and revisits the echo-chamber debate with an unusually large sample.

## Key Contributions

- A novel, scalable Bayesian ideal-point method placing elites and citizens on the same continuous scale with uncertainty estimates.
- Ideology measurement that needs no roll-call, expert-survey, or contribution data, and can be produced at arbitrary time points and across many polities — overcoming static-measurement, bridging, and self-selection limitations.
- Cross-national validation in six countries with differing party-system complexity.
- A fine-grained, low-cost covariate for studying political behavior, and a re-examination of the echo-chamber/polarization debate with a far larger, more precise sample.
- Open replication data and tooling (Stan code, the `streamR` package), plus proposed extensions to dynamic and cross-country bridging estimation.

## Methods

The model treats the probability that user *i* follows political account *j* as a logit function of squared Euclidean distance between their latent ideological positions, adjusted for account popularity (α) and user political interest (β), within a hierarchical multilevel framework. Identification is handled by fixing means/variances and setting left/right starting values to resolve additive, scaling, and reflection invariance. Estimation proceeds in two MCMC stages: a No-U-Turn Hamiltonian sampler in Stan estimates elite parameters on a 10,000-user subsample, then a parallelizable random-walk Metropolis–Hastings sampler in R estimates individual positions. Follower data were collected via the Twitter REST and Streaming APIs for 118–318 political accounts per country, yielding analytic samples from ~49,000 (Germany) to ~301,537 (US). Estimates were validated against DW-NOMINATE/IRT roll-call scores, the Chapel Hill Expert Survey, Lax & Phillips state opinion, Bonica contribution ideal points, and Ohio voter-registration records. The application analyzed ~65 million Obama/Romney tweets from the 2012 campaign.

## Findings

- Twitter ideal points correlate strongly with DW-NOMINATE (ρ = 0.941 House, 0.954 Senate; within-party ρ = 0.546 Republicans, 0.610 Democrats).
- Non-partisan actors (e.g., Limbaugh, Beck; Moore, Maddow) are placed with high face validity.
- European party estimates broadly reproduce Chapel Hill left-right orderings, though accuracy varies (weakest in the UK; extreme parties pulled toward center) as a single dimension compresses multidimensional policy spaces.
- Mass-public estimates reproduce known patterns: bimodal distributions, elites more polarized than voters, and correctly ordered self-identified liberals, moderates, and conservatives.
- State median ideal points correlate more strongly with survey liberal opinion (ρ = 0.876) than with Obama's vote share (ρ = 0.785), suggesting the dimension captures ideology, not mere partisanship.
- Individual-level validation is strong: 90% of users right of the median donated to Republicans, 98% left of the median to Democrats (ρ = 0.80 with contribution ideal points).
- In 2012, tweet volume was bimodal (modes near ±1); conservatives were more active (118 vs 82 tweets) and 85% of retweets were between ideologically similar users, confirming echo-chamber structure, with polarization strongest among conservatives.

## Connections

This is a foundational entry in the computational-methods lineage for measuring ideology from social media; its author's related work on Twitter-based ideology and polarization is closely tied to [[Barbera2015-fw]]. The echo-chamber findings sit within a broader and often contested debate about selective exposure and cross-cutting exposure online, engaging arguments in [[Bakshy2015-rn]], [[Guess2023-ur]], [[Gonzalez-Bailon2023-uy]], [[Nyhan2023-gb]], and [[Flaxman2016-lm]], while [[Eady2023-xg]] and [[Osmundsen2021-et]] extend Twitter-based measurement to related behavioral questions.
