---
title: "From fake news to real protests: WhatsApp’s role in Brazilian political coordination"
aliases: ["From fake news to real protests: WhatsApp’s role in Brazilian political coordination"]
authors: ["Daniel Kansaon", "Philipe de Freitas Melo", "Savvas Zannettou", "Fabricio Benevenuto"]
year: 2025
doi: 10.1609/icwsm.v19i1.35857
bibtex_key: Kansaon2025-id
topics: [coordinated-inauthentic-behavior, digital-media-elections-global]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1609/icwsm.v19i1.35857
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# From fake news to real protests: WhatsApp’s role in Brazilian political coordination

> Kansaon, D., Melo, P. D. F., Zannettou, S., & Benevenuto, F. (2025). From fake news to real protests: WhatsApp’s role in Brazilian political coordination. *Proceedings of the International AAAI Conference on Web and Social Media*, *19*, 1007–1020. https://doi.org/10.1609/icwsm.v19i1.35857
>
> [View paper](https://doi.org/10.1609/icwsm.v19i1.35857)

## Summary

This paper offers the first large-scale empirical study of coordinated inauthentic behavior on WhatsApp, analyzing 13.4 million messages from 1,444 public Brazilian political groups around the 2022 presidential election. Adapting Pacheco et al.'s Rapid Retweet Network to WhatsApp's closed-messaging architecture, the authors detect 1,575 accounts that post identical content within tight time windows and amplify misinformation, news links, and stickers. Crucially, they document how this digital coordination scaffolded offline mobilization — including the doxxing of Supreme Court justices and the January 8, 2023 attacks — and they argue that WhatsApp's existing anti-virality tools (forwarding limits, bans) are largely irrelevant because coordinated actors bypass forwarding entirely.

## Key Contributions

- First large-scale empirical evidence of synchronous coordination on WhatsApp using a 13M-message Brazilian political corpus.
- Methodological adaptation of the Rapid Retweet Network to a closed messaging platform, providing a stricter operational definition of coordination than content-similarity alone.
- Empirical chain-of-evidence linking WhatsApp coordination to specific offline events (justice doxxing, military-intervention protests, Jan 8 mobilization).
- Critique of platform countermeasures: forwarding limits miss the bulk (58.9%) of coordinated messages, which are sent directly rather than forwarded.
- Policy implications for transparency, simultaneous-posting detection, and electoral-authority collaboration in the Global South.

## Methods

The authors collected messages via invitation-link discovery and local extraction over seven months, deduplicating with MD5 and perceptual hashing. They built a "Rapid Spread Network" linking users who posted identical content within 60 seconds, applied elbow-thresholding (min edge weight 5) and Louvain community detection, and validated robustness with 30s/90s sensitivity analyses and 35 random non-coordinated samples. URL domains were manually coded using an iteratively refined five-category codebook, and BERTopic with PTT5 Portuguese embeddings produced 15 topical clusters, two of which (Supreme Court attacks; electoral fraud) were examined qualitatively.

## Findings

- 1,575 coordinated accounts produced 14,440+ amplified messages; 27.2% of accounts generated 80% of coordinated traffic.
- The coordination graph is highly fragmented (450 components, 73.7% pairs) but contains a large connected component of 332 nodes.
- Coordinated messages are overwhelmingly textual (70.24%) and URL-rich (97.31% contain links vs. 16.91% for non-coordinated baselines).
- 85.11% of coordinated URLs are news links; 26% trace to two misinformation sites (pensandodireita, terrabrasilnoticias) flagged by Aos Fatos.
- Stickers are weaponized for flooding (e.g., three users dispatched 1,200 duplicate stickers in seven minutes).
- Topic distribution skews toward Supreme Court attacks (42.9%), election-fraud narratives, and calls for military intervention.
- Case 1: a doxxing message exposing justices' NYC hotel spread to 102 groups and precipitated in-person harassment (Nov 13, 2022).
- Case 2: a coordinated reinterpretation of Bolsonaro's post-election speech as endorsing military intervention reached 74 groups and helped seed protests at military barracks.

## Connections

This paper extends Twitter/Facebook coordination-detection traditions into encrypted messaging, complementing platform-comparative work on coordinated networks like [[Minici2024-tf]] and the rapid-network detection lineage drawn on by [[Luceri2025-tr]] and [[Bollenbacher2026-vz]]. Its documentation of how online coordination materializes into offline political action speaks directly to [[Kulichkina2026-zk]] on protest mobilization and to broader Brazilian-context studies of WhatsApp and information disorder such as [[Rossini2026-jn]] and [[Emilio2026-ik]]. The platform-governance critique resonates with transparency- and intervention-focused work like [[DeVerna2025-dl]] and [[Starbird2025-jj]].
