---
title: "Coordinated link sharing on Facebook"
aliases: ["Coordinated link sharing on Facebook"]
authors: ["Yunkang Yang", "Ramesh Paudel", "Jordan McShan", "Matthew Hindman", "H. Howie Huang", "David Broniatowski"]
year: 2025
doi: 10.1038/s41598-025-00233-w
bibtex_key: Yang2025-iv
topics: [coordinated-inauthentic-behavior, platform-data-access-methods]
citation_count: 4
open_access: false
source_url: https://doi.org/10.1038/s41598-025-00233-w
podcast_url: 
pdf_available: false
discovery_date: 2025-05-15T00:00:00Z
---

# Coordinated link sharing on Facebook

> Yang, Y., Paudel, R., McShan, J., Hindman, M., Huang, H. H., & Broniatowski, D. (2025). Coordinated link sharing on Facebook. *Scientific Reports*, *15*, 15684. https://doi.org/10.1038/s41598-025-00233-w
>
> [View paper](https://doi.org/10.1038/s41598-025-00233-w)

## Summary

This paper introduces a new method for detecting coordinated link-sharing behavior on Facebook that reduces reliance on post-timing signals, which manipulators can easily alter. The authors argue that while timing has been a mainstay of coordination detection, it is trivially manipulable and therefore vulnerable to evasion. Instead, they exploit statistical regularities in the *speed* and *frequency* of link sharing across accounts as more robust indicators of coordination. The approach is validated on a large corpus of 11.2 million Facebook link posts drawn from roughly 16,000 sources, positioning the work within computational social science and platform integrity research.

## Key Contributions

- A methodological advance in coordination detection that reduces dependence on easily manipulated post-timing features.
- Introduction of speed- and frequency-based statistical signatures as detection signals.
- Empirical application and validation at scale using millions of Facebook link posts.

## Methods

- Analysis of a large-scale Facebook dataset comprising 11.2 million link posts.
- Posts sourced from a curated list of roughly 16,000 accounts or domains.
- Statistical modeling of sharing speed and frequency distributions to identify coordinated activity.
- Empirical validation of the detection approach against this corpus.

## Findings

- Link-sharing speed and frequency display consistent statistical regularities across accounts.
- These regularities can be leveraged to detect coordinated sharing behavior on Facebook.
- The proposed signals offer a more evasion-resistant alternative to timing-based methods, validated on a large empirical dataset.

## Connections

This work sits squarely in the coordinated link-sharing detection tradition, most directly extending the coordinated link-sharing behavior (CLSB) framework developed across [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Giglietto2023-fa71a001]], whose reliance on temporal co-sharing this paper critiques and seeks to improve. Its focus on evasion-resistant, network-based coordination signals connects it to broader methodological efforts in [[Luceri2025-tr]] and [[Minici2024-tf]] on robust detection of coordinated inauthentic behavior.
