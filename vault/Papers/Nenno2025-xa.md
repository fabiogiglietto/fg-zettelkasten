---
title: "All the (fake) news that’s fit to share? News values in perceived misinformation across twenty-four countries"
aliases: ["All the (fake) news that’s fit to share? News values in perceived misinformation across twenty-four countries"]
authors: ["Sami Nenno", "Cornelius Puschmann"]
year: 2026
doi: 10.1177/19401612241311893
bibtex_key: Nenno2025-xa
topics: [information-disorder, computational-methods-llms]
citation_count: 2
open_access: false
source_url: https://doi.org/10.1177/19401612241311893
podcast_url: 
pdf_available: true
discovery_date: 2025-01-15T00:00:00Z
---

# All the (fake) news that’s fit to share? News values in perceived misinformation across twenty-four countries

> Nenno, S., & Puschmann, C. (2026). All the (fake) news that’s fit to share? News values in perceived misinformation across twenty-four countries. *The International Journal of Press/Politics*, 19401612241311893. https://doi.org/10.1177/19401612241311893
>
> [View paper](https://doi.org/10.1177/19401612241311893)

## Summary

This paper asks whether classic journalistic news values — conflict, negativity, proximity, individualization, and informativeness — are more pronounced in perceived misinformation than in regular news, and whether this pattern holds across both WEIRD and non-WEIRD countries. Drawing on ~82,000 political URLs from Facebook's URL Shares dataset across 24 countries, the authors build an automated multilingual pipeline to detect each news value and compare user-flagged versus unflagged items. They find that flagged content does exhibit elevated news values (especially conflict), but effect sizes are mostly small, and the WEIRD/non-WEIRD divide produces statistically significant though modest differences. The United States and Brazil emerge as distinctive outliers where news values discriminate flagged from unflagged content far more sharply, pointing to the role of polarized electoral contexts. The authors argue that Western-derived news value typologies need theoretical expansion to travel beyond WEIRD settings.

## Key Contributions

- First large-scale, transnational comparison of news values in perceived misinformation that deliberately incorporates non-WEIRD countries.
- A validated computational pipeline combining fine-tuned transformer models (RoBERTa, ConfliBERT, XLM-R), NER with OpenStreetMap matching, and idea density measures to operationalize five news values in multilingual corpora.
- Empirical demonstration that findings from WEIRD-based news values research do not cleanly generalize, motivating expansion of existing typologies.
- Identification of the U.S. and Brazil as a distinct cluster where news values strongly discriminate flagged from unflagged items, foregrounding the role of polarization.
- An openly released dataset to support reproducible cross-cultural misinformation research.

## Methods

The authors sample 12 WEIRD and 12 non-WEIRD countries (per UNCTAD developed/developing classification and Facebook market size), drawing ~5,000 most-flagged and ~25,000 unflagged URLs per country from the Facebook URL Shares dataset (Messing et al. 2020), focused on January 2017 – July 2019. URL content was scraped via the Internet Archive (61.8% retrieval), translated to English using Meta's NLLB, topic-modeled with BERTopic, and filtered for political content via Llama-3 zero-shot classification validated against human coders (α = 0.76). The final corpus of 82,431 political items (25% flagged) was scored on five news values using model-based detectors validated by four student coders (mean α = 0.68). Analysis combined chi-square tests with Cramer's V, t-tests with Cohen's d, and K-Means clustering on per-country effect sizes.

## Findings

- All news values except informativeness are significantly more prevalent in flagged than unflagged items; conflict shows the largest gap (56.8% vs. 52.3%), though Cramer's V ≤ 0.04 throughout.
- In flagged items, individualization is higher in non-WEIRD countries (41.8% vs. 34.3%), while negativity, proximity, and informativeness are higher in WEIRD countries; conflict is equally salient in both.
- Non-WEIRD coverage references WEIRD countries (particularly the U.S.) more than the reverse, indicating asymmetric geographic attention.
- K-Means clustering yields an optimal two-cluster solution: the U.S. and Brazil cluster together with sharply stronger flagged/unflagged differences on conflict, negativity, and individualization; all other countries form the second cluster.
- Informativeness shows the largest cross-country variation and does not align with the WEIRD/non-WEIRD divide, suggesting other structural factors drive it.
- Differences are statistically real but modest, complicating any claim that perceived misinformation is dramatically more sensational than other news.

## Connections

This paper sits alongside cross-national misinformation work such as [[Humprecht2025-ml]] on resilience and [[Cazzamatta2026-lo]] on comparative fact-checking, extending the WEIRD/non-WEIRD critique into news values theory. Its empirical reliance on Facebook URL flagging data connects it to large-scale platform-based studies like [[Gonzalez-Bailon2024-rq]] and [[Budak2024-ef]], while its emphasis on the U.S./Brazil polarization context resonates with work on hyperpartisan and electoral information environments such as [[Rossini2026-jn]] and [[Kansaon2025-id]].
