---
title: "State media control influences large language models"
aliases: ["State media control influences large language models"]
authors: ["Hannah Waight", "Eddie Yang", "Yin Yuan", "Solomon Messing", "Margaret E. Roberts", "Brandon M. Stewart", "Joshua A. Tucker"]
year: 2026
doi: 10.1038/s41586-026-10506-7
bibtex_key: Waight2026-ts
topics: [generative-ai-disinformation, llm-driven-content-analysis]
citation_count: 1
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

This paper asks whether government control of media influences the outputs of large language models through the training data those models ingest. Using six interlocking studies—five centred on China and one cross-national audit spanning 37 language-exclusive countries—the authors demonstrate that state-coordinated media content appears in widely-used training corpora, is memorized by commercial LLMs, and causes models to produce more pro-regime responses when queried in the languages of countries with lower media freedom. The central argument is that LLMs can effectively "launder" state-manipulated content into seemingly objective answers, revealing an indirect pathway of institutional influence distinct from direct model regulation. This reframes debates about AI bias in geopolitical terms: political power embedded in media environments, not merely design choices or cultural variation, shapes generative AI.

## Key Contributions

- First systematic empirical evidence that state media control shapes commercial LLM outputs via training data rather than direct regulation.
- A multi-study triangulation design combining open-data analysis, memorization audits, controlled pretraining experiments, cross-language audits, and a cross-national audit.
- Bridges social-science scholarship on media systems and propaganda with computer-science work on multilingual training, memorization, and model bias.
- Identifies a generalizable mechanism—language exclusivity combined with institutional content production—that extends beyond China and beyond state actors (illustrated with a vaccine-schedule mini-case).
- A public project website replicating key studies on newer models with interactive data access.

## Methods

The six studies escalate from correlational observation to causal manipulation. Study 1 uses five-word-gram cosine similarity to match ~189M Chinese CulturaX documents against Chinese state-scripted news and Xuexi Qiangguo articles. Study 2 audits memorization in commercial models (Claude, GPT-3.5/4/4o) by using lasso regression to isolate distinctive 20-word state-media phrases, then prompting with the first 10 words and measuring edit distance. Study 3 runs continued pretraining on Llama 2 13b (replicated on Llama 3.1) via LoRA, comparing scripted state news, topic/date-matched non-scripted state news, and random CulturaX, followed by English instruction tuning and GPT-4o-judged favorability. Studies 4 and 5 audit English-vs-Chinese prompt favorability using human raters and LLM judges, with Study 5 drawing on real user prompts (WildChat, Baidu Zhidao, Zhihu). Study 6 scales to 6,051 prompts across 37 language-exclusive countries, correlating language-vs-English favorability gaps with World Press Freedom Index scores.

## Findings

- ~1.64% of Chinese CulturaX documents substantially overlap with state-coordinated media, rising to 3.28–23.98% for politically salient keyword documents.
- State-coordinated 20-word phrases are memorized by major commercial LLMs at 3–10% rates, equal to or above common phrases.
- After only 6,400 scripted-news examples, Llama 2 produced more pro-government responses ~80% of the time; scripted news outperformed non-scripted state news and random content.
- Pretraining effects spilled over most strongly to traditional Chinese, Japanese, and Korean—languages sharing tokens with simplified Chinese.
- Human raters found GPT-3.5's Chinese-prompted responses more favorable to China 75.3% of the time; larger models (Claude Opus 88.2%) showed stronger effects.
- Real-user prompts replicated the cross-language favorability gap.
- Across 37 countries, lower media freedom correlated with greater favorability of target-language responses relative to English.

## Connections

This paper directly extends the authors' related work on Chinese state media and LLMs in [[Waight2025-al]] and [[Yang2026-tq]]. Its concern with how generative AI can produce and disseminate politically biased or persuasive content connects it to the disinformation-focused strand represented by [[Hackenburg2025-dj]], [[DeVerna2025-dl]], and [[Costello2024-bg]], while its cross-national, multilingual audit methodology bears on measurement questions in [[Gilardi2026-hw]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Waight2026-ts.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-state-media-shapes-what-ai-tells-you/id1866587707?i=1000767719309)
