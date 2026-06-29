---
title: "Effects of antivaccine tweets on COVID-19 vaccinations, cases, and deaths"
aliases: ["Effects of antivaccine tweets on COVID-19 vaccinations, cases, and deaths"]
authors: ["John Bollenbacher", "Filippo Menczer", "John Bryden"]
year: 2026
doi: 10.1140/epjds/s13688-025-00606-1
bibtex_key: Bollenbacher2026-vz
topics: [health-information-online, information-disorder]
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

Bollenbacher, Menczer, and Bryden ask whether antivaccine content on Twitter causally reduced COVID-19 vaccine uptake — and downstream cases and deaths — in US counties during the 2021 vaccine rollout. They build SIRVA, a compartmental epidemic model that augments SIR with a vaccinated compartment and a hesitancy compartment whose conversion rate depends on per-capita exposure to geolocated antivaccine tweets propagated through a county-to-county retweet network. Combining Bayesian inference with a causal graphical model, they estimate that roughly 14,000 Americans refused vaccination because of Twitter antivaccine exposure between February and August 2021, producing at least ~545 additional cases and ~8 additional deaths. The paper's central contribution is methodological: a mechanistic bridge from platform-level speech to aggregate epidemic outcomes that goes beyond intention-based experiments and correlational hesitancy studies.

## Key Contributions

- Observational causal evidence linking online antivaccine exposure to *realized* vaccination behavior and downstream epidemiological harm, not just stated intentions.
- The SIRVA model, which embeds an exposure-driven hesitancy compartment into a standard SIR framework.
- Integration of Bayesian epidemic fitting (NumPyro/NUTS) with do-calculus to derive an interpretable Average Treatment Effect of online content on vaccination rates.
- A reproducible pipeline — RoBERTa antivaccine classifier, county-level retweet exposure measure, MCMC inference — usable for other speech-to-outcome public health questions.
- Quantitative lower-bound harm estimates relevant to platform moderation and public health communication policy.

## Methods

The authors trained a RoBERTa classifier (F1 ≈ 0.74) on ~6,200 annotated tweets to identify antivaccine content in the CoVaxxy corpus (Feb–Aug 2021). They constructed county-level per-capita exposure by routing antivaccine tweet volumes through a county-to-county COVID retweet network. SIRVA was fit per county and globally via Bayesian MCMC to CDC case, death, and vaccination time series, with hesitancy conversion γ = γ_p + γ_e·E. Causal graphical modeling yielded an ATE of exposure on vaccinations. Model comparison used PSIS-LOO against SIRV, a static-hesitancy variant, and a word-of-mouth alternative; robustness checks included county-shuffle nulls and a comparison with Meta's Social Connectedness Index to rule out generic social-tie confounds.

## Findings

- The exposure-to-hesitancy coefficient γ_e is ≈ 0.18 (95% CI 0.15–0.22; p = 0.0002), clearly distinguishable from zero.
- ATE of exposure on vaccination rate ≈ −3.2×10⁻⁴ vaccinations per daily antivaccine tweet per capita.
- Estimated 14,086 (95% CI 11,414–16,759) Twitter-attributable vaccine refusals, against ~27 million Americans becoming hesitant overall — i.e., Twitter is a meaningful but minority channel.
- ~545 additional cases and ~8 additional deaths attributable to those refusals, treated as a lower bound.
- SIRVA beats SIRV in ELPD-LOO by roughly three standard errors, supporting an explicit hesitancy dynamic.
- Shuffling exposure across counties eliminated the effect; the COVID retweet network is uncorrelated with Meta's Social Connectedness Index, arguing against generic social-network confounding.

## Connections

This paper is the causal/epidemic-outcomes counterpart to platform-level audits of vaccine misinformation exposure such as [[DeVerna2025-dl]], and complements work on which actors and content drive antivaccine narratives like [[Efstratiou2026-ij]]. It also speaks to broader debates over the real-world impact of misinformation exposure summarized in [[Budak2024-ef]] and [[Gonzalez-Bailon2024-rq]], offering a mechanistic, harm-quantified data point in a literature that often finds exposure effects to be small or diffuse.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bollenbacher2026-vz.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-antivax-tweets-how-misinformation/id1866587707?i=1000748625004)
