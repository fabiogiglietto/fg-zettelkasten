"""A classic (toread `_classic`, Paperpile's Classics folder) is an ordinary
paper that is never announced in #toread."""
from src.feed_client import _item_to_paper
from src.main import digest_queued

ITEM = {
    "id": "bibtex:Vosoughi2018-ab",
    "title": "The spread of true and false news online",
    "authors": [{"name": "Soroush Vosoughi"}],
    "_academic": {"doi": "10.1126/science.aap9559"},
}


def test_feed_flag_is_parsed():
    assert _item_to_paper({**ITEM, "_classic": True}).is_classic
    assert not _item_to_paper(ITEM).is_classic
    # Only a literal true counts; anything else is an ordinary paper.
    assert not _item_to_paper({**ITEM, "_classic": "yes"}).is_classic


def test_a_classic_is_never_queued_for_a_digest():
    classic = _item_to_paper({**ITEM, "_classic": True})
    assert digest_queued(classic, "all") is False
    assert digest_queued(classic, "team") is False


def test_ordinary_papers_keep_the_scope_rules():
    paper = _item_to_paper(ITEM)
    assert digest_queued(paper, "all") is True
    assert digest_queued(paper, "team") is False
    team = _item_to_paper({**ITEM, "_slack_suggestion": {
        "channel_id": "C1", "ts": "1.2", "submitted_by": "Teammate"}})
    assert digest_queued(team, "team") is True


def test_the_digest_loop_skips_a_classic_queued_before_the_move():
    """Guard in cmd_update, asserted on the source like test_mark_processed:
    a paper queued as ordinary and later moved to Classics must not post."""
    import inspect

    from src import main

    src = inspect.getsource(main.cmd_update)
    loop = src[src.index("if post_to_slack:"):]
    assert "if paper.is_classic:" in loop[:loop.index("slack_client.post_paper")]
