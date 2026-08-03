---
title: "Relying on the mainstream? Entity networks in alternative media"
aliases: ["Relying on the mainstream? Entity networks in alternative media"]
authors: ["Paul Balluff", "Hajo G. Boomgaarden", "Annie Waldherr"]
year: 2026
doi: 10.31235/osf.io/43nvp_v1
bibtex_key: Balluff2026-ev
topics: [computational-network-structure-analysis, political-communication-elections]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/43nvp_v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-ev.mp3
pdf_available: true
discovery_date: 2026-07-28T12:18:04.022684Z
---

# Relying on the mainstream? Entity networks in alternative media

> Balluff, P., Boomgaarden, H. G., & Waldherr, A. (2026). Relying on the mainstream? Entity networks in alternative media. *SocArXiv*. https://doi.org/10.31235/osf.io/43nvp_v1
>
> [View paper](https://doi.org/10.31235/osf.io/43nvp_v1)

## Summary

This exploratory study examines how German alternative and legacy media differ in the actors they reference, using coverage of the Nord Stream 2 pipeline (2011–2022) as a case. Analyzing nearly 40,000 articles from 37 alternative and 98 legacy outlets, the authors extract named entities and build co-occurrence networks to compare reporting patterns. Contrary to the assumption that alternative media diverge sharply from the mainstream in the actors they cite, the paper finds substantial overlap in referenced entities. The key differences instead lie in *how* actors are relationally organized and in alternative media's heavier tendency to mention other outlets—suggesting a reactive, resource-constrained, and strategically positioned reporting style rather than a fundamentally distinct informational universe.

## Key Contributions

- A large-scale, actor-centered and relational computational analysis of alternative versus legacy media reporting, an understudied area.
- A novel application of a structural topic model built exclusively on media-type named entities to identify latent media-mentioning profiles.
- Nuances the alternative/legacy distinction by showing that entity overlap coexists with structural network and referencing differences, especially for internationally salient topics.
- Validated German-language NER and entity-linking pipelines, plus a publicly released Creative Commons validation set for entity linking in news.

## Methods

- Corpus of 3,918 alternative articles (from 37 outlets, mostly right-leaning) via the Meteor database and 35,707 legacy articles (98 outlets) via LexisNexis and the Tagesschau API, split into four time periods.
- Named entity recognition with a fine-tuned mLUKE multilingual transformer (F1 = 0.85 for German), extracting over 2.5 million entities.
- Entity linking against Wikidata using mGENRE (80.5% accuracy), pruned to 11,611 entities mentioned at least eight times.
- Entity prominence, diversity (Shannon entropy, disparity, novelty Z-scores), and weighted co-occurrence networks per outlet and period computed in igraph (communities, density, diameter, transitivity, modularity, growth).
- Inter-media referencing analyzed via media mention ratios and a structural topic model on media-type entities.
- A Bayesian generalized linear mixed-effects model (Bernoulli likelihood, logit link) predicting whether an outlet is alternative, with outlet random intercepts.

## Findings

- The top 10 most frequent entities are highly similar across media types, with only minor differences (e.g., Erdoğan and the AfD more prominent in alternative media).
- Alternative media exhibit more cohesive, tightly-knit entity networks (higher transitivity, lower modularity); legacy media are more fragmented and modular.
- In the Bayesian model, diameter and modularity were negatively associated with alternative media, while network growth, transitivity, and media mention ratio were positively associated (credible intervals excluding zero).
- Diversity measures showed weak, uncertain associations—actor breadth is comparable across media types.
- STM revealed distinct media-mentioning profiles: legacy media rely heavily on DPA, while alternative media mix major German outlets (Der Spiegel, Die Welt) with foreign agencies (Reuters, TASS); patterns were stable over time.
- Alternative media engagement intensified in later periods, suggesting reactive, politically opportunistic coverage tied to shifting salience.

## Connections

This paper's use of entity co-occurrence networks to characterize alternative media ecosystems connects to network-based studies of conspiracy and problematic-information spread such as [[Di-Marco2025-aa]] and [[Gerard2025-br]], and its focus on right-leaning German alternative media resonates with work on the far right and alternative online spaces like [[Askanius2026-de]]. The relational, media-ecosystem framing also relates to broader efforts to map cross-platform and cross-outlet coordination structures in [[Giglietto2022-b30e8b4e]] and [[Giglietto2019-e9be81c1]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Balluff2026-ev.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
