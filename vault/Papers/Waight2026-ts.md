---
title: "State media control influences large language models"
aliases: ["State media control influences large language models"]
authors: ["Hannah Waight", "Eddie Yang", "Yin Yuan", "Solomon Messing", "Margaret E. Roberts", "Brandon M. Stewart", "Joshua A. Tucker"]
year: 2026
doi: 10.1038/s41586-026-10506-7
bibtex_key: Waight2026-ts
topics: [generative-ai-media, information-disorder]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1038/s41586-026-10506-7
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Waight2026-ts.mp3
pdf_available: true
discovery_date: 2026-05-14T05:47:06.196009Z
---

# State media control influences large language models

> Waight, H., Yang, E., Yuan, Y., Messing, S., Roberts, M. E., Stewart, B. M., & Tucker, J. A. (2026). State media control influences large language models. *Nature*, 1–9. https://doi.org/10.1038/s41586-026-10506-7
>
> [View paper](https://doi.org/10.1038/s41586-026-10506-7)

## Summary

This paper provides systematic empirical evidence that state control over media environments shapes the outputs of commercial large language models through a previously underexamined pathway: training data. Using China as a primary case and a 37-country cross-national audit as a generalization test, the authors trace a causal chain from state-coordinated media production, to its inclusion in open-source web corpora, to memorization by commercial LLMs, to measurable pro-regime tilts in model outputs—especially when prompted in languages exclusive to lower-press-freedom countries. The core argument is that LLMs can "launder" state-manipulated content into seemingly neutral responses, constituting an indirect form of institutional influence distinct from direct regulation of model design.

## Key Contributions

- First systematic, multi-study empirical demonstration that state media control influences commercial LLM outputs via training data rather than direct regulatory pressure.
- A triangulation design combining corpus overlap analysis, memorization audits, controlled pretraining experiments, cross-language prompt audits, and a 37-country generalization audit.
- Bridges political communication research on authoritarian media systems with NLP work on multilingual training, memorization, and bias.
- Identifies a generalizable mechanism—language-exclusive media environments under institutional control—that extends beyond state actors and beyond China.
- Publicly releases replication materials and an interactive site updating results on newer models.

## Methods

The authors run six interlocking studies. Study 1 matches ~189M Chinese CulturaX documents against scripted state media using five-word gram cosine similarity. Study 2 audits memorization in Claude Sonnet/Opus, GPT-3.5, GPT-4, and GPT-4o by prompting with 10-word prefixes of phrases identified (via lasso regression) as distinctively state-coordinated. Study 3 performs LoRA continued pretraining on Llama 2 13b (replicated on Llama 3.1) with scripted, non-scripted state, or random CulturaX corpora, then measures favorability with GPT-4o-as-judge across languages. Studies 4–5 are pre-registered English-vs-Chinese audits using both researcher-designed prompts (human-rated) and real-user prompts from WildChat, Baidu Zhidao, and Zhihu. Study 6 generalizes via 6,051 prompts across 37 language-exclusive countries, correlating outputs with World Press Freedom Index scores.

## Findings

- ~1.64% of Chinese CulturaX documents substantially overlap with state-coordinated media; this rises to 3.28–23.98% for politically salient content (e.g., Xi Jinping, CCP, Party Congress).
- Commercial LLMs memorize state-coordinated 20-word phrases at 3–10% rates, equal to or exceeding memorization of common Chinese phrases.
- Just 6,400 additional pretraining examples of scripted news shift Llama 2 toward more pro-CCP outputs ~80% of the time; scripted state news has stronger effects than non-scripted state media or random web text.
- Pretraining effects spill over most to languages sharing tokens with simplified Chinese (traditional Chinese, Japanese, Korean).
- GPT-3.5 responses to Chinese prompts were rated more favorable to China 75.3% of the time; the gap grew with model scale (88.2% for Claude Opus).
- Real-user prompts from WildChat, Baidu, and Zhihu reproduce the cross-language favorability gap.
- Across 37 countries, lower press freedom predicts greater target-language favorability relative to English; high-press-freedom countries show flat or reversed patterns.

## Connections

This paper sits alongside other audits of LLM political behavior and bias under the generative-AI register, including work on multilingual and ideological skew such as [[Tornberg2025-ir]] and [[Le-Mens2025-qz]], and broader assessments of LLM persuasive capacity like [[Hackenburg2025-dj]]. It also extends the author's earlier work on Chinese information control ([[Waight2025-al]]) into the AI domain, and complements concerns about AI-mediated information disorder raised in [[DeVerna2025-dl]] and [[Triedman2025-uy]]. The geopolitical framing of training-data influence makes it a natural counterpart to studies of state-aligned information operations and propaganda diffusion in the wider topic cluster.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Waight2026-ts.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ais/id1866587707?i=1000767719309)
