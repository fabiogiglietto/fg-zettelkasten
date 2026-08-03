---
title: "Multi-platform analysis of electoral discourse on social media as a research infrastructure problem"
aliases: ["Multi-platform analysis of electoral discourse on social media as a research infrastructure problem"]
authors: ["Ludwig Schulte", "Dino Pasic", "Catalina Goanta", "Adriana Iamnitchi"]
year: 2026
doi: 10.1145/3795513.3807440
bibtex_key: Schulte2026-df
topics: [platform-data-access-governance, political-communication-elections]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3795513.3807440
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schulte2026-df.mp3
pdf_available: true
discovery_date: 2026-05-26T17:18:00.349369Z
---

# Multi-platform analysis of electoral discourse on social media as a research infrastructure problem

> Schulte, L., Pasic, D., Goanta, C., & Iamnitchi, A. (2026). Multi-platform analysis of electoral discourse on social media as a research infrastructure problem. *Companion Publication of the 2026 18th ACM Web Science Conference*, 66–69. https://doi.org/10.1145/3795513.3807440
>
> [View paper](https://doi.org/10.1145/3795513.3807440)

## Summary

Using the 2025 German federal election as a case study, this paper recasts multi-platform electoral discourse analysis as a research infrastructure problem rather than a sequence of standalone empirical studies. The authors collected 81,866 X posts and 43,597 TikTok videos across seven German parties, applied BERTopic for topic modeling, and built a multimodal pipeline combining facial, vocal, and textual analysis on diarized TikTok segments. They argue that the central obstacle to studying electoral harms is not a lack of studies but the absence of consolidated, reusable tools, workflows, and documentation for cross-platform observability under increasingly constrained platform access. The paper closes with four recommendations on data standardization, quality, content-type-tailored analysis, and interdisciplinary collaboration.

## Key Contributions

- Reframes multi-platform election analysis as an infrastructure problem requiring reusable foundations rather than ad hoc empirical projects.
- A documented parallel X/TikTok collection case study, distinguishing "authored" (official accounts) from "promoted" (mentions, hashtags, retweets) content.
- A concrete multimodal TikTok pipeline integrating facial emotion (DeepFace), vocal tone (HuBERT), and textual sentiment (XLM-R) at the diarized-segment level.
- A catalogue of biases — algorithmic, temporal, sampling, and noise — arising from post-API scraping conditions.
- Four actionable recommendations: standardized data structures, higher data-quality benchmarks (e.g., transparent electoral account labeling), content-type-tailored analysis, and interdisciplinary expertise integration.

## Methods

The study covers 6 Nov 2024 (collapse of the German government) to 23 Feb 2025 (election day). X data was gathered via an API v2-based scraper seeded with official party accounts and expanded through mentions; TikTok data was assembled by aggregating partial results across repeated hashtag-based calls and expanded via party-linked accounts. Posts were clustered with BERTopic and tracked temporally. TikTok videos were diarized with pyannote.audio, then analyzed for facial emotion (OpenCV + DeepFace), vocal tone (HuBERT), and textual sentiment (XLM-R), with Cramér's V quantifying inter-modal associations.

## Findings

- Dataset: 81,866 X posts from 541 accounts and 43,597 TikTok videos from 4,682 accounts across seven parties.
- Parties strategically diverge across platforms: BSW dominates on X but barely uses TikTok; AfD is highly active on TikTok; FDP and CDU span both.
- Facial, vocal, and textual modalities on TikTok are only weakly associated (Cramér's V ≤ 0.104), functioning as semi-independent channels.
- Political TikTok content frequently pairs negative/critical text and visuals with calm, neutral vocal delivery — a politainment signature.
- Russia/Ukraine and immigration top both platforms but in reversed order; migration is more salient on TikTok, while Israel/Gaza and EU topics dominate on X.
- About two-thirds of hashtag-scraped TikTok content was non-political, signaling substantial noise bias.
- X's ~1,000 posts/day per-account API ceiling prevents historical recovery for active users; TikTok returns algorithmically filtered partials, embedding temporal and engagement bias.

## Connections

This paper sits squarely in the "post-API age" debate over what computational election research can still do, connecting to [[Freelon2024-sc]], [[Bruns2025-fz]], and [[Bruns2026-yv]] on access decay, and to [[Rieder2025-ju]] and [[Rieder2026-pp]] on platform observability as infrastructure. Its multimodal TikTok pipeline and emphasis on TikTok-specific scraping artefacts connect to [[Achmann-Denkler2026-lx]], [[Pierri2025-hm]], and [[Bouchaud2026-lr]], while its cross-platform German election framing relates to [[Heiss2026-qv]] and the DSA Article 40 vetted-access discussions echoed in [[Ohme2026-nv]] and [[Vincent_undated-re]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Schulte2026-df.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-why-one-platform-isnt-enough-to/id1866587707?i=1000771443693)
