---
title: "Forgetful by design? A critical audit of YouTube&#x27;s search API for academic research"
aliases: ["Forgetful by design? A critical audit of YouTube&#x27;s search API for academic research"]
authors: ["Bernhard Rieder", "Adrian Padilla", "Oscar Coromina"]
year: 2025
doi: 10.1080/1369118X.2025.2591767
bibtex_key: Rieder2025-ju
topics: [platform-governance-data-access, computational-methods-social-research]
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

Rieder, Padilla, and Coromina conduct the first systematic empirical audit of YouTube Data API v3's search endpoint, a tool heavily relied on for academic research yet rarely scrutinized methodologically. Through six months of weekly searches across eleven queries (health, political, popular culture), they document that the endpoint is "forgetful by design": it behaves more like a recommendation engine optimized for freshness than a traditional information retrieval system. The authors find severe temporal decay, inconsistent results across identical queries, large discrepancies between ranking parameters, and conclude that the API is inadequate both for robust academic research and for fulfilling Digital Services Act obligations to study systemic platform risks.

## Key Contributions

- First systematic empirical audit of YouTube's search API endpoint, extending API-critique scholarship from Twitter, Facebook, and TikTok to YouTube.
- Names and quantifies a three-phase **temporal decay** pattern (head ~20 days, middle ~40 days, flat tail) affecting findability of still-public videos.
- Demonstrates replicability failures: repeated identical queries yield non-overlapping result sets.
- Offers concrete mitigation strategies (early/repeated collection, keyword filtering, multiple query formulations, complementary crawling/random sampling).
- Provides policy-relevant evidence that current API access fails DSA researcher-access requirements, with specific recommendations to YouTube.

## Methods

A "maximalist" collection strategy using YouTube Data Tools' one-search-per-day technique to bypass the 500-result cap. Weekly searches were run for six months starting April 2024 across eleven queries (e.g., "Andrew Tate," "Gaza ceasefire," "European Parliament election," "Mukbang"), all anchored to a fixed start date of 15 October 2023. The team compared "relevance" vs. "date" ranking and analyzed three dimensions: precision (keyword matching on titles, descriptions, tags), temporal coverage (decay as a function of distance from publication), and consistency across repeated extractions. A qualitative case study on the 2024 European Parliament elections used five search dates spaced five weeks apart.

## Findings

- Relevance ranking returns up to 8× more videos than date ranking but at far lower precision (e.g., 17.2% vs. 57.6% keyword match for "European Parliament election").
- Three temporal phases recur across queries: ~450 videos/day in the 20-day head, ~130/day in the 40-day middle, and <20/day in the long tail.
- The decay reflects a search-indexing artifact, not video deletion — affected videos remain publicly accessible on YouTube.
- Repeated extractions are inconsistent: ten consecutive [chatgpt] searches returned 773 unique videos vs. only 456 from a single run.
- For the 2024 EP elections, waiting five weeks post-event reduced retrievable on-topic videos by ~41% (filtered) / 64% (unfiltered); ten weeks reduced them by 76% / 92%.
- Even highly-viewed videos vanish from search: only 5 of the top 10 most-viewed remained findable four months later.

## Connections

This paper extends the "APIcalypse"/"Post-API Age" lineage of platform-data critique most directly carried forward by [[Bruns2025-fz]] and [[Freelon2024-sc]], and complements other recent infrastructural audits and data-access analyses such as [[Helmond2026-ll]], [[Ohme2026-nv]], and [[Bouchaud2026-lr]]. It pairs naturally with [[Rieder2026-pp]] from the same lead author and informs DSA-oriented governance work including [[Vincent_undated-re]] and [[Schiffrin_undated-gi]]; methodologically it is also relevant to YouTube-based studies relying on search retrieval, such as [[Ulloa2024-jm]].
