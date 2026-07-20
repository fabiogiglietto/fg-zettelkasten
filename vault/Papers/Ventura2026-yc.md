---
title: "The partisan effects of social media bans"
aliases: ["The partisan effects of social media bans"]
authors: ["Tiago Ventura", "Christopher Barrie", "Margaret E. Roberts", "Christopher Schwarz", "Joshua A Tucker"]
year: 2026
doi: 10.31235/osf.io/4stfw_v1
bibtex_key: Ventura2026-yc
topics: [political-polarization-partisanship, electoral-communication-cross-national]
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

This paper offers one of the first causal analyses of a nationwide social-media ban in a democratic, polarized context: Brazil's Supreme Court–ordered shutdown of X from August 30 to October 8, 2024. Using an event-study design on a panel of politically engaged users with correspondence-analysis-based ideal-point estimates, the authors show that the ban did not silence the platform uniformly. Instead, conservative (anti-government) users disproportionately circumvented the ban while liberal users went silent or left, shifting the platform's news environment sharply rightward. Crucially, these effects persisted for months after the ban was lifted, which the authors interpret as a durable "sorting ratchet" — asymmetric partisan compliance that reshapes a platform's composition long after the intervention ends. The core policy implication is that misinformation-targeting bans in democracies may reallocate rather than neutralize partisan control of information environments.

## Key Contributions

- Provides an early causal analysis of a platform ban in a democratic, polarized setting, extending a literature dominated by authoritarian cases.
- Introduces and empirically documents the **"sorting ratchet"** concept: asymmetric partisan compliance that durably reshapes platform composition even after restrictions end.
- Combines correspondence-analysis ideal-point estimation of both users and news domains with a Poisson event-study design.
- Shifts the analytic focus from *within-platform* algorithmic sorting to *between-platform* sorting induced by state regulation.
- Frames a policy trade-off: bans intended to curb misinformation can deepen polarization instead.

## Methods

- Case study of Brazil's ~six-week ban on X, with tweet data collected via the X Decahose API (~14M Portuguese-language tweets with URLs over 90 pre-ban days).
- Estimated ideal points for 9,061 users and 242 political news domains via correspondence analysis on a user-by-domain sharing matrix; political/news domains identified with GPT-4o zero-shot classification plus manual review.
- Validated ideology scores against survey-based audience-ideology measures (Pearson r = 0.85).
- Scraped timelines (June–December 2024) for 7,471 users via Nitter (~6.7M tweets, ~430K news shares).
- Poisson event-study (flexible difference-in-differences) models with user and day fixed effects and clustered standard errors, with robustness checks across OLS specifications, bandwidths (10/30 days), alternative ideology cutoffs, and engagement outcomes.

## Findings

- Overall activity collapsed during the ban (daily tweets fell from ~37,207 to ~11,305; news shares from 2,587 to 395).
- Right-leaning users posted roughly 5.8× more than left-leaning users during the ban (β = 1.76, z = 12.6).
- Weighted median news ideology rose from 0.27 pre-ban to 1.26 during the ban (~1.05 SD more right-leaning), and remained elevated at 0.30 afterward.
- Of 7,291 pre-ban active users, 2,346 went silent and 656 never returned; dropouts were disproportionately left-leaning.
- Engagement concentrated among right-leaning users: their share of likes rose from ~73% pre-ban to ~90% during, settling around 80% post-ban.
- Partisan divergence began *before* formal enforcement, tracking the mid-August legal escalation.
- Results are robust across alternative specifications and outcomes.

## Connections

This paper shares authors and methodological lineage with [[Ventura2025-sw]], and its correspondence-analysis approach to platform-level ideological composition and news exposure connects to large-scale platform-audience studies such as [[Gonzalez-Bailon2024-rq]], [[Bakshy2015-rn]], and [[Allcott2025-jb]]. Its focus on platform governance and content moderation as drivers of information-environment change also links it to work on misinformation and platform interventions like [[Starbird2025-jj]] and [[Mosleh2024-op]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ventura2026-yc.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-banned-no-more-how-platform-bans/id1866587707?i=1000757761797)
