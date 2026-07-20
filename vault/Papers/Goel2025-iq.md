---
title: "Using co-sharing to identify use of mainstream news for promoting potentially misleading narratives"
aliases: ["Using co-sharing to identify use of mainstream news for promoting potentially misleading narratives"]
authors: ["Pranav Goel", "Jon Green", "David Lazer", "Philip S. Resnik"]
year: 2025
doi: 10.1038/s41562-025-02223-4
bibtex_key: Goel2025-iq
topics: [information-disorder-disinformation, coordinated-inauthentic-behavior]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1038/s41562-025-02223-4
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# Using co-sharing to identify use of mainstream news for promoting potentially misleading narratives

> Goel, P., Green, J., Lazer, D., & Resnik, P. S. (2025). Using co-sharing to identify use of mainstream news for promoting potentially misleading narratives. *Nature Human Behaviour*, 1–18. https://doi.org/10.1038/s41562-025-02223-4
>
> [View paper](https://doi.org/10.1038/s41562-025-02223-4)

## Summary

This paper argues that the dominant source-level (domain blocklist) approach to measuring online misinformation systematically overlooks a potentially larger phenomenon: users repurposing factually true content from mainstream, reliable outlets to advance misleading narratives. Using a large Twitter/X panel matched to a U.S. voter file (May 2018–November 2021), the authors identify mainstream news articles that are disproportionately co-shared alongside "fake news," and test whether those articles more often contain the narrative structures found in fake news and fact-checked false claims. They find co-shared mainstream articles are significantly more likely than control articles from the same outlets to carry potentially misleading narratives, an effect robust to partisan controls, and illustrate the mechanism through vaccine and voter-fraud case studies. The core conceptual move is to shift misinformation measurement from source reliability toward user behavior and narrative function.

## Key Contributions

- A scalable, generalizable **co-sharing-based method** to identify mainstream articles likely repurposed for misinformation, complementing domain-list approaches.
- Operationalizes **"potentially misleading narratives"** via automated narrative extraction over fake news content and fact-checked claims, producing reusable narrative libraries.
- Empirical evidence that misinformation networks extend well beyond fake-news domains, broadening the conceptual scope of the field.
- Two detailed qualitative case studies (vaccines, 2020 voter fraud) demonstrating concrete repurposing mechanisms.
- Implications for journalistic practice — framing and headline choices as repurposing risks — plus released code and data.

## Methods

- Twitter panel of >1.6M U.S. users exact-matched to a TargetSmart voter file; tweets sharing English-language news collected via Twitter API v1 (May 2018–Nov 2021).
- Filtering to URLs shared by ≥20 distinct users yielded ~420,000 URLs from ~2,400 domains; article text scraped with Newspaper3k.
- NewsGuard used to classify domains, with "fake news" defined narrowly (regularly publishing false content); mainstream outlets identified via prior domain ratings and YouGov passive-metering popularity.
- A weighted **bipartite co-sharing graph** between fake news and reliable URLs, pruned to control for popularity; top 1% of co-sharing scores define the co-shared set, and articles outside the top 5% form the control group.
- Narratives extracted with the `relatio` tool as AGENT–VERB→PATIENT strings at two granularities; three misleading-narrative libraries built from fake news articles, fake news headlines, and ~24k fact-checked false claims.
- One-sided Wilcoxon signed-rank tests comparing co-shared vs. control articles, with robustness checks (audience-partisanship controls, domain fixed effects, trustworthy- and liberal-only subsets, quote removal) and two qualitative case studies.

## Findings

- Across all three narrative libraries and both granularities, co-shared mainstream articles contain misleading narratives at significantly higher rates than controls (~0.94 vs. ~0.58 per article; 2.2% vs. 1.3% of extracted narratives).
- Effect holds under partisan controls, trustworthy-only, and liberal-only subsets — not an artifact of partisan composition; odds ~1.24× for co-shared articles.
- Co-shared mainstream articles reach roughly **twice** the audience of fake news articles (≈121 vs. ≈58 sharing users), making cross-source diffusion larger than fake-news-only metrics suggest.
- Vaccine case study identifies three repurposed article types: clickbait headlines, recontextualized older articles, and ambiguous content.
- Voter-fraud case study identifies 11 mainstream articles usable to support mail-in-ballot conspiracies (clickbait, isolated fraud reports, and unrebutted quoted claims).
- Removing direct quotations, the effect holds in 16 of 18 testing instances; manual annotation finds "share-to-criticize" behavior rare (3/100 tweets), supporting an endorsement interpretation.

## Connections

This work reframes information-disorder measurement around user behavior and narrative rather than source reliability, and its co-sharing graph methodology connects directly to the co-sharing/coordination-detection literature associated with [[Giglietto2022-0e951ac5]], [[Giglietto2020-9d8acdd7]], [[Giglietto2019-e9be81c1]], [[Giglietto2017-4375de2f]], and [[Giglietto2023-fa71a001]]. Its critique of domain-list fake-news metrics and attention to overall misinformation exposure speaks to audience-scope work such as [[Budak2024-ef]] and [[Gonzalez-Bailon2024-rq]], while its narrative-repurposing framing resonates with research on strategic misleading framing like [[Hameleers2026-mc]].
