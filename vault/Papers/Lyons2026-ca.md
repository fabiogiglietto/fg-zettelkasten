---
title: "Exposure to low-credibility online health content is limited and is concentrated among older adults"
aliases: ["Exposure to low-credibility online health content is limited and is concentrated among older adults"]
authors: ["Benjamin Lyons", "Andy J. King", "Rebecca L. Barter", "Kimberly A. Kaphingst"]
year: 2026
doi: 10.1038/s43587-025-01059-x
bibtex_key: Lyons2026-ca
topics: [health-misinformation-online, information-disorder-misinformation]
citation_count: 2
open_access: false
source_url: https://doi.org/10.1038/s43587-025-01059-x
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lyons2026-ca.mp3
pdf_available: true
discovery_date: 2026-02-10T06:52:51.874075Z
---

# Exposure to low-credibility online health content is limited and is concentrated among older adults

> Lyons, B., King, A. J., Barter, R. L., & Kaphingst, K. A. (2026). Exposure to low-credibility online health content is limited and is concentrated among older adults. *Nature Aging*, 1–9. https://doi.org/10.1038/s43587-025-01059-x
>
> [View paper](https://doi.org/10.1038/s43587-025-01059-x)

## Summary

This paper links national US survey data (n=1,059) with passive web-tracking and YouTube viewing histories collected over roughly four weeks in late 2023 to measure real-world exposure to low-credibility online health content. The central finding is that such exposure is rare in the aggregate — a mean of 0.5 low-credibility health visits per person, roughly 3% of all health browsing — but highly concentrated: the top 10% of users account for 77% of it. That concentration is patterned by age, cognition, and worldview: adults aged 60+, those with poorer health-information discernment, those holding stronger conspiracist beliefs, and consumers of dubious political news are disproportionately exposed. Crucially, exposure is driven not by social media or search engines but by referrals from other low-credibility sites, implying habitual cross-domain consumption rather than incidental encounters. The work extends the digital-trace misinformation literature from its usual focus on political news into the health domain, showing that age-based vulnerability generalizes across topics and platforms.

## Key Contributions

- Extends digital-trace misinformation research beyond political news into online health content, testing cross-domain generalizability of age effects.
- Provides one of the first linked studies combining survey responses with passive web and YouTube tracking specifically for health misinformation exposure.
- Introduces a hybrid embedding + LLM-assisted pipeline for classifying and credibility-rating health content at scale, validated against human coders.
- Identifies referral pathways (cross-linking among low-credibility sites, not search/social) with implications for platform intervention design.
- Validates digital-trace exposure measures against survey-based misperception and discernment outcomes.

## Methods

The authors used YouGov's Pulse Panel (n=1,059 with web data; survey October–November 2023), approximating the US adult population. Passive metering (RealityMine) captured 9.7 million web addresses across devices over ~4 weeks per participant. URLs were classified as health-related using YouGov category tags plus OpenAI text embeddings; 1,155 health domains were hand-coded for credibility (78 flagged, Krippendorff's α = 1.00). YouTube data (~470,000 videos) were classified for health relevance via embeddings, then 3,902 health videos were credibility-coded using a hybrid manual + fine-tuned GPT-4o approach (Cohen's κ = 0.89–0.97). Survey measures covered cancer headline discernment, cancer risk-factor (mis)perceptions, conspiracism, ideology, and demographics. Analysis relied on preregistered OLS regression with robust standard errors and survey weights, supplemented by logistic and negative binomial models and outlier-exclusion robustness checks, plus a referrer analysis based on the temporal sequence of visits.

## Findings

- ~13% of respondents visited any low-credibility health domain in the window (mean 0.5, max 122); ~77% saw any health content (mean 34 visits).
- Low-credibility content made up ~3% of health visits on the open web and ~10% on YouTube.
- Exposure was highly concentrated: top 1% of users accounted for 37%, top 10% for 77%, of total low-credibility exposure.
- Adults 60+ were significantly more exposed than 18–29 year olds, robust to controls for total health visits and total web sessions.
- Poorer cancer headline discernment and belief in false cancer risk factors predicted greater exposure, with effects strongest among older adults.
- Older conservatives and older heavy consumers of right-leaning partisan news showed the highest exposure.
- Referrals to low-credibility health sites came predominantly from other low-credibility sites (especially among 60+), with minimal search or social referral.
- No age difference in absolute YouTube low-credibility exposure, but older adults' lower overall YouTube use made such content a larger share of their health video diet.
- Dubious political news consumption and low-credibility health website visits independently predicted low-credibility YouTube health exposure.
- A companion media-literacy treatment had no significant downstream effects on exposure.

## Connections

This work sits within the broader effort to validate what digital trace and survey data actually reveal about online information exposure, connecting to methodological discussions of measurement and platform data in [[Ulloa2024-jm]] and web-tracking approaches in [[Fattorini2026-bo]]. Its emphasis on cross-domain consumption profiles and the limited, concentrated nature of misinformation exposure resonates with related evidence on who encounters low-credibility content in [[Stagnaro2025-pz]] and [[DiGiuseppe2025-es]]. The other topic papers largely concern network diffusion or political news specifically and are not directly engaged here.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Lyons2026-ca.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-aging-online-health-misinformations/id1866587707?i=1000749136914)
