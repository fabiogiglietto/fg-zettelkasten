---
title: "Research note: Examining potential bias in large-scale censored data"
aliases: ["Research note: Examining potential bias in large-scale censored data"]
authors: ["Jennifer Allen", "Markus Mobius", "David M. Rothschild", "Duncan J. Watts"]
year: 2021
doi: 10.37016/mr-2020-74
bibtex_key: Allen2021-ai
topics: [platform-data-access-governance, misinformation-exposure-recalibration]
citation_count: 20
open_access: false
source_url: https://doi.org/10.37016/mr-2020-74
podcast_url: 
pdf_available: false
discovery_date: 2026-09-26T08:39:39.445478Z
---

# Research note: Examining potential bias in large-scale censored data

> Allen, J., Mobius, M., Rothschild, D. M., & Watts, D. J. (2021). Research note: Examining potential bias in large-scale censored data. *Harvard Kennedy School Misinformation Review*. https://doi.org/10.37016/mr-2020-74
>
> [View paper](https://doi.org/10.37016/mr-2020-74)

## Summary

This research note interrogates the analytical costs of privacy-preserving modifications applied to Facebook's 10-trillion cell URLs dataset — one of the largest platform datasets ever released for academic research. To protect user privacy, the dataset was altered in two ways: differentially private noise was added to engagement counts, and URLs shared publicly fewer than 100 times were censored entirely. The authors argue that, despite the dataset's unprecedented scale, these alterations can introduce systematic bias that distorts the conclusions researchers might draw, particularly for questions concerning the prevalence of content categories such as fake news. The note thus sits at the intersection of platform-data-access debates and the methodology of studying misinformation exposure.

## Key Contributions

- Provides a methodological assessment of how privacy-preserving techniques (differential privacy noise and share-count censoring) bias inferences drawn from a major social media dataset.
- Identifies the 100-public-share censoring threshold and the additive noise as the two primary sources of analytical concern.
- Offers practical guidance to researchers on interpreting results derived from censored and noise-added platform data.
- Highlights that sheer dataset scale does not guarantee validity for all research questions.

## Methods

The authors work directly with Facebook's URLs dataset, which records shared URLs alongside engagement metrics. They examine the two alteration mechanisms — differentially private noise on engagement counts and the 100-public-share inclusion threshold — and estimate the prevalence of content categories (e.g., fake news) to assess how these modifications shift measured outcomes.

## Findings

- The study estimates the prevalence of certain content types to gauge the impact of the alterations on analytical conclusions.
- Privacy-driven modifications can systematically bias prevalence estimates, meaning conclusions about phenomena like misinformation may be compromised even in a massive dataset.
- (Specific quantitative results are not recoverable from the abstract alone.)

## Connections

This note extends debates on platform data access and the trade-offs of privacy-preserving releases, resonating with work on the governance and mechanics of researcher data access such as [[Freelon2018-ao]] and other analyses of platform-provided datasets. Its focus on measuring the prevalence of fake news connects it to the broader empirical literature on misinformation exposure and its recalibration, including [[Allen2020-nj]], [[Grinberg2019-ua]], [[Guess2019-ym]], and [[Budak2024-ef]], all of which grapple with how much low-quality content people actually encounter — a question directly sensitive to the censoring and noise biases this paper documents.
