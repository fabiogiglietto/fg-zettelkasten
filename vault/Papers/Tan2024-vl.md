---
title: "Large Language Models for data annotation and synthesis: A survey"
aliases: ["Large Language Models for data annotation and synthesis: A survey"]
authors: ["Zhen Tan", "Dawei Li", "Song Wang", "Alimohammad Beigi", "Bohan Jiang", "Amrita Bhattacharjee", "Mansooreh Karami", "Jundong Li", "Lu Cheng", "Huan Liu"]
year: 2024
doi: 
bibtex_key: Tan2024-vl
topics: [llm-computational-content-analysis, llm-augmented-research-methods]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2402.13446v3
podcast_url: 
pdf_available: false
discovery_date: 2024-02-15T00:00:00Z
---

# Large Language Models for data annotation and synthesis: A survey

> Tan, Z., Li, D., Wang, S., Beigi, A., Jiang, B., Bhattacharjee, A., Karami, M., Li, J., Cheng, L., & Liu, H. (2024). Large Language Models for data annotation and synthesis: A survey. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2402.13446v3)

## Summary

This survey maps the emerging subfield of using Large Language Models (LLMs) like GPT-4 to automate data annotation and synthesis — tasks historically dependent on costly human labor. The authors argue that while prior surveys cover LLM architectures and training pipelines, none focus specifically on LLMs as annotators and data generators. They propose a three-part taxonomy organizing the literature around how LLM annotations are generated, how their quality is assessed, and how they are utilized downstream, while also flagging methodological and ethical concerns distinct to this paradigm.

## Key Contributions

- Presents what the authors describe as the first dedicated survey of LLM-based data annotation and synthesis.
- Introduces a structured taxonomy along three axes: annotation generation, annotation assessment, and annotation utilization.
- Reviews the spectrum of learning paradigms that consume LLM-generated labels for training downstream models.
- Catalogs recurring challenges and ethical issues, framing them as an agenda for future research.

## Methods

The paper is a literature survey rather than an empirical study. The authors aggregate work across LLM-based annotation pipelines and build a taxonomy classifying methods by stage (generation, assessment, utilization) and by learning paradigm (e.g., supervised and other downstream uses). Coverage is positioned as complementary to existing LLM surveys, with a deliberate focus on annotation/synthesis as an application domain.

## Findings

- The literature decomposes naturally into generation, assessment, and utilization phases of LLM-produced annotations.
- A diversity of learning strategies — supervised fine-tuning and beyond — exist for integrating LLM-generated labels into model training.
- Quality assurance of generated annotations remains an unsolved, recurring concern across studies.
- Ethical risks tied to automated labeling (bias propagation, accountability, transparency) are a persistent theme deserving structured attention.

## Connections

This survey provides foundational scaffolding for the many empirical studies in this register that use LLMs to annotate political, communication, or social-science text data — e.g., [[Tornberg2026-lc]], [[Tornberg2025-ir]], [[Le-Mens2025-qz]], [[Balluff2026-if]], and [[Dierickx2026-tw]] all operationalize LLMs as annotators in ways the taxonomy here helps situate. It also speaks directly to the quality-assessment concerns raised in validation-focused work such as [[DeVerna2025-dl]] and [[Lee2026-je]], and to synthesis-as-substitute-for-human-data debates relevant to [[Hackenburg2025-dj]].
