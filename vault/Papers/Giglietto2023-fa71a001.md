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

This paper proposes an iterative workflow for keeping lists of coordinated social media accounts up to date, addressing the fact that static actor lists decay quickly as accounts get suspended, pivot, or recruit new assets. Starting from a seed of 435 previously identified coordinated Italian accounts, the authors schedule API queries every six hours to retrieve overperforming political posts and then apply CooRnet-based detection of Coordinated Link, Image-Text, and Message Sharing Behavior to surface new accounts engaged in the same patterns. Applied to the 2022 Italian snap election campaign, the workflow detected 620 previously unknown coordinated accounts and produced three illustrative case studies — a Five Star Movement hyperpartisan network, a clickbait operation laundering political content through religious pages, and a Church of Almighty God proselytism network using Messenger bots — demonstrating that the same behavioral signatures can reveal ideologically, economically, and religiously motivated operations.

## Key Contributions

- A circular, near-real-time workflow that continuously updates lists of coordinated accounts rather than relying on static, manually compiled inventories.
- Extension of Coordinated Link Sharing Behavior detection (CooRnet) with Coordinated Image-Text Sharing (CITSB) and Coordinated Message Sharing (CMSB, cosine similarity > .7), addressing evasion tactics such as moving links to comments.
- An empirical mapping of the 2022 Italian election information environment with three documented case studies spanning distinct motivations.
- A content- and actor-agnostic alert framework intended to triage investigations for fact-checkers, journalists, and researchers without prejudging harm.
- Discussion of portability to other platforms via emerging researcher APIs under the EU Digital Services Act Article 40.

## Methods

The authors compiled a seed list of 435 coordinated accounts from prior Italian CLSB studies (2018, 2019, COVID era), built on 73,842 links across 398,385 political posts. An R script scheduled via cronR queried CrowdTangle every 6 hours (July 28–September 25, 2022) for top overperforming political posts and posts from the top 10% of newly detected accounts. CooRnet was applied with a 30-second coordination interval and a 26+ share threshold (0.995 percentile), augmented by CITSB and CMSB detection. Political posts were filtered via a keyword list with capitalization checks. Surfaced cases were analyzed with François's A-B-C framework, NewsGuard reliability scoring, and a Facebook-internal vs. external URL taxonomy.

## Findings

- The workflow surfaced 1,022 overperforming political posts, 272 coordinated links, 66 new coordinated political accounts, and 554 generic coordinated accounts beyond the seed list.
- The M5S network comprised 90 entities reaching ~1.55M users and produced 534,353 posts in two months, peaking above 50 posts/minute on election day; 80% of posts contained no links, creating an echo chamber that circulated fabricated favorable polls.
- A clickbait cluster of 46 Pages — including two religious Pages reaching ~768,000 followers — posted two-thirds non-religious political clickbait, exposing devotional audiences to incidental political messaging.
- A Church of Almighty God operation spanned 1,390 groups across seven language clusters; its Italian subset (61 groups, 13 Pages, ~2M combined audience) used Messenger bots and unusually large administrator teams (avg. 72.6 per Page) to funnel users into undisclosed proselytism.
- Only 2% of external M5S-network links were NewsGuard-rated unreliable, but 76% were unrated, complicating reliability assessments that depend solely on such ratings.

## Connections

This paper directly extends the authors' prior CLSB program on Italian elections in [[Giglietto2022-0e951ac5]] and connects to subsequent refinements of coordination detection in [[Giglietto2026-9b6a992d]]. It sits alongside methodological work pushing beyond static or single-behavior detection — including [[Graham2025-gp]], [[Minici2024-tf]], and [[Luceri2025-tr]] — and shares the behavioral-signature orientation of [[Kulichkina2026-zk]] and [[Schroeder2026-im]]. Within the Italian electoral context, it is a natural companion to [[Iannucci2025-eg]], [[Mannocci2025-ig]], and [[Orlando2025-ul]].
