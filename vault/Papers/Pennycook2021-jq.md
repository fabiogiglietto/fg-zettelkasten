---
title: "The psychology of fake news"
aliases: ["The psychology of fake news"]
authors: ["Gordon Pennycook", "David Gertler Rand"]
year: 2021
doi: 10.31234/osf.io/ar96c
bibtex_key: Pennycook2021-jq
topics: [information-operations-disinformation-narratives, political-polarization-partisanship]
citation_count: 9
open_access: false
source_url: https://doi.org/10.31234/osf.io/ar96c
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445552Z
---

# The psychology of fake news

> Pennycook, G., & Rand, D. G. (2021). The psychology of fake news. *Trends Cogn. Sci.*, *25*, 388–402. https://doi.org/10.31234/osf.io/ar96c
>
> [View paper](https://doi.org/10.31234/osf.io/ar96c)

## Summary

This paper reframes the phrase "fake news" not as a neutral descriptor of false content but as a **strategic rhetorical weapon** used to delegitimize political opponents. Pennycook and Rand (via an Italian case study) propose the **Strategic Delegitimization and Selective Amplification (SDSA) model**, which treats each fake news accusation as a triadic interaction between an accuser, a target, and a media outlet that selectively amplifies the accusation according to its editorial leanings. Drawing on a corpus of 2,778 Italian newspaper articles (2020–2024), the study maps who accuses whom and finds a counterintuitive pattern: populist parties are disproportionately the *targets* of fake news accusations rather than the main accusers, and partisan media condition coverage chiefly by emphasizing accusations against ideologically distant actors — a mode the authors call "negative epistemic gatekeeping."

## Key Contributions

- Introduces the **SDSA model**, integrating three literatures — "fake news" as a strategic label, negative campaigning, and political parallelism — into a single replicable framework.
- Advances the study of negative campaigning by folding **media selectivity** into the analysis of epistemic delegitimization.
- Provides large-scale empirical evidence on fake news discourse in a **multiparty, high-parallelism system** (Italy).
- Clarifies the **dual role of populist parties** as both accusers and (especially) targets.
- Reconceptualizes contemporary political parallelism as operating through **negative epistemic gatekeeping** rather than affirmative amplification of allies.

## Methods

The authors built a novel corpus of 2,778 articles from five Italian newspapers spanning the ideological spectrum (La Repubblica, Corriere della Sera, il Giornale, il Fatto Quotidiano, il Manifesto), retrieved from Factiva by searching "fake news" / "notizia falsa" alongside party or leader references. GPT-4 with zero-shot prompting classified actors in text windows as accuser or accused, outputting structured JSON; party affiliations were assigned manually. LLM coding was validated against a stratified 5% manual sample (75% agreement), yielding 1,082 coded observations. Parties were classified as populist/non-populist via The PopuList and placed ideologically using Chapel Hill Expert Survey left–right scores. Analysis used chi-square and proportion tests, negative binomial regression on accusation counts between party pairs, and descriptive party-level share analyses across outlets.

## Findings

- Populist parties made 50.9% of accusations — not above parity (p=.41), so they are **not** disproportionately accusers.
- Populist parties were ~70% of accused actors (p<.001); Lega and FdI were especially likely targets. A significant party-type × role association (χ²(1)=18.58, p<.001) was driven by the accused role.
- Over 80% of accusation dyads crossed opposing ideological blocs; each additional point of left–right distance was associated with ~10% more accusations, but the effect was not significant (p=.11).
- Newspapers amplified proximate-party *accusers* only weakly (H4).
- Newspapers strongly emphasized accusations against ideologically *distant* parties in four of five outlets (La Repubblica 84.4%, il Manifesto 77.8%, il Fatto Quotidiano 59.4%, Corriere della Sera 56.2%).
- Il Giornale was a deviant case with a symmetrical distribution, suggesting it **normalizes** fake news rhetoric rather than deploying it selectively.

## Connections

This work sits at the intersection of the strategic-label view of "fake news" and the study of partisan media systems and affective polarization. It resonates with research on how "fake news" accusations serve elite and partisan delegitimization goals — see Egelhofer2021-lm is not in the register, so more directly it connects to work on partisan asymmetries in misinformation attention such as [[Osmundsen2021-et]] and to broader disinformation-narrative scholarship like [[Farkas2026-lr]] and [[Hameleers2026-mc]]. Its focus on media-politics parallelism and elite polarization also links it to [[Iyengar2019-jj]] on affective polarization.

*(Note: the title and named authors here appear mismatched with the summarized Italian-newspaper study; the connections above are drawn from the described content, and any apparent author discrepancy in the source should be verified.)*
