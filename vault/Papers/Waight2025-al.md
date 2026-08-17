---
title: "Quantifying narrative similarity across languages"
aliases: ["Quantifying narrative similarity across languages"]
authors: ["Hannah Waight", "Solomon Messing", "Anton Shirikov", "Margaret E. Roberts", "Jonathan Nagler", "Jason Greenfield", "Megan A. Brown", "Kevin Aslett", "Joshua A. Tucker"]
year: 2025
doi: 10.1177/00491241251340080
bibtex_key: Waight2025-al
topics: [llm-and-computational-content-analysis, disinformation-narratives-and-information-operations]
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

This paper introduces **narrative similarity** — the extent to which two documents make the same claims about the same subjects — as a distinct estimand that existing text-as-data methods (lexical overlap, topic modeling, semantic similarity) conflate and fail to capture faithfully. The authors propose a three-stage pipeline that uses LLMs to distill documents into their core claims and subjects, SBERT to filter candidate pairs down to a tractable set, and a fine-tuned GPT-4o annotator to make pairwise judgments. They rigorously validate the approach against four alternative estimators using hand-coded gold-standard data, then apply it to trace how Russian state media narratives about Ukrainian U.S.-funded "biolabs" diffused into mainstream and low-quality U.S. news during the opening months of the 2022 invasion.

## Key Contributions

- Defines **narrative similarity** as a precise estimand grounded in the sociology of narrative, distinct from lexical, semantic, or topical similarity.
- Offers a scalable multilingual pipeline: LLM distillation → SBERT candidate filtering → LLM pairwise annotation.
- Develops an out-of-sample validation strategy (ranked human-in-the-loop recall set with a stopping rule) that yields supervised metrics for an effectively unsupervised task.
- Demonstrates large gains from fine-tuning on purposively sampled boundary cases.
- Provides empirical evidence of Russian narrative laundering by U.S. outlets, and a general framework transferable to propaganda, misinformation, and policy/cultural diffusion.

## Methods

The authors assembled a corpus of 692,560 articles from 45 Russian state, mainstream U.S., low-quality U.S., and Ukrainian sources (Jan–Apr 2022), filtering to 3,491 biolab-related articles. GPT-4o with concept-guided chain-of-thought prompts summarized each article and enumerated its subjects and its descriptive, normative, causal, and conceptual claims. A two-stage SBERT pipeline (bi-encoder then cross-encoder) reduced 6.09M possible pairs to ~64,677 candidates, which GPT-4o labeled for shared subjects and claims — first zero-shot, then via a version fine-tuned on 622 boundary cases. Validation used human-coded recall and precision sets, and the method was benchmarked against 5-gram text reuse, structural topic modeling, standalone SBERT, and a Relatio semantic-role approach.

## Findings

- The fine-tuned SBERT-LLM pipeline achieved the best overall performance (F1=60.4, precision=78.8, recall=48.9); fine-tuning raised precision from ~37% to ~79% with only modest recall loss.
- Zero-shot SBERT-LLM maximized recall (66.0%) but at low precision (37.0%).
- Exact 5-gram text reuse had high precision but negligible recall (6.4%, F1=11.4), making it unsuitable for studying diffusion beyond direct syndication.
- Topic modeling (F1=14.7) and Relatio (F1=16.0) performed poorly; standalone SBERT (F1=35.6) was second-best but far below the full pipeline.
- Low-quality U.S. outlets shared narratives with Russian state media far more than mainstream outlets (14.1% vs 5.4%).
- The n-gram estimator detected *zero* mainstream U.S. articles sharing Russian narratives, whereas SBERT-LLM detected ~10% — a phenomenon invisible to lexical methods, showing estimator choice has substantive consequences.
- Coverage spiked around Russia's March 11 UN Security Council request and March 24 Hunter Biden funding allegations.

## Connections

This work sits at the methodological core of LLM-based computational content analysis and directly addresses the study of coordinated influence and misinformation diffusion. It shares a companion authorship and empirical focus with [[Waight2026-ts]], and its concern with narrative diffusion connects to work on coordinated information operations and misinformation ecosystems such as [[Starbird2025-jj]] and [[Pierri2025-hm]]; its LLM-as-measurement approach speaks to broader debates on validating LLM annotation for content analysis exemplified by [[Le-Mens2025-qz]] and [[Tornberg2025-ir]].
