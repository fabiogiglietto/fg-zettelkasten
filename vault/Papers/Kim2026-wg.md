---
title: "Targeted digital voter suppression efforts likely decrease voter turnout"
aliases: ["Targeted digital voter suppression efforts likely decrease voter turnout"]
authors: ["Young Mie Kim", "Ross Dahlke", "Hyebin Song", "Richard Heinrich"]
year: 2026
doi: 10.1073/pnas.2519944123
bibtex_key: Kim2026-wg
topics: [digital-media-elections-global, information-disorder]
citation_count: 0
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

This paper offers the first independent, individual-level empirical analysis of targeted digital voter suppression during the 2016 US Presidential Election, including ads later attributed to Russia's Internet Research Agency. Combining a custom browser-based ad tracking tool (EScope) with survey responses and verified turnout records, the authors document systematic geo-racial targeting of suppression ads at non-White voters in minority-majority counties of battleground states, and estimate that exposure was associated with reduced turnout — modest on average (~1.86 percentage points) but substantial (~17%) among the precisely targeted subpopulations. The authors argue that prior null findings on Russian interference reflect methodological limits of average treatment effect designs and indirect exposure proxies, and that heterogeneous effects are essential to understanding microtargeted political advertising.

## Key Contributions

- First independent, individual-level empirical documentation of digital voter suppression targeting and turnout effects, free from reliance on platform or government data.
- Methodological framework integrating real-time user-side ad capture, survey data, and verified voter file turnout records, bypassing both platform opacity and self-report bias.
- Reframes microtargeting research around heterogeneous treatment effects, showing how ATE-only designs can obscure real-world impacts on small targeted segments.
- Empirical evidence that undisclosed (including foreign) campaigns exploit the absence of disclosure rules to suppress turnout among racial minorities in pivotal jurisdictions.
- Public replication materials and an archived dataset (ICPSR) for downstream research on targeted political advertising.

## Methods

EScope, a browser-based ad-tracking tool, was deployed for roughly six weeks before the November 2016 election to a GfK Knowledge Panel sample (~13,500 consenting; 10,441 baseline survey completers) representative of the US voting-age population. A validated dictionary (Krippendorff's α = 0.93) identified four suppression ad categories — election boycott, deception, third-party promotion, and same-side candidate attack — yielding 59,771 suppression ads. Exposure was linked to verified turnout via TargetSmart voter files. Targeting was tested with hierarchical linear models; turnout effects were estimated via entropy balancing on 35 covariates with PU-learning for missing labels, plus exact and CBPS full matching, false-shock tests, sensitivity analyses for unobserved confounders, and 2012 placebo tests.

## Findings

- Non-Whites in minority counties of battleground states received disproportionately more suppression ads, controlling for income, education, and party ID (HLM interaction b = 0.24, p = 0.04).
- Exposure was associated with a 1.86-point lower turnout (67.75% → 65.89%; Cohen's d = 0.059), implying roughly 4.7 million fewer votes nationally.
- Among non-Whites in minority counties of battleground states, exposure tracked a 17.3% lower turnout (d ≈ −0.515); the gap versus unexposed Whites in non-minority, non-battleground counties reached 14.2%.
- Non-suppression political ad exposure was associated with *higher* turnout, distinguishing suppression from generic mobilization effects.
- Results were robust across counterfactual specifications, matching strategies, confounder sensitivity, and 2012 placebo tests.

## Connections

This work speaks directly to research on foreign influence operations and their measured effects, complementing platform-data studies such as [[DeVerna2025-dl]] and [[Bollenbacher2026-vz]] by offering an alternative, user-side measurement strategy that challenges the prevailing null-effects consensus on IRA impact. It connects to broader work on the limited but heterogeneous reach of disinformation and political ads (e.g., [[Budak2024-ef]], [[Gonzalez-Bailon2024-rq]]) by arguing that average effects mask consequential targeted harms, and resonates with scholarship on platform-mediated harms to marginalized communities such as [[Marwick2025-ov]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kim2026-wg.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-digital-voter-suppression-how-microtargeting/id1866587707?i=1000747664390)
