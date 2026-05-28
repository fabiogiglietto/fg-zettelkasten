---
title: "\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"
aliases: ["\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"]
authors: ["Fabio Giglietto"]
year: 2025
doi: 10.31235/osf.io/8dqag_v2
bibtex_key: Giglietto2025-1765bb4f
kind: own
topics: [platform-governance-and-data-access, italian-elections-political-communication]
citation_count: 0
open_access: true
source_url: https://doi.org/10.31235/osf.io/8dqag_v2
podcast_url: 
pdf_available: true
discovery_date: 
---

# "A Pretty Blunt Approach": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility

## Summary

This working paper provides the first independent empirical assessment of Meta's 2021–2025 political content reduction policy on the Facebook visibility of Italian parliamentarians and other political actors. Drawing on 2.5 million posts collected through the Meta Content Library, Giglietto uses a discovery-validation design with structural breakpoint detection to show that the policy suppressed re-elected MPs' per-post reach by 72% at its trough, began roughly ten months before Meta's announced global rollout, and only partially recovered after the January 2025 reversal. Critically, extremist accounts evaded the policy's intended effect by sharply increasing posting frequency, gaining aggregate weekly reach even as mainstream politicians lost it. The paper frames these results as evidence of serious transparency deficits in Meta's DSA reporting while affirming the research value of DSA-enabled data infrastructures.

## Key Contributions

- First independent empirical quantification of Meta's political content reduction policy effects on elected officials in a European democracy.
- A discovery-validation breakpoint-detection methodology designed for platform policy changes with opaque or ambiguous implementation timelines.
- Documentation of asymmetric effects across mainstream and extremist actors, including a posting-volume compensation mechanism that undermines policy intent.
- Identification of specific gaps between Meta's DSA transparency disclosures and empirically observable ranking-change impacts.
- A fully documented, reproducible R pipeline and public producer lists enabling cross-country replication via the Meta Content Library.
- A normative argument for collaborative — rather than purely adversarial — platform governance research grounded in current data-access realities.

## Methods

The study analyzes 2,529,933 posts from 901 Facebook accounts (Jan 2021–Nov 2025), collected through the Meta Content Library API within Meta's Secure Research Environment. Accounts are partitioned into four mutually exclusive groups: re-elected MPs (discovery), newly elected MPs, prominent non-parliamentary politicians, and extremist/alternative-media accounts (validation). Views — the primary outcome — are imputed for posts censored at the 100-view threshold using group-specific power-law fits, with sensitivity checks. Weekly aggregated views, reactions, shares, and comments are fed to Bai–Perron and PELT breakpoint detectors, with 30-day consensus clustering identifying validated changepoints. Resulting policy phases are compared via Kruskal–Wallis and Bonferroni-corrected Dunn's tests, and a robustness check contrasts per-post averages with total weekly reach.

## Findings

- Three robust breakpoints emerged: implementation (Sept 19, 2021), post-election adjustment (Jan 1, 2023), and reversal (March 9, 2025).
- Re-elected MPs' mean weekly views per post collapsed from 53,368 to 14,869 (–72% peak-to-trough) and recovered only to 34,918 (~65% of baseline) after the reversal.
- Peak-to-trough declines were 72.1% (re-elected MPs), 51.2% (new MPs), 57.3% (prominent politicians), but only 24.3% for extremists.
- The expected DOWN→DOWN→UP recovery pattern held for all mainstream groups but not for extremists, who showed no significant per-post recovery.
- Measured as total weekly reach, extremists grew +13.7% across phases and overtook mainstream politicians in aggregate visibility, driven by 61.5–140.5% increases in posting frequency.
- Italian implementation preceded Meta's announced July 2022 global rollout by ~303 days; the detected reversal lagged Meta's January 2025 announcement by ~61 days, consistent with gradual deployment.

## Connections

This paper extends the author's ongoing program on Italian political communication and platform-mediated visibility ([[Giglietto2026-632ef967]], [[Giglietto2025-1e9a0917]], [[Giglietto2023-fa71a001]], [[Giglietto2022-b30e8b4e]], [[Giglietto2020-9d8acdd7]], [[Giglietto2019-882f1900]], [[Marino2024-2fbc690f]], [[Rossi2023-847d5a9f]]) into the domain of algorithmic curation and policy auditing. It speaks directly to emerging work on DSA-era data access and Meta Content Library affordances ([[Rieder2025-ju]], [[Rieder2026-pp]], [[Bruns2026-yv]], [[Helmond2026-ll]]) and to critiques of platform transparency and governance ([[Bak-Coleman2025-pm]], [[Bak-Coleman2026-mk]], [[Schiffrin_undated-gi]], [[Farkas2026-lr]]). The finding that extremist accounts offset reach suppression via posting volume resonates with broader debates on demotion, amplification, and asymmetric platform effects ([[Allen2025-ot]], [[Pierri2025-hm]]).
