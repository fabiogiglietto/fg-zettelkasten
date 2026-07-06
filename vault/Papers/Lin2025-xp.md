---
title: "Persuading voters using human–artificial intelligence dialogues"
aliases: ["Persuading voters using human–artificial intelligence dialogues"]
authors: ["Hause Lin", "Gabriela Czarnek", "Benjamin Lewis", "Joshua P. White", "Adam J. Berinsky", "Thomas Costello", "Gordon Pennycook", "David G. Rand"]
year: 2025
doi: 10.1038/s41586-025-09771-9
bibtex_key: Lin2025-xp
topics: [generative-ai-media, elections-political-communication]
citation_count: 14
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

This paper presents four preregistered randomized experiments testing whether brief (3–5 round) dialogues with large language models can shift voter attitudes in high-stakes electoral contexts: the 2024 US presidential election, the 2024 Massachusetts psychedelics ballot measure, the 2025 Canadian federal election, and the 2025 Polish presidential election. Across all four settings, human–AI conversations produced meaningful shifts in candidate preference and voting intentions that substantially exceeded effect sizes typically reported for political advertising, with roughly a third of the effect persisting more than a month later. Mechanistically, the authors find that persuasion operates primarily through the "central route" — relevant facts and evidence — rather than personalization or sophisticated psychological manipulation. They also document a systematic asymmetry: LLMs advocating for right-leaning candidates produced more inaccurate claims than those advocating for left-leaning candidates, though inaccuracy did not predict greater persuasiveness.

## Key Contributions

- First large-scale, cross-national experimental evidence that human–AI dialogues shift attitudes in high-salience national elections, not only low-stakes issues.
- Direct experimental isolation of facts/evidence versus personalization as the active ingredients of AI persuasion, finding facts to be central and personalization largely dispensable.
- Documentation of a partisan asymmetry in factual accuracy of frontier LLM political arguments, robust across 12 models and three countries.
- Benchmarking of AI dialogue persuasion against canonical advertising and canvassing effect sizes, with evidence of >1-month persistence.
- A reusable multi-agent system (Vegapunk) and validated LLM-based pipelines for fact-checking and strategy coding of persuasive dialogue at scale.

## Methods

Four preregistered randomized survey experiments (total n ≈ 6,500) with pre-/post-dialogue measurement of candidate preference (0–100), voting likelihood, and categorical vote choice. Participants chatted 3–5 rounds with an AI prompted to advocate a specific candidate or position; factorial designs varied persuasion direction, conversation focus (policy vs. personality in the US), and strategy conditions (baseline, no-facts, non-personalized, non-specific in Canada/Poland). Multiple LLMs (GPT-4o, GPT-4.1, DeepSeek-V3, Llama-4-Maverick) served as persuaders. Analyses used robust linear regression with FDR correction and Bayes factors. Post hoc, two LLMs coded 27 persuasion strategies in transcripts, lasso regression identified predictive features, and 8,134 AI statements were fact-checked via Perplexity AI (validated against professional and lay raters).

## Findings

- US election: pro-Harris and pro-Trump AI conditions shifted preference by ~2.88 points on a 0–100 scale; policy conversations and out-party targets showed larger effects (e.g., pro-Harris AI moved Trump supporters ~3.90 points on policy).
- ~34% of the immediate US effect persisted at a ~41-day follow-up.
- Canadian baseline effect ~10 points; Polish baseline ~9.9 points — roughly three times the US effect.
- On the Massachusetts ballot measure, pro-psychedelics AI shifted strong opponents by ~14.85 points; the between-condition gap among non-extreme participants was ~22.7 points.
- Removing facts/evidence cut persuasion by >50% (Canada) and ~78% (Poland); removing personalization or strategy specificity had no significant effect.
- Most-used strategies were politeness, evidence/facts, optimism/value alignment, cognitive elaboration, and empathic listening; manipulative tactics were rare.
- Lasso analysis identified evidence/facts and personalization as strongest positive predictors of persuasion; pre-emptive counter-arguments were negative predictors; accuracy was not predictive.
- Median statement accuracy was 90/100, but pro-right-leaning AIs were consistently less accurate than pro-left-leaning AIs across all three countries and all 12 models tested.
- No significant differences in persuasiveness across the tested LLMs.

## Connections

This paper sits squarely within the emerging experimental literature on LLM persuasion and is a direct counterpart to [[Hackenburg2025-dj]], extending dialogue-based persuasion findings into multiple national elections and demonstrating cross-national robustness. It complements [[DeVerna2025-dl]] on AI-driven belief change and connects to [[Schroeder2026-im]] and [[Triedman2025-uy]] on the political behaviors and asymmetries of LLMs themselves — particularly relevant given the documented right-leaning accuracy gap. More broadly, it engages debates about generative AI and democratic information environments addressed by [[Tornberg2025-ir]] and [[Schiffrin_undated-gi]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lin2025-xp.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-persuading-voters-using-human-artificial/id1866587707?i=1000743818522)
