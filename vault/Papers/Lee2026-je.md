---
title: "LLMs can infer political alignment from online conversations"
aliases: ["LLMs can infer political alignment from online conversations"]
authors: ["Byunghwee Lee", "Sangyeon Kim", "Filippo Menczer", "Yong-Yeol Ahn", "Haewoon Kwak", "Jisun An"]
year: 2026
doi: 
bibtex_key: Lee2026-je
topics: [llm-computational-content-analysis, political-polarization-partisanship]
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

This paper asks whether large language models can uncover users' political alignment from their online writing — including posts that are not overtly political. Using self-identified partisans from Debate.org and score-labeled users from Reddit's r/Conservative and r/democrats, the authors test GPT-4o and Llama-3.1-8B in a zero-shot setting against traditional supervised classifiers. They find that LLMs reliably infer partisanship, surpass supervised baselines, and exploit subtle lexical cues — including ostensibly nonpolitical cultural references like "Tesla," "Taylor Swift," and "boomer." The work frames this dual capacity as both an analytical instrument for studying the politicization of culture and a substantive privacy risk enabling scalable political micro-targeting.

## Key Contributions

- Shows off-the-shelf LLMs perform reliable zero-shot political alignment inference without task-specific training, beating supervised ML baselines.
- Introduces confidence-based user-level aggregation (confidence-weighted and maximum-confidence averaging) that markedly improves accuracy.
- Provides cross-platform (Debate.org, Reddit) and cross-model (GPT-4o, Llama-3.1-8B) evidence that topical informativeness is a stable property of discourse.
- Links inference accuracy to interpretable features — semantic similarity and user overlap with political discourse — offering a framework for cross-domain signal leakage.
- Develops a word-level confidence analysis that surfaces politicized non-political vocabulary, suggesting a method for tracking cultural politicization over time.
- Flags privacy and democratic risks; releases anonymized data and replication code.

## Methods

- Two datasets: 3,511 partisan Debate.org users (22,265 arguments, 23 categories) and 2,000 Reddit users (~46,000 subreddit-aggregated texts), with Reddit labels validated by a five-annotator study (majority-vote accuracy 0.92, Fleiss κ = 0.576).
- Zero-shot prompting of GPT-4o and Llama-3.1-8B-Instruct with structured JSON outputs yielding a label plus 1–5 confidence score.
- Reddit subreddits mapped to the 23 Debate.org categories via GPT-4o for cross-platform comparison.
- Three aggregation strategies compared: majority vote, confidence-weighted average, maximum-confidence average.
- Supervised baselines (Naive Bayes, Logistic Regression, SVM, Random Forest, XGBoost) using TF-IDF and Sentence-BERT features with 5-fold CV.
- Category proximity measured by embedding cosine similarity (semantic) and Jaccard/NPMI of user participation (social); word-level partisan log-odds via a Dirichlet-prior method.
- Sensitivity analyses filtered explicit political content from general-topic texts.

## Findings

- Text-level macro F1: GPT-4o 0.647 (DDO) / 0.624 (Reddit); Llama 0.619 / 0.534 — all above chance.
- Model-reported confidence correlates monotonically with accuracy; highest-confidence groups exceed F1 = 0.8, lowest near chance.
- User-level aggregation helps: GPT-4o maximum-confidence aggregation reaches F1 = 0.799 on Reddit general texts (+0.193 over text level).
- GPT-4o beats all supervised baselines (best ≈ 0.612 DDO, 0.579 Reddit); Llama matches or exceeds them at the user level.
- Category-level scores correlate strongly across models (r = 0.758 DDO, 0.837 Reddit) and platforms (r = 0.673), indicating stable topical effects.
- "Politics" is most informative, but "Religion," "Economics," "Science," "Society," and "Health" also enable strong inference.
- Semantic and social proximity to the Politics category predict category-level inference performance.
- High word-level confidence tracks partisan signal, spanning both explicit terms (abortion, tax, climate) and politicized cultural terms — robust to stricter content filters.

## Connections

This work extends the LLM-based content-analysis line by showing zero-shot models outperform supervised classifiers, complementing efforts to use LLMs for scaling ideological and stance measurement such as [[Le-Mens2025-qz]]. Its concern with LLM-enabled manipulation and micro-targeting connects to work on AI persuasion and influence like [[Hackenburg2025-dj]] and [[Costello2024-bg]]. The politicization-of-culture framing links to research on partisan divergence in seemingly nonpolitical discourse such as [[Green2025-ap]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lee2026-je.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-knows-your-politics-are-online/id1866587707?i=1000755386486)
