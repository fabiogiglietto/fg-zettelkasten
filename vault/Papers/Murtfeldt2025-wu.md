---
title: "RIP Twitter API: A eulogy to its vast research contributions"
aliases: ["RIP Twitter API: A eulogy to its vast research contributions"]
authors: ["Ryan Murtfeldt", "Sejin Paik", "Naomi Alterman", "Ihsan Kahveci", "Jevin D. West"]
year: 2024
doi: 
bibtex_key: Murtfeldt2025-wu
topics: [platform-governance-data-access]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2404.07340v2
podcast_url: 
pdf_available: true
discovery_date: 2025-10-15T00:00:00Z
---

# RIP Twitter API: A eulogy to its vast research contributions

> Murtfeldt, R., Paik, S., Alterman, N., Kahveci, I., & West, J. D. (2024). RIP Twitter API: A eulogy to its vast research contributions. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2404.07340v2)

## Summary

This paper offers a scientometric "eulogy" for Twitter's research APIs, quantifying the scholarly footprint they enabled before X effectively closed access in 2023 by pricing the Enterprise API at $42,000/month. Through a systematic search of eight databases spanning 2006–2024, the authors identify 33,306 studies in 8,914 venues accumulating over 610,000 citations across 16 disciplines. They document a "Golden Age" of roughly 25% annual growth in Twitter-based scholarship through 2022, followed by stagnation in 2023 and a 13% decline in 2024 — empirical evidence that platform data restrictions are reshaping what social science can know about online discourse. The piece doubles as a policy argument for legislative interventions (DSA, PATA) to guarantee researcher access.

## Key Contributions

- The most comprehensive cross-disciplinary bibliometric accounting of Twitter-data research to date, surpassing prior reviews (Karami et al. 2020; Yu & Munoz-Justicia 2020) in database coverage and scope.
- First systematic empirical documentation of the post-API-closure decline in scholarly output, moving the debate beyond anecdote.
- A dual classification scheme (venue-based vs. top-cited-study-based) that surfaces how disciplinary labels themselves shape bibliometric portraits of a field.
- Transparent, replicable pipeline (code + data on GitHub) including a corrected citation extraction that fixes an error in the preprint version.
- Empirical grounding for policy arguments framing API access as a structural determinant of public knowledge.

## Methods

A systematic search across eight databases (LISTA, Web of Science, Global Health, ACM DL, IEEE Xplore, Engineering Village) using a tailored Boolean string (`twitter NEAR/3 data OR api OR dataset NOT survey`) restricted to articles, conference papers, dissertations, and preprints. Engineering Village's full 43,354-record set was retrieved via Elsevier's API to bypass a 1,000-result UI cap. Hand-coded relevance sampling (≥50 papers/database) yielded relevance rates of 80–97%. Records were deduplicated in R by DOI/title/abstract, and citation counts pulled from Crossref. Disciplines were assigned twice — to the top 100 venues and to the top 100 most-cited studies — followed by manual thematic analysis of top-cited papers per discipline.

## Findings

- 33,306 unique studies in 8,914 venues with 610,738 Crossref citations across 16 disciplines (2006–2024).
- Median 25% annual growth from 2006 to 2022; +0.6% in 2023; –13% in 2024.
- Earliest identified paper is Java et al. (2007), "Why we twitter," despite APIs being available from 2006.
- Venue-based disciplinary breakdown: Science/Engineering 27%, Information Science 14%, Computer Science 11%, Data Science 10%, Social Media 9%, Medicine 8%, Social Science & Internet Technology 7% each.
- Study-based breakdown of top-cited papers: Social Science 24%, Data Science 19%, Social Media Studies 14%, with the rest spread across Public Health, CS, AI, Business, Emergency Response, etc.
- Dominant themes: information dissemination, information integrity (disinformation, hate speech), big-data methods (sentiment analysis, topic modeling, geolocation), event/crisis detection, and behavior research (politics, marketing, mental health).
- External reports indicate >100 research projects were directly disrupted in 2023, including the shutdown of Botometer.
- Continued decline is likely, since much 2024 output still drew on pre-shutdown data.

## Connections

This paper sits at the empirical center of the "post-API age" debate and pairs naturally with [[Freelon2024-sc]] and [[Bruns2025-fz]] on the political economy of platform data access, as well as [[Tornberg2025-ir]] and Davis-style critiques of platform power. Its policy framing connects directly to work on the DSA and Article 40 access regimes — see [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Ohme2026-nv]] — while its bibliometric strategy complements methodological reflections in [[Bak-Coleman2025-pm]], Bastos2025-ol, and [[Munger2025-cz]] on the fragility of computational social science infrastructures. Substantively adjacent are studies that themselves depended on Twitter APIs and now face replication crises, including [[Pierri2025-hm]], [[Luceri2025-tr]], and [[Minici2024-tf]].
