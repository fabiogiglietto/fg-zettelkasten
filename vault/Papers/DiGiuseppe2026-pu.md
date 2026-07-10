---
title: "Perceived political bias in LLMs reduces persuasive abilities"
aliases: ["Perceived political bias in LLMs reduces persuasive abilities"]
authors: ["Matthew DiGiuseppe", "Joshua Robison"]
year: 2026
doi: 
bibtex_key: DiGiuseppe2026-pu
topics: [public-perceptions-and-labor-impacts-of-ai, political-polarization-partisan-news]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2602.18092v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/DiGiuseppe2026-pu.mp3
pdf_available: true
discovery_date: 2026-03-05T20:57:12.346424Z
---

# Perceived political bias in LLMs reduces persuasive abilities

> DiGiuseppe, M., & Robison, J. (2026). Perceived political bias in LLMs reduces persuasive abilities. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2602.18092v1)

## Summary

This preregistered U.S. survey experiment (N=2144) asks whether perceptions of political bias undermine the persuasive power of conversational AI. Participants who held one of six common economic misconceptions engaged in a three-round conversation with GPT-4.1 designed to correct their belief while remaining truthful. Before the conversation, they were randomly assigned to receive no information, a non-directional bias warning, or a light or heavy warning claiming the model was politically biased against their party. Brief out-party bias cues reduced belief correction by roughly 23–28% relative to the neutral control. Because the model's arguments were held constant, the effect stems from perceptions of the messenger rather than message content, leading the authors to argue that LLM persuasion is politically contingent on perceived neutrality.

## Key Contributions

- First *experimental* (rather than correlational) evidence that manipulating an LLM's perceived political bias causally attenuates its persuasive effect.
- Extends classic source-credibility and motivated-reasoning theory to human–LLM interaction, positioning perceived neutrality as a boundary condition for AI persuasion.
- Introduces a transcript-scaling method combining LLM-as-judge pairwise comparisons with a Bayesian Bradley–Terry model to estimate latent conversational behaviors (argumentativeness, dismissiveness).
- Flags policy-relevant asymmetries: elite politicization of AI could blunt the epistemic benefits of LLM fact-checking and distribute them unevenly across the political spectrum.

## Methods

- Preregistered four-arm between-subjects online experiment on Prolific (Dec 2025–Jan 2026), U.S. quota sample, N=2144 analytic.
- Two-stage measurement of six economic misconceptions (e.g., household-government budget analogy, rent control, zero-sum immigration, trade deficits, tax cuts, Buy American) to mitigate acquiescence bias.
- Random assignment to: no-information control, non-directional bias warning, light out-party bias warning, or heavy out-party warning (adding text and an image linking OpenAI's CEO to the respondent's out-party).
- Three-round conversation with GPT-4.1 prompted to persuade toward the academic-economist consensus while staying truthful.
- OLS with topic fixed effects and pretreatment agreement; bootstrap CIs for attenuation ratios; tests for heterogeneity by partisanship, alignment, affective polarization, AI trust, and topic knowledge.
- Transcript analysis via LLM-as-judge (gpt-5-mini) pairwise comparisons scaled through Bayesian Bradley–Terry, with uncertainty propagated using Rubin's Rules.

## Findings

- Mean pre–post change in misconception agreement (0–4 scale): −1.20 in control vs. −0.93 (light) and −0.86 (heavy).
- Full opinion reversals dropped from 34.4% (control) to 22.1% (heavy treatment).
- Persuasion-undermining effects were broadly distributed, with positive point estimates in four of six topics.
- Bias warnings raised perceived out-party bias for both Democrats and Republicans, erasing baseline partisan differences.
- No significant heterogeneity by partisan strength, alignment, affective polarization, AI trust, or self-reported knowledge.
- Heavy-treatment respondents wrote more and were rated more argumentative but not more dismissive — contradicting a pure low-effort heuristic-discounting account and supporting directional motivated reasoning.
- Treatments also lowered rated LLM persuasiveness (d=−0.31), willingness to reuse AI to challenge beliefs (d=−0.20), general trust in chatbots (d=−0.10), and support for politicians using AI (d=−0.24).

## Connections

This paper directly engages the growing literature on LLM persuasion and belief correction, most notably connecting to [[Hackenburg2026-ud]] on the scale and mechanisms of AI persuasive power. It also speaks to work on partisan attitudes toward AI and elite-driven politicization such as [[Gottfried2026-ww]], and its concern with motivated reasoning in politically charged information environments links it to broader partisan-news and polarization research including [[Van_Erkel2026-mk]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/DiGiuseppe2026-pu.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-llms-can-political-bias-kill-persuasion/id1866587707?i=1000753721566)
