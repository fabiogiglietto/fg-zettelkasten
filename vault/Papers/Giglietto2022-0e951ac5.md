---
title: "Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"
aliases: ["Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"]
authors: ["Fabio Giglietto", "Manolo Farci", "Giada Marino", "Serena Mottola", "Tommaso Radicioni", "Massimo Terenzi"]
year: 2022
doi: 10.31235/osf.io/6umqs
bibtex_key: Giglietto2022-0e951ac5
kind: own
topics: [coordinated-inauthentic-behavior, problematic-health-information]
citation_count: 8
open_access: true
source_url: https://doi.org/10.31235/osf.io/6umqs
podcast_url: 
pdf_available: true
discovery_date: 
---

# Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking

> Giglietto, F., Farci, M., Marino, G., Mottola, S., Radicioni, T., & Terenzi, M. (2022). Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking. *Center for Open Science*. https://doi.org/10.31235/osf.io/6umqs
>
> [View paper](https://doi.org/10.31235/osf.io/6umqs)

## Summary

This report documents the MINE-FACTS project, an Italian collaboration between researchers and the fact-checking outlet Facta.news that built a content-agnostic prototype for accelerating COVID-19 fact-checking on Facebook. Building on the authors' prior work on Coordinated Link Sharing Behavior (CLSB) and the CooRnet R package, the paper maps Italian "nefarious" actors at macro, meso, and micro scales; traces the emergence of a covid-skeptic coordinated network as an offshoot of pre-existing partisan clusters; and catalogues the evasion tactics these actors use to circumvent platform mitigations. A one-month operational test showed that behaviour-based triage surfaces problematic content at roughly 40% — significantly above the ~28% baseline rate of routine third-party fact-checking.

## Key Contributions

- An operational prototype integrating CooRnet, CrowdTangle, and IFCN databases into a fact-checker's workflow.
- A multi-scale (macro/meso/micro) map of Italian coordinated networks spreading COVID-19 misinformation.
- Documentation of novel evasion tactics: first-comment link placement, image-macro "link laundering," cross-site monetization via shared AdSense IDs, and Page rebranding.
- Empirical evidence that content-agnostic, behaviour-based detection outperforms content-based triage in surfacing problematic material.
- A methodological demonstration of iterative CooRnet seeding to dynamically expand inventories of coordinated accounts.
- OSINT reconstructions attributing specific disinformation operations (notably the Mag24 network) to identifiable individuals.

## Methods

- Meta's URL Shares dataset (FORT) for widely engaged Italian links (Feb–Jun 2020).
- CooRnet-based CLSB detection across Pages, public groups, and verified profiles, seeded from 212 IFCN false claims and 1,258 URLs, then iteratively re-seeded from links posted by previously flagged accounts.
- Social network analysis with Force Atlas 2 for macro-level cluster mapping.
- Qualitative meso-level case studies of four networks using Camille François's Actors–Behavior–Content (ABC) framework.
- OSINT (WHOIS, reverse WHOIS, AdSense/Analytics IDs, Wayback Machine) for actor attribution.
- One-month (November 2021) operational test with Facta.news rating outputs by a veracity typology.

## Findings

- Top-circulating Italian Facebook links in early 2020 included a Tgcom24 piece amplifying an "American expert" bioweapon claim (15M+ views) and removed YouTube videos linking 5G to COVID; partisan, oversimplified framings outperformed balanced ones.
- The initial iteration found 30 Pages (2.1M followers) and 308 groups (2.73M members) engaged in CLSB; interactions in conspiracy groups roughly tripled during lockdown versus a modest rise in non-conspiracy groups.
- A second iteration on October 2020 links yielded 344 coordinated accounts forming a giant political component with 5 conspiracy sub-clusters; the largest covid-skeptic cluster overlapped with League- and Five Star Movement-affiliated accounts.
- The 2021 iteration on 403,071 links produced 2,151 accounts across 89 components, with bridging groups tying together covid-skeptic, political, and religious clusters.
- Case studies exposed: a Blogspot conspiracy network monetized via shared AdSense IDs; a 62-group Catholic network intermittently injected with covid-skeptic content; a 31-Page network laundering links through GEDI-group outlets (Repubblica, tvzap, caffeinamagazine); and the long-running Mag24 network tied via WHOIS/AdSense to a named individual, using image macros with links in first comments.
- The prototype test surfaced 70 links / 360 posts with ~40% rated problematic, versus ~28% in routine fact-checking.
- Problematic content shows a distinctive comments-to-shares ratio, whereas non-problematic content is dominated by shares — a useful ranking signal.

## Connections

This paper is a direct extension of the authors' CLSB/CooRnet research program on the Italian information ecosystem, building on [[Giglietto2020-9d8acdd7]], [[Giglietto2019-882f1900]], [[Giglietto2023-fa71a001]], and [[Marino2023-9137f448]], and connects to their later work on partisan coordination in [[Giglietto2026-9b6a992d]]. Its content-agnostic, behaviour-based approach to detecting coordinated networks resonates with broader CIB detection efforts such as [[Luceri2025-tr]], [[Minici2024-tf]], and [[Graham2025-gp]], while the operational fact-checking angle links it to platform-manipulation studies like [[Kuznetsova2025-nu]].
