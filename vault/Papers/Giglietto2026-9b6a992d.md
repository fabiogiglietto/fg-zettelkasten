---
title: "Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"
aliases: ["Synthetic seduction: Evolving visual persuasion in coordinated online gambling promotion with generative {AI}"]
authors: ["Fabio Giglietto", "Massimo Terenzi", "Anwesha Chakraborty", "Giada Marino"]
year: 2026
doi: 10.1007/978-3-032-11782-3_4
bibtex_key: Giglietto2026-9b6a992d
kind: own
topics: [coordinated-inauthentic-behavior, generative-ai-and-media]
citation_count: 0
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

This paper examines how coordinated networks of Facebook groups promote online gambling through visual content, and how the public release of generative AI tools has reshaped that promotion. Analyzing 2,323 images shared across 223 coordinated public groups (identified through link-sharing coordination seeded from fact-checker-flagged accounts), the authors build a typology of persuasive visual drivers — aspirational wealth, manufactured trust, FOMO, gamification, celebrity endorsements, social-relations exploitation, and cultural localization — and show that generative AI has not invented new strategies but radically intensified, recombined, and scaled existing ones. They argue that the central governance problem is not moderation per se but algorithmic amplification operating in a regulatory grey zone where Meta strictly polices paid gambling ads while leaving organic gambling content largely unconstrained.

## Key Contributions

- An empirically grounded typology of visual persuasion drivers in coordinated organic gambling promotion.
- Evidence that generative AI functions as an accelerant and intensifier of established persuasion architectures rather than a source of qualitatively new strategies.
- A reproducible mixed-methods pipeline combining VLM-based denotative/connotative image description, dual embeddings, HDBSCAN clustering, and human qualitative coding for large-scale visual analysis.
- Identification of Meta's paid/organic regulatory asymmetry as a structural enabler of harmful gambling content.
- A reflexive critique of using LLMs as analytic tools while studying content produced by closely related generative technologies.

## Methods

The authors identified 223 coordinated Facebook groups via the Vera AI coordinated link-sharing detection workflow (14-second window, 0.995 edge weight) seeded from accounts that had spread fact-checker-flagged content, then collected 10,671 posts and 2,323 unique images (2017–2024) through the Meta Content Library plus a custom image downloader. Each image received structured denotative and connotative descriptions from gpt-4o-2024-08-06, which were embedded with text-embedding-3-small, reduced via UMAP, and clustered with HDBSCAN (101 denotative, 51 connotative clusters). Four coders qualitatively analyzed 85 high-frequency cluster combinations to derive the driver typology. Temporal analysis used two-sample tests, interaction-term regression, and structural break detection around the ChatGPT launch, complemented by qualitative pre/post comparison of stylistic markers of AI-generated imagery.

## Findings

- Aspirational wealth and hyper-masculine status motifs appear in ~55% of analyzed cluster combinations; transactional "trust proof" visuals (payment receipts, cash-out screenshots) in ~37%.
- Drivers operate synergistically and are often layered within single images, including celebrity endorsements (e.g., Manny Pacquiao) and localized cultural framings in Filipino and Urdu.
- An Urdu-language cluster embeds gambling within conservative moral narratives, using emotionally charged depictions of women in distress and family conflict.
- Mean monthly posts rose from 2,121 (pre-ChatGPT) to 280,952 (post-ChatGPT) — a 13,242% increase — with regression confirming both a level shift and a slope change (p<0.0001) and a structural break in July 2023.
- Post-2022 imagery shows consistent AI-generation markers (hyper-real lighting, smoothed surfaces, dreamlike saturation, improbable symbolic juxtapositions) and tends to combine multiple persuasion drivers in one frame.
- Two emblematic AI-generated posts reached 4.3M and 3.3M views with thousands of shares across the coordinated network.

## Connections

This paper sits at the intersection of the register's two themes — coordinated inauthentic behavior and generative AI in media — and builds directly on the Vera AI / CooRnet lineage of coordinated link-sharing detection developed in [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], and Giglietto2023-fa951ac5 (and methodologically related work such as [[Minici2024-tf]] and [[Graham2025-gp]]). Its argument that generative AI intensifies rather than replaces existing manipulation infrastructures resonates with [[Luceri2025-tr]], [[Gerard2025-br]], and [[DiGiuseppe2026-pu]] on AI-enabled influence operations, while its VLM-driven visual analysis pipeline parallels approaches in [[Achmann-Denkler2026-lx]] and [[Kansaon2025-id]]. The focus on algorithmic amplification and platform governance asymmetries also speaks to [[Helmond2026-ll]] and [[Hurcombe2025-cs]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Giglietto2026-9b6a992d.mp3)
