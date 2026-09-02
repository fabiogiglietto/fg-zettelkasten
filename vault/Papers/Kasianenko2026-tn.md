---
title: "Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices"
aliases: ["Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices"]
authors: ["Kateryna Kasianenko", "Caroline Gardam", "Katherine M. FitzGerald", "Ashwin Nagappa", "Axel Bruns", "Shir Weinbrand", "Daniel Angus", "Samantha Vilkins", "Abdul Karim Obeid"]
year: 2026
doi: 10.1177/1329878x261481856
bibtex_key: Kasianenko2026-tn
topics: [conspiracy-narratives-in-media, generative-ai-disinformation]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1177/1329878x261481856
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kasianenko2026-tn.mp3
pdf_available: true
discovery_date: 2026-09-02T09:44:54.715331Z
---

# Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices

> Kasianenko, K., Gardam, C., FitzGerald, K. M., Nagappa, A., Bruns, A., Weinbrand, S., Angus, D., Vilkins, S., & Obeid, A. K. (2026). Searching for the truth? search engines and their AI affordances’ responses to conspiratorial search practices. *Media International Australia*. https://doi.org/10.1177/1329878x261481856
>
> [View paper](https://doi.org/10.1177/1329878x261481856)

## Summary

This paper presents an algorithmic audit of how Google Search and its AI Overview (AIO) feature respond to conspiratorially framed versus general information-seeking queries, using the chemtrails (established) and 15-minute cities (emergent) conspiracy theories as comparative case studies. The authors argue that search engines are a core infrastructure for conspiratorial information-seeking, and that how they respond to different query formulations helps explain online conspiracy dynamics. They find that conspiratorially framed queries return markedly different results — more news articles and social media posts (some conspiratorial in content) — while general queries surface more government sources. AI Overviews are sensitive to query framing and generally attempt to debunk conspiracy claims, but their guardrails are uneven: debunking is often brief and evidence-poor, and newer narratives are inadvertently legitimized when AIOs frame them as "debates," "fears," or "criticism."

## Key Contributions

- Introduces a query-design methodology grounded in actual traces of conspiratorial communities' information-seeking practices (Instagram hashtags, a geoengineering forum FAQ, Reddit subreddits, Google Trends), moving beyond purposive or news-sourced query sampling.
- Provides one of the first algorithmic audits of Google's AI Overviews in relation to conspiracy theories, extending search-audit scholarship to AI-powered affordances.
- Adapts the social-media "practice mapping" network visualization method to compare search result similarity across query formulations.
- Offers a comparative case study of an established (chemtrails) versus emergent (15-minute cities) conspiracy theory, showing guardrails are weaker for newer narratives.
- Documents the underexamined role of commercial sources in giving visibility to problematic content within AI-generated summaries.

## Methods

The authors ran a virtual agent-based audit of Google Search including AIOs from Sydney, twice daily over 7 days (Jan 14–20, 2026). They developed realistic conspiratorial and non-conspiratorial query sets (65 chemtrails, 53 15-minute cities queries) grounded in community traces. They collected 1,629 search page observations (17,298 URLs and 1,342 AIOs referencing 863 unique sources) via Selenium, parsed with Beautiful Soup and Regex. Analysis included cosine-similarity comparison of top-10 result sets visualized with Gephi/Force Atlas 2, source concentration via Jaccard Index, manual source-type coding (Krippendorff's α 0.78), and coding of 80 AIOs for conspiratorial stance (intercoder reliability 0.76) plus discursive strategies.

## Findings

- Results for conspiratorial queries diverge substantially from general queries; minor variations produce similar results, while more tendentious formulations diverge more.
- Location-specific queries produced localized results, consistent with prior search audit literature.
- Conspiratorial queries returned more news media (often reputable debunking outlets) and more social media posts (some explicitly conspiratorial); general queries returned more government websites.
- Moderation sometimes backfired: a European Parliament page (appearing in 46 result sets) presented conspiratorial tropes with the debunking answer hidden behind a non-obvious link.
- Chemtrails AIOs applied consistent guardrails, but for 15-minute cities, 5 of 40 analyzed AIOs actively promoted the conspiracy by framing it as legitimate "debate," "fears," or "criticism."
- AIO debunking was often brief, dismissive, and evidence-poor; conspiratorial queries produced lower-quality AIOs (unexplained acronyms, an untranslated word).
- Commercial sources (Amazon links to conspiracy books, real estate agencies) were more prominent in AIOs than in organic results, sometimes promoting conspiratorial ideation even alongside debunking text.

## Connections

This audit of AI Overviews sits at the intersection of conspiracy-narrative research and concerns about generative AI mediating disinformation, complementing work assessing generative models' propensity to produce or amplify misleading content such as [[Hameleers2026-mc]] and [[Emilio2026-ik]]. Its close reading of how conspiratorial communities practice "do your own research" and information-seeking connects to broader studies of conspiracy epistemics and community dynamics like [[Grusauskaite2026-po]] and [[Marwick2025-ov]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Kasianenko2026-tn.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
