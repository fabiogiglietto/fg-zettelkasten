---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [coordinated-inauthentic-behavior, generative-ai-and-llms]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1007/978-3-032-11782-3_4
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3
pdf_available: true
discovery_date: 
---

# Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}

## Summary

This paper investigates how generative AI has reshaped coordinated organic gambling promotion on Facebook. Drawing on 2,323 images from 223 coordinated public groups identified via the Vera AI alerts workflow, the authors build a typology of visual persuasion drivers and trace how ChatGPT's release coincides with an exponential surge in posting activity. Their central argument is that generative AI does not invent new persuasion strategies but acts as an *accelerant*, intensifying and recombining established drivers (aspirational wealth, manufactured trust, FOMO, gamification, cultural localization) at industrial scale — a dynamic enabled by Meta's asymmetric governance, which polices paid gambling ads but permits permissive organic promotion, and by algorithmic amplification infrastructures that remain a regulatory blind spot.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in coordinated organic gambling promotion.
- Evidence that generative AI intensifies, rather than replaces, existing persuasion architectures.
- A reproducible mixed-methods pipeline combining VLM image description, dual denotative/connotative embeddings, HDBSCAN clustering, and human qualitative coding for large-scale visual analysis.
- Identification of the paid/organic regulatory asymmetry on Meta and of algorithmic amplification as the central governance gap.
- A reflexive methodological note on using LLMs as analytical instruments for studying content these same technologies help produce.

## Methods

The authors identified 223 coordinated Facebook groups via the Vera AI workflow (14-second link-sharing window, 0.995 edge weight), seeded from accounts spreading fact-checker-flagged content. Posts and images (10,671 posts; 2,323 images; 2017–2024) were collected through the Meta Content Library plus a custom image downloader. Each image received denotative and connotative descriptions from `gpt-4o-2024-08-06`, which were embedded with `text-embedding-3-small`, reduced via UMAP, and clustered with HDBSCAN (101 denotative, 51 connotative clusters). A co-occurrence matrix across 366 cluster pairs was qualitatively coded by four researchers until saturation. Posting-volume dynamics were modeled with t-tests, Wilcoxon tests, interaction-term regression, and structural break detection, using ChatGPT's November 2022 launch as the intervention point.

## Findings

- Aspirational wealth/hyper-masculine status motifs appear in ~55% of analyzed cluster combinations; transactional "trust proof" visuals (payment receipts, cash-out screenshots) in ~37%.
- Core drivers include aspirational wealth, manufactured trust, FOMO/urgency, gamification, celebrity endorsements (e.g., Manny Pacquiao), exploitation of social relations, and cultural/linguistic localization (Filipino, Urdu).
- The Urdu-language cluster embeds gambling in conservative cultural framings via depictions of women in distress and family-moral conflict — an ideologically inflected localization strategy.
- Mean monthly posts rose from 2,121 (pre-ChatGPT) to 280,952 (post-ChatGPT), a 13,242% increase; regression confirmed both level shift and slope change (p<0.0001), with a structural break in July 2023.
- Post-2022 visuals display AI-generation markers (hyper-real lighting, smoothed surfaces, improbable symbolic juxtapositions like sharks with slot machines) and stack multiple persuasion drivers in single images.
- Two emblematic AI-generated posts reached 4.3M and 3.3M views and were widely reshared across coordinated groups.

## Connections

This work extends the Vera AI / CooRnet lineage of coordinated link-sharing detection — see [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Giglietto2024-cbeb3f70]], and [[Marino2024-a678b03f]] — by applying its alert pipeline to a non-political harm domain. On the generative-AI side, it complements studies of AI-generated images and synthetic media in influence and coordinated operations such as [[DiGiuseppe2026-pu]], [[DiGiuseppe2025-es]], [[Kansaon2025-id]], and [[Achmann-Denkler2026-lx]], and shares concerns with broader work on AI-enabled coordinated campaigns like [[Luceri2025-tr]] and [[Yang2025-iv]]. Its emphasis on algorithmic amplification over moderation resonates with platform-governance critiques in [[Hurcombe2025-cs]] and [[Graham2025-gp]].

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
