---
title: "Generative AI, large language models, and their agentic framing in news media"
aliases: ["Generative AI, large language models, and their agentic framing in news media"]
authors: ["Dennis Nguyen", "Magdalena Wischnewski"]
year: 2026
doi: 10.1007/s00146-026-03070-1
bibtex_key: Nguyen2026-vm
topics: [generative-ai-imaginaries, platform-critique-anniversary-essays]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1007/s00146-026-03070-1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Nguyen2026-vm.mp3
pdf_available: true
discovery_date: 2026-05-15T05:52:01.125136Z
---

# Generative AI, large language models, and their agentic framing in news media

> Nguyen, D., & Wischnewski, M. (2026). Generative AI, large language models, and their agentic framing in news media. *AI & SOCIETY*. https://doi.org/10.1007/s00146-026-03070-1
>
> [View paper](https://doi.org/10.1007/s00146-026-03070-1)

## Summary

This study asks how English-language news media linguistically construct large language models (LLMs) and generative AI, with particular attention to *mentalistic-agentic framings* — language that attributes human-like cognitive or experiential capacities to these systems. Drawing on media framing theory and science and technology studies (notably sociotechnical imaginaries), the authors analyze 18,032 articles from 15 outlets across Europe, Asia, the Middle East, and North America (2022–2024). Their central argument is nuanced: mentalistic framings do appear in journalistic discourse but are neither dominant nor uniformly problematic. Anthropomorphic language can reproduce corporate hype, but it can also serve routine explanatory simplification or adversarial critique. The paper positions journalism as a key site where public epistemologies of AI are co-produced, and resists a one-dimensional condemnation of anthropomorphism.

## Key Contributions

- Fine-grained, text-level analysis of how LLMs *specifically* (not AI broadly) are linguistically framed in news.
- Empirical grounding for normative debates on anthropomorphic AI language, showing it is not uniformly tied to hype.
- A comparative cross-cultural dimension testing whether framings are globally uniform or culturally differentiated.
- A replicable mixed-methods pipeline: BERTopic topic modeling, dependency parsing, dictionary-based mind-perception detection, and manual coding.
- Contribution to debates on AI imaginaries, public epistemology, and critical AI literacy in journalism.

## Methods

Mixed computational and manual content analysis of a Nexis-sourced corpus (Jan 2022–Aug 2024). Preprocessing used SpaCy's transformer model; BERTopic (run 20 times for stability, mean pairwise Jaccard 0.75) yielded a 316-cluster solution labeled inductively into emphasis frames and 24 meta-frames. A RegEx classifier (>95% accuracy) identified 1,631 LLM-centric articles. Sentence-level dependency parsing detected LLMs as grammatical subjects (2,188 subject-sentences), which were manually coded for agentic framing (α = 0.76) and mentalistic/experiential framing using Schweitzer et al.'s Mind Perception Dictionary (α = 0.78). Word2Vec embeddings explored semantic neighborhoods, and chi-square tests with Cramér's V assessed framing associations with region and outlet.

## Findings

- AI articles are a small share of total news output (e.g., 0.9% of NYT) but grew over the period.
- A techno-capitalist master frame dominates globally; secondary themes diverge regionally — European/North American outlets emphasize risks/ethics, Asian outlets emphasize education, applications, and industry (χ²(46) = 1399.64, p < 0.001).
- Only 9.2% of AI articles are LLM-centric; ChatGPT appears in 82.5% of these, dwarfing Gemini/Bard (15.7%), Claude (2.5%), and Mistral (1%).
- 45.5% of LLM articles present the technology as agentic, but only 8.8% (0.8% of the full corpus) use explicitly mentalistic-agentic framings; no experiential/emotional framings were found.
- Framing distribution differed by outlet (χ²(12) = 74.00, p < 0.001; V = 0.06) but *not* by region (p = 0.75), implicating editorial and individual journalistic practice over culture.
- Critical denials of agency (negated constructions) are rare (6.19%).
- Anthropomorphic language serves multiple functions — corporate reproduction, explanation, and critique (e.g., calling chatbots "dumb" or "bullshitters").
- Embeddings cluster ChatGPT with education terms and Bard/Gemini with user-interaction and limitation terms like "hallucination."

## Connections

This paper's focus on media framing and public epistemology of generative AI connects it to work on how the public perceives and reasons about AI systems and to journalism-facing research on AI in newsrooms — see [[Dierickx2026-tw]] on AI and journalistic practice, [[Beacken2026-zb]] and [[Baym2026-tr]] on public perceptions and discourse around AI. Its concern with hype, anthropomorphic imaginaries, and the risks of inflated AI claims also sits alongside [[Schiffrin_undated-gi]] on media narratives about AI.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Nguyen2026-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-does-chatgpt-really-think-how-news/id1866587707?i=1000769065452)
