---
title: "LLMs can infer political alignment from online conversations"
aliases: ["LLMs can infer political alignment from online conversations"]
authors: ["Byunghwee Lee", "Sangyeon Kim", "Filippo Menczer", "Yong-Yeol Ahn", "Haewoon Kwak", "Jisun An"]
year: 2026
doi: 
bibtex_key: Lee2026-je
topics: [llms-computational-content-analysis, political-polarization-partisan-news]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2603.11253v2
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lee2026-je.mp3
pdf_available: true
discovery_date: 2026-03-14T13:25:43.225280Z
---

# LLMs can infer political alignment from online conversations

> Lee, B., Kim, S., Menczer, F., Ahn, Y., Kwak, H., & An, J. (2026). LLMs can infer political alignment from online conversations. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2603.11253v2)

## Summary

This paper asks whether off-the-shelf LLMs can infer users' political alignment from online text — including discourse that is not overtly political. Using self-identified partisans on Debate.org and partisan-subreddit-active users on Reddit, the authors evaluate GPT-4o and Llama-3.1-8B in zero-shot settings against supervised ML baselines. They show that LLMs reliably classify partisanship from individual posts and especially from aggregated user histories, exploiting both explicitly political vocabulary and culturally politicized terms ("Tesla," "Taylor Swift," "boomer"). The work frames this dual-use capability as both a methodological tool for studying the politicization of culture and a serious privacy risk for scalable micro-targeting.

## Key Contributions

- Demonstrates that zero-shot LLMs outperform supervised classifiers (Naive Bayes, LR, SVM, RF, XGBoost over TF-IDF and SBERT) at political alignment inference on two platforms.
- Introduces **confidence-weighted** and **maximum-confidence** user-level aggregation, leveraging LLM-reported confidence to push F1 to ~0.80 on Reddit general discourse.
- Provides cross-model and cross-platform evidence that topical informativeness for political inference is a stable property of *discourse*, not a model artifact.
- Links category-level inference performance to interpretable measures: semantic similarity and user-participation overlap with explicitly political communities.
- Develops a word-level confidence analysis surfacing politicized non-political vocabulary, suggesting a methodology for tracking cultural politicization.
- Releases anonymized data and replication code.

## Methods

The authors built two datasets: 3,511 partisan-labeled Debate.org users (22,265 arguments across 23 categories) and 2,000 Reddit users labeled via positive-karma activity in r/Conservative or r/democrats (~46,000 texts), with the Reddit labels validated by a five-annotator study (majority-vote accuracy 0.92, Fleiss κ = 0.576). GPT-4o and Llama-3.1-8B were prompted zero-shot for a partisan label plus an integer 1–5 confidence score in structured JSON. User-level predictions used majority vote, confidence-weighted mean, and maximum-confidence mean. Supervised baselines used TF-IDF and Sentence-BERT features under 5-fold CV. Category-level analyses combined SBERT cosine similarity with Jaccard and NPMI user overlap; word-level analyses used Monroe et al.'s Dirichlet-prior log-odds alongside mean per-word LLM confidence. Sensitivity checks filtered explicit political content from general categories.

## Findings

- Text-level macro F1: GPT-4o 0.647 (DDO) / 0.624 (Reddit); Llama-3.1-8B 0.619 / 0.534 — all well above chance.
- LLM-reported confidence is monotonically tied to accuracy: top-confidence bins exceed F1 = 0.8; bottom bins are near chance.
- User-level maximum-confidence aggregation reaches F1 = 0.799 on Reddit general texts (+0.193 over text level).
- GPT-4o beats all supervised baselines; Llama matches or exceeds them after user aggregation.
- Strong cross-model (r = 0.76–0.84) and cross-platform (r = 0.67) correlations in category-level F1 indicate stable topical effects.
- Beyond Politics, Religion, Economics, Science, Society, and Health categories yield strong inference (e.g., DDO Religion F1 = 0.742 with GPT-4o).
- Category inference performance correlates with both semantic and social proximity to Politics.
- High word-level model confidence predicts partisan informativeness; politicized cultural terms (Tesla, Taylor Swift, boomer) carry partisan signal despite balanced raw frequencies.
- Results survive filters that strip explicit political content from non-political categories.

## Connections

This work extends the trait-inference-from-digital-traces tradition into the LLM era and speaks directly to ongoing concerns about LLM-enabled profiling and targeting; it pairs naturally with [[DeVerna2025-dl]] on LLM behavior in political contexts and [[Hackenburg2025-dj]] on LLM persuasion/micro-targeting. Methodologically, its zero-shot classification framing connects to broader text-as-data uses of LLMs in [[Tornberg2025-ir]] and [[Le-Mens2025-qz]], while the focus on politicization of ostensibly nonpolitical discourse resonates with cultural-signal work such as [[Tan2024-vl]]. On the risk side, it complements studies of manipulation infrastructure like [[Luceri2025-tr]] and [[Minici2024-tf]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lee2026-je.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-knows-your-politics-are-online/id1866587707?i=1000755386486)
