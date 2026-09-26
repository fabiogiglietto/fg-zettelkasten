---
title: "The spread of true and false news online"
aliases: ["The spread of true and false news online"]
authors: ["Soroush Vosoughi", "Deb Roy", "Sinan Aral"]
year: 2018
doi: 10.1126/science.aap9559
bibtex_key: Vosoughi2018-at
topics: [misinformation-exposure-recalibration, information-operations-disinformation-narratives]
citation_count: 6665
open_access: false
source_url: https://doi.org/10.1126/science.aap9559
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445481Z
---

# The spread of true and false news online

> Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. *Science*, *359*, 1146–1151. https://doi.org/10.1126/science.aap9559
>
> [View paper](https://doi.org/10.1126/science.aap9559)

## Summary

This landmark study offers the first large-scale, systematic analysis of how verified true and false news differ in their diffusion online. Drawing on ~126,000 rumor cascades tweeted by ~3 million people between 2006 and 2017, the authors classify stories using the concurring verdicts of six independent fact-checking organizations. Their central finding is stark and consistent: falsehood spread significantly farther, faster, deeper, and more broadly than truth across every category of information, with the disparity most pronounced for political news. Crucially, they attribute this pattern to human behavior—driven partly by the greater novelty of false news—rather than to automated bots, which accelerated true and false content at roughly equal rates.

## Key Contributions

- First comprehensive, veracity-based empirical study of true versus false news diffusion at scale, moving beyond single-rumor case studies.
- Introduces a clean framework distinguishing news, rumors, and cascades, deliberately avoiding the politicized term "fake news."
- Overturns the assumption that bots or network/user characteristics drive false-news spread, redirecting attention to human sharing choices.
- Proposes novelty and emotional response as candidate behavioral mechanisms.
- Suggests behavioral interventions (labeling, incentives) over an exclusive focus on curtailing bots; releases code and data.

## Methods

The authors assembled all fact-checked rumor cascades on Twitter from 2006–2017, parsing verdicts from six fact-checkers (95–98% cross-agreement) and reconstructing retweet cascades, including OCR-extracted text from images. Diffusion was quantified via four metrics—depth, size, maximum breadth, and structural virality. Statistical comparisons used Kolmogorov-Smirnov tests and a logistic regression of retweet likelihood controlling for account age, activity, followers, followees, and verification. Novelty was measured with a 200-topic LDA model comparing rumor tweets against what users had seen in the prior 60 days (information uniqueness, KL divergence, Bhattacharyya distance), and emotional content of replies was scored using the NRC lexicon mapped to Plutchik's eight emotions. Robustness checks included cluster-robust standard errors, an independently annotated validation set (Fleiss' κ = 0.88), and two bot-detection algorithms.

## Findings

- The top 0.01% of false cascades exceeded depths of 19 hops—about eight hops deeper than truth, which rarely surpassed depth 10.
- Truth rarely reached more than 1,000 people; the top 1% of false cascades reached 1,000–100,000.
- Truth took ~6× as long to reach 1,500 people and ~20× as long to reach depth 10.
- Politics was the largest category (~45,000 cascades); false political news was the deepest, broadest, fastest, and most viral.
- Users spreading false news had fewer followers, followed fewer people, were less active, less often verified, and newer to Twitter.
- Falsehoods were 70% more likely to be retweeted even after controlling for user and network features.
- False rumors were more novel across all three metrics; they elicited more surprise and disgust, while true rumors elicited more sadness, anticipation, joy, and trust.
- Bot traffic affected true and false spread roughly equally, leaving the main conclusions unchanged.

## Connections

This paper is foundational to the misinformation-diffusion literature and connects to work on echo chambers and viral misinformation such as [[Del-Vicario2016-uj]], to studies of who actually shares and consumes fake news like [[Grinberg2019-ua]] and [[Guess2019-ym]], and to the broader definitional and agenda-setting call in [[Lazer2018-mm]]. Its emphasis on human sharing behavior and the role of reflection versus impulse anticipates intervention research such as [[Pennycook2021-jq]], while its bot-versus-human debate relates to state-linked and automated amplification work including [[Starbird2019-qv]].
