---
title: "The challenges of working with platform data from clean room environments"
aliases: ["The challenges of working with platform data from clean room environments"]
authors: ["Axel Bruns", "Laura Vodden"]
year: 2026
doi: 10.25358/openscience-15825
bibtex_key: Bruns2026-pn
topics: [platform-data-access-governance, llm-assisted-content-analysis]
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

This report by Bruns and Vodden examines the rise of "clean room" data access environments as the dominant model through which major platforms now supply research data, following the closure of open APIs after the Cambridge Analytica scandal. Focusing on the Meta Content Library (MCL) and its two access frameworks, the authors argue that while clean rooms address legitimate privacy, ethical, and legal concerns, their design severely constrains which researchers and which methods can actually make use of platform data. They situate their critique within the arc of platform studies — from the permissive API "Wild West," through the "APIcalypse," to today's regulated but restrictive "walled gardens" — and conclude that regulators must scrutinise not only whether platforms grant access under laws like the EU Digital Services Act, but whether that access is genuinely useful for research.

## Key Contributions

- A concrete, practitioner-informed account of how the Meta Content Library's Virtual Data Enclave (VDE) and newer Secure Research Environment (SRE) actually operate and evolve.
- A systematic critique of the methodological and equity limitations of the clean room model for social media research.
- Attention to the underexplored downstream effects of DSA Article 40 implementation on real-world research usability.
- Extension of the clean room critique beyond social media by connecting it to news-content databases like ProQuest's TDM Studio.
- Practical guidance for legislators and regulators to attend not just to access provision but to its adequacy.

## Methods

The paper offers a critical, descriptive analysis of clean room data access infrastructures grounded in the authors' hands-on experience. It provides a detailed case description of the MCL and its two access frameworks — the VDE hosted via SOMAR/ICPSR and the newer SRE — with comparative reference to ProQuest's TDM Studio as a non-social-media example of the same philosophy. The analysis is situated within prior scholarship on API closures, platform data governance, and the DSA.

## Findings

- MCL access replaced CrowdTangle (decommissioned August 2024), reducing data access precisely during the final phase of the 2024 US presidential election.
- The original VDE access chain (remote Windows machine → Linux machine → Jupyter Notebook querying AWS-hosted data) is cumbersome and especially slow from outside the US.
- The improved SRE uses an Amazon Workspaces Secure Browser plugin but mandatorily deletes all accessed data from the working directory on the first of each month, obstructing longitudinal studies.
- Restriction to Jupyter Notebooks with limited packages excludes researchers lacking coding skills and those from media, communication, and political communication disciplines.
- Clean rooms lack qualitative coding tools (e.g., NVivo, MaxQDA), spreadsheets, and open-Web access, preventing use of commercial LLMs and hindering mixed-methods work.
- Clean rooms exist in isolation, preventing combination of datasets across platforms and limiting cross-platform analysis to high-level aggregate observations.
- The clean room model embeds a philosophy that distrusts researchers' data handling, privileges quantitative code-based analysis, and widens the resource gap between well-funded Global North teams and researchers in the Majority World.
- The EU has begun proceedings against Meta and TikTok for failing their DSA transparency and data-access obligations.

## Connections

This paper is a central reference point for the platform-governance-and-data-access strand, complementing other critical accounts of DSA implementation and post-API research infrastructures such as [[Rieder2025-ju]], [[Bruns2025-fz]], and [[Bruns2026-yv]]. Its concern that clean rooms obstruct commercial LLM use and mixed-methods coding connects to the computational-annotation literature — e.g. [[DeVerna2025-dl]] and [[Le-Mens2025-qz]] — where the very tools clean rooms exclude are increasingly central to research practice.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bruns2026-pn.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-when-platforms-lock-the-doors-to/id1866587707?i=1000777535116)
