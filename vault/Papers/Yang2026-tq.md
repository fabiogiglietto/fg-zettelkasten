---
title: "A systematic review of social science studies analyzing social media data, 2010-2024"
aliases: ["A systematic review of social science studies analyzing social media data, 2010-2024"]
authors: ["Kai-Cheng Yang", "Pranav Goel", "Meredith L. Pruden", "Qunfang Wu", "Colby Eagan", "David Lazer", "Deen Freelon"]
year: 2026
doi: 10.31235/osf.io/yexp6_v1
bibtex_key: Yang2026-tq
topics: [platform-governance-data-access, llms-computational-content-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/yexp6_v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Yang2026-tq.mp3
pdf_available: true
discovery_date: 2026-05-09T17:26:23.924172Z
---

# A systematic review of social science studies analyzing social media data, 2010-2024

> Yang, K., Goel, P., Pruden, M. L., Wu, Q., Eagan, C., Lazer, D., & Freelon, D. (2026). A systematic review of social science studies analyzing social media data, 2010-2024. https://doi.org/10.31235/osf.io/yexp6_v1
>
> [View paper](https://doi.org/10.31235/osf.io/yexp6_v1)

## Summary

This systematic review maps fifteen years (2010–2024) of empirical social media research across 59 journals spanning Communication, Economics, Political Science, Psychology, Sociology, and interdisciplinary outlets. Using a human-in-the-loop LLM annotation pipeline applied to nearly 860,000 publications, the authors estimate that 0.78% of papers in their corpus (3.15% within social science journals proper) rely on social media data, with Twitter/X and Facebook dominating to a degree wildly disproportionate to their public popularity. The paper's central argument is that the field is at an inflection point: empirical social media research roughly tripled from 2010 into the early 2020s but plateaued and declined in 2022–2024 in lockstep with API closures, foreshadowing a structural transformation in how — and whether — social scientists can study platforms.

## Key Contributions

- First multi-platform, multi-disciplinary systematic baseline of empirical social media research across 15 years and 59 journals, moving beyond the Twitter-centric framing of prior reviews.
- Demonstrates that Web of Science substantially under-reports relevant papers and develops an alternative discovery pipeline using full-text journal-website search.
- Validates a reproducible human-in-the-loop LLM annotation methodology (codebook, prompts, and code released) for large-scale meta-scientific work.
- Quantifies the empirical footprint of the "post-API" turn, documenting how data access restrictions are reshaping publishing patterns and pushing researchers toward alternative platforms and data-donation paradigms.
- Maps the topical landscape (COVID-19, social movements, political communication, misinformation, body image, etc.) to identify which substantive areas are most exposed to platform data access restrictions.
- Calls for indexing standardization (uniform tagging of publication types, mandatory author keywords) to enable future meta-science.

## Methods

A keyword search across 59 h5-index-ranked journals (10 per discipline plus interdisciplinary, minus an excluded outlier) for eight platform names yielded 27,951 matched papers; stratified sampling produced an analytical set of 5,218. Two-stage annotation — (1) is the paper empirical? (2) which platforms supplied data? — was developed with six coders and assessed with Krippendorff's α. Three LLMs were benchmarked against human gold standards; o4-mini (100% accuracy on empirical identification, ≥91% on platform identification) was deployed on the full sample, and journal-year sampling ratios scaled estimates to the matched corpus. Topic structure was recovered via ensemble Louvain community detection (1,000 runs) on Scopus keyword co-occurrence.

## Findings

- 0.78% of all papers (3.15% in social science-only journals) use social media data empirically; Communication leads at 12.86%, followed by Political Science (5.11%), Psychology (1.22%), Economics (<0.7%), interdisciplinary (<0.3%).
- Twitter/X appears in 50.86% of empirical social media papers and Facebook in 36.28%; YouTube (17.11%), Reddit (5.66%), TikTok, Instagram, and LinkedIn trail far behind.
- Research-versus-public misalignment is stark: Twitter/X is overrepresented (used by ~21% of Americans) and YouTube dramatically underrepresented (used by ~84% of Americans).
- Single-platform studies dominate at 82.59%; multi-platform research is rare.
- Empirical social media research grew ~235% from 2010 into the early 2020s before plateauing and declining in 2022–2024, with the drop driven by Twitter/X and Facebook following API closures.
- Twitter/X usage spikes around 2015–2016 (U.S. election) and 2020–2022 (COVID-19, 2020 election); TikTok and YouTube show recent upward trends.
- COVID-19 is the single most prominent topic (over 60% of Economics papers using social media data); other clusters include social movements, political communication, journalism, body image (heavily Psychology), ideology, and disinformation.
- Topical diversity varies sharply by discipline: Communication is the most balanced (Gini = 0.38), Economics the most concentrated (Gini = 0.72).

## Connections

This paper provides the quantitative meta-scientific backbone for the broader "post-API age" conversation, directly extending [[Freelon2024-sc]] and complementing the Twitter-focused review in [[Murtfeldt2025-wu]]. Its documentation of API-closure effects connects to work probing what remains feasible under restricted access and data-donation paradigms — see [[Ohme2026-nv]], [[Bak-Coleman2025-pm]], [[Rieder2025-ju]], and [[Rieder2026-pp]] — as well as TikTok- and YouTube-focused efforts that exemplify the platform shift the authors identify, such as [[Pierri2025-hm]], [[Bouchaud2026-lr]], and [[Ulloa2024-jm]]. The framing also dovetails with platform governance and DSA-era data access debates represented by [[Vincent_undated-re]] and [[Helmond2026-ll]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Yang2026-tq.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-the-post-api-age-what-we-lose-when/id1866587707?i=1000769319467)
