---
title: "Effects of antivaccine tweets on COVID-19 vaccinations, cases, and deaths"
aliases: ["Effects of antivaccine tweets on COVID-19 vaccinations, cases, and deaths"]
authors: ["John Bollenbacher", "Filippo Menczer", "John Bryden"]
year: 2026
doi: 10.1140/epjds/s13688-025-00606-1
bibtex_key: Bollenbacher2026-vz
topics: [health-misinformation-networks, information-disorder-and-fact-checking]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1140/epjds/s13688-025-00606-1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bollenbacher2026-vz.mp3
pdf_available: true
discovery_date: 2026-02-07T01:01:16.924569Z
---

# Effects of antivaccine tweets on COVID-19 vaccinations, cases, and deaths

> Bollenbacher, J., Menczer, F., & Bryden, J. (2026). Effects of antivaccine tweets on COVID-19 vaccinations, cases, and deaths. *EPJ Data Science*, *15*, 12. https://doi.org/10.1140/epjds/s13688-025-00606-1
>
> [View paper](https://doi.org/10.1140/epjds/s13688-025-00606-1)

## Summary

This paper asks whether exposure to antivaccine content on Twitter/X *causally* reduced COVID-19 vaccination uptake in US counties between February and August 2021 — and, downstream, whether it produced additional cases and deaths. The authors bridge the gap between controlled misinformation experiments (which measure intentions) and correlational studies (which cannot establish causation) by building a mechanistic epidemic model coupled to causal inference. Their central estimate is that antivaccine tweets caused roughly 14,000 vaccine refusals, translating to a lower bound of ~545 additional cases and ~8 additional deaths over the six-month window. The work argues that platform-level speech can be linked to offline public health outcomes with an interpretable, reproducible pipeline.

## Key Contributions

- Observational **causal** evidence tying online antivaccine exposure to real-world vaccination behavior, cases, and deaths — going beyond intention-based lab studies and purely correlational work.
- Introduces **SIRVA**, a compartmental epidemic model extending SIR with Vaccinated and hesitant/Antivaccine compartments, where the hesitancy conversion rate is driven partly by exogenous information exposure.
- Combines Bayesian epidemic modeling with causal graphical modeling (do-calculus) to derive an interpretable Average Treatment Effect of exposure.
- Offers an open, reproducible methodology for connecting platform speech data to offline epidemic dynamics — with implications for moderation policy and public health communication.

## Methods

The authors trained a RoBERTa classifier to detect antivaccine tweets (F1 ≈ 0.74), then constructed a county-to-county COVID retweet network to define per-capita antivaccine *exposure* propagated across counties and normalized by population. The SIRVA model adds a Vaccinated compartment and an Antivaccine/hesitant compartment (A = αS), with a conversion rate γ = γ_p + γ_e·E partly driven by exposure. Parameters were inferred per county and globally via Bayesian MCMC (NumPyro/NUTS), fitted to CDC county-level case, death, and vaccination data plus CoVaxxy tweets (Feb 6–Aug 9, 2021). Causal graphical modeling yielded the ATE. Model comparison used PSIS-LOO against SIRV and static variants; robustness checks included county-shuffle nulls and comparison against Meta's Social Connectedness Index.

## Findings

- The exposure-to-hesitancy coefficient γ_e had posterior mean ≈ 0.18 (95% CI: 0.15–0.22), significantly greater than zero (p = 0.0002).
- Estimated ATE of exposure on vaccination rate ≈ −3.2×10⁻⁴ vaccinations per daily antivaccine tweet per capita.
- An estimated 14,086 people (95% CI: 11,414–16,759) refused vaccination due to Twitter exposure, against ~27 million who became hesitant overall.
- Roughly 545 additional cases and 8 additional deaths attributed to these Twitter-induced refusals (a lower bound).
- SIRVA outperformed SIRV in ELPD-LOO by about three standard errors, indicating better out-of-sample fit.
- Shuffling exposure across counties nullified the effect, and the COVID retweet network was uncorrelated with Meta's Social Connectedness Index — supporting a platform-specific causal interpretation.

## Connections

This is one of several works in the corpus focused specifically on COVID-19 vaccine misinformation on Twitter/X; it complements [[Pierri2025-hm]], whose correlational findings on online misinformation and hesitancy this paper explicitly extends toward causal estimation, and [[DeVerna2025-dl]], which shares the CoVaxxy-style approach to studying vaccine discourse. More broadly it sits within the health-misinformation-networks literature that models how misinformation propagates and affects offline behavior.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bollenbacher2026-vz.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-antivax-tweets-how-misinformation/id1866587707?i=1000748625004)
