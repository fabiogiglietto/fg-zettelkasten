---
title: "Information pathways in online science communication: The role of platform actors and news media"
aliases: ["Information pathways in online science communication: The role of platform actors and news media"]
authors: ["Alexandros Efstratiou", "Giuseppe Russo", "Luca Luceri"]
year: 2026
doi: 
bibtex_key: Efstratiou2026-ij
topics: [coordinated-inauthentic-behavior, information-disorder-disinformation]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2603.17249v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Efstratiou2026-ij.mp3
pdf_available: true
discovery_date: 2026-03-22T16:51:47.195162Z
---

# Information pathways in online science communication: The role of platform actors and news media

> Efstratiou, A., Russo, G., & Luceri, L. (2026). Information pathways in online science communication: The role of platform actors and news media. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2603.17249v1)

## Summary

This paper offers a holistic, multi-level analysis of how COVID-19 scientific papers circulate across Twitter and news media, examining the distinct and intersecting roles of organic users, bots, superspreaders, coordinated accounts, and news outlets. Drawing on 1.24M tweets and 211k news articles referencing pandemic preprints, the authors find a predominantly contrarian coordinated retweet network that amplifies a small set of credentialed anti-consensus experts, in contrast to mainstream superspreaders who are largely pro-consensus science communicators. A central claim is that news coverage of scientific papers typically *follows* rather than precedes superspreader activity on Twitter, revealing a Twitter-to-news information pathway, with high-trust outlets aligning with conformist superspreaders and low-trust outlets with contrarian ones.

## Key Contributions

- A joint, multi-level characterization of online science communication analyzing coordinated networks, superspreaders, bots, and news media together rather than in isolation.
- Empirical evidence that grassroots coordination can centralize influence around perceived experts, offering a mechanism behind documented false-consensus and expert-centralization effects in anti-science communities.
- Documentation of a Twitter-to-news temporal pathway in science dissemination, complicating assumptions about news-driven attention cycles.
- A demonstration that coordination is distinct from automation—coordinated behavior here is not bot-driven.
- A reusable methodological template combining co-retweet detection, h-index superspreader identification, kernel density precedence analysis, and outlet trust binarization.

## Methods

Using a dataset of 25k+ bioRxiv/medRxiv COVID-19 preprints with 1.24M tweets (346k users) and 211k news articles (2.34k outlets) through November 2022, the authors build co-retweet similarity networks (30-minute windows, TF-IDF, cosine similarity, eigenvector centrality thresholds). Superspreaders were identified via an h-index metric (top 1%, N=764); bots were scored with Botometer. Comparisons used bootstrapped t-tests and chi-squared tests against random samples. Topics were extracted with BERTopic, tweet emotions with a DistilRoBERTa classifier, and superspreaders were manually annotated into credential categories. Cross-platform alignment was measured via cosine similarity between superspreader and outlet DOI vectors with KNN analysis, and Gaussian kernel density estimation over paper mentions built directed precedence networks between actor classes, with outlet credibility binarized via Youden's J on trust scores.

## Findings

- The coordinated network is almost entirely contrarian (96.4%), younger, and topically narrower (Gini=0.80 vs. 0.69 overall); 90.4% of its retweeted content originates from contrarian accounts.
- Coordinated amplification targets contrarian *credentialed experts* who are not the most popular overall (top-promoted accounts ranked 37th–385th).
- Bot scores do not differ significantly between coordinated and non-coordinated accounts—coordination is not automation.
- Superspreaders are predominantly conformist (80.6%), more verified (28% vs. 1.8%), and 60% of conformists are physicians/scientists; contrarian superspreaders are more often non-credentialed (55.4%).
- Conformist superspreaders express the most fear (50.4%), while contrarian superspreaders are paradoxically the most neutral.
- Six coordinated subclusters emerged around vaccines/boosters, viral mutations, excess deaths, and T-cell immunity narratives.
- Contrarian superspreaders align strongly with low-credibility (conspiratorial/pseudoscientific) outlets; conformists align with high-trust mainstream/medical sources.
- Both superspreader types significantly precede news coverage (median lag ~19–28 hours), with no significant precedence ordering between outlet types.

## Connections

This paper builds directly on prior superspreader and coordination-detection methods and sits alongside broader work on coordinated inauthentic behavior detection such as [[Luceri2025-tr]] and [[Minici2024-tf]]. Its focus on health-related contrarian amplification connects to studies of health misinformation networks and polarized scientific discourse like [[Di-Marco2025-aa]]. Its finding that coordination is distinct from automation contributes to ongoing debates on how organic coordination differs from bot-driven amplification across the CIB literature.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Efstratiou2026-ij.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-who-really-drives-science-talk-online/id1866587707?i=1000756731148)
