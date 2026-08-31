---
type: structure
slug: mine-research-program
topic: "MINE — Mapping Italian News Program"
---

# MINE — Mapping Italian News Program

## Two papers, one long-running programme

MINE is less a single research question than an institutional container: since 2017 it has hosted the researcher's sustained attention to how Italian political news circulates on social media around elections. The two papers currently filed here sit eight years apart in the programme's timeline but share the same empirical anchor — the flow of political news through Italian social media during national election campaigns — while pulling in almost opposite methodological directions. Read together, they trace an arc from substantive political-communication findings toward the methodological infrastructure needed to keep producing such findings at scale.

## From findings about polarization to findings about method

[[Giglietto2019-882f1900]] is squarely a substantive contribution: using the 2018 election as its case, it asks how partisan communities on Twitter and Facebook interact with news, and finds that populist-aligned sources (M5S above all) are more "insular," that insularity predicts an amplification-over-contestation pattern in Facebook engagement, and that M5S in particular has built a supporter base capable of strategically shaping the attention economy around both favorable and unfavorable coverage. It is explicitly conversant with the literature on echo chambers, hybrid media systems, and populism (Hallin & Mancini, Chadwick, Waisbord), and treats the Italian case as a theoretically useful non-US test bed for these debates.

[[Giglietto2024-cbeb3f70]], by contrast, is a methods paper that happens to use the same kind of data — Facebook-shared political news around the 2018 and 2022 elections — but asks a completely different question: not "what do Italians do with news on social media" but "how should we even segment that news into meaningful topics computationally." It compares OpenAI's text-embedding-3-large against the Italian-specific UmBERTo model for unsupervised clustering, adapting Grimmer & King's cluster-quality framework and outsourcing thematic-coherence judgments to a fine-tuned GPT-4o-mini. The 2018 dataset that grounded the insularity analysis in [[Giglietto2019-882f1900]] reappears here as a benchmark for embedding quality, alongside a fresh 2022 dataset — quietly demonstrating that MINE's data infrastructure has itself become an object of methodological reflection, not just a resource for one-off studies.

## What connects them

The throughline is less thematic than infrastructural: both papers depend on the ability to classify and interpret large volumes of Italian-language political news shared on social media, and both wrestle with the problem of imposing meaningful structure on that content — [[Giglietto2019-882f1900]] structures it by partisan source and audience behavior, [[Giglietto2024-cbeb3f70]] structures it by semantic topic via clustering. Notably, [[Giglietto2024-cbeb3f70]] finds that clustering quality *declined* from 2018 to 2022 across every model/algorithm configuration tested — an incidental but suggestive echo of the earlier paper's argument that the Italian political information environment is becoming more fragmented and harder to characterize with any single lens, whether human-coded partisan categories or embedding-based topic clusters.

## The gap the note reveals

Filed together, these two papers expose a gap that MINE's future work (or its dormant sub-projects) would need to fill: the 2019 paper offers a rich substantive account of partisan dynamics but relies on labor-intensive manual/semi-automated source adjudication, while the 2024 paper builds automated, cheap ($3 in inference costs) tooling for topic discovery but does not yet feed that tooling back into a partisan-engagement analysis. The implicit next step for the programme — using LLM-embedding-based clustering to re-run or extend the insularity/amplification analysis across more elections and more topics — is visible in the seam between the two papers, even though no filed paper yet closes it. In that sense this structure note itself performs MINE's institutional role: sustaining a line of inquiry across a funding gap, holding the substantive question (how populism and partisanship shape Italian media ecologies) and the methodological question (how to measure that at scale with contemporary NLP tools) in the same frame until they can be rejoined.
