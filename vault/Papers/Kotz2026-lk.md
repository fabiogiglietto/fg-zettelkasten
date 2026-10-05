---
title: "Conversational AI shifts beliefs and policy support among skeptics across contested societal issues"
aliases: ["Conversational AI shifts beliefs and policy support among skeptics across contested societal issues"]
authors: ["Johannes Kotz", "Kevin E. Tiede", "Jelena Meyer", "Maj-Britt Sterba", "Christian Breunig", "Wolfgang Gaissmaier"]
year: 2026
doi: 10.31234/osf.io/7szrn_v1
bibtex_key: Kotz2026-lk
topics: [climate-and-misinformation-message-interventions, generative-ai-and-synthetic-media]
citation_count: 0
open_access: false
source_url: https://doi.org/10.31234/osf.io/7szrn_v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kotz2026-lk.mp3
pdf_available: true
discovery_date: 2026-07-12T07:23:36.517977Z
---

# Conversational AI shifts beliefs and policy support among skeptics across contested societal issues

> Kotz, J., Tiede, K. E., Meyer, J., Sterba, M., Breunig, C., & Gaissmaier, W. (2026). Conversational AI shifts beliefs and policy support among skeptics across contested societal issues. https://doi.org/10.31234/osf.io/7szrn_v1
>
> [View paper](https://doi.org/10.31234/osf.io/7szrn_v1)

## Summary

This large-scale preregistered experiment (N=6,558 U.S. participants) tests whether brief, evidence-based dialogues with GPT-5 can shift beliefs and policy support across three structurally distinct contested issues: climate change, vaccination, and economic inequality. Compared to a neutral control conversation, the AI dialogues shifted beliefs in all three domains and increased support for politically contested policy instruments such as carbon and estate taxes. Crucially, effects were strongest among the audiences typically hardest to reach — initially skeptical participants — and were amplified among those with higher trust in science. Text analysis revealed that GPT-5 adaptively tailored its persuasive strategies to skeptics, leaning more on prebunking and steelmanning. The authors position conversational AI as a scalable tool for evidence-based public communication, while flagging governance concerns about persuasion at scale.

## Key Contributions

- Demonstrates that AI-based persuasion generalizes across three structurally distinct contested issues, moving beyond single-domain studies.
- Extends the research frontier from belief change to specific contested *policy* instruments (carbon tax, mandatory vaccination, estate tax), showing belief change alone does not reliably translate into policy support.
- Provides systematic heterogeneity evidence: effects are strongest among skeptics and high-science-trust individuals — contrasting prior work suggesting static AI messages work best on sympathetic audiences.
- Characterizes the persuasive strategies conversational AI adopts and how it adapts them to participants' baseline attitudes.
- Offers a low-cost, prompt-based communication tool while raising ethical and governance concerns.

## Methods

- Preregistered online experiment via Qualtrics/Bilendi, N=6,558 U.S. participants (mean age 58.6; 62.8% female), with a deliberate conservative oversample (~57.6% Republican / 42.4% Democrat).
- Ten conditions: 3 topics (climate, vaccination, inequality) × 3 intervention types (belief-targeted, policy-targeted, combined) plus a neutral control (cats vs. dogs).
- Participants engaged in a structured three-round GPT-5 dialogue advocating the target belief/policy with scientific evidence while inviting questions; beliefs and policy support measured pre/post on 0–100 sliders.
- Analysis: multiple linear regression predicting post-intervention attitudes (controlling for baseline and actively open-minded thinking), with interaction terms for baseline attitudes and trust moderators; Bonferroni correction within outcome families (α=.0056); mixed-effects robustness checks; and exploratory GPT-5-based classification of 11 persuasive strategies (88.5% reproducibility).

## Findings

- All interventions raised beliefs and policy support in their targeted domains; largest main effects for economic inequality (belief +6.36 pps; estate tax +8.98 pps) where baseline attitudes were lowest.
- Climate belief rose ~3.5–3.7 pps and carbon tax support up to 4.80 pps (combined); vaccination effects were smaller due to high baselines, with mandatory-vaccination policy shifts not surviving correction.
- Treatment effects grew as baseline attitudes declined — dialogues were most effective among skeptics — exceeding what regression to the mean would predict.
- Combined interventions did not outperform outcome-specific ones; belief-targeted interventions produced only smaller spillover onto policy support.
- Trust in science consistently roughly doubled effect sizes at +1 SD; trust in AI was weaker, trust in government inconsistent, and AOT unreliable.
- GPT-5 most consistently used iterative collaborative dialogue and person-centered alignment, applying prebunking/debunking and steelmanning more with skeptics and bridging-to-action strategies more with supporters.

## Connections

This paper builds directly on demonstrations that LLM dialogues can durably reduce conspiracy beliefs, most notably [[Costello2024-bg]], extending that dialogue paradigm from misbeliefs to contested policy attitudes. It shares the empirical concern with measuring AI persuasion magnitude and audience heterogeneity found in [[Hackenburg2025-dj]], while its finding that skeptics are the most movable audience offers a counterpoint to static-message persuasion work. The steelmanning/prebunking strategies it identifies connect to inoculation and prebunking research such as [[van-der-Linden2026-jt]] and [[Spampatti2026-kx]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kotz2026-lk.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
