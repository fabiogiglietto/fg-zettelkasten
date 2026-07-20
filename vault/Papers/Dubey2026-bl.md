---
title: "Investigating perceived trust and utility of balanced news chatbots among individuals with varying conspiracy beliefs"
aliases: ["Investigating perceived trust and utility of balanced news chatbots among individuals with varying conspiracy beliefs"]
authors: ["Shreya Dubey", "Paul E. Ketelaar", "Tilman Dingler", "Hannah K. Peetz", "Hein T. van Schie"]
year: 2026
doi: 10.1016/j.chb.2026.108920
bibtex_key: Dubey2026-bl
topics: [climate-and-misinformation-message-interventions, survey-methodology-validity]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1016/j.chb.2026.108920
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Dubey2026-bl.mp3
pdf_available: true
discovery_date: 2026-01-15T00:00:00Z
---

# Investigating perceived trust and utility of balanced news chatbots among individuals with varying conspiracy beliefs

> Dubey, S., Ketelaar, P. E., Dingler, T., Peetz, H. K., & van Schie, H. T. (2026). Investigating perceived trust and utility of balanced news chatbots among individuals with varying conspiracy beliefs. *Computers in Human Behavior*, 108920. https://doi.org/10.1016/j.chb.2026.108920
>
> [View paper](https://doi.org/10.1016/j.chb.2026.108920)

## Summary

This paper investigates whether "balanced news chatbots" — conversational agents that present an equal mix of mainstream and alternative/conspiratorial perspectives on a contested issue — are accepted by users who differ in conspiracy belief. The authors built a custom chatbot called "Infobot" that serves climate-change article headlines split evenly between mainstream and conspiratorial framings, then applied an adapted Technology Acceptance Model (TAM) across two preregistered studies. Their central and counterintuitive finding is that people with *higher* conspiracy beliefs — both generic and climate-specific — rated the chatbot more positively, trusted it more, and were more inclined to use it than people with lower conspiracy beliefs. This challenges the widespread assumption that conspiracy-minded users reflexively reject counter-attitudinal or "balanced" information sources.

## Key Contributions

- Extends the Technology Acceptance Model to balanced news chatbots, identifying **trust** and **perceived usefulness** as the dominant drivers of adoption.
- Provides empirical evidence that conspiracy-believing users can respond favorably to tools offering diverse information, complicating theories of motivated reasoning and reactance.
- Introduces and tests a working prototype ("Infobot") as a depolarization / bubble-piercing intervention.
- Reframes echo-chamber debates by suggesting mainstream-believing users may themselves resist balanced exposure.
- Delivers a replicated SEM model with preregistration and open materials via OSF.

## Methods

Two preregistered online survey experiments with US panel participants. Infobot (built with Rasa + web front-end) presented eight climate headlines — four mainstream, four alternative/conspiratorial — in a randomized carousel, requiring participants to read at least four summaries. Study 1 (n=177) split groups via the Generic Conspiracist Beliefs Scale; Study 2 (n=58) used a self-constructed 4-item climate-specific conspiracy scale (α=.83). TAM constructs (ease of use, usefulness, perceived risks, trust, attitude, intention) were measured on 7-point Likert scales. Analysis used structural equation modeling (lavaan, robust ML) with CFI/RMSEA/SRMR fit indices, Welch's t-tests for group comparisons, and exploratory analysis of article selection and reading times.

## Findings

- Perceived usefulness (β=.64 / .80) and trust (β=.35 / .40) significantly predicted attitude, explaining ~91% of variance; ease of use and perceived risks were non-significant.
- Attitude strongly predicted intention to use (β=.98 / .97), explaining 94–96% of variance.
- Higher-conspiracy participants reported significantly greater trust (5.48 vs. 4.39; 5.54 vs. 4.54), more positive attitudes, and stronger usage intentions than lower-conspiracy participants.
- Higher-conspiracy participants were more politically conservative in both studies; Study 1 found no group difference in belief in anthropogenic climate change.
- Study 1: participants overall read more mainstream articles, but high-conspiracy participants spent less time reading several of them, hinting at selective engagement. Study 2: participants read more alternative articles overall, with no reading-time differences.
- A negatively worded trust item cross-loaded onto perceived risk and was dropped to improve fit.

## Connections

This work sits alongside other interventions aimed at conversational persuasion and correction of misinformation, most directly the LLM-based dialogue approaches in [[Costello2024-bg]] and [[Hackenburg2025-dj]], which similarly probe whether AI agents can shift attitude-incongruent beliefs. Its climate-misinformation framing links it to inoculation and message-intervention research such as [[Spampatti2026-kx]] and [[van-der-Linden2026-jt]], and its finding that conspiracy believers engage rather than reject balanced tools speaks to debates about selective exposure explored in [[DeVerna2025-dl]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Dubey2026-bl.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-investigating-perceived-trust-and/id1866587707?i=1000745538358)
