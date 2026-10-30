---
title: "If Likes Were Votes: An Empirical Study on the 2011 Italian Administrative Elections"
aliases: ["If Likes Were Votes: An Empirical Study on the 2011 Italian Administrative Elections"]
authors: ["Fabio Giglietto"]
year: 2012
doi: 10.2139/ssrn.1982736
bibtex_key: Giglietto2012-32b6b551
kind: own
topics: [italian-political-communication-elections, social-media-research-methods-infrastructure]
citation_count: 35
open_access: true
source_url: https://doi.org/10.2139/ssrn.1982736
podcast_url: 
pdf_available: true
discovery_date: 
---

# If Likes Were Votes: An Empirical Study on the 2011 Italian Administrative Elections

> Giglietto, F. (2012). If Likes Were Votes: An Empirical Study on the 2011 Italian Administrative Elections. *Elsevier BV*. https://doi.org/10.2139/ssrn.1982736
>
> [View paper](https://doi.org/10.2139/ssrn.1982736)

## Summary

This paper tests the popular hypothesis that social media popularity can forecast election outcomes, using the 2011 Italian administrative elections as a fresh empirical case. Giglietto collected Facebook Like counts for mayoral candidates across Italy's 29 provincial capitals and built two forecasting models: one predicting candidate vote shares and one predicting the winning candidate. The results are deliberately mixed. Facebook Like share does *not* reliably predict vote share — error margins far exceed what would be tolerable for conventional polling. Yet Facebook popularity does carry a weak signal of candidate viability: the most popular candidate on Facebook won or placed second in 82% of contests. Rather than resolving the contradictory prior literature on social media election forecasting, the study confirms that the relationship is real but noisy, and crucially context- and party-dependent.

## Key Contributions

- Introduces the Italian administrative-election context to a literature previously dominated by US and German (Twitter-centric) cases.
- Proposes two complementary forecasting models — a vote-share prediction model and a winner-prediction precision index.
- Develops refined evaluation metrics: the Candidate Prediction Gap (CPG), Municipality Prediction Gap (MPG), Party Prediction Gap (PPG), and a 0–10 prediction precision index.
- Documents systematic *partisan bias* in social media prediction — overestimation of extreme parties and underestimation of the center-right — suggesting corrective weighting analogous to poll adjustment.

## Methods

Giglietto sampled 229 mayoral candidates across the 29 provincial capitals and located 104 candidate Facebook pages (~44.5% coverage) via Facebook's internal search. Like counts were harvested through periodic Graph API queries between 25 April and 15 May 2011 (179,003 total Likes across monitored pages at the mid-May snapshot). Prediction gaps were computed by comparing each candidate's vote share to their Like share (adapting the Olson and Bunnett 2010 methodology), aggregated to municipality and party levels. Candidates were categorized into seven political areas (extreme right to extreme left), and municipalities grouped by Facebook-coverage proportion and electorate size.

## Findings

- No significant correlation between Facebook popularity share and vote share.
- Average absolute CPG was 15.77% (range 0–84.18%); average ABS[MPG] was 18.99%.
- Prediction error dropped sharply as Facebook coverage rose — ABS[MPG] fell from 29.43% (0–33% of candidates on Facebook) to 11.88% (over 67%).
- Large cities were predicted more accurately (ABS[MPG] 9.52% for electorates over 200,000 vs. ~21% for smaller ones).
- All PPG values were negative (predicted shares typically exceeded actual votes); extreme parties showed the largest gaps, while the center-right was markedly underestimated (ABS[PPG] − PPG = +26.45).
- Average precision index score was 4.71/10; the top Facebook candidate won 39% of races and came second in 43%.

## Connections

This is an early entry in Giglietto's own long trajectory of Italian social-media and electoral research, laying groundwork for later methodological and infrastructural work such as [[Giglietto2019-882f1900]], [[Giglietto2019-e9be81c1]], and [[Giglietto2020-9d8acdd7]], and it sits alongside related Italian political-communication studies like [[Iannelli2015-e0818c3e]] and [[Iannelli2018-ebd918b7]]. Its core concern — whether aggregated social media metrics track real-world political support — directly anticipates debates on the representativeness and partisan skew of platform data examined in [[Barbera2015-fw]].
