---
title: "They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse"
aliases: ["They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse"]
authors: ["Walter Paci", "Alessandro Panunzi", "Sandro Pezzelle"]
year: 2025
doi: 
bibtex_key: Paci2025-ag
topics: [computational-methods-llms, political-communication-elections]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2506.06775v1
podcast_url: 
pdf_available: true
discovery_date: 2025-06-15T00:00:00Z
---

# They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse

> Paci, W., Panunzi, A., & Pezzelle, S. (2025). They want to pretend not to understand: The Limits of Current LLMs in Interpreting Implicit Content of Political Discourse. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2506.06775v1)

## Summary

This paper asks whether current large language models can interpret *manipulative implicit content*—specifically implicatures and presuppositions—embedded in naturalistic Italian political discourse. Drawing on Gricean and post-Gricean pragmatic theory, the authors argue that political speech is a uniquely rigorous testbed for pragmatic reasoning because its implicit meanings are deployed strategically and depend heavily on context and world knowledge. Using the expert-annotated IMPAQTS corpus of Italian political speeches, they build a new dataset (IMPAQTS-PID) of ~31.8K implicit passages with expert explanations and evaluate four multilingual LLMs across a multiple-choice task and an open-ended generation task. The central conclusion is negative but instructive: even the best model (GPT-4o-mini) falls well short of expert-level interpretation on ecological data, despite performing better on artificially constructed pragmatic benchmarks.

## Key Contributions

- First use of the IMPAQTS corpus in NLP, and release of **IMPAQTS-PID** (~31.8K annotated implicit passages with expert explanations and validated context windows).
- A dual-task evaluation framework (multiple-choice generation + open-ended generation) paired with an expert linguist human-evaluation protocol.
- Empirical evidence that state-of-the-art LLMs for Italian fall well below expert performance on *naturalistic* pragmatic interpretation, contrasting with stronger results on synthetic benchmarks.
- Demonstration that Chain-of-Thought prompting partially mitigates pragmatic limitations, and identification of contextual/world-knowledge integration as a promising path forward.
- Public release of data and code.

## Methods

- Leveraged the IMPAQTS corpus (1,500 Italian political speeches, 1946–2023) with expert annotations of manipulative "non-bona-fide true" implicit content, yielding 14,932 implicatures and 16,890 presuppositions, each paired with expert explanations and four sentences of left-hand context.
- A human validation study with 9 expert linguists confirmed that four preceding context sentences suffice for interpretation.
- **Multiple-Choice Generation (MCG):** models pick among four candidate explanations; distractors chosen via topic modeling to build hard- and easy-negative subsets, scored against chance (25%), an estimated ceiling (91%), and a BLEU-4 baseline (64%). Models tested: GPT-4o-mini, Aya Expanse 8B, LLAMA3.1 8B, LLAMA3.2 3B.
- **Open-Ended Generation (OEG):** GPT-4o-mini in zero-shot, few-shot, and CoT settings; 150 samples per setting judged by 10 expert linguists on a 5-point scale, with an LLM-as-judge (GPT-4o) comparison.
- Supplementary evaluation on IronITA (irony) and the INVALSI pragmatics benchmark.

## Findings

- On MCG, GPT-4o-mini reached 70% (vs. Aya 62%, LLAMA3.1 56%, LLAMA3.2 43%); only GPT-4o-mini consistently beat the 64% n-gram baseline, yet stayed ~20 points under the 91% ceiling.
- All models did better on easy- than hard-negative distractors (GPT-4o-mini: 73% vs. 65%), showing distractor design strongly affects measured performance.
- LLAMA models showed positional bias toward the last option and refused politically sensitive prompts (up to 91 refusals).
- In OEG, GPT-4o-mini produced fully correct explanations in only 21% (zero-shot), 21% (few-shot), and 27% (CoT) of cases, with "totally wrong" answers around a third to 39%.
- CoT reduced wrong answers and modestly raised correct ones; few-shot gave no meaningful gain.
- Implicatures and presuppositions were comparably difficult (~64% vs. 65% acceptable under CoT).
- The LLM-as-judge rated outputs even more harshly than humans (~60% totally wrong).
- GPT-4o-mini scored 66% on IronITA and 83% on INVALSI pragmatics, indicating pragmatic competence is uneven between artificial and naturalistic settings.

## Connections

This work sits at the intersection of computational pragmatics and political-language analysis; its concern with what LLMs can and cannot reliably extract from political text speaks to broader efforts to use LLMs for content analysis and classification of political and partisan language, such as [[Le-Mens2025-qz]] and [[Balluff2026-if]]. Its emphasis on rigorous, expert-validated benchmarking and the fragility introduced by evaluation design (distractor selection, LLM-as-judge harshness) also resonates with methodological cautions raised in [[Ober2026-vd]]. Otherwise its narrow focus on Italian pragmatic interpretation makes it fairly distinct from the misinformation- and platform-oriented papers in these topic sets.
