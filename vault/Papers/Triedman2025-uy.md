---
title: "What did Elon change? A comprehensive analysis of Grokipedia"
aliases: ["What did Elon change? A comprehensive analysis of Grokipedia"]
authors: ["Harold Triedman", "Alexios Mantzarlis"]
year: 2025
doi: 
bibtex_key: Triedman2025-uy
topics: [llms-in-content-analysis, misinformation-exposure-recalibration]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2511.09685v1
podcast_url: 
pdf_available: true
discovery_date: 2025-11-15T00:00:00Z
---

# What did Elon change? A comprehensive analysis of Grokipedia

> Triedman, H., & Mantzarlis, A. (2025). What did Elon change? A comprehensive analysis of Grokipedia. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2511.09685v1)

## Summary

This paper delivers the first large-scale, full-corpus comparison of Grokipedia—the AI-generated encyclopedia launched by Elon Musk in October 2025—against English Wikipedia. Scraping nearly the entire Grokipedia corpus (883,858 articles), the authors combine embedding-based similarity, citation analysis, and external reliability datasets to characterize how the two services differ. Their central finding is a dual portrait: Grokipedia is heavily *derivative* of Wikipedia—especially in its CC-licensed subset—yet longer, more heavily sourced, and systematically more reliant on low-quality and blacklisted domains, with pronounced ideological divergence in articles on controversial topics and elected officials. The authors frame Grokipedia as simultaneously a "synthetic derivative" of crowdsourced knowledge and an ideological project reflecting Musk's stated political views.

## Key Contributions

- First comprehensive, full-corpus comparative analysis of Grokipedia versus English Wikipedia.
- Public release of a structured scrape of ~99.8% of Grokipedia plus full-corpus embeddings (HuggingFace) and analysis code (GitHub).
- Empirical evidence characterizing Grokipedia as both a synthetic derivative of Wikipedia and an ideological project, especially in political and controversial domains.
- Documentation of a novel "LLM auto-citogenesis" pattern, where an AI-built encyclopedia cites outputs from its own underlying chatbot and Musk-affiliated X accounts.
- A reusable auditing framework combining embedding similarity with multiple external reliability datasets (Perennial Sources, Lin et al. domain scores).

## Methods

The authors scraped 883,858 Grokipedia articles (28–30 October 2025) via a Markdown-based parser and compared them to the 28 October Wikimedia Enterprise English dump, joined on exact title matches. They chunked articles into 250-token windows with 100-token overlap, embedded them with Google's EmbeddingGemma (300M), and computed within-article cosine similarity. CC-license status was detected via footer string matching. External joins included WMF pageview aggregations, Wikipedia's Perennial Sources reliability list, Lin et al. (2023) domain reliability scores, Wikidata queries for US Congress and UK Parliament members, and Wikipedia's controversial topics category (2,056 articles). Quality and topic classification used WMF's language-agnostic models on a 30,000-article subsample.

## Findings

- 56% of Grokipedia articles (496,058) carry a CC-BY-SA license and are far more similar to Wikipedia (~90% chunk similarity) than the 385,139 non-CC articles (~77%), implying different generation prompts.
- Grokipedia's articles overlap with Wikipedia pages accounting for ~69% of English Wikipedia's October pageviews—evidence it prioritized popular content and its highest-quality (Featured/Good) articles.
- Non-CC articles are ~4.6x longer and cite roughly twice as many sources; chunk similarity is highest at article openings and declines toward the end.
- Source reliability degrades: "generally reliable" citations fall from 12.7% to 7.7%, "generally unreliable" rise from 2.9% to 5.4%, and non-CC articles are 3.2x more likely to cite unreliable and 13x more likely to cite blacklisted sources.
- Grokipedia includes 12,522 citations to very-low-quality domains, including 42 to Stormfront and 34 to InfoWars—zero of which appear on Wikipedia.
- Novel "LLM auto-citogenesis": ~1,050 citations to shared Grok chatbot conversations, 232 to @grok, and 186 to @elonmusk on X.
- Controversial-topic articles diverge most (mean similarity 0.73 vs 0.82), overwhelmingly lack CC licensing (93.1%), and skew ideologically toward Musk's stated views; Biography, Politics, History, and Society topics are predominantly rewritten while STEM and pop-culture content are near-copies.

## Connections

This paper is a methodologically rigorous entry in the study of AI-mediated and ideologically motivated knowledge platforms; within the provided set, its concerns about synthetic content and unreliable sourcing connect to work on LLM-generated persuasion and disinformation such as [[Hackenburg2025-dj]] and [[DeVerna2025-dl]], and to broader analyses of source reliability and information disorder like [[Cazzamatta2026-lo]]. Its documentation of an AI system citing its own outputs offers a concrete case study for debates about self-referential AI knowledge that resonate with generative-AI risk work such as [[Spampatti2026-kx]]. No other listed paper directly addresses Wikipedia forks or encyclopedic auditing, so those remain the closest genuine intellectual links.
