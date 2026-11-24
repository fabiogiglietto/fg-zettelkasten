---
title: "Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"
aliases: ["Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"]
authors: ["Diego Gómez-Zará", "Hernán Valdivieso", "Jorge Pérez", "Denis Parra", "Sebastián Valenzuela"]
year: 2026
doi: 10.1080/21670811.2026.2730327
bibtex_key: Gomez-Zara2026-as
topics: [llm-augmented-research-methods, computational-methods-llms]
citation_count: 0
open_access: false
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

This methods article proposes a workflow for using large language models as *analytical collaborators*—explicitly not automated classifiers—in deductive content analysis for framing research in journalism. The authors argue that applying theoretically grounded codebooks to large, heterogeneous, and time-dependent news corpora exposes ambiguities, borderline cases, and underspecified criteria that theory alone cannot resolve. Rather than treating these as classification errors, the paper reframes them as opportunities for methodological and theoretical refinement. The core proposal, "The LLM Codebook Prompt," positions LLMs as "augmentative interlocutors" that externalize decision rules, surface latent dimensions, and support iterative codebook revision while researchers retain final interpretive authority. The approach is illustrated through a case study of over 3,400 Chilean news articles coded using Semetko and Valkenburg's four generic frames.

## Key Contributions

- Introduces "The LLM Codebook Prompt," a reproducible seven-phase workflow integrating corpus-level pattern surfacing with iterative, explanation-driven codebook refinement.
- Reframes codebook development from a one-time upfront task into an iterative, dialogic process where theoretical assumptions are surfaced, tested, and revised.
- Shows how treating LLM classifications and their justifications as objects of analytic scrutiny—rather than as final outputs—can reveal latent frames and clarify theoretical boundaries.
- Provides concrete prompt-design components (role instruction, theory-referenced frame definitions, few-shot positive/negative cases, justification-requiring questions) usable with off-the-shelf models.
- Emphasizes that the primary value is theory-facing creativity, not scalability or efficiency.

## Methods

The authors define a structured meta-prompt and a seven-phase procedure: (1) establishing theoretical boundaries, (2) broad corpus exposure and pattern surfacing, (3) selection of representative and borderline cases, (4) initial codebook prompt and application, (5) analytic interrogation and criteria elicitation, (6) codebook refinement and theoretical clarification, and (7) stabilization, scaling, and validation. They used commercially available models (ChatGPT 5.2, GPT-5 mini) without fine-tuning, uploading headlines and leads to surface framing prevalence and latent frames, curate clear/borderline/ambiguous cases, elicit explicit justifications, and iteratively refine definitions. A final quantitative validation benchmarked the refined codebook against human-annotated ground truth and against random, Naive Bayes, and TF-IDF/Random Forest baselines using accuracy, precision, recall, and F1. Replication scripts are posted on OSF.

## Findings

- The LLM identified "conflict" as the most frequent frame, "responsibility" next, and "morality" least frequent—often diluted within other frames.
- It surfaced latent frames outside the original framework: security and order, exceptional/rare events, and risk and emergency events characteristic of Chilean coverage.
- Systematic human–LLM divergences exposed implicit theoretical assumptions: human coders labeled inherently ethical issues (abuse, corruption) as moral without explicit normative language, whereas the LLM required explicit moral judgments.
- Borderline cases (a sports match as ambiguous conflict, a tsunami alert as ambiguous human interest) forced explicit theorization of frame boundaries.
- A 2014 iCloud leak article revealed how the original morality definition failed to capture contemporary understandings of privacy and digital respect, suggesting frame definitions are historically contingent.
- Researchers productively *rejected* an LLM suggestion to treat sensational language as a distinct frame, clarifying that stylistic devices are not framing constructs.
- In final evaluation, GPT-5 mini matched or slightly beat baselines (conflict F1 .71, economic F1 .71, morality F1 .56), though metrics were reported for transparency rather than optimization.

## Connections

This paper sits in a growing body of work treating LLMs as instruments for content analysis and coding, and is best read alongside studies that validate or problematize LLM annotation against human coders, such as [[Le-Mens2025-qz]] and [[Tan2024-vl]]. Its insistence on preserving human interpretive authority and using divergence diagnostically contrasts with efficiency- and scalability-oriented classification approaches, making it a methodological counterpoint to work on automated coding pipelines like [[Nenno2025-xa]] and Bastos2025-ol.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gomez-Zara2026-as.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-your-codebook-disagrees-with/id1866587707?i=1000790461414)
