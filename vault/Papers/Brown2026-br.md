---
title: "Evaluating echo chambers, rabbit holes, and radicalization pathways on YouTube"
aliases: ["Evaluating echo chambers, rabbit holes, and radicalization pathways on YouTube"]
authors: ["Megan A. Brown", "James Bisbee", "Angela Lai", "Richard Bonneau", "Jonathan Nagler", "Joshua A. Tucker"]
year: 2026
doi: 10.1080/10584609.2026.2671765
bibtex_key: Brown2026-br
topics: [platform-governance-apis, polarization-hybrid-media]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1080/10584609.2026.2671765
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Brown2026-br.mp3
pdf_available: true
discovery_date: 2026-06-13T22:33:59.084618Z
---

# Evaluating echo chambers, rabbit holes, and radicalization pathways on YouTube

> Brown, M. A., Bisbee, J., Lai, A., Bonneau, R., Nagler, J., & Tucker, J. A. (2026). Evaluating echo chambers, rabbit holes, and radicalization pathways on YouTube. *Political Communication*, 1–27. https://doi.org/10.1080/10584609.2026.2671765
>
> [View paper](https://doi.org/10.1080/10584609.2026.2671765)

## Summary

This paper asks whether YouTube's recommendation algorithm — independent of user choice — drives users into ideological echo chambers, content rabbit holes, or partisan radicalization pathways. The authors formally distinguish these three phenomena (as static distributions, serially-correlated dynamic sequences, and their interaction) and design an audit study that recruits real, logged-in users but randomizes both seed videos and traversal rules to separate supply-side from demand-side effects. They find only weak echo-chamber effects that largely vanish once user choice is removed, strong evidence of content (but not ideological) rabbit holes, and no evidence of radicalization pathways. Notably, the algorithm exhibits a uniform drift toward moderately conservative content for all users, regardless of partisanship or starting point.

## Key Contributions

- A formal, hierarchical conceptualization of echo chambers, rabbit holes, and radicalization pathways grounded in spatial utility models.
- A novel audit design that preserves ecological validity (real accounts, real watch histories) while randomizing seeds and traversal rules to identify algorithmic effects net of user choice.
- An original dataset of YouTube recommendations from 1,639 U.S. users collected in fall 2020.
- Empirical reconciliation of conflicting prior work: the algorithm produces content rabbit holes, not radicalization.
- A transferable auditing framework applicable to other recommender systems (TikTok, Facebook, X).
- Evidence that policy debates narrowly targeting YouTube's algorithm as a radicalization engine may be misdirected.

## Methods

The authors fielded a browser-plug-in audit study (Oct–Dec 2020) with 1,639 U.S. YouTube users recruited via Facebook ads. Users were randomly assigned one of 24 seed videos (15 political, 9 nonpolitical) and either a "preference" condition (click whichever recommendation looked interesting) or an "audit" condition (always click the *n*th recommendation), then traversed 20 recommendation steps. Video ideology was estimated via a two-stage method: correspondence analysis on a Reddit-derived video-by-subreddit matrix to generate training scores, then a BERT model predicting ideology from video metadata. Linear regressions with seed and step fixed effects, clustered standard errors, and triple-interaction specifications model recommendation ideology and its variance as functions of partisanship, watch history, current video, and step.

## Findings

- Republicans receive slightly more conservative recommendations than non-Republicans only in the preference condition (~0.16); the gap vanishes under the audit rule, indicating no independent algorithmic echo chamber.
- The currently played video strongly predicts the next recommendation's ideology (coefficients ~0.25–0.41), confirming content rabbit holes in both conditions.
- Influence of prior videos decays rapidly: only the two most recent videos meaningfully shape final-step recommendations, consistent with a Markov-like process.
- Recommendation ideological diversity narrows over traversal steps for all users.
- All users — Democrats, Republicans, liberal-seed, conservative-seed alike — drift toward moderately conservative content, but curvilinearly and with tapering, not escalating extremism.
- Descriptive analysis of 1.7M political videos shows YouTube's political catalog skews conservative and conservative content is more popular, plausibly explaining the algorithmic tilt.

## Connections

This paper sits squarely within the online-radicalization-far-right literature that increasingly questions strong algorithmic-radicalization narratives; it complements review and conceptual work such as [[Rothut2026-wt]] on far-right radicalization pathways and [[Nangle2026-yo]] on contested mechanisms of online radicalization. Its supply-vs-demand framing also speaks to broader debates on algorithmically mediated polarization addressed in [[Esau2025-tf]]. The other listed papers appear less directly related to the specific audit-methodology and recommender-system questions raised here.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Brown2026-br.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-whos-really-driving-youtubes-rabbit/id1866587707?i=1000772632531)
