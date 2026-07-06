---
title: "“keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities"
aliases: ["“keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities"]
authors: ["CATIE SNOW BAILARD", "REBEKAH TROMBLE", "WEI ZHONG", "FEDERICO BIANCHI", "PEDRAM HOSSEINI", "DAVID BRONIATOWSKI"]
year: 2024
doi: 10.1017/s0003055423001478
bibtex_key: Bailard2024-pj
topics: [computational-social-science, information-disorder]
citation_count: 9
open_access: false
source_url: https://doi.org/10.1017/s0003055423001478
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bailard2024-pj.mp3
pdf_available: true
discovery_date: 2026-05-17T08:06:58.350298Z
---

# “keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities

> BAILARD, C. S., TROMBLE, R., ZHONG, W., BIANCHI, F., HOSSEINI, P., & BRONIATOWSKI, D. (2024). “keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities. *American Political Science Review*, *118*, 1–18. https://doi.org/10.1017/s0003055423001478
>
> [View paper](https://doi.org/10.1017/s0003055423001478)

## Summary

This paper investigates whether and how the Proud Boys' online discourse on Telegram is linked to their offline violent and nonviolent activities between January 2020 and July 2022. Combining a fine-tuned DeBERTa classifier of collective action frames across 500,000+ messages from 92 affiliated channels with ACLED event data, the authors use vector autoregression and impulse response analysis to demonstrate temporal relationships between framing and action. Their core argument is that diagnostic (grievance) and motivational (solidarity/pride) framing—not explicit calls-to-action—predict subsequent offline violence, and that offline nonviolent protests feed back into motivational framing, producing a reciprocal cycle that culminates in violent mobilization. The findings challenge content-moderation paradigms focused on discrete hateful posts and argue for analyzing extremist discourse as a temporally dynamic ecosystem.

## Key Contributions

- One of the first large-scale longitudinal empirical links between specific types of far-right online discourse and offline violent/nonviolent events.
- A fine-tuned DeBERTa NLP pipeline for detecting collective action frames at scale, moving beyond toxicity/hate-speech classifiers (macro F1 = 0.80).
- Theoretical articulation of a reciprocal "online messaging–offline action cycle" between protest activity and solidarity discourse.
- Extension of collective action framing theory with moralizing and moral convergence concepts to explain the grievance-to-violence pathway.
- Practical implications for moderation: explicit calls-to-action are *not* the most predictive content; grievance and solidarity-building speech matter more.
- Public release of code and classified datasets via the APSR Dataverse.

## Methods

The authors snowball-collected Telegram channels via Telethon, narrowing to 92 explicitly Proud Boys-affiliated channels. Trained annotators hand-coded 12,189 messages (Gwet's AC ≈ 0.82) along diagnostic, prognostic, motivational, injustice, and othering frames, which were used to fine-tune a DeBERTa multi-label classifier. Classified weekly time series were merged with 376 ACLED Proud Boys-involved events and analyzed using VAR models, Granger causality tests, and impulse response functions, with stationarity and residual diagnostics. Robustness checks include a regional first-difference time-series cross-sectional analysis across 53 region-specific channels and a structural equation mediation model.

## Findings

- Diagnostic frames dominate (~34% of weekly posts); motivational frames appear in ~9%.
- Rising diagnostic framing Granger-causes later offline violent events; injustice/othering subframes show weaker but similar effects.
- Increases in motivational framing (both proportion and frequency) predict subsequent violent events.
- Prognostic frames (explicit calls-to-action) predict neither violent nor nonviolent events.
- Nonviolent protests predict subsequent increases in motivational framing—but not other frame types.
- Impulse response analysis suggests a ~4-week cycle: nonviolent protest → motivational framing peaks at ~2 weeks → violent event probability peaks ~2 weeks later.
- SEM estimates ~8% of the nonviolent-to-violent effect is mediated by motivational framing.
- Regional analysis confirms motivational frequency predicts state-level violence, while diagnostic framing does not at that scale.

## Connections

This work complements other computational and discursive analyses of far-right online ecosystems—particularly studies that map how grievance and identity-building discourse drive radicalization trajectories such as [[Rothut2026-wt]] and [[Askanius2026-de]]. Its emphasis on solidarity/motivational framing as a mobilization mechanism resonates with work on far-right community-building and affective belonging like [[Nangle2026-yo]] and [[Karo2026-dn]], while its critique of content-moderation paradigms speaks to platform-governance concerns raised in [[Bouchafra2026-ts]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bailard2024-pj.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-the-hidden-speech-that-predicts/id1866587707?i=1000768724100)
