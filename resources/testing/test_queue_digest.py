#!/usr/bin/env python3
"""Regression tests for plugin/throughliner/scripts/queue_digest.py.

Host-only dev artifact — not shipped in the plugin package.

Run:  py resources/testing/test_queue_digest.py

No test framework, matching test_reorder_queue.py alongside it: this project has
no test runner, and `python` on the author's machine resolves to an application's
bundled interpreter that has no pytest.

The digest is imported directly rather than run as a subprocess, because what
needs pinning here is what each field computes, not the command-line wrapper.
Each case writes a small project — a QUEUE.md, sometimes a LOG/ folder — into a
temp dir and asserts on the rendered output.

The standing constraint these tests protect: every field reports a fact, never a
verdict. A case asserting that some item is "ready to lift" would be pinning an
interpretation, and interpreting dependency conditions is what this method
retired. Assert on lookups.
"""

import importlib.util
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, "plugin", "throughliner", "scripts", "queue_digest.py")

_spec = importlib.util.spec_from_file_location("queue_digest", SCRIPT)
digest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(digest)

MARKER = "--- Cleared to run above this line ---"

_failures = []


def check(name, condition, detail=""):
    if condition:
        print("  ok   " + name)
    else:
        print("  FAIL " + name + ("\n       " + detail if detail else ""))
        _failures.append(name)


def project(processed="", unprocessed="", log_entries=()):
    """Write a temp project and return its root. Never a git repository.

    Not being a repo is deliberate for most cases — it exercises the quiet
    degrade of the age field on every run rather than only in the case written
    for it.
    """
    d = tempfile.mkdtemp(prefix="digest-test-")
    with open(os.path.join(d, "QUEUE.md"), "w", encoding="utf-8") as f:
        f.write(
            "# QUEUE\n\nIntro prose.\n\n## Processed\n\n"
            + processed
            + "\n" + MARKER + "\n\n## Unprocessed\n\n"
            + unprocessed
        )
    if log_entries:
        os.mkdir(os.path.join(d, "LOG"))
        for name in log_entries:
            with open(os.path.join(d, "LOG", name), "w", encoding="utf-8") as f:
                f.write("An entry.\n")
    return d


def run(root):
    items = digest.parse(os.path.join(root, "QUEUE.md"))
    return items, digest.render(items, root, os.path.join(root, "QUEUE.md"))


# --- field: slugs cited, resolved against LOG --------------------------------

def test_shipped_citation_prints():
    root = project(
        processed=(
            "#### Do the thing [alpha]\n"
            "This builds on [beta], which is already done.\n"
            "**Files:** `docs/a.md`\n"
        ),
        log_entries=("2026-08-01-beta.md",),
    )
    _, out = run(root)
    check(
        "a citation with a LOG entry prints on the item's line",
        "Cites shipped: [beta]" in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_unshipped_citation_stays_quiet():
    root = project(
        processed=(
            "#### Do the thing [alpha]\n"
            "This waits on [gamma], which has not shipped.\n"
        ),
        log_entries=("2026-08-01-beta.md",),
    )
    _, out = run(root)
    check(
        "a citation with no LOG entry prints nothing",
        "gamma" not in out.split("## Placement")[0].split("Cites shipped")[-1]
        and "Cites shipped" not in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_flavor_tag_is_not_a_citation():
    """[freeform] in prose must not resolve as a slug of that name."""
    root = project(
        processed="#### Do the thing [alpha]\nThis is tagged [freeform] work.\n",
        log_entries=("2026-08-01-freeform.md",),
    )
    _, out = run(root)
    check(
        "a flavor tag in prose is not read as a citation",
        "Cites shipped" not in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_own_slug_is_not_a_citation():
    root = project(
        processed="#### Do the thing [alpha]\nAs [alpha] says, do it.\n",
        log_entries=("2026-08-01-alpha.md",),
    )
    _, out = run(root)
    check(
        "an item citing its own slug does not report itself",
        "Cites shipped" not in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


# --- field: files named by two or more items ---------------------------------

def test_shared_file_is_grouped():
    root = project(
        processed=(
            "#### First [alpha]\n**Files:** `docs-b/plan.md` (a change)\n\n"
            "#### Second [beta]\n**Files:** `docs-b/plan.md` (another change)\n"
        ),
    )
    _, out = run(root)
    check(
        "a file named by two items is reported with both slugs",
        "docs-b/plan.md: [alpha], [beta]" in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_single_file_is_not_grouped():
    root = project(processed="#### Only one [alpha]\n**Files:** `docs-b/plan.md`\n")
    _, out = run(root)
    check(
        "a file named by one item surfaces nothing",
        "## Files named by two or more items — 0" in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_backticked_non_path_is_ignored():
    """A Files line backticks skill names too; those are not files."""
    root = project(
        processed=(
            "#### First [alpha]\n**Files:** `/plan` and `docs/a.md`\n\n"
            "#### Second [beta]\n**Files:** `/plan` and `docs/b.md`\n"
        ),
    )
    _, out = run(root)
    check(
        "a backticked non-path is not grouped as a file",
        "/plan:" not in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


# --- placement contradictions: chains ----------------------------------------

def test_terminating_chain_is_not_reported():
    """A deliberate pacing chain ending in Unprocessed is correct work.

    Three of these fired on every run of the real queue before the fix, on a
    chain built to the user's own instruction. Each held item's own line already
    prints its blocker, so reporting the chain again said nothing new.
    """
    root = project(
        processed=(
            MARKER + "\n\n"
            "#### First post [post-one]\nProse.\nBlocked by: [wake-up]\n\n"
            "#### Second post [post-two]\nProse.\nBlocked by: [post-one]\n"
        ),
        unprocessed="#### Wake up [wake-up]\nProse.\n",
    )
    _, out = run(root)
    check(
        "a chain terminating outside the held region is not reported",
        "## Placement contradictions — 0" in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_looping_chain_is_reported():
    root = project(
        processed=(
            MARKER + "\n\n"
            "#### One [alpha]\nProse.\nBlocked by: [beta]\n\n"
            "#### Two [beta]\nProse.\nBlocked by: [alpha]\n"
        ),
    )
    _, out = run(root)
    check(
        "a chain that comes back to itself is reported as a loop",
        "loop of blockers" in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_absent_blocker_is_not_a_loop():
    root = project(
        processed=MARKER + "\n\n#### One [alpha]\nProse.\nBlocked by: [ghost]\n",
    )
    _, out = run(root)
    check(
        "a blocker resolving to nothing is left alone, not called a loop",
        "loop of blockers" not in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


# --- placement contradictions: the do-not-build phrase list -------------------

def test_built_into_is_not_a_do_not_build_phrase():
    """"Must not be built into X" says other work stays out — the opposite."""
    root = project(
        processed=(
            "#### Do the thing [alpha]\n"
            "Other work must not be built into this item; keep it narrow.\n"
        ),
    )
    _, out = run(root)
    check(
        "a phrase followed by 'into' does not fire the do-not-build check",
        "## Placement contradictions — 0" in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_do_not_build_still_fires():
    root = project(
        processed="#### Do the thing [alpha]\nThis must not be built as written.\n",
    )
    _, out = run(root)
    check(
        "a genuine do-not-build statement still fires",
        "must not be built as written" in out and "Placement contradictions — 1" in out,
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


# --- field: age ---------------------------------------------------------------

def test_no_git_degrades_quietly():
    """A project that is not a git repository gets no dates and no noise."""
    root = project(processed="#### Do the thing [alpha]\nProse.\n")
    items, out = run(root)
    check(
        "first_seen returns nothing outside a git repository",
        digest.first_seen(root, os.path.join(root, "QUEUE.md")) == {},
    )
    check(
        "no date is printed and no error appears in the output",
        "First seen" not in out and "error" not in out.lower(),
        out,
    )
    shutil.rmtree(root, ignore_errors=True)


def test_age_prints_in_this_repository():
    """The real project is a git repo with a committed QUEUE.md, so dates land.

    Skipped rather than failed where that isn't true — a checkout without
    history is a legitimate state, and the degrade case above is what pins the
    behaviour that matters.
    """
    dates = digest.first_seen(ROOT, os.path.join(ROOT, "QUEUE.md"))
    if not dates:
        print("  skip first-seen dates (no git history for QUEUE.md here)")
        return
    check(
        "every date is an ISO day",
        all(len(d) == 10 and d[4] == "-" for d in dates.values()),
        str(list(dates.items())[:3]),
    )


if __name__ == "__main__":
    print("test_queue_digest.py")
    test_shipped_citation_prints()
    test_unshipped_citation_stays_quiet()
    test_flavor_tag_is_not_a_citation()
    test_own_slug_is_not_a_citation()
    test_shared_file_is_grouped()
    test_single_file_is_not_grouped()
    test_backticked_non_path_is_ignored()
    test_terminating_chain_is_not_reported()
    test_looping_chain_is_reported()
    test_absent_blocker_is_not_a_loop()
    test_built_into_is_not_a_do_not_build_phrase()
    test_do_not_build_still_fires()
    test_no_git_degrades_quietly()
    test_age_prints_in_this_repository()
    print()
    if _failures:
        print(f"{len(_failures)} failure(s): " + ", ".join(_failures))
        sys.exit(1)
    print("all passed")
