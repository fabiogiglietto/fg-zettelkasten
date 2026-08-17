---
title: "On narrative: The rhetorical mechanisms of online polarisation"
aliases: ["On narrative: The rhetorical mechanisms of online polarisation"]
authors: ["Jan Elfes", "Marco Bastos", "Luca Maria Aiello"]
year: 2026
doi: 
bibtex_key: Elfes2026-jb
topics: [political-polarization-and-partisanship, llm-and-computational-content-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2601.07398v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Elfes2026-jb.mp3
pdf_available: true
discovery_date: 2026-02-04T11:06:02.329326Z
---

# On narrative: The rhetorical mechanisms of online polarisation

> Elfes, J., Bastos, M., & Aiello, L. M. (2026). On narrative: The rhetorical mechanisms of online polarisation. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2601.07398v1)

## Summary

This paper introduces **narrative polarisation** — the extent to which partisan groups assign opposing roles to the same key actors within contested issues — as a distinct dimension of online polarisation that complements affective and ideological measures. The authors argue that conventional interaction- and opinion-based metrics miss the rhetorical mechanisms by which groups construct opposing realities, and instead operationalise structuralist narratology (Greimas' Actantial Model) via a large language model. Applied to YouTube videos and comments about the Israeli–Palestinian conflict, the study finds that videos propagate strongly polarised narratives, yet user comments substantially converge at the surface level. Beneath this convergence, however, recurring narrative motifs continue to encode partisan differences — suggesting narrative may be partially orthogonal to user ideology.

## Key Contributions

- Formalises **narrative polarisation** as a measurable construct complementing affective and ideological polarisation.
- Demonstrates scalable computational use of Greimas' Actantial Model (six roles) well beyond its folktale origins.
- Provides an LLM-based annotation pipeline with codebook, validation data, and OSF repository for extracting actantial roles from text.
- Develops quantitative measures — overlap coefficient, subject divergence, and narrative motifs — for comparing narratives across partisan environments.
- Offers empirical evidence that comments can mitigate content-level narrative polarisation on the surface while sustaining deeper polarisation through motifs.

## Methods

The authors built partisan search queries from offline protest claims (Crowd Counting Consortium) plus neutral baselines to retrieve 212 English-language YouTube videos (107 Israeli-leaning, 105 Palestinian-leaning, Oct 2023–Oct 2024) and 90,029 top-level comments. Videos were transcribed with Whisper and segmented at 150-word boundaries. Actantial roles were annotated by DeepSeek-R1-Distill-Qwen-32B using a curated set of 21 actor and 7 object labels, validated against two expert human annotators (micro F1 ≈ 0.73, Krippendorff's α ≈ 0.59 — comparable to inter-human agreement). Analysis combined an overlap coefficient for Subject–Object distributions, a subject-divergence measure of attribution skew, permutation tests (Bonferroni/FDR corrected), and qualitative close reading of three identified narrative motifs (convergent, adversarial, dependent).

## Findings

- Between-group narrative overlap was higher in comments (0.80) than in transcripts (0.63), indicating surface-level harmonisation rather than reinforcement of echo chambers.
- Average absolute subject divergence dropped from 0.19 (transcripts) to 0.07 (comments), with the sharpest reduction for attribution of violence (−0.43 → −0.05).
- Videos diverged strongly on who perpetrates violence (Palestinian-skewed in Israeli-leaning videos) and who holds security and rights claims (Israeli-skewed).
- Comments introduced an Israeli-skew on "peace" absent in videos, likely reflecting in-group appeals folded into generic "both sides" framings.
- Convergent motifs highlighted in-group vulnerabilities (Israeli security; Palestinian rights); adversarial motifs justified violence as retaliation; dependent motifs stressed Israeli control over Palestinian rights and territory.
- The LLM's inter-coder agreement matched that of human annotators and exceeded prior LLM narrative-annotation benchmarks.

## Connections

This work extends the echo chamber and selective exposure literature—foundational to [[Bakshy2015-rn]]—by arguing that polarisation operates between narratives as well as between people, complementing measures of affective and ideological division. Its LLM-based content analysis pipeline sits alongside other computational-annotation and generative-modeling approaches to political discourse such as [[Le-Mens2025-qz]] and [[Tornberg2025-ir]], and its finding that audiences may be less polarised than the content they consume speaks to broader debates on partisan media exposure and platform-level polarisation captured in [[DeVerna2025-dl]] and [[Bouchaud2026-lr]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Elfes2026-jb.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-narrative-warfare-how-stories-fuel/id1866587707?i=1000748224708)
