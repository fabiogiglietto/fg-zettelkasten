---
title: "Computational research in the post-API age"
aliases: ["Computational research in the post-API age"]
authors: ["Deen Freelon"]
year: 2018
doi: 10.31235/osf.io/56f4q
bibtex_key: Freelon2018-ao
topics: [platform-data-access-governance, llm-augmented-research-methods]
citation_count: 7
open_access: false
source_url: https://doi.org/10.31235/osf.io/56f4q
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445549Z
---

# Computational research in the post-API age

> Freelon, D. (2018). Computational research in the post-API age. *Polit. Commun.*, *35*, 665–668. https://doi.org/10.31235/osf.io/56f4q
>
> [View paper](https://doi.org/10.31235/osf.io/56f4q)

## Summary

This brief, agenda-setting essay by Deen Freelon argues that computational communication research has entered a **"post-API age"**, precipitated by Facebook's April 2018 closure of its Pages API, which eliminated all terms-of-service-compliant methods for independently extracting Facebook content. The central claim is that heavy investment in platform-specific API methods is dangerously fragile: companies can restrict or eliminate access overnight, without recourse, rendering hard-won methodological skills and training obsolete. Drawing on his own experience of a Facebook workshop and Python module made instantly useless, Freelon offers two guiding recommendations for graduate computational methods education — teach web scraping as a more durable and flexible skill, and cultivate literacy in the legal and ethical consequences of violating platform terms of service. The piece reframes data access as inherently tenuous and contingent on corporate power, urging methodological resilience and ethical reflexivity.

## Key Contributions

- Names and diagnoses the **"post-API age"** as a defining structural challenge for computational communication research.
- Provides practical guidance for graduate curricula, advocating web scraping instruction alongside API training.
- Articulates ethical/legal recommendations: prefer authorized methods, distinguish TOS compliance from research ethics, and understand the risks of TOS violation.
- Calls on scholars to foreground data-access fragility in future publications and conference submissions.

## Methods

A reflective, argumentative essay rather than an empirical study. Freelon draws on his personal experience with tools rendered obsolete by the API closure, reviews and compares a spectrum of web scraping tools (browser extensions like Web Scraper and Grepsr; standalone software like Teleport Pro; cloud services like Import.io and Webhose.io; and code frameworks like BeautifulSoup and Selenium), and uses illustrative cases such as collecting US Congressional campaign messages via the Twitter API versus scraping candidate websites.

## Findings

- Code-based scraping tools (BeautifulSoup, Selenium) offer maximum flexibility at minimum cost but require understanding each page's unique DOM structure, making them harder to learn and site-specific.
- Major platforms (Facebook, Google) prohibit automated scraping in their TOS and actively detect and block it, though carefully crafted software can circumvent restrictions.
- Consequences of TOS violation range from blacklisted API credentials and temporary IP bans to, in extreme cases, criminal prosecution under the Computer Fraud and Abuse Act (as in the Aaron Swartz case).
- The then-pending *Sandvig v. Sessions* lawsuit challenges criminal prosecution of TOS violations, but its unresolved status leaves researchers in legal uncertainty.
- **TOS compliance is distinct from human subjects compliance**: respecting a company's terms does not equate to protecting users.

## Connections

This essay is a foundational statement of the platform-data-access problem that later work develops empirically and normatively. It directly anticipates studies documenting the collapse and instability of API access and defending scraping as a research practice, such as [[Tonneau2025-bv]] and [[Freelon2024-sc]], and connects to debates over data-access governance and researcher-platform relations taken up in [[Rieder2025-ju]], [[Bruns2019-nr]], and [[Ohme2026-nv]]. Its call to distinguish TOS compliance from research ethics resonates with ongoing discussions of platform governance and legal risk in [[Helmond2026-ll]] and [[Bechmann2026-dr]].
