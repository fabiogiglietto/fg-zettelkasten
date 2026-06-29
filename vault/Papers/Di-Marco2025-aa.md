---
title: "Post-hoc evaluation of nodes influence in information cascades: The case of coordinated accounts"
aliases: ["Post-hoc evaluation of nodes influence in information cascades: The case of coordinated accounts"]
authors: ["Niccolò Di Marco", "Sara Brunetti", "Matteo Cinelli", "Walter Quattrociocchi"]
year: 2025
doi: 10.1145/3700644
bibtex_key: Di-Marco2025-aa
topics: [coordinated-inauthentic-behavior, computational-methods-social-research]
citation_count: 6
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

This paper develops a graph-theoretic, post-hoc framework for measuring how much influence a labeled subset of nodes — here, coordinated accounts — actually exerts within directed retweet cascades, and compares observed influence against optimal and resource-matched benchmarks. Treating cascades as directed trees with binary node labels, the authors define influence as the number of non-coordinated out-neighbors of coordinated nodes and provide algorithms for both unconstrained and budget-constrained optimal placement. Applied to ~49K retweet cascades from the 2019 UK general election, the framework shows that real coordinated accounts exert only a fraction of the influence achievable under optimal or greedy placement, and that their positions in cascades are statistically indistinguishable from random. The paper concludes that Coordinated Inauthentic Behaviour (CIB) is likely far less pivotal in information diffusion than prevailing narratives suggest.

## Key Contributions

- A general post-hoc framework for quantifying the influence of a labeled node subset in directed trees, with CIB as the motivating but not exclusive application.
- An exact O(|V|) dynamic-programming algorithm (TreeMaxInfluence) for unconstrained influence maximization, plus a pruning procedure yielding the minimal optimal coordinated-set size.
- A greedy switch-based heuristic for the budget-constrained k-node placement problem.
- Empirical demonstration on 2019 UK election Twitter/X data that observed coordinated placements are far from optimal and effectively random.
- Phase-diagram and KL-divergence diagnostics for benchmarking observed coordinated-account configurations against optimal, greedy, and random baselines.

## Methods

The authors formalize influence on directed trees with binary node labels and derive two algorithms: an unconstrained dynamic-programming optimum (post-order traversal, linear time) with a pruning step for minimum coordinated-set size, and a constrained greedy heuristic that iteratively applies a "switch" operator to improve influence under a fixed budget k. They validate scaling behavior on synthetic random directed trees of varying size and height, enumerate all labelings of a small 25-node tree to map the (m10, m11) phase space, and apply the framework to ~49K retweet cascades reconstructed from ~1.4M tweets about the 2019 UK general election (cascade reconstruction via De Nies et al.; coordination detection via the Nizzoli et al. pipeline). Empirical, greedy, and random-placement influence distributions are compared via KL divergence.

## Findings

- On synthetic trees, optimal influence I* grows ~linearly with n (slope ≈0.6) while minimum optimal coordinated-set size k* scales at slope ≈0.28 (R² = 0.99).
- Tree height strongly suppresses achievable influence for fixed n, stabilizing only beyond heights ~20.
- Optimal and greedy labelings occupy rare, boundary regions of the (m10, m11) phase diagram — strategic placements are statistically unusual.
- In large empirical cascades, real coordinated accounts achieve ~10% of cascade size in influence versus the ~60% predicted by the optimum.
- Only ~1% of nodes in large cascades are coordinated, far below the ~30% threshold needed to approach optimal influence.
- D_KL(p_real || q_random) = 0.097 vs. D_KL(p_real || q_greedy) = 4.278: observed placements are close to random, far from greedy-optimal.

## Connections

This work contributes a formal, algorithmic counterweight to the broad CIB literature that often presumes coordinated accounts meaningfully shape diffusion, aligning with skeptical empirical findings in [[Bak-Coleman2026-mk]] and the broader reassessments of platform manipulation impact in [[Allen2025-ot]] and [[Murtfeldt2025-wu]]. Its tree-based cascade modeling and detection pipeline relate methodologically to coordination-detection and cascade-analysis work such as [[Luceri2025-tr]], [[Minici2024-tf]], and [[Mannocci2025-ig]], while its election-context empirical focus connects to [[Kulichkina2026-zk]] and [[Gerard2025-br]]. More broadly, the paper's post-hoc, benchmark-against-optimum stance complements critical methodological reflections on CIB inference such as [[Freelon2024-sc]] and [[Graham2025-gp]].
