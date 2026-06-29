---
title: "Cross-national information attacks: A two-decade analysis of troll behavior in Korea"
aliases: ["Cross-national information attacks: A two-decade analysis of troll behavior in Korea"]
authors: ["Jaehong Kim", "Hyeonseung Kim", "Jiseon Kim", "Alice Oh", "Thorsten Holz", "Wonjae Lee", "Meeyoung Cha"]
year: 2026
doi: 
bibtex_key: Kim2026-br
topics: [coordinated-inauthentic-behavior, information-disorder]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2606.22785v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kim2026-br.mp3
pdf_available: true
discovery_date: 2026-06-29T08:30:16.580141Z
---

# Cross-national information attacks: A two-decade analysis of troll behavior in Korea

> Kim, J., Kim, H., Kim, J., Oh, A., Holz, T., Lee, W., & Cha, M. (2026). Cross-national information attacks: A two-decade analysis of troll behavior in Korea. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2606.22785v1)

## Summary

This paper develops an explainable, hierarchical machine learning pipeline to detect suspected state-linked troll accounts in South Korean news comment sections, then applies it to a near-two-decade corpus (2006–2025) of 112 million Naver News comments from 4 million users. Bootstrapping from 70 officially identified troll seeds, the authors flag 23,998 suspected troll accounts and characterize their behavior over time. The central empirical claim is that these accounts rely far more on morally *condemning* rhetoric — especially condemnation of South Korea and its political leaders across the ideological spectrum — than on overt praise of foreign actors, and that this condemning content is disproportionately amplified under engagement-based ranking. The paper frames the work within cognitive-warfare research and argues that span-level explainability is essential for auditable moderation.

## Key Contributions

- A near-two-decade longitudinal dataset of 112M Korean news comments anchored to verified troll seeds, released publicly for influence-operations research.
- A theory-grounded, three-level hierarchical detector (foreign-state origin → moral-emotional framing → target country) that outputs both class labels and span-level rationales, distilled into a ~0.1B-parameter Korean PLM for scalable inference.
- Empirical mapping of multi-year influence-operation strategy: election-timed account influxes, dominance of condemning over praising rhetoric, and visibility advantages for moral condemnation of domestic elites.
- Operational handoff of the suspected-troll account list to Naver and the Korean Institute for National Security Strategy, with privacy safeguards.

## Methods

The authors expand from 70 known troll seeds through follow-network ties and shared-article co-commenting to build a candidate pool, then human-annotate 1,452 comments (with span-level rationales) under a three-tier scheme grounded in moral-emotion theory: (L1) foreign-state-suspected, (L2) other-condemning vs. other-praising, (L3) target country (Korea, MNS, Partner, Rival, Unknown). GPT-4.1 is fine-tuned on these labels and used to annotate ~50K additional comments, whose labels are then distilled into a KcELECTRA-based ensemble of 18 binary, multi-label, and BIO-tagging classifiers. A user-level XGBoost model combines 14 aggregated content-probability features with 10 behavioral/metadata features (follow ties, self-duplication, engagement) and is trained on 70 known trolls vs. 81 verified non-trolls. Validation uses SHAP, temporal-synchronization tests against known trolls, Welch's t-tests, and fractional logit regressions of like-ratio on rhetorical intensity with year/month fixed effects.

## Findings

- User-level detector reaches F1 = 0.94; flagged accounts (0.59% of users) show daily/weekly/monthly posting synchronization with known trolls (r ≈ 0.81–0.85), significantly above non-trolls.
- Detected trolls produce troll-class content at 67% vs. 22% for non-trolls and use MNS-language tokens at 53% vs. 5%, supporting the labels' validity.
- "Condemning Korea" is the dominant rhetorical mode across 2006–2025, peaking in 2018 around the THAAD dispute and MNS military-civil fusion period.
- New troll-like account creation spikes around elections (+51% weekly influx, p<0.01), with the largest surge around the May 2017 presidential election.
- Only "Condemning Korea" exceeds the 0.5 like-ratio threshold (mean 0.514); fractional logit shows its intensity positively predicts visibility (β=0.109), while praising MNS (β=−1.09) and condemning Rival (β=−0.51) suppress engagement.
- High-visibility condemnation targets political leaders from *both* ideological camps (Moon, Lee, Yoon, Cho), consistent with polarization amplification rather than partisan promotion.

## Connections

This work fits squarely within the coordinated inauthentic behavior detection literature, complementing network- and behavior-based detection approaches such as [[Luceri2025-tr]], [[Minici2024-tf]], and [[Mannocci2025-ig]] by adding theory-grounded, span-level content explainability. Its finding that influence operations amplify polarization by attacking domestic elites across the ideological spectrum resonates with [[DeVerna2025-dl]] and [[Bollenbacher2026-vz]] (read: [[Bollenbacher2026-vz]]) on the downstream effects of inauthentic activity, and with broader accounts of cross-national information attacks discussed in [[Kuznetsova2025-nu]] and [[Starbird2025-jj]]. The emphasis on engagement-ranking amplification of moral condemnation also connects to work on moral-emotional virality and platform incentives like [[Rossini2026-jn]] and [[Mosleh2024-op]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kim2026-br.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
