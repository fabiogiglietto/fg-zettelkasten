---
title: "Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"
aliases: ["Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"]
authors: ["Fabio Giglietto", "Manolo Farci", "Giada Marino", "Serena Mottola", "Tommaso Radicioni", "Massimo Terenzi"]
year: 2022
doi: 10.31235/osf.io/6umqs
bibtex_key: Giglietto2022-0e951ac5
kind: own
topics: [coordinated-inauthentic-behavior, problematic-health-information]
citation_count: 0
open_access: true
source_url: https://doi.org/10.31235/osf.io/6umqs
podcast_url: 
pdf_available: true
discovery_date: 
---

# Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking

## Summary

This report describes the MINE-FACTS project, which built and operationally tested a content-agnostic prototype tool to help Italian fact-checkers (notably Facta.news) surface problematic COVID-19 information on Facebook faster than manual triage allows. Building on Coordinated Link Sharing Behavior (CLSB) detection via the CooRnet R package, the authors map Italian "nefarious" coordinated networks at macro, meso, and micro scales, trace the rise of an Italian covid-skeptic coordinated network grafted onto pre-existing political clusters, and document the tactics these networks use to evade platform enforcement. A one-month live test showed the prototype flagged a substantially higher share of problematic content than routine third-party fact-checking workflows.

## Key Contributions

- An operational fact-checking prototype integrating CooRnet, CrowdTangle, and the IFCN CoronaVirusFacts database into Italian newsroom workflows.
- A multi-scale (macro/meso/micro) map of Italian coordinated networks spreading COVID-19 misinformation on Facebook.
- Documentation of novel evasion tactics: first-comment link placement, image-macro "link laundering," shared Google AdSense IDs across domains, and Page rebranding.
- Empirical evidence that behavior-based, content-agnostic detection outperforms content-based triage in identifying problematic content.
- A methodological demonstration of iterative CooRnet seeding, where links from already-identified coordinated accounts are used to discover new ones.
- OSINT-driven attribution (WHOIS, reverse WHOIS, AdSense/Analytics IDs, Wayback Machine) linking specific domains and operators to disinformation operations.

## Methods

The authors combine Meta's URL Shares dataset and CrowdTangle queries seeded from 212 IFCN-listed Italian false claims to build URL inventories, then apply CooRnet iteratively to detect CLSB across Facebook Pages, groups, and verified profiles. Macro-level structure is visualized with Force Atlas 2 network layouts; meso-level dynamics are examined through four qualitative case studies framed by Camille François's Actors-Behavior-Content (ABC) model; micro-level analysis assesses individual flagged posts. OSINT techniques attribute domains and actors, and a one-month November 2021 deployment with Facta.news tests the prototype in production.

## Findings

- February–June 2020 top Italian Facebook links favored partisan, oversimplified narratives, including a Tgcom24 piece amplifying a bioweapon claim (15M+ views) and removed 5G-COVID YouTube videos.
- Initial CooRnet runs identified 30 Pages (2.1M followers) and 308 groups (2.73M members) engaged in CLSB; conspiracy-group interactions roughly tripled during lockdown.
- Iterative seeding eventually surfaced 2,151 coordinated accounts (242 Pages, 1,900 groups) across 89 components, with the largest covid-skeptic cluster overlapping League- and Five Star Movement-affiliated accounts and bridging groups linking political, religious, and covid-skeptic communities.
- Case studies revealed (i) a Blogspot conspiracy-blog network monetized via shared AdSense IDs, (ii) a 62-group Catholic network occasionally injected with covid-skeptic content, (iii) a 31-Page network laundering traffic to reputable GEDI-group outlets, and (iv) the Mag24 image-macro network traced via WHOIS/AdSense to a specific operator.
- In the November 2021 test, ~40% of prototype-surfaced links/posts were rated problematic, versus ~28% in routine third-party fact-checking.
- The comments-to-shares ratio is a useful ranking signal: non-problematic content is dominated by shares, problematic content shows relatively more commenting.
- Unprincipled "celebrities" (Montagnier, Viganò, Kennedy) and covid-skeptic communities form a symbiotic amplification loop, and quoted false claims often evade fact-check labeling because the quote itself is authentic.

## Connections

This paper sits squarely in the CooRnet/CLSB research program developed by the same group, extending [[Giglietto2023-fa71a001]] and [[Marino2024-a678b03f]] with COVID-specific Italian network mapping and a fact-checker-facing tool; it also resonates with [[Ghezzi2023-8bebc91f]] on Italian problematic health information. Its content-agnostic, behavior-based detection logic connects to broader work on coordinated inauthentic behavior such as [[Luceri2025-tr]], [[Minici2024-tf]], and [[Graham2025-gp]], and to evasion-and-adaptation themes explored in [[Kuznetsova2025-nu]] and [[Schroeder2026-im]].
