---
title: "ConflLlama: Domain-specific adaptation of large language models for conflict event classification"
aliases: ["ConflLlama: Domain-specific adaptation of large language models for conflict event classification"]
authors: ["Shreyas Meher", "Patrick T. Brandt"]
year: 2025
doi: 10.1177/20531680251356282
bibtex_key: Meher2025-qb
topics: [computational-methods-social-research]
citation_count: 3
open_access: false
source_url: https://doi.org/10.1177/20531680251356282
podcast_url: 
pdf_available: true
discovery_date: 2025-07-15T00:00:00Z
---

# ConflLlama: Domain-specific adaptation of large language models for conflict event classification

> Meher, S., & Brandt, P. T. (2025). ConflLlama: Domain-specific adaptation of large language models for conflict event classification. *Research & Politics*, *12*. https://doi.org/10.1177/20531680251356282
>
> [View paper](https://doi.org/10.1177/20531680251356282)

## Summary

ConflLlama is a methodological proof-of-concept showing that parameter-efficient fine-tuning of open-source LLMs can deliver state-of-the-art classification of conflict events while running on consumer-grade hardware. The authors fine-tune Llama 3.1 (8B) with QLoRA on the Global Terrorism Database to classify attack types as a multi-label problem, achieving macro AUC 0.791 and weighted F1 0.753 — a 37.6% improvement over the zero-shot base model and dramatic gains for rare attack categories. The paper argues that fine-tuned generative LLMs should now displace both BERT-style encoders (e.g., ConfliBERT) and manual/rule-based coding pipelines as the default approach for conflict event coding, and provides a replicable roadmap for political scientists to adapt LLMs to their own domains.

## Key Contributions

- A reproducible QLoRA-based fine-tuning recipe for adapting open-source LLMs to political science classification, runnable in ~1 hour under 6 GB VRAM.
- Released ConflLlama model variants (Q4, Q8, BF16) as LoRA adapters and GGUF files, plus replication code on Harvard Dataverse.
- Systematic multi-label benchmarks on the GTD across quantization levels, temporal training windows, and prompt formulations.
- Empirical case for moving conflict event coding from BERT-style encoders toward fine-tuned generative LLMs.
- A practical accessibility argument: lowering hardware and expertise barriers for computational conflict research.

## Methods

The authors fine-tune Llama 3.1 8B with QLoRA (via the Unsloth library), targeting key transformer components for 1000 training steps. The GTD is split temporally at January 1, 2017, yielding 171,514 training and 38,192 test events; preprocessing standardizes descriptions and combines primary/secondary/tertiary attack labels to preserve multi-label structure. They produce zero-shot, Q4, Q8, and BF16 variants and evaluate with macro AUC, accuracy, macro/weighted F1, Hamming Loss, Subset Accuracy, Jaccard partial match, and label density. Ablations vary the temporal training window (1990–2005 through full data) and prompt framing (terrorism-framed vs. neutral).

## Findings

- ConflLlama-Q8 reached macro AUC 0.791 vs. 0.575 for the zero-shot base; Q4 reached 0.749, indicating higher-precision quantization better preserves nuanced distinctions.
- Largest gains were on rare classes: Unarmed Assault +1464%, Barricade Hostage Taking +692%, Hijacking +527%; common classes also improved substantially.
- Multi-label metrics improved sharply: Hamming Loss 0.148 → 0.052, Subset Accuracy 0.320 → 0.724, Partial Match 0.356 → 0.738, with predicted label density (0.975) tracking true density (0.963).
- Broader temporal coverage monotonically improved performance (accuracy 0.69 → 0.76, F1 0.51 → 0.66), suggesting evolving conflict patterns benefit from longer historical windows.
- Residual errors cluster among semantically adjacent categories (e.g., Armed Assault vs. Assassination), where contextual rather than tactical cues dominate.
- Prompt rephrasing barely changed macro F1 (0.635 vs. 0.634), suggesting the fine-tuned model has internalized robust category representations.

## Connections

This work fits a growing methodological literature on adapting LLMs to substantive social-science classification tasks, especially efforts to validate LLM outputs against curated human-coded data — see [[DiGiuseppe2026-pu]] and [[DiGiuseppe2025-es]] on conflict/IR applications, and [[Schroeder2026-im]], [[Le-Mens2025-qz]], and [[Tornberg2025-ir]] on LLMs as annotators or classifiers for political text. The accessibility-via-fine-tuning argument also resonates with broader assessments of open-source LLM viability such as [[Tan2024-vl]].
