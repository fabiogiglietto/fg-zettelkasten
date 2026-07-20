---
title: "A systematic review of social science studies analyzing social media data, 2010-2024"
aliases: ["A systematic review of social science studies analyzing social media data, 2010-2024"]
authors: ["Kai-Cheng Yang", "Pranav Goel", "Meredith L. Pruden", "Qunfang Wu", "Colby Eagan", "David Lazer", "Deen Freelon"]
year: 2026
doi: 10.31235/osf.io/yexp6_v1
bibtex_key: Yang2026-tq
topics: [platform-data-access-methods, llm-augmented-research-methods]
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

This systematic review provides a 15-year, cross-disciplinary baseline of how social science research has relied on social media data. Analyzing 859,105 publications across 59 journals in five disciplines plus interdisciplinary outlets (2010-2024), the authors estimate that 0.78% of papers overall—and 3.15% within social science journals—use social media data empirically. They document a heavy and persistent concentration on Twitter/X and Facebook, a threefold growth in such research through the early 2020s, and a subsequent plateau and decline in 2022-2024 coinciding with platform API restrictions. The paper argues that the empirical study of social media is on the cusp of a significant transformation, driven by the closure of data access and emerging shifts toward alternative platforms and data collection paradigms.

## Key Contributions

- First multi-platform, multi-disciplinary systematic baseline of empirical social media research, moving beyond prior Twitter-centric reviews.
- Demonstrates that Web of Science under-reports relevant papers, and develops an alternative journal-website search pipeline.
- Introduces and validates a reproducible human-in-the-loop LLM annotation methodology for large-scale meta-science, with publicly released materials.
- Quantitatively documents the impact of API closures on academic publishing and identifies emerging shifts toward TikTok, YouTube, and user-donated data.
- Maps the topical landscape of empirical social media research, showing which substantive areas are most exposed to data access restrictions.
- Calls for journal and indexing standardization (uniform publication-type tagging, mandatory author keywords) to enable future meta-science.

## Methods

- Systematic review of 859,105 publications from 59 journals selected via Google Scholar h5-index rankings supplemented by Web of Science searches.
- Keyword search of journal websites for eight platforms yielded 27,951 matched papers (Pinterest later dropped for poor reliability); stratified sampling produced an analytical sample of 5,218 papers.
- Two-stage annotation: (1) identifying empirical papers, (2) identifying which platforms provided the data, with iteratively developed codebooks and inter-rater reliability via Krippendorff's α.
- Three LLMs evaluated against human ground truth; o4-mini selected (100% accuracy on empirical identification, ≥91% on platform identification) and applied to the full sample.
- Sample annotations scaled to the full corpus using journal-year sampling ratios; topics identified via co-occurrence networks of author keywords and ensemble Louvain community detection.

## Findings

- 0.78% of all papers (3.15% in social science-only journals) use social media data empirically, with wide disciplinary variation: Communication 12.86%, Political Science 5.11%, Psychology 1.22%, Economics <0.7%.
- Twitter/X (50.86%) and Facebook (36.28%) dominate as data sources; YouTube 17.11%, Reddit 5.66%, with TikTok, Instagram, and LinkedIn smaller.
- Research platform usage is misaligned with public adoption: Twitter/X is overrepresented (used by 21% of Americans) while YouTube (84%) is underrepresented.
- 82.59% of papers rely on a single platform; multi-platform research remains rare.
- The share of social media papers tripled before plateauing and declining in 2022-2024, driven by drops in Twitter/X and Facebook use after free APIs ended.
- TikTok and YouTube show recent growth as researchers begin shifting platforms.
- COVID-19 is the most common topic (over 60% of Economics papers), alongside social movements, political communication, journalism, body image (Psychology), and disinformation; Communication has the most balanced topic distribution.

## Connections

This review provides the meta-scientific frame for the wider "post-API age" literature on platform data access, connecting directly to prior Twitter-centric reviews such as [[Murtfeldt2025-wu]] and to work on the consequences of API closures for research infrastructure. Its documentation of shifts toward user-donated data and alternative platforms relates to studies of data donation and platform governance like [[Ohme2026-nv]] and [[Rieder2025-ju]], while its LLM annotation pipeline connects to the broader computational content analysis strand exemplified by [[Le-Mens2025-qz]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Yang2026-tq.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-the-post-api-age-what-we-lose-when/id1866587707?i=1000769319467)
