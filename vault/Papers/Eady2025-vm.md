---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.31219/osf.io/ch8gj
bibtex_key: Eady2025-vm
topics: [political-polarization-partisanship, election-campaigns-social-media]
citation_count: 14
open_access: false
source_url: https://doi.org/10.31219/osf.io/ch8gj
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3
pdf_available: true
discovery_date: 2026-07-20T15:24:30.361188Z
---

# News sharing on social media: Mapping the ideology of news media, politicians, and the mass public

> Eady, G., Bonneau, R., Tucker, J. A., & Nagler, J. (2025). News sharing on social media: Mapping the ideology of news media, politicians, and the mass public. *Polit. Anal.*, *33*, 73–90. https://doi.org/10.31219/osf.io/ch8gj
>
> [View paper](https://doi.org/10.31219/osf.io/ch8gj)

## Summary

This paper introduces a Bayesian measurement model — and an accompanying open-source R package (`mediascores`) — that places news media organizations, politicians, and ordinary social media users on a **common ideological scale** using only the behavior of sharing news URLs. Because links are platform-agnostic and require no labeled data, the approach offers a near-universal "currency" for ideology estimation. Applied to Twitter data from the 116th Congress and a sample of politically engaged users, the model reveals that news sharing cleanly separates legislators by party, that ordinary engaged citizens (not politicians) share most polarized content, and that ideologically extreme legislators share both more and more extreme news. The authors further link sharing polarization to electoral incentives: representatives in less competitive districts share more polarized, higher-volume news, suggesting a connection between electoral reform (e.g., gerrymandering) and the online information ecosystem.

## Key Contributions

- A unified, label-free Bayesian ideal-point model placing media, politicians, and users on a shared scale from link-sharing behavior alone.
- An open-source R package (`mediascores`) plus replication data for applied use.
- A **behavioral** measure of politician ideology derived from their own conduct rather than user perceptions (following/endorsement), extending to candidates lacking roll-call records.
- Empirical documentation that elite online information environments are skewed by high-volume, ideologically extreme sharers, with polarization tied to electoral competitiveness.
- A framework extensible to cross-platform, temporal/dynamic, and article-level estimation.

## Methods

The core model treats user-by-domain link-sharing counts as negative-binomial draws, where the probability a user shares an outlet decreases with the squared distance between latent user ideology (θ) and latent media ideology (ζ), with user- and domain-specific intercepts and a media dispersion parameter (ω). A homophily assumption underpins identification, resolved via Jackman's (2001) treatment of reflection invariance, hierarchical group priors (Democratic and Republican politicians, ordinary users), and centering media priors at zero to handle additive aliasing. Data include 1,152 manually compiled elite Twitter accounts, 220 national news domains, and 10,000 politically engaged users (per Barberá's definition), covering tweets back to 2015. Validation relies on convergent validity: correlating politician scores with NOMINATE and user scores with YouGov survey measures. OLS regressions then test whether district/state partisan alignment predicts ideological extremity of sharing, controlling for party, chamber, and NOMINATE.

## Findings

- News sharing separates members of Congress by party almost perfectly — only ~3% distributional overlap after removing indirect party information.
- Media scores correlate with NOMINATE at ρ = 0.96 overall (weaker but meaningful within party).
- User media scores correlate with survey-based ideology at ρ ≈ 0.73, on par with inter-correlations among the survey measures themselves.
- Outlet estimates show high face validity (Breitbart right of FOX, right of WSJ; HuffPost/The Nation left of NYT/WaPo/CNN; Reuters and AP near center) with a bimodal, left-skewed distribution.
- Engaged left-leaning users sit further left than the most liberal member of Congress; conservative users cluster near Republican legislators.
- Less electoral competition predicts more ideologically extreme sharing for both parties (robust to NOMINATE controls); extreme politicians also share far more news.
- Politicians share news more frequently than users (~0.082 vs. ~0.024 news links per tweet).

## Connections

This paper is a foundational methodological anchor for behavioral measurement of ideology and news sharing on social platforms, and it draws directly on the follow-based ideal-point tradition it seeks to complement. It relates most clearly to work on ideological cross-cutting exposure and diffusion via link sharing, [[Bakshy2015-rn]] and [[Gonzalez-Bailon2024-rq]], and connects to studies of coordinated or partisan link-sharing behavior such as [[Giglietto2023-fa71a001]] and [[Giglietto2024-cbeb3f70]]; its emphasis on how misperceptions and elite signals shape sharing links it loosely to [[Mosleh2024-op]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-safe-seats-and-extreme-feeds-whos/id1866587707?i=1000778009373)
