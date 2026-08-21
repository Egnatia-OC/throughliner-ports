#!/usr/bin/env python3
"""Fixture suite for the build-view generator.

Run: py resources/testing/test_build_view.py
(Plain script, never pytest — see CLAUDE.md's scripting constraints.)

What matters here is byte-for-byte fidelity. The build block is the run's whole
instruction set, so anything that reformats it in passing is a place where what
the run acts on can silently differ from what the user approved at the
keep-step. A test that only checked the block "appears" would pass through a
generator that reflowed it.

The other half is what the view must NOT carry. The saving is not the point on
its own — a build transcribes what it reads, and rationale written into a work
item was measured reaching the method's shipped documents in near-verbatim form.
So a test asserting the history is absent is testing the actual mechanism, not
an optimisation.
"""

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass

ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, "plugin", "throughliner", "scripts",
                      "generate_build_view.py")

failures = []


def check(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + ("" if ok else f" — {detail}"))
    if not ok:
        failures.append(label)


def load():
    spec = importlib.util.spec_from_file_location("generate_build_view", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# A block with awkward whitespace and characters on purpose: trailing spaces,
# an em-dash, a nested fence and a blank line. Anything that normalises text
# will change at least one of them.
BLOCK_BODY = """Changes: `plan.md` — the keep-step gains one clause.
Acceptance: the suite passes, and a generated view carries the clause.

Refused: a sixth skill, because every skill is loaded and documented.
  indented continuation, two spaces
Red flag: none"""

QUEUE = """# QUEUE

Intro prose that mentions --- Cleared to run above this line --- inside a sentence.

## Processed

#### A cleared item with a block [alpha]
Rationale prose nobody should ever see in the view. SECRETHISTORY.
This paragraph is the decision history and is the whole reason the view exists.

--- Build block ---
""" + BLOCK_BODY + """
--- End build block ---

More rationale after the block. ALSOSECRET.

#### A cleared item with no block [beta]
Rationale only. No instructions were ever authored for this one.

--- Cleared to run above this line ---

#### A held item [gamma]
Rationale.
Blocked by: [alpha]

## Unprocessed

#### A capture [delta]
Rationale.
"""


def project(queue=QUEUE):
    d = tempfile.mkdtemp(prefix="build-view-test-")
    with open(os.path.join(d, "QUEUE.md"), "w", encoding="utf-8") as f:
        f.write(queue)
    return d


def generate(root):
    out = os.path.join(root, "BUILD-VIEW.md")
    subprocess.run(
        [sys.executable, SCRIPT, os.path.join(root, "QUEUE.md"), "--out", out],
        check=True, capture_output=True, encoding="utf-8",
    )
    with open(out, encoding="utf-8") as f:
        return f.read()


def summary(root):
    """The generator's own stdout summary line."""
    out = os.path.join(root, "BUILD-VIEW.md")
    r = subprocess.run(
        [sys.executable, SCRIPT, os.path.join(root, "QUEUE.md"), "--out", out],
        check=True, capture_output=True, encoding="utf-8",
    )
    return r.stdout.strip()


def test_block_is_copied_byte_for_byte():
    """The instruction set the user approved is what the run acts on.

    Checked as one exact substring rather than line by line, so a reflow, a
    stripped trailing space or a normalised dash all fail it.
    """
    root = project()
    view = generate(root)
    check("the block appears byte-for-byte", BLOCK_BODY in view,
          repr(view[view.find("Changes:"):][:300]))
    shutil.rmtree(root, ignore_errors=True)


def test_decision_history_is_absent():
    """The view carries instructions and no rationale. This is the mechanism."""
    root = project()
    view = generate(root)
    check("rationale before the block is absent", "SECRETHISTORY" not in view, view[:400])
    check("rationale after the block is absent", "ALSOSECRET" not in view, view[:400])
    shutil.rmtree(root, ignore_errors=True)


def test_refusal_travels():
    """A refusal is the one part of the history that must survive.

    A build that cannot see why an option was rejected proposes it again and
    stops to ask, which is exactly the interruption the view is meant to remove.
    """
    root = project()
    view = generate(root)
    check("the refused option and its reason are carried",
          "a sixth skill" in view and "every skill is loaded" in view, view[:400])
    shutil.rmtree(root, ignore_errors=True)


def test_every_entry_is_listed_by_name():
    """Duplicate detection, restored at almost no cost.

    Every entry in both sections appears by heading and slug — including the
    held one and the capture, which are not built and are still filed.
    """
    root = project()
    view = generate(root)
    listing = view.split("Everything in the queue, by name only")[1]
    for slug in ("alpha", "beta", "gamma", "delta"):
        check(f"[{slug}] is listed by name", f"[{slug}]" in listing, listing[:400])
    check("the held item's rationale is still absent",
          "Blocked by" not in listing, listing[:400])
    shutil.rmtree(root, ignore_errors=True)


def test_uncleared_item_contributes_no_block():
    """Only the cleared region is buildable, so only it carries instructions."""
    root = project()
    view = generate(root)
    cleared_part = view.split("Everything in the queue, by name only")[0]
    check("a held item gets no build section in the cleared region",
          "### [gamma]" not in cleared_part, cleared_part[:400])
    check("a capture gets no build section either",
          "### [delta]" not in cleared_part, cleared_part[:400])
    shutil.rmtree(root, ignore_errors=True)


def test_missing_block_is_stated_in_the_view():
    """A run must meet the gap where it will act on it, not only in a lint line.

    An item with no block cannot be built from the view, and the run halts on it
    as underspecified. Saying so silently — by omission — would leave the run to
    infer the halt from an absence.
    """
    root = project()
    view = generate(root)
    section = view.split("### [beta]")[1].split("###")[0]
    check("the item with no block says so", "No build block" in section, section[:300])
    shutil.rmtree(root, ignore_errors=True)


def test_marker_text_in_prose_does_not_move_the_line():
    """The readiness marker is a line, never a substring.

    The intro prose quotes the marker text. Matching it as a substring would
    end the cleared region before the first item and produce an empty view —
    the same defect the digest once had.
    """
    root = project()
    view = generate(root)
    check("the first cleared item survives marker text in prose",
          "### [alpha]" in view, view[:400])
    shutil.rmtree(root, ignore_errors=True)


def test_unterminated_block_is_reported_not_repaired():
    """A malformed block is named and never tidied.

    The block is the user-approved instruction set. A generator that repairs one
    is a generator that can change what the run builds.
    """
    bad = QUEUE.replace("--- End build block ---", "")
    root = project(bad)
    out = os.path.join(root, "BUILD-VIEW.md")
    proc = subprocess.run(
        [sys.executable, SCRIPT, os.path.join(root, "QUEUE.md"), "--out", out],
        capture_output=True, encoding="utf-8",
    )
    check("the malformed block is named on stderr",
          "malformed block" in proc.stderr, proc.stderr[:300])
    with open(out, encoding="utf-8") as f:
        view = f.read()
    check("no rationale leaks through the malformed block",
          "ALSOSECRET" not in view, view[:400])
    shutil.rmtree(root, ignore_errors=True)


def test_slug_is_not_printed_twice():
    """The heading already ends with its slug, and the view keys on it."""
    root = project()
    view = generate(root)
    check("the slug appears once per cleared heading",
          "[alpha] A cleared item with a block" in view
          and "[alpha] A cleared item with a block [alpha]" not in view,
          view[:400])
    shutil.rmtree(root, ignore_errors=True)


MARKER_LINE = "--- Cleared to run above this line ---"

RUNS_ALONE_QUEUE = """# QUEUE

## Processed

#### A cleared item that must run on its own [solo]
Prose.
Runs alone

--- Build block ---
Changes: `a.md` — something.
Acceptance: it worked.
--- End build block ---

""" + MARKER_LINE + """

## Unprocessed
"""

WALKTHROUGH_QUEUE = """# QUEUE

## Processed

#### A build item with a block [alpha]
Prose.

--- Build block ---
Changes: `a.md` — something.
Acceptance: it worked.
--- End build block ---

#### [user] A step only the user can run [beta]
Prose.

#### [freeform] Work a run must not build [gamma]
Prose.

""" + MARKER_LINE + """

## Unprocessed
"""

BLOCKLESS_QUEUE = """# QUEUE

## Processed

#### A build item with a block [alpha]
Prose.

--- Build block ---
Changes: `a.md` — something.
Acceptance: it worked.
--- End build block ---

#### A build item with no block at all [delta]
Prose.

""" + MARKER_LINE + """

## Unprocessed
"""


def test_runs_alone_reaches_the_view():
    """The run's second bound has to be visible where the run reads.

    The marker sits outside the build block, so the projection dropped it and a
    run could not see where it was supposed to stop — /next reads the literal.
    """
    root = project(RUNS_ALONE_QUEUE)
    view = generate(root)
    cleared = view.split("## Everything in the queue")[0]
    check("the Runs alone marker appears in the cleared-items region",
          "Runs alone" in cleared, cleared[:500])
    shutil.rmtree(root, ignore_errors=True)


def test_completeness_can_read_equal_with_walkthrough_items():
    """Equal must be reachable in a project holding [user]/[freeform] work.

    Both are cleared and neither is built from a block, so counting them among
    the items that need one made the two numbers permanently unequal — and a
    number that can never match distinguishes nothing at the moment it is read.
    """
    root = project(WALKTHROUGH_QUEUE)
    line = summary(root)
    check("the two counted numbers are equal",
          "1 block-needing cleared item(s), 1 with a build block" in line, line)
    check("the exempt items are still reported, not hidden",
          "2 cleared [user]/[freeform] item(s), which need none" in line, line)
    shutil.rmtree(root, ignore_errors=True)


def test_a_genuinely_blockless_build_item_still_reads_unequal():
    """The test must still fail when a migration is actually incomplete."""
    root = project(BLOCKLESS_QUEUE)
    line = summary(root)
    check("a build item with no block makes the numbers differ",
          "2 block-needing cleared item(s), 1 with a build block" in line, line)
    shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    print("test_build_view")
    test_runs_alone_reaches_the_view()
    test_completeness_can_read_equal_with_walkthrough_items()
    test_a_genuinely_blockless_build_item_still_reads_unequal()
    test_block_is_copied_byte_for_byte()
    test_decision_history_is_absent()
    test_refusal_travels()
    test_every_entry_is_listed_by_name()
    test_uncleared_item_contributes_no_block()
    test_missing_block_is_stated_in_the_view()
    test_marker_text_in_prose_does_not_move_the_line()
    test_unterminated_block_is_reported_not_repaired()
    test_slug_is_not_printed_twice()
    print(f"\n{len(failures)} failure(s)" if failures else "\nall passed")
    sys.exit(1 if failures else 0)
