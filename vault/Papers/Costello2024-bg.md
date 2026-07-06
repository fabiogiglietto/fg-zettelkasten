---
title: "Durably reducing conspiracy beliefs through dialogues with AI"
aliases: ["Durably reducing conspiracy beliefs through dialogues with AI"]
authors: ["Thomas H Costello", "Gordon Pennycook", "David Gertler Rand"]
year: 2024
doi: 10.31234/osf.io/xcwdn
bibtex_key: Costello2024-bg
topics: [generative-ai-media, information-disorder]
citation_count: 12
open_access: false
source_url: https://doi.org/10.31234/osf.io/xcwdn
podcast_url: 
pdf_available: true
discovery_date: 2024-09-15T00:00:00Z
---

# Durably reducing conspiracy beliefs through dialogues with AI

> Costello, T. H., Pennycook, G., & Rand, D. G. (2024). Durably reducing conspiracy beliefs through dialogues with AI. *Science*, *385*, eadq1814. https://doi.org/10.31234/osf.io/xcwdn
>
> [View paper](https://doi.org/10.31234/osf.io/xcwdn)

## Summary

This paper tests whether personalized, evidence-based dialogues with GPT-4 Turbo can durably reduce belief in conspiracy theories. Across two preregistered experiments with roughly 2,190 American conspiracy believers, a three-round AI conversation tailored to each participant's stated conspiracy and supporting evidence reduced belief in the focal conspiracy by about 20%, an effect that persisted at least two months and generalized to unrelated conspiracies and to behavioral intentions. The authors argue the findings challenge motivational accounts that frame conspiracy beliefs as impervious to counterevidence, suggesting instead that sufficiently compelling, tailored evidence — at a level of depth previously impractical at scale — can shift even entrenched beliefs, vindicating analytic-reasoning models of belief revision.

## Key Contributions

- Empirical evidence against the view that conspiracy beliefs are inherently resistant to facts.
- A scalable AI-based intervention that produces durable, generalizing reductions in conspiracy belief.
- A methodological pipeline for embedding real-time, personalized LLM dialogues inside survey experiments, allowing open-ended elicitation and adaptive treatment.
- A public Conversation Browser and dataset of human–AI debunking dialogues.
- A concrete demonstration of the prosocial potential — and, by symmetry, the persuasive risks — of frontier LLMs.

## Methods

Two preregistered online experiments (Study 1 n=1,055; Study 2 n=2,286, plus a Lucid replication) recruited US adults via CloudResearch with census quota matching. Participants described in their own words a conspiracy they believed and the evidence for it; GPT-4 Turbo produced a one-sentence summary that they rated on a 0–100 belief scale. Participants were randomized (~60/40) to either a treatment dialogue in which the LLM was prompted to persuade them against their belief, or a control dialogue on an unrelated topic, across three rounds (~8.4 minutes). Outcomes included re-rated focal belief, a modified Belief in Conspiracy Theories Inventory, and (in Study 2) behavioral intentions and trust. Study 1 added 10-day and 2-month follow-ups. NLP clustering, GAMs, and causal forests probed heterogeneity, and a professional fact-checker audited 128 representative AI claims.

## Findings

- Treatment cut focal-conspiracy belief by ~20% on average (Study 1 d=1.15; Study 2 d=0.79); about 27% of treated participants moved below the scale midpoint.
- Effects were undiminished at 10-day and 2-month follow-ups.
- Reductions held across 12 distinct conspiracy clusters, including 2020 election fraud and COVID-19, with no significant differences by topic.
- Effects persisted among participants with maximally strong prior belief, high worldview-importance ratings, or top-decile conspiratorial ideation.
- Spillover: belief in unrelated BCTI conspiracies fell ~8% (~12% among initially believed items) and persisted at 2 months; intentions to unfollow conspiracy posters and to argue with believers rose.
- The AI did *not* reduce belief in true conspiracies (e.g., MK Ultra), with a directionally positive effect significantly different from the false-conspiracy effects.
- Fact-checking: 99.2% of AI claims true, 0.8% misleading, 0% false, with no detectable partisan bias.
- Trust in generative AI and in institutions were the most consistent moderators, both amplifying treatment effects.

## Connections

This paper sits at the intersection of debunking/correction research and the emerging literature on LLMs as persuasive agents; it is closely related to work on inoculation and conspiracy-belief interventions such as [[van-der-Linden2026-jt]] and [[Spampatti2026-kx]], and to studies of LLM persuasion and political messaging like [[Hackenburg2025-dj]]. It also speaks to broader debates on the real-world prevalence and dynamics of misinformation exposure addressed in [[Budak2024-ef]] and [[Gonzalez-Bailon2024-rq]], and to fact-checking and correction-effectiveness work represented by [[Cazzamatta2026-lo]] and [[DeVerna2025-dl]].
