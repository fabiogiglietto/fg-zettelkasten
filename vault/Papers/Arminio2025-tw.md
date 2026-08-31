---
title: "Leveraging VLLMs for visual clustering: Image-to-text mapping shows increased semantic capabilities and interpretability"
aliases: ["Leveraging VLLMs for visual clustering: Image-to-text mapping shows increased semantic capabilities and interpretability"]
authors: ["Luigi Arminio", "Matteo Magnani", "Matias Piqueras", "Luca Rossi", "Alexandra Segerberg"]
year: 2025
doi: 10.31235/osf.io/bf459
bibtex_key: Arminio2025-tw
topics: [llms-in-content-analysis, digital-research-methods-teaching]
citation_count: 2
open_access: false
source_url: https://doi.org/10.31235/osf.io/bf459
podcast_url: 
pdf_available: true
discovery_date: 2025-09-15T00:00:00Z
---

# Leveraging VLLMs for visual clustering: Image-to-text mapping shows increased semantic capabilities and interpretability

> Arminio, L., Magnani, M., Piqueras, M., Rossi, L., & Segerberg, A. (2025). Leveraging VLLMs for visual clustering: Image-to-text mapping shows increased semantic capabilities and interpretability. *Soc. Sci. Comput. Rev.*. https://doi.org/10.31235/osf.io/bf459
>
> [View paper](https://doi.org/10.31235/osf.io/bf459)

## Summary

This paper argues that semantic image clustering for computational social science should be reframed as **connotative clustering** — grouping images by their socially and culturally embedded meaning rather than merely by the objects they depict. Drawing on Barthes' denotation/connotation distinction, the authors contend that the CNN-based pipelines currently dominant in the field capture denotative content well but miss connotative meaning and are hard to interpret. They propose a Vision-and-Large-Language-Model (VLLM) pipeline that generates connotative textual descriptions of images, embeds and clusters those descriptions, and summarizes clusters with TF-IDF keywords. Tested on a dataset of 11,873 climate-change Instagram images, the VLLM approach substantially improves connotative cluster quality and interpretability at a small cost to denotative coherence.

## Key Contributions

- Reframes semantic clustering for social science explicitly as connotative clustering, grounded in Barthesian semiotic theory.
- Proposes and evaluates a VLLM-to-text-to-embedding-to-clustering pipeline as a drop-in alternative to CNN feature extraction, enabling direct comparison.
- Adapts the Grimmer & King cluster quality measure to separately quantify denotative and connotative validity using human-annotated image pairs.
- Provides empirical evidence that VLLM pipelines yield both higher connotative quality and much greater interpretability.
- Demonstrates generality by replicating gains with an open-source model (LLaVA), and identifies trade-offs and future directions.

## Methods

- **Data:** 11,873 climate-change Instagram images, previously used as a clustering benchmark.
- **VLLM pipeline:** one-paragraph connotative descriptions from GPT-4-turbo (and LLaVA-1.5 for open replication), embedded with a MiniLM BERT model, dimensionality-reduced (UMAP/PCA), and clustered with HDBSCAN (min cluster sizes 50/100/200).
- **Baseline:** VGG16 feature extraction with matched reduction and clustering.
- **Quality evaluation:** adapted Grimmer & King measure split into denotative and connotative dimensions, using 500 expert-rated image pairs (Krippendorff's α reaching .81/.71 after consensus rounds).
- **Interpretability evaluation:** three coders matched 160 image sets to TF-IDF cluster summaries (Cohen's Kappa ≈ .74).
- Robustness checks with alternative embeddings, CNNs, and prompts in the appendix.

## Findings

- The VLLM pipeline achieves substantially higher connotative quality across all tested cluster sizes; the CNN pipeline is only marginally better on denotative quality — the expected trade-off.
- Larger minimum cluster sizes can degrade VLLM connotative quality by merging visually similar but connotatively distinct images.
- Qualitatively, the VLLM pipeline groups wind turbines and solar panels together (renewable energy), whereas the CNN groups visually similar Earth imagery despite semantic heterogeneity.
- Open-source LLaVA reproduces the trend at lower absolute scores; it was weaker at reading text and missed symbolic cues (e.g., a runic eco-fascist symbol GPT-4 caught).
- Interpretability: precision/recall ≈ .83 (vs. ~.03 chance), rising to .87 after merging adjacent clusters; errors concentrated on semantically overlapping cluster pairs.

## Connections

This is primarily a methods contribution to the [[llm-augmented-research-methods]] register, using LLM-generated text as an interpretable intermediate representation for computational analysis. Its climate-communication testbed of memes and protest imagery touches on visual content relevant to misinformation and message-intervention research, though the other papers under those topics address persuasion and intervention effects rather than clustering methodology, so the intellectual overlap is thematic rather than direct.
