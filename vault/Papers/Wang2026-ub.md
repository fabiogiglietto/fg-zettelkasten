---
title: "The failed migration of academic Twitter: A case study of precocious adopters"
aliases: ["The failed migration of academic Twitter: A case study of precocious adopters"]
authors: ["Xinyu Wang", "Sai Koneru", "Sarah Rajtmajer"]
year: 2024
doi: 
bibtex_key: Wang2026-ub
topics: []
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2406.04005v3
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Wang2026-ub.mp3
pdf_available: true
discovery_date: 2026-03-22T08:20:48.605756Z
---

# The failed migration of academic Twitter: A case study of precocious adopters

> Wang, X., Koneru, S., & Rajtmajer, S. (2024). The failed migration of academic Twitter: A case study of precocious adopters. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2406.04005v3)

## Summary

This paper examines whether academic Twitter could successfully transplant itself to Mastodon after Musk's 2022 acquisition, tracking 7,542 self-identified scholarly early adopters over one year. Despite being a coordinated, highly motivated cohort with well-connected internal networks, most academics reduced activity or drifted back to Twitter, with active users falling from ~7,500 to ~2,400. The authors argue that decentralized affordances, fragmented attention across emerging alternatives (Bluesky, Threads), and the difficulty of porting accumulated social capital combined to produce an incomplete migration — though field-specific server communities like infosec.exchange retained users at substantially higher rates than general-purpose instances.

## Key Contributions

- A targeted longitudinal case study of a coordinated professional community's migration, complementing general-population Twitter-to-Mastodon studies.
- Introduction of a federated interaction diversity metric (Shannon entropy over target servers) shown to robustly predict retention.
- Integration of longitudinal tracking, network analysis, cross-platform matching, and Cox survival modeling to identify measurable retention predictors.
- Empirical evidence that discipline-specific Mastodon servers retain users far better than general-purpose ones.
- Documentation of divergent effects of prior Twitter follower size (risk) versus posting history (protective), illuminating how social capital constrains platform substitution.

## Methods

The authors curated 7,542 academic Mastodon accounts from a community-maintained GitHub list spanning 50 disciplines, collected weekly profile/engagement data via the Mastodon API (Nov 2022–Oct 2023), and retrospectively gathered interaction data (replies, boosts, mentions, favorites). They matched 3,131 scholars to Twitter accounts for cross-platform comparison, constructed follower and interaction networks aggregated by field and server, categorized users by active-span quartiles, and collected migration discourse via Zeeschuimer and hashtag scraping. Cox proportional hazards models (with L2 penalization and sensitivity checks across 14/30/60-day windows) estimated retention predictors in both Mastodon-centric and cross-platform variants.

## Findings

- Monthly active academic users dropped from 7,505 (Nov 2022) to 2,398 (Oct 2023); a brief July 2023 resurgence coincided with Twitter's rate limits and X rebrand.
- ~79.7% of matched scholars remained active on Twitter; only ~7.4% were both persistent on Mastodon and inactive/locked on Twitter.
- Information Security scholars on infosec.exchange showed ~40.9% persistent retention — far above comparably sized disciplines on general-purpose servers.
- The Mastodon follower network was hub-structured around mastodon.social (21.3% of academics), with cross-server ties supplemented by boosts/mentions.
- Cox model (concordance 0.69): protective factors included initial followers (HR=0.72), posts (HR=0.74), topic-specific server (HR=0.84), multidisciplinary identity (HR=0.59), and 30-day interaction diversity (HR=0.84); high server out-degree ratio was a risk factor (HR=1.80).
- Cross-platform model: larger Twitter following (HR=1.13) and followers (HR=1.11) increased Mastodon attrition; more Twitter posts (HR=0.92) and older Twitter accounts (HR=0.88) predicted retention.
- Of 626 scholars referencing Mastodon in Twitter bios, 308 also referenced Bluesky and 69 Threads — diffuse multi-platform exploration rather than concentrated migration.

## Connections

This study sits alongside other Mastodon and Fediverse migration research, most directly [[Bruns2025-fz]] and broader work on platform alternatives. It connects to the platform-governance strand examining post-Musk Twitter/X dynamics — including [[Bak-Coleman2025-pm]], [[Murtfeldt2025-wu]], and [[Hurcombe2025-cs]] — and to studies of cross-platform user behavior and data-access constraints exemplified by Davis-style work such as [[Ohme2026-nv]] and [[Helmond2026-ll]]. Methodologically, its use of survival modeling and federated network analysis complements computational approaches in [[Pierri2025-hm]] and Bastos2025-ol.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Wang2026-ub.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-academic-twitters-exodus-why-the/id1866587707?i=1000756565108)
