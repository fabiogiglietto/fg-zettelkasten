---
title: "They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse"
aliases: ["They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse"]
authors: ["Walter Paci", "Alessandro Panunzi", "Sandro Pezzelle"]
year: 2025
doi: 10.18653/v1/2025.findings-acl.804
bibtex_key: Paci2025-ag
topics: [llms-computational-content-analysis, political-polarization-partisan-news]
citation_count: 0
open_access: false
source_url: https://doi.org/10.18653/v1/2025.findings-acl.804
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse

> Paci, W., Panunzi, A., & Pezzelle, S. (2025). They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2506.06775v1)

## Summary

This paper asks whether contemporary multilingual LLMs can correctly interpret manipulative implicit content — implicatures and presuppositions — in naturalistic Italian political discourse. The authors build IMPAQTS-PID, a dataset of ~31.8K implicit passages drawn from the IMPAQTS corpus of Italian political speeches (1946–2023), each paired with an expert linguist's explanation and a validated four-sentence left context window. They evaluate four LLMs (GPT-4o-mini, Aya Expanse 8B, LLAMA3.1 8B, LLAMA3.2 3B) on both multiple-choice and open-ended generation tasks. All models fall substantially short of expert ceilings: even the strongest model produces fully correct explanations in only about a quarter of open-ended cases, suggesting current LLMs lack the pragmatic competence required for ecologically valid political-language interpretation, despite stronger performance on artificial pragmatics benchmarks.

## Key Contributions

- First NLP use of the IMPAQTS corpus of expert-annotated Italian political speeches.
- Release of **IMPAQTS-PID**, ~31.8K implicit passages (14.9K implicatures + 16.9K presuppositions) with expert explanations and empirically validated context windows.
- A paired MCG + OEG evaluation framework with an expert-linguist judgment protocol for pragmatic interpretation.
- Evidence that LLMs systematically underperform on naturalistic pragmatic reasoning, contradicting more optimistic findings from artificial benchmarks.
- Demonstration that Chain-of-Thought prompting partially mitigates pragmatic deficits while few-shot does not.
- Public release of data and code.

## Methods

The authors filtered IMPAQTS for non-bona-fide-true implicit content and aligned each instance with expert explanations plus four preceding sentences of context (a window validated through a survey of 9 expert linguists). They ran two tasks: (1) Multiple-Choice Generation, where models pick among four candidate explanations with distractors sampled via topic modeling to yield hard- and easy-negative subsets, benchmarked against chance (25%), a BLEU-4 baseline (64%), and an estimated ceiling (91%); and (2) Open-Ended Generation with GPT-4o-mini under zero-shot, few-shot, and CoT prompting, scored on 150 samples per condition by 10 expert linguists on a 5-point scale. Supplementary checks include IronITA, the INVALSI pragmatics benchmark, and an LLM-as-judge comparison using GPT-4o.

## Findings

- GPT-4o-mini led MCG at 70% accuracy, but stayed ~20 points below the 91% expert ceiling; smaller open models (Aya 62%, LLAMA3.1 56%, LLAMA3.2 43%) often failed to beat the BLEU-4 baseline.
- Distractor difficulty mattered substantially: GPT-4o-mini scored 73% on easy negatives vs. 65% on hard negatives, indicating MCG setups can confound pragmatic evaluation.
- LLAMA models displayed positional bias toward the last option and frequent refusals on politically sensitive content.
- In open-ended generation, GPT-4o-mini produced fully correct explanations only 21% (zero-shot), 21% (few-shot), and 27% (CoT) of the time, with totally wrong rates of 39/38/33%.
- CoT prompting modestly helped (more correct, fewer totally wrong); few-shot prompting did not.
- Implicatures and presuppositions were comparably difficult (~64–65% acceptable under CoT).
- Models often grasped partial meaning and targets but failed to assign responsibility to specific political actors.
- GPT-4o-as-judge was harsher than humans (~60% rated totally wrong), suggesting LLM-as-judge underestimates already poor outputs.
- The same model reached 83% on the artificial INVALSI pragmatics subtask, highlighting a gap between constructed and naturalistic pragmatic settings.

## Connections

This work complements other evaluations of LLM limitations on politically and rhetorically complex language, including studies on populist rhetoric detection ([[Arminio2025-tw]]), persuasion in political messaging ([[Hackenburg2025-dj]]), and broader audits of LLM political behavior ([[DeVerna2025-dl]], [[Tan2024-vl]]). It also connects to efforts using LLMs for fine-grained classification of political content ([[Le-Mens2025-qz]], [[Tornberg2025-ir]], [[Brown2025-jk]]), where the present paper's findings on poor pragmatic interpretation provide a cautionary counterpoint to claims of human-level competence on surface-level political NLP tasks.
