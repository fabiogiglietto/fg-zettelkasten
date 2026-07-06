---
title: "Coordinated inauthentic behavior on TikTok: Challenges and opportunities for detection in a video-first ecosystem"
aliases: ["Coordinated inauthentic behavior on TikTok: Challenges and opportunities for detection in a video-first ecosystem"]
authors: ["Luca Luceri", "Tanishq Vijay Salkar", "Ashwin Balasubramanian", "Gabriela Pinto", "Chenning Sun", "Emilio Ferrara"]
year: 2025
doi: 
bibtex_key: Luceri2025-tr
topics: [coordinated-inauthentic-behavior]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2505.10867v2
podcast_url: 
pdf_available: false
discovery_date: 2025-05-15T00:00:00Z
---

# Coordinated inauthentic behavior on TikTok: Challenges and opportunities for detection in a video-first ecosystem

> Luceri, L., Salkar, T. V., Balasubramanian, A., Pinto, G., Sun, C., & Ferrara, E. (2025). Coordinated inauthentic behavior on TikTok: Challenges and opportunities for detection in a video-first ecosystem. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2505.10867v2)

## Summary

This paper develops a computational framework for detecting coordinated inauthentic behavior (CIB) on TikTok, addressing the fact that influence-operations research has overwhelmingly concentrated on text-centric platforms like Twitter/X and Facebook. The authors argue that video-first ecosystems demand methodological adaptation rather than direct transfer of existing techniques, and they extend network-based user similarity approaches to TikTok's distinctive content and interaction structures. The work both demonstrates feasibility of CIB detection on TikTok and reflects on the challenges and opportunities the platform's affordances create for influence-operation analysis.

## Key Contributions

- One of the first computational frameworks tailored specifically to coordinated inauthentic behavior detection on TikTok.
- Extension of established network-based CIB detection methodology from text-centric platforms to a video-first ecosystem.
- A diagnostic discussion of which behavioral signals are most informative for coordination on TikTok, and what platform-specific challenges and opportunities arise.

## Methods

The authors build user similarity networks in which edges encode shared behavioral or content traces among accounts, following the lineage of network-based CIB detection. They adapt the signal set to TikTok's video-first interaction structure and empirically evaluate the framework on TikTok data to surface coordinated clusters.

## Findings

- Network-based similarity approaches can be successfully adapted to TikTok and recover coordinated activity when calibrated to platform-specific signals.
- Text-focused CIB methods do not transfer cleanly: video, audio, and TikTok's algorithmic interaction layer require new diagnostic features.
- Video-first platforms simultaneously hinder some standard detection strategies (e.g., textual near-duplication) and open new ones (e.g., shared audio, effects, or remix traces).

## Connections

This work extends the network-based CIB detection tradition — particularly similarity-network frameworks like those developed in [[Minici2024-tf]] and applied across platforms in [[Lai2024-to]] — into the underexplored TikTok setting. It connects to broader efforts to generalize coordination detection across platforms and modalities, including [[Schroeder2026-im]], [[Kulichkina2026-zk]], and methodological scrutiny of what similarity-based approaches actually capture, as in [[Graham2025-gp]] and [[DiGiuseppe2025-es]]. It also complements platform-specific CIB studies such as [[Kansaon2025-id]] and TikTok-focused influence work in [[Gaw2025-ru]].
