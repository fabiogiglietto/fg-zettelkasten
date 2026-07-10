---
title: "Seeing candidates at scale: Multimodal LLMs for Visual Political Communication on Instagram"
aliases: ["Seeing candidates at scale: Multimodal LLMs for Visual Political Communication on Instagram"]
authors: ["Michael Achmann-Denkler", "Mario Haim", "Christian Wolff"]
year: 2026
doi: 
bibtex_key: Achmann-Denkler2026-lx
topics: [digital-media-elections-global, llms-computational-content-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2604.19489v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Achmann-Denkler2026-lx.mp3
pdf_available: true
discovery_date: 2026-04-30T07:40:12.891395Z
---

# Seeing candidates at scale: Multimodal LLMs for Visual Political Communication on Instagram

> Achmann-Denkler, M., Haim, M., & Wolff, C. (2026). Seeing candidates at scale: Multimodal LLMs for Visual Political Communication on Instagram. *arXiv [cs.CV]*.
>
> [View paper](http://arxiv.org/abs/2604.19489v1)

## Summary

This paper evaluates whether multimodal large language models can serve as practical tools for analyzing visual political communication, using Instagram content from the 2021 German federal election. The authors benchmark GPT-4o against established computer vision pipelines (RetinaFace, FaceNet512, Google Cloud Vision) on two tasks: identifying front-runner politicians and counting individuals in images. GPT-4o substantially outperforms the specialized tools while lowering technical barriers to entry. The validated methods are then applied to a substantive case study of "concentrated visibility," revealing that candidate and party accounts pursue complementary visual strategies and that Instagram stories and posts play distinct communicative roles.

## Key Contributions

- One of the first systematic benchmarks comparing multimodal LLMs against specialized computer vision tools for visual political communication research.
- A replicable, scalable prompt-based framework for measuring concentrated visibility.
- Extends empirical study to Instagram stories, an underexplored ephemeral campaign format.
- Open release of annotations, prompts, model outputs, and evaluation notebooks (corpus excluded for copyright).
- Explicit discussion of open-source vs. proprietary trade-offs (cost, privacy, replicability) to guide methodological choices in computational social science.

## Methods

- Corpus of 1,424 Instagram stories and 547 posts (957 images) from five German parties and five front-runners, Sept 12–25, 2021.
- Compared three approaches: RetinaFace + FaceNet512 (face detection/recognition), Google Cloud Vision API (object detection), and GPT-4o (multimodal LLM with iteratively engineered prompts).
- Two human annotation studies for ground truth: 13 annotators for face identities (Krippendorff's α = 0.86 stories / 0.94 posts) and 5 annotators for person counts on a 30% subsample (α = 0.81 / 0.91), coded in Label Studio.
- Evaluation via precision, recall, macro/weighted F1, and treating each model as an additional annotator for Krippendorff's alpha.
- Case study analysis via chi-squared tests with Bonferroni correction and Cramér's V across account types, parties, and content formats.

## Findings

- GPT-4o achieved macro F1 of 0.89 (stories) / 0.91 (posts) for face verification, versus 0.74 / 0.87 for FaceNet512.
- For person counting, GPT-4o reached macro F1 of 0.86 (stories) / 0.93 (posts), far ahead of Google Cloud Vision (0.58/0.44) and RetinaFace (0.48/0.53).
- FaceNet512 performed worst on the only female candidate, Annalena Baerbock (F1 = 0.66), suggesting possible gender bias or distinct visual personalization.
- Party accounts showed front-runners alone in only 12% of stories versus 33.5% in candidate accounts (χ² = 173.24, p < .001, Cramér's V = 0.349).
- Stories and posts differed significantly in front-runner visibility (χ² = 95.20, p < .001), with CDU, CSU, and SPD showing the strongest format variation.
- Markus Söder (CSU) showed the largest divergence between his own and the party account (Cramér's V = 0.53 stories, 0.70 posts).

## Connections

This paper sits within the growing use of LLMs for computational content analysis and shares methodological concerns with work validating LLMs as annotators and classifiers, such as [[Le-Mens2025-qz]] and [[Votta2025-xz]]. Its focus on visual and platform-specific political campaigning connects it to Instagram and visual communication research including [[Larsson2026-ro]] and [[Bouchafra2026-ts]], while its election-campaign framing complements broader studies of digital media in elections like [[Kalsnes2025-zb]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Achmann-Denkler2026-lx.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-can-gpt-4o-see-politicians-like-we-do/id1866587707?i=1000764671260)
