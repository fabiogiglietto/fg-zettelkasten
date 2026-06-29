---
title: "The Austrian political advertisement scandal: Patterns of “journalism for sale”"
aliases: ["The Austrian political advertisement scandal: Patterns of “journalism for sale”"]
authors: ["Paul Balluff", "Jakob-Moritz Eberl", "Sarina Joy Oberhänsli", "Jana Bernhard-Harrer", "Hajo G. Boomgaarden", "Andreas Fahr", "Martin Huber"]
year: 2026
doi: 10.1177/19401612241285672
bibtex_key: Balluff2026-bv
topics: [elections-political-communication, computational-methods-social-research]
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

This paper provides empirical evidence for media capture in an established Western democracy by examining Austria's *Inseratenaffäre* — the alleged 2016 arrangement in which Chancellor Sebastian Kurz funneled government advertising to the tabloid OE24 in exchange for favorable coverage and manipulated polls. Using a quasi-experimental design on a decade of Austrian political news, the authors show that after 2016 OE24 dramatically amplified Kurz's visibility relative to comparable outlets, without making coverage of Kurz himself more positive but by turning more negative against his competitors. They interpret this as a "pay positive to go negative" pattern of advertiser-driven media bias and argue that Austria's regulatory framework, despite the 2012 Media Transparency Law, leaves democratic-corporatist systems structurally vulnerable to covert political capture.

## Key Contributions

- Empirical demonstration of media capture mechanisms inside a consolidated Western European democracy, extending a literature dominated by CEE and hybrid-regime cases.
- A reusable computational pipeline combining transformer-based sentiment analysis with difference-in-differences and synthetic DiD to detect covert media-political arrangements.
- A fine-tuned GottBERT sentiment classifier trained on AUTNES data with counterfactual name-swapping augmentation to mitigate actor-specific bias.
- Documentation of the "pay positive to go negative" dynamic (Blasco et al. 2016) in a political — rather than commercial — advertiser context.
- Methodological template and policy implications for regulating government advertising and safeguarding media independence.

## Methods

The authors assembled 222,659 political news articles from 17 Austrian print and online outlets (2012–2021) via APA archives and web scraping, filtered with validated AUTNES Boolean queries for Kurz, Mitterlehner, Strache, and successive SPÖ leaders. Actor visibility was measured at the paragraph level via word-proximity search (corpustools) and aggregated monthly; favorability was scored using a fine-tuned GottBERT model (F1 = 0.77; RMSE = 0.65). The core identification strategy is a difference-in-differences design treating OE24 as the treated unit with 2015 as baseline, supplemented by 2012–2015 placebo tests, party-level robustness checks on a separate 250,442-article sample, alternative control sets (including Kronen Zeitung and Heute), and a synthetic DiD estimator that relaxes the common-trend assumption.

## Findings

- Pre-2016 visibility trends were largely parallel across OE24 and control outlets, supporting the DiD assumptions.
- Post-2016, paragraphs mentioning Kurz in OE24 roughly doubled relative to the counterfactual, with highly significant ATETs across all post-treatment years.
- No comparable visibility boost appeared for Mitterlehner or the SPÖ leader; Strache showed smaller, election-year-specific effects.
- Favorability toward Kurz did not significantly improve, but coverage of all his competitors in OE24 trended more negative after 2016.
- Synthetic DiD confirmed an average ~50% increase in Kurz's OE24 visibility over 2016–2019 (significant at 1%).
- Party-level analyses revealed no partisan tilt: the bias was actor-specific to Kurz, not pro-ÖVP in general.

## Connections

No other papers have been provided under shared topics, so there are no sibling notes to link. Intellectually, this work sits at the intersection of media-capture theory (Besley & Prat; Schiffrin), comparative media systems (Hallin & Mancini), and computational measurement of media bias, and would naturally connect to future notes on advertiser-driven slant and party-press parallelism once added to the vault.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-bv.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-journalism-for-sale-unpacking-an/id1866587707?i=1000746979127)
