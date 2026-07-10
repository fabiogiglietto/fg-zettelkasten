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

This paper introduces the concept of the **attention broker** (the *tertius amplificans*, or "third who amplifies") as a scaled extension of Obstfeld's *tertius iungens* orientation to social media platforms with many-to-many amplification affordances. The authors argue that the well-documented tendency toward triad transitivity in directed social networks is partly produced by a local, endogenous causal mechanism: when a high-degree account amplifies another user's content with attribution (e.g. a retweet), its followers form new following ties to the amplified account. Using a novel data-collection technique and a difference-in-differences design across two contrasting case studies—Jorts the Cat (pro-union) and J.K. Rowling (TERF advocacy)—they causally identify how amplification accelerates transitive triad closure beyond background virality. The mechanism works through *exposure* rather than persuasion, hastening ties among followers already predisposed to follow the amplified accounts.

## Key Contributions

- **Theoretical**: coins "attention brokerage" / *tertius amplificans*, a scaled, amplification-based extension of the *tertius iungens* applicable wherever attributed resharing occurs (retweets, citations, TikTok duets, corporate memos).
- **Methodological**: documents and operationalizes a Twitter/X V1 API cursor technique (exploiting a modified Unix nanosecond timestamp) to recover time-bounded follower events, enabling precise temporal analysis of tie formation.
- **Empirical**: provides causal (difference-in-differences) evidence that amplification by influential accounts generates transitive triads, across two structurally and ideologically divergent cases.
- **Conceptual bridge**: links local micro-mechanisms to macro-level network properties, offering a causal explanation for the prevalence of transitivity.
- **Open science**: releases an anonymized dataset (SOMAR/ICPSR) and code documenting the cursor-based collection method.

## Methods

A two-case comparative design contrasts Jorts the Cat (~200K followers, Dec 2021–Mar 2022) with J.K. Rowling (~14M followers, Jun 2018–Mar 2023). The authors collected brokers' full timelines via the `focalevents` package, filtered to simple retweets (excluding quote tweets to avoid "dunking"), and hand-labeled 646 (Jorts) and 534 (Rowling) retweeted accounts along cause-alignment and interest-actor dimensions with four coders and a tiebreaker. Treatment motifs (transitive triads: follower–broker–retweeted) and control motifs (open triads: nonfollower–broker–retweeted) were constructed over 2-week pre/post windows around each retweet. Attentive population sizes were estimated using the POPAN Jolly-Seber mark-recapture model in Project MARK. Causal estimates came from a two-stage difference-in-differences event study (Gardner) with account and time fixed effects, plus Rambachan–Roth sensitivity analysis for parallel-trends violations.

## Findings

- For both brokers, the day-0 (retweet day) treatment effect is positive and significant: followers follow the amplified account at much higher rates than nonfollowers.
- Effects are heterogeneous by account type: Jorts's brokerage is strongest for union-related accounts; Rowling's effect is significant across all types but largest for TERF interest-actor accounts.
- Smaller positive pre-retweet effects suggest incidental prior exposure also contributes; a post-spike decline in following rates suggests amplification accelerates ties that would eventually have formed, depleting the pool of latent followers.
- Rambachan–Roth sensitivity analyses show robustness: parallel-trends violations would have to be more than four times larger post-retweet than pre-retweet to overturn key results.
- Estimated attentive populations differ substantially (e.g. ~164K Jorts followers vs. ~17.9M nonfollowers; ~841K Rowling followers vs. ~2.68M nonfollowers in the sampled set).

## Connections

This paper's focus on how amplification by influential accounts reshapes the distribution of attention connects to work on influencer-driven amplification and structural roles in networks such as [[Rothut2026-or]] and [[Bakshy2015-rn]], the latter's exposure-based framing of what circulates on platforms being a natural counterpart to the exposure-not-persuasion mechanism argued here. Its use of case-based, mechanism-oriented network analysis also resonates with computational structural studies like [[Gaisbauer2025-by]] and [[Green2025-ap]], where local processes are linked to emergent macro-level patterns.
