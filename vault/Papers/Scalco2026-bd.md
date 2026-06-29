---
title: "How to detect information voids using longitudinal data from social media and web searches"
aliases: ["How to detect information voids using longitudinal data from social media and web searches"]
authors: ["Irene Scalco", "Francesco Gesualdo", "Roy Cerqueti", "Matteo Cinelli"]
year: 2026
doi: 
bibtex_key: Scalco2026-bd
topics: [information-disorder, health-information-online]
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

This paper introduces a quantitative pipeline for detecting "information voids" — periods when the supply of reliable content fails to meet public demand on a topic — by combining longitudinal data from social media platforms, news archives, and search/encyclopedia behavior. The authors define an "information delta" between rescaled supply and demand signals, decompose it via STL, and flag anomalies using an IQR rule on the remainder. Applied to COVID-19 vaccine discourse across six European countries (Jan 2020 – Apr 2021), the method identifies persistent voids around major vaccine events and shows these voids coincide with degraded content credibility and increased misinformation, moving the concept of "data voids" from qualitative description toward an operational, mechanistic construct.

## Key Contributions

- A replicable, multi-platform pipeline for operationalizing and detecting information voids from longitudinal supply/demand time series.
- A five-regime taxonomy of ecosystem states: **Void, Lack, Balance, Abundance, Overabundance**.
- Empirical evidence that voids are associated with lower-credibility content and higher misinformation prevalence, supporting their role in mechanistic accounts of misinformation emergence.
- A domain-agnostic methodology validated on both synthetic time series and a real-world COVID-19 vaccine case study.

## Methods

- **Supply proxies:** Facebook (CrowdTangle), Twitter (v2 academic API), news articles (GDELT). **Demand proxies:** Wikipedia page-views and Google Trends.
- Keyword-based collection on five vaccine brands across DK, FR, DE, IT, ES, UK (Jan 2020 – Apr 2021).
- Time series rescaled by expected value, differenced into an "information delta," then STL-decomposed; anomalies flagged via IQR on the remainder.
- Synthetic validation with injected Gaussian anomalies (1σ–15σ) measuring precision and F1.
- NewsGuard credibility scores (0–100) used to compare content quality across non-anomaly, void, and overabundance periods.

## Findings

- On synthetic data, precision >90% for anomalies above 6σ and F1 >0.68 above 9σ.
- Anomalous days made up ~7.9%–9.9% of the period across countries/platforms, with country-level asymmetries between positive and negative anomalies.
- Voids persisted longer than overabundance episodes — up to 29 consecutive days (e.g., Sputnik V on Twitter in Germany; Moderna on Facebook in Italy).
- Cumulative anomalies spiked around the Moderna EMA authorization and the AstraZeneca suspension (e.g., Facebook anomalies in Italy rising from 35% to 88% around the AstraZeneca event).
- During voids, highly credible content dropped (Facebook 33.7% → 20.8%; Twitter 31.6% → 23.9%) while highly unreliable content rose sharply (Twitter up to 27.3%).
- Demand–supply cross-correlations peaked at lag 0, suggesting largely synchronous ecosystem responses.

## Connections

This work sits alongside other quantitative infrastructures for measuring problematic information ecosystems, particularly cross-platform misinformation tracking and source-credibility approaches such as [[Bouchaud2026-lr]] and [[Bollenbacher2026-vz]], and complements platform-comparative studies of misinformation dynamics like [[Di-Marco2025-aa]]. Its supply–demand framing connects to attention-economy and exposure-based accounts of misinformation prevalence in [[Allen2025-ot]] and [[Bak-Coleman2026-mk]]'s [[Bak-Coleman2026-mk]] line of mechanistic ecosystem modeling, while methodologically it joins the growing toolkit of longitudinal computational social science represented by [[Minici2024-tf]] and [[Mannocci2025-ig]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Scalco2026-bd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-information-voids-where-misinformation/id1866587707?i=1000750869311)
