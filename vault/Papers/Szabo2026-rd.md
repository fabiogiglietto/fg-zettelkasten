---
title: "Conversational Inoculation to enhance resistance to misinformation"
aliases: ["Conversational Inoculation to enhance resistance to misinformation"]
authors: ["Dániel Szabó", "Chi-Lan Yang", "Aku Visuri", "Jonas Oppenlaender", "Bharathi Sekar", "Koji Yatani", "Simo Hosio"]
year: 2026
doi: 10.1145/3772318.379095
bibtex_key: Szabo2026-rd
topics: [climate-and-misinformation-message-interventions, computational-text-methods-llms]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1145/3772318.379095
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Szabo2026-rd.mp3
pdf_available: true
discovery_date: 2026-02-08T18:59:43.466543Z
---

# Conversational Inoculation to enhance resistance to misinformation

> Szabó, D., Yang, C., Visuri, A., Oppenlaender, J., Sekar, B., Yatani, K., & Hosio, S. (2026). Conversational Inoculation to enhance resistance to misinformation. *arXiv [cs.HC]*. https://doi.org/10.1145/3772318.379095
>
> [View paper](https://doi.org/10.1145/3772318.379095)

## Summary

This paper introduces **Conversational Inoculation**, a method for building resistance to misinformation through structured dialogue with an LLM-powered chatbot. The authors built **MindFort**, a web application implementing three conditions — Reading (supportive defense), Writing (traditional refutation), and Chatbot (a conversational agent named "Forty" grounded in inoculation theory) — and evaluated it in a within-subjects study of 65 participants across four health/environment topics. The central argument is that conversational, adaptive dialogue can inoculate people against misinformation at least as effectively as, and in some measures better than, traditional passive or written inoculation, while sustaining comparable engagement. The work sits at the intersection of Cognitive Inoculation Theory and HCI research on conversational agents, positioning dialogue-based adaptivity as a response to the rigidity of conventional inoculation.

## Key Contributions

- Introduces and operationalizes **Conversational Inoculation** as a paradigm distinct from passive/written inoculation.
- Provides **MindFort**, an open-source web prototype and participant dataset for reproducibility.
- Empirically validates that LLM-powered agents can deliver effective inoculation against health-related misinformation.
- Identifies four design factors shaping outcomes: adaptability, trust-building, fostering independent thinking, and friction reduction.
- Proposes future directions including multi-bot architectures (separating threat and facilitation roles) and inoculation targeting cognitive biases rather than topics.

## Methods

- Built MindFort in Flask using GPT-4o (temperature 1); the "Forty" persona was engineered via a structured system prompt grounded in inoculation theory.
- Within-subjects online experiment, 65 participants (61 after exclusions) via Prolific; sample size justified by G*Power for Wilcoxon signed-rank test.
- Each participant completed four lessons (one per topic) in counterbalanced Latin Square order across Control, Reading, Writing, and Chatbot conditions.
- Each lesson used a 5-stage protocol: pre-treatment certainty (15-point McGuire scale), treatment, mid-lesson certainty, strong counterattitudinal attack, post-attack certainty plus Intrinsic Motivation Inventory.
- Analysis via Friedman tests, Bonferroni-corrected Wilcoxon signed-rank tests, and a linear mixed-effects model (lme4); qualitative deductive content analysis and LIWC-22 linguistic analysis benchmarked against LMSYS-Chat-1M.

## Findings

- Chatbot produced significantly less post-attack certainty loss than Control (p=.001, r=−.33); pairwise differences with Reading (p=.07) and Writing (p=.08) were not significant.
- When controlling for individual susceptibility (Inoculation Effectiveness measure), Chatbot significantly outperformed both Reading (p=.004) and Writing (p=.033).
- The Chatbot treatment slightly increased mid-lesson certainty while Writing decreased it (r=−.30, p=.006).
- Inoculation effects varied by topic: exercise/mental health and binge drinking showed larger certainty drops than dental hygiene and protecting nature.
- IMI scores largely did not differ across conditions; post-debriefing scores rose significantly on Interest/Enjoyment, Perceived Competence, and Value/Usefulness.
- LIWC analysis showed chatbot conversations were less Analytic, more Authentic, and higher in Cognition, Conflict, Emotion, and Health words than reference dialogues, and significantly longer.
- Qualitative themes: adaptability, fostering independent thinking, trust through partnership rather than authority, and interactional friction as the key barrier.

## Connections

This work extends the psychological inoculation tradition into interactive, LLM-mediated formats and connects to broader debates on whether conversational AI can shift beliefs, as explored in [[Costello2024-bg]] (dialogue with LLMs reducing conspiracy beliefs) and [[van-der-Linden2026-jt]] on inoculation-based resistance. It also relates to work assessing LLMs as persuasion agents such as [[Hackenburg2025-dj]], and to studies on LLM-generated counter-misinformation content like [[DeVerna2025-dl]] and [[Spampatti2026-kx]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Szabo2026-rd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-chatbots-vs-fake-news-inoculating/id1866587707?i=1000748800904)
