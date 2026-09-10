---
title: "Did podcasts help Trump win young men? Gendered media spaces and gender gaps"
aliases: ["Did podcasts help Trump win young men? Gendered media spaces and gender gaps"]
authors: ["Melina Much", "Kylan Rutherford", "Jason Greenfield", "Joshua A. Tucker", "Jonathan Nagler"]
year: 2026
doi: 10.33774/apsa-2026-cdb6x
bibtex_key: Much2026-gu
topics: [electoral-campaigns-social-media, political-polarization-partisan-media]
citation_count: 0
open_access: false
source_url: https://doi.org/10.33774/apsa-2026-cdb6x
podcast_url: 
pdf_available: true
discovery_date: 2026-09-10T09:18:45.993588Z
---

# Did podcasts help Trump win young men? Gendered media spaces and gender gaps

> Much, M., Rutherford, K., Greenfield, J., Tucker, J. A., & Nagler, J. (2026). Did podcasts help Trump win young men? Gendered media spaces and gender gaps. *APSA Preprints*. https://doi.org/10.33774/apsa-2026-cdb6x
>
> [View paper](https://doi.org/10.33774/apsa-2026-cdb6x)

## Summary

This paper asks whether entertainment podcasts contributed to the sharp widening of the youth gender gap in the 2024 U.S. election, when young men shifted markedly toward Trump. The authors introduce the concept of **gendered media spaces**: non-political entertainment environments where audiences sort along masculine/feminine content preferences rather than ideology, yet nonetheless receive systematically different incidental political messaging. Because masculinity is cognitively linked to conservatism (and femininity to liberalism), this "gendered ideological sorting" delivers ideologically congruent content to listeners who never sought it. Combining two survey datasets with a transcript analysis of 36,659 episodes from the 276 most popular U.S. podcasts, they find that podcast masculinity correlates with conservative content, that Trump selected venues on gender rather than ideology, and that conservative podcast exposure predicts higher Trump support — though it explains only a small share of the gender gap.

## Key Contributions

- Introduces **gendered media spaces** and **gendered ideological sorting** as a political communication mechanism distinct from partisan selective exposure.
- Provides the first transcript-level, large-scale empirical mapping of the top U.S. podcast ecosystem along gender expression and ideology.
- Develops an LLM-based two-stage (detection then directional scoring) measurement method for gender and ideological content, validated against human coders.
- Documents candidate venue-selection strategies (Trump vs. Harris) along gender versus ideology dimensions.
- Links incidental podcast exposure to vote intention and vote choice using both a consumption panel (Edison) and a nationally representative panel (YouGov).

## Methods

The authors analyzed 36,659 episodes from the top 0.01% (276) most popular U.S. podcasts over the 2024 cycle, selected via ListenNotes popularity and validated against Edison rankings. Audio was transcribed and diarized with WhisperX, and ~8.5 million speaker chunks were labeled by Gemini 3 Flash Preview in a two-stage detection-then-scoring process, collapsed to ternary directional scores and validated against human coders. Episode- and podcast-level indices were built as word-count-weighted net gender and net ideology measures (gender blending 90% transcript / 10% host self-identification). Consumption was measured with Edison Podcast Metrics (show-level demographic profiles for all 276 podcasts plus individual-level data from 3,544 respondents across 129 non-political podcasts) and an original YouGov panel of 1,167 respondents linked to prior vote history, modeling Trump vote probability conditional on Joe Rogan and other candidate-interview listenership. Selection concerns were addressed by controlling for partisanship and prior vote.

## Findings

- Political-genre podcasts average 81% political content per episode; non-political podcasts average 15% (median 7%) — enough for meaningful incidental exposure.
- Among non-political episodes with political content, 47% lean liberal, 27% conservative, 26% moderate/mixed; among political-genre episodes 72% lean conservative.
- Liberal-leaning podcasts are more numerous and prolific overall (192 podcasts, 19,842 episodes vs. 79 conservative, 16,812), driven by the non-political sector.
- Masculine gender expression positively correlates with conservative ideology; nearly all conservative podcasts are heavily masculine, though masculinity spans the ideological spectrum.
- Trump's 16 non-political appearances aligned with podcast gender expression (persuasion), while Harris's 5 appearances aligned with ideological lean (mobilization).
- Young men received the most exposure to conservative content in non-political podcasts of any age-gender cohort.
- Conservative podcast exposure predicts higher Trump vote intention after controlling for party ID, concentrated among Independents; effect sizes are similar across groups, but young men encountered far more conservative content.
- Counterfactuals: giving young men the podcast diet of young women significantly lowers predicted Trump support; the reverse modestly raises it.
- YouGov panel: self-reported Joe Rogan listening predicts higher Trump vote probability even controlling for party ID and prior vote.
- The overall association is small and cannot explain the entirety of the youth gender gap.

## Connections

This paper extends work on the political persuasion effects of new and alternative media environments, complementing analyses of manosphere and influencer politics such as [[Marwick2026-qd]] and [[Copland2025-em]], and studies of partisan/alternative media effects like [[Arceneaux2026-xk]]. Its focus on how candidates strategically select media venues during a campaign links it to broader work on campaign communication on emerging platforms, including [[Rodarte2026-dk]] and [[Achmann-Denkler2026-lx]]. The LLM-based transcript coding approach connects methodologically to other efforts using large language models to scale political content measurement, such as [[Le-Mens2025-qz]].
