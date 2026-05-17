"""Topic-anchored assignment of papers to the register, plus emergent sub-themes.

Assignment is *guided* — papers map to existing register topics — not free
clustering. A paper fitting no anchor stays `unassigned`; an emergent topic is
created only when at least `emergent_min_papers` mutually cohesive unassigned
papers exist, so the register never fragments into one-paper topics.
"""
from __future__ import annotations


def _summary_digest(summary: dict) -> str:
    """A compact one-block digest of a structured summary for prompting."""
    fields = ("abstract", "key_claims", "findings", "framing")
    lines = []
    for field in fields:
        value = summary.get(field)
        if not value:
            continue
        if isinstance(value, list):
            value = "; ".join(str(v) for v in value)
        lines.append(f"{field}: {value}")
    return "\n".join(lines)


_ASSIGN_SYSTEM = """\
You file academic papers into a fixed topic register — the Schlagwortregister \
of a Zettelkasten. Assignment is topic-anchored: a paper maps onto existing \
register topics, you never invent new ones here.

Given a paper and the register, choose the 1-2 topics the paper most genuinely \
belongs to. Assign a topic only when the paper is a real contribution to it — \
a loose thematic brush is not enough. If no register topic fits, return an \
empty list; the paper will wait as `unassigned`.

Return ONLY a JSON object, no prose or fences:
  {"topics": ["slug-a", "slug-b"]}
Use at most two slugs, drawn verbatim from the register."""


def assign_paper(paper, summary: dict, topics: list[dict], claude, model: str) -> list[str]:
    """Return the slugs of the 1-2 register topics this paper belongs to.

    Returns [] when the paper fits no anchor topic — it then stays `unassigned`
    until the next recluster.
    """
    if not topics:
        return []

    register = "\n".join(
        f"- {t['slug']}: {t['name']} — {t.get('description', '')}" for t in topics
    )
    prompt = (
        f"Topic register:\n{register}\n\n"
        f"Paper:\nTitle: {paper.title}\n"
        f"Authors: {', '.join(paper.authors) or 'unknown'}\n\n"
        f"{_summary_digest(summary)}"
    )

    result = claude.complete_json(
        model=model,
        system=_ASSIGN_SYSTEM,
        prompt=prompt,
        max_tokens=1024,
    )
    valid = {t["slug"] for t in topics}
    chosen = [slug for slug in result.get("topics", []) if slug in valid]
    return chosen[:2]


_EMERGENT_SYSTEM = """\
You look for emergent sub-themes among papers that fit no existing register \
topic. The register must not fragment into one-paper topics, so propose a new \
topic ONLY for a group of at least {min_papers} papers that are genuinely, \
mutually cohesive — a shared research question or object, not a vague overlap.

Papers that do not form such a group are left out entirely; it is correct to \
return an empty list.

Return ONLY a JSON array, no prose or fences. Each element:
  {{"slug": ..., "name": ..., "description": ..., "members": ["bibtex-key", ...]}}
Slugs are lowercase-hyphenated; `members` lists the bibtex keys (given below) \
of the cohesive papers, at least {min_papers} per topic."""


def find_emergent(
    unassigned: list, summaries: dict, claude, model: str, min_papers: int
) -> list[dict]:
    """Cluster the `unassigned` papers and return any new emergent topics.

    An emergent topic is only proposed when at least `min_papers` of the
    unassigned papers are mutually cohesive (LLM check). Returns a list of
    {slug, name, description, is_emergent: True, members: [...]}.

    `unassigned` is a list of `Paper` objects; `summaries` maps bibtex key to
    the paper's structured summary.
    """
    if len(unassigned) < min_papers:
        return []

    blocks = []
    for paper in unassigned:
        digest = _summary_digest(summaries.get(paper.bibtex_key, {}))
        blocks.append(
            f"===== {paper.bibtex_key} =====\nTitle: {paper.title}\n{digest}"
        )
    prompt = (
        f"{len(unassigned)} unassigned papers follow.\n\n"
        + "\n\n".join(blocks)
    )

    proposals = claude.complete_json(
        model=model,
        system=_EMERGENT_SYSTEM.format(min_papers=min_papers),
        prompt=prompt,
        max_tokens=4096,
    )

    keys = {p.bibtex_key for p in unassigned}
    emergent: list[dict] = []
    for topic in proposals:
        members = [m for m in topic.get("members", []) if m in keys]
        if len(members) < min_papers:
            continue
        emergent.append(
            {
                "slug": topic["slug"],
                "name": topic["name"],
                "description": topic.get("description", ""),
                "is_emergent": True,
                "members": members,
            }
        )
    return emergent
