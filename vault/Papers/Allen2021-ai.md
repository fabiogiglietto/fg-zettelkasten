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
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445478Z
---

# Research note: Examining potential bias in large-scale censored data

> Allen, J., Mobius, M., Rothschild, D. M., & Watts, D. J. (2021). Research note: Examining potential bias in large-scale censored data. *Harvard Kennedy School Misinformation Review*. https://doi.org/10.37016/mr-2020-74
>
> [View paper](https://doi.org/10.37016/mr-2020-74)

## Summary

This research note examines a subtle but consequential source of bias in the Facebook Social Science One URLs dataset — one of the largest platform-data resources ever released to academics, comprising over 10 trillion cells of shared-URL engagement data. While much attention has focused on the differential-privacy noise added to the dataset, the authors argue that a second, less-scrutinized protection — the censoring of URLs shared publicly fewer than 100 times — is in fact the dominant driver of distortion in descriptive statistics. Because content types differ systematically in how often they are shared publicly, this threshold biases the dataset toward material optimized to be both clicked and publicly shared (news, entertainment) and against content circulated via ads or private links (retail, financial, gaming, social media). The upshot is a cautionary tale: scale alone does not guarantee unbiased inference, and censored big data can badly misstate even basic prevalence estimates — here, overrepresenting news by ~2X and fake news by ~4X.

## Key Contributions

- Empirically documents that **data censoring**, not just differential-privacy noise, is a major and underappreciated source of bias in large-scale platform datasets.
- Quantifies the magnitude of bias in the widely used Facebook URLs dataset for fake-news and news prevalence estimates.
- Provides converging evidence from three independent sources: external Nielsen matching, CrowdTangle share data, and an internal Facebook investigation.
- Offers concrete guidance for researchers (avoid cross-URL-type or cross-country comparisons with differing public-sharing rates) and design recommendations (favor differential privacy over censoring, or censor URL paths while retaining domains).

## Methods

The authors estimated the prevalence of fake news, credible news, and non-news clicks in the Facebook URLs dataset (Jan 2017–Dec 2018) using domain lists of ~9,000 credible and 624 fake-news domains. These estimates were benchmarked against a nationally representative Nielsen desktop web panel, isolating Facebook newsfeed referrals via the `fbclid` URL parameter. A random sample of 1,000 Nielsen URLs from December 2018 was matched against the Facebook dataset to test whether presence or absence tracked the 100-public-share threshold. CrowdTangle API data provided a lower-bound proxy for public shares and allowed examination of how composition changes as the threshold moves from 0 to 100. An internal Facebook investigation analyzed fact-checker-labeled false URLs at the share level, and appendices extended the analysis to non-news categories (top 2,000 ComScore domains) with robustness checks on deduplication and referral definitions.

## Findings

- The raw Facebook dataset attributed 12% of monthly clicks to fake news, 32% to credible news, and 56% to non-news; for December 2018 the figures were 10% / 38% / 52% versus the representative Nielsen estimate of 2.5% / 24% / 74% — a ~4X overestimate of fake news and ~1.7X of credible news.
- 84% of fake-news URLs in the Nielsen sample cleared the 100-share threshold, versus 50% of credible-news and only 23% of non-news URLs.
- Restricting Nielsen URLs to those matched in the Facebook dataset yielded 7% / 39% / 55%, closely reproducing the Facebook figures and supporting the threshold-as-cause hypothesis.
- CrowdTangle reproduced similar results, with a large spike in non-news URLs at 0 shares and fake news' share rising 45% between 1 and 100 shares.
- Facebook's internal analysis showed false URLs rose two orders of magnitude (0.00023% to 0.022% of unique URLs) with the threshold; 30.3 of 30.5 million false-URL public shares came from just 8,660 URLs above 100 shares.
- Across categories, news (2.2X) and entertainment (1.4X) were overrepresented, while gaming (0.025X), retail (0.13X), financial (0.25X), and social media (0.35X) were underrepresented.
- Robustness checks confirmed results held after deduplication and under a stricter referral definition.

## Connections

This note is a methodological companion to the misinformation-prevalence literature it draws on and corrects, most directly [[Allen2020-nj]], whose domain lists it reuses, and the broader body of representative-panel prevalence work in [[Grinberg2019-ua]] and [[Guess2019-ym]]; it also speaks to the "narrow reach of misinformation" arguments in [[Allen2024-av]]. As a study of the biases embedded in platform data-sharing infrastructure, it connects to work on data access and governance such as [[Gonzalez-Bailon2024-rq]] and [[Budak2024-ef]], and to critiques of researcher reliance on platform-provided tools like CrowdTangle in [[Freelon2018-ao]].
