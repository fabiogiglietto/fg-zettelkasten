---
title: "TubeStats and TokStats: Research tools for random samples of YouTube and TikTok"
aliases: ["TubeStats and TokStats: Research tools for random samples of YouTube and TikTok"]
authors: ["Kevin Zheng", "Reagan Keeney", "Ryan McGrady", "Vikramaditya Jaisingh", "Ethan Zuckerman"]
year: 2026
doi: 10.17645/mac.12085
bibtex_key: Zheng2026-bi
topics: [platform-data-access-and-governance, computational-network-structure-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.17645/mac.12085
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Zheng2026-bi.mp3
pdf_available: true
discovery_date: 2026-07-14T06:31:33.816869Z
---

# TubeStats and TokStats: Research tools for random samples of YouTube and TikTok

> Zheng, K., Keeney, R., McGrady, R., Jaisingh, V., & Zuckerman, E. (2026). TubeStats and TokStats: Research tools for random samples of YouTube and TikTok. *Media and Communication*, *14*. https://doi.org/10.17645/mac.12085
>
> [View paper](https://doi.org/10.17645/mac.12085)

## Summary

This paper introduces **TubeStats** and **TokStats**, two dashboard-based research tools that provide platform-wide statistics for YouTube and TikTok using random sampling techniques. The authors argue that neither platform offers sanctioned mechanisms—including their research APIs—to produce verifiable, representative samples, forcing researchers into opportunistic samples that systematically oversample popular, algorithmically amplified content. By exploiting the unique-ID indexing schemes of each platform, the tools generate defensible platform-wide denominators and engagement distributions that let scholars contextualize otherwise non-generalizable studies. Positioned within the "post-API age" and the open research infrastructure movement, the paper documents the tools' architecture, real-world uses, and the technical, financial, and ethical challenges of sustaining public-interest transparency research.

## Key Contributions

- Two publicly available, regularly updated dashboards: **TubeStats** (launched) and **TokStats** (planned September 2026), reporting video counts, view/like/comment/subscriber distributions, languages, categories, and growth over time.
- A validated, reproducible, API-independent methodology for generating representative random samples of YouTube and TikTok.
- Open-source release of sampling and dashboard code via GitHub for reuse and reproducibility.
- A practical solution to "denominator" and "distribution" problems, offering benchmarks for contextualizing non-representative samples and enabling cross-platform comparison.
- A model for privacy-preserving data sharing (aggregate dashboards plus tiered gated/public datasets) and reflection on sustaining open infrastructure under technical, financial, and regulatory pressure.

## Methods

For YouTube, the authors validate "dialing for videos" (querying purely random 11-character IDs) against the more efficient "random prefix sampling" that exploits hyphen-based prefix/postfix indexing in the platform's case-insensitive search. Tooling relies on the Innertube package, yt-dlp for metadata/audio, and OpenAI's Whisper for language identification (audio discarded immediately, never archived). For TikTok, they exploit the 64-bit structure of 19-digit video IDs—the first 32 bits encode a Unix creation timestamp—selecting a random second and generating tens of thousands of candidate ID combinations queried via Selenium. Dashboards use a SvelteKit front-end, static summary data in an S3 bucket, Chart.js charts, and pandas-generated statistics (logarithmic binning, percentile calculators via linear interpolation).

## Findings

- Random prefix sampling closely approximates full random sampling for YouTube (hours to sample), whereas TikTok sampling takes on the order of months.
- Calibration example: a YouTube video with 150 views is at the 68th percentile; 1,000–10,000 views place a video in the top 10%—confirming search-based samples heavily overrepresent popular content.
- Hindi YouTube differs markedly from English, Spanish, and Russian YouTube: newer, shorter videos, more education/entertainment, with distinct like-to-view patterns.
- TikTok is not predominantly a US phenomenon; most videos are uploaded outside the US, with popularity concentrated in Asian countries.
- External researchers used the datasets as baselines—e.g., finding X/Twitter attention more imbalanced than YouTube, and contextualizing Facebook engagement skew and abortion-related and educational content prevalence.
- Platform changes (YouTube's shift from DASH to the opaque SABR protocol, increased IP throttling partly attributed to AI-training scrapers) create ongoing maintenance obstacles.

## Connections

This paper sits squarely within post-API data-access and platform transparency debates, sharing concerns about the collapse of sanctioned research access with work on independent data infrastructures such as [[Freelon2024-sc]], Davis2025 and studies of DSA-era access regimes like [[Rieder2025-ju]] and [[Rieder2026-pp]]. Its critique of opportunistic, engagement-skewed sampling and its call for defensible denominators connect to methodological reflections on representativeness and platform sampling in [[Efstratiou2025-gs]] and [[Pierri2025-hm]]. Broader questions about sustaining open research infrastructure and reproducibility resonate with [[Bak-Coleman2025-pm]] and [[Murtfeldt2025-wu]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Zheng2026-bi.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
