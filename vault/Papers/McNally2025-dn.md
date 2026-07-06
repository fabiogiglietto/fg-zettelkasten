---
title: "The news feed is not a black box: A longitudinal study of Facebook’s algorithmic treatment of news"
aliases: ["The news feed is not a black box: A longitudinal study of Facebook’s algorithmic treatment of news"]
authors: ["Naoise McNally", "Marco Bastos"]
year: 2025
doi: 10.1080/21670811.2025.2450623
bibtex_key: McNally2025-dn
topics: [platform-governance-apis, computational-social-science]
citation_count: 6
open_access: false
source_url: https://doi.org/10.1080/21670811.2025.2450623
podcast_url: 
pdf_available: true
discovery_date: 2025-01-15T00:00:00Z
---

# The news feed is not a black box: A longitudinal study of Facebook’s algorithmic treatment of news

> McNally, N., & Bastos, M. (2025). The news feed is not a black box: A longitudinal study of Facebook’s algorithmic treatment of news. *Digital Journalism*, 1–20. https://doi.org/10.1080/21670811.2025.2450623
>
> [View paper](https://doi.org/10.1080/21670811.2025.2450623)

## Summary

This paper challenges the prevailing "black box" framing of recommender systems by demonstrating that Facebook's News Feed algorithm changes leave detectable, measurable traces in downstream engagement data. Using a decade-long corpus of ~1 million Guardian articles paired with CrowdTangle engagement metrics and a hand-compiled timeline of 52 documented News Feed ranking updates (2011–2020), McNally and Bastos apply time-series methods to test whether algorithmic interventions produced lagged effects on user engagement. They find that hard news engagement is significantly affected by ranking updates roughly three weeks after implementation, while soft news categories (Opinion, Lifestyle, Arts, Sport) are not — evidence that Facebook applies differential algorithmic treatment to news content and that recommender systems can be audited as sociotechnical artifacts shaped by institutional decisions.

## Key Contributions

- A decade-long empirical assessment of how Facebook News Feed updates affect engagement with news, one of the first of its kind.
- A publicly documented timeline of 52 Facebook News Feed ranking changes (2011–2020), parameterized by impact level and valence toward trusted news.
- A replicable methodological pipeline combining cross-correlation, Granger causality, and Seasonal Hybrid ESD anomaly detection for auditing platform algorithm changes.
- A sociotechnical reframing of recommender systems against the dominant "black box" metaphor.
- A concrete articulation of how DSA Article 40(4) and Recital 85 could ground long-run independent platform audits.

## Methods

The authors compiled a timeline of 52 News Feed ranking updates from public announcements, engineering papers, the Haugen disclosures, and leaks, coding each by impact and valence. They collected ~1.02M Guardian articles via the Guardian API, matching 576,673 to CrowdTangle engagement data across five Guardian "pillars" (News, Opinion, Sport, Arts, Lifestyle). After log-transforming and verifying stationarity (ADF tests), they ran cross-correlation function analysis to identify optimal lags, Granger causality tests at lags 1–30, and S-H-ESD anomaly detection on the engagement series.

## Findings

- Optimal cross-correlation lags clustered between 19–24 days across all sections (News: 19; Opinion: 21; Lifestyle: 23; Arts: 20; Sport: 24).
- Cross-correlation coefficients were highest for News (.35) and Sport (.31).
- Granger causality was statistically significant **only** for the News section (F = 1.68, p = .033 at lag 19).
- Anomalies clustered in 2014–2016; two-thirds of News anomalies fell in 2016, especially around the June 2016 friends-and-family prioritization.
- Sport anomalies concentrated in July 2014 (FIFA World Cup), confirming that exogenous events also drive engagement spikes.
- The ~19-day lag is consistent with phased software rollout practices in industry.

## Connections

This paper sits at the intersection of platform algorithm auditing and the politics of platform data access. It connects directly to [[Rieder2025-ju]] and [[Rieder2026-pp]] on auditing recommender systems and to [[Hurcombe2025-cs]], whose prior work on Facebook News Feed updates the authors build on. The argument about DSA Article 40 as a basis for systemic audits resonates with [[Bouchaud2026-lr]] and [[Ohme2026-nv]] on data-access regimes, while the CrowdTangle-based longitudinal design speaks to broader debates about post-CrowdTangle research infrastructure raised in [[Helmond2026-ll]] and [[Bruns2025-fz]].
