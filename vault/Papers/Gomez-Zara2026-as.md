---
title: "Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"
aliases: ["Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"]
authors: ["Diego Gómez-Zará", "Hernan Valdivieso", "Jorge Pérez", "Denis Parra", "Sebastián Valenzuela"]
year: 2026
doi: 10.1080/21670811.2026.2730327
bibtex_key: Gomez-Zara2026-as
topics: [llms-in-content-analysis, llm-augmented-research-methods]
citation_count: 0
open_access: true
source_url: https://doi.org/10.1080/21670811.2026.2730327
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gomez-Zara2026-as.mp3
pdf_available: true
discovery_date: 2026-09-18T06:05:31.384392Z
---

# Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis

> Gómez-Zará, D., Valdivieso, H., Pérez, J., Parra, D., & Valenzuela, S. (2026). Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis. *Digital Journalism*, 1–19. https://doi.org/10.1080/21670811.2026.2730327
>
> [View paper](https://doi.org/10.1080/21670811.2026.2730327)

## Summary

This methods article proposes a workflow for using large language models as **analytical collaborators** — rather than automated classifiers — in deductive content analysis, with a focus on framing research in journalism. The central argument is that applying theoretically grounded codebooks to large, heterogeneous, and evolving news corpora inevitably exposes ambiguities, borderline cases, and underspecified criteria that theory alone cannot resolve. The authors contend that LLMs can help externalize decision rules, surface latent dimensions, and support iterative codebook revision, all while researchers retain final interpretive authority. The approach, called "The LLM Codebook Prompt," is illustrated through a case study of over 3,400 Chilean news articles coded using Semetko and Valkenburg's four generic frames (conflict, economic consequences, human interest, morality).

## Key Contributions

- Introduces **"The LLM Codebook Prompt,"** a reproducible, structured seven-phase workflow combining corpus-level pattern surfacing with explanation-driven codebook refinement.
- Reframes codebook development from a one-time upfront task into an **iterative, dialogic process** where theoretical assumptions are surfaced, tested, and revised.
- Positions LLMs as "augmentative interlocutors" that scaffold reflection, treating model classifications and justifications as objects of analytic scrutiny rather than final outputs.
- Provides concrete prompt-design components (role instruction, theory-referenced frame definitions, few-shot cases, justification-eliciting questions, output instructions) usable with off-the-shelf models and no fine-tuning.
- Delivers documented methodological guidance for journalism and communication scholars working with large, cross-cultural, evolving corpora, with replication scripts on OSF.

## Methods

The workflow has seven phases: (1) establishing theoretical boundaries, (2) broad corpus exposure and pattern surfacing, (3) selection of representative and borderline cases, (4) initial codebook prompt and application, (5) analytic interrogation and criteria elicitation, (6) codebook refinement and theoretical clarification, and (7) stabilization, scaling, and validation. The authors use commercially available LLMs (ChatGPT 5.2; GPT-5 mini) without training or fine-tuning, uploading spreadsheets of headlines and leads, prompting the model to summarize framing prevalence, surface latent frames, curate clear/borderline/ambiguous cases, and justify its decisions. The final codebook is quantitatively validated against human-annotated ground truth using accuracy, precision, recall, and F1, benchmarked against random, Naive Bayes, and TF-IDF/Random Forest baselines — though the authors stress these metrics are reported for transparency, not as the primary contribution.

## Findings

- The LLM identified **conflict** as the most frequent frame, followed by responsibility, with **morality** least frequent and often diluted within other frames.
- It surfaced latent frames outside the original framework — security and order, exceptional/rare events, and risk and emergency events — characteristic of Chilean coverage.
- Systematic human–LLM divergences exposed implicit theoretical assumptions: human coders labeled inherently ethical issues (abuse, corruption) as moral without explicit normative language, while the LLM required explicit moral judgments; the LLM also over-inferred human interest and misclassified corruption/sports contracts under economic consequences.
- A 2014 iCloud leak article revealed that the original morality definition failed to capture **contemporary, digitally contingent understandings** of privacy and respect.
- Researchers productively **rejected** an LLM suggestion to treat sensational/rhetorical language as a distinct frame, clarifying that stylistic devices are not framing constructs.
- In final evaluation, GPT-5 mini achieved comparable or slightly better performance than baselines (conflict F1 .71, economic F1 .71, morality F1 .56).

## Connections

This paper sits within a growing methods literature on using LLMs for content analysis and as augmentations to research workflows, complementing validation-focused work such as [[Bailard2024-pj]] and framing-oriented classification studies like [[Waight2026-ts]] and [[Waight2025-al]]. Its emphasis on iterative, human-in-the-loop codebook refinement and interpretive authority contrasts with purely automated classification approaches and connects to broader debates on reliability and transparency in LLM-assisted coding represented by [[Balluff2026-if]] and [[Le-Mens2025-qz]]. Its attention to surfacing latent, context-dependent frames resonates with computational framing and topic-structure work exemplified by [[Freelon2018-ao]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gomez-Zara2026-as.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-your-codebook-disagrees-with/id1866587707?i=1000790461414)
