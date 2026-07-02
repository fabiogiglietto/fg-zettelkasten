---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [coordinated-inauthentic-behavior, generative-ai-and-media]
citation_count: 2
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

This paper investigates how generative AI has transformed coordinated organic gambling promotion on Facebook. Analyzing 2,323 images from 223 coordinated public groups (2017–2024) identified via the Vera AI project, the authors construct a typology of visual persuasion drivers and trace how the launch of ChatGPT catalyzed an exponential expansion of posting activity. They argue that generative AI does not invent new persuasion tactics but industrializes and intensifies existing ones—aspirational wealth, manufactured trust, FOMO, gamification, celebrity endorsement, and cultural localization—while exploiting Meta's asymmetric governance, which strictly regulates paid gambling ads but permits organic gambling content under permissive visibility rules.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in coordinated organic gambling promotion.
- Evidence that generative AI functions as an accelerant of, not a replacement for, established persuasion architectures.
- A reproducible mixed-methods pipeline combining VLM-based image description, dual denotative/connotative embeddings, HDBSCAN clustering, and qualitative human coding.
- Identification of algorithmic amplification and the paid/organic regulatory asymmetry as central governance blind spots.
- A reflexive discussion of using LLMs as analytical instruments to study content produced by the very same class of technology.

## Methods

The authors detect coordinated link-sharing among Facebook public groups (14-second window, 0.995 edge weight) seeded from accounts spreading fact-checker-flagged content, collecting posts and images through the Meta Content Library. Images are described in both denotative and connotative registers by GPT-4o, embedded via `text-embedding-3-small`, reduced with UMAP, and clustered with HDBSCAN (101 denotative, 51 connotative clusters). A co-occurrence matrix across 366 cluster combinations guides qualitative coding by four researchers of 85 dense combinations. Longitudinal post-volume changes are tested via t-tests, Wilcoxon tests, interaction-term regression, and structural break detection, using ChatGPT's release as the intervention.

## Findings

- Aspirational wealth and hyper-masculine status motifs dominate (~55% of coded combinations); transactional "trust proofs" like payment screenshots appear in ~37%.
- Persuasion drivers work synergistically: FOMO/urgency, gamification, celebrity endorsements (e.g., Manny Pacquiao), and social-relations exploitation combine within single images.
- Urdu-language content embeds gambling in conservative moral narratives of family conflict and women in distress—an ideologically inflected localization strategy.
- Mean monthly posts rose from 2,121 pre-ChatGPT to 280,952 post-ChatGPT (a 13,242% jump), with a statistically robust structural break in July 2023.
- Post-2022 imagery shows consistent AI-generation markers (hyper-real lighting, smoothed surfaces, improbable symbolic juxtapositions like sharks with slot machines).
- Individual AI-generated posts reached millions of views (4.3M and 3.3M) with wide cross-group amplification.

## Connections

This work sits at the intersection of coordinated inauthentic behavior research and studies of synthetic media's role in influence and marketing. It builds directly on the authors' prior CIB detection infrastructure ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2024-cbeb3f70]], [[Marino2024-2fbc690f]]) and speaks to broader concerns about generative AI's role in coordinated campaigns and manipulative content ecosystems (e.g., [[DeVerna2025-dl]], [[Minici2024-tf]], [[Luceri2025-tr]], [[Yang2025-iv]], [[Di-Marco2025-aa]]). Its focus on AI-generated visual persuasion and platform amplification also connects to work on synthetic image detection and aesthetics ([[Achmann-Denkler2026-lx]], [[Kansaon2025-id]]) and to debates on algorithmic governance failures ([[Gillespie2026-aa]]).

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
