---
title: "Information pathways in online science communication: The role of platform actors and news media"
aliases: ["Information pathways in online science communication: The role of platform actors and news media"]
authors: ["Alexandros Efstratiou", "Giuseppe Russo", "Luca Luceri"]
year: 2026
doi: 
bibtex_key: Efstratiou2026-ij
topics: [coordinated-inauthentic-behavior, health-information-online]
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

This paper offers a multi-actor account of how COVID-19 scientific papers circulate across Twitter and news media, jointly analyzing organic users, bots, superspreaders, coordinated accounts, and news outlets rather than studying them in isolation. Drawing on 1.24M tweets and 211k news articles referencing pandemic-era preprints, the authors show that a predominantly contrarian coordinated retweet network amplifies a narrow set of credentialed anti-consensus experts, while mainstream superspreaders are largely pro-consensus physicians and scientists. Crucially, news coverage of scientific papers tends to *follow* superspreader activity on Twitter — with high-trust outlets aligning with conformist superspreaders and low-trust outlets with contrarian ones — suggesting a platform-to-news information pathway in science communication.

## Key Contributions

- A holistic, multi-level characterization of online science communication integrating coordinated networks, superspreaders, bots, and news outlets.
- Empirical evidence that grassroots coordination centralizes influence around *perceived experts*, providing a mechanism for false consensus and expert centralization in anti-science communities.
- Documentation of a Twitter-to-news temporal precedence in science dissemination, complicating news-driven attention narratives.
- Disentangles coordination from automation: bot scores do not distinguish coordinated from non-coordinated accounts.
- A reusable methodological pipeline combining co-retweet networks, h-index superspreader detection, kernel-density precedence analysis, and outlet trust binarization.

## Methods

The authors use a dataset of 25k+ bioRxiv/medRxiv preprints, 1.24M tweets from 346k users, and 211k articles from 2.34k outlets through Nov 2022. They construct co-retweet similarity networks (30-min windows, TF-IDF, cosine similarity, eigenvector centrality cutoffs at top 1%), detect superspreaders via the h-index metric (top 1%, N=764), and score automation with Botometer. Statistical tests use bootstrapped t-tests and chi-squared against random samples. They apply BERTopic for paper topics, DistilRoBERTa for emotion classification, and manual annotation of superspreader credentials. Outlet alignment is measured via cosine similarity over DOI vectors with KNN; temporal precedence is estimated by Gaussian KDE on per-paper mention activity, with outlets binarized into high/low credibility via Youden's J on external trust scores.

## Findings

- The coordinated network is 96.4% contrarian, younger on average, and topically narrower (Gini=0.80 vs. 0.69) than the broader network; six subclusters cover vaccines/boosters, mutations, excess mortality, and T-cell immunity.
- 90.4% of content retweeted by coordinated accounts comes from contrarian sources; 78.4% of contrarian superspreaders are amplified vs. only 14.6% of conformist ones.
- Coordinated amplification targets contrarian credentialed experts who are *not* the most popular overall (ranked 37th–385th).
- Superspreaders are 80.6% conformist, with 60% being physicians or scientists; contrarian superspreaders are more often non-credentialed (55.4%).
- Emotion patterns are counter-intuitive: conformist superspreaders express the most fear (50.4%), contrarian superspreaders are the most emotionally neutral, and random contrarians dominate anger/sadness.
- Contrarian superspreaders align more tightly with low-credibility/pseudoscientific outlets than conformist superspreaders do with mainstream outlets.
- Both superspreader types precede news coverage by ~19–28 hours; no significant precedence between high- and low-credibility outlets.
- Bot scores do not differ significantly between coordinated and non-coordinated accounts.

## Connections

This paper builds directly on superspreader and coordinated-behavior detection methodologies that recur across the register; the co-retweet similarity approach connects naturally to [[Luceri2025-tr]] and related coordination-detection work like [[Minici2024-tf]], [[Kulichkina2026-zk]], and [[Graham2025-gp]]. Its focus on contrarian health discourse and perceived experts links it to problematic-health-information studies such as [[Schroeder2026-im]], [[Poliakoff2026-fa]], and [[Di-Marco2025-aa]], while its decoupling of coordination from automation echoes themes in [[Yang2025-iv]] and [[Bollenbacher2026-vz]]. The Twitter-to-news precedence finding extends cross-platform information-flow concerns also visible in [[Kansaon2025-id]] and [[Gerard2025-br]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Efstratiou2026-ij.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-covid-conspiracies-how-social-media/id1866587707?i=1000756731148)
