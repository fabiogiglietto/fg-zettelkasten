---
title: "Statistical detectability of coordination"
aliases: ["Statistical detectability of coordination"]
authors: ["Letizia Iannucci", "Antonis Matakos", "Mikko Kivelä"]
year: 2026
doi: 
bibtex_key: noauthor_undated-yy
topics: [coordinated-inauthentic-behavior, computational-network-structure-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2610.37970v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/noauthor_undated-yy.mp3
pdf_available: false
discovery_date: 2026-11-03T18:30:29.287158Z
---

# Statistical detectability of coordination

> Iannucci, L., Matakos, A., & Kivelä, M. (2026). Statistical detectability of coordination. *arXiv*.
>
> [View paper](http://arxiv.org/abs/2610.37970v1)

## Summary

This paper interrogates a foundational assumption in coordinated-inauthentic-behavior research: that dense subgraphs or behavioural clusters in account-similarity networks constitute evidence of genuine coordination. The authors argue that standard detection pipelines — which project account-entity interactions into similarity networks based on temporal proximity, shared actions, or behavioural overlap — tend to surface co-activated accounts or forcibly partition *all* users into clusters, regardless of whether real coordination is present. The central reframing is to treat coordination detection as a problem of **statistical detectability**: under what conditions can coordinated activity be distinguished from ordinary or incidental co-activity, and where do the statistical limits of that distinction lie?

## Key Contributions

- Reframes coordination detection as a question of statistical detectability rather than simple co-activity identification.
- Critiques the methodological assumptions underlying similarity-network and clustering-based approaches, which can manufacture "coordinated" groups out of noise.
- Argues that the detectability of coordination has intrinsic statistical limits that should be characterised explicitly rather than assumed away.

## Methods

The work analyses the common coordination-detection pipeline: account-entity interactions are projected into account-similarity networks (weighted by temporal proximity, action counts, or behavioural similarity), after which dense-subgraph detection or behavioural clustering identifies putative coordinated groups. The authors examine how these steps behave when applied to data lacking genuine coordination, exposing the gap between detecting similarity and establishing coordination.

## Findings

- Prevailing methods identify co-activated accounts or forcibly cluster all users — neither of which establishes that true coordination exists.
- Detected structure must be assessed against a null expectation to determine whether it is statistically distinguishable from incidental similarity.
- (The provided abstract is truncated; detailed quantitative results beyond the critique of co-activation and clustering methods are not available in the summary.)

## Connections

This paper extends the authors' own prior critical line of work on coordination detection [[Iannucci2025-eg]], and speaks directly to the broad similarity-network and clustering tradition exemplified by [[Nizzoli2020-cf]] and the coordinated-link-sharing lineage [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]]. By foregrounding statistical nulls and false positives, it is in dialogue with methodological assessments of detection reliability such as [[Luceri2025-tr]] and [[Kulichkina2026-zk]], offering a cautionary foundation for the many pipeline-based detection studies in this topic area.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/noauthor_undated-yy.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
