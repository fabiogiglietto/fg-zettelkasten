---
title: "What 81,000 people told us about the economics of AI"
aliases: ["What 81,000 people told us about the economics of AI"]
authors: []
year: 
doi: 
bibtex_key: UnknownUnknown-db
topics: []
citation_count: 0
open_access: false
source_url: https://scholar.google.com/scholar?q=What%2081%2C000%20people%20told%20us%20about%20the%20economics%20of%20AI
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/UnknownUnknown-db.mp3
pdf_available: true
discovery_date: 2026-05-20T18:37:02.902736Z
---

# What 81,000 people told us about the economics of AI

## Summary

This Anthropic Economic Index report analyzes open-ended survey responses from roughly 81,000 Claude.ai users to map how workers perceive AI's effects on their jobs and productivity. Using Claude itself as a classifier to extract occupation, career stage, productivity gains, and displacement concerns from free-form text, the authors link these self-reports to a behavioral measure of occupational AI exposure. The central argument is that workers' intuitions about AI threat track actual usage patterns: occupations with higher observed AI penetration show more displacement anxiety, while productivity benefits — dominated by scope expansion rather than mere speed — are distributed unevenly, with a U-shaped wage profile and concentrated gains for entrepreneurs and technical workers.

## Key Contributions

- Couples qualitative worker sentiment with a quantitative, usage-derived measure of occupational AI exposure.
- Demonstrates an LLM-classifier pipeline for converting open-ended responses into structured economic variables (occupation, career stage, productivity type, beneficiary).
- Provides early evidence that worker anxiety is calibrated to real AI diffusion at the occupational level.
- Documents heterogeneity in productivity gains across the wage distribution, including unexpected benefits for some low-wage users running side ventures.
- Surfaces a U-shaped relationship between self-reported speedup and displacement concern as a hypothesis for further study.

## Methods

The authors analyze 80,508 personal Claude.ai survey responses, using Claude-powered classifiers to infer occupation, career stage, and productivity-related attributes from free text. Productivity is coded on a 1–7 scale with anchored examples. Inferred occupations are linked to an "observed exposure" measure (share of an occupation's tasks performed by Claude) drawn from prior work by Massenkoff and McCrory. Robustness checks restrict analysis to the ~11% of respondents who explicitly stated their occupation. Key results come from cross-tabulating perceived job threat against exposure quartile, career stage, and speedup level.

## Findings

- About 20% of respondents voiced concern about economic displacement from AI.
- A 10-percentage-point rise in occupational exposure corresponds to a 1.3-point rise in perceived job threat; the top exposure quartile mentions threat three times as often as the bottom.
- Mean self-reported productivity is 5.1 ("substantially more productive"); only 3% report negative or neutral effects, while 42% give no clear signal.
- Management (largely solopreneurs) and computer/math occupations report the highest gains; scientific and legal professions the mildest.
- Scope expansion is cited by 48% of respondents discussing productivity, ahead of speed (40%); quality and cost benefits trail.
- Early-career workers report personal benefit less often than senior workers (60% vs. 80%) and express more displacement anxiety.
- Around 10% of respondents naming a beneficiary believe employers or clients are capturing the gains via increased work demands.
- The reported-speedup vs. job-threat relationship is U-shaped: both those slowed by AI and those most accelerated by it express the greatest displacement concern.

## Connections

No related papers were provided under shared topics, so there are no internal links to make here. The work sits adjacent to task-based AI exposure literatures (e.g., the Massenkoff and McCrory measure it borrows) and to broader debates on AI's labor-market incidence and surplus distribution.

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/UnknownUnknown-db.mp3)
