---
title: "Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"
aliases: ["Integrating Large Language Models in Political Discourse Studies on Social Media: Challenges of Validating an LLMs-in-the-loop Pipeline"]
authors: ["Giada Marino", "Fabio Giglietto"]
year: 2024
doi: 10.6092/issn.1971-8853/19524
bibtex_key: Marino2024-2fbc690f
kind: own
topics: [generative-ai-media, computational-social-science]
citation_count: 12
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

This methodological essay documents the design and validation of an "LLMs-in-the-loop" pipeline for studying political discourse on Italian Facebook during the 2018 and 2022 general elections. The authors integrate OpenAI models at three distinct pipeline stages — a fine-tuned GPT-3 Curie binary political classifier, `text-embedding-3-large` embeddings feeding k-means clustering, and GPT-4-turbo cluster labeling — and propose a three-phase, task-specific human validation protocol. Their central argument is that fully LLM-integrated pipelines demand novel validation strategies distinct from those developed for fine-tuned transformer models, because LLMs are general-purpose, produce narratives at variable granularity, and often surpass low-skilled crowd workers, forcing reliance on expert annotators.

## Key Contributions

- An end-to-end, reproducible LLMs-in-the-loop pipeline applied to a non-English (Italian) political communication corpus of ~85k URLs.
- A three-phase validation protocol matched to each LLM-integrated task (classification, clustering coherence, label accuracy), with publicly shared codebooks and rubrics.
- Articulation of three generalizable validation challenges: LLM general-purposeness, variable narrative granularity, and the limits of crowdsourced human evaluation.
- Reusable prompt templates and annotation guidelines for researchers adopting similar workflows.
- A methodological argument for early, competent adoption of LLMs by political communication scholars as a counterweight to manipulative uses.

## Methods

The pipeline runs in five steps: URL collection from the Meta URL Shares Dataset (84,874 Italian-viewed links); binary political classification via a fine-tuned GPT-3 Curie model trained on 3,800 URLs coded by seven experts (Krippendorff's α = 0.812); embedding via `text-embedding-3-large` (3,072 dims); k-means clustering with Bayesian-optimized k (Silhouette + Hplus), yielding ~199 clusters per election; and GPT-4-turbo cluster labeling using density-based item sampling within an 8,000-token cap. Validation proceeds in three phases: standard precision/recall/F1 for the classifier; pairwise cluster coherence on a 0–4 scale plus "uncertain" by six expert coders; and label-accuracy evaluation on a three-level rubric across four criteria (thematic alignment, implications, content coverage, contextual alignment).

## Findings

- Binary classifier reached F1 = 0.897 (precision 0.911, recall 0.883) on held-out data.
- 54% of 2018 posts and 53% of 2022 posts were classified as political.
- `text-embedding-3-large` outperformed `text-embedding-ada-002` and `e5-mistral-7b-instruct` on internal metrics for Italian political news.
- Resulting clusters spanned drastically different levels of granularity, from broad policy domains to individual news events, motivating a multi-level coherence rubric.
- Fiverr/MTurk-style crowd annotators were deemed inadequate because LLM outputs already exceed their quality on nuanced political tasks; PhD-level expert coders were required.
- Labeling all 397 clusters via the GPT-4-turbo API cost roughly $30.

## Connections

This paper contributes to the growing methodological conversation on repurposing generative AI for computational social science, sitting alongside work that benchmarks or critically evaluates LLMs as annotation and analysis tools such as [[Gilardi2026-hw]], [[Le-Mens2025-qz]], and [[Balluff2026-if]]. Its focus on Italian election discourse via the Meta URL Shares Dataset connects it directly to the authors' prior work on coordinated and problematic information sharing, including [[Giglietto2026-9b6a992d]], [[Giglietto2024-cbeb3f70]], [[Giglietto2022-b30e8b4e]], and [[Giglietto2020-6278a4aa]]. The concern with validating LLM-driven narrative and topic extraction also resonates with efforts to audit or characterize LLM behavior in political contexts such as [[Bollenbacher2026-vz]] and [[Alizadeh2026-es]].
