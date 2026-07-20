---
title: "Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States"
aliases: ["Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States"]
authors: ["Christian Schemer", "Klara Langmann", "Ariel Hasell", "Brian Weeks"]
year: 2026
doi: 10.1080/10584609.2026.2699105
bibtex_key: Schemer2026-mh
topics: [political-polarization-partisanship, survey-methodology-validity]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/10584609.2026.2699105
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schemer2026-mh.mp3
pdf_available: true
discovery_date: 2026-07-12T07:23:36.517732Z
---

# Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States

> Schemer, C., Langmann, K., Hasell, A., & Weeks, B. (2026). Does the method affect the outcome? How measures of partisan slant of media outlets and affective polarization drive results about polarization in the United States. *Political Communication*, 1–25. https://doi.org/10.1080/10584609.2026.2699105
>
> [View paper](https://doi.org/10.1080/10584609.2026.2699105)

## Summary

This paper interrogates a methodological problem at the heart of the partisan-media-and-polarization literature: does the way researchers measure media slant and polarization determine the conclusions they reach? Using three-wave YouGov panel data from the 2020 U.S. presidential election, the authors run a specification curve analysis (SCA) across 504 combinations of independent- and dependent-variable operationalizations. Their central finding is nuanced but consequential: methodological choices substantially alter the *strength* and *significance* of the observed relationship between partisan media diets and affective/belief polarization—but not its *direction*. Coefficients never flipped sign, yet the largest was nearly seven times the smallest. The paper thus makes an empirical case that the ongoing normative debate about whether partisan media "matters" is partly a debate about measurement.

## Key Contributions

- Systematic SCA demonstration (504 specifications) that measurement decisions drive divergent conclusions in the partisan media–polarization literature.
- Distinguishes the practical consequences of three scoring paradigms—analytic content-based, holistic content-based, and audience-based media partisanship scores (MPS)—and clarifies which suits which research question.
- Exposes partisan asymmetries (stronger conservative-side associations) that bipolar and difference scores conceal.
- Offers best-practice recommendations: justify measurement by research question, run sensitivity analyses, and report both bipolar and disaggregated component results.

## Methods

Original three-wave panel survey fielded via YouGov (Sept–Oct 2020); wave 1 n = 1,800 quota-matched to U.S. adults, with 1,401 reinterviewed. Media use was captured via the list-frequency technique across 63 outlets. The authors compiled 17 published MPS spanning the three scoring families, imputed them to respondents, and combined them into 42 IV specifications (weighted/unweighted, continuous/categorical). Twelve DV specifications covered nine affective polarization measures (feeling thermometers and trust toward Trump, Biden, and their supporters) plus three belief-polarization (misperception) measures. SCA via the R package `specr` ran all 504 IV × DV combinations with variance decomposition and controls, plus robustness checks excluding Independents and lagged-DV longitudinal models.

## Findings

- Most specifications yielded positive, significant relationships: more conservative diets predicted greater Trump favorability/trust and Trump-favoring misperceptions.
- Coefficient magnitudes varied widely (mean b = .33); largest b = .47 vs. smallest b = .07.
- Audience-based MPS produced the largest estimates (M = .35); analytic content-based the smallest (M ≈ .21–.26); holistic in between (M = .33).
- MPS choice accounted for 56% of coefficient variance; DV choice for 42%.
- Trust (M = .37) and misperception (M = .35) measures yielded stronger coefficients than feeling thermometers (M = .30).
- Disaggregation revealed asymmetry: conservative diets (M = .24) associated more strongly than liberal diets (M = −.19); centrist diets only weakly negative (M = −.05).
- Lagged longitudinal analyses produced consistently small coefficients with far less variation.

## Connections

This paper sits at the intersection of the partisan-media-and-polarization debate and the "researcher degrees of freedom" methodological turn; its concern with measurement validity connects it to work reassessing how exposure and slant are operationalized, such as [[Balluff2026-bv]] and the broader audience-versus-content-scoring questions raised in [[Bakshy2015-rn]]. Its use of specification curve analysis to stress-test a substantive controversy makes it a methodological companion to studies probing the robustness of polarization estimates like [[Ventura2026-yc]] and [[Stagnaro2025-pz]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schemer2026-mh.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
