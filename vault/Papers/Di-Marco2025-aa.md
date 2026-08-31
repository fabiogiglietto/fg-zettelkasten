---
title: "Post-hoc evaluation of nodes influence in information cascades: The case of coordinated accounts"
aliases: ["Post-hoc evaluation of nodes influence in information cascades: The case of coordinated accounts"]
authors: ["Niccolò Di Marco", "Sara Brunetti", "Matteo Cinelli", "Walter Quattrociocchi"]
year: 2025
doi: 10.1145/3700644
bibtex_key: Di-Marco2025-aa
topics: [coordinated-inauthentic-behavior, computational-network-structure-analysis]
citation_count: 7
open_access: false
source_url: https://doi.org/10.1145/3700644
podcast_url: 
pdf_available: true
discovery_date: 2025-05-15T00:00:00Z
---

# Post-hoc evaluation of nodes influence in information cascades: The case of coordinated accounts

> Marco, N. D., Brunetti, S., Cinelli, M., & Quattrociocchi, W. (2025). Post-hoc evaluation of nodes influence in information cascades: The case of coordinated accounts. *ACM Transactions on the Web*, *19*, 1–19. https://doi.org/10.1145/3700644
>
> [View paper](https://doi.org/10.1145/3700644)

## Summary

This paper introduces a post-hoc, graph-theoretic framework for quantifying how much influence a subset of nodes — representing coordinated accounts — actually exerts within information cascades modeled as directed trees. The authors define influence as the number of non-coordinated out-neighbors reachable from coordinated (labeled) nodes and develop algorithms to compute both the unconstrained optimum and a resource-constrained greedy benchmark. Applying these to ~49K retweet cascades from the 2019 UK general election, they find that real coordinated accounts fall far short of theoretical optima: they are too few and are placed in ways statistically indistinguishable from random. The central argument is that Coordinated Inauthentic Behaviour (CIB) may be far less pivotal to information diffusion than prevailing narratives assume, due to both resource scarcity and non-strategic positioning.

## Key Contributions

- A general post-hoc framework for evaluating the influence of a labeled node subset in directed trees, applicable beyond CIB to any binary-label tree influence problem.
- An exact O(|V|) dynamic-programming algorithm (TreeMaxInfluence) for optimal influence maximization, plus a pruning procedure to identify the minimal coordinated-set size.
- A greedy switch-based heuristic for the constrained k-node placement problem.
- Empirical evidence that coordinated accounts in the 2019 UK election exerted limited influence relative to theoretical optima.
- Quantitative evidence (via KL divergence and phase diagrams) that observed placements are statistically close to random and far from greedy-optimal.

## Methods

The influence measure `I_l(T)` counts non-coordinated out-neighbors of coordinated (1-labeled) nodes in a directed tree. Two core algorithms are developed: a dynamic-programming, post-order traversal computing optimal influence in linear time (with a pruning step for redundant coordinated nodes), and a greedy heuristic operating under a fixed budget *k* using an iterative "switch" operator. Synthetic simulations on random directed trees (5–100 nodes, varying height) characterize growth rates of optimal influence and minimum coordinated-set size. A phase-diagram analysis enumerates all labelings of a 25-node tree to assess how rare optimal placements are. The empirical case study reconstructs cascades from ~1.4M tweets about the 2019 UK election using the De Nies et al. cascade-reconstruction heuristic and Nizzoli et al.'s coordination-detection pipeline, then uses Kullback–Leibler divergence to compare empirical, greedy, and random-placement distributions.

## Findings

- On random trees, optimal influence scales roughly linearly with node count (slope ~0.6), while the optimal coordinated-set size scales at slope ~0.28 (R² = 0.99).
- Optimal influence falls sharply as tree height increases for fixed size, stabilizing only past heights around 20.
- Optimal and greedy labelings occupy rare, boundary regions of the phase diagram — high influence is unlikely without deliberate placement.
- Real coordinated accounts achieve influence around 10% of cascade size in large cascades, versus ~60% predicted by the optimal model.
- Only ~1% of nodes in large cascades are coordinated, far below the ~30% needed for optimal influence.
- KL divergence to random placement (0.097) is dramatically smaller than to greedy-optimal (4.278), indicating real placements resemble random assignment.

## Connections

This paper sits at the intersection of coordinated-behaviour detection and network-structure analysis, complementing work that operationalizes and detects coordination such as [[Giglietto2020-9d8acdd7]], [[Giglietto2022-0e951ac5]], [[Giglietto2023-fa71a001]], [[Minici2024-tf]], and [[Luceri2025-tr]]. Its skeptical conclusion — that coordinated accounts are less pivotal to diffusion than commonly assumed — speaks directly to debates about the actual impact of coordinated and inauthentic activity found in [[Ferrara2026-io]] and [[Kulichkina2026-zk]]. Methodologically, its focus on cascade structure connects to diffusion and network-influence studies like [[Bakshy2015-rn]].
