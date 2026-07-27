---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.31219/osf.io/ch8gj
bibtex_key: Eady2025-vm
topics: [political-polarization-partisanship, computational-network-structure-analysis]
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

This paper introduces a Bayesian measurement model — and an accompanying open-source R package (`mediascores`) — that places news media outlets, politicians, and ordinary social media users on a *common* ideological scale using only the behavior of sharing news URLs. The core insight is that web links function as a near-universal, platform-agnostic, label-free currency for ideal-point estimation: no hand-coding of content or user labels is required. Applying the model to Twitter data from the 116th U.S. Congress and a sample of politically engaged users, the authors map the ideological structure of online news sharing and show that the elite online information environment is skewed toward polarization by a minority of extreme, high-volume sharers, with sharing polarization tied to reduced electoral competition.

## Key Contributions

- A unified, platform-agnostic, label-free Bayesian ideal-point model placing media, politicians, and mass public on one scale from link-sharing alone.
- An open-source R package (`mediascores`) plus public replication data for applied use.
- A *behavioral* measure of politician ideology derived from their own conduct rather than from follower/endorsement perceptions — usable even for candidates lacking roll-call records.
- Empirical documentation that extreme, high-volume sharers distort the elite information environment, with a link to electoral competitiveness (implying gerrymandering/reform may reshape the online ecosystem).
- A framework extensible to cross-platform, dynamic/temporal, and article-level ideology estimation.

## Methods

- A Bayesian measurement model treats user–outlet link-sharing counts as negative-binomially distributed, with the sharing probability declining in the squared distance between latent user ideology (θ) and latent media ideology (ζ); includes user- and domain-specific intercepts and a media dispersion parameter (ω).
- Homophily assumption; identification via Jackman's approach to reflection invariance, hierarchical group-level priors (Democratic politicians, Republican politicians, ordinary users), and media priors centered at zero to resolve additive aliasing.
- Data: manually compiled Twitter accounts of the 116th Congress and prominent figures (1,152 accounts, 699 actors), 220 national news domains, and 10,000 politically engaged ordinary users; tweets back to 2015, quote-tweet links excluded.
- Validation by convergent validity: correlating politician media scores with NOMINATE, and user scores with YouGov survey measures (issue positions, self-placement, partisanship strength) for 481 respondents.
- OLS regressions of the ideological extremity of politicians' news sharing on district/state partisan alignment (Trump–Clinton vote-share gap), controlling for party, chamber, and NOMINATE.

## Findings

- News-sharing behavior cleanly separates members of Congress by party — only ~3% distributional overlap even after removing indirect party information.
- Media scores correlate strongly with NOMINATE overall (ρ = 0.96) and moderately within party; user scores correlate with survey ideology at ρ ≈ 0.73, on par with the survey measures' own inter-correlations.
- Media-outlet estimates have high face validity (e.g., Breitbart right of FOX, right of WSJ; HuffPost/The Nation left of NYT/WaPo/CNN; Reuters and AP near center), with a bimodal, left-skewed distribution.
- Politically engaged left users are more liberal than the most liberal legislator, while conservative users cluster nearer Republican legislators; sharing-based mapping differs from following-based measures.
- Greater partisan alignment (less electoral competition) predicts more extreme news sharing in both parties, robust to controlling for NOMINATE; extreme politicians also share far more news.
- Ordinary politically interested citizens — not politicians — share the majority of polarized political news; politicians nonetheless share news more frequently per tweet (~0.082 vs ~0.024).

## Connections

This paper sits within the measurement and polarization literatures on mapping ideology from online behavior; it is closely related to work reasoning about news slant, gatekeeping, and diffusion on social platforms such as [[Bakshy2015-rn]] and [[Gonzalez-Bailon2024-rq]]. Its concern with elite versus mass polarization and the skew of the online information environment connects it to the broader partisanship and news-sharing research in this register.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Eady2025-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
