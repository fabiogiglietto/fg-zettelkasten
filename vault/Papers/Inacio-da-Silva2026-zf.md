---
title: "Identifying potentially irregular electoral ads in Facebook during the Brazilian elections"
aliases: ["Identifying potentially irregular electoral ads in Facebook during the Brazilian elections"]
authors: ["Marcio Inacio da Silva", "Lucas de Oliveira", "Pedro Olmo Vaz de Melo", "Oana Goga", "Fabrício Benevenuto"]
year: 2026
doi: 10.1145/3796545
bibtex_key: Inacio-da-Silva2026-zf
topics: [elections-political-communication, platform-governance-data-access]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1145/3796545
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Inacio-da-Silva2026-zf.mp3
pdf_available: false
discovery_date: 2026-02-16T20:52:21.543650Z
---

# Identifying potentially irregular electoral ads in Facebook during the Brazilian elections

> da Silva, M. I., de Oliveira, L., de Melo, P. O. V., Goga, O., & Benevenuto, F. (2026). Identifying potentially irregular electoral ads in Facebook during the Brazilian elections. *ACM Transactions on the Web*. https://doi.org/10.1145/3796545
>
> [View paper](https://doi.org/10.1145/3796545)

## Summary

This paper reports on an independent auditing infrastructure deployed during the 2018 Brazilian general elections to monitor political advertising on Facebook. Motivated by concerns raised after the 2016 U.S. presidential election about opaque targeted political ads, the authors built a browser plugin that scraped ads served to volunteer users' timelines and analyzed the resulting corpus to identify advertising that appeared to violate Brazilian electoral rules. The work argues that volunteer-based, crowdsourced auditing is a feasible response to platforms' insufficient ad transparency, and demonstrates that such a system can surface concrete cases of potentially irregular electoral advertising in a major election outside the U.S.

## Key Contributions

- Design and deployment of an independent, crowdsourced ad-auditing infrastructure adapted to the Brazilian electoral and regulatory context.
- Empirical evidence on the nature of political advertising on Facebook during the 2018 Brazilian elections, including ads flagged as potentially irregular.
- A reusable methodological template for browser-plugin-based platform auditing applicable to other electoral environments where platform-provided disclosure is inadequate.

## Methods

The authors adapted an existing browser plugin to capture ads appearing on the Facebook timelines of more than 2,000 Brazilian volunteers during the 2018 election period. The collected ads were then analyzed and classified, with attention to whether they conformed to Brazilian electoral advertising rules; ads deviating from these rules were flagged as potentially irregular.

## Findings

- The crowdsourced infrastructure successfully assembled a real-world corpus of political ads served to Brazilian Facebook users during the campaign.
- A meaningful subset of collected ads were identified as potentially irregular under Brazilian electoral law.
- The exercise demonstrates concrete gaps between platform self-disclosure and what independent auditing can reveal.

## Connections

This paper sits squarely in the lineage of independent platform auditing that responds to inadequate data access from major platforms; methodologically it resonates with browser-extension and donation-based approaches discussed in [[Ohme2026-nv]] and [[Ulloa2024-jm]], and with broader arguments about researcher access in [[Rieder2026-pp]] and [[Rieder2025-ju]]. Its substantive focus on political ad transparency connects to work on ad libraries and electoral influence such as [[Bouchaud2026-lr]] and [[Votta2025-xz]], extending those concerns from U.S. and European contexts to Brazil.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Inacio-da-Silva2026-zf.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-facebook-ads-spotting-election-interference/id1866587707?i=1000750088383)
