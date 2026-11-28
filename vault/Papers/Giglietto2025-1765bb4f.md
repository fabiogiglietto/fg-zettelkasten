---
title: "\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"
aliases: ["\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"]
authors: ["Fabio Giglietto"]
year: 2025
doi: 10.31235/osf.io/8dqag_v2
bibtex_key: Giglietto2025-1765bb4f
kind: own
topics: [platform-governance-regulation, political-communication-elections]
citation_count: 3
open_access: true
source_url: https://doi.org/10.31235/osf.io/8dqag_v2
podcast_url: 
pdf_available: true
discovery_date: 
---

# "A Pretty Blunt Approach": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility

> Giglietto, F. (2025). "A Pretty Blunt Approach": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility. *Center for Open Science*. https://doi.org/10.31235/osf.io/8dqag_v2
>
> [View paper](https://doi.org/10.31235/osf.io/8dqag_v2)

## Summary

This working paper provides the first independent empirical measurement of how Meta's 2021–2025 political content reduction policy affected the Facebook visibility of Italian parliamentarians, prominent politicians, and extremist accounts. Drawing on over 2.5 million posts collected via the DSA-enabled Meta Content Library, Giglietto uses a discovery-validation design with structural breakpoint detection to show that the policy materially suppressed the reach of elected officials — a 72% peak-to-trough decline for re-elected MPs — and that its effects in Italy emerged roughly ten months before Meta's announced global rollout. Meta's January 2025 reversal produced only a partial rebound. The paper reframes algorithmic visibility as democratic infrastructure and argues both that Meta's policy communication suffered a serious transparency deficit and that DSA-mandated research infrastructure nonetheless represents meaningful progress toward collaborative platform governance research.

## Key Contributions

- First independent empirical quantification of Meta's political content reduction policy on elected officials in a European democracy.
- A discovery-validation breakpoint-detection methodology designed for platform policy changes with opaque or ambiguous implementation timelines.
- Documentation of asymmetric effects across mainstream and extremist actors, including a volume-compensation mechanism that can undermine the policy's intended goals.
- Evidence of specific gaps between Meta's DSA transparency reporting and the observable impact of its ranking changes on democratic communication.
- A fully documented, reproducible R analytical pipeline and public producer lists to enable cross-country and cross-platform replication.
- A normative argument for collaborative rather than purely adversarial platform governance research.

## Methods

The study collected 2,529,933 Facebook posts from 901 accounts (Jan 2021–Nov 2025) through the Meta Content Library API within Meta's Secure Research Environment. Accounts were divided into four mutually exclusive groups: re-elected MPs (discovery sample) plus newly elected MPs, prominent non-parliamentary politicians, and extremist/alternative-media accounts (validation samples). "Views" was the primary outcome, with group-specific power-law imputation for posts censored at the 100-view threshold and accompanying sensitivity analyses. Structural breakpoints were detected on weekly aggregated engagement metrics using both Bai–Perron and PELT algorithms, with 30-day consensus clustering to cross-validate break locations. The resulting four policy phases were compared using Kruskal–Wallis tests with Dunn's post-hoc pairwise comparisons (Bonferroni corrected), and a robustness check contrasted per-post average reach against total weekly reach to control for posting frequency.

## Findings

- Three cross-validated breakpoints emerged: T1 (19 Sept 2021, implementation), T2 (1 Jan 2023, post-election adjustment), and T3 (9 March 2025, reversal).
- Re-elected MPs' mean weekly views per post fell from 53,368 to 26,079 (–51%) at T1, then to 14,869 at T2, before partially recovering to 34,918 after T3 — about 65% of pre-policy levels.
- Peak-to-trough declines were 72.1% (re-elected MPs), 51.2% (new MPs), 57.3% (prominent politicians), and only 24.3% (extremists).
- The expected DOWN→DOWN→UP pattern held for all three mainstream groups, but extremists showed DOWN→DOWN→DOWN in per-post reach with no significant recovery.
- Measured as *total* weekly reach, extremists grew continuously (+13.7% from Phase 0 to Phase 2), surpassing mainstream politicians in aggregate visibility by increasing posting frequency 61.5–140.5%.
- The implementation breakpoint preceded Meta's announced global rollout by ~303 days; the reversal breakpoint followed Meta's January 2025 announcement by ~61 days.

## Connections

This paper sits within the author's own ongoing program on platform algorithms, elections, and data access, extending methods and concerns found in [[Giglietto2024-cbeb3f70]], [[Giglietto2023-fa71a001]], [[Giglietto2026-632ef967]], and [[Giglietto2025-ed60bc90]]. Its concern with DSA-enabled transparency infrastructure and the limits of platform self-reporting connects it to broader debates on platform governance and data access in [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Votta2025-xz]]. Its framing of algorithmic reach as democratic infrastructure and its explicit engagement with the US-centric 2020 US Election study link it to work on algorithmic curation and exposure such as [[Gonzalez-Bailon2024-rq]] and [[Bakshy2015-rn]].
