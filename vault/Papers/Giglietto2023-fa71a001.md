---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, political-communication-elections]
citation_count: 25
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

This paper tackles a persistent methodological problem in studying coordinated social media behavior: lists of known problematic actors become stale almost as soon as they are compiled, because malicious operators adapt, get suspended, or migrate to new assets. The authors propose a circular, near-real-time workflow that begins with a seed list of known coordinated accounts, monitors their best-performing posts every few hours, and uses near-duplicate detection to surface *new* accounts engaged in coordinated sharing of links, image-text, or messages. Applied to the 2022 Italian snap election, the workflow expanded an initial list of 435 coordinated accounts by surfacing 620 newly detected ones, and the authors illustrate its outputs with three case studies spanning ideological, economic, and religious motivations. The approach is deliberately content- and actor-agnostic, targeting *behaviors* rather than predetermined individuals or content.

## Key Contributions

- Introduces an iterative workflow that continuously updates lists of coordinated accounts rather than relying on static, manually compiled lists.
- Extends prior Coordinated Link Sharing Behavior (CLSB) detection by adding Coordinated Image Text Sharing (CITSB) and Coordinated Message Sharing (CMSB), capturing adaptations like placing links in comments.
- Delivers an empirical application to the 2022 Italian election with three documented case studies (hyperpartisan network, clickbait operation, religious proselytism).
- Offers a behaviorally agnostic alert system for fact-checkers, journalists, and researchers — while cautioning that flagged actors are not automatically harmful.
- Discusses portability to other platforms via emerging researcher APIs in light of DSA Article 40 data access provisions.

## Methods

The authors built a circular pipeline combining scheduled API monitoring, overperformance scoring (CrowdTangle's overperforming score plus a combined metric weighting comment/share ratios), and coordination detection. A seed list of 435 coordinated accounts was compiled by running CooRnet over 73,842 links from prior Italian studies (2018, 2019, COVID-era). An R script scheduled via cronR queried the CrowdTangle posts/search API every six hours between July 28 and September 25, 2022, retrieving top overperforming political and unfiltered posts. CooRnet (30-second coordination interval, 26+ share repetition at the 0.995 percentile) detected CLSB, with extensions for CITSB and CMSB (cosine similarity > .7). Political posts were filtered via a keyword list with capitalization checks. The three surfaced cases were analyzed using François's A-B-C (Actors–Behavior–Content) framework, classifying URL sources and using NewsGuard ratings for reliability.

## Findings

- Beyond the 435-account seed, the workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts.
- **Case 1 (M5S network):** 90 entities with potential reach of ~1.55M users published 534,353 posts in two months (averaging 6.2 posts/min on election day, peaking above 50/min); 80% of posts had no links and most linked content was Facebook-internal — an echo-chamber environment circulating fabricated pro-M5S polls.
- **Case 2 (clickbait network):** 46 Pages published 58,035 posts; two religious Pages (~768K combined followers) posted two-thirds non-religious political clickbait with misleading headlines, exposing religious audiences to political content incidentally.
- **Case 3 (religious proselytism):** 1,390 public groups across seven language clusters tied to the Church of Almighty God; the Italian subset (61 groups, ~1.7M members; 13 Pages) used Messenger bots to funnel users into catechism chats without disclosing affiliation.
- In the M5S network, only 2% of external links came from NewsGuard-rated unreliable sources, but 76% were unrated — illustrating that reliability ratings alone poorly capture ideologically aligned amplification.

## Connections

This paper is a direct extension of the authors' long-running program on Coordinated Link Sharing Behavior and the CooRnet toolkit in Italian elections — see [[Giglietto2020-9d8acdd7]], [[Giglietto2020-6278a4aa]], [[Giglietto2019-882f1900]], [[Giglietto2022-0e951ac5]], and related methodological work in [[Giglietto2024-cbeb3f70]], [[Giglietto2025-1765bb4f]], and [[Marino2024-2fbc690f]]. Its behavior-focused, actor-agnostic stance connects to the broader coordinated inauthentic behavior literature represented by [[Nizzoli2020-cf]], [[Starbird2019-qv]], [[Keller2019-nk]], and [[Luceri2025-tr]], and its framing of problematic information draws on debates reflected in [[Benkler2018-lw]] and [[Allcott2017-yz]].
