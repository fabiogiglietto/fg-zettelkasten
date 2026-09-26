---
title: "How do social media feed algorithms affect attitudes and behavior in an election campaign?"
aliases: ["How do social media feed algorithms affect attitudes and behavior in an election campaign?"]
authors: ["Andrew M. Guess", "Neil Malhotra", "Jennifer Pan", "Pablo Barberá", "Hunt Allcott", "Taylor Brown", "Adriana Crespo-Tenorio", "Drew Dimmery", "Deen Freelon", "Matthew Gentzkow", "Sandra González-Bailón", "Edward Kennedy", "Young Mie Kim", "David Lazer", "Devra Moehler", "Brendan Nyhan", "Carlos Velasco Rivera", "Jaime Settle", "Daniel Robert Thomas", "Emily Thorson", "Rebekah Tromble", "Arjun Wilkins", "Magdalena Wojcieszak", "Beixian Xiong", "Chad Kiewiet de Jonge", "Annie Franco", "Winter Mason", "Natalie Jomini Stroud", "Joshua A. Tucker"]
year: 2023
doi: 10.1126/science.abp9364
bibtex_key: Guess2023-ur
topics: [election-campaigns-social-media, political-polarization-partisanship]
citation_count: 325
open_access: false
source_url: https://doi.org/10.1126/science.abp9364
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445505Z
editorial_notices: [correction]
---

# How do social media feed algorithms affect attitudes and behavior in an election campaign?

> [!note] Corrected
> - Correction (2024-12-05): [10.1126/science.adu8261](https://doi.org/10.1126/science.adu8261)
> - Correction (2026-03-19): [10.1126/science.aeh2575](https://doi.org/10.1126/science.aeh2575)

> Guess, A. M., Malhotra, N., Pan, J., Barberá, P., Allcott, H., Brown, T., Crespo-Tenorio, A., Dimmery, D., Freelon, D., Gentzkow, M., González-Bailón, S., Kennedy, E., Kim, Y. M., Lazer, D., Moehler, D., Nyhan, B., Rivera, C. V., Settle, J., Thomas, D. R., Thorson, E., Tromble, R., Wilkins, A., Wojcieszak, M., Xiong, B., de Jonge, C. K., Franco, A., Mason, W., Stroud, N. J., & Tucker, J. A. (2023). How do social media feed algorithms affect attitudes and behavior in an election campaign?. *Science*, *381*, 398–404. https://doi.org/10.1126/science.abp9364
>
> [View paper](https://doi.org/10.1126/science.abp9364)

## Summary

This paper reports one of the largest field experiments ever conducted on social media and politics, run during the 2020 US presidential election in collaboration with Meta. The authors randomly assigned consenting Facebook and Instagram users to receive a reverse-chronological feed—rather than the default machine-learning-ranked feed—for roughly three months. The central finding is a stark disconnect: while the chronological feed dramatically reshaped users' on-platform experience (less time spent, less engagement, a different mix of content and sources), it produced *no* detectable changes in downstream political outcomes such as affective polarization, issue polarization, political knowledge, or offline participation. The paper uses this well-defined counterfactual to argue that feed-ranking algorithms, while powerful shapers of experience, are not by themselves the direct root cause of individual-level political harms often attributed to them.

## Key Contributions

- Isolates the causal effect of the proprietary *feed-ranking algorithm* specifically, rather than the entire social media "bundle," a distinction most prior work could not make.
- Uses reverse-chronological ranking as a clean counterfactual that directly matches real-world regulatory and policy proposals.
- Documents a striking gap between large algorithm-induced changes in user experience and negligible changes in political attitudes and behavior.
- Tempers popular "filter bubble" and folk theories about algorithmic harm with large-scale experimental evidence.
- Contributes deidentified data and code (via SOMAR) as a replication and research template.

## Methods

Two preregistered randomized controlled experiments were embedded within Facebook (n = 23,391) and Instagram (n = 21,373), recruiting consenting US adults via in-feed survey invitations. The treatment group received a reverse-chronological feed from 24 September to 23 December 2020, affecting roughly 80% of on-platform material (ads unchanged). Data combined five survey waves with on-platform behavioral logs and passive off-platform web-tracking (fieldwork by NORC). The primary estimand was the population average treatment effect, weighted by predicted ideology, friend count, political pages followed, and days active. Content was classified along dimensions including political content, news, ideological cross-cutting versus like-minded sources, source trustworthiness, incivility, and slur usage. Meta funded data collection but held no prepublication approval rights; academic lead authors retained final control.

## Findings

- **Time spent fell sharply**: daily time relative to average users dropped from +73% to +37% on Facebook and +107% to +84% on Instagram, with substitution toward TikTok, YouTube, Reddit, and Instagram.
- **Engagement declined**: Facebook likes fell from 6.7% to 3.1% of exposures, with comparable drops in Instagram likes and comments.
- **Content mix shifted**: chronological feeds increased political content, political news, and untrustworthy-source content, while decreasing uncivil content and slur words on Facebook.
- **Source composition changed**: on Facebook, both like-minded (53.7%→48.1%) and cross-cutting (20.7%→18.7%) sources fell, while moderate/mixed-audience sources rose (22.6%→30.9%) and friend-sourced content dropped ~24 points.
- **No significant political effects**: no changes in affective or issue polarization, election or news knowledge, self-reported participation, or turnout on either platform.
- On-platform political engagement declined (Facebook −0.117 SD; Instagram −0.090 SD).
- The lone significant secondary effect: Facebook chronological-feed users clicked more on partisan political news (0.107 SD), attributed to greater exposure to frequently posted partisan links.

## Connections

This paper is part of the same Meta–academic collaboration that produced parallel large-scale 2020 experiments, and it directly engages the echo-chamber and cross-cutting-exposure literature exemplified by [[Bakshy2015-rn]], [[Gonzalez-Bailon2023-uy]], [[Nyhan2023-gb]], and [[Guess2023-ai]]. Its null findings on polarization speak to debates over the drivers of affective polarization and folk theories of algorithmic harm found in [[Bail2018-fk]], [[Iyengar2019-jj]], and filter-bubble arguments such as [[Flaxman2016-lm]] and [[Del-Vicario2016-uj]]. It also complements experimental deactivation and exposure studies including [[Allcott2017-yz]] and [[Guess2020-rr]] by isolating ranking as a distinct causal factor rather than the whole platform bundle.
