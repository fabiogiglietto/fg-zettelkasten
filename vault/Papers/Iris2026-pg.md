---
title: "Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections"
aliases: ["Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections"]
authors: ["Íris Damião", "João Franco", "Mariana Menezes Melo Silva", "Paulo Almeida", "Pedro V.S. Magalhaes", "Joana Gonçalves-Sá"]
year: 2026
doi: 
bibtex_key: Iris2026-pg
topics: [elections-political-communication, polarization-hybrid-media]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2601.05826
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iris2026-pg.mp3
pdf_available: true
discovery_date: 2026-01-15T00:00:00Z
---

# Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections

> Damião, Í., Franco, J., Silva, M., Almeida, P., Magalhães, P. C., & Gonçalves-Sá, J. (2026). Cross-national evidence of disproportionate media visibility for the Radical Right in the 2024 European elections. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2601.05826v1)

## Summary

This paper examines whether the Radical Right received media visibility commensurate with its electoral strength during the two months preceding the 2024 European Parliament elections. Analyzing ~21,500 online news articles from leading outlets across Austria, Germany, Ireland, Poland, and Portugal, the authors use an LLM-based pipeline to extract mentions of political parties and politicians in article titles and URLs, then compare visibility shares against three benchmarks: 2019 EP results, 2024 polling projections, and the actual 2024 outcomes. They find a systematic and structural overrepresentation of the Radical Right that intensifies in the final campaign weeks, persists across outlets of differing popularity and editorial orientation, and contradicts populist claims of being marginalized by mainstream media.

## Key Contributions

- A cross-national, computational mapping of political-family media visibility across five European countries during a major election cycle.
- A reproducible multilingual pipeline combining ChatGPT-4o entity extraction, fuzzy matching (Ratcliff/Obershelp), and manual validation (~95% accuracy).
- Empirical evidence that rightward visibility bias is *structural* rather than outlet-specific, appearing even in center-left outlets like *Der Spiegel* and *The Guardian*.
- A direct empirical rebuttal to the populist narrative that mainstream media systematically marginalize the Radical Right.
- Extension of media-salience literature to a transnational frame, suggesting party-family contagion via coverage of foreign actors even where domestic radical-right organization is weak (e.g., Ireland).

## Methods

Outlets were selected from Semrush traffic rankings, and news collected via Media Cloud using a combinatorial keyword strategy across three thematic groups in English, German, Polish, and Portuguese, with exclusions filtering concurrent local elections. The two-month window (9 April – 9 June 2024) produced 21,528 unique items. Political entities were extracted from titles/URLs via three ChatGPT-4o runs per country plus fuzzy matching, with manual coder validation. Parties were mapped to EP groups and to five ideological leanings (Radical Left, Mainstream Left, Greens, Mainstream Right, Radical Right) using the 2024 Chapel Hill Expert Survey. Visibility shares were benchmarked against 2019 seats, pre-election polling, and 2024 results, with both per-country and seat-weighted aggregate analyses.

## Findings

- About 50% of EU-election articles named a political entity; ~31% of those mentioned the Radical Right.
- Mainstream Right + Radical Right combined captured 57% (Portugal) to 85% (Poland) of all mentions; Left families never exceeded 35%.
- The Radical Right was the most-mentioned family in Austria, Germany, and Poland, and second in Ireland.
- Overrepresentation exceeded two standard deviations across all three benchmarks in Austria, Germany, and Ireland — including Ireland, which has no radical-right MEPs.
- Poland was the lone exception, with the Radical Right slightly under-represented relative to its strength (though still having the highest absolute mention count, 1,526).
- From mid-May onward, Radical Right mentions overtook Mainstream Right mentions in Austria, Germany, and Poland — coinciding with the most persuadable period for undecided voters.
- The Radical Right dominated coverage in 50–62.5% of outlets across all popularity/output quadrants; Mainstream Left dominated in only 2 outlets and Radical Left in none.
- Mainstream Left was systematically underrepresented in Austria and Portugal.

## Connections

This paper sits alongside other computational studies using LLMs to audit political content and ideological dynamics in news and platforms, including [[Balluff2026-if]] and [[Tornberg2025-ir]] on automated analysis of political media, and [[Larsson2026-ro]] on coverage patterns in European political communication. Its findings on radical-right amplification also resonate with platform-level work on partisan and ideological asymmetries such as [[DeVerna2025-dl]] and [[Emilio2026-ik]], and complement methodological efforts to use LLMs for entity and stance extraction in multilingual political text (e.g., [[Dierickx2026-tw]], [[Achmann-Denkler2026-lx]]).

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Iris2026-pg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-cross-national-evidence-of/id1866587707?i=1000744834590)
