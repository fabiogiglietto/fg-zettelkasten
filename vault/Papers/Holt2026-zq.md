---
title: "What Facebook users flag as false news: A mixed-methods investigation of user-reported links"
aliases: ["What Facebook users flag as false news: A mixed-methods investigation of user-reported links"]
authors: ["Anton Elias Holt"]
year: 2026
doi: 10.1080/21670811.2026.2703607
bibtex_key: Holt2026-zq
topics: [platform-data-access-and-governance, health-misinformation-and-fact-checking]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/21670811.2026.2703607
podcast_url: 
pdf_available: true
discovery_date: 2026-08-20T12:21:52.011920Z
---

# What Facebook users flag as false news: A mixed-methods investigation of user-reported links

> Holt, A. E. (2026). What Facebook users flag as false news: A mixed-methods investigation of user-reported links. *Digital Journalism*, 1–19. https://doi.org/10.1080/21670811.2026.2703607
>
> [View paper](https://doi.org/10.1080/21670811.2026.2703607)

## Summary

This paper asks an empirically neglected question with sharp policy relevance: what do Facebook users actually flag as "False News"? Motivated by Meta's January 2025 decision to abandon third-party fact-checking in the US in favour of Community Notes and greater reliance on user reports, the author uses the Meta-created URL Shares dataset to compare three sets of links — those users reported as false, those professionally fact-checked as false, and a matched control sample. The central finding is that user reports do not reliably track factual falsity. Instead, users tend to flag content about polarized political topics that *contextualizes* controversial events rather than content that is outright false — reporting functions closer to a "statement of objection" than to misinformation detection. This casts serious doubt on the assumption that crowd-sourced reporting can substitute for professional fact-checking.

## Key Contributions

- First URL-level empirical content analysis of what users actually report as false, moving beyond largely theoretical, experimental, or lab-based literature.
- Directly engages Meta's 2025 policy shift toward user-report-driven moderation and Community Notes with relevant evidence.
- Introduces user reports as a platform-intrinsic signal of "problematic" content within the URL Shares dataset, whose reporting data had previously only served to validate simulated models.
- Provides non-US-centric evidence (Brazil 2018 election) alongside a controlled high-trust mainstream-media comparison (BBC).
- Extends descriptive work on demographic (age) engagement patterns to user-reported content specifically.

## Methods

A mixed-methods design applied to the Meta URL Shares dataset (URLs shared publicly 100+ times, Jan 2017–Nov 2022), using the Attributes, Breakdown, and User Reports tables. Differentially-private noisy cells were filtered to retain only statistically certain interactions (alpha < 0.001). Three samples were built: a Reported Sample (110,224 URLs with 20+ real reports), a Misinformation Sample (28,271 fact-checked-false URLs), and a matched Control Sample (200,000 non-reported, non-fact-checked URLs). Multilingual link texts were translated via Meta's NLLB-200-3B model inside the FORT environment. Analysis combined frequency counts and Rank Difference Scores with qualitative close reading, two critical case studies (Brazil October 2018; BBC.com/news), and interaction-pattern heatmaps by age group normalized per view.

## Findings

- In 2018 Brazil, user-reported URLs outnumbered fact-checked-false URLs 71:1 (1,568 vs. 22) — large scale, weak precision.
- Reported Brazil links overwhelmingly concerned the two candidates, electoral processes, corruption/fraud allegations, WhatsApp smears, and the contested "gay kit" story — often contextualizing rather than asserting falsehoods.
- Contradictory reported links existed on the same contested topic, indicating politically motivated flagging.
- BBC reported links (239) had a narrower, more political, more negative and sensational focus (Trump, Covid, vaccines, Kashmir) than the diverse, neutral control links (301).
- Reported and Misinformation samples overlapped only modestly (12.2% of Misinformation, 3.1% of Reported), so reports are not a subset of fact-checked content.
- Older users engaged more heavily with reported URLs (more likes, comments, shares-without-clicks, angry reactions); the youngest groups clicked control links more.
- Elevated angry reactions and shares-without-clicks signal that reported content is more partisan and contested.

## Connections

This paper's empirical use of the URL Shares dataset and its differential-privacy handling connect it methodologically to broader debates about platform data access and the reliability of Meta's research products; see [[Bak-Coleman2026-mk]], [[Bak-Coleman2025-pm]], and [[Pierri2025-hm]] on working with and validating platform-provided data. Its critical assessment of crowd-sourced moderation and Community Notes speaks to work on the value and limits of community-based fact-checking, notably [[Allen2025-ot]] and [[DeVerna2025-dl]]. The Brazil case and mainstream-media focus also link it to research on fact-checking practice and misinformation ecosystems such as [[Cazzamatta2026-lo]].
