---
title: "Seeing candidates at scale: Multimodal LLMs for Visual Political Communication on Instagram"
aliases: ["Seeing candidates at scale: Multimodal LLMs for Visual Political Communication on Instagram"]
authors: ["Michael Achmann-Denkler", "Mario Haim", "Christian Wolff"]
year: 2026
doi: 
bibtex_key: Achmann-Denkler2026-lx
topics: [generative-ai-and-media, elections-political-communication]
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

This paper benchmarks a multimodal large language model (GPT-4o) against specialized computer vision pipelines (RetinaFace + FaceNet512, Google Cloud Vision) on two visual political communication tasks — front-runner face recognition and person counting — using 1,424 Instagram stories and 547 posts from the 2021 German federal election. GPT-4o substantially outperforms the specialized tools and approaches inter-annotator reliability levels, leading the authors to argue that prompt-based multimodal analysis lowers technical barriers for visual computational social science. They then deploy the validated pipeline in a substantive case study of *concentrated visibility*, showing that candidate accounts foreground front-runners more than party accounts and that stories and posts play distinct roles in personalized campaign communication.

## Key Contributions

- An early systematic benchmark of a multimodal LLM versus specialized CV pipelines for political image analysis.
- A replicable, prompt-based workflow for measuring concentrated visibility at scale.
- Empirical extension to Instagram **stories**, an ephemeral format underrepresented in campaign research.
- Open release of annotations, prompts, model outputs, and evaluation notebooks (corpus withheld for copyright).
- Practical guidance on trade-offs (cost, privacy, replicability) between open-source and proprietary tools.

## Methods

- Corpus: 1,424 stories and 547 posts (957 images) from five German parties and their front-runners, Sept 12–25, 2021.
- Three computational approaches compared: RetinaFace + FaceNet512, Google Cloud Vision, and GPT-4o with iteratively engineered prompts (refined via ChatGPT).
- Two annotation studies in Label Studio: 13 annotators for face identity (Krippendorff's α = 0.86 / 0.94) and 5 annotators on a 30% subsample for person counts (α = 0.81 / 0.91).
- Evaluation via precision, recall, macro/weighted F1, and treating each model as an additional annotator for α.
- Substantive analysis with chi-squared tests (Bonferroni-corrected) and Cramér's V to compare visibility across accounts, parties, and formats.

## Findings

- GPT-4o face verification macro F1 = 0.89 (stories) / 0.91 (posts), versus FaceNet512 at 0.74 / 0.87.
- GPT-4o person counting macro F1 = 0.86 / 0.93, far above Google Cloud Vision (0.58 / 0.44) and RetinaFace (0.48 / 0.53).
- FaceNet512 performed worst on Annalena Baerbock (F1 = 0.66), hinting at gender bias or distinct visual personalization patterns.
- Front-runners appeared alone in 33.5% of candidate stories but only 12% of party stories (χ² = 173.24, Cramér's V = 0.349).
- Stories and posts differ significantly in front-runner visibility (χ² = 95.20), especially for CDU, CSU, and SPD.
- Markus Söder showed the sharpest split between his account and the CSU account (Cramér's V = 0.53 stories, 0.70 posts).

## Connections

This paper sits with other CSS work validating LLMs as flexible annotators and classifiers, particularly visual and multimodal extensions of that agenda — see [[Balluff2026-if]] and [[Dierickx2026-tw]] on automated content analysis pipelines, and [[Le-Mens2025-qz]] on LLMs as measurement tools. It also speaks to ongoing benchmarking of GPT-class models against task-specific systems explored in [[Hackenburg2025-dj]] and [[Allen2025-ot]]. Substantively, its focus on Instagram political communication links to platform-level studies of campaign behavior such as [[Minici2024-tf]] and [[Bouchaud2026-lr]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Achmann-Denkler2026-lx.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-sees/id1866587707?i=1000764671260)
