---
title: "Curation bubbles"
aliases: ["Curation bubbles"]
authors: ["JON GREEN", "STEFAN MCCABE", "SARAH SHUGARS", "HANYU CHWE", "LUKE HORGAN", "SHUYANG CAO", "DAVID LAZER"]
year: 2025
doi: 10.1017/s0003055424000984
bibtex_key: Green2025-ap
topics: [political-polarization-partisan-news, computational-network-structure-analysis]
citation_count: 12
open_access: false
source_url: https://doi.org/10.1017/s0003055424000984
podcast_url: 
pdf_available: true
discovery_date: 2025-01-15T00:00:00Z
---

# Curation bubbles

> GREEN, J., MCCABE, S., SHUGARS, S., CHWE, H., HORGAN, L., CAO, S., & LAZER, D. (2025). Curation bubbles. *American Political Science Review*, 1–19. https://doi.org/10.1017/s0003055424000984
>
> [View paper](https://doi.org/10.1017/s0003055424000984)

## Summary

Green and colleagues argue that social media information consumption is structured by *networked curation*: users follow others who selectively unbundle stories from their parent outlets and re-bundle them according to identity and partisan appeal. They introduce the concept of **partisan curation bubbles** — audiences that consume partisan-consistent stories drawn from diverse sources — and show that conventional domain-level measures of audience partisanship systematically mischaracterize moderate outlets by averaging away substantial story-level heterogeneity. The implication is both methodological (URL-level measurement is necessary) and theoretical (polarized consumption can reflect ordinary democratic identity performance rather than algorithmic pathology).

## Key Contributions

- Introduces "partisan curation bubbles" as a framework distinct from echo chambers and filter bubbles, locating selectivity at the story level within networked sharing rather than at source selection.
- Provides a measurement critique showing that domain-level audience partisanship scores conflate heterogeneity with moderation, especially for centrist-scoring outlets.
- Delivers cross-platform empirical evidence using both Twitter (voter-file-matched panel) and Facebook (FORT URL Shares) data, spanning productive (sharing) and consumptive (views, clicks, reactions) behaviors.
- Reconciles findings that aggregate source exposure looks diverse with evidence that actual story-level consumption is partisan-homogeneous.
- Reframes polarized consumption as partly a participatory, identity-expressive practice rather than purely a democratic harm.

## Methods

The authors analyze ~369,675 political URLs from 718 domains shared by ~1.6M Twitter users (2017–2018) matched to TargetSmart voter-file partisanship scores, and ~214,995 political URLs from 780 domains in the Facebook FORT URL Shares dataset (2017–2021). URLs are classified as political via a CNN with GloVe embeddings (99% precision, 92% recall). Audience partisanship is scored on [−1,1] by averaging partisanship of users engaging with each URL/domain. They compare URL- and domain-level distributions using KS and Wasserstein tests, use equivalence-style tests (CI widened by 0.1) to identify URLs substantively distinct from their parent domain, and validate against hand-coded partisan appeal on 1,000 URLs (Krippendorff's α = 0.673).

## Findings

- URL-level audience score distributions are significantly more extreme than domain-level distributions on both Twitter (KS D = 0.23) and Facebook (KS D = 0.12).
- Story-level heterogeneity holds for consumption (views, clicks, reactions), with public-facing behaviors (shares, reactions) more extreme than private ones (clicks, views).
- Hand-coded partisan appeal correlates strongly with URL-level scores (r = 0.75) but much less with domain-level scores (r = 0.55); domain scores add little explanatory power once URL scores are included.
- The share of stories substantively distinct from their domain's mean rises sharply as domain scores approach zero: extreme outlets (Breitbart, Daily Kos, Fox) are uniform, while moderate-scoring outlets (WSJ, Mediaite, NY Post) are highly heterogeneous.
- Case example: the *Wall Street Journal*'s moderate domain score (−0.34) masks that its most Republican-shared content is conservative editorial while its most Democratic-shared content is mainstream reporting unfavorable to Republicans.
- For unlikely Democrats, right-leaning sharing rises from 28% (domain measure) to 39.1% (URL measure), showing users extract partisan-congruent stories from cross-cutting sources.

## Connections

This paper directly extends and complicates [[Bakshy2015-rn]]'s domain-level account of exposure diversity on Facebook, arguing its measurement strategy understates partisan homogeneity at the story level. The curation-bubble framework speaks to ongoing debates about whether echo chambers are real or overstated, connecting to work like [[Bruns2025-fz]] on echo-chamber discourse and [[Bennett2025-xs]] on selective exposure, while the methodological move toward URL- and audience-level partisan scoring resonates with [[Bouchaud2026-lr]] and computational audience-measurement efforts such as [[Ulloa2024-jm]].
