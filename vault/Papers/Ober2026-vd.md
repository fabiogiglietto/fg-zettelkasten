---
title: "Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts"
aliases: ["Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts"]
authors: ["Teresa Ober", "Karyssa A. Courey", "Michael Flor"]
year: 2026
doi: 10.5281/zenodo.18733521
bibtex_key: Ober2026-vd
topics: [llm-augmented-research-methods]
citation_count: 0
open_access: true
source_url: https://doi.org/10.5281/zenodo.18733521
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ober2026-vd.mp3
pdf_available: true
discovery_date: 2026-02-27T06:09:00.657393Z
---

# Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts

> Ober, T., Courey, K. A., & Flor, M. (2026). Integrating topic modeling and LLM prompt engineering into a human-driven approach to analyze interview transcripts. *Zenodo (CERN European Organization for Nuclear Research)*, *18*, 156–179. https://doi.org/10.5281/zenodo.18733520
>
> [View paper](https://doi.org/10.5281/zenodo.18733520)

## Summary

This paper proposes a human-in-the-loop methodological framework that integrates grounded human coding, sentence-embedding topic modeling, and LLM prompt engineering to analyze qualitative interview data at scale without sacrificing interpretive depth. The authors demonstrate the workflow on six focus groups with 13 U.S. middle and high school teachers discussing how communication and digital literacy should be conceptualized and assessed within competency-based education (CBE). They argue that topic modeling supplies mathematically transparent thematic structure, LLMs accelerate labeling and codebook refinement, and human analysts preserve construct validity and theoretical coherence — yielding a refined, more structured codebook and substantive insights into teacher perspectives on 21st-century skills.

## Key Contributions

- A replicable multi-stage pipeline combining grounded human coding, SentenceBERT embeddings with Affinity Propagation clustering, and LLM-assisted topic labeling.
- Use of **cross-model agreement** (ChatGPT-4o vs. Copilot) — exact-match rates and cosine similarity — as a quality-assurance heuristic for LLM-generated labels.
- A worked example of codebook refinement (Version 1 → Version 2) illustrating how AI-surfaced clusters can reshape human categories.
- Substantive findings on how teachers conceptualize and assess communication and digital literacy in CBE contexts.
- Practical guidance (prompts, model settings, thresholds) for transparent, reproducible AI-augmented qualitative research.

## Methods

Six Zoom-based semi-structured focus groups (2023–2024, 13 teachers) were transcribed, cleaned, and segmented by skill and topic at the sentence level. After preliminary grounded human coding produced an initial codebook, sentences were embedded with SentenceBERT, clustered via Affinity Propagation into first-level clusters and superclusters, and filtered by cosine similarity (threshold 0.5) to extract representative "bestwords." ChatGPT-4o and Copilot were then prompted (following Barany et al., 2024) to generate topic labels and descriptions from the representative content. Cross-model exact-match and cosine-similarity comparisons served as quality checks, and human analysts iteratively mapped themes onto clusters to produce the refined codebook.

## Findings

- Topic modeling yielded 14 meaningful higher-level clusters for communication and 16 for digital literacy after pruning conversational-filler outliers.
- LLM label agreement: 33.3% identical labels for communication clusters and 43.8% for digital literacy; cosine similarities ranged 0.827–0.880 across labels and descriptions.
- Human review found no clear hallucinations; cross-model disagreements were mostly minor phrasing differences.
- Teachers framed communication as multimodal (speaking, listening, writing, presenting) with audience and social-emotional dimensions, and asked for less "squishy" frameworks.
- Digital literacy was described as fast-evolving, centered on information evaluation, digital citizenship, and ethical engagement under AI and misinformation pressures.
- Assessment challenges clustered around validity, subjectivity, equity, and difficulty of standardizing interpersonal/ethical dimensions; disciplinary differences (STEM vs. humanities) also emerged.
- Codebook V2 introduced finer subcategories (e.g., whole-skill vs. subskill prioritization), added a "teaching" category, and consolidated redundant codes.

## Connections

No other papers have been indexed under shared topics yet, so there are no sibling notes to link. Intellectually, the work sits alongside Barany et al. (2024) and Xiao et al. (2023) on hybrid LLM-assisted qualitative coding, and extends Braun & Clarke–style thematic analysis and grounded theory into a transparent, embeddings-plus-LLM workflow.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Ober2026-vd.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-ai-human-insight-analyzing-interviews/id1866587707?i=1000751869925)
