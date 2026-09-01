"""The change signal must survive a skipped render.

`content_hash` is the only record that a paper still needs re-rendering, and
the render loop bails for a paper whose summary is missing from disk. The two
used to run in that order — advance, then render — so a changed paper with no
summary lost its signal permanently: the next run classified it "unchanged"
and never looked again, freezing the stale note in the vault.
"""

import inspect

from src.main import classify_feed_paper, mark_processed


def test_mark_processed_records_the_current_content():
    entry = {"content_hash": "stale", "podcast_linked": False}
    mark_processed(entry, "a real abstract", True)

    assert entry["content_hash"] != "stale"
    assert entry["podcast_linked"] is True
    assert entry["last_processed"]
    # And the paper is now settled: the same content classifies as unchanged.
    assert classify_feed_paper(entry, entry["content_hash"]) == "unchanged"


def test_unmarked_entry_stays_changed_so_the_next_run_retries():
    """The whole point: a render that never happened must be retried. This is
    what a metadata backfill needs — its papers are all `changed`, and one of
    them has had its junk summary deleted so it regenerates."""
    entry = {"content_hash": "stale"}
    fresh = dict(entry)
    mark_processed(fresh, "a real abstract", False)

    assert classify_feed_paper(entry, fresh["content_hash"]) == "changed"


def _cmd_update_source():
    from src import main
    return inspect.getsource(main.cmd_update)


def test_the_only_hash_write_outside_mark_processed_is_the_tombstone_guard():
    """Guard against reintroducing the bug as a loop that refreshes the hash
    up front. The only direct writes left in `cmd_update` are the tombstoned
    branches — one per path — which advance the hash precisely *because* that
    paper must never reach the render loop."""
    src = _cmd_update_source()
    lines = src.splitlines()
    writes = [i for i, ln in enumerate(lines)
              if 'entry["content_hash"] =' in ln]

    assert writes, "the tombstone guard should still be here"
    for i in writes:
        preceding = "\n".join(lines[max(0, i - 6):i])
        assert 'kind == "tombstoned"' in preceding, (
            "changed papers must settle via mark_processed, after write_note"
        )


def test_mark_processed_is_called_only_after_the_note_is_written():
    """Ordering is the fix. Every `mark_processed` call in `cmd_update` must
    follow a `write_note` call, on both the feed and own-publications paths."""
    src = _cmd_update_source()
    writes = [i for i, ln in enumerate(src.splitlines())
              if "note_builder.write_note(" in ln]
    marks = [i for i, ln in enumerate(src.splitlines())
             if ln.strip().startswith("mark_processed(")]

    assert len(marks) == 2, "expected the feed and own-publications paths"
    assert len(writes) == 2
    for mark, write in zip(marks, writes):
        assert mark > write, "mark_processed must follow write_note"
