---
title: "“keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities"
aliases: ["“keep your heads held high boys!”: Examining the relationship between the Proud Boys’ online discourse and offline activities"]
authors: ["CATIE SNOW BAILARD", "REBEKAH TROMBLE", "WEI ZHONG", "FEDERICO BIANCHI", "PEDRAM HOSSEINI", "DAVID BRONIATOWSKI"]
year: 2024
doi: 10.1017/s0003055423001478
bibtex_key: Bailard2024-pj
topics: [online-radicalization-and-extremism-on-platforms, llms-in-content-analysis]
citation_count: 11
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

This paper investigates how the online discourse of the Proud Boys on Telegram relates to their offline violent and nonviolent activities across a 31-month period (January 2020–July 2022). Drawing on collective action framing theory and supplementing it with theories of moralizing and moral convergence, the authors move away from a content-moderation paradigm that treats extremist speech as discrete hateful posts. Instead, they analyze the discursive ecosystem and its temporal dynamics, classifying over 500,000 messages into collective action frames and linking them to real-world event records. Their central finding is a reciprocal "online messaging–offline action cycle": grievance-based (diagnostic) and solidarity-building (motivational) framing predict subsequent offline violence, while offline nonviolent protests in turn feed back into motivational framing online.

## Key Contributions

- One of the first large-scale empirical analyses linking specific types of right-wing extremist online discourse to offline violent and nonviolent activity over time.
- A fine-tuned DeBERTa NLP pipeline for detecting collective action frames at scale, going beyond standard hate speech or toxicity classifiers.
- Identification and theorization of a reciprocal online messaging–offline action cycle between offline protest and online solidarity messaging.
- Extension of collective action framing theory by integrating moralizing and moral convergence frameworks.
- Practical implications for content moderation: explicit calls-to-action and hateful posts are less predictive than grievance and solidarity-building speech.
- Public release of documentation, classified datasets, and analysis scripts via the APSR Dataverse.

## Methods

The authors snowball-collected Telegram data via the Telethon API, identifying ~2,900 Proud Boys-affiliated channels and focusing on a core network of 92 explicitly Proud Boys channels. Trained annotators hand-coded 12,189 messages using a codebook covering diagnostic, prognostic, motivational, injustice, and othering frames (Gwet's AC ≈ 0.82, 88% agreement). A pretrained DeBERTa model was fine-tuned for multi-label frame classification (macro F1 = 0.80) and validated against held-out and blind-annotated samples. The classified message data were merged with ACLED US Crisis Monitor records of 376 Proud Boys-involved events, aggregated into weekly time-series. Analysis used vector autoregression (VAR) with Granger causality tests and impulse response functions, plus a regional first-difference cross-sectional analysis and a structural equation mediation model as robustness checks.

## Findings

- Diagnostic frames appeared in ~34% of weekly posts (injustice 13%, othering 11%), prognostic in 12%, motivational in 9%.
- Increased proportion of diagnostic frames Granger-causes subsequent offline violent events; injustice and othering subframes show weaker effects (p ≈ 0.07–0.09).
- Both the proportion and frequency of motivational frames predict subsequent violent events.
- Prognostic frames (explicit calls-to-action) do not predict either violent or nonviolent offline events.
- Nonviolent protests predict an increase in the proportion of motivational frames online in following weeks; no other frame type shows this responsiveness.
- Impulse response functions suggest a roughly four-week cycle: nonviolent protest → peak motivational framing at ~2 weeks → peak violent event probability ~2 weeks later.
- SEM estimates ~8% of the effect of nonviolent protests on later violent events is mediated by increases in motivational framing.
- Regional first-difference analysis confirms motivational message frequency predicts state-level violent events, while diagnostic framing does not at the regional level.

## Connections

This work sits within a cluster of studies on right-wing extremism and mobilization dynamics on platforms; it connects to research on the Proud Boys and far-right ecosystems such as [[Grusauskaite2026-po]] and [[Askanius2026-de]], and to work on radicalization pathways and online-to-offline linkages like [[Rothut2026-or]] and [[Rothut2026-wt]]. On the methodological side, its fine-tuned supervised classification of frames beyond toxicity detection aligns with computational content-analysis efforts such as [[Achmann-Denkler2026-lx]] and [[Balluff2026-if]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bailard2024-pj.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-the-hidden-speech-that-predicts/id1866587707?i=1000768724100)
