---
title: "Quantifying narrative similarity across languages"
aliases: ["Quantifying narrative similarity across languages"]
authors: ["Hannah Waight", "Solomon Messing", "Anton Shirikov", "Margaret E. Roberts", "Jonathan Nagler", "Jason Greenfield", "Megan A. Brown", "Kevin Aslett", "Joshua A. Tucker"]
year: 2025
doi: 10.1177/00491241251340080
bibtex_key: Waight2025-al
topics: [information-disorder, generative-ai-media]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1177/00491241251340080
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# Quantifying narrative similarity across languages

> Waight, H., Messing, S., Shirikov, A., Roberts, M. E., Nagler, J., Greenfield, J., Brown, M. A., Aslett, K., & Tucker, J. A. (2025). Quantifying narrative similarity across languages. *Sociological Methods & Research*. https://doi.org/10.1177/00491241251340080
>
> [View paper](https://doi.org/10.1177/00491241251340080)

## Summary

This paper defines *narrative similarity* — whether two texts make the same claims about the same events — as a distinct measurement target that prior text-as-data methods (text reuse, topic modeling, semantic similarity) systematically conflate with looser notions of textual overlap. The authors build a three-stage LLM-based pipeline that distills articles into structured claims and subjects, filters candidate pairs with SBERT, and uses GPT-4o (zero-shot or fine-tuned on boundary cases) to judge whether pairs share narratives. They validate the pipeline against four alternative estimators using a hand-coded multilingual gold standard, then apply it to trace how Russian state media's 2022 claims about U.S.-funded Ukrainian "biolabs" diffused into Ukrainian, mainstream U.S., and low-quality U.S. news.

## Key Contributions

- Articulates *narrative similarity* as a precisely defined estimand grounded in narrative sociology, distinct from lexical, semantic, or topical similarity.
- Proposes a scalable LLM-distillation → SBERT-filtering → LLM-annotation pipeline tractable on corpora of hundreds of thousands of multilingual documents.
- Develops a human-in-the-loop ranked-recall validation strategy that yields precision/recall/F1 for what is effectively an unsupervised task.
- Shows that purposive fine-tuning on boundary cases lifts precision from 37% to ~79% with only modest recall loss.
- Provides empirical evidence that low-quality U.S. outlets launder Russian state media narratives at roughly 2.6× the mainstream rate — a pattern entirely invisible to ngram text-reuse methods.

## Methods

The authors assembled 692,560 articles from 45 Russian state, Ukrainian, mainstream U.S., and low-quality U.S. sources (Jan–Apr 2022), keyword-filtering to 3,491 bioweapons-relevant pieces. GPT-4o with concept-guided chain-of-thought prompts produced English summaries plus enumerated subjects and four claim types (descriptive, normative, causal, conceptual) per article. A two-stage SBERT bi-encoder + cross-encoder cascade reduced 6.09M possible pairs to ~64,677 candidates, which GPT-4o then labeled for shared subjects and shared claims (both zero-shot and after fine-tuning on 622 purposively sampled boundary pairs). Validation used a 1,631-pair ranked recall set plus majority-vote precision sampling, benchmarked against 5-gram text reuse, STM topic clustering, standalone SBERT cross-encoder, and a Relatio semantic-role-labeling estimator.

## Findings

- Fine-tuned SBERT-LLM achieved the best performance (F1=60.4; precision 78.8, recall 48.9).
- Zero-shot SBERT-LLM maximized recall (66.0%) but at lower precision (37.0%).
- 5-gram text reuse achieved only 6.4% recall (F1=11.4) — high precision but unfit for studying narrative diffusion beyond syndication.
- Topic modeling (F1=14.7) and Relatio (F1=16.0) performed poorly; standalone SBERT cross-encoder (F1=35.6) trailed the full pipeline.
- 14.1% of low-quality U.S. articles shared narratives with Russian state media vs. 5.4% of mainstream U.S. articles.
- The ngram estimator detected *zero* mainstream U.S. articles sharing Russian narratives, while SBERT-LLM detected ~10% — illustrating how estimator choice can erase a substantive phenomenon.
- Coverage peaked around Russia's March 11 UN Security Council request and the March 24 Hunter Biden funding allegations.

## Connections

This paper is methodologically adjacent to other work on LLM-based measurement of political and propaganda content, notably [[Waight2026-ts]] (likely a companion piece by the same lead author) and approaches to detecting coordinated or laundered messaging such as [[Starbird2025-jj]] and [[DiGiuseppe2026-pu]]/[[DiGiuseppe2025-es]] on Russian information operations. Its concern with cross-lingual narrative tracking connects to [[Humprecht2025-ml]] on comparative misinformation and to broader text-as-data validation debates engaged by [[Le-Mens2025-qz]] and [[Tornberg2025-ir]] on LLMs as measurement instruments.
