---
title: "The partisan effects of social media bans"
aliases: ["The partisan effects of social media bans"]
authors: ["Tiago Ventura", "Christopher Barrie", "Margaret E. Roberts", "Christopher Schwarz", "Joshua A Tucker"]
year: 2026
doi: 10.31235/osf.io/4stfw_v1
bibtex_key: Ventura2026-yc
topics: [platform-governance-apis, polarization-hybrid-media]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31235/osf.io/4stfw_v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ventura2026-yc.mp3
pdf_available: true
discovery_date: 2026-03-27T17:13:56.619909Z
---

# The partisan effects of social media bans

> Ventura, T., Barrie, C., Roberts, M. E., Schwarz, C., & Tucker, J. A. (2026). The partisan effects of social media bans. https://doi.org/10.31235/osf.io/4stfw_v1
>
> [View paper](https://doi.org/10.31235/osf.io/4stfw_v1)

## Summary

This paper exploits Brazil's 2024 Supreme Court–ordered nationwide ban on X to study how platform-level bans reshape partisan information environments in democracies. Combining ideal-point estimates from news-sharing behavior with an event-study design on a panel of politically engaged users, the authors show that conservative (anti-government) users disproportionately circumvented the ban via VPNs while liberal users complied and went silent. The resulting rightward shift in posting, engagement, and shared news persisted months after the ban was lifted. The authors theorize this as a "sorting ratchet": politicized bans produce asymmetric compliance shaped by partisan reputational and instrumental incentives, durably reshaping the digital public sphere rather than neutrally reducing harm.

## Key Contributions

- Provides one of the first causal estimates of a democratic platform ban's partisan consequences, moving beyond the authoritarian cases that dominate the information-control literature.
- Introduces the **sorting ratchet** concept: asymmetric partisan compliance with platform regulation that durably alters platform composition even after restrictions end.
- Methodologically combines correspondence-analysis ideal-point estimation (validated against survey audience-ideology measures, r = 0.85) with a Poisson event-study design.
- Reframes platform polarization debates by emphasizing between-platform sorting induced by state regulation, not just within-platform algorithmic dynamics.
- Surfaces a regulator's dilemma: misinformation-targeted bans may reallocate rather than neutralize partisan control of information ecosystems.

## Methods

A case study of Brazil's Aug 30–Oct 8, 2024 X ban. The authors collected ~14M Portuguese tweets with URLs (Decahose, 90 days pre-ban) and used GPT-4o plus manual review to identify 242 political news domains. Correspondence analysis on a 9,061-user × 242-domain sharing matrix yielded ideal points for users and outlets. They scraped timelines (Jun–Dec 2024) for 7,471 politically engaged users via Nitter (~6.7M tweets, ~430K news shares), then estimated Poisson event-study models with user and day fixed effects to capture monthly partisan differences in posting and news-sharing, alongside descriptive analyses of dropout, engagement concentration, and news-environment ideology. Robustness checks vary bandwidths, ideology cutoffs, estimators, and engagement outcomes.

## Findings

- Overall activity collapsed during the ban (daily tweets fell from ~37k to ~11k; news shares from ~2,587 to ~395).
- Right-leaning users posted roughly 5.8× more than left-leaning users during the ban (β = 1.76, z = 12.6).
- The weighted median ideology of shared news rose from 0.27 pre-ban to 1.26 during the ban (~1.05 SD rightward), and remained elevated at 0.30 post-ban.
- 2,346 of 7,291 pre-ban active users went silent during the ban; 656 never returned, with left-leaning users disproportionately exiting.
- Right-leaning users' share of likes rose from ~73% pre-ban to ~90% during the ban, settling around 80% post-ban — engagement concentration is durable.
- Partisan divergence began *before* formal enforcement, tracking the political escalation of the legal conflict in mid-August.

## Connections

This paper speaks directly to platform governance work on the political consequences of moderation and removal decisions, complementing studies of deplatforming and migration such as [[Efstratiou2025-gs]] and [[Jurg2025-ur]], and broader debates on platform power and regulation in [[Rieder2026-pp]] and [[Helmond2026-ll]]. Its sorting-ratchet account of asymmetric partisan exit and persistence engages the polarization and echo-chamber literature represented by [[Tornberg2025-ir]], [[Tornberg2026-lc]], and [[Bakshy2015-rn]], reframing platform-induced polarization as a between-platform phenomenon driven by state regulation. The Brazilian case also resonates with hyperpartisan and misinformation-ecosystem work like [[Rossini2026-jn]] and [[Cazzamatta2026-lo]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ventura2026-yc.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-banned-no-more-how-platform-bans/id1866587707?i=1000757761797)
