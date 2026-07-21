---
title: "Beyond verification| post-truth spaces: Studying authenticity and influence on the internet"
aliases: ["Beyond verification| post-truth spaces: Studying authenticity and influence on the internet"]
authors: ["Richard Rogers", "Kamila Koronska"]
year: 2026
doi: 10.65476/1fw44702
bibtex_key: Rogers2026-cy
topics: [coordinated-inauthentic-behavior, information-disorder-disinformation]
citation_count: 0
open_access: false
source_url: https://doi.org/10.65476/1fw44702
podcast_url: 
pdf_available: true
discovery_date: 2026-07-21T07:26:09.444391Z
---

# Beyond verification| post-truth spaces: Studying authenticity and influence on the internet

> Rogers, R., & Koronska, K. (2026). Beyond verification| post-truth spaces: Studying authenticity and influence on the internet. *International Journal of Communication*, *20*, 1863–1885. https://doi.org/10.65476/1fw44702
>
> [View paper](https://doi.org/10.65476/1fw44702)

## Summary

This paper introduces the **"post-truth space"** as a conceptual and methodological tool for helping fact-checkers locate influential problematic sources online. The authors define a post-truth space as a cluster of densely interlinked web pages and public social media accounts that are difficult to verify or are known disinformation sources advancing a program of political influence. They situate this concept alongside four prior frameworks — alternative influence networks, fake news engagement spaces, coordinated inauthentic behavior, and participatory propaganda — and develop a mapping technique combining network analysis, digital investigation of source provenance, and a cluster-based influence metric. The approach is demonstrated through a case study of Russia-Ukraine war discourse on Moldovan Facebook, and was conducted within the EU-funded vera.ai verification project.

## Key Contributions

- **Conceptual**: defines and situates the "post-truth space" as a distinct category among frameworks for studying problematic online information.
- **Methodological**: an integrated workflow combining keyword-based network mapping, provenance verification via platform transparency signals, and a cluster-betweenness influence metric.
- **Practical**: a workflow generating monitorable source leads for fact-checkers, developed within the vera.ai project.
- **Replicable protocol**: a demonstrated case-study method (Moldova) extensible to other regions.

## Methods

- Situated the concept against four prior frameworks (alternative influence networks, fake news engagement spaces, coordinated inauthentic behavior, participatory propaganda).
- Queried war-related keywords in CrowdTangle to retrieve Moldovan Facebook posts/pages/groups; tidied data by resolving URLs to domains and native links.
- Network analysis in Gephi (ForceAtlas2 spatialization, Louvain modularity community detection) plus visual network analysis to identify clusters.
- Digital investigation using Facebook transparency indicators (account name history, default "digital creator" names, pending verification status) to assess source provenance.
- Developed a **cluster betweenness centrality** metric as a proxy for influence, measuring how far post-truth clusters bridge into other communities.
- Case study of Russia-Ukraine war discourse on Moldovan Facebook (March 2023), chosen for Moldova's exposure to pro-Kremlin disinformation and Facebook's local dominance.

## Findings

- The mapping surfaced distinct clusters: three proximate post-truth clusters, a "borderline" cluster, plus conservative/nationalist, pro-Ukraine, mainstream media, and finance/military analysis clusters.
- Top post-truth nodes included stiripesurse.ro (denying the Bucha massacre), digital creator Liliana Mitrea, and Ionel Mojoiu (laundering Russian sources like TASS and lenta.ru without attribution).
- Post-truth clusters had **low betweenness** (76.39, 12.73, 11.14), indicating minimal direct centrality, but supplied bridges to the influential borderline cluster.
- The **borderline cluster** (top node Aktual24.ro, flagged as a disinformation provider) had the highest betweenness (2567.10) — exceeding even the mainstream media cluster (1798.77) — showing that war discourse was driven substantially by content straddling the post-truth spaces.
- Post-truth cluster URLs were rarely shared outside their own clusters except for bridges to the borderline cluster, demonstrating the influence metric's capture of cluster interpenetration.

## Connections

The paper's conceptual grounding in post-truth and problematic-information debates overlaps with related theoretical work on disinformation framings [[Marwick2026-qd]] and [[Farkas2026-lr]]. Its network-mapping and co-sharing methodology, along with its engagement with the coordinated inauthentic behavior framework, connects directly to the large body of CIB detection and synchronized-sharing research, such as [[Giglietto2020-9d8acdd7]], [[Giglietto2019-e9be81c1]], [[Giglietto2022-0e951ac5]], and [[Luceri2025-tr]]. Its case-study focus on pro-Kremlin influence and Eastern European information environments relates to [[Kuznetsova2025-nu]] and [[Kulichkina2026-zk]].
