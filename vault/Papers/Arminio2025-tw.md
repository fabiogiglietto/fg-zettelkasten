---
title: "Leveraging VLLMs for visual clustering: Image-to-text mapping shows increased semantic capabilities and interpretability"
aliases: ["Leveraging VLLMs for visual clustering: Image-to-text mapping shows increased semantic capabilities and interpretability"]
authors: ["Luigi Arminio", "Matteo Magnani", "Matias Piqueras", "Luca Rossi", "Alexandra Segerberg"]
year: 2025
doi: 10.31235/osf.io/bf459
bibtex_key: Arminio2025-tw
topics: [llm-augmented-research-methods, climate-and-misinformation-message-interventions]
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

This paper proposes and evaluates a Vision-and-Large-Language-Model (VLLM) based pipeline for clustering social media images by *connotative* rather than *denotative* meaning. Drawing on Barthes' semiotic distinction, the authors argue that computational social science needs clusters organised by culturally embedded meaning (e.g., "renewable energy") rather than by depicted objects (e.g., "round things"). They use GPT-4-turbo (and LLaVA as an open alternative) to generate paragraph-length descriptions of Instagram climate-change images, embed those texts, and cluster them — then compare against a standard VGG16 CNN baseline. The VLLM pipeline yields substantially higher connotative cluster quality, comparable denotative quality, and—crucially—high human interpretability via TF-IDF keyword summaries.

## Key Contributions

- Reframes semantic image clustering for social science as **connotative clustering**, grounded in Barthesian semiotics rather than object-recognition benchmarks.
- Proposes a VLLM-to-text-to-embedding-to-clustering pipeline as a drop-in alternative to CNN feature extraction.
- Adapts the Grimmer & King cluster-quality measure to separately quantify denotative and connotative validity using expert-coded image pairs.
- Demonstrates that intermediate textual descriptions make clusters human-interpretable, addressing a long-standing opacity problem in CNN-based visual analysis.
- Shows the result generalises (with reduced absolute performance) to open-source VLLMs, suggesting the finding is about model class rather than vendor.

## Methods

- Dataset of 11,873 Instagram climate-change images (Zhang & Peng, 2022).
- VLLM pipeline: GPT-4-turbo (and LLaVA-1.5-7b) generates one-paragraph connotative descriptions → MiniLM BERT embedding → UMAP/PCA reduction → HDBSCAN clustering.
- Baseline: VGG16 features → same reduction/clustering family.
- Evaluation: 500 expert-annotated image pairs scored on denotative and connotative similarity (Krippendorff's α reaching .81/.71 after consensus). Interpretability assessed by having three raters match image sets to TF-IDF keyword summaries of clusters (Cohen's κ ≈ .74).
- Robustness: alternative embedders (OpenAI text-embedding-3-small), alternative CNNs, alternative prompts.

## Findings

- VLLM-based clustering yields substantially higher connotative quality across all minimum cluster sizes; CNN baseline is marginally better on denotative quality — an explicit and acceptable trade-off.
- Qualitative example: VLLM groups wind turbines and solar panels together as "renewable energy"; CNN groups visually similar Earth images that are semantically heterogeneous.
- Interpretability: raters matched image sets to TF-IDF cluster summaries with .83 precision/recall (vs. ~.03 chance), rising to .87 after merging semantically adjacent clusters; 18/32 clusters had perfect precision.
- Open-source LLaVA reproduces the trend but with lower absolute quality, partly because it misreads embedded text and misses symbolic cues (e.g., an eco-fascist rune that GPT-4 identified).
- Larger minimum cluster sizes increase variance and can degrade connotative quality by merging visually similar but connotatively distinct images.

## Connections

This paper sits in the strand of work using VLLMs and LLMs as semantic interpreters for social-science data, alongside [[Achmann-Denkler2026-lx]] on visual political communication and [[Tornberg2026-lc]] on LLM-driven analysis. It contributes to broader methodological efforts to make generative models reliable, interpretable measurement instruments — adjacent to validation-oriented work like [[Le-Mens2025-qz]] and [[DiGiuseppe2026-pu]] on LLM-based classification, and [[Lai2024-to]] on multimodal social-media analysis. The Barthesian framing and focus on memes/protest imagery also resonate with visual-content studies of platforms such as [[Pante2025-pq]].
