---
title: "The imaginative landscape of AI: Locating Silicon Valley’s “quiet futuring”"
aliases: ["The imaginative landscape of AI: Locating Silicon Valley’s “quiet futuring”"]
authors: ["Andreas Hepp"]
year: 2026
doi: 10.1177/01634437261454515
bibtex_key: Hepp2026-oi
topics: [platform-governance-and-data-access, computational-social-science-methods]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1177/01634437261454515
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Hepp2026-oi.mp3
pdf_available: true
discovery_date: 2026-05-26T19:31:02.136444Z
---

# The imaginative landscape of AI: Locating Silicon Valley’s “quiet futuring”

## Summary

Despite the title metadata, this paper is an infrastructure-oriented case study of the 2025 German federal election that examines the practical, methodological, and governance bottlenecks of monitoring electoral discourse across X and TikTok. Collecting 81,866 X posts and 43,597 TikTok videos, the authors document how platform-specific affordances, restrictive APIs, and divergent party strategies make reproducible multi-platform analysis extremely difficult under current conditions. They argue that "platform observability" should be reframed as a shared, reusable research infrastructure — standardized tools, workflows, and documentation — rather than as a series of one-off empirical studies, and they derive four recommendations to that end.

## Key Contributions

- An empirical multi-platform, multi-modal dataset spanning X and TikTok across seven major German parties during the 2025 federal election campaign.
- Concrete documentation of post-API bottlenecks: rate limits, algorithmically filtered results, noisy hashtag-based sampling, and obstructed access.
- A reframing of election observability as a *research infrastructure* problem rather than a study-by-study data-collection problem.
- Four actionable recommendations: standardize platform-specific data structures; raise data-access quality standards (including transparent labeling of political accounts); tailor analytical methods to content type (multimodal for video); and institutionalize interdisciplinary computational/political-science collaboration.
- Empirical input for ongoing DSA Article 40 vetted-researcher-access debates.

## Methods

- Case study window: 6 November 2024 – 23 February 2025.
- Parallel scraping of X (X API v2 via a twitter-api-client implementation) and TikTok, seeded with official party accounts and expanded via mentions (X) and hashtags (TikTok).
- Distinction between *authored* (party-account) and *promoted* (retweets, mentions, shared hashtags) content.
- Multimodal TikTok pipeline: pyannote.audio (speaker diarization), OpenCV + DeepFace (facial emotion), HuBERT (vocal tone), XLM-R (textual sentiment); Cramér's V for cross-modal association.
- BERTopic for topic modeling and cross-platform/temporal comparison.

## Findings

- Dataset: 81,866 X posts from 541 accounts; 43,597 TikTok videos from 4,682 accounts.
- Strong cross-party divergence in platform preference: BSW dominates on X with minimal TikTok presence; AfD is highly active on TikTok; FDP and CDU active on both.
- Cross-modal associations on TikTok are uniformly weak (Cramér's V ≤ 0.104) — text, voice, and face carry largely independent emotional signals.
- Political TikToks frequently combine negative textual sentiment and expressive faces with calm vocal delivery, consistent with a "politainment" register.
- Topic overlap exists (Russia/Ukraine, migration dominate both), but migration is more prominent on TikTok, while EU and Israel/Gaza skew toward X; acute news events (Magdeburg attack, Syrian regime fall) surface on X but not in TikTok top topics.
- ~2/3 of hashtag-sampled TikTok content is non-political noise needing aggressive filtering.
- X API v2 caps (~1000 posts/day per account) preclude full historical recovery; TikTok returns partial, algorithmically shaped results.

## Connections

This paper sits squarely in the post-APIcalypse debate over what computational election research can still do, sharing concerns with work on data access constraints and platform-governance critique such as [[Rieder2025-ju]], [[Rieder2026-pp]], and [[Ohme2026-nv]]. Its push to treat observability as durable shared infrastructure connects to the social media observatory and monitoring-workflow agenda exemplified by [[Bruns2025-fz]], [[Bruns2026-yv]], and [[Helmond2026-ll]], while its multi-platform, multimodal TikTok analysis of electoral discourse resonates with platform-comparative election work such as [[Bouchaud2026-lr]] and [[Achmann-Denkler2026-lx]].

## Podcast

A research-radio episode discusses this paper: [Listen](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Hepp2026-oi.mp3)
