---
title: "The challenges of working with platform data from clean room environments"
aliases: ["The challenges of working with platform data from clean room environments"]
authors: ["Axel Bruns", "Laura Vodden"]
year: 2026
doi: 10.25358/openscience-15825
bibtex_key: Bruns2026-pn
topics: [platform-data-access-and-governance, llm-and-computational-content-analysis]
citation_count: 0
open_access: true
source_url: https://doi.org/10.25358/openscience-15825
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bruns2026-pn.mp3
pdf_available: true
discovery_date: 2026-07-18T05:54:58.327075Z
---

# The challenges of working with platform data from clean room environments

> Bruns, A., & Vodden, L. (2026). The challenges of working with platform data from clean room environments. *Gutenberg Open Science*. https://doi.org/10.25358/openscience-15825
>
> [View paper](https://doi.org/10.25358/openscience-15825)

## Summary

This report examines the rise of "clean room" data access environments as the dominant model through which major platforms now provide research data, following the closure of open APIs after the Cambridge Analytica scandal. Focusing on the Meta Content Library (MCL) and its two evolving access frameworks — the Virtual Data Enclave (VDE) and the newer Secure Research Environment (SRE) — Bruns and Vodden argue that while clean rooms respond to legitimate privacy, ethical, and legal concerns, their design severely constrains the range of researchers and research methods that can use platform data. The paper frames clean rooms as a governance and power question about who controls authoritative platform data, and concludes that regulators must scrutinise not just whether platforms grant access under laws like the EU Digital Services Act (DSA), but whether that access is genuinely useful.

## Key Contributions

- A concrete, practitioner-informed account of how MCL's VDE and SRE environments actually operate and evolve.
- A systematic critique of the clean room model's methodological and equity limitations for social media research.
- Highlights the underexplored downstream effects of DSA Article 40 implementation on real-world research usability.
- Extends the clean room critique beyond social media by connecting it to news-content databases like ProQuest TDM Studio.
- Guidance to legislators and regulators to attend not just to access provision but to its practical adequacy.

## Methods

Critical, descriptive analysis grounded in the authors' hands-on experience with clean room infrastructures. The core is a detailed case description of the MCL and its two access chains, with comparative reference to ProQuest's TDM Studio as a non-social-media example of the same philosophy. The analysis is situated within prior scholarship on API closures (the "APIcalypse"), platform data governance, and the DSA.

## Findings

- MCL access replaced CrowdTangle (decommissioned August 2024), reducing access precisely during the final phase of the 2024 US presidential election.
- The original VDE access chain (remote Windows → Linux → Jupyter Notebook querying AWS-hosted data) is cumbersome and especially slow from outside the US.
- The improved SRE uses an Amazon Workspaces secure browser plugin but mandatorily deletes all accessed data on the first of each month, obstructing longitudinal studies.
- Restriction to Jupyter Notebooks with limited packages excludes researchers lacking coding skills and those from media, communication, and political communication disciplines.
- Clean rooms lack qualitative coding tools (NVivo, MaxQDA), spreadsheets, and open-Web access, preventing use of commercial LLMs and hindering mixed-methods work.
- Clean rooms exist in isolation, blocking cross-platform dataset combination and limiting comparative analysis to high-level aggregates.
- The EU has begun proceedings against Meta and TikTok for failing DSA transparency and data-access obligations.
- Clean rooms structurally privilege quantitative, code-based analysis and well-resourced Global North teams, reinforcing WEIRD/English-language bias.

## Connections

This paper is a central node in the platform-data-access-and-governance debate, complementing broader assessments of the DSA and post-API research landscape such as [[Bruns2026-yv]], [[Bruns2025-fz]], [[Rieder2025-ju]], and [[Ohme2026-nv]]. Its critique that clean rooms obstruct commercial LLM use and mixed-methods work speaks directly to computational content-analysis approaches that presume flexible data handling, including [[Balluff2026-if]] and [[Manovich2026-ih]]. Related work on TikTok's own research data access and cross-platform limitations includes [[Waight2026-ts]] and [[Waight2025-al]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bruns2026-pn.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-platforms-lock-the-doors-to/id1866587707?i=1000777535116)
