---
title: "Forgetful by design? A critical audit of YouTube&#x27;s search API for academic research"
aliases: ["Forgetful by design? A critical audit of YouTube&#x27;s search API for academic research"]
authors: ["Bernhard Rieder", "Adrian Padilla", "Oscar Coromina"]
year: 2025
doi: 10.1080/1369118X.2025.2591767
bibtex_key: Rieder2025-ju
topics: [platform-data-governance, digital-research-methods-teaching]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1080/1369118X.2025.2591767
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# Forgetful by design? A critical audit of YouTube&#x27;s search API for academic research

> Rieder, B., Padilla, A., & Coromina, O. (2025). Forgetful by design? A critical audit of YouTube&#x27;s search API for academic research. *Information, Communication and Society, 1-20*. https://doi.org/10.1080/1369118X.2025.2591767
>
> [View paper](https://doi.org/10.1080/1369118X.2025.2591767)

## Summary

This paper delivers the first systematic empirical audit of the search endpoint of YouTube's Data API (v3), a widely used but methodologically under-scrutinized tool for academic research. Through weekly maximalist searches over six months across eleven health, political, and popular-culture queries, the authors document severe deficiencies in completeness, representativeness, consistency, and bias. Their central argument is that the API is "forgetful by design": it systematically privileges freshness over comprehensive retrieval, behaving more like a recommendation engine than a traditional information retrieval system. The authors conclude the endpoint is inadequate for robust academic work — especially for meeting Digital Services Act obligations around studying systemic platform risks — and offer both researcher mitigation strategies and structural recommendations to YouTube.

## Key Contributions

- First systematic empirical audit of YouTube Data API's search endpoint, addressing a major gap in platform data-access scholarship.
- Documents and names a previously unquantified **temporal decay** problem, with distinct head/middle/tail phases.
- Demonstrates concrete consistency and replicability failures via a 2024 European Parliament election case study.
- Offers practical mitigation strategies (early collection, repeated searches, multiple keyword combinations, crawling, random sampling, keyword filtering).
- Provides policy-relevant evidence that current API access does not satisfy DSA requirements for studying systemic risks of very large online platforms.
- Extends the API-audit literature — previously centered on Twitter, Facebook, and TikTok — to YouTube.

## Methods

The authors used a "maximalist" collection strategy via YouTube Data Tools' "one search per day" technique to circumvent the 500-results-per-query cap. Eleven queries were run weekly over six months (from April 2024), each anchored to a fixed October 2023 start date, with primary focus on the default "relevance" ranking compared against "date" ranking. Analysis spanned three quantitative dimensions — query precision (via keyword filtering of titles, descriptions, and tags), temporal coverage (drop-off by distance from publication), and sample consistency across repeated extractions — complemented by a qualitative case study of the 2024 European Parliament elections across five search dates spaced five weeks apart.

## Findings

- Relevance ranking retrieves far more videos than date ranking (up to 8x for "European Parliament election") but at much lower precision (17.2% vs. 57.6% keyword match).
- A consistent three-phase temporal pattern: a ~20-day head (~450 videos/day), a ~40-day middle (~130 videos/day), and a long tail (<20 videos/day).
- Decay affects videos that remain publicly available, confirming it is a search-indexing/ranking artifact rather than deletion.
- Higher-volume queries show stronger decay under relevance ranking; lower-volume date-ranked queries decay less.
- Repeated identical searches yield different result sets — a "chatgpt" test found 773 videos across ten searches versus 456 in a single run.
- In the EP case study, waiting five weeks cut retrievable on-topic videos by ~41% (filtered) / 64% (unfiltered); ten weeks cut them by 76% / 92%.
- Popularity is no protection: only 5 of the top 10 most-viewed post-election videos remained findable four months later, despite still being live.

## Connections

This paper is closely allied with [[Rieder2026-pp]], sharing an author and its critical-audit orientation toward platform research infrastructure. It contributes to the broader platform-governance-data-access conversation about the adequacy of API and DSA researcher provisions, connecting with work such as [[Bruns2026-yv]], [[Bechmann2026-dr]], and [[de-Vreese2026-zx]] on data access under emerging European regulation. Its concern with the reliability and reproducibility of platform-derived samples also resonates with methodological critiques like [[Bouchaud2026-lr]] and [[Bouchaud2026-np]].
