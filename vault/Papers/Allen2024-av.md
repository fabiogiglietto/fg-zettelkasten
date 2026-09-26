---
title: "Quantifying the impact of misinformation and vaccine-skeptical content on Facebook"
aliases: ["Quantifying the impact of misinformation and vaccine-skeptical content on Facebook"]
authors: ["Jennifer Allen", "Duncan J. Watts", "David G. Rand"]
year: 2024
doi: 10.1126/science.adk3451
bibtex_key: Allen2024-av
topics: [misinformation-exposure-recalibration, health-misinformation-infodemic]
citation_count: 130
open_access: false
source_url: https://doi.org/10.1126/science.adk3451
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445514Z
---

# Quantifying the impact of misinformation and vaccine-skeptical content on Facebook

> Allen, J., Watts, D. J., & Rand, D. G. (2024). Quantifying the impact of misinformation and vaccine-skeptical content on Facebook. *Science*, *384*, eadk3451. https://doi.org/10.1126/science.adk3451
>
> [View paper](https://doi.org/10.1126/science.adk3451)

## Summary

This paper asks whether COVID-19 vaccine misinformation on Facebook actually had the ecosystem-scale impact needed to depress US vaccination rates — and delivers a counterintuitive answer. By decomposing societal impact into two multiplicative components, **exposure** (how many people saw content) and **persuasive influence** (how much seeing it changed behavior), the authors show that fact-check-flagged misinformation, though more persuasive per view, reached too few people to matter much in aggregate. Instead, *unflagged but vaccine-skeptical* content — factually accurate yet misleading stories, much of it from credible mainstream outlets — had an estimated 46-fold greater overall impact on vaccine hesitancy. The paper directly challenges the "infodemic" framing that blames viral falsehoods for vaccine refusal, arguing that veracity is the wrong axis for both diagnosis and moderation.

## Key Contributions

- Introduces a scalable **exposure × persuasive-influence** framework for estimating misinformation's societal impact, operationalized with survey experiments, crowdsourcing, and NLP.
- Provides one of the first *causal, ecosystem-scale* estimates of real-world misinformation impact rather than correlational or proxy measures.
- Demonstrates a **crowd-plus-machine-learning pipeline** that generalizes experimental treatment effects to thousands of real-world URLs using minimal platform data.
- Reframes the misinformation debate around factually accurate but misleading "gray-area" content from mainstream sources.
- Offers policy-relevant tooling for continuously flagging high-impact harmful content that veracity-based moderation misses.

## Methods

Two randomized survey experiments on Lucid (combined N = 18,725) measured the causal effect of 130 vaccine-related headlines on a pre-post vaccination-intentions index — study 1 using 40 fact-checker-debunked items, study 2 using 90 highly shared, quality- and topic-balanced articles (both true and false). Crowd raters labeled all 130 headlines on five dimensions (surprising, plausible, partisan lean, familiar, and harmful-vs-helpful to health), which were related to treatment effects via random-effects meta-regressions. To scale up, the authors used Facebook's Social Science One URL Shares dataset to measure actual views for 13,206 vaccine-related URLs (>100 public shares, Jan–Mar 2021). A crowd-machine pipeline had 177 raters predict persuasive effects to build a crowdsourced aggregate score, which a COVID-Twitter-BERT model was trained to predict across all URLs; predicted scores were passed through the meta-regression to estimate per-URL effects. Aggregate impact was computed as per-URL effect × views, normalized per user, with bootstrap confidence intervals.

## Findings

- A single exposure to vaccine misinformation reduced vaccination intentions by **1.5 pp** on average (P = 0.00004), varying widely across items.
- Only the **harmful-to-health** dimension consistently predicted negative persuasive effect (~−0.69 pp per point); veracity was non-significant once harm was controlled.
- Flagged misinformation received only **8.7 million views — 0.3%** of the 2.7 billion vaccine-related URL views; low-credibility domains accounted for just 5.1%.
- A single unflagged *Chicago Tribune* article ("A healthy doctor died two weeks after getting a COVID vaccine") reached ~**54.9 million** people (>20% of US Facebook users); its story cluster drew over six times the views of all flagged misinformation combined.
- The crowdsourced score predicted observed treatment effects well (adjusted r = 0.75); the BERT model reached 97% AUC on a hesitancy-inducing binary task.
- Vaccine-skeptical unflagged content lowered intentions by an estimated **−2.28 pp/user** vs **−0.05 pp** for flagged misinformation — a **46-fold** difference; 98% of hesitancy-inducing views were unflagged.
- Mainstream outlets drove the largest aggregate harm; low-credibility domains contributed only 9.3% of the total estimated decrease.
- The overall effect corresponds to roughly **2.3 pp lower intentions per user**, or an estimated ~3 million fewer vaccinated Americans.

## Connections

This paper is a cornerstone of the argument that misinformation's small *reach* limits its aggregate impact, extending prior exposure-focused work by the same authors such as [[Allen2020-nj]] and [[Allen2021-ai]], and it sits in tension with the persuasion-optimism of [[Vosoughi2018-at]] and the fact-check/accuracy-nudge tradition of [[Pennycook2021-jq]]. Its reframing toward mainstream "gray-area" content and its reliance on Facebook exposure data connect it to platform-ecosystem measurement studies like [[Gonzalez-Bailon2024-rq]] and [[Guess2023-ai]], and to the broader recalibration literature questioning the "infodemic" narrative, including [[Budak2024-ef]] and [[Nyhan2023-gb]].
