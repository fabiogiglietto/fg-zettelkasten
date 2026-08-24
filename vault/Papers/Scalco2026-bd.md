---
title: "How to detect information voids using longitudinal data from social media and web searches"
aliases: ["How to detect information voids using longitudinal data from social media and web searches"]
authors: ["Irene Scalco", "Francesco Gesualdo", "Roy Cerqueti", "Matteo Cinelli"]
year: 2026
doi: 
bibtex_key: Scalco2026-bd
topics: [health-misinformation-networks, information-disorder-and-fact-checking]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2602.15476v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Scalco2026-bd.mp3
pdf_available: true
discovery_date: 2026-02-22T07:52:03.950374Z
---

# How to detect information voids using longitudinal data from social media and web searches

> Scalco, I., Gesualdo, F., Cerqueti, R., & Cinelli, M. (2026). How to detect information voids using longitudinal data from social media and web searches. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2602.15476v1)

## Summary

This paper introduces a quantitative pipeline for detecting and measuring **information voids** — periods when the supply of reliable content fails to meet public demand for information on a topic. Where prior work treated data/information voids qualitatively, the authors operationalize them as statistically anomalous negative imbalances between information demand (Wikipedia page-views, Google Trends) and supply (Facebook, Twitter, GDELT news). By constructing an "information delta" time series and applying STL decomposition with IQR-based anomaly detection, they classify the online information ecosystem into five regimes and identify persistent voids in COVID-19 vaccine discourse across six European countries. Crucially, they show these voids empirically coincide with degraded content quality and elevated misinformation.

## Key Contributions

- First systematic, replicable pipeline for operationalizing and detecting information voids from longitudinal, multi-platform data.
- A five-regime taxonomy of ecosystem states — **Void, Lack, Balance, Abundance, Overabundance** — grounded in demand–supply dynamics.
- Empirical evidence linking voids to reduced credible content and higher misinformation prevalence, motivating their inclusion in mechanistic models of misinformation.
- A domain-agnostic, reproducible methodology with applications to public health, politics, and crisis communication.
- Dual validation on synthetic time series and a real-world COVID-19 vaccine case study.

## Methods

The core is a data-science pipeline: rescale each supply and demand series by its expected value, compute an "information delta" (rescaled supply minus demand), decompose it via STL (Seasonal–Trend decomposition using Loess), and flag anomalies in the remainder using an IQR threshold. Supply proxies are Facebook (CrowdTangle), Twitter (v2 full-archive academic API), and GDELT news; demand proxies are Wikipedia page-views and Google Trends. Keyword collection spanned five vaccine brands across Denmark, France, Germany, Italy, Spain, and the UK (Jan 2020–Apr 2021). The pipeline was validated on synthetic Gaussian series with injected anomalies (1σ–15σ), and NewsGuard credibility scores (0–100) were integrated to compare content quality across void, overabundance, and non-anomaly periods.

## Findings

- On synthetic data, mean precision exceeded 90% above 6σ and mean F1 exceeded 0.68 above 9σ.
- Anomalous days ranged from ~7.9% to ~9.9% across countries and platforms, with country-level differences in positive vs. negative anomaly balance.
- Voids reached up to 29 consecutive days and generally outlasted overabundance episodes — evidence of asymmetric recovery dynamics.
- Cumulative anomalies spiked around key events (e.g., Moderna EMA authorization drove Facebook anomalies in Italy from 30% to 81% within a month; AstraZeneca suspension pushed them from 35% to 88%).
- During voids, highly credible content (NewsGuard = 100) fell to 20.84% (Facebook) and 23.87% (Twitter), while highly unreliable content rose to 6.1% (Facebook) and 27.28% (Twitter).
- Demand–supply cross-correlations peaked at lag 0, indicating largely synchronous ecosystem responsiveness.

## Connections

This paper contributes a measurement infrastructure to the health-misinformation and infodemic literature; it connects to work using multi-platform social-media data to trace COVID-19 misinformation dynamics such as [[Pierri2025-hm]] and to prior methodological work on coordinated and anomalous information flows exemplified by [[Giglietto2022-0e951ac5]], [[Giglietto2019-e9be81c1]], and [[Giglietto2017-4375de2f]]. Its supply–demand framing of the attention economy also complements broader accounts of misinformation credibility and circulation like [[van-der-Linden2026-jt]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Scalco2026-bd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-information-voids-where-misinformation/id1866587707?i=1000750869311)
