---
title: "The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic"
aliases: ["The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic"]
authors: ["Yunya Song", "Yin Zhang", "Sheng Zou", "Xian Yang", "Qintao Huang"]
year: 2025
doi: 10.1007/s42001-025-00401-y
bibtex_key: Song2025-yh
topics: [coordinated-inauthentic-behavior, health-misinformation-and-fact-checking]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1007/s42001-025-00401-y
podcast_url: 
pdf_available: true
discovery_date: 2025-11-15T00:00:00Z
---

# The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic

> Song, Y., Zhang, Y., Zou, S., Yang, X., & Huang, Q. (2025). The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic. *Journal of Computational Social Science*, *8*. https://doi.org/10.1007/s42001-025-00401-y
>
> [View paper](https://doi.org/10.1007/s42001-025-00401-y)

## Summary

This study conducts a cross-national comparison of coordinated link sharing behavior (CLSB) surrounding COVID-19 vaccine discourse on Facebook in the UK and US. Drawing on a corpus of nearly 3.5 million public posts, the authors combine stance classification, network analysis, URL fact-checking, and structural topic modeling to characterize who coordinates, how credible the shared content is, and what narratives are amplified. Their central argument is that CLSB is ideologically agnostic — it is not inherently malicious but rather a scalable dissemination tactic used by both anti-vaccine communities spreading problematic content and pro-vaccine actors circulating institutional, evidence-based messaging. The disaggregation by nation reveals that coordination strategies and thematic emphases are strongly shaped by local political culture.

## Key Contributions

- One of the first systematic cross-national comparisons of vaccine-related CLSB across the UK and US.
- Complicates the framing of CLSB as inherently malicious by demonstrating its dual use for both misinformation and credible public health communication.
- Extends Xu and Wang's approach into a six-metric framework for characterizing coordinated link sharing networks.
- Integrates network analysis, fact-checking, and structural topic modeling to jointly map actors, content authenticity, and narrative themes.
- Draws implications for culturally and politically tailored public health communication that could leverage CLSB constructively.

## Methods

- Collected 3,469,719 English-language public Facebook posts (Jan 2020–Oct 2022) via CrowdTangle using COVID-19 and vaccine keywords/hashtags.
- Stance classification with a CT-BERT transfer-learning model trained on 5,000 annotated posts (κ = 0.86), yielding four subsets: UK-Anti, UK-Pro, US-Anti, US-Pro.
- CLSB detection using the CooRnet R package, identifying entities sharing identical URLs within unusually short intervals, followed by network component and structural analysis (density, modularity, clustering, diameter).
- Manual fact-checking of unique URLs via Google's Fact Check Explorer (Problematic / True / Unknown; 94.6% inter-coder agreement).
- Structural Topic Modeling (14-topic models) with publication date and country as covariates.

## Findings

- CLSB constituted a substantial share of network activity: 61.5% of nodes in UK-Anti, 38.5% in UK-Pro, 49.8% in US-Anti, and 57.6% in US-Pro networks.
- UK anti-vaccine networks were densest (density 0.01, avg degree 21.88); US pro-vaccine networks had the highest average degree (27.54) and largest entity count.
- Only 9.6% of UK-Anti URLs verified as true versus 45.6% for UK-Pro; 12% of US-Anti versus 40.4% for US-Pro. Anti-vaccine networks carried ~74–80% "Unknown" content.
- Anti-vaccine topics: Vaccine Safety Issues (59.1%), Vaccine Refusal (27.3%), Criticism of Politicians/Big Pharma (13.5%).
- Pro-vaccine topics: Effectiveness and Safety (38.5%), Vaccination Progress (34.2%), Efficacy Evidence (27.2%).
- National framing diverged: UK anti-vaccine discourse stressed safety and trial concerns (e.g., AstraZeneca), while US anti-vaccine discourse foregrounded individual freedom and religious exemption; pro-vaccine actors were institutionally grounded (NHS, CDC, hospitals).

## Connections

This paper sits within CLSB scholarship built on the CooRnet toolkit and coordinated link sharing framework developed by Giglietto and colleagues — see [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], and [[Giglietto2026-9b6a992d]]. Its focus on COVID-19 vaccine and health misinformation networks connects it to [[Di-Marco2025-aa]], while its argument that coordination is not inherently inauthentic or malicious speaks to methodological debates about detecting and interpreting coordinated behavior found in [[Luceri2025-tr]] and [[Minici2024-tf]].
