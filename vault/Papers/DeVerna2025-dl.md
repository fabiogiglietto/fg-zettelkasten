---
title: "Large language models require curated context for reliable political fact-checking -- even with reasoning and web search"
aliases: ["Large language models require curated context for reliable political fact-checking -- even with reasoning and web search"]
authors: ["Matthew R. DeVerna", "Kai-Cheng Yang", "Harry Yaojun Yan", "Filippo Menczer"]
year: 2025
doi: 
bibtex_key: DeVerna2025-dl
topics: [generative-ai-media, information-disorder]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2511.18749v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/DeVerna2025-dl.mp3
pdf_available: true
discovery_date: 2026-02-26T05:15:14.418067Z
---

# Large language models require curated context for reliable political fact-checking -- even with reasoning and web search

> DeVerna, M. R., Yang, K., Yan, H. Y., & Menczer, F. (2025). Large language models require curated context for reliable political fact-checking -- even with reasoning and web search. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2511.18749v1)

## Summary

This paper benchmarks 15 large language models from OpenAI, Google, Meta, and DeepSeek on the task of fact-checking over 6,000 political claims drawn from PolitiFact's six-point Truth-O-Meter. Comparing standard, reasoning-enabled, and web-search-enabled variants against the same models augmented with a curated retrieval-augmented generation (RAG) pipeline built on GPT-3.5 summaries of PolitiFact articles, the authors find that internal knowledge and generic web search produce poor-to-moderate accuracy, whereas curated context raises macro F1 by an average of 233%. The central argument is that political fact-checking is bottlenecked by access to high-quality evidence rather than by model reasoning capacity, and that improvements in general LLM capability will not automatically solve verification.

## Key Contributions

- A large-scale six-label benchmark of 15 commercial and open-weight LLMs on PolitiFact claims.
- Systematic comparison of standard, reasoning, and web-search variants with and without curated RAG.
- A validated RAG pipeline indexing GPT-3.5 summaries of 24,451 PolitiFact articles (97% inter-annotator agreement on summary faithfulness).
- Empirical analysis of citation behavior in search-enabled LLMs, covering source types, NewsGuard reliability, and political leaning.
- Evidence reframing the bottleneck in automated fact-checking as evidence access rather than reasoning, with implications for deployment in verification workflows.

## Methods

The authors assembled the full PolitiFact archive (2007–October 2024), generated GPT-3.5-turbo article summaries, embedded them with Sentence-BERT (all-MiniLM-L6-v2), and indexed them in a Chroma vector store. They evaluated 15 LLMs across providers and three categories (standard, reasoning, search-enabled) under zero-shot and RAG conditions (k=3, 6, 9), at temperature zero, on stratified samples of 12k and 6k claims. The label set augmented PolitiFact's six-point scale with a "Not Enough Information" abstention option, and performance was measured by macro precision, recall, and F1. Citation patterns from search-enabled models were classified by domain type, scored on NewsGuard reliability and DomainDemo political lean, with robustness checks using Lin et al. (2023) ratings.

## Findings

- Zero-shot macro F1 for standard models was uniformly low (~0.1–0.3) across providers.
- Curated RAG improved macro F1 by 21–351% (mean 233%); best configurations reached 0.90 (GPT-4o) and 0.89 (DeepSeek-V3) at k=9.
- Reasoning models offered only marginal gains (+0.06 on average) and sometimes hurt performance.
- GPT search models markedly improved over non-search variants (+0.50 for GPT-4o), while Gemini search variants underperformed by rarely producing citations.
- Retrieval was highly accurate (top-k accuracy 0.96 at k=3, 0.98 at k≥6; median rank 1).
- GPT search models cited URLs in 59–72% of responses, often pointing directly to the matching PolitiFact article; PolitiFact, AP, Snopes, FactCheck.org, and Wikipedia dominated.
- Cited sources skewed toward high-reliability but left-leaning outlets, robust to removing PolitiFact and to alternative reliability ratings.
- The "Not Enough Information" abstention label was used <10% of the time and concentrated on "Pants on Fire" claims where retrieval was weaker.

## Connections

This paper extends end-to-end LLM fact-checking work and connects to broader concerns about LLM-based information assessment and ideological skew explored in [[Le-Mens2025-qz]] and DeGiuseppe2025-es adjacent debates; see also [[Hackenburg2025-dj]] on LLM persuasion capabilities and [[Triedman2025-uy]], [[Lin2025-xp]] for related evaluations of LLM behavior on contested content. Its emphasis on curated evidence as the bottleneck speaks to professional fact-checker workflows examined in [[Cazzamatta2026-lo]] and [[Dierickx2026-tw]], and complements platform-level misinformation research such as [[Mosleh2024-op]] and [[Budak2024-ef]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/DeVerna2025-dl.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-fact-check-fail-the-bias/id1866587707?i=1000751701628)
