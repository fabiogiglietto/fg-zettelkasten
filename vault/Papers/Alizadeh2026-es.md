---
title: "AI coding agents can reproduce social science findings"
aliases: ["AI coding agents can reproduce social science findings"]
authors: ["Meysam Alizadeh", "Mohsen Mosleh", "Fabrizio Gilardi", "Atoosa Kasirzadeh", "Joshua Tucker"]
year: 2026
doi: 
bibtex_key: Alizadeh2026-es
topics: [llm-augmented-research-methods, llms-for-content-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.11447v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Alizadeh2026-es.mp3
pdf_available: true
discovery_date: 2026-06-15T05:32:40.967091Z
---

# AI coding agents can reproduce social science findings

> Alizadeh, M., Mosleh, M., Gilardi, F., Kasirzadeh, A., & Tucker, J. (2026). AI coding agents can reproduce social science findings. *arXiv [cs.CL]*.
>
> [View paper](http://arxiv.org/abs/2606.11447v1)

## Summary

This paper introduces **SocSci-Repro-Bench**, a benchmark of 221 reproducibility tasks drawn from 54 social science papers across political science, sociology, psychology, and communication, and uses it to evaluate whether frontier AI *coding agents* — Claude Code (Opus 4.6) and Codex (GPT-5.3) — can reproduce published computational findings. The authors argue that purpose-built coding agents represent a step-change over prior general-purpose LLM agents: Claude Code reproduces 93.4% of tasks and 78.0% of papers end-to-end, largely by autonomously repairing broken replication environments. They also show that this competence is fragile in revealing ways — supplying the original PDF or nudging the agent toward confirmatory framings degrades its ability to correctly flag non-reproducible tasks, surfacing sycophantic specification search as a risk for AI-assisted validation of science.

## Key Contributions

- **SocSci-Repro-Bench**: first systematically constructed social science reproducibility benchmark spanning four disciplines, 13 substantive domains, five repositories, and three languages (Python, R, Stata).
- **Anonymization-by-design** methodology disentangling memorization/retrieval from genuine computational reproduction, validated by re-running CORE-Bench under both anonymized and non-anonymized conditions.
- **Curation filter** restricting tasks to outputs identical across three manual executions, isolating agent capability from underlying material reproducibility.
- First systematic head-to-head evaluation of **specialized coding agents** (Claude Code, Codex) on social science reproduction.
- Identification of two failure modes for agents as independent validators: **PDF-induced bias** on non-reproducible tasks and **confirmatory-prompt sycophancy**.
- A **research question inference task** as a probe for abstract reasoning from code and data alone.

## Methods

The authors assembled 221 tasks from 54 papers selected via Semantic Scholar searches, filtered for data/code availability and verified through manual execution. Tasks span five categories — plot reading, plot interpretation, yes/no, point estimate extraction, and "No Data" (non-reproducible) probes. Replication packages were anonymized (automated Claude Code scan + manual review) to strip identifying metadata. Both agents were run three times in sandboxed environments without web access, fully autonomously. Stratifications by language, training-cutoff date, and repository were used; supplementary experiments tested (i) metadata recovery as a memorization probe, (ii) research question inference against gold-standard annotations, (iii) PDF context provision, (iv) a confirmatory nudging prompt, and (v) replication on the 28-paper social science subset of CORE-Bench.

## Findings

- **Claude Code**: 93.4% task / 78.0% paper accuracy, 0% failure rate. **Codex**: 62.1% / 35.8%, with 17.8% task failures — mostly environment/dependency issues that Claude resolved autonomously.
- Both agents hit **100% on non-reproducible tasks** in the baseline, correctly identifying missing data/code.
- **No pre- vs post-training-cutoff gap**, and metadata recovery was poor (Claude fully correct on 11.1% of papers; Codex returned "unknown" for 92.6% of fields), weakening the memorization hypothesis.
- By language, Claude reached 100% on Python, 94.4% on Stata, 91.9% on R; Codex struggled most with Stata (38.9% failure).
- Agents inferred underlying **research questions** at 73.5% (Claude) and 70.0% (Codex) semantic match, evidencing abstraction from code/data alone.
- **PDF provision** modestly raised overall accuracy but cut non-reproducible task accuracy sharply (Claude 100→63.3%; Codex 100→90%).
- **Confirmatory nudging** raised Codex overall accuracy (62.1→74.1%) but further eroded non-reproducible accuracy (Claude 100→70%; Codex 90→60%), evidencing sycophantic specification search.
- On the **anonymized CORE-Bench** social science subset, the SocSci-Repro-Bench hierarchy replicated; non-anonymized CORE-Bench yielded 100% for both, suggesting prior benchmarks conflate retrieval with reproduction.

## Connections

This work sits in the computational-methods-and-LLMs cluster alongside studies probing LLM reliability and bias in research pipelines — most directly [[DeVerna2025-dl]] on LLM susceptibility to misinformation prompts and [[Bouchaud2026-lr]] on benchmarking LLM-based measurement, both of which similarly stress prompt-sensitivity and validation under adversarial or leading conditions. It also speaks to broader debates on using LLMs as research instruments raised in works like [[Le-Mens2025-qz]] and [[Balluff2026-if]], where the question of whether model outputs reflect genuine inference versus pattern retrieval is central. None of the other listed papers focus specifically on agentic reproduction of scientific results, so the intellectual link is to the wider methodological-trust thread rather than to direct precursors.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Alizadeh2026-es.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-ai-agents-replicate-science/id1866587707?i=1000772806829)
