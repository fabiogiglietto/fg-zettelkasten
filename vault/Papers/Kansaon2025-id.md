---
title: "From fake news to real protests: WhatsApp’s role in Brazilian political coordination"
aliases: ["From fake news to real protests: WhatsApp’s role in Brazilian political coordination"]
authors: ["Daniel Kansaon", "Philipe de Freitas Melo", "Savvas Zannettou", "Fabricio Benevenuto"]
year: 2025
doi: 10.1609/icwsm.v19i1.35857
bibtex_key: Kansaon2025-id
topics: [coordinated-inauthentic-behavior, political-polarization-and-partisanship]
citation_count: 2
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

This paper offers the first large-scale empirical study of rapid, synchronous coordination on WhatsApp, examining Brazilian political groups during the 2022 presidential election and its violent aftermath. Analyzing 13 million messages from 1,444 public groups (July 2022–January 2023), the authors adapt a network-based coordination-detection method from Twitter research to WhatsApp's closed messaging architecture. They demonstrate that coordinated accounts systematically amplified news and misinformation and — critically — that this digital coordination fed directly into offline mobilization, including the doxxing of Supreme Court justices and the protests culminating in the January 8, 2023 attacks. The paper argues that WhatsApp's existing anti-virality countermeasures are insufficient because coordinated actors largely bypass the forwarding mechanisms those measures target.

## Key Contributions

- First large-scale empirical study of rapid, synchronous coordination on WhatsApp, using a 13-million-message dataset.
- Adapts the "Rapid Retweet Network" method into a "Rapid Spread Network" for WhatsApp, offering a more restrictive, timing-based definition of coordination than content-similarity-only approaches.
- Documents a direct link between digital coordination and offline political mobilization, including the events surrounding January 8, 2023.
- Empirically demonstrates the limitations of WhatsApp's forwarding limits, since coordinated actors largely avoid forwarding.
- Offers concrete policy implications: platform transparency, simultaneous-posting detection, and collaboration with electoral authorities.

## Methods

- Collected 13,452,039 messages from 1,444 public Brazilian political WhatsApp groups over seven months via invitation-link discovery and periodic local extraction.
- Deduplicated text/media with MD5 hashing and images with perceptual hashing (pHash).
- Built a Rapid Spread Network linking users who post identical messages within a 60-second window; applied an elbow-method edge-weight threshold (≥5) and Louvain community detection.
- Validated the time window via sensitivity analyses (30s, 60s, 90s) and compared results against 35 random non-coordinated samples with 95% confidence intervals.
- Manually labeled URL domains with an iteratively refined five-category codebook.
- Modeled 15 topics in coordinated text using BERTopic with PTT5 Portuguese embeddings, UMAP, HDBSCAN, and c-TF-IDF, then conducted qualitative case studies on Supreme Court attacks and electoral fraud narratives.

## Findings

- Identified 1,575 coordinated nodes and 1,491 edges forming 450 components; 73.7% were pairs, but one large component held 332 nodes (21% of the network).
- Activity was highly concentrated: 27.2% of coordinated accounts produced 80% of coordinated messages.
- Text dominated coordinated messaging (70.24% vs. 43.78% in non-coordinated samples), and 97.31% of coordinated text messages contained embedded URLs (vs. 16.91%).
- 85.11% of coordinated URLs linked to news sites; 26% came from two misinformation domains flagged by Aos Fatos.
- Stickers featured in flooding attacks (e.g., three users sent 1,200 duplicate stickers in seven minutes).
- Topics were dominated by Supreme Court attacks (42.9%), plus election fraud and military-intervention narratives.
- Case study 1: a doxxing message revealing Supreme Court ministers' New York hotel spread to 102 groups and led to in-person harassment.
- Case study 2: a coordinated message reframing Bolsonaro's speech as endorsing military intervention reached 74 groups and helped mobilize street protests.

## Connections

This paper extends the coordinated-inauthentic-behavior detection tradition — particularly the coordinated-link-sharing and rapid-retweet lineage of [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Giglietto2023-fa71a001]] — into WhatsApp's closed, encrypted ecosystem. Its focus on Brazilian elections and offline mobilization connects it to other Global South and election-integrity work in the register, notably [[Inacio-da-Silva2026-zf]] and [[Pante2025-pq]]. Methodologically it shares the network-based coordination-detection framing found in [[Minici2024-tf]], [[Luceri2025-tr]], and [[Gonzalez-Bailon2024-rq]].
