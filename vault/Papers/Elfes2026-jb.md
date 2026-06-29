---
title: "On narrative: The rhetorical mechanisms of online polarisation"
aliases: ["On narrative: The rhetorical mechanisms of online polarisation"]
authors: ["Jan Elfes", "Marco Bastos", "Aiello, Luca Maria"]
year: 2026
doi: 10.48550/arxiv.2601.07398
bibtex_key: Elfes2026-jb
topics: [polarization-hybrid-media, computational-methods-social-research]
citation_count: 0
open_access: true
source_url: https://doi.org/10.48550/arxiv.2601.07398
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Elfes2026-jb.mp3
pdf_available: true
discovery_date: 2026-02-04T11:06:02.329326Z
---

# On narrative: The rhetorical mechanisms of online polarisation

> Elfes, J., Bastos, M., & Aiello, L. M. (2026). On narrative: The rhetorical mechanisms of online polarisation. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2601.07398v1)

## Summary

This paper introduces *narrative polarisation* as a distinct dimension of online polarisation, defined as the divergent ways partisan groups assign actants — heroes, villains, helpers, victims — to key actors in a contested issue. The authors operationalise Greimas' Actantial Model via a large language model and apply it to 212 YouTube videos and ~90,000 comments on the Israeli-Palestinian conflict. They find that while videos encode sharply opposed narratives (especially about who perpetrates violence versus who claims security or rights), comments substantially flatten this surface-level divergence. However, underlying *narrative motifs* — convergent, adversarial, and dependent configurations of actors — continue to carry partisan structure, suggesting that narrative polarisation can persist beneath apparent consensus and may be partially orthogonal to user ideology.

## Key Contributions

- Formalises "narrative polarisation" as a construct complementing affective and ideological polarisation, grounded in structuralist narratology.
- Scales Greimas' Actantial Model from folktale analysis to large-scale social media discourse.
- Releases an LLM-based annotation pipeline (DeepSeek-R1-Distill-Qwen-32B) with codebook, validation data, and an OSF repository for actantial role extraction.
- Proposes quantitative measures — overlap coefficient, subject divergence, and narrative motif typology — for analysing narrative-level polarisation.
- Empirically shows divergence between content-level and comment-level narrative polarisation, complicating echo chamber accounts.

## Methods

The authors retrieve YouTube videos using partisan search queries derived from Crowd Counting Consortium offline protest claims, plus neutral baselines, yielding 107 Israeli-leaning and 105 Palestinian-leaning videos (Oct 2023–Oct 2024) and 90,029 top-level comments. Whisper-large-v3 transcribes videos, segmented at 150-word boundaries. DeepSeek-R1-Distill-Qwen-32B annotates actantial roles using 21 actor labels and 7 object labels, validated against two expert annotators on 292 comments (avg micro F1 0.73, Krippendorff's α 0.59 — comparable to inter-human agreement). Analyses combine overlap coefficients, a subject-divergence statistic with permutation tests (Bonferroni/FDR corrected), and qualitative close reading of three identified narrative motifs.

## Findings

- Videos showed strong narrative polarisation: Israeli-leaning videos attributed violence to Palestinian actors, while Palestinian-leaning videos attributed security and rights/freedoms claims primarily to Israeli actors.
- Comments substantially reduced surface divergence: between-group overlap rose from 0.63 (transcripts) to 0.80 (comments), and average absolute subject divergence fell from 0.19 to 0.07.
- The largest convergence occurred around violence attribution (divergence collapsing from -0.43 to -0.05); a new IS-skewed peace narrative emerged in comments.
- **Convergent motifs**: in-group critique (e.g., Israeli-leaning commenters criticising Israeli security failures).
- **Adversarial motifs**: structured violence discourse, often justifying retaliation against the opposing side.
- **Dependent motifs**: predominantly cast Palestinians as subjects dependent on Israeli control, especially in Israeli-leaning discussion threads.
- LLM–human inter-coder agreement matched human–human agreement and exceeded prior narrative-annotation benchmarks.

## Connections

This paper extends polarisation research beyond opinion- and interaction-based measures toward rhetorical structure, complicating echo chamber findings such as [[Bakshy2015-rn]] and resonating with work showing that exposure-level polarisation does not map cleanly onto audience attitudes, e.g. [[Tornberg2025-ir]] and [[Tornberg2026-lc]]. Its LLM-based annotation pipeline connects methodologically to recent uses of generative models for measuring partisan or ideological content like [[Le-Mens2025-qz]] and [[Hackenburg2025-dj]], while the narrative-motif analysis of conflict discourse complements affective and identity-centred approaches in [[Mosleh2024-op]] and [[Knupfer2025-vt]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Elfes2026-jb.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-narrative-warfare-how-stories-fuel/id1866587707?i=1000748224708)
