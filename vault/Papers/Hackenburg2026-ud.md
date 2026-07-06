---
title: "AI systems out-persuade expert humans"
aliases: ["AI systems out-persuade expert humans"]
authors: ["Kobi Hackenburg", "Caroline Wagner", "Luke Hewitt", "Ben M. Tappin", "Ed Saunders", "Hannah Rose Kirk", "Helen Margetts", "Christopher Summerfield"]
year: 2026
doi: 
bibtex_key: Hackenburg2026-ud
topics: [generative-ai-media]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.16475v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Hackenburg2026-ud.mp3
pdf_available: true
discovery_date: 2026-06-27T09:20:30.108921Z
---

# AI systems out-persuade expert humans

> Hackenburg, K., Wagner, C., Hewitt, L., Tappin, B. M., Saunders, E., Kirk, H. R., Margetts, H., & Summerfield, C. (2026). AI systems out-persuade expert humans. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2606.16475v1)

## Summary

This paper reports four large preregistered online experiments (n=18,978 conversations, 6,923 participants) pitting frontier conversational AI systems against progressively more capable human persuaders — random laypeople, tournament-selected laypeople, world-class competitive debaters (including coached ones), and professional charity canvassers. Across all comparisons, AI systems were reliably more persuasive than humans on UK policy attitudes and were nearly three times more effective than professional canvassers at eliciting real-money donations to Save the Children. A constraint experiment and an automated fact-checking pipeline implicate information throughput — the sheer density of fact-checkable claims per conversation — as the primary mechanism, rather than rapport or perceived humanness. The authors argue that current frontier models already exceed expert human persuasive capability, with implications for elections, fundraising, disinformation, and AI oversight.

## Key Contributions

- First large-scale, well-powered head-to-head evidence that frontier conversational AI out-persuades expert humans, including world and continental debate champions and professional canvassers.
- Demonstration that ~8 hours of targeted coaching — including practice against the specific AI opponent — fails to close the human–AI gap.
- Identification of information throughput / fact density as the likely mechanism, supported by a throughput-constraint condition that eliminates AI's advantage.
- Extension from attitude change to a consequential behavioral outcome (real-money charitable giving) in partnership with a professional UK fundraising firm.
- Methodological innovations: a four-round preregistered persuasion-selection tournament for identifying elite lay persuaders, and a lagged adaptive prompting design that matches AI message length and latency to human baselines.

## Methods

Four preregistered, single-blind, between-subjects experiments were run on a custom real-time matchmaking platform supporting text conversations of 2–10 turns. Human persuader classes spanned random Prolific workers, tournament-selected laypeople (top ~10% of 1,154 competitors), elite debaters (n=56, including 15 world/continental champions), coached debaters, and 19 professional canvassers from AppcoUK. AI persuaders included Claude Opus, ChatGPT-4o/GPT-5, Grok 4, and Gemini 2.5 Pro, prompted with an "information-first" strategy (Studies 1–3) or an "impact-efficacy" donation strategy (Study 4). Study 2 added a Constrained AI condition matching elite-debater message length (~51 words) and latency (~92s). Outcomes were 0–100 pre/post attitude scales across 10 UK policy issues and the share of a £1 bonus donated to Save the Children. Analyses used linear mixed-effects models with crossed random intercepts for persuader and persuadee, and an automated two-stage fact-checking pipeline quantified claim density per message. Humans received substantial cash incentives, including tiered prize pools up to £1,000.

## Findings

- AI beat Random Laypeople by 8.2 pp, Selected Laypeople by 5.6 pp, Elite Debaters by 4.6 pp, and Professional Canvassers by 5.9 pp on attitude change (all p<.001).
- AI-focused coaching of elite debaters yielded only a non-significant +1.0 pp gain; a +4.1 pp AI advantage persisted.
- Constraining AI to human message length and latency collapsed its advantage over coached debaters to 0.0 pp.
- No individual human (of 275) reliably matched the pooled AI estimate; the AI advantage held across all 10 issues and 46 of 49 prespecified persuadee subgroups.
- Fact-checkable claims per conversation predicted persuasive impact with R²=0.89, and controlling for log-fact density drove the AI-vs-human coefficient near zero.
- Constraining AI lowered perceived argument strength and learning (~−11.8 pp) while *increasing* perceived human-likeness (+7.5 pp) — undermining a "rapport/humanness" account.
- In Study 4, AI elicited +17.2 pp donation vs. +6.4 pp for canvassers (~3x), via both more donors and larger gifts.
- AI outscored canvassers on all 7 preregistered donation mechanisms, including six it was never explicitly prompted to use.
- AI's advantage was largest for persuadees with weaker priors and less issue knowledge.

## Connections

This paper sits at the center of the emerging evidence base on generative-AI persuasion, directly extending [[Costello2024-bg]]'s conspiracy-belief intervention from a single domain to broad policy attitudes and behavior against expert human comparators, and complementing [[Hackenburg2025-dj]] on the scaling and limits of AI political persuasion. The fact-density mechanism connects to concerns about AI-generated political messaging and disinformation explored in work such as [[Hameleers2026-mc]] and [[Schroeder2026-im]], while the real-money donation result speaks to behavioral, not just attitudinal, downstream effects of LLM-mediated communication.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Hackenburg2026-ud.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
