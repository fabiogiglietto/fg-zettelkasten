---
title: "Targeted digital voter suppression efforts likely decrease voter turnout"
aliases: ["Targeted digital voter suppression efforts likely decrease voter turnout"]
authors: ["Young Mie Kim", "Ross Dahlke", "Hyebin Song", "Richard Heinrich"]
year: 2026
doi: 10.1073/pnas.2519944123
bibtex_key: Kim2026-wg
topics: [political-communication-elections]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1073/pnas.2519944123
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kim2026-wg.mp3
pdf_available: true
discovery_date: 2026-02-02T06:36:34.699078Z
---

# Targeted digital voter suppression efforts likely decrease voter turnout

> Kim, Y. M., Dahlke, R., Song, H., & Heinrich, R. (2026). Targeted digital voter suppression efforts likely decrease voter turnout. *Proceedings of the National Academy of Sciences*, *123*, e2519944123. https://doi.org/10.1073/pnas.2519944123
>
> [View paper](https://doi.org/10.1073/pnas.2519944123)

## Summary

This study offers the first systematic, individual-level empirical documentation of targeted digital voter suppression advertising during the 2016 US Presidential Election, including ads later attributed to Russia's Internet Research Agency (IRA). Rather than relying on indirect exposure proxies or self-reported behavior—the methodological choices the authors argue produced prior null findings on Russian interference—the team directly measured individual ad exposure with a custom browser tracking tool, then linked that exposure to survey responses and verified voter turnout records. They document clear geo-racial targeting and an association between exposure and reduced turnout, with the sharpest declines concentrated precisely among the most heavily targeted voters. The core methodological argument is that average treatment effects obscure the real-world consequences of microtargeting; heterogeneous effects on targeted subpopulations are where the damage lives.

## Key Contributions

- First independent, individual-level empirical evidence on digital voter suppression targeting and its turnout effects, obtained without reliance on governments or platform companies.
- A methodological framework combining user-based real-time ad tracking (EScope), survey data, and verified turnout records to circumvent platform data-access limits and self-report bias.
- A demonstration that heterogeneous treatment effects are essential in microtargeting research, challenging the field's reliance on average treatment effects.
- Documentation of undisclosed campaigns—including foreign interference—exploiting microtargeting in the absence of disclosure requirements, with normative implications for election integrity.
- Publicly archived data and replication materials via ICPSR.

## Methods

The authors deployed EScope, a user-based browser tool that captures ads and metadata in real time, to a GfK KnowledgePanel sample (~13,500 consenting participants, 10,441 completing baseline surveys) resembling the US voting-age population over roughly six weeks before the November 2016 election. A dictionary-based classifier identified four voter suppression ad types (election boycott, deception, third-party promotion, same-side candidate attack), validated by human coders (Krippendorff's α = 0.93), yielding 59,771 suppression ads. Individual exposure was linked to geographic context (minority-majority counties, battleground states with <5% margins) and to verified turnout records matched via TargetSmart voter files. Analyses used Hierarchical Linear Models for targeting patterns and entropy balancing with 35 covariates for average and heterogeneous treatment effects, with PU-learning to impute missing turnout labels. Robustness checks included exact and full matching (CBPS), unobserved-confounder sensitivity analyses, false-shock tests, and 2012 placebo tests.

## Findings

- Non-White voters in minority counties of battleground states received significantly more suppression ads even after controlling for income, education, and party ID (HLM interaction b = 0.24, p = 0.04).
- Exposure was associated with a 1.86 percentage-point lower turnout (67.75% vs 65.89%; Cohen's d = 0.059), roughly 4.7 million fewer votes nationally.
- Among non-Whites in minority counties of battleground states, exposure was associated with a 17.3% lower turnout (d ≈ -0.515); the gap versus unexposed Whites in non-minority, non-battleground counties reached 14.2%.
- Non-suppression political ad exposure was associated with *increased* turnout, distinguishing suppression effects from generic political advertising.
- Results held across multiple counterfactual comparisons, confounder sensitivity analyses, 2012 placebo tests, and alternative matching techniques.

## Connections

This paper's argument that microtargeted political manipulation demands direct exposure measurement and attention to heterogeneous effects speaks to broader work on coordinated influence operations and their measurable reach, such as [[Luceri2025-tr]] and [[Pierri2025-hm]]. Its focus on foreign interference and information disorder around US elections connects it to work on manipulation campaigns and their contested effects, including [[DeVerna2025-dl]] and [[Starbird2025-jj]]. The turnout-suppression framing also relates to studies of targeted political advertising and audience effects more broadly, such as [[Votta2025-xz]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kim2026-wg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-digital-voter-suppression-how-microtargeting/id1866587707?i=1000747664390)
