---
title: "Coordinated link sharing on Facebook"
aliases: ["Coordinated link sharing on Facebook"]
authors: ["Yunkang Yang", "Ramesh Paudel", "Jordan McShan", "Matthew Hindman", "H. Howie Huang", "David Broniatowski"]
year: 2025
doi: 10.1038/s41598-025-00233-w
bibtex_key: Yang2025-iv
topics: [coordinated-inauthentic-behavior]
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

This paper proposes a new method for detecting coordinated link-sharing behavior on Facebook that reduces reliance on post-timing signals, which adversaries can easily manipulate. The authors argue that the *speed* and *frequency* of link sharing across accounts follow consistent statistical regularities, and that deviations from these regularities provide a more evasion-resistant signature of coordination. They validate the approach on a large corpus of 11.2 million Facebook link posts drawn from roughly 16,000 sources, positioning the work as a methodological contribution to platform integrity research and the broader study of coordinated inauthentic behavior.

## Key Contributions

- A coordination detection method that moves beyond timing-based signals, which are trivially gameable by sophisticated actors.
- Identification of statistical regularities in link-sharing speed and frequency that function as robust behavioral signatures.
- Empirical validation at scale using a corpus of 11.2 million Facebook link posts across ~16,000 sources.

## Methods

- Assembly of a large-scale Facebook link-sharing dataset (11.2M posts, ~16K sources).
- Statistical characterization of the distributions of sharing speed and frequency across accounts.
- Development of a detection procedure based on departures from these regularities.
- Empirical evaluation of the procedure on the assembled corpus.

## Findings

- Sharing speed and frequency exhibit stable, regular statistical patterns across accounts under normal conditions.
- Coordinated link-sharing activity produces detectable deviations from these regularities.
- The proposed signals function effectively at scale, suggesting practical viability for platform-level detection.

## Connections

This work sits squarely in the methodological strand of coordinated inauthentic behavior detection that critiques timing-based co-sharing approaches; it relates closely to [[Graham2025-gp]] and [[Graham2026-fb]]–style network methods, and to robustness/evasion concerns raised in [[Bouchaud2026-lr]] and [[Luceri2025-tr]]. It also complements broader CIB detection efforts such as [[Minici2024-tf]] and [[Kulichkina2026-zk]], which similarly seek behavioral signatures that go beyond temporal co-occurrence.
