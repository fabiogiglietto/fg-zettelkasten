---
title: "How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic"
aliases: ["How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic"]
authors: ["Silke Adam", "Tobias Rohrbach", "Franziska Keller", "Mykola Makhortykh", "Ernesto de León", "Chiara Valli", "Ani Baghumyan", "Maryna Sydorova"]
year: 2026
doi: 10.1093/joc/jqaf033
bibtex_key: Adam2026-tz
topics: [information-disorder-misinformation, health-misinformation-online]
citation_count: 5
open_access: false
source_url: https://doi.org/10.1093/joc/jqaf033
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Adam2026-tz.mp3
pdf_available: true
discovery_date: 2026-05-16T09:10:27.779284Z
---

# How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic

> Adam, S., Rohrbach, T., Keller, F., Makhortykh, M., de León, E., Valli, C., Baghumyan, A., & Sydorova, M. (2026). How do media contribute to the dissemination of conspiracy beliefs? A field study combining panel and web tracking at the outbreak of the COVID-19 pandemic. *Journal of Communication*, *76*, 119–133. https://doi.org/10.1093/joc/jqaf033
>
> [View paper](https://doi.org/10.1093/joc/jqaf033)

## Summary

This study leverages a fortuitously timed two-wave panel survey in Germany and German-speaking Switzerland (March–May 2020), bracketing a web-tracking phase, to examine how *actual* online exposure to conspiracy content combined with political predispositions to shape early COVID-19 conspiracy beliefs. The authors argue that conspiracy belief formation is a "marriage" of media information and predispositions, requiring a holistic model that integrates alternative media (as vectors of contagion), mainstream media (as debunking mitigators), and audience dispositions such as populism and political mistrust. Grounding itself in Zaller's information-plus-predispositions framework and motivated reasoning theory, the paper traces both direct exposure effects and indirect pathways of selective engagement, selective avoidance, reinforcement, and counterarguing.

## Key Contributions

- One of the first real-time, behavioral-tracking studies of conspiracy belief formation at the *onset* of a global crisis, avoiding retrospective and self-report bias.
- Integrates content-level exposure measurement (source *and* stance) with panel measurement of predispositions and beliefs.
- Develops and tests a holistic model uniting alternative media, mainstream media, and predispositions, with selective engagement/avoidance and reinforcement/counterarguing pathways.
- Shows empirically that mainstream debunking works for the general public but can backfire among strong populists.
- Releases methodological infrastructure: the WebTrack browser plugin and fine-tuned German BERT classifiers for conspiracy detection and stance.

## Methods

- Two-wave online panels: Germany (n=573) and German-speaking Switzerland (n=574), quota-sampled, fielded T1 (March 2020) and T2 (May 2020).
- Web tracking via a custom Chrome/Firefox plugin capturing desktop browsing HTML between waves (3,531,606 documents).
- Sentence-level classification using fine-tuned German BERT to detect conspiracy content and supporting/opposing stance, validated against a 498-sentence gold standard (macro F1 = 0.94 detection; 0.78–0.82 stance) and trained on 12,745 manually coded sentences.
- URL-based source classification (mainstream quality/tabloid, hyperpartisan alternative conspiracy media, social platforms).
- Survey scales for populism, political mistrust, and COVID-19 conspiracy beliefs; OLS regression plus bootstrapped mediation (10,000 iterations) on pooled data with country control.

## Findings

- On average 7.2% of visited documents contained conspiracy-related content (~113 documents per participant).
- Conspiracy-*supporting* content was more prevalent than opposing content across all media types — including mainstream media.
- Exposure across sources was positively correlated: most users met conspiracy content across multiple sources, not via single-source selectivity.
- **Contagion:** conspiracy-supporting alternative media exposure increased beliefs (b=0.14, p<.001).
- **Mitigation:** conspiracy-opposing mainstream media exposure decreased beliefs (b=-0.05, p=.001).
- Populism (b=0.38) and political mistrust (b=0.20) directly predicted conspiracy beliefs.
- Populists selectively engaged with conspiracy-supporting alternative media (b=0.76) and avoided conspiracy-opposing mainstream media (b=-0.91).
- Significant reinforcement (via alternative media) and counterarguing/backfire (mainstream debunking increasing populists' beliefs) indirect effects.
- Roughly 25–30% of respondents saw at least some truth in, or were uncertain about, COVID-19 conspiracies.

## Connections

This paper sits alongside other work on health misinformation and inoculation/correction dynamics, notably [[Spampatti2026-kx]] and [[van-der-Linden2026-jt]] on countering conspiracy and misinformation, where the backfire finding among populists is a relevant complication. Its web-tracking approach to measuring actual exposure connects methodologically to behavioral-trace studies such as [[Gonzalez-Bailon2024-rq]] and [[DeVerna2025-dl]], and its populism–conspiracy nexus links to research on alternative and hyperpartisan media audiences like [[Frischlich2025-vn]]. It also shares first-author infrastructure and concerns with [[Rohrbach2026-rc]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Adam2026-tz.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-debunking-backfires-how-covid/id1866587707?i=1000768904634)
