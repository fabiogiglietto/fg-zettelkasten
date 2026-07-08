---
title: "Emergent structures of attention on social media are driven by amplification and triad transitivity"
aliases: ["Emergent structures of attention on social media are driven by amplification and triad transitivity"]
authors: ["Alyssa H Smith", "Jon Green", "Brooke F. Welles", "David Lazer"]
year: 2025
doi: 10.1093/pnasnexus/pgaf106
bibtex_key: Smith2025-kc
topics: [computational-network-structure-analysis]
citation_count: 0
open_access: false
source_url: https://doi.org/10.1093/pnasnexus/pgaf106
podcast_url: 
pdf_available: true
discovery_date: 2025-04-15T00:00:00Z
---

# Emergent structures of attention on social media are driven by amplification and triad transitivity

> Smith, A. H., Green, J., Welles, B. F., & Lazer, D. (2025). Emergent structures of attention on social media are driven by amplification and triad transitivity. *PNAS Nexus*, *4*, gaf106. https://doi.org/10.1093/pnasnexus/pgaf106
>
> [View paper](https://doi.org/10.1093/pnasnexus/pgaf106)

## Summary

This paper introduces the concept of the **attention broker** (*tertius amplificans*, "the third who amplifies") as a scaled, social-media-native extension of Obstfeld's *tertius iungens*. The authors argue that triad transitivity in directed online networks is partly produced by a local causal mechanism: when a high-degree account amplifies another user's content with attribution (e.g. via retweet), the broker's followers form new ties to the amplified account, closing open triads into transitive ones. Using two contrasting case studies—Jorts the Cat (pro-union) and J.K. Rowling (TERF advocacy)—and a novel API technique that recovers time-stamped follow events, the paper offers difference-in-differences evidence that amplification causally accelerates tie formation, providing a micro-mechanism for a long-observed macro-structural regularity.

## Key Contributions

- **Theoretical:** introduces *tertius amplificans* / attention brokerage as an amplification-based extension of *tertius iungens*, applicable to any sociotechnical system with attributed resharing.
- **Methodological:** documents an exploit of the Twitter/X V1 API cursor parameter (encoding a modified Unix nanosecond timestamp) to retrieve time-bounded follower events, enabling precise temporal analysis of tie formation.
- **Empirical:** delivers causal (DiD) evidence that amplification by influential accounts generates transitive triads, across two ideologically and structurally divergent cases.
- **Conceptual:** links local micro-mechanisms to macro network properties, complementing Schelling-style accounts of how local rules generate global structure and addressing a causal gap in brokerage literatures.
- **Open science:** releases anonymized data (via SOMAR/ICPSR) and code for the cursor-based collection method.

## Methods

- Two-case comparative design: Jorts the Cat (~200K followers, Dec 2021–Mar 2022) vs. J.K. Rowling (~14M followers, Jun 2018–Mar 2023).
- Cursor-based collection of time-bounded following events around each retweet event; broker timelines collected via the `focalevents` package, restricted to simple retweets (quote tweets excluded to avoid "dunking").
- Hand-coding of 646 (Jorts) and 534 (Rowling) retweeted accounts by four coders along cause-alignment (union/TERF) and interest-actor status, with adjudication.
- Treatment motif = transitive triad (follower–broker–retweeted); control motif = open triad (nonfollower–broker–retweeted); 2-week pre/post windows.
- Attentive population estimated using POPAN Jolly-Seber mark-recapture (Program MARK).
- Two-stage event-study DiD (Gardner) with account and time fixed effects, plus Rambachan-Roth sensitivity analysis for parallel-trends violations.

## Findings

- Day-0 treatment effects are positive and statistically significant for both brokers: their followers follow the amplified account at substantially higher rates than nonfollowers.
- Effects are heterogeneous by content type: Jorts's brokerage is strongest for union-aligned accounts; Rowling's effect is significant across categories but largest for TERF interest-actor accounts.
- Small positive *pre*-retweet effects suggest incidental prior exposure also contributes; a post-spike decline implies amplification *accelerates* ties that would have eventually formed, depleting a latent-follower pool rather than persuading the indifferent.
- Rambachan-Roth sensitivity analyses show parallel-trends violations would need to be more than 4× larger post- than pre-retweet to overturn the main results.
- Attentive populations vary widely (e.g. ~164K Jorts followers vs. ~17.9M nonfollowers; ~841K Rowling followers vs. ~2.68M nonfollowers in the sampled set).

## Connections

No other papers were provided under shared topics, so there are no in-corpus wikilinks to make here. Intellectually, the paper sits between classical brokerage and structural-holes theory (Burt, Obstfeld, Simmel/Granovetter on triads) and computational work on virality, influencer effects, and platform affordances, offering a causal bridge between the two literatures.
