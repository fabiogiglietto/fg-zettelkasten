---
title: "Community-driven API and AI writer design for openly scaling Community Notes"
aliases: ["Community-driven API and AI writer design for openly scaling Community Notes"]
authors: ["Brad Miller", "Jay Baxter", "Jiansong Chao", "Keith Coleman", "Sophie Hilgard", "Daniel Ortiz"]
year: 2026
doi: 
bibtex_key: Miller2026-cp
topics: [platform-governance-data-access, information-disorder-disinformation]
citation_count: 0
open_access: true
source_url: http://arxiv.org/abs/2609.40067v1
podcast_url: https://github.com/fabiogiglietto/research-radio/releases/download/audio/Miller2026-cp.mp3
pdf_available: true
discovery_date: 2026-10-16T14:29:24.642888Z
---

# Community-driven API and AI writer design for openly scaling Community Notes

> Miller, B., Baxter, J., Chao, J., Coleman, K., Hilgard, S., & Ortiz, D. (2026). Community-driven API and AI writer design for openly scaling Community Notes. *arXiv [cs.SI]*.
>
> [View paper](http://arxiv.org/abs/2609.40067v1)

## Summary

This paper documents the design and real-world operation of X's Community Notes AI Note Writer API and the accompanying open-source Community Writer (CW), an AI client that proposes fact-checking notes. The central argument is that AI can scale the *production* of context on a platform without displacing human authority over what gets shown: the API changes how notes can be written but preserves the founding Community Notes principle that human raters decide, via a bridging/consensus algorithm, which notes display broadly. The authors frame the system around a core constraint — contributor rating attention is finite — and present engineering mechanisms plus a June 2026 empirical evaluation showing that AI note writing is additive and complementary to human contributions.

## Key Contributions

- Documentation of an open, decentralized AI Note Writer API, including an earn-in admissions process, a non-linear quota system tied to writer hit rate, and a hierarchical feed structure (Small/Large/XL/XXL plus Retry/Revise queues).
- Release of the Community Writer as Apache 2.0 open-source software, including prompts, feature extraction, and model training code.
- Attention-economizing mechanisms (Notable Post Model, rejectors, Deletion Model) that scale note production while conserving finite human rating effort.
- An evaluation framework introducing latency/lead-time, quality, and quantity metrics across topics, distinguishing top human contributors from AI clients — moving past prior offline or single-client evaluations.

## Methods

The authors describe a five-function AI API embedded in the broader X API, with earn-in gates (URL validity, harassment classifier, ClaimOpinion checks on recent notes) and a quota tied to hit rate. Posts are routed through a feed hierarchy based on explicit note requests, implicit engagement, and requester helpfulness. The open-source CW pipeline combines a Notable Post Model (an MLP over engagement, author, and context features including all-mpnet-base-v2 embeddings), two writing models (Grok 4.20 and a post-trained CN Grok), four rejectors, and a logistic-regression Deletion Model; a ClaimOpinion evaluator fine-tunes DistilRoBERTa-base. Empirical evaluation ran over a frozen system from June 2–29, 2026, measuring CRH rates, note views, ratings consumed, latency, and topic coverage, with AUC analysis, z-tests, and Wilson confidence intervals.

## Findings

- AI writers increased daily Currently-Rated-Helpful (CRH) note volume by 86.0% since the API's September 2025 launch.
- The Community Writer produced 41% of proposed notes but 52% of CRH notes and 55% of CRH note views, while consuming only 22% of contributor ratings.
- The CW submitted the first non-deleted note on 60% of posts (and the first AI note on 95%), showing a clear speed advantage.
- AI and human writing are complementary: among posts with CRH notes, 42% had only AI notes, 30% had only human notes, and 41% had no AI CRH note at all.
- The Notable Post Model is most selective on large, sparse feeds (passing only 17.1% of XXL posts) while retaining most human-CRH posts; rejectors produced 7.9–10.5% CRH rates per feed.
- A CW rating had a 29% chance of leading to a CRH note versus 17% for top human writers; human writers averaged 10.4% CRH.
- Of 65 accounts that began earn-in, 32 earned writing ability and 19 stayed active; 54% of non-majority-rating notes received fewer than 10 ratings.

## Connections

This paper extends the empirical literature on Community Notes' accuracy and effect on misinformation, connecting to work such as [[Allen2025-ot]], [[Murtfeldt2025-wu]], and [[Bak-Coleman2025-pm]] on crowdsourced fact-checking and bridging-based moderation. It speaks directly to debates on platform governance and data access raised in [[DeVerna2025-dl]] and to broader concerns about scaling fact-checking against information disorder. As a self-described first account of an open, demand-driven AI note-writing API, it situates AI-assisted content moderation within the human-authority framing that distinguishes it from fully automated moderation approaches.

## Podcast

A [research-radio](https://fabiogiglietto.github.io/research-radio/) episode discusses this paper: 🎧 [MP3](https://github.com/fabiogiglietto/research-radio/releases/download/audio/Miller2026-cp.mp3) · [Spotify](https://open.spotify.com/show/5V99ieB2ljNvcwPZ53EoPX)
