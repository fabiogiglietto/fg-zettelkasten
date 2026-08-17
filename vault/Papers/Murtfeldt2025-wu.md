---
title: "RIP Twitter API: A eulogy to its vast research contributions"
aliases: ["RIP Twitter API: A eulogy to its vast research contributions"]
authors: ["Ryan Murtfeldt", "Sejin Paik", "Naomi Alterman", "Ihsan Kahveci", "Jevin D. West"]
year: 2024
doi: 
bibtex_key: Murtfeldt2025-wu
topics: [platform-data-access-and-governance]
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

This paper delivers a scientometric "eulogy" to Twitter's research APIs, quantifying the scholarly output they enabled and the measurable collapse that followed their 2023 closure. By systematically tabulating academic publications using Twitter data from 2006 to 2024, the authors document a "Golden Age" of open social media research spanning 16 disciplines, then chart its stagnation and decline after Twitter restricted access and set Enterprise API pricing at $42,000/month. The central argument is that API restrictions are not merely technical or economic decisions but exercises of platform power that reshape society's empirical capacity to study online public discourse — and that legislative interventions are needed to preserve researcher access.

## Key Contributions

- The most comprehensive cross-disciplinary bibliometric accounting of Twitter-data research to date (33,306 studies), surpassing prior reviews in scope and database coverage.
- Empirical (rather than anecdotal) documentation of the immediate post-API-closure decline in scholarship across 2023–2024.
- A transparent, replicable methodology with code and data released via GitHub, plus a corrected citation count fixing an error in the earlier preprint version.
- A dual-discipline classification scheme (venue-based and study-based) that exposes how labeling choices shape bibliometric portraits.
- Empirical grounding for policy debates on platform data governance (DSA, PATA), framing API access as a structural determinant of public knowledge.

## Methods

The authors ran a systematic literature search across eight databases (LISTA, Web of Science, Global Health, ACM Digital Library, IEEE Xplore, and Engineering Village), using a tailored Boolean search string adjusted per database and restricted to journal articles, conference papers, dissertations, and preprints. To overcome the web interface's 1,000-result download cap, they retrieved Engineering Village's full 43,354-record set via Elsevier's APIs. Relevance was validated through hand-coded sampling (≥50 papers per database, yielding 80–97% relevance rates). Deduplication was performed in R via DOI, title, and abstract; citation counts came from the Crossref REST API. Two parallel disciplinary classifications were applied — one to the top 100 venues and one to the top 100 most-cited studies — followed by manual thematic analysis of top-cited papers.

## Findings

- 33,306 unique studies in 8,914 venues with 610,738 Crossref citations across 16 disciplines (2006–2024).
- Research grew at a median 25% annually from 2006–2022, stagnated in 2023 (+0.6%), then declined 13% in 2024.
- The earliest identified Twitter-data paper is Java et al. (2007), despite API availability beginning in 2006.
- Venue-based classification skews toward Science/Engineering (27%) and Information/Computer/Data Science; study-based classification of top-cited work is led by Social Science (24%), Data Science (19%), and Social Media Studies (14%).
- Dominant topics: information dissemination, information integrity (disinformation, hate speech), big data methods, event detection/response, and human behavior.
- External reports indicate over 100 research projects were directly impacted in 2023, including the shutdown of Botometer.
- Further declines are anticipated, since much 2024 output still relied on pre-shutdown data.

## Connections

This paper is a keystone empirical reference for the platform-governance-data-access literature, providing the bibliometric scale against which more focused analyses of the post-API landscape operate. It connects directly to work interrogating platform data access regimes and their scholarly consequences, including [[Freelon2024-sc]], [[Tonneau2025-bv]], [[Rieder2025-ju]], and [[Rieder2026-pp]], as well as policy-oriented studies of the DSA and researcher access such as [[Bechmann2026-dr]] and [[Schulte2026-df]]. Its documentation of lost empirical capacity also speaks to work on data infrastructures and misinformation research reliant on that data, e.g. [[Pierri2025-hm]] and [[Bak-Coleman2025-pm]].
