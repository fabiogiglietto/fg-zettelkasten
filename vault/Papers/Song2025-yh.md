---
title: "The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic"
aliases: ["The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic"]
authors: ["Yunya Song", "Yin Zhang", "Sheng Zou", "Xian Yang", "Qintao Huang"]
year: 2025
doi: 10.1007/s42001-025-00401-y
bibtex_key: Song2025-yh
topics: [coordinated-inauthentic-behavior, information-disorder]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1007/s42001-025-00401-y
podcast_url: 
pdf_available: true
discovery_date: 2025-11-15T00:00:00Z
---

# The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic

> Song, Y., Zhang, Y., Zou, S., Yang, X., & Huang, Q. (2025). The spread of pro- and anti-vaccine views by coordinated communities on facebook during COVID-19 pandemic. *Journal of Computational Social Science*, *8*. https://doi.org/10.1007/s42001-025-00401-y
>
> [View paper](https://doi.org/10.1007/s42001-025-00401-y)

## Summary

This paper offers a cross-national comparison of coordinated link sharing behavior (CLSB) around COVID-19 vaccine discourse on Facebook in the UK and US between January 2020 and October 2022. Drawing on 3.47 million public posts, the authors combine transfer-learning stance classification, CooRnet-based network analysis, manual fact-checking, and structural topic modeling to characterize who coordinates, what they share, and which narratives they amplify. The central argument is that CLSB is not inherently malicious: anti-vaccine coordinators disseminate disproportionately problematic or unverifiable content, while pro-vaccine coordinators amplify institutional sources like the NHS, CDC, and NIH. National political cultures shape the discourse — UK anti-vaccine messaging foregrounds safety and scientific skepticism, while US anti-vaccine messaging centers individual freedom and government distrust.

## Key Contributions

- One of the first systematic UK–US comparisons of CLSB in vaccine discourse on Facebook.
- Reframes CLSB as ideologically agnostic infrastructure, used by both misinformation actors and credible public health communicators.
- Extends Xu and Wang's framework with a six-metric scheme for characterizing the scope and structure of coordinated link sharing networks.
- Integrates network analysis, URL-level fact-checking, and STM to jointly map coordination, content authenticity, and thematic emphasis.
- Draws practical implications for designing culturally tailored, coordination-aware public health communication.

## Methods

The authors collected 3,469,719 English-language Facebook posts via CrowdTangle using COVID-19/vaccine keywords, then classified post-level stance using a CT-BERT model fine-tuned on 5,000 annotated posts (κ = 0.86), yielding four corpora (UK/US × Pro/Anti). CLSB was detected with CooRnet, which flags entities sharing identical URLs within unusually short windows. Networks were characterized with six descriptive metrics plus standard structural attributes (density, modularity, clustering, diameter). Unique URLs were manually fact-checked via Google Fact Check Explorer (94.6% inter-coder agreement) and coded as Problematic, True, or Unknown. Finally, 14-topic STM models with date and country as covariates were fit separately to anti- and pro-vaccine corpora.

## Findings

- CLSB accounted for a large share of nodes in every network: 61.5% (UK-Anti), 38.5% (UK-Pro), 49.8% (US-Anti), 57.6% (US-Pro).
- UK anti-vaccine networks were densest (density 0.01, avg degree 21.88); US pro-vaccine networks were largest and most connected (avg degree 27.54).
- Fact-checking showed sharp credibility asymmetries: only 9.6% of UK-Anti and 12% of US-Anti URLs verified as true, versus 45.6% (UK-Pro) and 40.4% (US-Pro); ~74–80% of anti-vaccine URLs were "Unknown."
- Anti-vaccine topics clustered into Vaccine Safety Issues (59.1%), Vaccine Refusal (27.3%), and Criticism of Politicians/Big Pharma (13.5%).
- Pro-vaccine topics centered on Effectiveness and Safety (38.5%), Vaccination Progress (34.2%), and Efficacy Evidence (27.2%).
- National framings diverged: UK anti-vaccine discourse emphasized trial safety (e.g., AstraZeneca); US anti-vaccine discourse foregrounded freedom and religious exemptions; UK pro-vaccine messaging stressed centralized NHS rollout, while US pro-vaccine messaging stressed incentives and grassroots mobilization.
- Anti-vaccine coordinators in the UK skewed ideological (liberty groups, conspiracy communities); US anti-vaccine networks spanned partisan, religious, and local political pages; pro-vaccine networks were institutionally anchored.

## Connections

This paper sits squarely in the CLSB tradition initiated by Giglietto and colleagues and shares its dual-use reframing of coordination with [[Graham2025-gp]] and [[Graham2026-fb]], which similarly probe whether coordinated behavior should be treated as inherently inauthentic. Its focus on COVID-19 vaccine misinformation ecosystems connects to broader work on problematic health information such as [[Di-Marco2025-aa]], [[Pante2025-pq]], and [[Kansaon2025-id]], while its cross-national comparative design resonates with [[Kuznetsova2025-nu]] and [[Hurcombe2025-cs]]. Methodologically, the CooRnet-based network detection links it to [[Minici2024-tf]] and [[Luceri2025-tr]] on computational approaches to coordination discovery.
