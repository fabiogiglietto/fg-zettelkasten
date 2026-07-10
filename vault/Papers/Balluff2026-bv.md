---
title: "The Austrian political advertisement scandal: Patterns of “journalism for sale”"
aliases: ["The Austrian political advertisement scandal: Patterns of “journalism for sale”"]
authors: ["Paul Balluff", "Jakob-Moritz Eberl", "Sarina Joy Oberhänsli", "Jana Bernhard-Harrer", "Hajo G. Boomgaarden", "Andreas Fahr", "Martin Huber"]
year: 2026
doi: 10.1177/19401612241285672
bibtex_key: Balluff2026-bv
topics: [information-disorder, political-polarization-partisan-news]
citation_count: 5
open_access: false
source_url: https://doi.org/10.1177/19401612241285672
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-bv.mp3
pdf_available: true
discovery_date: 2026-01-27T10:52:07.596221Z
---

# The Austrian political advertisement scandal: Patterns of “journalism for sale”

> Balluff, P., Eberl, J., Oberhänsli, S. J., Bernhard-Harrer, J., Boomgaarden, H. G., Fahr, A., & Huber, M. (2026). The Austrian political advertisement scandal: Patterns of “journalism for sale”. *The International Journal of Press/Politics*, *31*, 91–117. https://doi.org/10.1177/19401612241285672
>
> [View paper](https://doi.org/10.1177/19401612241285672)

## Summary

This paper investigates Austria's *Inseratenaffäre* ("advertisement scandal"), in which former chancellor Sebastian Kurz allegedly arranged for the tabloid OE24 to receive government advertising revenue in exchange for favorable coverage and manipulated polling. Using automated content analysis of 222,659 political news articles from 17 Austrian outlets (2012–2021) and a difference-in-differences design, the authors test whether OE24's coverage of Kurz diverged from comparable outlets after the alleged 2016 onset of the scheme. They find a substantial increase in Kurz's visibility in OE24, no significant boost in his favorability, but more negative coverage of his political competitors — a pattern consistent with "paying positive to go negative" dynamics in media capture. The study frames Austria as a "most likely case" within the democratic-corporatist model, demonstrating that media capture via government advertising is not confined to hybrid or Central/Eastern European regimes.

## Key Contributions

- Provides rare empirical evidence of media capture mechanisms within an established Western European democracy, extending a literature focused largely on CEE and developing contexts.
- Introduces a quasi-experimental computational pipeline combining transformer-based sentiment analysis with difference-in-differences (DiD) and synthetic DiD to detect coverage irregularities consistent with covert political-media arrangements.
- Develops and validates a fine-tuned GottBERT German sentiment model using counterfactual data augmentation (name-swapping) to reduce actor-specific bias.
- Documents the "pay positive to go negative" pattern in a political (rather than purely commercial) advertiser context.
- Offers a transferable methodological template for studying alleged media capture and informs policy debates on regulating government advertising.

## Methods

- Automated content analysis of 222,659 political news articles from 17 Austrian print/online outlets (2012–2021), sourced via the APA archive and targeted web scraping.
- Article filtering with validated Boolean search strings (from AUTNES) identifying mentions of Kurz, Mitterlehner, Strache, and successive SPÖ leaders.
- Paragraph-level actor visibility via word-proximity search (R package `corpustools`), aggregated to monthly outlet-level counts and log-transformed.
- Favorability measured with a fine-tuned GottBERT model trained on AUTNES manual coding (classification F1 = 0.77, regression RMSE = 0.65).
- DiD estimation of the Average Treatment Effect on the Treated (ATET), treating OE24 as the treated outlet with 2015 as baseline; placebo tests (2012–2015) checked the common trend assumption.
- Robustness checks: party-level analysis (250,442 articles), alternative control groups (Kronen Zeitung, Heute), and a synthetic DiD estimator relaxing the common trend assumption.

## Findings

- Pre-2016 visibility trends across OE24 and controls were largely parallel, supporting the common trend assumption.
- After 2016, paragraphs mentioning Kurz in OE24 roughly doubled relative to the counterfactual, with highly significant ATETs across all post-treatment years.
- No comparable visibility effects for Mitterlehner or the SPÖ leader; Strache showed significant positive effects only in two election years and at smaller magnitudes.
- Favorability ATETs for Kurz were not statistically significant, but coverage of all other candidates trended more negative in OE24 after 2016.
- Synthetic DiD estimated an average ~50% increase in Kurz's visibility over 2016–2019 relative to a weighted control (significant at 1%).
- Party-level checks showed a general uptick in OE24 coverage of all parties but no party-specific effect — the bias was actor-focused on Kurz rather than partisan.

## Connections

This paper sits within the strand of information-disorder research concerned with structural, top-down manipulation of the news environment rather than bottom-up misinformation. Its focus on partisan and biased coverage of political actors connects it to [[Balluff2026-if]], sharing a lead author and likely methodological lineage in computational Austrian media analysis. Beyond that shared computational-content-analysis tradition, the paper stands somewhat apart from the topic cluster's typical emphasis on social-media disorder, since its core concern is covert political-media capture through advertising rather than platform dynamics.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-bv.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-journalism-for-sale-unpacking-an/id1866587707?i=1000746979127)
