---
title: "Conversational Inoculation to enhance resistance to misinformation"
aliases: ["Conversational Inoculation to enhance resistance to misinformation"]
authors: ["Dániel Szabó", "Chi-Lan Yang", "Aku Visuri", "Jonas Oppenlaender", "Bharathi Sekar", "Koji Yatani", "Simo Hosio"]
year: 2026
doi: 10.1145/3772318.379095
bibtex_key: Szabo2026-rd
topics: [climate-and-misinformation-message-interventions]
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

This paper introduces *Conversational Inoculation*, a method for building cognitive resistance to misinformation through structured dialogue with an LLM-powered chatbot. The authors built MindFort, a web application implementing three inoculation modes—Reading, Writing, and a GPT-4o chatbot persona named "Forty"—and ran a within-subjects experiment with 61 participants across four health and environmental topics. The chatbot condition significantly outperformed a no-treatment control on resistance to a subsequent counterattitudinal attack, and outperformed both Reading and Writing once individual baseline susceptibility was controlled. Beyond the effectiveness result, the paper argues that what makes conversational inoculation work is not just argument content but interaction design: adaptability, trust-building, fostering independent thinking, and minimizing interactional friction.

## Key Contributions

- Operationalizes *Conversational Inoculation* as a distinct paradigm from passive reading or active writing-based inoculation.
- Releases MindFort, an open-source web prototype, plus a participant dataset for reproducibility.
- Provides empirical evidence that LLM-powered agents can deliver effective inoculation against health misinformation.
- Identifies four design mechanisms—adaptability, trust through partnership, independence-fostering, and friction reduction—shaping conversational inoculation outcomes.
- Sketches future directions including multi-bot architectures that separate threat and facilitation roles, and inoculation targeted at cognitive biases rather than topics.

## Methods

A within-subjects online experiment (N=61, recruited via Prolific) had each participant complete four lessons—one per topic, one per condition (Control, Reading, Writing, Chatbot)—in counterbalanced Latin Square order. Each lesson followed a 5-stage protocol: pre-treatment certainty rating (McGuire 15-point scale), treatment, mid-treatment certainty, exposure to a strong counterattitudinal attack, then post-attack certainty plus the Intrinsic Motivation Inventory. The chatbot used GPT-4o with a system prompt grounded in inoculation theory. Analyses combined Friedman/Wilcoxon tests, a linear mixed-effects model with participants and topics as random effects, deductive qualitative coding of conversations, and LIWC-22 linguistic analysis benchmarked against the LMSYS-Chat-1M corpus.

## Findings

- Chatbot produced significantly less post-attack certainty loss than Control (p=.001, r=-.33); pairwise differences with Reading and Writing were marginal (p≈.07–.08).
- Controlling for individual susceptibility, Chatbot significantly outperformed both Reading (p=.004) and Writing (p=.033).
- The Chatbot treatment slightly *increased* mid-lesson certainty, whereas Writing decreased it (r=-.30, p=.006).
- Effect sizes varied by topic: exercise/mental health and binge drinking yielded larger certainty drops than dental hygiene or nature protection.
- Intrinsic motivation did not differ significantly across conditions—conversational format sustained engagement without sacrificing it.
- LIWC showed Forty's conversations were less Analytic, more Authentic, and richer in Cognition, Conflict, Emotion, and Health language than reference chatbot dialogues, and substantially longer.
- For binge drinking, LIWC "Achieve" language strongly correlated with inoculation effectiveness (ρ=0.92, p=.008); no overall linguistic correlates survived Bonferroni correction.
- Qualitative mechanisms: chatbot adaptability, fostering independent research, trust through partnership rather than authority, and interactional friction as the dominant barrier.

## Connections

This work sits in the HCI corner of misinformation-resistance research, complementing population-scale studies of corrective messaging such as [[Voelkel2026-lc]] on political misperceptions and [[Allcott2025-jb]] on the limits of media-literacy interventions. It also resonates with experimental work on AI-mediated belief change like [[Gauthier2026-iq]], offering a constructive counterpart focused on prophylactic rather than corrective dialogue. The connection to [[Dubey2026-bl]] is thinner and not pursued here.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Szabo2026-rd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-chatbots-vs-fake-news-inoculating/id1866587707?i=1000748800904)
