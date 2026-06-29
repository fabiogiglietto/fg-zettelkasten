---
title: "Generative AI, large language models, and their agentic framing in news media"
aliases: ["Generative AI, large language models, and their agentic framing in news media"]
authors: ["Dennis Nguyen", "Magdalena Wischnewski"]
year: 2026
doi: 10.1007/s00146-026-03070-1
bibtex_key: Nguyen2026-vm
topics: [generative-ai-and-media]
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

This paper investigates how English-language news media linguistically construct large language models (LLMs) and generative AI, with particular attention to *mentalistic-agentic* framings that attribute human-like cognition to these systems. Drawing on a corpus of 18,032 articles from 15 outlets across Europe, Asia, North America, and the Middle East (2022–2024), the authors combine computational NLP with manual content analysis to map thematic emphases, isolate LLM-centric coverage, and detect anthropomorphic metaphors. They argue that mentalistic framings are present but neither dominant nor uniform, varying more by outlet and editorial culture than by region. Crucially, the authors resist a blanket critique of anthropomorphic language: such framings can reproduce corporate hype, serve as conventional explanatory shorthand, or function as adversarial critique. The paper positions journalism as a central site where public epistemologies of AI are negotiated.

## Key Contributions

- A text-level, LLM-specific (rather than AI-general) analysis of journalistic framing.
- An empirically grounded, multi-functional account of anthropomorphic language in AI news — challenging the assumption that it uniformly fuels hype.
- A cross-regional comparison testing whether AI framings are globally uniform or culturally differentiated.
- A replicable mixed-methods pipeline integrating BERTopic, dependency parsing, dictionary-based mentalism detection, and manual coding.
- A contribution to debates on AI imaginaries, public epistemology, and critical AI literacy in journalism.

## Methods

A mixed computational–manual design. Articles were retrieved from Nexis and preprocessed with SpaCy's transformer model. BERTopic (run 20 times; mean pairwise Jaccard 0.75) produced a 316-cluster solution inductively labeled into 24 meta-frames. A validated RegEx classifier isolated 1,631 LLM-centric articles. Dependency parsing identified 2,188 sentences with LLMs as grammatical subjects, which were then manually coded for agentic framing (Krippendorff's α = 0.76) and mentalistic framing using Schweitzer et al.'s Mind Perception Dictionary (α = 0.78). Word2Vec embeddings probed semantic neighborhoods of "ChatGPT" and "Bard/Gemini"; chi-square tests and Cramér's V assessed associations with region and outlet.

## Findings

- AI articles form a small but growing share of news output (e.g., 0.9% at NYT).
- A techno-capitalist master frame dominates globally; secondary emphases diverge — risk/ethics in Europe and North America; education, applications, and industry in Asia (χ²(46) = 1399.64, p < 0.001).
- Only 9.2% of AI articles are LLM-centric, and ChatGPT appears in 82.5% of these, dwarfing Gemini/Bard (15.7%), Claude (2.5%), and Mistral (1%).
- 45.5% of LLM articles present the technology as agentic, but only 8.8% deploy explicitly mentalistic-agentic framings (0.8% of full corpus); no experiential/emotional framings were detected.
- Mentalistic framing varies significantly by outlet (NYT, Straits Times, AFP over-represented) but not by region (p = 0.75).
- Only 6.19% of LLM-subject sentences contain negations denying agency — explicit critical pushback is rare.
- Anthropomorphic language serves diverse rhetorical functions, from uncritical reproduction of corporate narratives to adversarial critique (e.g., chatbots as "bullshitters").
- ChatGPT clusters semantically with education; Bard/Gemini clusters around user interaction and "hallucination."

## Connections

This paper sits within an emerging strand of LLM-and-media scholarship attentive to how generative AI is publicly represented and discursively shaped. It connects most directly to work on AI hype, narrative framing, and journalistic practice such as [[Waight2026-ts]], [[Waight2025-al]], [[Achmann-Denkler2026-lx]], and [[Dierickx2026-tw]], and complements studies of how LLMs themselves construct or distort discourse, such as [[Tornberg2026-lc]] and [[Le-Mens2025-qz]]. Its concern with public epistemology and sociotechnical imaginaries also resonates with [[Schiffrin_undated-gi]] on news ecosystems shaped by generative AI.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Nguyen2026-vm.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/fgs-research-radio-does-chatgpt-really-think-how-news/id1866587707?i=1000769065452)
