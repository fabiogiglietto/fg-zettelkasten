---
title: "Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks"
aliases: ["Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks"]
authors: ["Niccolò Di Marco", "Matteo Cinelli", "Shinichi Nakano", "Andrea Frosini"]
year: 2026
doi: 
bibtex_key: Di_Marco2026-xu
topics: [coordinated-inauthentic-behavior, computational-network-structure-analysis]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2609.24398v1
podcast_url: 
pdf_available: false
discovery_date: 2026-09-27T15:41:52.990035Z
---

# Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks

> Marco, N. D., Cinelli, M., Nakano, S., & Frosini, A. (2026). Optimal and heuristic strategies for evaluating the influence of coordinated behavior in information cascades and retweet networks. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2609.24398v1)

## Summary

This paper reframes the study of Coordinated Inauthentic Behavior (CIB) around a question that is usually left aside: once coordinated accounts have been detected, *how much do they actually shape the way information spreads?* The authors argue that the field has become preoccupied with detection while neglecting the downstream quantification of influence. To address this gap they propose two complementary post-hoc evaluation frameworks — one built on information cascades and one on retweet networks — and develop both optimal and heuristic strategies for measuring the contribution of coordinated accounts to diffusion outcomes.

## Key Contributions

- Introduces two complementary frameworks for the *post-hoc* evaluation of coordinated accounts in information diffusion: one on information cascades and one on retweet networks.
- Shifts the CIB research agenda from detection toward influence quantification.
- Provides both optimal and heuristic algorithmic strategies applicable to each framework, trading exactness against scalability.

## Methods

The authors formalize the CIB influence-evaluation problem in two settings. The first casts the problem over information cascades; the second draws on retweet-network structure (with fuller details beyond the available abstract fragment). For each formulation they derive an optimal strategy for assessing how coordinated accounts affect diffusion, and complement it with heuristic approaches intended to remain tractable on larger structures.

## Findings

- The paper's central empirical results are not recoverable from the provided abstract fragment, which cuts off before the results are described.
- The methodological claim advanced is that CIB influence *can* be systematically evaluated after detection, and that both optimal and heuristic strategies are viable for doing so.

## Connections

This work sits within the broader coordinated-behavior literature that has been dominated by detection methods — for instance the coordination-detection and network-structure approaches in [[Nizzoli2020-cf]], [[Luceri2025-tr]], [[Minici2024-tf]], and the Giglietto line of work on coordinated link/network sharing ([[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]]) — but distinguishes itself by pivoting to influence quantification rather than identification. Its focus on retweet networks and cascade structure connects it to computational analyses of diffusion structure such as [[Di-Marco2025-aa]] and the amplification-and-cascade framing in [[Keller2019-nk]] and [[Starbird2019-qv]].
