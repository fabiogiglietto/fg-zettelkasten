---
title: "The political effects of X’s feed algorithm"
aliases: ["The political effects of X’s feed algorithm"]
authors: ["Germain Gauthier", "Roland Hodler", "Philine Widmer", "Ekaterina Zhuravskaya"]
year: 2026
doi: 10.1038/s41586-026-10098-2
bibtex_key: Gauthier2026-iq
topics: [platform-governance-apis, polarization-hybrid-media]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1038/s41586-026-10098-2
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gauthier2026-iq.mp3
pdf_available: true
discovery_date: 2026-02-19T06:33:46.898860Z
---

# The political effects of X’s feed algorithm

> Gauthier, G., Hodler, R., Widmer, P., & Zhuravskaya, E. (2026). The political effects of X’s feed algorithm. *Nature*, 1–8. https://doi.org/10.1038/s41586-026-10098-2
>
> [View paper](https://doi.org/10.1038/s41586-026-10098-2)

## Summary

This paper reports a pre-registered field experiment with ~5,000 active US-based X users in summer 2023, exploiting X's then-new ability to toggle between an algorithmic "For you" feed and a chronological "Following" feed. Random assignment for seven weeks shows that switching users from chronological to algorithmic exposure causally shifts political attitudes in a conservative direction — on policy priorities, the Trump investigations, and the war in Ukraine — while leaving partisanship and affective polarization unmoved. The effect is strikingly asymmetric: turning the algorithm off does not undo it, because algorithmic exposure induces users to follow conservative activist accounts whose content continues to dominate their feed afterward. The authors argue this persistence mechanism reconciles their findings with the null results of the 2020 Meta studies and reconceptualizes algorithms as shaping exposure indirectly through follow choices, not merely through ranking.

## Key Contributions

- First independent (non-platform-collaborative) randomized evidence that a major feed algorithm causally moves political attitudes.
- Identifies an asymmetric, hysteretic mechanism — algorithm-induced follows persist — that resolves the puzzle of prior null findings.
- Documents the post-Musk slant of X's algorithm: amplification of conservative and activist content, demotion of traditional news outlets.
- Methodological template for platform-independent RCTs that exploits user-facing feed-choice features.
- Conceptual distinction between malleable outcomes (issue attitudes) and rigid ones (party ID, affective polarization).

## Methods

Pre-registered RCT (AEARCTR-0011464) with 4,965 YouGov panelists who are active X users, randomized for seven weeks between the "For you" and "Following" tabs, with pre/post surveys on engagement, attitudes, and polarization. A custom Chrome extension scraped the first 100 posts shown to each user under each feed, and follow-lists were collected for 2,387 consenting users. Posts and accounts were classified for political leaning and type (activist, news, entertainment, official) using a Llama-3 pipeline validated against ML and human annotators. Estimation combines ITT regressions, GRF-adjusted conditional specifications, 2SLS LATEs, Lee bounds for attrition, and Poisson/OLS models with fixed effects for content composition.

## Findings

- Switching on the algorithm increased conservative policy priorities by 0.12 SD, belief that Trump investigations are unacceptable by 0.08 SD, and pro-Kremlin Ukraine attitudes by 0.12 SD.
- Engagement rose 0.14 SD when the algorithm was turned on; likes, reposts, and comments on shown posts jumped roughly 480%, 408%, and 508%.
- Switching the algorithm off produced no significant attitude changes — confirming asymmetry.
- Partisanship and affective polarization were precisely null in both directions.
- Algorithmic feed showed 19.9% more conservative posts, 27.4% more activist content, 21.5% more entertainment, and 58.1% fewer traditional news outlet posts.
- Algorithm exposure increased follows of conservative accounts (+0.17 SD) and conservative activists (+0.18 SD), and these follows persisted; users later on chronological feeds still saw 9 pp more conservative content.
- Attitude effects concentrated among Republicans and Independents; Democrats largely unaffected.

## Connections

This paper is in direct dialogue with the Meta 2020 collaborative studies, and its asymmetry-via-follows mechanism offers a substantive reinterpretation of [[Allcott2025-jb]]'s broader work on social-media exposure and political outcomes. It also complements experimental work on persuasion and messaging effects such as [[Voelkel2026-lc]] by showing that algorithmically curated exposure — rather than designed interventions — can shift issue attitudes while leaving identity-laden measures like partisanship and affective polarization unchanged.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gauthier2026-iq.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-x-algorithm-how-feeds-shift-political/id1866587707?i=1000750452305)
