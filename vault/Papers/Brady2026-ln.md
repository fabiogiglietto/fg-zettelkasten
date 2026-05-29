---
title: "Redesigning algorithms to intervene on social norm misperceptions during a national election"
aliases: ["Redesigning algorithms to intervene on social norm misperceptions during a national election"]
authors: ["William J. Brady", "Meriel Doyle", "Abdo Elnakouri", "Eli J. Finkel", "Joshua Conrad Jackson", "Nour Kteily", "Victoria Parker", "Curtis Puryear", "Trevor Spelman", "Jacob Teeny", "Mark Torres"]
year: 2026
doi: 10.1038/s41586-026-10536-1
bibtex_key: Brady2026-ln
topics: [climate-and-political-messaging-effects, polarization-partisanship-hyperpartisan-media]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1038/s41586-026-10536-1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Brady2026-ln.mp3
pdf_available: true
discovery_date: 2026-05-29T05:48:08.354531Z
---

# Redesigning algorithms to intervene on social norm misperceptions during a national election

## Summary

This Registered Report presents a large-scale Bluesky field experiment during the 2024 US presidential election in which 2,000 US partisans were randomly assigned for eight weeks to one of three custom feed-ranking algorithms: an engagement-based feed mimicking major platforms, a reverse-chronological control, and a newly designed "diversified extremity" algorithm that down-weights extreme political users. The authors argue that engagement-based ranking amplifies intergroup, moralized and emotional (IME) content, which in turn distorts users' perceptions of social norms around political dialogue and inflates perceived partisan animosity. Reframing the algorithm-and-polarization debate away from echo chambers and toward an algorithm-mediated social-learning account, they show that a prosocial alternative algorithm can meaningfully reduce IME exposure and improve norm accuracy without sacrificing platform enjoyment.

## Key Contributions

- One of the first industry-independent, large-scale field experiments with full researcher control over a live platform's feed-ranking algorithm, executed on Bluesky's open infrastructure.
- Introduces and empirically tests a novel "diversified extremity" ranking algorithm as a scalable intervention against algorithmic distortion of norm perceptions.
- Develops an algorithm-mediated social-learning theory in which misperceived norms — not selective exposure or direct attitude change — are the central pathway from ranking algorithms to partisan animosity.
- Provides a preregistered causal test of engagement-based ranking's effects on IME exposure, norm accuracy, animosity, and behaviour around a major political event.
- Releases a replicable methodological template (custom Bluesky feeds, LLM content classification, weekly norm/animosity surveys) that does not require industry partnerships.

## Methods

A preregistered, 3-condition between-subjects field experiment recruited 2,000 active US partisan Bluesky users (Democrats and Republicans) across two waves spanning September–December 2024. The team built three custom feeds on Bluesky: an ML-based engagement-prediction algorithm with approximate nearest-neighbour retrieval, a diversified extremity algorithm combining filters for super-poster suppression, toxicity reduction, and constructive-dialogue promotion, and a reverse-chronological control. Roughly 20 million firehose posts were classified for intergroup, moral and emotional content using fine-tuned and prompt-tuned LLMs, and for toxicity/constructiveness via Perspective API. Weekly surveys captured descriptive and prescriptive norms, in/outgroup dislike, platform enjoyment, sectarianism, and issue-attitude extremity, analyzed with generalized linear mixed models including pre/post-election interactions and powered for d = 0.20.

## Findings

- Engagement-based feeds amplified aggregate IME content by 5.1% pre-election and 23.1% post-election relative to reverse-chronological, with moral outrage up to +79.2% and political content up to +57.3% post-election.
- Toxic content rose 13–17% and negative emotional content 7.6–14.7% under engagement-based ranking, while positive emotional content fell 2.5–11.4%.
- The diversified extremity algorithm cut aggregate IME content by ~6–7% versus engagement-based feeds and consistently reduced moral outrage, toxicity, and political content.
- Engagement-based feeds reduced prescriptive norm accuracy by ~5 scale points, but unexpectedly users *underestimated* peer permissiveness for toxic political content.
- Post-election, engagement-based feeds raised perceived outgroup dislike (~4.5 pts) and ingroup dislike (~3.5 pts); diversified extremity improved prescriptive norm accuracy but did not significantly move animosity.
- Neither algorithm significantly shifted users' own engagement with IME or toxic content; bounding analyses ruled out large effects but not small ones.
- Toxic engagement was extraordinarily concentrated: only 13.6% of participants ever engaged with toxic content, and the top 5% produced 75% of such engagement (Gini = 0.93).
- Post-election, engagement-based feeds reduced overall Bluesky enjoyment, whereas the diversified extremity condition preserved or improved enjoyment despite slightly less-enjoyable rated content.
- Exploratory tests showed only small, non-significant rises in political sectarianism and no detectable change in issue-attitude extremity over eight weeks.

## Connections

This paper directly engages the literature on whether feed-ranking algorithms drive polarization, most notably the 2020 Facebook/Meta collaborations represented here by [[Bakshy2015-rn]], and connects to broader work testing depolarization interventions such as [[Voelkel2026-lc]]. Its focus on misperceived norms and toxic-content dynamics resonates with research on hyperpartisan and toxic information environments like [[Mosleh2024-op]] and [[Efstratiou2025-gs]], while its emphasis on prosocial algorithmic design as an alternative to engagement maximization complements platform- and exposure-focused studies including [[Allcott2025-jb]] and [[Green2025-ap]].

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Brady2026-ln.mp3)
