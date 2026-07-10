---
title: "\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"
aliases: ["\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"]
authors: ["Fabio Giglietto"]
year: 2025
doi: 10.31235/osf.io/8dqag_v2
bibtex_key: Giglietto2025-1765bb4f
kind: own
topics: [platform-governance-data-access, italian-election-media-mapping]
citation_count: 2
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

This working paper provides the first independent empirical audit of how Meta's 2021–2025 political content reduction policy affected the Facebook visibility of Italian elected officials and other political actors. Analyzing 2.5 million posts from 901 accounts via the Meta Content Library API, the author uses a discovery-validation design with structural breakpoint detection to show that the policy took effect in Italy roughly ten months before Meta's publicly announced July 2022 global rollout, cut re-elected MPs' average per-post reach by 72% at trough, and only partially reverted after Meta's January 2025 reversal. Crucially, extremist accounts offset per-post declines by dramatically increasing posting volume, ending the policy period with *more* aggregate weekly reach than mainstream politicians. The paper frames these results as evidence of significant transparency deficits in Meta's DSA compliance while nevertheless defending the DSA-enabled infrastructure as a genuine research advance worth building on collaboratively.

## Key Contributions

- First independent quantification of Meta's political content reduction policy on parliamentarians in a European democracy.
- A reusable discovery-validation breakpoint-detection methodology for auditing platform policy changes with opaque implementation timelines.
- Empirical documentation of asymmetric policy effects, including a volume-compensation mechanism through which extremist actors circumvented the intended suppression.
- Concrete evidence of gaps between Meta's DSA transparency reports and observable ranking effects on democratic communication.
- A fully documented, reproducible R pipeline and public producer lists enabling cross-country replication via the Meta Content Library.
- A normative articulation of collaborative platform governance research, drawing on the Knight-Georgetown Institute's "Better Access" framework.

## Methods

The study collects 2,529,933 Facebook posts (Jan 2021–Nov 2025) from 901 accounts through the Meta Content Library API inside Meta's Secure Research Environment, partitioned into four mutually exclusive actor groups: re-elected MPs (discovery sample), newly elected MPs, prominent non-parliamentary politicians, and extremist/alternative-media accounts (validation samples). Weekly aggregated views (with group-specific power-law imputation for the 100-view censoring threshold) are analyzed using both Bai–Perron and PELT breakpoint detection, with 30-day consensus clustering across algorithms. Detected phase boundaries structure Kruskal–Wallis tests with Bonferroni-corrected Dunn's post-hoc comparisons, and a robustness check contrasts per-post reach against total weekly reach to capture posting-frequency compensation.

## Findings

- Three cross-validated breakpoints: implementation (Sept 19, 2021), post-election adjustment (Jan 1, 2023), and reversal (March 9, 2025).
- The implementation breakpoint precedes Meta's announced global rollout by ~303 days; the reversal follows Meta's January 2025 announcement by ~61 days.
- Re-elected MPs: mean weekly views per post fell from 53,368 to a trough of 14,869 (–72%) and only recovered to 34,918 (~65% of baseline) after the reversal.
- Peak-to-trough declines: 72.1% (re-elected MPs), 51.2% (new MPs), 57.3% (prominent politicians), 24.3% (extremists).
- The expected DOWN→DOWN→UP pattern held for all three mainstream groups but not for extremists, whose per-post reach continued declining after the reversal.
- In *total weekly reach*, extremists grew 13.7% from Phase 0 to Phase 2 and overtook mainstream politicians, driven by a 61.5–140.5% increase in posting frequency.
- Meta did not disclose this policy in its DSA compliance reports, a substantive transparency gap.

## Connections

This paper extends the author's ongoing program on platform ranking effects and Italian political communication ([[Giglietto2026-632ef967]], [[Giglietto2025-1e9a0917]], [[Giglietto2025-ed60bc90]], [[Giglietto2026-855a54cb]], [[Giglietto2023-fa71a001]], [[Giglietto2022-b30e8b4e]], [[Giglietto2020-9d8acdd7]], [[Giglietto2019-882f1900]]) and speaks directly to broader debates on DSA-era transparency, data access, and platform-mediated research infrastructures ([[Rieder2026-pp]], [[Rieder2025-ju]], [[Bruns2026-yv]], [[Bechmann2026-dr]], [[Bouchaud2026-lr]], [[Bouchaud2026-np]]). Its finding that visibility suppression benefits high-volume extremist actors relative to mainstream politicians resonates with work on algorithmic amplification and electoral communication such as [[Gonzalez-Bailon2024-rq]], [[Bouchafra2026-ts]], and [[Larsson2026-ro]].
