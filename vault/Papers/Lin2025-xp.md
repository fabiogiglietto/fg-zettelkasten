---
title: "Persuading voters using human–artificial intelligence dialogues"
aliases: ["Persuading voters using human–artificial intelligence dialogues"]
authors: ["Hause Lin", "Gabriela Czarnek", "Benjamin Lewis", "Joshua P. White", "Adam J. Berinsky", "Thomas Costello", "Gordon Pennycook", "David G. Rand"]
year: 2025
doi: 10.1038/s41586-025-09771-9
bibtex_key: Lin2025-xp
topics: [generative-ai-and-synthetic-media, climate-and-misinformation-message-interventions]
citation_count: 22
open_access: false
source_url: https://doi.org/10.1038/s41586-025-09771-9
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lin2025-xp.mp3
pdf_available: true
discovery_date: 2025-12-15T00:00:00Z
---

# Persuading voters using human–artificial intelligence dialogues

> Lin, H., Czarnek, G., Lewis, B., White, J. P., Berinsky, A. J., Costello, T., Pennycook, G., & Rand, D. G. (2025). Persuading voters using human–artificial intelligence dialogues. *Nature*, 1–8. https://doi.org/10.1038/s41586-025-09771-9
>
> [View paper](https://doi.org/10.1038/s41586-025-09771-9)

## Summary

This paper reports four preregistered randomized survey experiments testing whether brief conversations with large language models can shift real voter attitudes across high-salience electoral contexts: the 2024 US presidential election, the 2025 Canadian federal election, the 2025 Polish presidential election, and a 2024 Massachusetts ballot measure on legalizing psychedelics. Across all four settings, short (3–5 round) human–AI dialogues produced meaningful, sometimes large, shifts in candidate preference, voting intention, and ballot-measure support — with effect sizes substantially exceeding those typically reported for traditional political advertising. Crucially, the authors trace this persuasion primarily to the central route (relevant facts and evidence) rather than sophisticated psychological manipulation or personalization, while documenting a systematic asymmetry: AI advocating for right-leaning candidates consistently made more inaccurate claims than AI advocating for left-leaning candidates. The work positions itself between alarmist and dismissive framings of generative AI's electoral threat, offering direct causal evidence.

## Key Contributions

- First large-scale, cross-national experimental evidence that human–AI dialogues substantively shift attitudes in high-salience national elections, not just low-stakes issues.
- Experimentally isolates the causal role of facts/evidence versus personalization by directly manipulating the AI's persuasion strategy.
- Documents a systematic partisan asymmetry in the factual accuracy of frontier-LLM political arguments (right-leaning less accurate), relevant to AI safety and moderation.
- Benchmarks AI dialogue persuasion against canonical advertising and canvassing effect sizes.
- Demonstrates persistence: ~one-third of the immediate effect survives more than a month.
- Releases a validated LLM-based fact-checking and strategy-coding pipeline (Vegapunk multi-agent system).

## Methods

- Four preregistered randomized experiments: US presidential (n=2,306; ~41-day follow-up n=1,936), Massachusetts psychedelics measure (n=501), Canadian federal (n=1,530), Polish presidential (n=2,118).
- Participants completed pre-treatment outcome measures, engaged in a 3–5 round chat with an AI prompted to advocate for an assigned candidate/position, then repeated the measures.
- Factorial randomization across persuasion direction, conversation focus (policy vs. personality in the US), and strategy conditions (baseline, no-facts, non-personalized, non-specific) in Canada/Poland.
- Multiple persuader LLMs (GPT-4o, GPT-4.1, DeepSeek-V3-0324, Llama-4-Maverick).
- Analysis via robust-SE linear regression, Storey–Tibshirani FDR correction, Bayes factors; post hoc LLM coding of 27 persuasion strategies with lasso feature selection; fact-checking of 8,134 statements using Perplexity, validated against professional and lay raters.

## Findings

- US election: significant shifts in candidate preference (main effect b=2.88 on 0–100), larger for policy than personality and larger for out-party participants (pro-Harris AI moved Trump supporters 3.90 points on policy).
- ~34% of the immediate preference change persisted at ~41-day follow-up.
- Massachusetts measure: pro-psychedelics AI raised support among strong opponents ~14.85 points; among non-extreme participants the between-condition gap reached ~22.7 points.
- Canadian and Polish baseline effects (~10 and ~9.9 points) were about three times larger than the US effect.
- Removing facts/evidence cut persuasion by more than half in Canada and ~78% in Poland; removing personalization or specific strategy instructions had no significant effect in Poland.
- AI relied most on politeness, evidence/facts, optimism/value alignment, cognitive elaboration, and empathic listening; manipulative tactics were rare.
- Lasso identified personalization and evidence/facts as strongest positive predictors; pre-emptive counter-arguments negatively associated; claim accuracy was not predictive of persuasiveness.
- Median statement accuracy was 90/100, but pro-right-leaning AIs were significantly less accurate across all three countries and 12 tested models.
- No significant persuasiveness differences across the LLMs tested.

## Connections

This paper extends the emerging line of work on AI dialogue-based belief change into electoral persuasion, closely relating to experimental studies of LLM persuasion and durable attitude change such as [[Hackenburg2025-dj]]. Its documentation of partisan asymmetry in LLM factual accuracy connects to broader concerns about generative AI in disinformation and elections raised across this topic cluster, though most neighbouring papers address platform-level or observational dynamics rather than the controlled experimental persuasion mechanisms studied here.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lin2025-xp.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-persuading-voters-using-human-artificial/id1866587707?i=1000743818522)
