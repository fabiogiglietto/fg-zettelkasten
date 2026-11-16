---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, italian-political-communication]
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

This paper introduces a circular, iterative workflow for keeping lists of coordinated social media accounts current, addressing the well-known decay of static actor lists as malicious operators adapt, get suspended, or shift assets. Starting from a seed list of known coordinated accounts, the system polls their overperforming posts every six hours via platform APIs and applies near-duplicate detection across links, image-text pairs, and message content to surface previously unknown accounts engaged in the same coordinated behaviors. Applied to the 2022 Italian snap election, the workflow expanded an initial 435-account seed into hundreds of newly detected coordinated accounts, revealing three qualitatively distinct operations: a hyperpartisan Five Star Movement echo-chamber network, a religious-clickbait click-economy scheme, and a Church of Almighty God proselytism operation using Messenger bots. The authors argue the approach is behavior- and content-agnostic, portable across platforms, and better suited than static lists or content-based methods to producing accurate prevalence estimates of information operations.

## Key Contributions

- A near-real-time iterative workflow that dynamically updates coordinated-account lists rather than relying on manual, static compilations.
- Extension of Coordinated Link Sharing Behavior (CLSB) detection with Coordinated Image-Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), capturing adaptation tactics such as moving links into comments.
- Empirical demonstration on the 2022 Italian election with three documented case studies spanning ideological, economic, and religious motivations.
- A behaviorally agnostic alert system for journalists, fact-checkers, and researchers, framed with appropriate caveats about not equating coordination with harm.
- Discussion of portability to other platforms under the EU Digital Services Act Article 40 data access regime.

## Methods

The authors built an R-based pipeline scheduled via cronR to query the CrowdTangle posts/search API four times daily (July 28–September 25, 2022), retrieving top overperforming posts from a seed of 435 previously identified coordinated Italian accounts plus posts from the top 10% of newly detected accounts. Overperformance was assessed via CrowdTangle's score augmented by a comment/share ratio metric. CooRnet was applied with a 30-second coordination interval and a repetition threshold at the 0.995 percentile (≥26 shares) to detect CLSB, complemented by CITSB and CMSB (cosine similarity > .7). Political posts were filtered via keyword lists of parties, leaders, and institutions with capitalization heuristics. Surfaced networks were analyzed using François's A-B-C framework, with URL sources classified as Facebook-internal vs. external and news reliability rated via NewsGuard.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 additional generic coordinated accounts beyond the seed.
- The M5S network (90 entities, ~1.5M potential reach) produced 534,353 posts in two months, averaging 6.2 posts/minute on election day and peaking above 50/minute, with 80% link-free posts and heavy Facebook-internal circulation — an echo chamber amplifying fabricated pro-M5S polls.
- A clickbait operation used two large religious Pages (~768,000 combined followers) to funnel devotional audiences toward misleading political clickbait headlines, with roughly two-thirds of their content unrelated to religion.
- A Church of Almighty God proselytism cluster spanned 1,390 groups in seven language clusters; the Italian subset (61 groups, 13 Pages, ~2M combined audience) exhibited anomalously high admin counts (avg 72.6/Page) and used Messenger bots to route users into undisclosed catechism chats.
- In the M5S network, only 2% of external links were NewsGuard-rated unreliable, but 76% were unrated; reliable links skewed toward ideologically aligned outlets.

## Connections

This work directly extends the authors' prior CLSB program on Italian elections and COVID-era coordination — see [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2019-882f1900]], [[F2020-6278a4aa]], and [[Iannelli2015-e0818c3e]] — and connects to their subsequent methodological refinements in [[Giglietto2025-1765bb4f]], [[Giglietto2025-1e9a0917]], and [[Giglietto2026-9b6a992d]]. Methodologically it sits alongside other CooRnet-derived and coordination-detection contributions such as [[Mannocci2025-ig]], [[Minici2024-tf]], and [[Luceri2025-tr]], and thematically speaks to work on election-time coordinated behavior including [[Kulichkina2026-zk]] and [[Graham2025-gp]].
