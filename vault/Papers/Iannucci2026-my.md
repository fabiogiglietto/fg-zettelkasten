---
title: "Statistical Detectability of Coordination"
aliases: ["Statistical Detectability of Coordination"]
authors: ["Letizia Iannucci", "Antonis Matakos", "Mikko Kivelä"]
year: 2026
doi: 
bibtex_key: Iannucci2026-my
supersedes: noauthor_undated-yy
topics: [coordinated-inauthentic-behavior, computational-network-structure-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2610.37970v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iannucci2026-my.mp3
pdf_available: true
discovery_date: 2026-11-06T16:26:05.822637Z
---

# Statistical Detectability of Coordination

> Iannucci, L., Matakos, A., & Kivelä, M. (2026). Statistical Detectability of Coordination. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2610.37970v1)

## Summary

This paper reframes the detection of coordinated inauthentic behaviour (CIB) as a rigorous two-level statistical hypothesis-testing problem rather than a graph-clustering exercise. The authors first convert pairwise tests of account co-activity into p-values, then arrange these into a score matrix in which a coordinating group manifests as a *planted submatrix*. By mapping coordination detection onto the well-studied planted-submatrix (and planted-clique) problem, they derive information-theoretic and computational detectability boundaries — impossible, hard, and easy regimes — as functions of group size, population size, and signal strength. Their central methodological argument is that a detected dense group counts as evidence of coordination only relative to an *explicit null model*, and that the choice of null model decisively shapes which operations are detectable. They further show, against common practice, that structural density of a recovered cluster is not evidence of coordination.

## Key Contributions

- A symmetric planted-submatrix formulation of CIB with shifted-exponential score entries, yielding scan, information-theoretic, sum, and spectral detectability boundaries, plus a reduction transferring the planted-clique computational lower bound to this setting.
- A new window-free, statistically grounded coordination-detection methodology that achieves higher agreement with labelled ground truth than previously reported methods.
- Systematic evaluation of four explicit null models across 26 labelled information operations, surfacing assumptions usually left implicit.
- A theoretical proof that combining *M* independent modalities lowers every detection threshold by a factor of 1/√M, grounding prior empirical claims that multimodality helps.
- A demonstration that density and significant permutation tests are poor proxies for recovering an operation, plus identification of a likely sampling bias in existing benchmark datasets.

## Methods

Account activity is modelled across 7 modalities (hashtags, URL sharing, mentions, replies to posts/accounts, reposts of posts/accounts), each defining a co-action layer graph whose edges link accounts acting on the same item. A window-free temporal statistic based on mean inter-action intervals between co-acting pairs produces item-level Monte Carlo p-values (B=100), combined across shared items via Fisher's method. Four null models randomise timestamps while preserving different structure: uniform-modality, uniform-account, account-activity (hourly/day-of-week profile), and item-virality (adoption curves). P-values are transformed into centred scores Y = −log(p) − 1 (mean 0, variance 1 under the null), with coordinated pairs modelled as Beta(λ,1) p-values and the group as a symmetric planted submatrix. Detection boundaries are derived analytically, then empirically compared against recovery by two greedy heuristics and a spectral method on 26 labelled operations, evaluated with F1, hypergeometric "beats chance" tests, and density permutation tests.

## Findings

- Predicted regimes depend strongly on the null model: the easy regime covers 36% of layers under item-virality, 54% under account-activity, 81% under uniform-account, and 84% under uniform-modality.
- A calibration–discrimination trade-off exists: null models that attribute more timing structure to chance are better calibrated for controls but absorb coordination signal, while simpler nulls separate coordinated pairs more strongly yet leave organic synchrony.
- The spectral method (given the labelled group size) outperforms all previously evaluated methods on the same operations, with the highest median F1 (0.62) for reposts under the uniform-account null.
- Combining modalities moves most operations into the easy regime and reduces null-model dependence, but the gain is below 1/√M because pairs appear in only ~1.34 layers on average and modalities engage different account subsets.
- Permutation tests find dense sets in nearly all layers regardless of regime — recovered sets are often denser than the real operation yet dominated by control accounts (precision as low as 0.04–0.22), confirming density is not evidence of recovery.
- The counterintuitive success of the *simplest* null models suggests a sampling artefact: benchmark operation accounts are not actually hiding within organic timing patterns, hinting at platform detection or data-collection bias.

## Connections

This work is a theoretical and methodological companion to the authors' own benchmarking of coordination-detection methods [[Iannucci2025-eg]], which the paper extends by showing *why* and *when* detection succeeds. Its critique of density-based and community-detection pipelines connects to the broader coordinated-behaviour literature represented by [[Nizzoli2020-cf]], [[Starbird2019-qv]], [[Luceri2025-tr]], and [[Giglietto2020-9d8acdd7]], while its insistence on explicit null models and detectability limits offers a principled statistical foundation these approaches often leave implicit.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iannucci2026-my.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-dense-clusters-arent-evidence-rethinking/id1866587707?i=1000800566620)
