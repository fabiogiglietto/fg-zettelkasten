---
title: "Industry influence in high-profile social media research"
aliases: ["Industry influence in high-profile social media research"]
authors: ["Joseph Bak-Coleman", "Jevin West", "Cailin O'Connor", "Carl T. Bergstrom"]
year: 2026
doi: 
bibtex_key: Bak-Coleman2026-mk
topics: [platform-data-access-methods, platform-critique-anniversary-essays]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2601.11507v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bak-Coleman2026-mk.mp3
pdf_available: true
discovery_date: 2026-01-22T06:56:36.937566Z
---

# Industry influence in high-profile social media research

> Bak-Coleman, J., West, J., O'Connor, C., & Bergstrom, C. T. (2026). Industry influence in high-profile social media research. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2601.11507v1)

## Summary

This paper delivers the first systematic quantitative mapping of industry influence across the full pipeline of high-profile social media research — authorship, editorial handling, and peer review — in Science, Nature, PNAS, and their transfer journals. Working entirely from public data on funding, collaboration, and employment ties to Meta, X, Google, and Microsoft, the authors show that roughly half of these papers carry disclosable industry ties, yet the vast majority go undeclared. They argue that influence is not diffuse but concentrated in a small cadre of repeatedly-engaged scientists who also dominate editorial and review roles, and that this structural dependence skews the literature both in attention (industry-tied work receives roughly double the citations and public reach) and in topic (toward user-focused questions like misinformation sharing and away from platform-scale dynamics). Framed within the metascience tradition of documenting industry influence in tobacco, pharmaceutical, and nutrition science, the paper introduces "industrial saturation" as a composite measure and estimates that only about one in five papers is likely fully independent.

## Key Contributions

- First systematic quantitative mapping of industry influence spanning authorship, editorial handling, and peer review in top-tier social media research.
- Introduces the concept of **industrial saturation** — a composite measure of industry influence across the entire production and evaluation pipeline.
- Empirically documents the gap between formal competing-interest disclosures and industry ties identifiable from public data.
- Links the metascience of industry influence to specific research domains, showing topical bias consistent with industrial selection effects.
- Offers concrete policy recommendations: stronger disclosure norms, corrections to the existing record, and explicit independence statements from unaffiliated authors.

## Methods

The authors built a corpus of 295 articles by 1,210 authors via OpenAlex queries for social media terms, refined with bibliographic coupling. They identified disclosable funding, collaboration, and employment ties to four major platforms using OpenAlex plus industry-announced RFPs and fellowships, manually validating every funding and employment tie and counting only those falling within each journal's 3–5 year disclosure window. Impact was assessed by combining OpenAlex with Altmetric scores across scholarly, policy, news, social media, and Wikipedia dimensions. Editorial analysis covered 80 academic editors handling 167 manuscripts (supplemented with public CVs to estimate detection sensitivity), and peer-review analysis covered 82 named reviewers across 49 papers. Community detection on the coupling network identified topical clusters, and Bayesian binomial and logistic regressions modeled disclosure rates, tie probability, and editor behavior.

## Findings

- 49% of papers had disclosable industry ties, but only 13% included competing-interest declarations and 20% had any identifiable mention of ties.
- 42% of papers explicitly declaring *no* competing interests nonetheless had disclosable ties.
- Prior collaboration was the most common tie, then funding; direct employment was rare.
- Funding and collaboration are highly concentrated (Gini 0.919); the top 10% of authors accounted for 79% of total industry investment.
- Authors with six or more high-profile social media publications almost invariably had disclosable ties.
- 34% of editors had disclosable ties (about twice the author rate), none disclosed; 11% of papers handled by tied editors were authored by their recent co-authors — a pattern absent among independent editors.
- Only 14% of editor funding-years identifiable from CVs were detectable through public data, implying the study *underestimates* true ties.
- Estimated industrial saturation across authors, editors, and reviewers is ~80%.
- Misinformation-sharing research was over-represented among industry-tied work; platform-dynamics research was under-represented.
- Industry-tied papers receive roughly double the citations, policy mentions, news coverage, social media discussion, and Wikipedia references of independent work.

## Connections

This paper sits at the intersection of the platform data-access debate and the broader critique of platform-dependent research, quantifying the structural cost of the access bargain that others in this register describe qualitatively — see [[Rieder2025-ju]] and [[Rieder2026-pp]] on data access regimes, and [[Freelon2024-sc]] on the post-API research landscape. Its concern with the reliability and independence of the social media research record connects to metascientific and reproducibility work such as [[Murtfeldt2025-wu]] and [[Efstratiou2025-gs]], while its topical focus on misinformation research overlaps with [[Allen2025-ot]] and [[Pierri2025-hm]]. It also complements the same lead author's related work in [[Bak-Coleman2025-pm]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bak-Coleman2026-mk.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-social-media-research-how-biased/id1866587707?i=1000746176106)
