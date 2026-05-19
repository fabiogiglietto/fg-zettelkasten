---
title: "A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"
aliases: ["A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election"]
authors: ["Fabio Giglietto", "Giada Marino", "Roberto Mincigrucci", "Anna Stanziano"]
year: 2023
doi: 10.1177/20563051231196866
bibtex_key: Giglietto2023-fa71a001
kind: own
topics: [coordinated-inauthentic-behavior, italian-elections-political-communication]
citation_count: 7
open_access: true
source_url: https://doi.org/10.1177/20563051231196866
podcast_url: 
pdf_available: true
discovery_date: 
---

# A Workflow to Detect, Monitor, and Update Lists of Coordinated Social Media Accounts Across Time: The Case of the 2022 Italian Election

## Summary

This article proposes a methodological workflow that addresses a recurring weakness in research on coordinated inauthentic behavior: lists of malicious or coordinated accounts decay rapidly as actors adapt, get suspended, or shift assets. Starting from a known seed of coordinated accounts, the authors iteratively monitor their overperforming posts via API and apply near-duplicate detection across links, image-text pairs, and messages to surface previously unknown accounts engaged in coordinated sharing. Applied to the 2022 Italian snap election, the workflow expanded an initial seed of 435 accounts by detecting 620 new coordinated accounts and produced three illustrative case studies spanning ideological, economic, and religious motivations, demonstrating that a behavior-focused, content-agnostic alert system can yield more accurate estimates of an operation's reach than static lists.

## Key Contributions

- A circular, near-real-time workflow for continuously updating lists of coordinated accounts rather than relying on static, manually curated rosters.
- Extension of Coordinated Link Sharing Behavior (CLSB) detection to Coordinated Image Text Sharing Behavior (CITSB) and Coordinated Message Sharing Behavior (CMSB), addressing evasion tactics like moving links into comments.
- An empirical application to the 2022 Italian election yielding three documented case studies (M5S hyperpartisan network, religious-clickbait operation, Church of Almighty God proselytism via Messenger bots).
- A content- and actor-agnostic alert system designed to help fact-checkers, journalists, and researchers prioritize investigations without prejudging harm.
- Discussion of portability to other platforms in light of the EU Digital Services Act Article 40 data access regime.

## Methods

The authors compiled a seed of 435 coordinated accounts by running CooRnet on 73,842 links from earlier Italian election and COVID-era studies. An R script (scheduled via cronR every six hours from 28 July to 25 September 2022) queried the CrowdTangle posts/search API for the top 100 overperforming political and unfiltered posts plus posts from the top 10% of newly detected accounts. Overperformance was measured using CrowdTangle's score combined with a comment/share ratio metric. CooRnet was applied with a 30-second coordination interval and a 26+ share repetition threshold (0.995 percentile) to detect CLSB; CITSB and CMSB (cosine similarity > .7) extended detection to images and near-duplicate text. Political filtering used keyword lists with capitalization checks. Case studies were analyzed using François's A-B-C framework, with URL classification (Facebook-internal vs. external) and NewsGuard ratings for source reliability.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 additional generic coordinated accounts beyond the seed list.
- The M5S network comprised 90 entities reaching ~1.5M users and producing 534,353 posts in two months, peaking above 50 posts/minute on election day; 80% of posts had no links and most linked content was Facebook-internal, indicating an echo-chamber circulating fabricated favorable polls.
- A clickbait network of 46 Pages used two large religious Pages (~768,000 combined followers) to post two-thirds non-religious political clickbait, exposing religiously oriented audiences to misleading political content.
- A religious proselytism cluster of 1,390 public groups across seven languages was tied to the Church of Almighty God; the Italian subset included 61 groups (1.7M members) and 13 Pages whose Messenger bots funneled users into catechism chats without disclosing affiliation.
- Only 2% of external M5S-network links were NewsGuard-rated unreliable, but 76% were unrated, with reliable links concentrated in ideologically aligned outlets.

## Connections

This paper builds directly on the authors' prior CLSB/CooRnet work on Italian elections — see [[Giglietto2026-9b6a992d]], Giglietto2025-1765bb4f, and Giglietto2025-1e9a0917 — and on broader Italian election-monitoring efforts such as [[Iannucci2025-eg]] and [[Mannocci2025-ig]]. Methodologically it sits alongside other coordination-detection pipelines and evaluations like [[Minici2024-tf]], [[Luceri2025-tr]], [[Graham2025-gp]], and [[Kulichkina2026-zk]], which similarly grapple with adapting detection to evolving coordinated behaviors across platforms.
