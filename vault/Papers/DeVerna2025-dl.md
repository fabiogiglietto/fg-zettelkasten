---
title: "Large language models require curated context for reliable political fact-checking -- even with reasoning and web search"
aliases: ["Large language models require curated context for reliable political fact-checking -- even with reasoning and web search"]
authors: ["Matthew R. DeVerna", "Kai-Cheng Yang", "Harry Yaojun Yan", "Filippo Menczer"]
year: 2025
doi: 
bibtex_key: DeVerna2025-dl
topics: [llm-and-computational-content-analysis, health-misinformation-and-fact-checking]
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

This paper delivers a large-scale benchmark of LLM political fact-checking, evaluating 15 models from OpenAI, Google, Meta, and DeepSeek against more than 6,000 PolitiFact claims scored on a six-point veracity scale. The central argument is that fact-checking is not a task that scaling model capability will automatically solve: standard and reasoning-enabled models perform poorly on internal knowledge alone, and built-in web search offers only moderate, provider-specific gains. The decisive intervention is *evidence access* — a curated retrieval-augmented generation (RAG) pipeline built on summaries of PolitiFact articles raises macro F1 by an average of 233%. The authors also surface an ideological wrinkle: search-enabled models tend to cite credible but left-leaning sources.

## Key Contributions

- A large-scale benchmark comparing 15 LLMs (commercial and open-weight) on six-label PolitiFact fact-checking.
- Systematic evaluation of reasoning and web-search capabilities, both with and without curated RAG augmentation.
- Construction and validation of a curated RAG pipeline using GPT-3.5 summaries of ~24,451 PolitiFact articles.
- Empirical analysis of citation practices in search-enabled LLMs — domain type, reliability, and ideological orientation.
- Evidence that the fact-checking bottleneck is evidence access rather than reasoning, with policy implications for verification workflows.

## Methods

- Assembled the complete PolitiFact archive (2007–Oct 2024), yielding 24,611 claims with six-point Truth-O-Meter verdicts after filtering.
- Built the RAG pipeline: GPT-3.5-turbo summaries → Sentence-BERT (all-MiniLM-L6-v2) embeddings → Chroma vector database; summary faithfulness validated via dual-annotator coding (97% agreement).
- Evaluated 15 LLMs across three categories (standard, reasoning, web-search) in zero-shot and curated RAG conditions (k=3, 6, 9), temperature zero, on stratified samples of 12k and 6k claims.
- Augmented the six-point scale with a "Not Enough Information" abstention label; measured macro precision, recall, and F1.
- Analyzed citation patterns using domain-type classification, NewsGuard reliability scores, and DomainDemo political-leaning scores, with sensitivity checks against alternative quality ratings.

## Findings

- Zero-shot macro F1 for standard models was uniformly low (~0.1–0.3) across all providers.
- Curated RAG raised macro F1 by 21–351% (mean 233%); top configurations reached F1 0.90 (GPT-4o) and 0.89 (DeepSeek-V3) at k=9.
- Reasoning models improved only minimally (avg +0.06) and sometimes performed worse.
- GPT search models substantially beat their non-search variants (+0.50 for GPT-4o), while Gemini search models underperformed by rarely producing citations.
- Retrieval was highly accurate: top-k accuracy 0.96 at k=3, 0.98 at k=6/9; median retrieval rank was 1.
- Cited sources skewed toward high NewsGuard reliability and left-leaning orientation, a pattern robust to excluding PolitiFact and to alternative ratings.
- Models rarely used the "Not Enough Information" label (<10%), invoking it more for "Pants on Fire" claims where retrieval was weaker.

## Connections

This paper sits at the intersection of automated fact-checking and LLM-based content analysis, arguing that curated evidence — not raw model capability — is the limiting factor. It relates to work on LLM ideological and political bias such as [[Rossi2023-847d5a9f]], and to broader efforts using LLMs and correction to counter misinformation, including [[Costello2024-bg]] and [[Spampatti2026-kx]]. Its citation-reliability analysis also connects to source-quality and platform verification concerns explored in [[Cazzamatta2026-lo]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/DeVerna2025-dl.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-fact-check-fail-the-bias/id1866587707?i=1000751701628)
