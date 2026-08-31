---
title: "Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts"
aliases: ["Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts"]
authors: ["Teresa Ober", "Karyssa A. Courey", "Michael Flor"]
year: 2026
doi: 10.5281/zenodo.18733521
bibtex_key: Ober2026-vd
topics: [llm-augmented-research-methods, digital-research-methods-teaching]
citation_count: 0
open_access: true
source_url: https://doi.org/10.5281/zenodo.18733521
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ober2026-vd.mp3
pdf_available: true
discovery_date: 2026-02-27T06:09:00.657393Z
---

# Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts

> Ober, T., Courey, K. A., & Flor, M. (2026). Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts. *Open MIND*, *18*, 156–179. https://doi.org/10.5281/zenodo.18733521
>
> [View paper](https://doi.org/10.5281/zenodo.18733521)

## Summary

This paper proposes a hybrid, human-in-the-loop methodological framework for analyzing qualitative interview data that integrates three components: grounded human coding, semantic topic modeling, and LLM prompt engineering. The authors apply the workflow to focus group transcripts from 13 U.S. middle and high school teachers discussing how communication and digital literacy skills should be conceptualized and assessed within competency-based education (CBE). The central argument is that combining mathematically grounded, reproducible topic clustering with LLM-assisted labeling and iterative human codebook refinement can scale qualitative analysis while preserving interpretive depth and epistemological integrity. Topic modeling is positioned as a more transparent foundation than opaque neural approaches, with LLMs augmenting — never replacing — human analysts.

## Key Contributions

- A replicable, multi-stage framework combining grounded human coding, SentenceBERT topic modeling with Affinity Propagation clustering, and LLM prompt engineering.
- A cross-model consistency check (ChatGPT-4o vs. Copilot) as a quality-assurance strategy for AI-generated topic labels.
- Transparent documentation of LLM configurations, prompts, and a worked example of codebook refinement (Version 1 → Version 2).
- Substantive insights into how teachers conceptualize and assess communication and digital literacy in CBE contexts.
- A contribution to emerging best practices for integrating AI into qualitative educational research under a human-in-the-loop paradigm.

## Methods

Six semi-structured Zoom focus groups (2023–2024) with 13 teachers were transcribed, cleaned, and segmented by skill (communication, digital literacy) and topic (framework, assessment), with sentences as units of analysis. Preliminary grounded coding produced an initial codebook. A topic modeling pipeline used SentenceBERT embeddings, Affinity Propagation clustering (~78–79 first-level clusters, 32 superclusters per skill), cosine similarity filtering (threshold 0.5), and representative "bestwords." LLM prompting (adapted from Barany et al., 2024) with ChatGPT-4o and Copilot generated topic labels and descriptions, evaluated via exact-match rates and cosine similarity across models. Human analysts then mapped themes onto data-derived clusters to refine the codebook.

## Findings

- Topic modeling produced 14 meaningful high-level clusters for communication and 16 for digital literacy after removing conversational-filler outliers.
- Cross-model label agreement: 33.3% identical labels (communication) and 43.8% (digital literacy); average cosine similarities ranged 0.827–0.880 for labels and descriptions.
- No clear hallucinations were observed on human review; divergences were mostly minor phrasing differences.
- Teachers framed communication as inherently multimodal with audience awareness and social-emotional dimensions, calling for less "squishy" frameworks.
- Digital literacy was seen as fluid and rapidly evolving, emphasizing information evaluation, digital citizenship, and ethical engagement amid AI and misinformation.
- Assessment challenges centered on validity, subjectivity, equity, and capturing nuanced interpersonal/ethical dimensions.
- Disciplinary variation emerged (STEM technical precision vs. humanities audience adaptation), and the codebook revision introduced finer subcategories, a new "teaching" category, and more explicit contextual dimensions.

## Connections

This paper sits within the growing literature on LLM-augmented content analysis and coding; its cross-model consistency check and human-in-the-loop stance connect it to work validating LLMs as classifiers and coders such as [[Le-Mens2025-qz]], [[Tan2024-vl]], and [[Fan2025-ut]]. Its emphasis on reproducibility and preserving human interpretive authority resonates with methodological caution found in [[Waight2025-al]] and [[Balluff2026-if]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ober2026-vd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-human-insight-analyzing-interviews/id1866587707?i=1000751869925)
