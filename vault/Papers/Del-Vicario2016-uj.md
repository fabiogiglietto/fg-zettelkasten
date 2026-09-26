---
title: "The spreading of misinformation online"
aliases: ["The spreading of misinformation online"]
authors: ["Michela Del Vicario", "Alessandro Bessi", "Fabiana Zollo", "Fabio Petroni", "Antonio Scala", "Guido Caldarelli", "H. Eugene Stanley", "Walter Quattrociocchi"]
year: 2016
doi: 10.1073/pnas.1517441113
bibtex_key: Del-Vicario2016-uj
topics: [political-polarization-partisanship, misinformation-exposure-recalibration]
citation_count: 1854
open_access: false
source_url: https://doi.org/10.1073/pnas.1517441113
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445413Z
---

# The spreading of misinformation online

> Vicario, M. D., Bessi, A., Zollo, F., Petroni, F., Scala, A., Caldarelli, G., Stanley, H. E., & Quattrociocchi, W. (2016). The spreading of misinformation online. *Proceedings of the National Academy of Sciences*, *113*, 554–559. https://doi.org/10.1073/pnas.1517441113
>
> [View paper](https://doi.org/10.1073/pnas.1517441113)

## Summary

This paper offers large-scale quantitative evidence that misinformation spreads on Facebook primarily through homogeneous, polarized communities — "echo chambers" — formed by selective exposure and confirmation bias. Analyzing five years (2010–2014) of public Facebook data across 67 pages, the authors contrast two distinct narrative types, scientific news and conspiracy theories, and characterize how each is consumed and diffused. They argue that social homogeneity, rather than content quality, is the preferential driver of information cascades, and support this with a data-driven percolation model showing that homogeneity and polarization are the main determinants of cascade size. A notable implication is that purely algorithmic countermeasures (e.g., trustworthiness scores) may be ill-suited to a problem rooted in social psychology.

## Key Contributions

- Large-scale empirical demonstration that echo chambers form around distinct narratives (science vs. conspiracy), each with its own cascade dynamics.
- Introduction of formal measures of user polarization (σ) and edge homogeneity (σij) to quantify social similarity in diffusion.
- A data-driven percolation/branching-process model on a signed small-world network that predicts cascade size from homogeneity and polarization.
- Empirical linkage of confirmation bias and social homogeneity to misinformation spreading, reframing debates on countermeasures.

## Methods

The authors collected public Facebook data via the Graph API across 32 conspiracy-theory pages, 35 science-news pages, and 2 troll pages (used as a benchmark for model fitting). They reconstructed "sharing trees" to characterize cascade size, height, and lifetime, and defined user polarization and edge homogeneity to measure similarity between sharing users. Statistical analysis included power-law fitting of cascade-size distributions, PDFs/CCDFs of lifetime and homogeneity, and Kolmogorov–Smirnov tests. A percolation model on a Watts–Strogatz signed network (n=5,000 nodes, m=1,000 news items) was parameterized by sharing threshold, fraction of homogeneous links, and rewiring probability, validated against 1,072 troll-page sharing trees.

## Findings

- Cascade size and maximum degree are power-law distributed for all content types (exponents ≈ 2.21 science, 2.47 conspiracy, 2.44 trolling), with maximum cascades of 952, 2,422, and 3,945 respectively.
- Cascade lifetimes are similar across categories, peaking around 1–2 h and ~20 h; roughly 40% of content diffuses within 5 h.
- Science news reaches high diffusion quickly with no lifetime–size relation, while conspiracy rumors assimilate slowly and show a positive lifetime–size relation.
- Mean-edge homogeneity is almost always ≥ 0, indicating content circulates primarily within homogeneous echo chambers.
- Larger science cascades correspond to high homogeneity (0.5–0.8), larger conspiracy cascades to lower homogeneity (~0.25), yet homogeneity remains the underlying driver.
- The percolation model reproduces observed dynamics; ϕHL ≈ 0.5–0.56 splits the network into two isolated echo chambers (best fit ϕHL=0.56, r=0.01, δ=0.015).

## Connections

This is a foundational echo-chamber study whose confirmation-bias mechanism is challenged and refined by later exposure-measurement work such as [[Bakshy2015-rn]], [[Guess2021-ym]], and [[Gonzalez-Bailon2023-uy]], which question how prevalent algorithmically-driven echo chambers actually are. Its account of cascade dynamics is a direct counterpart to [[Vosoughi2018-at]] on how falsehoods spread, and its polarization framing connects to broader partisan-sorting literature including [[Iyengar2019-jj]] and [[Osmundsen2021-et]].
