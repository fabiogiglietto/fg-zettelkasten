---
title: "ConflLlama: Domain-specific adaptation of large language models for conflict event classification"
aliases: ["ConflLlama: Domain-specific adaptation of large language models for conflict event classification"]
authors: ["Shreyas Meher", "Patrick T. Brandt"]
year: 2025
doi: 10.1177/20531680251356282
bibtex_key: Meher2025-qb
topics: [computational-text-methods-llms, llm-augmented-research-methods]
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

ConflLlama is a methods-oriented proof of concept showing that open-source large language models can be efficiently adapted for domain-specific classification in political science. The authors fine-tune Llama 3.1 (8B) using Quantized Low-Rank Adaptation (QLoRA) to classify attack types in terrorism events drawn from the Global Terrorism Database (GTD), achieving a macro-averaged AUC of 0.791 and a weighted F1 of 0.753. Their central argument is dual: that efficient fine-tuning dramatically outperforms zero-shot base models on nuanced, multi-label conflict coding, and that this performance is attainable on consumer-grade hardware (under 6 GB of GPU VRAM), lowering barriers to entry for resource-constrained researchers. The paper frames fine-tuned generative LLMs as the successor to manual coding, rule-based systems, and BERT-style encoders like ConfliBERT.

## Key Contributions

- A practical, reproducible QLoRA fine-tuning methodology for political science classification tasks, positioned as a roadmap other researchers can follow.
- Released ConflLlama model variants (Q4, Q8, BF16) as LoRA adapters and GGUF files on Hugging Face, with replication code on Harvard Dataverse.
- Systematic multi-label benchmarks on the GTD, comparing quantization levels, temporal training scopes, and prompt formulations.
- Empirical support for a shift away from encoder-based approaches (ConfliBERT) toward fine-tuned generative LLMs for conflict event coding.

## Methods

- Fine-tuned Llama 3.1 8B via Parameter-Efficient Fine-Tuning with QLoRA, targeting key transformer components using the Unsloth optimization package (1000 steps, ~1 hour, constant GPU memory under 6 GB).
- Built train/test splits from the GTD with a January 1, 2017 cutoff (171,514 pre-2017 training events; 38,192 post-2017 test events), with preprocessing that standardized event descriptions and combined primary/secondary/tertiary attack labels to preserve multi-label structure.
- Produced base zero-shot, Q4, Q8, and unquantized BF16 variants; evaluated with macro/weighted F1, macro ROC/AUC, Hamming Loss, Subset Accuracy, Partial Match (Jaccard), and label density.
- Ran temporal scope experiments (expanding windows from 1990–2005 through full data) and prompt-variation experiments (terrorism-framed vs. neutral prompts).

## Findings

- ConflLlama-Q8 reached macro AUC 0.791 vs. 0.575 for base Llama-3.1 (a 37.6% overall improvement); Q4 reached 0.749.
- Gains were largest for rare categories: Unarmed Assault +1464%, Hostage Taking (Barricade) +692%, Hijacking +527%; common categories also improved (Bombing/Explosion +65%, Armed Assault +84%).
- Multi-label metrics improved sharply: Hamming Loss dropped to 0.052 (from 0.148), Subset Accuracy rose to 0.724 (from 0.320), Partial Match to 0.738, with predicted label density (0.975) closely matching truth (0.963).
- Broader temporal coverage raised accuracy from 0.69 to 0.76 and F1 from 0.51 to 0.66.
- Misclassifications clustered among semantically related categories (Armed Assault vs. Assassination; Kidnapping vs. Barricade hostage-taking), where context matters more than tactical cues.
- Prompt rephrasing produced near-identical macro F1 (0.635 vs. 0.634), indicating the model learned robust internal representations rather than surface patterns.

## Connections

This paper sits within the broader methodological conversation on using LLMs as substitutes for human annotators in political text analysis, sharing that concern with [[DiGiuseppe2025-es]], [[Le-Mens2025-qz]], and [[Tan2024-vl]]. Its emphasis on fine-tuning open-source models for domain-specific classification complements work benchmarking LLM classification reliability and validity such as [[Fan2025-ut]] and [[Fan2026-af]].
