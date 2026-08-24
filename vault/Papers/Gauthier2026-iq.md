---
title: "The political effects of X’s feed algorithm"
aliases: ["The political effects of X’s feed algorithm"]
authors: ["Germain Gauthier", "Roland Hodler", "Philine Widmer", "Ekaterina Zhuravskaya"]
year: 2026
doi: 10.1038/s41586-026-10098-2
bibtex_key: Gauthier2026-iq
topics: [platform-policy-and-content-visibility, political-polarization-and-engagement]
citation_count: 8
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

This paper reports a pre-registered field experiment (July–September 2023, 4,965 US-based X users) that randomly assigned participants for seven weeks to either X's algorithmic "For you" feed or its chronological "Following" feed. The core finding is that switching from a chronological to an algorithmic feed causally shifted users' political attitudes in a conservative direction — on policy priorities, the criminal investigations into Trump, and the war in Ukraine — while switching the algorithm *off* produced no comparable reversal. The authors trace this asymmetry to a persistence mechanism: algorithmic exposure leads users to follow conservative activist accounts, and those follows (and the exposure they create) endure even after the algorithm is deactivated. In doing so, the paper offers an explanation for why Meta's 2020 collaborative studies found null feed-algorithm effects, and documents the partisan slant of X's algorithm following Musk's acquisition.

## Key Contributions

- First independent (non-platform-cooperative) randomized evidence that a major feed algorithm causally shifts political attitudes.
- Resolves the puzzle of null effects in the 2020 Meta study by demonstrating that algorithmic effects are asymmetric and persist through users' follow choices.
- Documents the conservative/activist slant of X's post-acquisition algorithm, which amplifies conservative and activist content while demoting traditional media.
- Introduces a design that exploits platform-provided feed-choice features to run platform-independent randomized experiments.
- Reframes algorithmic influence as operating not only directly (what is shown) but indirectly (whom users choose to follow).
- Distinguishes malleable outcomes (policy attitudes, current-event views) from rigid ones (partisanship, affective polarization).

## Methods

- Pre-registered RCT (AEARCTR-0011464) with US-based YouGov panelists who were active X users; two simultaneous experiments based on users' initial feed setting.
- Seven-week treatment with pre/post surveys covering engagement, partisanship, affective polarization, policy priorities, Trump-investigation views, Ukraine attitudes, and life satisfaction.
- Custom Chrome extension captured the first 100 posts each user saw under each feed setting; scraping of followed-account lists for 2,387 consenting participants.
- Llama 3-based NLP classified posts and accounts by political leaning and type (activist, news outlet, entertainment, official), validated against ML classifiers and human annotators.
- ITT regressions (unconditional and GRF-adjusted), LATE via 2SLS instrumenting self-reported compliance, Lee bounds and re-weighting for attrition, and Poisson/OLS with fixed effects for content differences.

## Findings

- Switching onto the algorithm produced a 0.12 SD rise in conservative policy priorities, 0.08 SD greater belief that Trump investigations are unacceptable, and 0.12 SD more pro-Kremlin attitudes on Ukraine.
- Engagement rose 0.14 SD when the algorithm was switched on; switching it off gave a non-significant 0.06 SD decline.
- Effects were precisely null for partisanship and affective polarization in both directions.
- The algorithmic feed made conservative posts 2.9 pp (19.9%) more likely, political-activist posts 5.9 pp (27.4%) more likely, and entertainment posts 9.1 pp more likely, while cutting news-outlet posts by 15.5 pp (58.1%).
- It increased likes, reposts, and comments on shown posts by roughly 480%, 408%, and 508%.
- Users switched onto the algorithm became more likely to follow conservative accounts (+0.17 SD) and conservative activist accounts (+0.18 SD) — follows that persisted.
- Even on later chronological feeds, previously exposed users saw ~9 pp more conservative-account posts, showing persistent reshaping of exposure.
- Effects concentrated among Republicans and Independents; Democrats were largely unaffected.

## Connections

This is a rare independent, causal counterpoint to platform-cooperative feed experiments, and it directly engages the algorithmic-amplification and filter-bubble debates that run through much of this literature — including [[Bakshy2015-rn]]'s foundational work on selective exposure and algorithmic curation on social platforms. Its focus on X's post-Musk partisan slant and content ranking connects to platform-behavior and amplification studies such as [[Bouchaud2026-lr]] and [[Efstratiou2025-gs]], while its distinction between malleable attitudes and stable affective polarization speaks to the partisan-news and polarization strand represented by work like [[Green2025-ap]] and [[Tornberg2025-ir]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gauthier2026-iq.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-x-algorithm-how-feeds-shift-political/id1866587707?i=1000750452305)
