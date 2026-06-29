---
title: "Who’s driving the AI hype in its formative phase? A longitudinal analysis of stakeholders in the US and German AI discourse on Twitter 2012–2021"
aliases: ["Who’s driving the AI hype in its formative phase? A longitudinal analysis of stakeholders in the US and German AI discourse on Twitter 2012–2021"]
authors: ["Vanessa Richter", "Daria Dergacheva", "Vasilisa Kuznetsova", "Christian Katzenbach"]
year: 2026
doi: 10.1007/s00146-026-03079-6
bibtex_key: Richter2026-bt
topics: [generative-ai-and-media]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1007/s00146-026-03079-6
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Richter2026-bt.mp3
pdf_available: true
discovery_date: 2026-06-16T10:49:57.670972Z
---

# Who’s driving the AI hype in its formative phase? A longitudinal analysis of stakeholders in the US and German AI discourse on Twitter 2012–2021

> Richter, V., Dergacheva, D., Kuznetsova, V., & Katzenbach, C. (2026). Who’s driving the AI hype in its formative phase? A longitudinal analysis of stakeholders in the US and German AI discourse on Twitter 2012–2021. *AI & SOCIETY*, 1–14. https://doi.org/10.1007/s00146-026-03079-6
>
> [View paper](https://doi.org/10.1007/s00146-026-03079-6)

## Summary

This paper investigates which stakeholders dominated public AI discourse on Twitter in the US and Germany during the formative pre-GenAI decade (2012–2021). The authors develop a two-dimensional typology that crosses stakeholder type (industry, government, advocacy, academia, media, civil society) with organisational level (network, organisation, sub-organisation, individual), and apply it to the top 100 most-retweeted accounts per year in each language. They find that the often-repeated claim of uniform industry dominance is too coarse: Germany underwent *institutionalisation*, with academic, advocacy and governmental organisations rising to prominence, while the US underwent *individualisation*, with tech influencers increasingly displacing corporate accounts even as industry-affiliated voices remained dominant overall. These divergent formative trajectories, the authors argue, prefigure the contrasting GenAI regulatory and discursive landscapes the two countries entered after 2022.

## Key Contributions

- A two-dimensional stakeholder typology (sector × organisational level) for analysing AI and other socio-technical discourses.
- The first systematic longitudinal, cross-country mapping of AI stakeholders on Twitter for Germany and the US (2012–2021).
- An empirical nuancing of the "industry dominance" narrative in AI discourse, showing it is country- and time-dependent and increasingly mediated by individual figureheads in the US.
- Identification of contrasting *institutionalisation* (Germany) vs. *individualisation* (US) trajectories that help explain post-GPT regulatory divergence.
- A reusable framework portable to adjacent discourses such as climate or energy.

## Methods

- Collection of tweets via the Twitter Academic API (`academictwitteR`) for #AI, #ArtificialIntelligence (EN) plus #KI, #KuenstlicheIntelligenz (DE), Jan 2012–Dec 2021; corpus of ~761k German and ~13.4M English tweets.
- Retweet-based "name network" construction via `igraph`, selecting the top 100 accounts per year per language by in-degree centrality.
- Manual coding of accounts by two independent coders for stakeholder type, organisational level, and country (Cohen's κ = 0.85), using the Wayback Machine to recover suspended/deleted accounts.
- Agresti–Coull confidence intervals to estimate uncertainty in yearly proportions; comparative longitudinal analysis across the two corpora.
- Conceptual framework synthesised from the governance triangle literature and Gorwa's platform governance stakeholder typology, refined inductively via trial coding.

## Findings

- In Germany, individual accounts dominated in 2012 but fell to ~25% of top accounts by 2021, reflecting institutionalisation.
- By 2021 the German top accounts were led by academia (~25%) and advocacy (~20%), with industry, government and media each in the 10–20% range; tech influencers remained marginal (~5%).
- German governmental accounts surged around 2018 (~15%), coinciding with EU-level AI regulatory debates.
- US industry dominance grew from 2012 to a 2017 peak of ~70% of top accounts, with tech influencers adding another ~15%.
- From 2016 onward, US individual accounts climbed to over three-quarters of top accounts by 2021, driven by tech influencers.
- By 2021 the US AI discourse was largely a tech-influencer discourse, with little academic, traditional media, or advocacy presence among top accounts.
- Media and lay accounts dominated early years in both countries but rapidly receded as professional actors entered.
- Most yearly proportion standard errors fell below 5%, supporting trend robustness.

## Connections

This paper complements work on the structural and platform-level dynamics shaping AI's public emergence, including studies of how AI infrastructures are embedded in platform ecosystems such as [[Helmond2026-ll]] and broader generative-AI/media transformations like [[Vertesi2026-lv]]. Its emphasis on the cultural framing and stakeholder construction of AI also speaks to research on AI discourse and imaginaries in journalism and media, such as [[Dierickx2026-tw]] and [[Schroeder2026-im]]. Most other papers under this topic focus on GenAI outputs, persuasion, or election effects rather than the upstream stakeholder ecology, so direct intellectual ties are limited.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Richter2026-bt.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-who-really-drove-the-ai-hype-tech/id1866587707?i=1000773111056)
