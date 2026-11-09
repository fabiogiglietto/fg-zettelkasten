---
title: "Like-minded sources on Facebook are prevalent but not polarizing"
aliases: ["Like-minded sources on Facebook are prevalent but not polarizing"]
authors: ["Brendan Nyhan", "Jaime Settle", "Emily Thorson", "Magdalena Wojcieszak", "Pablo Barberá", "Annie Y. Chen", "Hunt Allcott", "Taylor Brown", "Adriana Crespo-Tenorio", "Drew Dimmery", "Deen Freelon", "Matthew Gentzkow", "Sandra González-Bailón", "Andrew M. Guess", "Edward Kennedy", "Young Mie Kim", "David Lazer", "Neil Malhotra", "Devra Moehler", "Jennifer Pan", "Daniel Robert Thomas", "Rebekah Tromble", "Carlos Velasco Rivera", "Arjun Wilkins", "Beixian Xiong", "Chad Kiewiet de Jonge", "Annie Franco", "Winter Mason", "Natalie Jomini Stroud", "Joshua A. Tucker"]
year: 2023
doi: 10.1038/s41586-023-06297-w
bibtex_key: Nyhan2023-gb
topics: [misinformation-exposure-recalibration, political-polarization-partisanship]
citation_count: 254
open_access: false
source_url: https://doi.org/10.1038/s41586-023-06297-w
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445495Z
editorial_notices: [correction]
---

# Like-minded sources on Facebook are prevalent but not polarizing

> [!note] Corrected
> - Correction (2023-11-01): [10.1038/s41586-023-06795-x](https://doi.org/10.1038/s41586-023-06795-x)

> Nyhan, B., Settle, J., Thorson, E., Wojcieszak, M., Barberá, P., Chen, A. Y., Allcott, H., Brown, T., Crespo-Tenorio, A., Dimmery, D., Freelon, D., Gentzkow, M., González-Bailón, S., Guess, A. M., Kennedy, E., Kim, Y. M., Lazer, D., Malhotra, N., Moehler, D., Pan, J., Thomas, D. R., Tromble, R., Rivera, C. V., Wilkins, A., Xiong, B., de Jonge, C. K., Franco, A., Mason, W., Stroud, N. J., & Tucker, J. A. (2023). Like-minded sources on Facebook are prevalent but not polarizing. *Nature*, *620*, 137–144. https://doi.org/10.1038/s41586-023-06297-w
>
> [View paper](https://doi.org/10.1038/s41586-023-06297-w)

## Summary

This paper combines population-scale behavioral measurement with a large preregistered field experiment to test the popular claim that social media echo chambers drive political polarization. Using exposure data for the full population of active US adult Facebook users during the 2020 election, the authors document that a majority of content viewed comes from politically like-minded sources — though political and news content is only a small fraction of overall exposure, and extreme echo chambers are relatively uncommon. In a three-month field experiment with 23,377 consenting users, an algorithmic intervention that reduced like-minded exposure by about a third measurably reshaped feeds but produced no detectable change in any of eight preregistered attitudinal outcomes. The tightly bounded null results challenge narratives that blame like-minded exposure for polarization, suggesting instead that what users see may reflect their existing identities more than it shapes their expressed views.

## Key Contributions

- First systematic, non-self-report behavioral measurement of like-minded content exposure across the entire US adult Facebook population, overcoming longstanding platform data-access limits.
- Rare large-scale causal evidence from a real-world field experiment on an operating platform, rather than survey self-reports or brief simulations.
- Shows that algorithmic interventions can reshape feed composition without automatically increasing cross-cutting exposure or shifting attitudes.
- Precisely estimated null results with tight equivalence bounds, methodologically distinguishing genuine nulls from underpowered failures.
- Provides a model of industry–academic collaboration with preregistration and academic control over analysis and publication.

## Methods

- **Descriptive component:** classified sources seen by ~231 million monthly active US adult users (Q3–Q4 2020) as like-minded, cross-cutting, or neither, using an internal Facebook ideology classifier (liberal ≤0.4, conservative ≥0.6).
- **Experimental component:** a preregistered five-wave field experiment (24 Sept–23 Dec 2020) with 23,377 consenting users, block-randomized at equal probability. The treatment downranked *all* content — from friends, Pages, and groups — predicted to match the participant's political leaning, using the strongest demotion that would not empty feeds.
- Combined on-platform behavioral exposure/engagement data with survey outcomes; analysis via OLS with HC2 standard errors, lasso-selected covariates, survey weights, FDR adjustment, and equivalence-bounds tests. Fieldwork by NORC as part of the 2020 Facebook and Instagram Election Study; academics retained final analytic and publication control.

## Findings

- The median user received 50.4% of content from like-minded sources versus 14.7% cross-cutting; civic and news content were small shares of total exposure (medians 6.9% and 6.7%).
- Extreme echo chambers were uncommon: 20.6% of users got >75% of exposures from like-minded sources, while 23.1% got <25%.
- The treatment cut like-minded exposure from 53.7% to 36.2% (−0.77 s.d.), but this did *not* symmetrically raise cross-cutting content — most of the gain went to content that was neither (25.6% to 35.9%).
- The intervention incidentally reduced exposure to uncivil content, slurs, and misinformation repeat offenders.
- Total engagement with like-minded content fell, but the conditional engagement *rate* rose — users interacted more with the reduced congenial content they still saw.
- No measurable effects on eight preregistered attitudinal outcomes; seven of eight estimates fell within ±0.03 s.d., with effects of ±0.12 s.d. or larger confidently ruled out, and no significant heterogeneity across 272 subgroup tests.

## Connections

This is part of the 2020 Facebook and Instagram Election Study cluster and directly extends the algorithmic-feed intervention work in [[Guess2023-ai]] and [[Guess2023-ur]], as well as the broader description of Facebook exposure and ideological segregation in [[Gonzalez-Bailon2023-uy]] and the earlier [[Bakshy2015-rn]]. Its null findings on attitudes speak to the same tradition as [[Bail2018-fk]] (which found exposure to opposing views did not reduce polarization) and to selective-exposure and filter-bubble debates traced in [[Flaxman2016-lm]] and [[Barbera2015-fw]]; the finding that reduced like-minded exposure also cut misinformation exposure links it to [[Gonzalez-Bailon2024-rq]] and work on affective polarization such as [[Iyengar2019-jj]].
