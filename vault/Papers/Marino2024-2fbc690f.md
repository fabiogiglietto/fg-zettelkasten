---
title: "Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"
aliases: ["Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"]
authors: ["Giada Marino", "Fabio Giglietto"]
year: 2024
doi: 10.6092/issn.1971-8853/19524
bibtex_key: Marino2024-2fbc690f
kind: own
topics: [llm-augmented-research-methods, political-communication-elections]
citation_count: 17
open_access: true
source_url: https://doi.org/10.6092/issn.1971-8853/19524
podcast_url: 
pdf_available: true
discovery_date: 
---

# Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline

> Marino, G., & Giglietto, F. (2024). Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline. *Sociologica*. https://doi.org/10.6092/issn.1971-8853/19524
>
> [View paper](https://doi.org/10.6092/issn.1971-8853/19524)

## Summary

This methodological essay documents the design and validation of a fully LLM-integrated ("LLMs-in-the-loop") research pipeline for analyzing political content shared on Facebook during the 2018 and 2022 Italian general elections. Marino and Giglietto embed OpenAI models at three distinct pipeline stages — fine-tuning a binary political classifier, generating embeddings for link clustering, and producing descriptive cluster labels — and argue that such workflows demand novel, task-specific validation protocols rather than the single evaluation step used for conventional fine-tuned transformers. The paper is less about substantive findings than about the methodological reckoning that comes with building research infrastructure atop general-purpose generative models, especially in a non-English context.

## Key Contributions

- Presents a concrete, end-to-end LLMs-in-the-loop pipeline for political discourse analysis on social media in a non-English (Italian) setting.
- Proposes a three-phase, task-specific validation protocol with publicly shared codebooks for cluster coherence and label accuracy.
- Articulates three core validation challenges — the general-purposeness of LLMs, the variable granularity of generated narratives, and the limits of human assessment — and offers practical responses to each.
- Supplies reusable annotation guidelines and prompt templates for researchers adopting similar pipelines.

## Methods

The authors build a five-step pipeline (data gathering, political classification, embedding, clustering, cluster labeling) over 84,874 URLs from the Meta URL Shares Dataset, using only titles and descriptions. A GPT-3 Curie model was fine-tuned as a binary political/non-political classifier on 3,800 URLs hand-coded by seven Italian political communication scholars (Krippendorff's α = 0.812). They benchmarked several embedding models (settling on text-embedding-3-large) and clustering algorithms (settling on k-means with Lloyd's algorithm over 3,072-dimensional embeddings), using Bayesian optimization of cluster count via Silhouette and Hplus metrics. Cluster labels were generated with GPT-4-turbo using engineered prompts and density-based sampling. Validation proceeded in three phases: standard precision/recall/F1 for the classifier; pairwise cluster-coherence judgments by six expert coders on a 0–4 scale; and cluster-label accuracy rated on a three-level scale across four criteria.

## Findings

- The fine-tuned classifier achieved F1 = 0.897 (precision 0.911, recall 0.883), identifying roughly 54% of 2018 and 53% of 2022 posts as political.
- `text-embedding-3-large` outperformed alternatives on internal clustering metrics for Italian political news, yielding ~199 clusters per election.
- Cluster granularity varied substantially — from broad policy areas to single journalistic stories — necessitating a multi-level coherence rubric and complicating the theoretical definition of "narrative."
- Crowdsourced annotators (initially considered via Fiverr) were deemed inadequate because LLMs surpass low-skilled workers on nuanced political-context tasks; PhD-level expert coders were used instead.
- The full labeling task for 397 clusters cost approximately $30 in API fees.

## Connections

This paper is a natural companion to [[Marino2026-he]] by the same research group, and sits squarely within the methodological literature on validating LLM-based measurement and classification, connecting to work on repurposing generative models for text classification such as [[Le-Mens2025-qz]] and on LLM-annotation quality like [[Alizadeh2026-es]]. Its concerns about expert versus crowd evaluation and task-specific validation also speak to the broader push, reflected across [[Balluff2026-bv]] and [[Votta2025-xz]], to establish rigorous standards for integrating LLMs into computational social science workflows.
