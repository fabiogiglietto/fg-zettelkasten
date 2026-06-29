---
title: "Perceived political bias in LLMs reduces persuasive abilities"
aliases: ["Perceived political bias in LLMs reduces persuasive abilities"]
authors: ["Matthew DiGiuseppe", "Joshua Robison"]
year: 2026
doi: 10.48550/arxiv.2602.18092
bibtex_key: DiGiuseppe2026-pu
topics: [generative-ai-and-media]
citation_count: 0
open_access: true
source_url: https://doi.org/10.48550/arxiv.2602.18092
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/DiGiuseppe2026-pu.mp3
pdf_available: true
discovery_date: 2026-03-05T20:57:12.346424Z
---

# Perceived political bias in LLMs reduces persuasive abilities

> DiGiuseppe, M., & Robison, J. (2026). Perceived political bias in LLMs reduces persuasive abilities. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2602.18092v1)

## Summary

This preregistered U.S. survey experiment (N=2144) tests whether perceived political bias of a conversational LLM diminishes its ability to correct economic misconceptions. Participants holding one of six economic misconceptions engaged in a three-round dialogue with GPT-4.1 after being told either nothing, that the model was generically biased, or that the model was biased against their party (light or heavy framing). Brief out-party bias warnings cut belief correction by roughly 23–28% relative to control, with transcript analysis showing users argued back more rather than disengaging. The authors argue that perceived neutrality is a previously underappreciated boundary condition on LLM persuasion, and that elite politicization of AI could blunt its epistemic value.

## Key Contributions

- First experimental (rather than observational) evidence that manipulating perceived political bias of an LLM causally attenuates its persuasive power.
- Extends classical source-credibility and motivated-reasoning theories from political science into human–LLM interaction, positioning perceived neutrality alongside interactivity, personalization, and information volume as a lever of AI persuasion.
- Introduces a measurement pipeline combining LLM-as-judge pairwise comparisons with a Bayesian Bradley–Terry model to recover latent conversational traits (argumentativeness, dismissiveness) from transcripts.
- Surfaces policy-relevant implications about how elite politicization of AI could asymmetrically distribute the epistemic benefits of LLM-based fact-checking.

## Methods

A four-arm between-subjects experiment on Prolific (Dec 2025–Jan 2026) randomized participants to a no-information control, a non-directional bias warning, or light/heavy out-party bias warnings (the heavy condition added an image linking Sam Altman to the respondent's out-party). Each participant held one of six economic misconceptions (e.g., household-budget analogy, rent control, trade deficits) measured pre/post, then completed a three-round conversation with GPT-4.1 prompted to argue the academic-economist consensus while remaining truthful. Analysis used OLS with topic fixed effects and pretreatment controls, bootstrap CIs on attenuation ratios, heterogeneous-effects tests, and a Bradley–Terry scaling of LLM-judged transcript comparisons with Rubin's Rules for uncertainty propagation.

## Findings

- Mean misconception agreement (0–4 scale) shifted by −1.20 in control vs. −0.93 (light) and −0.86 (heavy), an attenuation of ~23–28%.
- Full opinion reversals fell from 34.4% in control to 22.1% under the heavy treatment.
- Effects were broadly distributed: positive attenuation point estimates in four of six topics.
- Bias warnings raised perceived out-party bias for both Democrats and Republicans, erasing baseline partisan asymmetries in trust.
- No significant moderation by partisan strength, misconception-party alignment, affective polarization, AI trust, or topic knowledge.
- Heavy-treatment respondents wrote longer, more argumentative (but not more dismissive) replies — consistent with motivated reasoning rather than heuristic disengagement.
- Treatments also lowered rated persuasiveness (d=−0.31), willingness to use AI to challenge beliefs (d=−0.20), general AI chatbot trust (d=−0.10), and support for political use of AI (d=−0.24).

## Connections

This paper directly extends the LLM-persuasion line of work by [[Hackenburg2025-dj]] and [[Schroeder2026-im]], introducing perceived neutrality as a moderator that earlier apolitical designs could not detect. It complements [[DeVerna2025-dl]] on LLM fact-checking and resonates with [[Lin2025-xp]] and [[Triedman2025-uy]] on how political framing and source perceptions shape engagement with AI outputs; it also pairs naturally with the same authors' prior work [[DiGiuseppe2025-es]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/DiGiuseppe2026-pu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-llms-can-political-bias-kill-persuasion/id1866587707?i=1000753721566)
