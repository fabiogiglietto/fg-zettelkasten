---
title: "\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"
aliases: ["\"A Pretty Blunt Approach\": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility"]
authors: ["Fabio Giglietto"]
year: 2025
doi: 10.31235/osf.io/8dqag_v1
bibtex_key: Giglietto2025-1e9a0917
kind: own
topics: [platform-governance-and-data-access, italian-elections-political-communication]
citation_count: 0
open_access: true
source_url: https://doi.org/10.31235/osf.io/8dqag_v1
podcast_url: 
pdf_available: true
discovery_date: 
---

# "A Pretty Blunt Approach": Meta's Political Content Reduction Policy and Italian Parliamentarians' Facebook Visibility

## Summary

This working paper provides the first independent, large-scale empirical assessment of how Meta's 2021–2025 political content reduction policy affected the Facebook visibility of Italian parliamentarians. Drawing on over 2.5 million posts from 901 accounts collected through the Meta Content Library API, Giglietto uses a discovery-validation design with structural breakpoint detection to show that policy effects in Italy began roughly ten months before Meta's announced July 2022 global rollout, produced a 72% peak-to-trough collapse in per-post reach for re-elected MPs, and were only partially reversed after Meta's January 2025 rollback. A key twist: extremist accounts compensated for per-post declines by posting far more frequently, ending up with greater total weekly reach than mainstream politicians. The paper reads these findings simultaneously as evidence of transparency deficits in Meta's official disclosures and as a demonstration of the research value of DSA Article 40.12-enabled infrastructure, advocating a collaborative rather than purely adversarial model of platform research.

## Key Contributions

- First independent, large-scale empirical quantification of Meta's political content reduction policy on elected officials, focused on Italy.
- Documents a ~10-month gap between Meta's announced global rollout (July 2022) and the actual onset of effects in Italy (September 2021).
- Introduces a replicable discovery-validation pipeline combining Bai–Perron and PELT breakpoint detection with cross-group directional validation.
- Surfaces an asymmetric, potentially counterproductive effect: extremist accounts gained relative visibility through volume compensation.
- Demonstrates the practical research utility of the DSA-enabled Meta Content Library and releases open replication materials and a cross-country replication guide.

## Methods

- 2,529,933 Facebook posts from 901 accounts across 256 weeks (Jan 2021–Nov 2025), collected via the Meta Content Library API inside Meta's Secure Research Environment.
- Four mutually exclusive actor groups: re-elected MPs (discovery), plus newly elected MPs, prominent non-parliamentary politicians, and extremist/alternative-media accounts (validation).
- Two complementary breakpoint algorithms (Bai–Perron, PELT) applied to four weekly engagement metrics, with 30-day consensus clustering to retain cross-algorithm validated breakpoints.
- Censored view counts (≤100 views returned as NA) imputed via group-specific power-law ratio-weighting, with sensitivity analysis.
- Phase-based descriptive analysis, Kruskal–Wallis tests, and Bonferroni-corrected Dunn's post-hoc comparisons; robustness checks contrasting per-post reach against total weekly reach.

## Findings

- Three cross-validated breakpoints emerged: T1 (19 Sept 2021, implementation), T2 (1 Jan 2023, adjustment), and T3 (9 March 2025, reversal).
- Re-elected MPs lost 72.1% of mean per-post views peak-to-trough (53,368 → 14,869), via a 51% drop at T1 and a further 43% drop at T2.
- After the January 2025 reversal, reach rebounded 134.8% from the trough but recovered only to 65.4% of the pre-policy baseline.
- The expected DOWN→DOWN→UP pattern validated across re-elected MPs, new MPs, and prominent politicians (all p < 2×10⁻¹⁶), but extremist accounts showed an anomalous DOWN→DOWN→DOWN pattern with smaller per-post declines (−24.3%).
- Measured as total weekly reach, extremist accounts grew 13.7% from Phase 0 to Phase 2 and overtook mainstream politicians, driven by posting frequency increases of +61.5% and +140.5% in Phases 2 and 3.
- Mainstream actors reduced posting frequency during the policy period (e.g., prominent politicians −41.4% in Phase 2), compounding their per-post reach losses.

## Connections

This paper extends Giglietto's ongoing line of work on Italian political communication and platform dynamics, building methodologically and substantively on [[Giglietto2026-632ef967]], [[Giglietto2025-1765bb4f]], [[Giglietto2023-fa71a001]], and [[Giglietto2022-b30e8b4e]]. It speaks directly to platform-governance debates about the DSA's data-access regime and the politics of algorithmic visibility, resonating with [[Rieder2025-ju]], [[Rieder2026-pp]], [[Helmond2026-ll]], and [[Bruns2026-yv]], and connects to the broader concern with how content moderation and reduction policies reshape political information ecosystems addressed in [[Tornberg2025-ir]] and [[Bak-Coleman2025-pm]].
