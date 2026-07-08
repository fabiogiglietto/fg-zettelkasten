---
title: "Representativeness and response validity across nine opt-in online samples"
aliases: ["Representativeness and response validity across nine opt-in online samples"]
authors: ["Michael Nicholas Stagnaro", "James Druckman", "Adam J. Berinsky", "Antonio Alonso Arechar", "Robb Willer", "David Gertler Rand"]
year: 2025
doi: 10.31234/osf.io/h9j2d_v2
bibtex_key: Stagnaro2025-pz
topics: [survey-methodology-validity]
citation_count: 1
open_access: false
source_url: https://doi.org/10.31234/osf.io/h9j2d_v2
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Stagnaro2025-pz.mp3
pdf_available: true
discovery_date: 2026-03-19T18:07:58.545277Z
---

# Representativeness and response validity across nine opt-in online samples

> Stagnaro, M. N., Druckman, J., Berinsky, A. J., Arechar, A. A., Willer, R., & Rand, D. G. (2025). Representativeness and response validity across nine opt-in online samples. *PsyArXiv*. https://doi.org/10.31234/osf.io/h9j2d_v2
>
> [View paper](https://doi.org/10.31234/osf.io/h9j2d_v2)

## Summary

This paper provides a head-to-head empirical comparison of nine widely used opt-in online survey platforms (N=13,053), evaluating each on response validity (attention, effort, honesty, speeding, attrition), representativeness against the 2020 ANES benchmark, and respondent professionalism. The authors document a central trade-off: samples that rely on demographic quotas (notably Lucid and Forthright) better approximate the population — including on non-demographic attitudes — but exhibit weaker response validity, largely because their respondents disproportionately use mobile phones. They show that two trivial front-end attention checks substantially improve validity without harming representativeness, and that post-stratification weights can recover average treatment effects but not heterogeneous ones. The paper argues that opt-in samples should not be treated as a homogeneous category, and offers decision-oriented guidance for matching platform to research goal.

## Key Contributions

- A comprehensive, identical-instrument comparison of nine major opt-in platforms (Lucid, Prolific, CloudResearch Connect, Forthright, CR Toolkit, CRSTAL, Open MTurk, and two "NR" variants) on three distinct quality dimensions.
- Documentation of a systematic representativeness–validity trade-off, with mobile-phone usage identified as a plausible mechanism.
- Empirical demonstration that two simple attention checks at the start of a survey are a near-free intervention that raises validity without distorting demographics.
- Evidence that survey weights restore average treatment effects but fail to recover heterogeneous treatment effects in non-representative samples.
- Practical guidelines for platform selection by research purpose, and a clear recommendation against using Open MTurk.

## Methods

The authors fielded an identical survey on nine platforms (June 2022–Nov 2023) under each platform's standard quota and payment defaults. The instrument included demographics, attitude items, seven attention checks, an effort task, an honesty self-report, speeding/attrition indicators, platform-experience questions, and two canonical replication experiments (welfare/poor framing; Asian-disease risky-choice framing). They built an aggregate response-validity index, measured representativeness as summed absolute deviations from ANES benchmarks (overall and by partisanship), and tested heterogeneous treatment effects via ordinal logistic and logistic regressions. Within-platform "NR" comparisons (e.g., Prolific vs. Prolific NR) isolated quota effects from platform effects, and they evaluated the consequences of attention-check filtering and post-stratification weighting.

## Findings

- Samples fall into three validity tiers: high (Connect, Connect NR, Prolific, Prolific NR, CRSTAL), middle (Forthright, CR Toolkit), and low (Lucid, Open MTurk).
- Two front-end attention checks raised mean validity from .771 to .822, with the largest gains in the lowest-validity samples.
- Quota-based samples (Lucid, Forthright) most closely matched ANES on both demographics and attitudes, though all samples deviated more for Republicans and on gun control specifically.
- Filtering on up to two attention checks did not appreciably damage representativeness; Lucid was most sensitive at higher filter levels.
- The welfare/poor framing main effect replicated everywhere, but partisan, racial, and age moderation appeared only in the more representative samples.
- The risky-choice framing effect replicated uniformly with no demographic moderation, suggesting cognitive paradigms are less sample-sensitive.
- Weights recovered main effects (even on Open MTurk) but did not recover heterogeneous treatment effects.
- Professional respondents concentrated in less representative samples and had higher validity; representative samples leaned heavily on mobile respondents (~70% on Lucid/Forthright vs. <10% elsewhere).
- Expected demographic-attitude correlations (e.g., Black ideology/party alignment, male skew in Trump support) appeared only in more representative samples, hinting at possible identity misreporting in less representative ones.
- Open MTurk was dominated on essentially every dimension.

## Connections

No other papers are currently catalogued under shared topics, so there are no internal wikilinks to make. Conceptually, this work extends the lineage of methodological audits of online samples (Berinsky et al., Coppock, Mullinix et al., Peer et al.) and speaks to ongoing debates about when convenience samples suffice for causal inference and when they mislead — particularly for heterogeneous treatment effect estimation.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Stagnaro2025-pz.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-online-samples-are-your-participants/id1866587707?i=1000756199554)
