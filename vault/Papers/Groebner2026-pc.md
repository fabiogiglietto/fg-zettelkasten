---
title: "From national outlets to transnational audiences: far-right hyperpartisan news sources on YouTube"
aliases: ["From national outlets to transnational audiences: far-right hyperpartisan news sources on YouTube"]
authors: ["Klaus Groebner"]
year: 2026
doi: 10.1177/1329878x261474201
bibtex_key: Groebner2026-pc
topics: [online-radicalization-and-extremism-on-platforms, computational-network-structure-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1177/1329878x261474201
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Groebner2026-pc.mp3
pdf_available: true
discovery_date: 2026-08-17T05:56:38.430452Z
---

# From national outlets to transnational audiences: far-right hyperpartisan news sources on YouTube

> Groebner, K. (2026). From national outlets to transnational audiences: far-right hyperpartisan news sources on YouTube. *Media International Australia*. https://doi.org/10.1177/1329878x261474201
>
> [View paper](https://doi.org/10.1177/1329878x261474201)

## Summary

This article provides empirical evidence for a transnational far-right audience on YouTube by studying four English-speaking far-right hyperpartisan news channels: Sky News Australia (Australia), Fox News (US), Rebel News (Canada) and GB News (UK). Drawing on a near-complete dataset of 114,025 videos and over 51 million comments spanning each channel's full lifetime, Groebner uses social network analysis and topic modelling to trace commenter overlaps and content strategies across national borders. The central argument is that these outlets — better classified as "hyperpartisan" than "alternative" news — form a highly integrated transnational information space in which US-based content occupies a central position, and in which the most engaged users are also the most transnational.

## Key Contributions

- Provides strong empirical evidence for a transnational far-right *audience* on YouTube, filling a gap where prior work centred on elites, institutions, and hyperlink networks rather than audiences.
- Introduces and validates a novel data-gathering method using YouTube's Search endpoint on a per-day, per-channel basis to overcome the platform's 20,000-video playlist limit, producing a historically representative dataset.
- Shifts analytic attention from the "Alternative Influence Network" of individual influencers to traditional far-right hyperpartisan news outlets, and reframes "alternative" news as "hyperpartisan" news.
- Identifies concrete transnationalising content strategies: covering another country's politics, constructing shared enemies, and featuring internationally recognisable figures.
- Documents the central role of US content and the US far right within the ecosystem.

## Methods

Groebner circumvented YouTube's PlaylistItems 20,000-video ceiling by querying the Search endpoint per-day, per-channel, collecting metadata, engagement metrics, captions, and top-level comments back to each channel's founding (through 31 December 2024). The method was validated against a ground-truth set of the 20,000 most recent videos per channel using binary logistic regression. Content was analysed with BERTopic (all-MiniLM-L6-v2 embeddings, UMAP, HDBSCAN, min_cluster_size=50), yielding 175 topics (coherence 0.61, diversity 0.60). Audience structure was examined via lifetime and monthly commenter-overlap analysis and a co-commenting network of each channel's top 1000 videos (edges >200 shared commenters), with Louvain community detection in Gephi, and E-I and Gini-Simpson indices for community structure.

## Findings

- Substantial lifetime commenter overlap across all four channels; the strongest was Sky News Australia → Fox News (56.22%), with Fox a major overlap target for Rebel News (44%) and GB News (38%).
- Fox News is the largest, most domestically-oriented channel but the central overlap target; Sky News Australia emerges as the transnational hub connecting to all channels.
- Monthly (same-month) overlap approached 50% for some channels; new channels rapidly gained transnational overlap within 2–3 months of founding, implying a pre-existing transnational audience.
- Engagement rises with transnationality: mean comments per account rose from 3.01 (one channel) to 97.4 (all four), and average active time span from 155 to 1687 days.
- The co-commenting network (2743 nodes, 121,703 edges) was structured by both upload period and topic; communities formed around shared themes (British Royals, the 2024 US election), while Rebel News formed a relatively isolated Canada-focused cluster.
- Transphobia functions as a transnational connector by constructing a common enemy; US politics (anti-Biden, pro-Trump) is a central transnational theme.
- Topic modelling confirmed content built on nativism, authoritarianism, and populism (Fox News border/police, GB News anti-immigration/Islamophobia, Rebel News Trudeau criticism at 28.86% of output).

## Connections

This paper's YouTube focus and concern with algorithmic amplification and radicalization connect it to broader platform-radicalization work such as [[Rothut2026-or]] and [[Rothut2026-wt]], and its emphasis on how transnational far-right audiences and shared enemies cohere resonates with studies of far-right movement discourse and community formation like [[Askanius2026-de]] and [[Grusauskaite2026-po]]. Methodologically, its co-commenting and audience-overlap network approach aligns with computational analyses of cross-outlet audience structure such as [[Gonzalez-Bailon2024-rq]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Groebner2026-pc.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
