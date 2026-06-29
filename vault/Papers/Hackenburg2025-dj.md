---
title: "The levers of political persuasion with conversational artificial intelligence"
aliases: ["The levers of political persuasion with conversational artificial intelligence"]
authors: ["Kobi Hackenburg", "Ben M. Tappin", "Luke Hewitt", "Ed Saunders", "Sid Black", "Hause Lin", "Catherine Fist", "Helen Margetts", "David G. Rand", "Christopher Summerfield"]
year: 2025
doi: 10.1126/science.aea3884
bibtex_key: Hackenburg2025-dj
topics: [generative-ai-and-media]
citation_count: 19
open_access: false
source_url: https://doi.org/10.1126/science.aea3884
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Hackenburg2025-dj.mp3
pdf_available: true
discovery_date: 2026-03-11T09:32:00.321924Z
---

# The levers of political persuasion with conversational artificial intelligence

> Hackenburg, K., Tappin, B. M., Hewitt, L., Saunders, E., Black, S., Lin, H., Fist, C., Margetts, H., Rand, D. G., & Summerfield, C. (2025). The levers of political persuasion with conversational artificial intelligence. *Science*, *390*, eaea3884. https://doi.org/10.1126/science.aea3884
>
> [View paper](https://doi.org/10.1126/science.aea3884)

## Summary

This paper presents the largest systematic empirical investigation of what makes conversational AI persuasive in political contexts, using three preregistered experiments with 42,357 UK participants, 19 LLMs spanning four orders of magnitude in compute, and 707 political issues. The authors find that *post-training* (especially reward modeling) and *prompting strategies* are far more powerful persuasion levers than model scale or personalization, and they identify **information density**—the number of fact-checkable claims per conversation—as the unifying mechanism. Crucially, the same levers that boost persuasion systematically *degrade* factual accuracy, exposing a persuasion–accuracy trade-off with direct implications for AI safety and political communication.

## Key Contributions

- Largest-scale mapping to date of which technical levers (scale, prompting, personalization, post-training) drive AI persuasion.
- Identification of **information density** as a unifying causal mechanism (~44–75% of variance explained).
- Quantification of a **persuasion–accuracy trade-off**: optimized persuasion configurations achieve 15.9 pp shifts but with ~30% inaccurate claims.
- Demonstration that cheap, subfrontier open-source models can be post-trained into highly persuasive agents, broadening the threat model.
- Empirical pushback against microtargeting alarmism: personalization effects are real but ≤1 pp.
- Evidence that information-based persuasion outperforms identity/affect-based strategies (moral reframing, deep canvassing) when delivered by AI.
- Public release of dataset and pipeline covering 466,769 fact-checked LLM claims.

## Methods

Three large-scale preregistered survey experiments measured pre/post attitude change (0–100 scale) after multi-turn (2–10) conversations with LLMs about politically balanced issues, benchmarked against no-conversation controls. The authors manipulated model scale (19 LLMs including GPT-3.5/4o/4.5, Grok-3-beta, Qwen, Llama), eight prompting strategies, three personalization methods, and three post-training regimes (SFT, reward modeling, SFT+RM)—the latter using 9,000 curated successful dialogues and a reward model trained on 56,283 conversations for best-of-k reranking. Claim-level accuracy was assessed via GPT-4o Search Preview, validated against professional fact-checkers (r = 0.84–0.87). Joint effects were estimated using cross-fit machine learning.

## Findings

- Each order-of-magnitude compute increase yielded only +1.83 pp persuasion among chat-tuned models.
- Reward-model post-training added +2.32 pp on open-source models (+0.63 pp on frontier); SFT alone was null.
- The simple "information" prompt was the most persuasive strategy (+27% over basic); moral reframing and deep canvassing underperformed.
- Information density correlated r ≈ 0.77 with persuasion.
- Personalization yielded only +0.43 pp on average; never above +1 pp.
- Conversations were 41–52% more persuasive than 200-word static messages; 36–42% of effects persisted at one-month follow-up.
- Information-prompting dropped GPT-4o accuracy from 78% to 62%; GPT-4.5 was no more accurate than Llama3.1-8B.
- Fully optimized configuration: 15.9 pp average effect (26.1 pp among initial disagreers), 30% inaccurate claims.

## Connections

This work directly extends and complicates concerns raised in [[DeVerna2025-dl]] about LLM-driven misinformation and in [[Triedman2025-uy]] on adversarial/persuasive AI behaviors, by isolating *which* technical levers actually drive persuasion and showing they trade off against accuracy. It also speaks to [[Tan2024-vl]] and [[Lin2025-xp]] on LLM-mediated political communication, and provides an empirical counterweight to microtargeting-focused narratives that recur across the broader generative-AI-and-politics literature (e.g., [[Schiffrin_undated-gi]], [[Brown2025-jk]]). Other listed papers under this topic appear less directly connected to its mechanism-focused persuasion agenda.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Hackenburg2025-dj.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-persuasion-facts-lies-and/id1866587707?i=1000754805732)
