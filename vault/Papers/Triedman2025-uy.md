---
title: "What did Elon change? A comprehensive analysis of Grokipedia"
aliases: ["What did Elon change? A comprehensive analysis of Grokipedia"]
authors: ["Harold Triedman", "Alexios Mantzarlis"]
year: 2025
doi: 
bibtex_key: Triedman2025-uy
topics: [generative-ai-media, information-disorder]
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

This paper presents the first large-scale comparative audit of Grokipedia, the AI-generated encyclopedia launched by Elon Musk on 27 October 2025, against English Wikipedia. By scraping virtually the entire Grokipedia corpus (883,858 articles) and combining embedding-based similarity with citation and reliability analyses, the authors show that Grokipedia is overwhelmingly derivative of Wikipedia — to the point of near-copying for its CC-licensed subset — yet systematically longer, more heavily cited, and significantly more reliant on low-quality and outright blacklisted sources. Divergence from Wikipedia concentrates in articles on controversial topics, politics, and biographies, where the rewrites exhibit an ideological slant aligned with Musk's stated views, supporting the framing of Grokipedia as both a synthetic derivative and an ideological project.

## Key Contributions

- First comprehensive, full-corpus comparison of Grokipedia and English Wikipedia.
- Public release of a structured Grokipedia scrape (~99.8% coverage), full-corpus embeddings, and analysis code.
- Empirical demonstration that Grokipedia functions simultaneously as a derivative work and an ideologically targeted rewrite.
- Documentation of a novel "LLM auto-citogenesis" pattern in which Grokipedia cites outputs from its own underlying Grok chatbot and from Musk's X account.
- A reusable auditing framework that combines embedding similarity with Wikipedia's Perennial Sources list and external domain-reliability datasets.

## Methods

The authors scraped 883,858 Grokipedia articles via cloud-parallelized proxied requests and parsed them through a Markdown-based pipeline, matching them against the 28 October 2025 Wikimedia Enterprise English Wikipedia dump on exact titles. Articles were chunked (250 tokens, 100-token overlap) and embedded with Google's EmbeddingGemma, with pairwise cosine similarity computed within matched pairs. CC-license status was detected via the attribution footer. They joined the corpus with WMF pageview data, the Perennial Sources reliability list, Lin et al. (2023) domain quality scores, Wikidata queries identifying US and UK legislators, and Wikipedia's controversial-topics category, and applied WMF language-agnostic models for article quality and topic classification on a 30,000-article subsample.

## Findings

- 56% of Grokipedia articles carry a CC-BY-SA license and show ~90% chunk similarity to Wikipedia; the remaining non-CC articles average ~77% similarity, indicating two distinct generation regimes.
- Non-CC Grokipedia articles are ~4.6x longer than their Wikipedia counterparts and cite roughly twice as many sources.
- Chunk similarity is highest at article openings and declines roughly linearly toward the end.
- "Generally reliable" sources drop from 12.7% to 7.7% of citations, while "generally unreliable" rise from 2.9% to 5.4% and "blacklisted" from 0.04% to 0.1%.
- Non-CC articles are 3.2x more likely to cite generally unreliable sources and 13x more likely to cite blacklisted ones; 11.7% cite at least one blacklisted source.
- Grokipedia includes 42 citations to Stormfront and 34 to InfoWars — none exist on Wikipedia — plus 232 citations to @grok, 186 to @elonmusk, and ~1,050 to shared Grok chatbot conversations.
- Controversial-topic articles diverge most (mean similarity 0.73 vs 0.82); 85.5% cite a generally unreliable source and 21.7% cite a blacklisted one.
- Featured and Good Articles on Wikipedia are disproportionately the targets of non-CC rewrites; Stub/Start/C-class articles are mostly near-copies.
- Topically, STEM and pop culture are largely copied; Biography, Politics, Religion, History, and Society are rewritten.
- Grokipedia's matched articles cover ~69% of Wikipedia's October 2025 non-bot pageviews, showing prioritization of popular topics.

## Connections

This work fits the growing literature interrogating how generative AI reshapes public knowledge infrastructures and ideological information environments, complementing studies of partisan content production and source reliability such as [[Lin2025-xp]] (whose domain reliability scores it directly leverages) and [[Budak2024-ef]] on measuring media quality. Its focus on AI-mediated rewriting of authoritative reference content connects to broader concerns about LLM-driven information ecosystems explored in [[Hackenburg2025-dj]] and [[DeVerna2025-dl]], and its documentation of an ideologically slanted alternative encyclopedia resonates with research on platform-level political asymmetry like [[Gonzalez-Bailon2024-rq]].
