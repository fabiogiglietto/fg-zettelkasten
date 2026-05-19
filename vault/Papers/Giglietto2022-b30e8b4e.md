---
title: "Unexpected consequences of a simple threshold: the effect of the 100 public shares on Meta’s URL Shares Dataset"
aliases: ["Unexpected consequences of a simple threshold: the effect of the 100 public shares on Meta’s URL Shares Dataset"]
authors: ["Fabio Giglietto", "Luca Rossi", "Nicola Righetti"]
year: 2022
doi: 10.31235/osf.io/2p7ws
bibtex_key: Giglietto2022-b30e8b4e
kind: own
topics: [platform-governance-and-data-access, computational-social-science-methods]
citation_count: 0
open_access: true
source_url: https://doi.org/10.31235/osf.io/2p7ws
podcast_url: 
pdf_available: true
discovery_date: 
---

# Unexpected consequences of a simple threshold: the effect of the 100 public shares on Meta’s URL Shares Dataset

## Summary

This paper exposes a previously unrecognized artifact in Meta's URL Shares Dataset (released through Social Science One): the 100-public-shares threshold used for anonymization, when combined with platform-wide changes to Feed ranking, produces systematic distortions that can swamp the social signals researchers aim to study. Analyzing monthly URL, share, and comment volumes across 46 countries from 2017 to 2021, the authors find that highly heterogeneous national contexts produce nearly identical temporal trajectories—a similarity they attribute to algorithmic forces (notably Meaningful Social Interactions optimization) shifting the probability that URLs cross the censoring threshold. The apparent COVID-19 spike in early 2020, they show, is largely the tail of a trend that began in mid-2019. The paper is both a methodological warning and a concrete demonstration of how privacy-preserving data engineering and algorithmic curation become entangled in research datasets.

## Key Contributions

- Identifies a cross-country, platform-wide artifact in the URL Shares Dataset caused by the interaction between the 100-share threshold and Feed ranking changes.
- Provides empirical evidence that comparative and longitudinal analyses on this dataset risk mistaking algorithmic effects for social phenomena (including the COVID-19 "shock").
- Introduces a standardized shares–comments delta score that accounts for the dataset's differential-privacy noise (Appendix A).
- Links observed dataset patterns to documented and leaked changes in Meta's MSI Feed optimization, offering a plausible causal mechanism.

## Methods

- Descriptive analysis of monthly shares, comments, and URL counts across 46 countries (2017–2021), using 95% confidence intervals derived from the dataset's differential-privacy noise.
- Restriction to URLs whose `top_country` matched the user country, focusing on interactions within two months of publication.
- Construction of a z-scored shares–comments delta to compare interaction patterns under noise.
- Hierarchical clustering of countries using Euclidean distance over scaled monthly metrics.
- Interpretive triangulation with leaked Facebook internal documents and reporting on MSI/Feed changes.

## Findings

- Global shares and comments declined through 2017, rebounded in 2018, and peaked in February–March 2020 alongside the WHO pandemic declaration.
- The top ten countries by share volume exhibit nearly identical monthly trajectories; India (and partly Argentina) deviate only because of a known 2019 data gap.
- Restricting to local URLs and applying the standardized delta does not dissolve the cross-country similarity.
- Hierarchical clustering produces four country groups, but differences trace mostly to dataset artifacts (late onboarding, the India gap) rather than substantive local variation.
- From mid-2019 onward URL counts converge across nearly all countries (except four African ones), indicating algorithmic acceleration well before COVID-19.

## Connections

This paper sits squarely within the critical literature on the affordances and limits of Meta-provided research datasets, complementing infrastructural and political-economic critiques of platform data access such as [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Helmond2026-ll]]. Its concern that algorithmic curation contaminates measured social signals resonates with methodological cautions in [[Bak-Coleman2025-pm]] and [[Allen2025-ot]], and it pairs naturally with work examining how Feed ranking and engagement optimization shape observed information flows, including [[Bouchaud2026-lr]] and [[Bruns2025-fz]]. The 100-share threshold issue is also directly relevant to URL- and link-based research practice exemplified by [[Giglietto2024-cbeb3f70]].
