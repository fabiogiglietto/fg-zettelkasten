---
title: "Re-generating hate"
aliases: ["Re-generating hate"]
authors: ["Fraser Crichton", "Guillen Torres"]
year: 2026
doi: 10.1177/29768624261449726
bibtex_key: Crichton2026-kn
topics: [generative-ai-and-synthetic-media, online-radicalization-and-extremism-on-platforms]
citation_count: 1
open_access: false
source_url: https://doi.org/10.1177/29768624261449726
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Crichton2026-kn.mp3
pdf_available: true
discovery_date: 2026-10-02T06:43:34.645266Z
---

# Re-generating hate

> Crichton, F., & Torres, G. (2026). Re-generating hate. *Platforms & Society*, *3*. https://doi.org/10.1177/29768624261449726
>
> [View paper](https://doi.org/10.1177/29768624261449726)

## Summary

This short article investigates how generative AI has become structurally entangled with far-right propaganda ecosystems, using the 2023 Dublin riots and 2024 Southport unrest as framing events. The authors build a "re-generative" pipeline that converts extremist images collected from Telegram and X into text prompts and then regenerates new images through commercial AI models. Rather than neutralizing hateful content, these systems sanitize its most explicit markers while preserving, displacing, or rearticulating the underlying ideological bias. The central argument is that the affinity between far-right visual culture and generative AI is a structural feature of the models' design — rooted in training data and algorithmic architecture — not an accidental byproduct.

## Key Contributions

- Introduces the concept of a **re-generative loop** as both an analytical and methodological device for studying model bias.
- Demonstrates empirically, through a reproducible pipeline, how commercial generative models transform and launder far-right visual propaganda.
- Reframes concern about AI-generated extremist imagery away from deepfake-style deception toward **ideological transmission and amplification**.
- Links the aesthetic logics of commercial AI models (e.g., a 1950s Americana aesthetic) to far-right political imaginaries, arguing bias is a design feature rather than a flaw.

## Methods

The study is framed as a **media experiment**. Data were gathered by combining manual curation of far-right Telegram channels and X accounts with automated scraping — Telegram extraction via Bellingcat's Cisticola framework (built on Telethon) and Twitter via the Digital Methods Initiative's Zeeschuimer tool — yielding a corpus of 256 images (236 Telegram, 20 Twitter). Images were converted to text prompts using Replicate/Methexis Inc's Img2prompt model (chosen for zero-shot capability, low cost, and open-source status) and regenerated as new images using Stability AI's SDXL. The resulting image pairs were qualitatively curated and presented in a comparison table organized around a shared aesthetic.

## Findings

- The captioning model (Img2prompt) defaulted to blandness, declined to report race or ethnicity, and failed to recognize anti-Semitic imagery.
- The regeneration model (SDXL) imposed a **1950s Americana aesthetic** that appeared independent of the input prompts, signalling model-level bias.
- Contentious content was not removed but reconfigured into subtler ambient cues (e.g., a middle finger morphed into a "V for victory" sign) that remain legible to in-group audiences.
- Sanitization of explicit markers softens or displaces problematic ideological visions rather than eliminating them, keeping them meaningful for sympathetic viewers.

## Connections

This paper sits at the intersection of generative-AI harms and far-right visual culture, complementing work on radical-right aesthetics and multimodal propaganda such as [[Askanius2026-de]] and on AI's role in extremist content production like [[Rothut2026-or]] and [[Rothut2026-wt]]. Its reframing away from deepfake deception toward ideological transmission usefully contrasts with persuasion- and deception-focused studies of synthetic media such as [[Hameleers2026-mc]] and [[Hackenburg2026-ud]].

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Crichton2026-kn.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
