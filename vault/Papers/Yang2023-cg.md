---
title: "Visual misinformation on Facebook"
aliases: ["Visual misinformation on Facebook"]
authors: ["Yunkang Yang", "Trevor Davis", "Matthew Hindman"]
year: 2023
doi: 10.1093/joc/jqac051
bibtex_key: Yang2023-cg
topics: [misinformation-exposure-recalibration, information-operations-disinformation-narratives]
citation_count: 81
open_access: false
source_url: https://doi.org/10.1093/joc/jqac051
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445487Z
---

# Visual misinformation on Facebook

> Yang, Y., Davis, T., & Hindman, M. (2023). Visual misinformation on Facebook. *Journal of Communication*. https://doi.org/10.1093/joc/jqac051
>
> [View paper](https://doi.org/10.1093/joc/jqac051)

## Summary

This paper delivers the first large-scale, platform-complete measurement of image-based political misinformation on Facebook, analyzing nearly 13.7 million image posts from 14,532 pages and 11,454 public groups collected during the final months of the 2020 U.S. election campaign. Its central argument is methodological as much as empirical: prior work that operationalizes misinformation exclusively as links to noncredible domains has systematically undercounted the problem, because image posts — the single most common political post type — are entirely invisible to link-based measurement. Using perceptual hashing and computer vision to scale coding across millions of images, the authors estimate that roughly one in five sampled political images contained misinformation, with a stark partisan asymmetry favoring the right. Notably, they find that misleading images do *not* generate elevated engagement once partisanship and audience size are controlled, complicating a common assumption in the literature.

## Key Contributions

- First valid, platform-scale prevalence estimates of visual political misinformation on Facebook (and on any social platform).
- A scalable computational pipeline (perceptual hashing + facial recognition via AWS Rekognition) for studying visual political communication at the scale of millions of images.
- A direct methodological challenge to the "misinformation is minimal or declining" consensus, showing that image posts are a large, previously ignored vector.
- Post-level classification of misinformation rather than publisher-domain-level classification, reducing measurement error.
- Documentation of the field's textual bias: only 9 of 135 reviewed communication journal articles (2017–2021) focused on images.

## Methods

The authors assembled a near platform-complete "megalist" of top U.S. political pages and groups, collecting 13,723,654 image posts (Aug–Oct 2020) via CrowdTangle and licensed vendors (no scraping). AWS Rekognition identified political figures to build a 572,857-post public-figures sub-corpus, and pHash detected duplicate/reposted images. Human coders manually labeled four samples — a 1,000-image Overall Sample, a 1,000-image Public Figures Sample, and the top 300 most-reposted images from groups and from pages — with misinformation defined by contemporaneous expert consensus and reverse image search. Reliability was strong (Krippendorff's α = 0.78 for misinformation). Analysis included power-law fitting to estimate corpus coverage, difference-of-means tests, LOWESS, and negative binomial regressions controlling for partisanship and audience size.

## Findings

- ~20–25% of political images in the Overall Sample contained misinformation (17.5–21.6% in the Public Figures Sample).
- Sharp partisan asymmetry: 39% of right-leaning vs. 5% of left-leaning images were misleading (Overall Sample); right-leaning images were 5–8× more likely to mislead.
- Among top-reposted images, ~30% (groups) and ~26% (pages) were misleading, again concentrated on the right.
- Four common formats: altered images, misleading-text memes, unaltered images with false captions, and screenshots of misleading posts.
- Recurring themes: Biden as senile, attacks on Hunter Biden, Democrats endorsing violence, and QAnon promotion.
- No significant misinformation–engagement relationship once controls applied (near-zero T-statistics; p = .88, .92).
- The corpus captures ≥94% of page and ≥95% of group interactions given power-law engagement concentration.
- Image posts (13.7M) outnumbered link posts (9.4M), suggesting images may be the highest-volume misinformation vector.

## Connections

This paper's core methodological critique directly engages the link-based prevalence tradition that has argued misinformation exposure is small or concentrated — work such as [[Guess2020-rr]], [[Grinberg2019-ua]], [[Guess2019-ym]], and [[Allen2020-nj]] — by showing that image posts fall outside those measurement frames. Its finding that misleading content does *not* enjoy an engagement advantage complicates the widely cited claim that falsehood spreads faster (see [[Vosoughi2018-at]]), while its documentation of partisan asymmetry connects to debates over the demand side of misinformation in [[Osmundsen2021-et]]. The visual-first, computational classification approach also relates to broader efforts to move beyond domain-level measurement discussed in [[Budak2024-ef]].
