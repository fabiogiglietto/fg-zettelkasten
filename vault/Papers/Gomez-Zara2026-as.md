---
title: "Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"
aliases: ["Revisiting framing codebooks with AI: Employing large language models as analytical collaborators in deductive content analysis"]
authors: ["Diego Gómez-Zará", "Hernán Valdivieso", "Jorge Pérez", "Denis Parra", "Sebastián Valenzuela"]
year: 2026
doi: 10.1080/21670811.2026.2730327
bibtex_key: Gomez-Zara2026-as
topics: [computational-methods-llms, llm-augmented-research-methods]
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

This methods article proposes a workflow for using large language models as *analytical collaborators* — "augmentative interlocutors" — rather than automated classifiers in deductive content analysis, focused on framing research in journalism. The central argument is that applying theoretically grounded codebooks (here, Semetko and Valkenburg's four generic frames) to large, heterogeneous, and time-dependent news corpora inevitably exposes ambiguities and borderline cases that theory alone cannot resolve. Rather than treating these divergences as classification errors, the authors reframe them as opportunities for methodological and theoretical refinement. The approach, called "The LLM Codebook Prompt," is illustrated through a case study of over 3,400 Chilean news articles, and throughout the workflow the human researcher retains interpretive authority over frame definitions.

## Key Contributions

- Introduces "The LLM Codebook Prompt," a reproducible, structured, seven-phase workflow combining corpus-level pattern surfacing with iterative, explanation-driven codebook refinement.
- Reframes codebook development from a one-time upfront task into an iterative, dialogic process where theoretical assumptions are surfaced, tested, and revised during analysis.
- Positions LLMs as objects of analytic scrutiny — their classifications *and* justifications become material for reflection rather than final outputs.
- Provides concrete prompt-design components (role instruction, theory-referenced frame definitions, few-shot positive/negative cases, justification-eliciting questions) usable with off-the-shelf models without fine-tuning.
- Offers methodological guidance for journalism and communication scholars working with large, cross-cultural, evolving corpora.

## Methods

The workflow proceeds through seven phases: establishing theoretical boundaries, broad corpus exposure, selection of representative and borderline cases, initial codebook prompt and application, analytic interrogation and criteria elicitation, codebook refinement, and stabilization/scaling/validation. A structured "meta-prompt" pairs theory-derived frame definitions with few-shot examples and justification requirements. The case study uses commercially available models (ChatGPT 5.2 and GPT-5 mini, December 2025) applied to a dataset of 3,400+ Chilean news articles coded for four generic frames. A final quantitative validation compares the refined LLM codebook against human-annotated ground truth (accuracy, precision, recall, F1) benchmarked against random, Naive Bayes, and TF-IDF/Random Forest baselines, with replication scripts on OSF.

## Findings

- The LLM ranked "conflict" as most frequent and "morality" as least frequent (often diluted within other frames).
- It surfaced latent frames outside the original framework — security/order, exceptional events, and risk/emergency events — characteristic of Chilean coverage.
- Systematic human–LLM divergences exposed implicit theoretical assumptions: human coders labeled corruption/abuse as moral without explicit normative language, while the LLM required explicit moral judgment; the LLM over-inferred human interest and misclassified corruption under economic consequences.
- A 2014 iCloud leak article revealed that the original morality definition failed to capture contemporary understandings of privacy and digital respect — evidence that frame definitions may be historically contingent.
- Researchers productively *rejected* an LLM suggestion to treat sensational/rhetorical language as a distinct frame, clarifying that stylistic devices are not framing constructs.
- GPT-5 mini achieved comparable or slightly better performance than baselines (conflict F1 .71, economic F1 .71, morality F1 .56), though metrics were reported for transparency rather than optimization.

## Connections

This paper's argument for keeping human interpretive authority central and using LLM divergence as a diagnostic tool contrasts with work treating LLMs primarily as scalable classifiers, connecting it to broader debates on LLM-based annotation quality and validation such as [[Ober2026-vd]] and [[Balluff2026-if]]. Its concern with LLMs reconstructing latent conceptual dimensions and constructs relates to [[Le-Mens2025-qz]], while its emphasis on codebook and prompt design as a methodological object aligns with process-oriented treatments of LLM-augmented coding like [[Nguyen2026-vm]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Gomez-Zara2026-as.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
