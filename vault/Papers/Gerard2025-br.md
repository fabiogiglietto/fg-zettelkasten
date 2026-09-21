---
title: "Bridging the narrative divide: Cross-platform discourse networks in fragmented ecosystems"
aliases: ["Bridging the narrative divide: Cross-platform discourse networks in fragmented ecosystems"]
authors: ["Patrick Gerard", "Hans W. A. Hanley", "Luca Luceri", "Emilio Ferrara"]
year: 2025
doi: 
bibtex_key: Gerard2025-br
topics: [computational-network-structure-analysis, coordinated-inauthentic-behavior]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2505.21729v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gerard2025-br.mp3
pdf_available: true
discovery_date: 2025-05-15T00:00:00Z
---

# Bridging the narrative divide: Cross-platform discourse networks in fragmented ecosystems

> Gerard, P., Hanley, H. W. A., Luceri, L., & Ferrara, E. (2025). Bridging the narrative divide: Cross-platform discourse networks in fragmented ecosystems. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2505.21729v1)

## Summary

This paper introduces **Cluster Affiliation Network Embedding (CANE)** and its temporal extension **t-CANE**, a platform-agnostic framework for reconstructing user-user discourse networks. Rather than relying on platform-specific behavioral signals like reposts or follower ties — increasingly unavailable due to API restrictions and platform fragmentation — the method links users through shared participation in latent narrative clusters derived from content. The authors benchmark the approach against interaction- and similarity-based baselines across information operation detection, ideological stance prediction, and a new cross-platform engagement prediction task, achieving state-of-the-art results with far less data. Applied to Truth Social and X during the 2024 U.S. Presidential election, the framework surfaces a tiny set of "bridge users" who seed the majority of narratives that migrate between platforms, reframing cross-platform influence as a structural phenomenon rooted in shared discursive alignment rather than direct interaction.

## Key Contributions

- A platform-agnostic, content-driven framework (CANE and temporal t-CANE) for building user-user discourse networks from latent narrative participation instead of platform behavioral signals.
- A novel **cross-platform engagement prediction** benchmark testing whether user graphs encode behavioral alignment across fragmented ecosystems.
- Empirical evidence that 2024 U.S. election narrative diffusion between Truth Social and X was structured, directional, and concentrated in a small subset of bridge users.
- A theoretical bridge linking computational discourse network analysis to classic sociological concepts (Granovetter's weak ties, Gould and Fernandez's brokers, boundary spanners).
- Released anonymized code and datasets, including a cross-platform Truth Social/X corpus with narrative cluster annotations.

## Methods

- Posts embedded with MPNet (768-dim), then clustered into latent narratives using DP-Means with a cosine threshold (λ≈0.65).
- User-user graphs built from TF-IDF-weighted cluster affiliation vectors via cosine similarity, accelerated with FAISS-HNSW approximate nearest-neighbor search; **t-CANE** adds a Hawkes-process-inspired memory update over discrete timesteps.
- Benchmarks: state-backed IO detection (China and Iran datasets) with node2vec + random forest; ideological stance prediction on X and TikTok using GCN/node2vec structure-only classifiers; and a new cross-platform engagement prediction task on X + Truth Social (May–Nov 2024, 321 narrative themes) with GCNs.
- Narrative migration analyzed via Transfer Entropy with permutation tests; Louvain community detection plus Shannon entropy to locate mixed-platform "bridge zones."
- Validation via human evaluation of clustering, two-stage de-duplication, k-NN matched-pair engagement comparisons, and fear-speech classification.

## Findings

- t-CANE achieves top performance across tasks (e.g., F1 0.83/AUC 0.98 on China IO; F1 0.35/AUC 0.94 on cross-platform engagement vs. best baseline F1 0.11/AUC 0.64).
- CANE/t-CANE reach 95% of peak AUC with only 5–10% of available content data — far more data-efficient than baselines.
- Of 1,552 narratives showing cross-platform migration, 238 (15.3%) exhibit statistically significant directional diffusion; Truth Social is overrepresented as origin by ~11–14× relative to its post share.
- Truth Social-seeded narratives contain significantly more fear-laden language than X-originating ones (log-odds +0.22, ~22.5% relative increase).
- A single high-entropy discourse community of 2,864 users (0.33% of users, 2.14% of posts) is the first cross-platform carrier for ~68–69% of migrating narratives; just 122 users account for all earliest introductions of Truth Social narratives into X, and 4 users for ~25%.
- Narratives with early bridge-user engagement receive significantly more likes, replies, and reposts than matched controls, even for low-virality narratives.
- Ablations confirm TF-IDF weighting beats raw count and softmax, and FAISS-HNSW matches brute-force similarity at far lower cost.

## Connections

This work sits within the coordinated inauthentic behavior literature through its IO-detection benchmarks and shares the cross-platform diffusion focus of related studies of narrative migration and multi-platform coordination such as [[Ng2026-og]] and [[Kansaon2025-id]]. Its methodological emphasis on structure-only, content-driven network construction connects to other computational network-structure analyses of influence and community detection like [[Luceri2025-tr]] and [[Minici2024-tf]], while its bridge-user brokerage framing resonates with structural accounts of cross-cutting exposure and platform ecosystems in works such as [[Bakshy2015-rn]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gerard2025-br.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-bridging-the-narrative-divide/id1866587707?i=1000743818440)
