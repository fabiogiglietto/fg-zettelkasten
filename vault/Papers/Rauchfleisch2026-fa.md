---
title: "Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion"
aliases: ["Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion"]
authors: ["Adrian Rauchfleisch", "Andreas Jungherr"]
year: 2026
doi: 
bibtex_key: Rauchfleisch2026-fa
topics: [llm-augmented-research-methods, public-perceptions-and-labor-impacts-of-ai]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2608.11794v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Rauchfleisch2026-fa.mp3
pdf_available: true
discovery_date: 2026-08-15T07:48:43.299793Z
---

# Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion

> Rauchfleisch, A., & Jungherr, A. (2026). Toward meaningful transparency for AI chatbots: Disclosing persuasive intent reduces persuasion. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2608.11794v1)

## Summary

This preregistered experiment tests a deceptively simple regulatory question: does telling people they are talking to an AI actually protect them from being persuaded by it? Using 1,500 UK adults conversing with an identical persuasive chatbot about one of 60 policy issues, the authors compared no disclosure, an EU AI Act-style AI-identity label, and a label plus disclosure of the chatbot's *persuasive intent and instructions*. The headline result is that identity labels alone did nothing to blunt persuasion, whereas disclosing intent cut the attitude shift roughly in half. The paper argues that meaningful transparency must reveal *what an AI system is trying to do*, not merely *what it is* — a distinction that indicts the dominant source-labeling logic of EU AI Act Article 50 as an empirically weak template for governing persuasive AI.

## Key Contributions

- Direct experimental evidence that AI-identity disclosure (EU AI Act Article 50) does **not** reduce persuasion in live chatbot conversations.
- Introduces and tests **intent disclosure** as a more effective transparency instrument, operationalizing the "meaningful transparency" logic of EU political-advertising regulation (Regulation 2024/900).
- Offers a conceptual distinction between **formal transparency** (source labeling) and **meaningful transparency** (intent/instruction disclosure) for AI governance.
- Documents a downstream **reputational tradeoff**: intent disclosure protects audiences but imposes reputational and acceptability costs on the actor deploying the AI.
- Preregistered, robustness-checked estimates that hold across all 60 issues and both persuadable and less-persuadable issue halves.

## Methods

Three-arm preregistered online experiment (N=1,500, UK Prolific sample with sex/age/party quotas). Participants reported an initial attitude on a randomly assigned policy stance, held a 2–6 turn conversation with an identical persuasive chatbot (gpt-5.6-terra) using the most effective persuasion prompt, then re-reported attitude plus additional outcomes. Conditions: control (no disclosure), T1 (EU-style AI-generated-content label with pre-chat card and persistent banner), and T2 (label plus disclosure of the chatbot's persuasive intent and verbatim instructions). The chatbot and server were identical across arms and blind to condition, so the bot could not adapt. Analysis used linear mixed models with random intercepts for policy issue, Holm correction, and preregistered TOST equivalence tests. Supplementary fact-checking assessed the accuracy of chatbot claims.

## Findings

- The chatbot shifted attitudes by **12.6 points (control)** and **13.1 points (T1)**; the AI-identity label was statistically **equivalent** to no disclosure (pTOST=.002).
- Intent disclosure (T2) cut persuasion to **6.3 points — roughly half** — versus both control and T1; the protective effect was negative for all 60 issues.
- **Persuasion knowledge** rose most strongly under intent disclosure (d=0.49), consistent with the persuasion-knowledge model.
- T2 also raised perceived manipulation and counterarguing and made the chatbot rated ~5 points colder, but did **not** increase anger.
- T2 participants judged the campaign's methods less acceptable and supported stronger sponsor penalties; the identity label produced no such penalty.
- The null label effect was **not** inattention: 97.8% recalled the label, 98–99% across all arms recognized the AI, and 29.5% of control participants even *falsely* recalled seeing a label.
- Reduced persuasion was not due to early exit — T2 participants wrote slightly more messages and spent more time.
- Fact-checking found ~2.01 claims per message with **95.7% accurate**, indicating persuasion rested on accurate information rather than misinformation.

## Connections

This paper builds directly on recent experimental work quantifying the persuasive power of large language models, from which it borrows its policy stances and fact-checking pipeline; it extends that agenda from measuring persuasion to intervening on it — see [[Hackenburg2025-dj]] and [[Hackenburg2026-ud]]. Its focus on the (in)effectiveness of transparency labeling connects it to broader debates about AI disclosure, provenance, and audience perception in the same topic clusters, such as work on synthetic-media detection and labeling in [[Hameleers2026-mc]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Rauchfleisch2026-fa.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
