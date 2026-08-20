---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A. Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.1017/pan.2024.19
bibtex_key: Eady2025-vm
topics: [political-polarization-and-partisanship, computational-network-structure-analysis]
citation_count: 9
open_access: false
source_url: https://doi.org/10.1017/pan.2024.19
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3
pdf_available: true
discovery_date: 2026-07-20T15:24:30.361188Z
---

# News sharing on social media: Mapping the ideology of news media, politicians, and the mass public

> Eady, G., Bonneau, R., Tucker, J. A., & Nagler, J. (2025). News sharing on social media: Mapping the ideology of news media, politicians, and the mass public. *Political Analysis*, *33*, 73–90. https://doi.org/10.1017/pan.2024.19
>
> [View paper](https://doi.org/10.1017/pan.2024.19)

## Summary

This paper introduces a Bayesian measurement model — released as an open-source R package (`mediascores`) — that places news media outlets, politicians, and ordinary social media users on a *common* ideological scale using only the behavioral trace of sharing news URLs. The key methodological advance is that link-sharing serves as a near-universal, platform-agnostic, label-free "currency" for ideology estimation. Applying the model to Twitter data from U.S. members of Congress and politically engaged users, the authors map the ideological structure of online news sharing and find that elite information environments are skewed by ideologically extreme, high-volume sharers, and that reduced electoral competition is associated with more polarized sharing.

## Key Contributions

- A unified, platform-agnostic, label-free Bayesian model placing media, politicians, and users on one ideological scale from link-sharing alone.
- An open-source R package (`mediascores`) plus public replication data for applied use.
- A *behavioral* measure of politician ideology derived from their own sharing conduct (rather than users' following/endorsement), extendable to little-known candidates without voting records.
- Empirical evidence that elite online information environments are skewed by extreme high-volume sharers, and that sharing polarization tracks electoral competitiveness — linking gerrymandering/electoral reform to the online information ecosystem.

## Methods

A Bayesian measurement model treats user–outlet link-sharing counts as negative-binomial, with sharing probability declining in the squared distance between latent user ideology (θ) and latent media ideology (ζ), plus user- and domain-specific intercepts and a media dispersion parameter (ω). Identification follows a homophily assumption, Jackman's (2001) treatment of reflection invariance, hierarchical group priors (Democratic politicians, Republican politicians, ordinary users), and zero-centered media priors to resolve additive aliasing. Data cover 1,152 manually compiled Twitter accounts of the 116th Congress and prominent figures (699 actors), 220 national news domains, and a random sample of 10,000 politically engaged users (per Barberá's definition), with tweets back to 2015. Validation uses convergent validity: politicians' scores against NOMINATE, and users' scores against YouGov survey-linked measures; OLS regressions relate sharing extremity to district partisan alignment.

## Findings

- News-sharing behavior cleanly separates Congress by party; with a single common prior only 3% of the two parties' distributions overlap.
- Media scores correlate strongly with NOMINATE overall (ρ = 0.96), more modestly within party (0.51–0.76).
- User media scores correlate with survey ideology measures at ρ = 0.73, comparable to the survey measures' inter-correlations.
- Outlet estimates have high face validity (e.g., Breitbart right of FOX, HuffPost/The Nation left of NYT/CNN, Reuters/AP near center), with a bimodal, left-skewed distribution.
- Politically engaged left-leaning users are more liberal than the most liberal member of Congress; conservative users cluster closer to Republican legislators.
- Politically interested citizens — not politicians — share most polarized political news; but ideologically extreme legislators share more news overall and more extreme content.
- Greater partisan alignment (less competition) predicts more extreme sharing for both parties, robust to controlling for NOMINATE.
- Politicians share news more frequently than users (~0.082 vs ~0.024 news links per tweet).

## Connections

This paper is foundational for behavioral, link-based ideology measurement and pairs naturally with work on partisan news exposure and sharing on platforms, such as [[Bakshy2015-rn]] and the platform-level exposure mapping of [[Gonzalez-Bailon2024-rq]]. Its concern with how news domains diffuse and cluster ideologically connects to coordinated and structural URL-sharing analyses like [[Giglietto2019-882f1900]], [[Giglietto2020-6278a4aa]], and [[Minici2024-tf]]. It also speaks to the broader elite-versus-mass polarization debate engaged by [[Green2025-ap]] and [[Tornberg2025-ir]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-safe-seats-and-extreme-feeds-whos/id1866587707?i=1000778009373)
