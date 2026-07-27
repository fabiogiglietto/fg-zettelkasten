---
title: "Beyond time delays: How web scraping distorts measures of online news consumption"
aliases: ["Beyond time delays: How web scraping distorts measures of online news consumption"]
authors: ["Roberto Ulloa", "Frank Mangold", "Felix Schmidt", "Judith Gilsbach", "Sebastian Stier"]
year: 2024
doi: 
bibtex_key: Ulloa2024-jm
topics: [survey-methodology-validity, computational-text-methods-llms]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2412.00479v1
podcast_url: 
pdf_available: true
discovery_date: 2024-11-15T00:00:00Z
---

# Beyond time delays: How web scraping distorts measures of online news consumption

> Ulloa, R., Mangold, F., Schmidt, F., Gilsbach, J., & Stier, S. (2024). Beyond time delays: How web scraping distorts measures of online news consumption. *arXiv [cs.CY]*.
>
> [View paper](http://arxiv.org/abs/2412.00479v1)

## Summary

This paper interrogates a foundational but largely untested assumption in web-tracking research: that ex-situ scraping of URLs visited by participants yields content comparable to what users actually saw in their browsers. Using a two-wave study of 412 German participants whose browsers captured 34,108 news article visits in-situ via extension, the authors compare that ground-truth HTML to parallel ex-situ scrapes at delays of 0, 30, 60, and 90 days. They find that the *collection environment itself* — not temporal decay — drives the bulk of discrepancy: roughly 33.8% of content diverges even at near-zero delay, while 90 days of additional aging contributes only ~6.5 percentage points. Crucially, these errors are systematically patterned across news types, largely because paywalls, login walls, and cookie consents block ex-situ scrapers from reaching the content that authenticated users see. The authors argue that in-situ capture is methodologically necessary for valid measures of online news exposure.

## Key Contributions

- First direct, URL-matched quantification of the in-situ vs. ex-situ gap in web-tracking research.
- Disentangles two error sources — collection environment and temporal delay — showing the former dominates, reversing prior emphasis.
- Demonstrates that scraping bias is systematic across domain-based, URL-keyword, and ML-content categorization schemes, with downstream consequences for studies of selective exposure and fragmentation.
- Tests and largely rejects simple bias-mitigation heuristics (threshold raising, domain dropping); only excluding interaction-heavy categories restores distributional equivalence.
- Provides practical recommendations for ex-situ infrastructure (user-agent rotation, rate management, dynamic-content handling) and motivates future error-correction frameworks.

## Methods

A two-wave web-tracking study (July–December 2023) used a desktop browser extension to capture URLs, HTML, and timestamps in-situ. Each visited URL was also scraped ex-situ in near real-time using `trafilatura` (fixed user agent) and `requests` (randomized user agents), with a subset re-scraped at 30/60/90-day delays calibrated to original visit times. News articles were identified via URL-pattern heuristics (F1 = .937 against manual annotation). Discrepancy was measured as normalized Levenshtein distance between in-situ and ex-situ content at three representations (cleaned text, raw text, full HTML). News was categorized via a domain typology, URL keywords, and an ML classifier trained on party press releases. Analyses used linear regression, ANOVA with Tukey HSD, and chi-square tests.

## Findings

- Mean in-situ vs. near-real-time ex-situ Levenshtein distance: 40.1% (cleaned text), 49.9% (raw text), 71.8% (HTML).
- Wave 1 baseline distance (33.8%) was lower than wave 2 (45.4%), suggesting cumulative deterioration as scrapers were detected and blocked.
- Post-hoc delay added only 6.5 pp over 90 days, with 5.5 pp accruing in the first 30 days and a plateauing trajectory thereafter.
- `trafilatura` was blocked by spiegel.de between waves due to its fixed user agent; user-agent randomization (via `requests`) was more resilient.
- Discrepancies were larger for legacy press and tabloids than for commercial broadcasters and hyperpartisan outlets, tracking paywall prevalence.
- 77.5% of in-situ Domestic Commerce pages were misclassified as Non-thematic ex-situ; 84% of the worst-misclassified articles required user interaction (73% paywalls/logins).
- Distributional equivalence between in-situ and ex-situ data was achieved only after excluding Domestic Commerce, Technology, and Non-thematic categories (χ²(19) = 16.87, p = .599).

## Connections

This paper extends ongoing methodological scrutiny of digital trace measurement, complementing critiques of platform data quality and scraping fragility such as [[Freelon2024-sc]] and [[Rieder2025-ju]], and joining work that benchmarks how data-collection design shapes downstream inferences like [[Bak-Coleman2026-mk]] and [[Murtfeldt2025-wu]]. It also speaks to studies of online news exposure and fragmentation that increasingly rely on web-tracking traces (e.g., [[Heiss2026-qv]], [[Bouchaud2026-lr]]), where the systematic biases documented here could materially affect substantive conclusions.
