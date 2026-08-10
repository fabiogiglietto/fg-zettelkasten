---
title: "Beyond verification| post-truth spaces: Studying authenticity and influence on the internet"
aliases: ["Beyond verification| post-truth spaces: Studying authenticity and influence on the internet"]
authors: ["Richard Rogers", "Kamila Koronska"]
year: 2026
doi: 10.65476/1fw44702
bibtex_key: Rogers2026-cy
topics: [coordinated-inauthentic-behavior, disinformation-narratives-and-information-operations]
citation_count: 0
open_access: false
source_url: https://doi.org/10.65476/1fw44702
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Rogers2026-cy.mp3
pdf_available: true
discovery_date: 2026-07-21T07:26:09.444391Z
---

# Beyond verification| post-truth spaces: Studying authenticity and influence on the internet

> Rogers, R., & Koronska, K. (2026). Beyond verification| post-truth spaces: Studying authenticity and influence on the internet. *International Journal of Communication*, *20*, 1863–1885. https://doi.org/10.65476/1fw44702
>
> [View paper](https://doi.org/10.65476/1fw44702)

## Summary

This paper introduces the concept of the **"post-truth space"** — clusters of densely interlinked web pages and public social media accounts that are difficult to verify or known to spread disinformation, advancing a program to assert political influence. The authors situate this category alongside four prior frameworks (alternative influence networks, fake news engagement spaces, coordinated inauthentic behavior campaigns, and participatory propaganda) and develop a practical mapping technique to help fact-checkers locate influential problematic sources. Combining network analysis, digital investigation of source provenance, and a cluster-betweenness influence metric, they demonstrate the method through a case study of Russia-Ukraine war discourse on Moldovan Facebook. The work is explicitly applied and interventionist, produced within the EU-funded vera.ai verification project.

## Key Contributions

- **Conceptual:** defines and situates the "post-truth space" among existing typologies of problematic online information.
- **Methodological:** an integrated workflow combining keyword-based network mapping, provenance verification via platform transparency signals, and a cluster-betweenness metric as a proxy for influence.
- **Practical:** a workflow generating monitorable source leads for fact-checkers and verification specialists.
- **Replicable protocol:** a demonstrated case-study design (Moldova) extensible to other regions.

## Methods

- Situated the concept against four prior frameworks (alternative influence networks, fake news engagement spaces, coordinated inauthentic behavior, participatory propaganda).
- Queried war-related keywords in CrowdTangle to retrieve Facebook posts, accounts, pages, and groups; tidied data by shortening URLs to domains and resolving native links.
- Ran network analysis in Gephi using ForceAtlas2 spatialization and Louvain modularity community detection, combined with visual network analysis.
- Applied digital investigation using Facebook transparency indicators (name history, default "digital creator" labels, pending verification status) to assess source provenance.
- Developed a **cluster betweenness centrality** metric as a proxy for influence — measuring how far post-truth clusters bridge into other communities.
- Case study: Russia-Ukraine war discourse on Moldovan Facebook (mapped March 2023), chosen for Moldova's exposure to pro-Kremlin disinformation and Facebook's local dominance.

## Findings

- Mapping surfaced distinct clusters: three proximate "post-truth" clusters, a "borderline" cluster, plus conservative/nationalist, pro-Ukraine, mainstream media, and finance/military analysis clusters.
- Top post-truth nodes included stiripesurse.ro (denying the Bucha massacre), digital creator Liliana Mitrea, and Ionel Mojoiu (laundering Russian sources like TASS and lenta.ru without attribution).
- Post-truth clusters had **low betweenness** (Stiri pe surse 76.39, Mitrea 12.73, Mojoiu 11.14) — minimal direct centrality — but supplied bridges to the influential borderline cluster.
- The **borderline cluster** (top node Aktual24.ro, flagged as a disinformation provider) had the highest betweenness (2567.10), exceeding even the mainstream media cluster (Libertatea.ro, 1798.77).
- Post-truth URLs were rarely shared outside their own clusters except via bridges to the borderline cluster, showing how the influence metric captures cluster interpenetration.

## Connections

This paper extends the coordinated-inauthentic-behavior tradition by proposing a complementary, verification-oriented category and mapping method; it shares CIB's synchronized-sharing and network-signal logic developed across the co-sharing literature (e.g. [[Giglietto2020-9d8acdd7]], [[Giglietto2019-e9be81c1]], [[Giglietto2022-0e951ac5]]) and the broader account of coordination and platform manipulation in [[Starbird2025-jj]] and [[Luceri2025-tr]]. Its focus on pro-Kremlin war narratives and influence connects to work on Russia-Ukraine information operations such as [[Kuznetsova2025-nu]], while its applied fact-checking orientation aligns with verification-workflow studies like [[Dierickx2026-tw]] and disinformation-source typologies in [[Cazzamatta2026-lo]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Rogers2026-cy.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
