---
title: "Toward a transnational information ecology on the right? Hyperlink networking among right-wing digital news sites in Europe and the United States"
aliases: ["Toward a transnational information ecology on the right? Hyperlink networking among right-wing digital news sites in Europe and the United States"]
authors: ["Annett Heft", "Curd Knüpfer", "Susanne Reinhardt", "Eva Mayerhöffer"]
year: 2021
doi: 10.1177/1940161220963670
bibtex_key: Heft2021-ky
topics: [computational-network-structure-analysis, information-operations-disinformation-narratives]
citation_count: 91
open_access: false
source_url: https://doi.org/10.1177/1940161220963670
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445543Z
---

# Toward a transnational information ecology on the right? Hyperlink networking among right-wing digital news sites in Europe and the United States

> Heft, A., Knüpfer, C., Reinhardt, S., & Mayerhöffer, E. (2021). Toward a transnational information ecology on the right? Hyperlink networking among right-wing digital news sites in Europe and the United States. *The International Journal of Press/Politics*, *26*, 484–504. https://doi.org/10.1177/1940161220963670
>
> [View paper](https://doi.org/10.1177/1940161220963670)

## Summary

This paper investigates whether right-wing alternative online news sites (RNS) form interconnected national and transnational news ecologies through hyperlinking across six Western democracies (Austria, Germany, US, UK, Denmark, Sweden). Using hyperlink data harvested from 65 RNS over three months in 2018, the authors examine both direct links between RNS and the shared external reference points these sites cite. They find that RNS do build interlinked right-wing ecologies domestically and transnationally, that U.S. sites serve as a central hub, and — counterintuitively — that legacy "mainstream" media are the most important transnationally shared reference points. This last finding qualifies the widespread assumption that such sites form insulated echo chambers, suggesting instead that they seek to connect to the broader information environment.

## Key Contributions

- Empirical cross-national mapping of transnational hyperlink networks among RNS across six Western democracies, extending beyond single-country studies.
- Introduction of the **Transnational Reference Score (TRS)**, combining a domain's prevalence among RNS and its spread across country collections to identify shared reference points.
- Evidence qualifying echo-chamber/counter-public fears: RNS link heavily to mainstream legacy media.
- Demonstration of the U.S. right-wing ecology's hub role in transatlantic information flows, framed as a possible developmental future for European ecologies.
- A hybrid conceptualization of RNS hyperlinking blending professional journalistic and political/movement logics, tied to country-level context conditions.

## Methods

Hyperlink network analysis of article content from 65 RNS across six countries, selected for institutionalization as news media, self-positioning as "alternative" correctives, right-wing ideology, and national scope. Article content (102,379 articles) was collected via Media Cloud for July–October 2018; hyperlinks were extracted using the R package `rvest` (~12.5 million links, cleaned to 725,450 substantive links). Transnationality was operationalized two ways: horizontal cross-border RNS-to-RNS links, assessed via the External-Internal (E-I) index, and the TRS for external reference points. Manual content analysis classified linked actors by type, scope, and country (Krippendorff's alpha 0.79 for country, 0.67 for actor type). Network analysis and visualization used igraph, sna, network, and ggplot2. Country selection was designed as a strong test case using three culturally proximate pairs (Germany-Austria, US-UK, Denmark-Sweden).

## Findings

- Of 725,450 total links, 23,806 connected sampled RNS, but only 830 crossed borders — most RNS-to-RNS linking is domestic.
- U.S. sites are by far the most active linkers (average outdegree 647.3), forming the densest, most homogeneously interconnected domestic cluster and the only cluster addressed by RNS from all other countries.
- Country patterns diverge sharply: U.S., Swedish, and German RNS link mostly domestically; Danish RNS link almost exclusively transnationally (95%); UK sites link only externally.
- Transnational links follow geographic/cultural proximity, with Danish and Swedish links predominantly pointing to U.S. sites.
- Among top transnationally shared reference points, legacy media dominate (nytimes.com, theguardian.com, reuters.com, dailymail.co.uk); Trump's Twitter ranked 8th; only four sampled RNS (all U.S., e.g. Breitbart) appear.
- About 75% of top-domain links go to media/journalists, ~16% to economic actors, under 5% each to political and societal actors.

## Connections

This work sits within research on cross-national disinformation infrastructures and resonates strongly with comparative studies of information-environment resilience such as [[Humprecht2020-gd]] and [[Humprecht2025-ml]], as well as structural accounts of asymmetric hyper-partisan media ecosystems like [[Benkler2018-lw]]. Its focus on right-wing alternative and far-right media links it to [[Askanius2026-de]] and to work on the digital right by [[Knupfer2025-vt]], while its use of hyperlink and coordinated-network methods connects it to the network-analytic tradition represented by [[Keller2019-nk]] and [[Giglietto2019-e9be81c1]].
