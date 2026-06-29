---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, elections-political-communication]
citation_count: 7
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

This paper introduces a circular, near-real-time workflow for detecting, monitoring, and continuously updating lists of coordinated social media accounts spreading problematic information. The authors argue that static, manually compiled lists of malicious actors decay quickly as accounts adapt, get suspended, or switch assets, leading to systematic underestimation of information operations' reach. Their solution leverages the coordinated behavior of already-known actors as a seed: by repeatedly scraping their overperforming posts via API and applying near-duplicate detection across links, image-text pairs, and message content, the system iteratively surfaces new accounts engaged in coordinated sharing. Applied to the 2022 Italian snap election, the workflow expanded an initial seed of 435 accounts by surfacing 620 additional coordinated accounts and revealed three structurally distinct operations: a hyperpartisan Five Star Movement echo chamber, a clickbait click-economy scheme exploiting religious Pages, and a covert religious proselytism network run by the Church of Almighty God.

## Key Contributions

- A novel iterative workflow that keeps lists of coordinated accounts current rather than treating detection as a one-shot exercise.
- An extension of Coordinated Link Sharing Behavior (CLSB) detection to also cover Coordinated Image Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), addressing actor adaptations such as moving links into comments.
- A behaviorally and ideologically agnostic alert system useful to fact-checkers, journalists, and researchers for triage rather than automatic harm attribution.
- An empirical demonstration on the 2022 Italian election yielding three contrasting case studies (political, economic, religious motivations).
- A discussion of portability to other platforms under emerging researcher API regimes and the EU Digital Services Act Article 40.

## Methods

The workflow combines scheduled CrowdTangle API queries (every 6 hours over the July 28–September 25, 2022 campaign) for overperforming posts, with CooRnet-based coordination detection (30-second window, 26+ share threshold at the 0.995 percentile) extended to images and near-duplicate text (cosine similarity > .7). A keyword-based political filter (party names, leaders, institutions) with capitalization checks reduces false positives. The seed was 435 accounts derived from prior CLSB studies of Italian elections and COVID-19. Surfaced cases were analyzed through François's A-B-C (Actors–Behavior–Content) framework, with URL sources classified as Facebook-internal vs. external and reliability assessed via NewsGuard.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the seed.
- **M5S hyperpartisan network**: 90 entities reaching ~1.55M users, publishing 534,353 posts in two months and averaging 6.2 posts/minute on election day (peaks >50/min). 80% of posts contained no links; most linked content was Facebook-internal, indicating a self-referential echo chamber circulating fabricated polls favoring M5S.
- **Clickbait operation**: 46 Pages including two religious Pages ("La Preghiera di Oggi", "Santa Rita da Cascia") with ~768K combined followers; two-thirds of their content was non-religious political clickbait with misleading headlines, incidentally exposing devout audiences to politicized content for ad revenue.
- **Church of Almighty God**: 1,390 groups across seven language clusters; the Italian subset (61 groups, 1.72M members; 13 Pages, 295K subscribers) used Messenger bots to funnel users into undisclosed catechism chats, with Pages showing anomalously many administrators (avg 72.6).
- Only 2% of external links in the M5S network came from NewsGuard-rated unreliable sources, but 76% were unrated, complicating reliability-based assessment.

## Connections

This paper is a direct methodological extension of the authors' prior CLSB program on Italian elections and COVID-19 disinformation, including [[Giglietto2022-b30e8b4e]], [[Giglietto2022-0e951ac5]], [[Giglietto2020-9d8acdd7]], and [[Iannelli2018-ebd918b7]], and shares concerns with subsequent CooRnet-based and coordination-detection work such as [[Giglietto2026-9b6a992d]], [[Giglietto2026-855a54cb]], [[Graham2025-gp]], and [[Schroeder2026-im]]. Its emphasis on iteratively updating actor lists and on behavior-based rather than content-based detection resonates with broader methodological reflections in [[Bruns2025-fz]] and [[Rieder2025-ju]], while the case of bot-mediated religious proselytism connects to recent work on automated and inauthentic account behavior such as [[Minici2024-tf]] and [[Luceri2025-tr]].
