---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, elections-political-communication]
citation_count: 20
open_access: true
source_url: https://doi.org/10.1177/20563051231196866
podcast_url: 
pdf_available: true
discovery_date: 
---

# A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election

> Giglietto, F., Marino, G., Mincigrucci, R., & Stanziano, A. (2023). A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election. *Social Media + Society*. https://doi.org/10.1177/20563051231196866
>
> [View paper](https://doi.org/10.1177/20563051231196866)

## Summary

This paper proposes an iterative workflow to keep lists of coordinated social media accounts current rather than allowing them to decay as bad actors adapt, migrate, or get suspended. Starting from a seed of known coordinated accounts, the system polls their overperforming posts every six hours via the CrowdTangle API and applies near-duplicate detection across links, image-text, and messages to surface newly coordinating accounts, which then feed back into the monitored set. Applied to the 2022 Italian snap election, the workflow expanded an initial 435-account seed by hundreds of new coordinated accounts and revealed three qualitatively distinct operations — a Five Star Movement hyperpartisan echo chamber, a religious-Page clickbait network, and a Church of Almighty God proselytism operation using Messenger bots — demonstrating that a behavior- and actor-agnostic approach can flag ideological, economic, and religious coordination alike.

## Key Contributions

- A circular, near-real-time workflow for **updating** rather than merely compiling lists of coordinated accounts.
- Extension of Coordinated Link Sharing Behavior (CLSB) detection with Coordinated Image-Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), addressing adaptations such as hiding links in comments.
- Empirical demonstration on the 2022 Italian election, with three documented case studies spanning ideological, economic, and religious motivations.
- A behavior-agnostic alerting logic for fact-checkers and researchers, framed cautiously so that flagged accounts are treated as leads rather than verdicts.
- A discussion of platform portability under the EU Digital Services Act Article 40 data access regime.

## Methods

The authors seeded the pipeline with 435 coordinated accounts identified in prior Italian CLSB studies (2018, 2019, COVID). An R script scheduled via cronR queried CrowdTangle every six hours for the top overperforming political and general posts, plus content from the top 10% of newly detected accounts. CooRnet was run with a 30-second coordination interval and a 26+ share threshold at the 0.995 percentile to detect CLSB; CITSB and CMSB used near-duplicate matching (text cosine similarity > .7). Political filtering relied on a keyword list of parties, leaders, and institutions with capitalization heuristics. Surfaced networks were analyzed using François's A-B-C (Actors–Behavior–Content) framework, with URL sources classified as Facebook-internal vs. external and reliability assessed via NewsGuard ratings.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 additional generic coordinated accounts beyond the seed.
- **M5S network**: 90 entities, potential reach ~1.55M users, 534,353 posts in two months, peaking above 50 posts/minute on election day; 80% of posts had no links and most links were Facebook-internal, sustaining an echo chamber that circulated fabricated pro-M5S polls.
- **Clickbait network**: 46 Pages publishing 58,035 posts; two religious Pages ("La Preghiera di Oggi", "Santa Rita da Cascia") with ~768,000 combined followers used misleading headlines to expose religious audiences to political clickbait.
- **Church of Almighty God**: 1,390 public groups across seven language clusters; the Italian subset had 61 groups (~1.72M members) and 13 Pages (~294K subscribers), with abnormally many admins (avg 72.6) and Messenger bots funneling users into catechism chats without disclosing affiliation.
- Only 2% of external links in the M5S network came from NewsGuard-rated unreliable sources, but 76% were unrated, with reliable links skewing toward outlets ideologically aligned with M5S.

## Connections

This paper is an explicit methodological extension of the authors' prior CLSB program on Italian elections and COVID-era information operations — see [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2019-882f1900]], and [[F2020-6278a4aa]] — and connects to more recent refinements and applications of the CooRnet/CLSB paradigm in [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], and [[Giglietto2026-9b6a992d]]. Its behavior-first, actor-agnostic stance sits alongside broader debates on defining and detecting coordinated inauthentic behavior discussed in [[Graham2026-fb]], [[Graham2025-gp]], and [[Starbird2025-jj]], and speaks to work on cross-platform monitoring pipelines such as [[Minici2024-tf]] and [[Luceri2025-tr]]. The Italian election context also connects to [[Iannelli2015-e0818c3e]] and [[Iannucci2025-eg]].
