---
title: "News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"
aliases: ["News sharing on social media: Mapping the ideology of news media, politicians, and the mass public"]
authors: ["Gregory Eady", "Richard Bonneau", "Joshua A Tucker", "Jonathan Nagler"]
year: 2025
doi: 10.31219/osf.io/ch8gj
bibtex_key: Eady2025-vm
topics: [electoral-communication-cross-national, political-polarization-partisanship]
citation_count: 14
open_access: false
source_url: https://doi.org/10.31219/osf.io/ch8gj
podcast_url: 
pdf_available: true
discovery_date: 2026-07-20T15:24:30.361188Z
---

# News sharing on social media: Mapping the ideology of news media, politicians, and the mass public

> Eady, G., Bonneau, R., Tucker, J. A., & Nagler, J. (2025). News sharing on social media: Mapping the ideology of news media, politicians, and the mass public. *Polit. Anal.*, *33*, 73–90. https://doi.org/10.31219/osf.io/ch8gj
>
> [View paper](https://doi.org/10.31219/osf.io/ch8gj)

## Summary

This paper introduces a Bayesian measurement model — and an accompanying open-source R package (`mediascores`) — for placing news media organizations, politicians, and ordinary social media users on a single, common ideological scale using only the behavioral trace of sharing news URLs. Applied to Twitter data from the 116th U.S. Congress and a sample of politically engaged users, the model reveals the ideological structure of online news sharing without any labeled training data. The central empirical arguments are that elite online information environments are skewed by ideologically extreme, high-volume sharers, and that reduced electoral competition is associated with more polarized sharing — connecting the online information ecosystem to structural features like district partisan alignment.

## Key Contributions

- A unified, label-free, platform-agnostic Bayesian model placing media, politicians, and the mass public on a common ideological scale from link-sharing behavior alone.
- The open-source `mediascores` R package plus public replication data.
- A *behavioral* measure of politician ideology derived from actors' own conduct rather than from followers' endorsements, enabling study of little-known candidates without roll-call records.
- Empirical documentation that elite information environments are dominated by extreme, high-volume sharers, and that sharing polarization tracks electoral competitiveness — implying gerrymandering and electoral reform may shape the online ecosystem.
- A framework extensible to cross-platform, temporal, and article-level ideology estimation.

## Methods

- A Bayesian model treating user–domain link-sharing counts as negative binomial, where sharing probability decreases with the squared distance between latent user ideology (theta) and latent media ideology (zeta), plus user- and domain-specific intercepts and a media dispersion parameter (omega).
- Homophily assumption; identification via Jackman's (2001) handling of reflection invariance, hierarchical group priors (Democratic/Republican politicians, ordinary users), and media priors centered at zero to resolve additive aliasing.
- Data: 1,152 manually compiled Twitter accounts (699 actors) of the 116th Congress, governors, executive/cabinet, and party figures; 220 national news domains; 10,000 randomly sampled politically engaged users; tweets back to 2015 (quote-tweet links excluded).
- Validation by convergent validity — correlating politician media scores with NOMINATE, and user media scores with YouGov survey measures (issue positions, self-placement, partisan strength). OLS regressions relate news-sharing extremity to district/state partisan alignment (Trump–Clinton vote gap), controlling for party, chamber, and NOMINATE.

## Findings

- News-sharing behavior cleanly separates legislators by party; with a single common prior, only ~3% of the two parties' distributions overlap.
- Media scores correlate strongly with NOMINATE overall (rho = 0.96), more modestly within party.
- User media scores correlate with survey-based ideology at rho = 0.73 on average, comparable to inter-correlations among the survey measures themselves.
- Media-outlet estimates show high face validity (e.g., Breitbart right of FOX, HuffPost/The Nation left of NYT, Reuters/AP near center) with a bimodal, left-skewed distribution.
- Politically engaged left users sit further left than the most liberal member of Congress, while conservative users cluster near Republican legislators; sharing-based and following-based mappings differ.
- Greater partisan alignment (less competition) predicts more ideologically extreme sharing for both parties, robust to NOMINATE controls; extreme politicians also share substantially more news.
- Politicians share news more frequently than users (~0.082 vs. ~0.024 news links per tweet), and politically interested citizens — not politicians — share the majority of polarized content.

## Connections

This paper sits at the intersection of measuring political actors' ideology and studying elite/mass polarization; it is a methodological cornerstone for behavioral, sharing-based ideology estimation. Its foundational engagement with algorithmic and behavioral exposure to ideologically slanted news connects it directly to [[Bakshy2015-rn]] on ideological diversity in shared news, and its concern with cross-platform news-sharing structure relates to [[Gonzalez-Bailon2024-rq]]. None of the other listed papers appear to bear a genuine intellectual connection.
