---
title: "Understanding Coordinated and Inauthentic Link Sharing Behavior on Facebook in the Run-up to 2018 General Election and 2019 European Election in Italy"
aliases: ["Understanding Coordinated and Inauthentic Link Sharing Behavior on Facebook in the Run-up to 2018 General Election and 2019 European Election in Italy"]
authors: ["Fabio Giglietto", "Nicola Righetti", "Giada Marino"]
year: 2019
doi: 10.31235/osf.io/3jteh
bibtex_key: Giglietto2019-0bd8b768
kind: own
topics: [coordinated-inauthentic-behavior, political-communication-elections]
citation_count: 30
open_access: true
source_url: https://doi.org/10.31235/osf.io/3jteh
podcast_url: 
pdf_available: false
discovery_date: 
---

# Understanding Coordinated and Inauthentic Link Sharing Behavior on Facebook in the Run-up to 2018 General Election and 2019 European Election in Italy

> Giglietto, F., Righetti, N., & Marino, G. (2019). Understanding Coordinated and Inauthentic Link Sharing Behavior on Facebook in the Run-up to 2018 General Election and 2019 European Election in Italy. *Center for Open Science*. https://doi.org/10.31235/osf.io/3jteh
>
> [View paper](https://doi.org/10.31235/osf.io/3jteh)

## Summary

This paper confronts a problem Facebook itself created: the platform coined the term "coordinated inauthentic behavior" to describe manipulative networked activity but never defined it with any precision. Giglietto, Righetti, and Marino respond by building a literature-grounded, operationalizable definition and an accompanying detection method they call **coordinated link sharing** — the behavior of multiple Facebook entities rapidly sharing the same political news story within a very short time window. Applying this to two Italian electoral periods (the 2018 general election and the 2019 European election), they show that such coordinated networks exist, amplify engagement, skew toward anti-immigration and far-right content, and frequently circulate news from outlets already blacklisted by fact-checkers.

## Key Contributions

- An operationalizable, literature-grounded definition of "coordinated inauthentic behavior" that bridges Facebook's vague operational concept with academic work on coordination and authenticity.
- The concept and detection method of **coordinated link sharing** on Facebook.
- A novel empirical pipeline combining the CrowdTangle API with curated datasets of Italian political news.
- Empirical evidence of coordinated inauthentic link sharing across two Italian elections, tying it to elevated engagement, far-right/anti-immigration propaganda, and blacklisted sources.

## Methods

The authors begin with a conceptual synthesis of prior scholarship on *coordination* and *authenticity* to derive their working definition. Empirically, they draw Facebook data on pages, groups, and verified public profiles via the CrowdTangle API, matched against two datasets of Italian political news stories from the run-up to the 2018 and 2019 elections. The core detection step identifies entities that shared the same news story within a very short time window and groups them into coordinated networks. They then qualitatively inspect the self-presentation of these entities (political vs. ostensibly non-political), compare the engagement of coordinated news against the rest of the dataset, and cross-reference the shared outlets against fact-checker blacklists.

## Findings

- In 2018, 10 coordinated networks were detected, comprising 28 entities.
- In 2019, 50 coordinated networks were detected, comprising 143 entities.
- Coordinating entities were mixed: some overtly political, others presenting as entertainment venues while sharing political content — the basis for the "inauthentic" label, since such framing reaches audiences unguarded against influence.
- News shared by coordinated networks received higher Facebook engagement than other news in the dataset.
- Much of the shared content boosted anti-immigration and far-right propaganda.
- Several of the shared outlets had already been blacklisted by fact-checkers.

## Connections

This is a foundational statement of the coordinated link sharing research program later refined and extended by the same group — see [[Giglietto2020-9d8acdd7]] and [[Giglietto2020-6278a4aa]], as well as subsequent work such as [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], and [[Marino2023-9137f448]]. It sits alongside parallel efforts to detect coordinated manipulation and its relation to disinformation, including [[Keller2019-nk]], [[Nizzoli2020-cf]], [[Starbird2019-qv]], and [[Guess2019-ym]].
