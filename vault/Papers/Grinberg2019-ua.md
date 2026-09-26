---
title: "Fake news on Twitter during the 2016 U.S. presidential election"
aliases: ["Fake news on Twitter during the 2016 U.S. presidential election"]
authors: ["Nir Grinberg", "Kenneth Joseph", "Lisa Friedland", "Briony Swire-Thompson", "David Lazer"]
year: 2019
doi: 10.1126/science.aau2706
bibtex_key: Grinberg2019-ua
topics: [misinformation-exposure-recalibration, election-campaigns-social-media]
citation_count: 1287
open_access: false
source_url: https://doi.org/10.1126/science.aau2706
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445442Z
---

# Fake news on Twitter during the 2016 U.S. presidential election

> Grinberg, N., Joseph, K., Friedland, L., Swire-Thompson, B., & Lazer, D. (2019). Fake news on Twitter during the 2016 U.S. presidential election. *Science*, *363*, 374–378. https://doi.org/10.1126/science.aau2706
>
> [View paper](https://doi.org/10.1126/science.aau2706)

## Summary

This paper offers one of the earliest direct, individual-level measurements of how ordinary U.S. voters encountered and spread fake news on Twitter during the 2016 presidential campaign. By linking a panel of 16,442 Twitter accounts to voter registration records, the authors reconstruct both what political news users were *exposed* to and what they *shared*. Their central argument tempers the alarmist narrative: engagement with fake news was real but extraordinarily concentrated among a tiny slice of users — disproportionately conservative, older, and highly politically engaged — while the overwhelming majority of political news exposure, across the political spectrum, still came from mainstream outlets. Rather than veracity, they find that *congruency* with existing beliefs drove sharing decisions, implying fake news was not intrinsically more viral than accurate reporting.

## Key Contributions

- One of the first direct measurements of citizens' fake news exposure and sharing on social media, anchored to real voter identities rather than aggregate platform data or self-report surveys.
- Documents extreme concentration of fake news engagement in tiny subpopulations, reframing the perceived scale of the problem.
- Uses individual-level regression to identify demographic and behavioral predictors (conservatism, age, political engagement).
- Maps fake news sources within the wider media ecosystem via a coexposure network, showing they form an insulated right-leaning cluster.
- Proposes and simulates concrete, targeted platform interventions (demoting frequent posters, capping daily posts, fact-checker partnerships).

## Methods

The authors built a panel of 16,442 Twitter accounts active from 1 August to 6 December 2016 by matching voter registration records to Twitter profiles, validating representativeness against a Pew probability sample. Fake news was defined at the publisher level (following Lazer et al.), classifying 171 "black," 64 "red," and 65 "orange" sources. Each member's news feed ("exposures") was estimated by sampling tweets from followed accounts, restricted to political tweets carrying external URLs. Individuals were placed into five political affinity groups plus an apolitical group based on feed similarity to registered partisans. Binomial and logistic regressions (fit separately by group) identified predictors of exposure and sharing; a statistically-significant-edge coexposure network with ensemble clustering located fake news sources in the ecosystem; and a simulation tested capping political URLs at 20 per day.

## Findings

- Fake news made up 5.0% of aggregate political URL exposures and 6.7% of shared political URLs, rising in the final campaign weeks.
- Engagement was extremely concentrated: 1% of users accounted for 80% of fake news exposures, and 0.1% for nearly 80% of shares.
- The top seven fake news sources supplied over 50% of fake news exposures; the median member had ~204 potential exposures in the final month (roughly 10 actually seen), just 1.18% of political exposures.
- Right-leaning skew was stark: 16.3% of the right had 5%+ fake news exposures (vs. 2.5% of the left), and 21% of the extreme right shared fake news (vs. under 5% on the left or center).
- Selective exposure was superlinear — a 10-fold increase in political exposures doubled the fake news proportion — and age was positively associated with engagement across all groups.
- Congruent sources were shared at higher rates than incongruent ones, with no significant sharing difference between congruent fake and nonfake sources.
- "Supersharers" and "superconsumers" dwarfed typical users (median supersharer: 71 tweets/day vs. 0.1) and appeared partly automated "cyborg" accounts.
- Capping political URLs at 20/day would cut fake news content by 32% while touching only 1% of non-supersharers' content.

## Connections

This paper is a foundational empirical touchstone for the misinformation-exposure literature, and it directly extends the publisher-level fake news framework and prior browsing/survey studies that this register also collects — see [[Lazer2018-mm]], [[Allcott2017-yz]], [[Guess2019-ym]], and [[Guess2020-rr]]. Its findings on the small, highly active supersharer minority and on concentration of misinformation resonate with Grinberg2019 follow-ups such as [[Mosleh2024-op]] and [[Budak2024-ef]], while its evidence against fake-news virality and echo-chamber dominance speaks to [[Vosoughi2018-at]], [[Gonzalez-Bailon2024-rq]], [[Guess2021-ym]], and [[Eady2023-xg]]; the finding that congruency rather than veracity drives sharing connects to [[Osmundsen2021-et]] and [[Pennycook2021-jq]].
