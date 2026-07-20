---
title: "Best practices for source-based research on misinformation and news trustworthiness using NewsGuard"
aliases: ["Best practices for source-based research on misinformation and news trustworthiness using NewsGuard"]
authors: ["Jula Lühring", "Hannah Metzler", "Ruggero Lazzaroni", "Apeksha Shetty", "Jana Lasser"]
year: 2025
doi: 10.51685/jqd.2025.003
bibtex_key: Luhring2025-od
topics: [information-disorder-disinformation, survey-methodology-validity]
citation_count: 4
open_access: false
source_url: https://doi.org/10.51685/jqd.2025.003
podcast_url: 
pdf_available: true
discovery_date: 2025-01-15T00:00:00Z
---

# Best practices for source-based research on misinformation and news trustworthiness using NewsGuard

> Lühring, J., Metzler, H., Lazzaroni, R., Shetty, A., & Lasser, J. (2025). Best practices for source-based research on misinformation and news trustworthiness using NewsGuard. *Journal of Quantitative Description: Digital Media*, *5*. https://doi.org/10.51685/jqd.2025.003
>
> [View paper](https://doi.org/10.51685/jqd.2025.003)

## Summary

This paper conducts a longitudinal empirical audit of NewsGuard, a widely used commercial source-level news trustworthiness rating system, examining how its ratings, coverage, and contextual labels have evolved from 2019 to 2024 across nine countries. The authors argue that while NewsGuard has become a reasonably stable instrument for source-based misinformation research since 2022—particularly for the US, France, Italy, Germany, and Canada—common methodological choices substantially shape downstream findings. Most notably, the conventional binary trustworthy/untrustworthy split at score 60 can distort results because a handful of high-volume sources (e.g., Breitbart, Bild) sit near the threshold and shift classification entirely when re-rated. The paper concludes with concrete best-practice recommendations, urging continuous scores, snapshot transparency, country-level stability checks, and greater use of NewsGuard's underutilized topic and political-orientation labels.

## Key Contributions

- First systematic longitudinal audit of the NewsGuard database across time and countries.
- Empirical demonstration that binary-vs-continuous operationalization and snapshot choice can materially alter substantive conclusions in misinformation research.
- Operational stability criteria (6-month windows, <0.5 SD month-to-month change, <5% source growth) for assessing country-level reliability.
- A reusable reproduction framework, built on Lasser et al. (2022), for testing measurement-instrument sensitivity.
- Best-practice recommendations and validation procedures for source-based misinformation work.
- Highlights the analytic value of NewsGuard's contextual labels (political orientation, topics) beyond the headline trust score.

## Methods

The authors analyze monthly NewsGuard snapshots (March 2019–September 2024) drawn from the public S3 bucket, computing descriptive statistics on coverage, updates, and criterion fulfillment across nine countries. They run factor and correlation analyses on the nine journalistic sub-criteria, reproduce Lasser et al. (2022) on politicians' news-sharing on Twitter using six historical snapshots plus dynamic month-by-month matching, and cross-validate ratings against external resources (GOND, MediaBiasFactCheck) and manual annotation of all 406 German-language sources.

## Findings

- The database grew from 2,375 to 12,288 sources, adding ~137 domains/month with few removals; average trustworthiness fell from 71.8 to 63.6, driven by additions of low-trust sources rather than re-evaluation.
- Sources are reviewed on average every 249 days, but scores actually change only every ~570 days.
- Two criteria—avoiding deceptive headlines and not repeatedly publishing false content—load on a single dominant factor (58.1% variance, r=0.9).
- Continuous-score reproduction results are stable across snapshots; binary results swing sharply (e.g., Republicans' untrustworthy-link share at 2–3% vs. 8%; AfD's roughly doubles in the 2024 snapshot, almost entirely due to bild.de crossing the threshold).
- 76.1% of rated sources are US-based; US sources score systematically lower even after controlling for time and coverage, consistent with Hallin & Mancini-style media-system differences.
- Only 33.4% of sources carry political-orientation labels (sparse outside the US), but where present they appear valid (83% agreement with manual coding and MBFC); right-leaning sources average 26.4 in trust vs. 60.6 for left-leaning.
- Topic labels cover 97% of sources; untrustworthy sources most commonly cover politics (79%), not conspiracies (32.5%).

## Connections

This paper is a methodological companion to a growing body of work that relies on NewsGuard or similar domain-level trust ratings for downstream claims about misinformation exposure and diffusion, including [[DeVerna2025-dl]], [[Bouchaud2026-lr]], [[Allen2025-ot]], and [[Lai2024-to]], all of which inherit the binary-vs-continuous and snapshot-sensitivity issues identified here. It also speaks directly to the measurement-critique tradition associated with [[Budak2024-ef]] and [[Gonzalez-Bailon2024-rq]], who argue that misinformation prevalence and effects estimates depend heavily on operationalization choices, and complements comparative and cross-national efforts such as [[Humprecht2025-ml]] by clarifying where NewsGuard coverage is reliable enough to support such comparisons.
