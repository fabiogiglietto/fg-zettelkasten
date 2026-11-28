---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [coordinated-inauthentic-behavior, generative-ai-media]
citation_count: 3
open_access: true
source_url: https://doi.org/10.1007/978-3-032-11782-3_4
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3
pdf_available: true
discovery_date: 
---

# Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}

> Giglietto, F., Terenzi, M., Chakraborty, A., & Marino, G. (2026). Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}. *Countering Disinformation in the Era of Generative AI*. https://doi.org/10.1007/978-3-032-11782-3_4
>
> [View paper](https://doi.org/10.1007/978-3-032-11782-3_4)

## Summary

This paper investigates visual persuasion in coordinated online gambling promotion on Facebook, analyzing over 2,300 images drawn from 223 coordinated public groups surfaced through the Vera AI project. Using a hybrid pipeline of vision-language models, embeddings, and density-based clustering, the authors construct a typology of persuasive visual drivers—aspirational wealth, manufactured trust, FOMO/urgency, gamification, celebrity endorsement, cultural localization, and social-relations exploitation—and document how these operate synergistically. The central argument is that generative AI has not introduced new persuasion strategies but rather intensified and recombined existing ones while enabling industrial-scale dissemination. The authors tie a dramatic post-ChatGPT surge in posting volume to the exploitation of a regulatory grey zone between Meta's strict rules on paid gambling ads and its permissive treatment of organic content, foregrounding algorithmic amplification as the key governance blind spot.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in coordinated organic gambling promotion.
- Evidence that generative AI acts as an accelerant and intensifier of existing persuasion architectures rather than a source of wholly novel strategies.
- A reproducible mixed-methods pipeline combining VLM-based image description, dual denotative/connotative embeddings, HDBSCAN clustering, and human qualitative coding.
- Identification of Meta's paid-versus-organic regulatory asymmetry and algorithmic amplification as governance failures.
- A reflexive critique of using LLMs as both analytical instruments and the enabling technology for the manipulative content under study.

## Methods

The authors identified 223 coordinated Facebook public groups via the Vera AI alerts workflow, which detects coordinated link-sharing behavior (14-second window, 0.995 edge weight) seeded from accounts spreading fact-checker-flagged content. They collected 10,671 posts and 2,323 distinct images (2017–2024) through the Meta Content Library and a custom image-downloader. GPT-4o generated both denotative and connotative image descriptions, which were embedded (text-embedding-3-small), reduced via UMAP, and clustered with HDBSCAN (101 denotative, 51 connotative clusters). A co-occurrence matrix across 366 combinations guided qualitative coding of 85 combinations by four coders. Monthly post volumes were analyzed quantitatively with t-tests, Wilcoxon tests, interaction-term regression, and structural break detection, using ChatGPT's launch as the intervention point.

## Findings

- Aspirational wealth and hyper-masculine status motifs appeared in ~55% of analyzed cluster combinations; transactional "trust proof" visuals (receipts, cash-out screenshots) in ~37%.
- Drivers identified include aspirational wealth, manufactured trust, FOMO/urgency, gamification, celebrity endorsement (e.g., Manny Pacquiao), social-relations exploitation, and cultural/linguistic localization (Filipino, Urdu).
- The Urdu-language cluster embedded gambling within conservative cultural framings via emotionally charged depictions of women in distress and family conflict.
- Mean monthly posts rose from 2,121 (pre-ChatGPT) to 280,952 (post-ChatGPT)—a 13,242% increase—with a confirmed level shift and slope change (p<0.0001) and a structural break in July 2023.
- Post-2022 visuals show consistent AI-generation markers (hyper-real lighting, smoothed surfaces, improbable symbolic juxtapositions) and combine multiple drivers per image.
- Two emblematic AI-generated posts reached 4.3M and 3.3M views across coordinated groups.

## Connections

This work extends the authors' broader program on coordinated link-sharing detection, drawing directly on the methodological lineage of [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and [[Giglietto2023-fa71a001]], and the visual-coordination strand in [[Marino2023-9137f448]]. Its concern with generative-AI aesthetics in influence and persuasion situates it alongside synthetic-media work such as [[Giada2026-fc9a3833]], while its theoretical grounding in coordinated inauthentic behavior connects it to foundational framings in [[Starbird2019-qv]] and [[Nizzoli2020-cf]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
