---
title: "Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections"
aliases: ["Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections"]
authors: ["Íris Damião", "João Franco", "Mariana Silva", "Paulo Almeida", "Pedro C. Magalhães", "Joana Gonçalves-Sá"]
year: 2026
doi: 
bibtex_key: Iris2026-pg
topics: [election-campaigns-on-social-media, platform-policy-and-content-visibility]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2601.05826v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iris2026-pg.mp3
pdf_available: true
discovery_date: 2026-01-15T00:00:00Z
---

# Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections

> Damião, Í., Franco, J., Silva, M., Almeida, P., Magalhães, P. C., & Gonçalves-Sá, J. (2026). Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2601.05826v1)

## Summary

This paper offers a cross-national computational analysis of online media visibility for political families during the run-up to the 2024 European Parliament elections. Drawing on nearly 21,500 news articles from leading outlets in Austria, Germany, Ireland, Poland, and Portugal, the authors extract and map political entities mentioned in article titles and URLs onto European Parliament groups and broad ideological leanings. Their central argument is that the Radical Right received disproportionate media visibility — well beyond what prior electoral results, polling projections, or actual 2024 outcomes would predict — and that this imbalance is a structural feature of European online news rather than a quirk of particular outlets. The authors interpret this attention pattern as a mechanism that may contribute to the normalization of radical-right movements.

## Key Contributions

- A systematic, cross-national mapping of media visibility across five diverse European contexts, addressing a gap left by prior single-country studies.
- A reproducible multilingual pipeline combining LLM-based entity extraction (ChatGPT-4o), fuzzy matching, and manual validation.
- Empirical documentation of a *structural* rightward visibility bias that persists across editorial orientation, outlet popularity, and publication volume.
- Direct empirical rebuttal of populist claims that mainstream media systematically marginalize or censor the Radical Right.
- An extension of media-salience theory showing visibility can decouple from domestic party strength, with implications for transnational party-family contagion.

## Methods

Outlets were selected per country using Semrush traffic rankings and news was collected via Media Cloud with a combinatorial, natively-validated keyword strategy across four languages, yielding 21,528 unique items from April 9 to June 9, 2024 (with a filter to exclude concurrent local election coverage). Political entities were extracted from headlines and URLs using ChatGPT-4o (three runs per country) complemented by fuzzywuzzy Ratcliff/Obershelp fuzzy matching, with manual validation of 150 articles by ten coders reaching ~95% accuracy. Entities were mapped onto EP groups and five broad leanings using the 2024 Chapel Hill Expert Survey and official EP sources, then compared against three benchmarks: 2019 seat distribution, pre-election polling, and 2024 results.

## Findings

- About 50% of election news items mentioned political entities; the Radical Right appeared in ~31% of those articles.
- Mainstream Right and Radical Right together drew between 57% (Portugal) and 85% (Poland) of all political mentions; the Left never exceeded 35%.
- Radical Right overrepresentation exceeded two standard deviations against all three benchmarks in Austria, Germany, and Ireland — notably in Ireland, where the Radical Right holds no parliamentary seats.
- Poland was the sole exception, with the Radical Right slightly underrepresented relative to its strength, yet still holding the highest absolute mention count (1,526).
- From mid-May, Radical Right mentions overtook Mainstream Right mentions in Austria, Germany, and Poland — intensifying in the crucial final campaign weeks.
- The bias appeared even in center-left outlets (e.g., Der Spiegel, The Guardian); the Radical Right dominated 50–62.5% of outlets across popularity/output quadrants, while the Mainstream Left dominated only two.

## Connections

This work sits within research on media salience, partisan news, and the media's role in the rise of the Radical Right. Its focus on how visibility patterns in digital news shape political perception connects to broader questions of algorithmic and editorial amplification explored in [[Gonzalez-Bailon2024-rq]] and [[Bakshy2015-rn]]. Its examination of European Parliament election communication and cross-national coverage relates to [[Gattermann2025-yx]], while its interest in the normalization and diffusion of radical-right discourse links to [[Nenno2025-xa]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iris2026-pg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-cross-national-evidence-of/id1866587707?i=1000744834590)
