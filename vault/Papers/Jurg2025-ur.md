---
title: "Ranking authority: A critical audit of YouTube’s content moderation"
aliases: ["Ranking authority: A critical audit of YouTube’s content moderation"]
authors: ["Daniel Jurg", "Salvatore Romano", "Bernhard Rieder"]
year: 2025
doi: 10.31219/osf.io/j3cn5_v1
bibtex_key: Jurg2025-ur
topics: [platform-governance-apis, elections-political-communication]
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

This chapter audits YouTube's content moderation during the 2024 European Parliamentary elections, focusing on the platform's twin commitments to elevate authoritative sources and remove harmful content. Combining browser-based scraping of search results in the Netherlands, Germany, and France with an API-collected sample of 8,142 election-related videos, Jurg, Romano, and Rieder show that legacy and Public Service Media dominate algorithmic rankings, that the "News Funding Notice" publisher context label is applied inconsistently across broadcasters and entirely missing in several EU languages, and that removal statements to users are vague and obfuscate the platform's own role. The authors argue that meaningful auditing under the Digital Services Act requires reconceiving transparency as "observability" and substantially expanding researcher data access.

## Key Contributions

- An election-specific empirical audit of YouTube moderation under the DSA regime.
- Documentation of previously underreported inconsistencies in the News Funding Notice across broadcasters, subsidiaries, and EU languages.
- A "critical audit" methodology that hybridizes API and scraping approaches while reflexively examining conditions of platform observability.
- A comparative removal-rate baseline between election queries and a banned-influencer (Andrew Tate) query.
- Concrete policy proposals: extending the YouTube Research API to include label and removal data, adding a "historical mode" to counter recency bias, and linking the DSA Transparency Database to video/channel IDs.

## Methods

The authors deploy a hybrid critical audit drawing on Sandvig et al.'s typology. Browser-based scraping (via AI Forensics) captured top-20 search results from local IPs in NL, DE, and FR for neutral and adversarial election queries between May–July 2024. Weekly YouTube API queries on "European Parliamentary election" (April–July 2024) yielded 8,142 unique videos, with later metadata retrieval to identify removals. Channels were classified into six categories (PSM, Legacy Media, Government, Political Parties, Natively Digital, Other). News Funding Notice visibility was tested systematically across EU countries and languages via VPNs; removal statements were scraped and compared with channel-page messaging, with the Internet Archive used to recover metadata of unavailable videos.

## Findings

- PSM dominate top search results in NL and DE; legacy media is more prominent in FR; 91% of PSM videos in the sample carried a News Funding Notice.
- The Notice is inconsistently applied: TRT Français lacks one while other TRT branches have it; RTBF carries one but RTBF Info does not; broadcasters like Ongehoord Nederland, L1 Limburg, and Omroep Flevoland are unlabeled.
- The Notice is absent in Finnish, Greek, Danish, Catalan, Basque, Galician, and European Portuguese language settings (though present in Brazilian Portuguese).
- Of 8,142 election videos, 6% became unavailable, versus 26% in the Andrew Tate comparison sample.
- Most removals are attributed to channel-level terminations; only four videos were explicitly flagged for Terms of Service violations, and YouTube communicates via ToS rather than Community Guidelines.
- Case studies (WealthHub reuploading Tate content; DDGeopolitics circulating RT/Sputnik material) show YouTube removing specific videos while leaving borderline channels active.

## Connections

This chapter sits within a growing body of platform-governance audits that interrogate the gap between platform self-presentation and observable practice; it pairs naturally with [[Rieder2026-pp]] and [[Rieder2025-ju]] on algorithmic visibility and platform knowledge, and with [[Votta2025-xz]] and [[Bouchaud2026-lr]] on auditing recommender and moderation systems. Its DSA-focused framing connects to broader debates on researcher data access and transparency infrastructures explored in [[Helmond2026-ll]] and [[Ohme2026-nv]], while its findings on authoritative-source promotion speak to platform-power arguments in [[Munger2025-cz]].
