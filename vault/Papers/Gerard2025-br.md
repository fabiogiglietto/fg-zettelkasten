---
title: "Bridging the narrative divide: Cross-platform discourse networks in fragmented ecosystems"
aliases: ["Bridging the narrative divide: Cross-platform discourse networks in fragmented ecosystems"]
authors: ["Patrick Gerard", "Hans W. A. Hanley", "Luca Luceri", "Emilio Ferrara"]
year: 2025
doi: 
bibtex_key: Gerard2025-br
topics: [computational-methods-social-research, coordinated-inauthentic-behavior]
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

This paper proposes **Cluster Affiliation Network Embedding (CANE)** and a temporal variant **t-CANE**, a platform-agnostic method for building user-user networks from shared participation in latent narrative clusters rather than from reposts, follows, or other platform-specific signals. By embedding posts with MPNet, clustering them with DP-Means, and linking users via TF-IDF-weighted affiliation vectors (accelerated with FAISS-HNSW), the authors construct discourse networks that match or exceed interaction- and similarity-based baselines on information operation detection, ideological stance prediction, and a newly introduced cross-platform engagement prediction task — using a fraction of the data. Applied to Truth Social and X during the 2024 U.S. Presidential election, the framework uncovers a small set of "bridge users" (0.33% of users) who introduce roughly 70% of narratives that migrate between the two platforms, reframing cross-platform influence as a structural phenomenon rooted in discursive alignment rather than direct ties.

## Key Contributions

- A content-driven, platform-agnostic framework (CANE / t-CANE) for reconstructing user networks from latent narrative participation, bypassing reliance on increasingly inaccessible interaction data.
- A novel **cross-platform engagement prediction** benchmark that tests whether discourse-based graphs encode behavioral alignment across fragmented ecosystems.
- Empirical evidence that political narrative diffusion between Truth Social and X is structured, directional, and concentrated in a small bridge population.
- A theoretical link between computational discourse-network analysis and classical sociological constructs — Granovetter's weak ties, Gould–Fernandez brokers, and boundary spanners.
- Released anonymized code, datasets, and a cross-platform Truth Social/X corpus.

## Methods

Posts are embedded with MPNet and clustered into latent narratives via DP-Means (cosine threshold ≈0.65). Users are represented as TF-IDF-weighted distributions over clusters; user-user edges are computed via cosine similarity with FAISS-HNSW nearest-neighbor search. The temporal extension t-CANE applies a Hawkes-process-inspired decay over discrete timesteps. Evaluation spans (i) state-backed information operation detection on China/Iran datasets, (ii) ideological stance prediction on labeled X and TikTok 2024 election data using GCN/node2vec classifiers, and (iii) a new cross-platform engagement task over 321 narrative themes from May–Nov 2024 Truth Social/X posts. Cross-platform diffusion is analyzed with Transfer Entropy (permutation-tested), Louvain communities, Shannon entropy for identifying mixed-platform bridge zones, and a fear-speech classifier for content analysis.

## Findings

- t-CANE achieves state-of-the-art results across all tasks (e.g., F1 0.83/AUC 0.98 on China IO; F1 0.35/AUC 0.94 on cross-platform engagement vs. best baseline F1 0.11/AUC 0.64).
- CANE/t-CANE reach 95% of peak AUC using only 5–10% of available content, dramatically outperforming baselines in data efficiency.
- Of 1,552 cross-platform migrating narratives, 238 (15.3%) show statistically significant directional diffusion via Transfer Entropy; **Truth Social is overrepresented as origin by ~11–14× relative to its post share**.
- Truth-Social-originating narratives contain ~22.5% more fear-laden language than X-originating ones (log-odds +0.22, p<0.01).
- A single high-entropy community of 2,864 users (0.33% of users, 2.14% of posts) is the first carrier of ~68–69% of migrating narratives; 122 users account for all earliest introductions of Truth Social narratives into X, with 4 users responsible for ~25%.
- Narratives where bridge users engage early (first 5% of participants) receive significantly higher likes, replies, and reposts than matched controls — robust even for low-virality narratives.
- Ablations confirm TF-IDF affiliation weighting beats raw counts/softmax, and FAISS-HNSW matches brute-force similarity at far lower cost.

## Connections

This work sits squarely within current efforts to study **coordinated and cross-platform information dynamics under deteriorating API access**, alongside [[Minici2024-tf]] and [[Luceri2025-tr]] on coordination detection, and [[Lai2024-to]] and [[Freelon2024-sc]] on inferring structure from limited signals. Its cross-platform narrative-diffusion framing connects to [[Bouchaud2026-lr]], Bastos2025-ya, and Bastos2025-ol on multi-platform political communication, while the methodological turn toward latent semantic/topic representations of users echoes [[Balluff2026-if]] and [[Kansaon2025-id]]. The "bridge user" finding resonates with broader work on small influential subpopulations such as [[Bak-Coleman2026-mk]] and [[Graham2025-gp]] on structurally pivotal accounts in online discourse.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gerard2025-br.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-bridging-the-narrative-divide/id1866587707?i=1000743818440)
