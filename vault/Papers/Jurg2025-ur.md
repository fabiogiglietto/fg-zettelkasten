---
title: "Ranking authority: A critical audit of YouTube’s content moderation"
aliases: ["Ranking authority: A critical audit of YouTube’s content moderation"]
authors: ["Daniel Jurg", "Salvatore Romano", "Bernhard Rieder"]
year: 2025
doi: 10.31219/osf.io/j3cn5_v1
bibtex_key: Jurg2025-ur
topics: [platform-data-access-and-governance, cross-national-digital-campaign-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31219/osf.io/j3cn5_v1
podcast_url: 
pdf_available: true
discovery_date: 2025-07-15T00:00:00Z
---

# Ranking authority: A critical audit of YouTube’s content moderation

> Jurg, D., Romano, S., & Rieder, B. (2025). Ranking authority: A critical audit of YouTube’s content moderation. https://doi.org/10.31219/osf.io/j3cn5_v1
>
> [View paper](https://doi.org/10.31219/osf.io/j3cn5_v1)

## Summary

This chapter conducts a critical audit of YouTube's content moderation during the 2024 European Parliamentary elections, focusing on two of the platform's stated commitments: raising authoritative sources and removing harmful content. Combining browser-based scraping of search results across the Netherlands, Germany, and France with an API sample of 8,142 election-related videos, the authors interrogate which sources are algorithmically privileged, how the "News Funding Notice" publisher context label is deployed, and how content removals are communicated to users. They argue that YouTube's post-"Adpocalypse" turn toward authoritative sources systematically favors legacy media and Public Service Media over natively digital creators, while its transparency instruments — publisher labels and removal statements — are inconsistently applied and deliberately opaque. The paper reframes transparency as "observability" and calls for expanded, scalable researcher data access via the YouTube Research Program.

## Key Contributions

- An empirical, election-focused audit of YouTube moderation under the EU Digital Services Act regime.
- Documentation of previously underreported inconsistencies in publisher context labeling across broadcasters and EU languages.
- A "critical audit" methodology combining API and scraping techniques while reflexively examining the conditions of platform observability.
- A comparative empirical baseline for removal rates (election queries vs. a banned-influencer benchmark).
- Concrete policy recommendations: integrating label and removal-statement data into the Research API, adding a "historical mode" to counter recency bias, and linking the DSA Transparency Database to video/channel IDs.

## Methods

A hybrid audit drawing on Sandvig et al.'s typology of algorithm audits. Country-specific browser-based collection (from AI Forensics, May 2–July 7, 2024) captured the top-20 YouTube search results in the Netherlands, Germany, and France via local IPs, for both "neutral" and "adversarial" (anti-immigration) queries. Weekly API queries for "European Parliamentary election" (April 23–July 15, 2024) yielded 8,142 unique videos, with later metadata retrieval to identify removed content. Channels were classified into six categories (PSM, Legacy Media, Government, Political Parties, Natively Digital, Other). The authors systematically tested News Funding Notice visibility across countries and language settings using VPNs, scraped removal statements, used the Internet Archive for unavailable-video metadata, and benchmarked removals against a banned-influencer query (Andrew Tate, N=65,159).

## Findings

- Public Service Media dominate top search results in the Netherlands and Germany; legacy media is more prominent in France. 91% of PSM videos in the dataset carried a News Funding Notice.
- News Funding Notices are inconsistently applied: TRT Français lacks one while other TRT branches have it; RTBF is labeled but its subsidiary RTBF Info is not; several regional broadcasters (L1 Limburg, Omroep Flevoland) and Ongehoord Nederland are unlabeled.
- Labels are entirely absent in Finnish, Greek, Danish, Catalan, Basque, Galician, and European Portuguese settings — though available for Brazilian Portuguese.
- Of the 8,142 election videos, 486 (6%) became unavailable, versus 26% in the Andrew Tate sample.
- Removal statements fall into six categories, mostly attributing unavailability to channel-level terminations; only four videos were explicitly flagged for Terms of Service violations.
- YouTube communicates removals via Terms of Service rather than Community Guidelines, and provides more detail on channel pages than on the removed video link. Two ToS case studies show specific videos removed while borderline channels remained active.

## Connections

This paper is part of a broader European effort using platform auditing and data-access tooling to study election-period governance; it connects closely to work on YouTube data infrastructures and observability such as [[Rieder2026-pp]] and [[Rieder2025-ju], and to platform-governance and data-access studies including [[Bruns2026-yv]] and [[Bechmann2026-dr]]. Its concern with DSA-era transparency and researcher access resonates with the wider platform-governance-and-data-access literature grouped here, while its focus on authoritative-source promotion and news labeling touches adjacent work on media visibility and moderation.
