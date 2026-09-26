---
title: "Cracking open the news feed"
aliases: ["Cracking open the news feed"]
authors: ["Andy Guess", "Kevin Aslett", "Joshua Tucker", "Richard Bonneau", "Jonathan Nagler"]
year: 2021
doi: 10.51685/jqd.2021.006
bibtex_key: Guess2021-ym
topics: [misinformation-exposure-recalibration, platform-data-access-governance]
citation_count: 41
open_access: false
source_url: https://doi.org/10.51685/jqd.2021.006
podcast_url: 
pdf_available: true
discovery_date: 2026-09-26T08:39:39.445475Z
---

# Cracking open the news feed

> Guess, A., Aslett, K., Tucker, J., Bonneau, R., & Nagler, J. (2021). Cracking open the news feed. *Journal of Quantitative Description: Digital Media*, *1*. https://doi.org/10.51685/jqd.2021.006
>
> [View paper](https://doi.org/10.51685/jqd.2021.006)

## Summary

This paper offers a large-scale descriptive portrait of how U.S. Facebook users encounter and share news, drawing on the Social Science One "Condor" dataset of URL-level engagement data covering millions of publicly shared links. Uniquely, the dataset lets the authors distinguish *views* (exposure) from *shares*, and combine platform-scale counts with supervised classifiers to categorize content as credible vs. low-credibility, political vs. non-political, and clickbait vs. non-clickbait. The central argument is descriptive rather than causal: low-credibility news is comparatively rare relative to credible news, but its circulation is far from trivial and is markedly concentrated among older and very conservative users, with clear signs of a preference for ideologically congenial misinformation. The paper also functions as a methodological proof of concept for working with differentially-private, aggregated platform data.

## Key Contributions

- First analysis of newly released, differentially-private Facebook engagement data that measures both exposure (views) and sharing of news, allowing the two behaviors to be separated.
- Fine-grained descriptive disaggregation of news into credible/low-credibility, political, and clickbait categories across age and ideological groups.
- A methodological template combining platform-scale URL data with supervised classifiers and misclassification bias correction (Hopkins–King plus bootstrap).
- An empirical descriptive foundation for subsequent research and policy debate on misinformation exposure and consumption.

## Methods

The authors analyze 466,591 URLs first posted in 2018 by U.S. users from the Condor dataset (URLs shared publicly more than 100 times, aggregated by URL-year-month-age-gender-political-page-affinity with Gaussian differential-privacy noise). They construct three binary URL-level measures: credibility (NewsGuard, threshold 60), political vs. non-political (a random forest trained on ~8,552 labeled headlines, ~90% accuracy, F1=0.90), and clickbait (a pre-trained SVM). Classifier misclassification is corrected via the Hopkins–King method with 100-sample bootstrap resampling to produce corrected proportions and confidence intervals. Ideological slant of sources comes from media partisanship scores and manual coding; user ideology comes from Facebook's five-point political page-affinity measure. An updated version corrects for inadvertent Facebook filtering of users lacking page-affinity scores, which shifted estimates slightly without changing the patterns.

## Findings

- Roughly 84% of news shares and 89% of views came from credible domains; about 15% of shares and views were from low-quality domains — roughly one in eight views of at least moderately popular news.
- 27% of news URLs shared by very conservative users were low-quality vs. 9% for very liberal users; for views, 19% vs. 7% — evidence of ideologically congenial misinformation.
- 20% of URLs shared by users 65+ were low-quality vs. 11% for the 24–35 bracket; the age gradient is steepest within the two most conservative groups.
- Older users don't view much more low-credibility news in absolute counts, but it forms a larger *share* of their news (18% vs. 8% for the second-youngest), suggesting sharing differences aren't merely a function of feed exposure.
- Low-quality content is disproportionately political and clickbait: 53.4% of low-quality URLs were political vs. 31.3% of credible; 12.3% were both political and clickbait vs. 6.3% of credible.
- No support that older users share more clickbait (26% for 25–34 vs. 24% for 65+), but strong support that they share more political news (22% vs. 56%).
- Of ~280 billion U.S. URL views in 2018, over 44% were news domains; of ~2.1 billion shares, over 48% were news.

## Connections

This paper sits alongside foundational descriptive work on the prevalence and skewed distribution of fake news exposure, connecting to [[Guess2020-rr]], [[Guess2019-ym]], and [[Grinberg2019-ua]] on the concentration of misinformation among older and conservative users, and to [[Allen2020-nj]] on how small misinformation is relative to the overall news diet. Its emphasis on ideologically congenial sharing links to [[Osmundsen2021-et]] and [[Vosoughi2018-at]], while its reliance on privacy-preserving platform data speaks to ongoing debates on platform-data-access-governance represented here by [[Gonzalez-Bailon2024-rq]] and [[Freelon2018-ao]]. Its exposure-versus-behavior framing also resonates with recalibration work in [[Budak2024-ef]] and [[Allen2024-av]].
