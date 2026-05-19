---
title: "Evaluating Embedding Models for Clustering Italian Political News: A Comparative Study of Text-Embedding-3-Large and UmBERTo"
aliases: ["Evaluating Embedding Models for Clustering Italian Political News: A Comparative Study of Text-Embedding-3-Large and UmBERTo"]
authors: ["Fabio Giglietto"]
year: 2024
doi: 10.31219/osf.io/2j9ed
bibtex_key: Giglietto2024-cbeb3f70
kind: own
topics: [generative-ai-and-llms, computational-social-science-methods]
citation_count: 0
open_access: true
source_url: https://doi.org/10.31219/osf.io/2j9ed
podcast_url: 
pdf_available: true
discovery_date: 
---

# Evaluating Embedding Models for Clustering Italian Political News: A Comparative Study of Text-Embedding-3-Large and UmBERTo

## Summary

This paper benchmarks OpenAI's `text-embedding-3-large` against the Italian-specific BERT model UmBERTo for unsupervised clustering of Italian political news URLs shared on Facebook before the 2018 and 2022 national elections. Using K-means and HDBSCAN (with and without UMAP), the author evaluates 1,650 clustering configurations via an adapted Grimmer & King (2011) cluster-quality metric, where thematic coherence between document pairs is rated by a fine-tuned GPT-4o-mini classifier substituting for human coders. The LLM-based embedding model consistently produces more semantically coherent clusters than UmBERTo across both election periods and both clustering algorithms, extending earlier English-language findings to Italian political text.

## Key Contributions

- First systematic comparison of LLM-based versus BERT-based embeddings for unsupervised clustering of Italian political news.
- Empirical evidence that the LLM-embedding advantage observed in English generalizes to Italian.
- A scalable adaptation of the Grimmer & King (2011) interpretive cluster validity framework, replacing human coders with a fine-tuned GPT-4o-mini rater (76.7% accuracy, 0.765 macro-F1).
- A methodological warning about HDBSCAN: high quality scores can correlate strongly with massive noise inflation, undermining representativeness.
- Publicly released code and data for replication and further benchmarking.

## Methods

The author collected 84,874 URLs (title + description) from the Meta URL Shares Dataset covering the pre-election periods of 2018 and 2022, filtered to roughly 35,000 political URLs via a custom binary classifier. Embeddings were generated with `text-embedding-3-large` (3,072 dims) and `umberto-commoncrawl-cased-v1` (768 dims). Clustering used K-means (25–200 clusters) and HDBSCAN (min cluster sizes 10–200), optionally preceded by UMAP, yielding 336 configurations × 5 runs. A balanced sample of 4,167 intra-/inter-cluster/noise document pairs was constructed; 2,506 human-coded pairs were used to fine-tune GPT-4o-mini on a 0–3 thematic coherence scale. ANOVA, multiple regression, and t-tests assessed the effects of embedding model, clustering method, and UMAP on quality scores.

## Findings

- In 2018, K-means + `text-embedding-3-large` (no UMAP) achieved the highest mean quality (1.862); HDBSCAN + UmBERTo scored lowest (0.694).
- In 2022, HDBSCAN + `text-embedding-3-large` (no UMAP) led at 1.681; HDBSCAN + UmBERTo again scored lowest (0.538).
- Embedding model and clustering algorithm had highly significant effects (p < 2e-16); UMAP did not. Models explained 51.6% (2018) and 42.6% (2022) of variance.
- K-means significantly outperformed HDBSCAN overall (2018: 1.745 vs. 1.278; 2022: 1.347 vs. 0.959).
- Cluster quality scores were uniformly lower in 2022 than in 2018 across configurations.
- HDBSCAN quality scores correlated strongly with the proportion of points discarded as noise (r = 0.775, p < 0.001), sometimes exceeding 90% of the data.
- Total cost of fine-tuning and running GPT-4o-mini inferences was under $3, suggesting affordability of LLM-as-judge evaluation.

## Connections

This study complements other Italian-context computational work on political communication and platform discourse such as [[Giglietto2026-9b6a992d]], [[DiGiuseppe2026-pu]], [[DiGiuseppe2025-es]], [[Mannocci2025-ig]], and [[Paci2025-ag]], offering them a validated unsupervised pipeline for thematic clustering of Italian political text. Methodologically, its use of a fine-tuned LLM as a scalable substitute for human coders speaks to broader debates about LLM-as-annotator reliability seen in [[Le-Mens2025-qz]] and [[Tornberg2025-ir]]. Its concerns about evaluation artifacts (HDBSCAN noise inflation, model-choice effects) resonate with critiques of measurement and benchmarking in LLM-driven social science such as [[Bak-Coleman2026-mk]].
