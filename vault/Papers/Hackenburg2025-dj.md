---
title: "The levers of political persuasion with conversational artificial intelligence"
aliases: ["The levers of political persuasion with conversational artificial intelligence"]
authors: ["Kobi Hackenburg", "Ben M. Tappin", "Luke Hewitt", "Ed Saunders", "Sid Black", "Hause Lin", "Catherine Fist", "Helen Margetts", "David G. Rand", "Christopher Summerfield"]
year: 2025
doi: 10.1126/science.aea3884
bibtex_key: Hackenburg2025-dj
topics: [generative-ai-disinformation, llms-in-content-analysis]
citation_count: 24
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

This paper reports the largest systematic empirical investigation to date of what makes conversational AI persuasive in the political domain. Across three preregistered experiments involving nearly 77,000 responses from 42,357 UK participants, 19 LLMs, and 707 political issues, the authors dismantle the persuasion process into its component "levers": model scale, prompting strategy, personalization, and post-training. Their central finding is that post-training and prompting matter far more than raw model size or personalization, and that all of these effects operate through a single mechanism — **information density**, the volume of fact-checkable claims packed into a conversation. Crucially, the same techniques that maximize persuasion also degrade factual accuracy, exposing a systematic persuasion–accuracy trade-off with direct implications for AI safety and misinformation policy.

## Key Contributions

- Maps the technical levers of conversational AI persuasion across model families and four orders of magnitude of pretraining compute.
- Identifies **information density** as a unifying mechanism linking scale, post-training, and prompting effects.
- Documents and quantifies a previously unmeasured **persuasion–accuracy trade-off**.
- Shows that cheap, subfrontier open-source models can be post-trained into agents matching or exceeding frontier models like GPT-4o — broadening the threat model beyond well-resourced labs.
- Reframes microtargeting fears by showing personalization yields only marginal gains.
- Contributes empirical evidence to the motivated-reasoning debate: information-based persuasion beats identity-based psychological strategies when delivered by AI.
- Releases a large dataset and analysis pipeline.

## Methods

Three large-scale preregistered survey experiments had UK adults engage in multi-turn (2–10 turn) conversations with LLMs about politically balanced issues, with pre/post attitude measured on a 0–100 scale against a no-conversation control. The authors deployed 19 open- and closed-source models (GPT-3.5 through GPT-4.5, Grok-3-beta, Qwen and Llama families), and systematically manipulated model scale, eight prompting strategies (information, moral reframing, storytelling, deep canvassing, etc.), three personalization methods, and three post-training methods (SFT, reward modeling, SFT+RM). Persuasion post-training used a curated SFT set of 9,000 dialogues plus a reward model trained on 56,283 conversations for best-of-k reranking. They fact-checked 466,769 generated claims via GPT-4o Search Preview, validated against professional fact-checkers (r ≈ 0.84–0.87), and used cross-fit ML to estimate the joint effect of stacking all persuasion-maximizing levers.

## Findings

- Each order-of-magnitude increase in compute yielded only +1.59–1.83 pp of persuasion (holding post-training constant).
- Reward-model post-training added +2.32 pp on open-source and +0.63 pp on frontier models; SFT alone had no significant effect.
- The "information" prompt was the most persuasive strategy (+27% over baseline); moral reframing and deep canvassing underperformed a basic prompt.
- Information density correlated strongly with persuasion (r ≈ 0.77), explaining ~44% of variance overall and ~75% among developer post-trained models.
- Personalization had a small effect (+0.43 pp, never exceeding +1 pp).
- Conversation beat static messages by 41–52%, with 36–42% of effects persisting at one month.
- Information-prompted GPT-4o accuracy fell from 78% to 62%; a maximally optimized configuration reached a 15.9 pp average effect (26.1 pp among disagreers) but with 30% of claims rated inaccurate.

## Connections

This work directly complements [[Costello2024-bg]], which demonstrated conversational AI's power to durably reduce conspiracy beliefs — both find that fact-dense, multi-turn dialogue is a potent persuasive tool, though the present paper sharpens this by exposing the accuracy costs. Its quantification of AI persuasion mechanisms also situates it against broader concerns about generative-AI-driven influence explored in [[DeVerna2025-dl]] and the disinformation-vulnerability work in [[Triedman2025-uy]]. The finding that microtargeting yields only marginal gains offers an empirical counterweight to speculative manipulation narratives.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Hackenburg2025-dj.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-persuasion-facts-lies-and/id1866587707?i=1000754805732)
