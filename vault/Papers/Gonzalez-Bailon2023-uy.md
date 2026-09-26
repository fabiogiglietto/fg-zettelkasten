---
title: "Asymmetric ideological segregation in exposure to political news on Facebook"
aliases: ["Asymmetric ideological segregation in exposure to political news on Facebook"]
authors: ["Sandra González-Bailón", "David Lazer", "Pablo Barberá", "Meiqing Zhang", "Hunt Allcott", "Taylor Brown", "Adriana Crespo-Tenorio", "Deen Freelon", "Matthew Gentzkow", "Andrew M. Guess", "Shanto Iyengar", "Young Mie Kim", "Neil Malhotra", "Devra Moehler", "Brendan Nyhan", "Jennifer Pan", "Carlos Velasco Rivera", "Jaime Settle", "Emily Thorson", "Rebekah Tromble", "Arjun Wilkins", "Magdalena Wojcieszak", "Chad Kiewiet de Jonge", "Annie Franco", "Winter Mason", "Natalie Jomini Stroud", "Joshua A. Tucker"]
year: 2023
doi: 10.1126/science.ade7138
bibtex_key: Gonzalez-Bailon2023-uy
topics: [political-polarization-partisanship, political-content-moderation-visibility]
citation_count: 256
open_access: false
source_url: https://doi.org/10.1126/science.ade7138
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445500Z
---

# Asymmetric ideological segregation in exposure to political news on Facebook

> González-Bailón, S., Lazer, D., Barberá, P., Zhang, M., Allcott, H., Brown, T., Crespo-Tenorio, A., Freelon, D., Gentzkow, M., Guess, A. M., Iyengar, S., Kim, Y. M., Malhotra, N., Moehler, D., Nyhan, B., Pan, J., Rivera, C. V., Settle, J., Thorson, E., Tromble, R., Wilkins, A., Wojcieszak, M., de Jonge, C. K., Franco, A., Mason, W., Stroud, N. J., & Tucker, J. A. (2023). Asymmetric ideological segregation in exposure to political news on Facebook. *Science*, *381*, 392–398. https://doi.org/10.1126/science.ade7138
>
> [View paper](https://doi.org/10.1126/science.ade7138)

## Summary

This paper offers one of the first large-scale, platform-internal maps of ideological segregation in political news exposure, using aggregated data on roughly 208 million US adult Facebook users during the 2020 election cycle. Adopting a "funnel of engagement" framework, the authors trace political news through three stages — what users *could* see (inventory), what they *actually* saw after algorithmic curation (feed), and what they *engaged* with — to disentangle the contributions of algorithms and social behavior. They find that news consumption on Facebook is far more ideologically segregated than prior web-browsing research implied, that segregation grows along the funnel, and that the segregation is asymmetric: there is a distinctly homogeneous conservative corner of the ecosystem, with no liberal equivalent, and most fact-checked misinformation lives inside it.

## Key Contributions

- First large-scale platform-internal account distinguishing potential exposure, actual exposure, and engagement, moving beyond reliance on external web-browsing panels.
- Introduces URL- (news-story-) level measurement of segregation, revealing within-domain curation that domain-level aggregation masks.
- Documents the outsized role of Pages and Groups (versus friends) as curation and amplification mechanisms driving segregation.
- Empirically establishes the asymmetric conservative concentration of both homogeneous audiences and misinformation.
- Provides a reproducible industry–academic collaboration model with a registered preanalysis plan, offering a blueprint for platform data access under regimes like the EU DSA.

## Methods

The analysis rests on aggregated (not individual-level) exposure and engagement data for ~208 million US adult active users from 1 September 2020 to 1 February 2021, restricted for privacy to URLs shared more than 100 times (~35,000 domains, ~640,000 URLs). Facebook's internal civic/news classifiers identified political news and an internal ideology classifier categorized users (≤0.35 liberal, ≥0.65 conservative). The authors compute a segregation index adapted from residential-segregation research (following Gentzkow and Shapiro) and favorability scores (−1 fully liberal to +1 fully conservative) at both domain and URL levels. They build coexposure networks (edges weighted by shared unique viewers) and apply Pons–Latapy walktrap community detection with backbone extraction. Misinformation is classified via Meta's Third-Party Fact-Checking Program. Robustness checks compare on-platform segregation to off-platform web browsing for consented users and vary content type, political interest, posting source, and ideology operationalization.

## Findings

- Domain-level segregation for exposed audiences hovered around 0.35, far above the 0.02–0.10 range in prior web-browsing studies; URL-level segregation was higher still, roughly 0.45–0.50.
- Segregation rose along the funnel: exposed exceeded potential, and engaged exceeded exposed — implicating both algorithmic and social amplification.
- Favorability distributions were right-skewed, with more content favored by very conservative than by very liberal audiences.
- 71–76% of untrustworthy domains and 97% of false URLs had conservative-leaning audiences across all funnel stages.
- Misinformation shared by Pages and Groups had audiences almost entirely on the right; Pages produced the most conservative audiences.
- Facebook segregation was roughly three times a within-person web-tracking benchmark for the same consented users.
- Community detection recovered clear liberal and conservative clusters from behavior alone, with the conservative cluster more isolated and exposed to more unreliable content.
- High-political-interest users were about twice as segregated as low-interest users; the single most-viewed story was a false claim about Pennsylvania military ballots from a low-ranked domain (pjmedia.com).

## Connections

This paper is a direct sequel to and critical revision of the friend-network filter-bubble study [[Bakshy2015-rn]], extending the analysis from friend-posted content to Pages and Groups and to URL-level curation. It sits alongside the companion Facebook and Instagram Election Study experiments on feed algorithms and reshares [[Guess2023-ai]], [[Guess2023-ur]], [[Nyhan2023-gb]], and its finding that misinformation concentrates on the right resonates with work on the asymmetric structure of partisan political behavior [[Osmundsen2021-et]] and affective polarization [[Iyengar2019-jj]]. Its coexposure-network mapping also connects to network-based studies of online audience clustering [[Del-Vicario2016-uj]], [[Barbera2015-fw]].
