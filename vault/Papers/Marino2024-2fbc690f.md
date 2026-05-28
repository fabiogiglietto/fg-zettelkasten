---
title: "Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"
aliases: ["Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"]
authors: ["Giada Marino", "Fabio Giglietto"]
year: 2024
doi: 10.6092/issn.1971-8853/19524
bibtex_key: Marino2024-2fbc690f
kind: own
topics: [generative-ai-and-llms, italian-elections-political-communication]
citation_count: 2
open_access: true
source_url: https://doi.org/10.6092/issn.1971-8853/19524
podcast_url: 
pdf_available: true
discovery_date: 
---

# Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline

## Summary

This methodological essay documents the design and validation of an "LLMs-in-the-loop" pipeline for analyzing political content shared on Facebook during the 2018 and 2022 Italian general elections. The authors integrate OpenAI models at three distinct stages — a fine-tuned binary political classifier, embedding generation for clustering URLs, and GPT-4-turbo-based cluster labeling — and argue that such fully LLM-integrated pipelines demand novel, task-specific validation protocols rather than the monolithic evaluations developed for fine-tuned transformer models. The core contribution is less the pipeline itself than a reflective articulation of three validation challenges: the general-purpose nature of LLMs, the variable granularity of LLM-generated narratives, and the scarcity of human evaluators competent enough to assess LLM outputs.

## Key Contributions

- An end-to-end LLMs-in-the-loop pipeline for political discourse analysis applied to a non-English (Italian) corpus of Facebook-shared URLs.
- A three-phase, task-specific validation protocol covering classification, cluster coherence, and label accuracy, with publicly shared codebooks and rubrics.
- Methodological articulation of three core challenges in validating LLM-integrated pipelines, with practical responses for each.
- Reusable annotation guidelines and prompt templates for researchers building similar pipelines.
- A normative argument that early, competent adoption of LLMs by political communication scholars is itself a countermeasure to their misuse.

## Methods

The pipeline processes 84,874 URLs from the Meta URL Shares Dataset around the 2018 and 2022 Italian elections, using only titles and descriptions. A GPT-3 Curie model was fine-tuned as a binary political classifier on 3,800 URLs coded by seven Italian political communication scholars (Krippendorff's α = 0.812). Embeddings from text-embedding-3-large (selected after comparison with ada-002 and e5-mistral-7b-instruct) were clustered using k-means with Lloyd's algorithm, with Bayesian optimization over 2–200 clusters via Silhouette and Hplus metrics, producing ~199 clusters per election year. GPT-4-turbo generated cluster labels using density-based sampling within an 8,000-token cap. Human validation comprised three phases: standard precision/recall/F1 for the classifier; pairwise cluster coherence rated by six expert coders on a 0–4 scale; and cluster-label accuracy on a three-level scale across four criteria (thematic alignment, implications, content coverage, contextual alignment).

## Findings

- The fine-tuned political classifier achieved F1 = 0.897 (precision 0.911, recall 0.883).
- 54% of 2018 posts and 53% of 2022 posts were classified as political.
- text-embedding-3-large outperformed alternative embedding models on internal clustering metrics for Italian political news.
- Cluster granularity varied substantially, from broad policy domains to single journalistic stories, requiring a multi-level coherence rubric.
- Crowdsourced annotation (e.g., Fiverr) proved inadequate because LLMs outperform low-skilled workers on nuanced political tasks; PhD-level expert coders were necessary.
- The full labeling step for 397 clusters cost approximately $30 in API calls.

## Connections

This paper extends the authors' longer line of work on Italian electoral discourse and coordinated link sharing — see [[Giglietto2023-fa71a001]], [[Giglietto2024-cbeb3f70]], [[Giglietto2020-9d8acdd7]], and [[Giglietto2019-882f1900]] — by recasting that empirical agenda through an LLM-integrated methodology. On the methodological side, it speaks directly to broader debates on repurposing generative models for social science annotation and classification, including [[Tornberg2025-ir]], [[Le-Mens2025-qz]], [[Balluff2026-if]], and [[Dierickx2026-tw]], and complements related Italian-context LLM pipelines such as [[Paci2025-ag]] and [[Arminio2025-tw]].
