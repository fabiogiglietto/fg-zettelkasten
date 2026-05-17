"""Topic-anchored assignment of papers to the register, plus emergent sub-themes.

Assignment is *guided* — papers map to existing register topics — not free
clustering. A paper fitting no anchor stays `unassigned`; an emergent topic is
created only when at least `emergent_min_papers` mutually cohesive unassigned
papers exist, so the register never fragments into one-paper topics.
"""
from __future__ import annotations


def assign_paper(paper, summary: dict, topics: list[dict], claude, model: str) -> list[str]:
    """Return the slugs of the 1-2 register topics this paper belongs to.

    Returns [] when the paper fits no anchor topic — it then stays `unassigned`
    until the next recluster.
    """
    # TODO: send paper + summary + the topic names/descriptions to Claude;
    #       ask which 1-2 topics fit (no embeddings).
    raise NotImplementedError("themes.assign_paper")


def find_emergent(
    unassigned: list, summaries: dict, claude, model: str, min_papers: int
) -> list[dict]:
    """Cluster the `unassigned` papers and return any new emergent topics.

    An emergent topic is only proposed when at least `min_papers` of the
    unassigned papers are mutually cohesive (LLM check). Returns a list of
    {slug, name, description, is_emergent: True, members: [...]}.
    """
    # TODO: cluster + cohesion check.
    raise NotImplementedError("themes.find_emergent")
