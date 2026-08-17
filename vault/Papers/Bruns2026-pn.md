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

This report offers a practitioner-informed critique of the "clean room" data access environments that have become the dominant model for platform-provided research data since the post–Cambridge Analytica "APIcalypse." Focusing on the Meta Content Library (MCL) and its evolving access frameworks — the Virtual Data Enclave (VDE) and the newer Secure Research Environment (SRE) — Bruns and Vodden argue that while clean rooms respond to genuine privacy, ethical, and legal concerns, their design structurally constrains which researchers and which methods can actually make use of platform data. The core argument is that merely mandating access, as under the EU Digital Services Act (DSA), is insufficient: the *manner* of access determines whether it is genuinely useful. Clean rooms are thus framed as a governance and power question about who controls authoritative platform data, with downstream consequences for democratic accountability and global research equity.

## Key Contributions

- A concrete, hands-on account of how MCL's VDE and SRE environments actually operate and evolve in practice.
- A systematic critique of the clean room model's methodological and equity limitations for social media research.
- Highlights the underexplored downstream effects of DSA Article 40 implementation on real-world research usability.
- Extends the clean room critique beyond social media by connecting it to news-content databases like ProQuest's TDM Studio.
- Offers regulators and legislators guidance to attend not just to access provision but to its practical adequacy.

## Methods

Critical, descriptive analysis grounded in the authors' first-hand experience navigating clean room infrastructures. The paper develops a detailed case description of the MCL and its two access frameworks (VDE hosted via SOMAR/ICPSR, and the SRE using an Amazon WorkSpaces Secure Browser plugin), draws a comparative reference to ProQuest's TDM Studio as a non-social-media example of the same philosophy, and situates the analysis within prior scholarship on API closures, platform data governance, and the DSA.

## Findings

- MCL access replaced CrowdTangle (decommissioned August 2024), reducing data access precisely during the final phase of the 2024 US presidential election.
- The original VDE access chain (remote Windows machine → Linux machine → Jupyter Notebook querying AWS-hosted data) is cumbersome and especially slow from outside the US.
- The SRE mandatorily deletes all accessed data from the working directory on the first of each month, obstructing longitudinal studies.
- Restriction to Jupyter Notebooks with limited packages excludes researchers lacking coding skills and those from media, communication, and political communication disciplines.
- Clean rooms lack qualitative coding tools (NVivo, MaxQDA), spreadsheets, and open-Web access, preventing use of commercial LLMs and hindering mixed-methods work.
- Clean rooms exist in isolation, preventing dataset combination across platforms and limiting cross-platform analysis to high-level aggregate observations.
- The clean room model widens the resource gap between well-funded Global North teams and isolated Majority World researchers, reinforcing a WEIRD/English-language bias.
- The EU has begun proceedings against Meta and TikTok over failures to meet DSA transparency and data-access obligations.

## Connections

This paper sits at the centre of ongoing debates about platform data governance and researcher access under the DSA, complementing critical accounts of platform-provided research infrastructures such as [[Rieder2026-pp]], [[Rieder2025-ju]], and [[Bruns2026-yv]]. Its concern with the practical usability and equity of mandated access speaks directly to work on DSA Article 40 implementation and data-access provision like [[de-Vreese2026-zx]] and [[Ohme2026-nv]], while its account of the post-CrowdTangle landscape connects to broader assessments of the shifting API and data-access ecosystem in [[Freelon2024-sc]] and [[Tonneau2025-bv]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Bruns2026-pn.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
