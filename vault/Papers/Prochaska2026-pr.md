---
title: "New election, same old story: How tropes form a grammar of election rumors"
aliases: ["New election, same old story: How tropes form a grammar of election rumors"]
authors: ["Stephen Prochaska", "Mert Bayar", "Ashlyn B. Aske", "Joseph Schafer", "Kate Starbird"]
year: 2026
doi: 
bibtex_key: Prochaska2026-pr
topics: [information-disorder-disinformation-narratives, conspiracy-narratives-in-media]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2610.37804v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Prochaska2026-pr.mp3
pdf_available: true
discovery_date: 2026-10-31T11:46:16.787064Z
---

# New election, same old story: How tropes form a grammar of election rumors

> Prochaska, S., Bayar, M., Aske, A. B., Schafer, J., & Starbird, K. (2026). New election, same old story: How tropes form a grammar of election rumors. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2610.37804v1)

## Summary

This paper argues that online election rumors — which feel chaotic, overwhelming, and endlessly novel — are in fact built from a stable, recurring repertoire of narrative tropes. Analyzing 568 distinct rumors drawn from 34.2 million tweets across the 2020 and 2022 U.S. elections, the authors develop a three-tiered hierarchical framework (Meta-category → Meso-trope → Micro-trope) for cataloguing these tropes, and they identify a "grammar" of election rumors in which most rumors combine an **Actor**, an **Object**, and an **Action**, with optional **Scene & Setting** and **Suggested Remedies** components. Drawing on narrative and folklore theory (Propp, Eco, de Certeau, Tangherlini), the framework is offered as a reusable information architecture that lets researchers, communicators, and election officials rapidly identify, diagnose, and anticipate emerging rumors.

## Key Contributions

- A hierarchical three-tier (Meta/Meso/Micro) framework for organizing election-rumor tropes by narrative function.
- The identification of a "grammar" of election rumors specifying how Actor, Object, and Action combine (with optional Scene & Setting and Suggested Remedies).
- An enumerated codebook plus empirical co-occurrence network analysis usable as a reusable architecture for studying past, present, and future rumors.
- Practical guidance for detection, prebunking, and election-official communication, including human-in-the-loop and gamified approaches.
- A methodological demonstration of combining LLM-assisted rumor summarization with expert qualitative coding at scale.

## Methods

A mixed-methods, multi-step design combining qualitative coding with computational tools. The dataset merges two prior Twitter corpora — a 2020 presidential corpus (~32.4M tweets, 455 rumors) and a 2022 midterm corpus (~1.8M tweets, 135 rumors) — yielding 568 in-scope rumors after exclusions. Coding was conducted at the rumor level (collections of tweets, not individual tweets). The team used ChatGPT 4.1 mini for two-step hierarchical summaries of up to 1,000 tweets per rumor (500 most-retweeted plus 500 random), supplemented by word clouds and tweet samples, to surface actors, claims, and actions. Expert coders developed the three-tier scheme through iterative inductive open coding, calibrating on a shared set of 50 rumors; each rumor was double-coded with third-coder arbitration and group consensus for difficult cases. Quantitative analysis examined code frequencies and micro-trope co-occurrence using Jaccard similarity (threshold .1) and Louvain community detection.

## Findings

- A nested framework of six meta-categories (Actor, Actor-Action, Object, Object-Action, Scene & Setting, Suggested Remedies) with meso- and micro-tropes (e.g., villains/heroes/victims, foreign interference, hacked machines, white vans, swing states).
- Actors appeared in over 96% of rumors (100% of proper-grammar rumors), confirming them as a core component.
- Scene & Setting appeared in ~74.8% and Suggested Remedies in ~70.8% of rumors, indicating rumors are action-oriented and contextually elaborated.
- ~69.9% (397) of rumors conformed to the Actor-Object-Action "proper grammar"; ~30.1% (171) were missing a core element — most often the Object (57.9% of improper cases), typically because objects were implied rather than central.
- Co-occurrence networks revealed distinct but fuzzy sub-narrative clusters: a central cluster (Democrats as villains, urban centers, swing states, Republicans as victims, calls for audits/recounts/litigation) plus clusters on media/big-tech distrust, voting-machine manipulation, offsite counting, voter intimidation, and mail-in fraud.
- The central cluster drew tropes from every meta-category, reinforcing tropes as combinable building blocks; categories rarely appear in isolation.
- Suggested Remedies function as the rumor's "moral," revealing political-strategic goals such as voter ID laws and abolishing machines or mail-in voting.

## Connections

This paper extends the authors' own prior work on collaborative and participatory election rumoring; see [[Starbird2025-jj]], [[Prochaska2025-ef]], and [[Starbird2019-qv]]. Its trope-and-grammar account of how familiar narratives are recombined connects to actant- and narrative-based analyses of conspiracy and disinformation such as [[Grusauskaite2026-po]] and [[Marwick2025-ov]], and its methodological use of LLM-assisted summarization relates to computational rumor and misinformation-detection studies like [[Kansaon2025-id]] and [[Wack2026-bt]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Prochaska2026-pr.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
