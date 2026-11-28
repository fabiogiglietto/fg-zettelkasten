---
title: "Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"
aliases: ["Mapping Nefarious Social Media Actors to Speed-up Covid-19 Fact-checking"]
authors: ["Fabio Giglietto", "Manolo Farci", "Giada Marino", "Serena Mottola", "Tommaso Radicioni", "Massimo Terenzi"]
year: 2022
doi: 10.31235/osf.io/6umqs
bibtex_key: Giglietto2022-0e951ac5
kind: own
topics: [coordinated-inauthentic-behavior, health-misinformation]
citation_count: 9
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

This report documents the MINE-FACTS project, a collaboration that built and operationally tested a content-agnostic prototype to help Italian fact-checkers (Facta.news) identify problematic COVID-19 information on Facebook faster than manual triage allows. Building on the authors' prior work on Coordinated Link Sharing Behavior (CLSB) and the open-source CooRnet R package, the paper maps Italian "nefarious" social media networks at macro, meso, and micro levels, traces the emergence of an Italian covid-skeptic coordinated network during the pandemic's first wave, and catalogs the evasion tactics these actors use to circumvent platform enforcement. Its central argument is that behavior-based, content-agnostic detection can surface problematic content at a significantly higher hit rate than routine content-based fact-checking.

## Key Contributions

- An operational prototype integrating CooRnet, CrowdTangle, and IFCN false-claim data into a real-time fact-checking workflow.
- An up-to-date multi-scale (macro/meso/micro) map of Italian coordinated networks spreading COVID-19 misinformation.
- Documentation of novel evasion tactics: first-comment link placement, image-macro "link laundering," cross-platform monetization via shared AdSense IDs, and shape-shifting Page rebranding.
- Empirical evidence that content-agnostic, behavioral detection can outperform content-based triage for surfacing problematic information.
- A methodological demonstration of *iterative CooRnet seeding* to dynamically expand coordinated-account inventories.
- Open-source-intelligence reconstructions attributing specific domains, ad IDs, and individuals to disinformation operations.

## Methods

The authors seeded URL datasets from 212 IFCN-listed Italian false claims and from Meta's URL Shares dataset (Feb–June 2020), then applied CooRnet to detect CLSB across Facebook Pages, public groups, and verified profiles. Successive CooRnet iterations seeded new detection cycles from links posted by previously identified coordinated accounts. Macro-level structure was mapped via social network analysis (Force Atlas 2); meso-level case studies of four networks used Camille François's Actors-Behavior-Content (ABC) framework; and OSINT techniques (WHOIS, reverse WHOIS, AdSense/Analytics ID matching, Wayback Machine) attributed domains and actors. A one-month operational test (November 2021) evaluated the dashboard with Facta.news against a veracity typology.

## Findings

- Partisan, oversimplified COVID explanations (e.g. a bioweapon claim reaching 15M+ views, 5G–COVID videos) outperformed balanced content in circulation.
- From 212 false claims and 1,258 URLs, CooRnet surfaced 30 Pages (2.1M followers) and 308 public groups (2.73M members) in CLSB; conspiracy-group interactions roughly tripled during lockdown.
- The largest covid-skeptic cluster overlapped with League- and Five Star Movement-affiliated unofficial accounts, indicating the network emerged as an offshoot of pre-existing political coordinated clusters.
- The 2021 iteration tracked 2,151 accounts (242 Pages, 1,900 groups) across 89 components, with bridging groups connecting covid-skeptic, political, and religious clusters.
- Case studies revealed AdSense-monetized Blogspot cross-posting, a Catholic-group network injected with political content, GEDI-outlet "link laundering," and the Mag24 image-macro network traced via WHOIS/AdSense to a named individual.
- In testing, the prototype flagged ~40% of surfaced content as problematic versus ~28% in routine fact-checking — a significantly higher hit rate.
- The comments-to-shares ratio differs systematically: non-problematic content is dominated by shares, offering a useful ranking signal.

## Connections

This paper extends the authors' CooRnet-based research program on Coordinated Link Sharing Behavior, directly building on [[Giglietto2020-9d8acdd7]] and connecting to related Italian coordination work in [[Giglietto2023-fa71a001]], [[Marino2023-9137f448]] and [[Giglietto2019-0bd8b768]]. Its content-agnostic, behavior-first stance sits alongside broader coordination-detection methodology such as [[Nizzoli2020-cf]] and [[Keller2019-nk]], and its infodemic framing links to health-misinformation and fact-checking triage work including [[Allen2024-av]].
