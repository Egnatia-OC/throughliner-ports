#!/usr/bin/env python3
"""Regression tests for plugin/si-plugin/scripts/reorder_queue.py.

Host-only dev artifact — not shipped in the plugin package.

Run:  python resources/testing/test_reorder_queue.py

No test framework required, deliberately: this project has no test runner and
adding one to guard a single script would cost more than it protects. Each test
writes a small QUEUE.md into a temp dir, runs the mover as a subprocess exactly
the way /plan drives it, and asserts on the resulting file.

The headline case is `marker above all items`. That shape made the mover refuse
EVERY reorder of Processed — not just the greenlighting move — because the
marker scan started at the first `####` item and so never matched a marker
sitting above them all. The defect is a scan-range off-by-one, which is easy to
reintroduce, so it gets a permanent case here.
"""

import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, "plugin", "si-plugin", "scripts", "reorder_queue.py")

MARKER = "--- Cleared to run above this line ---"

_failures = []


def build_queue(processed_body, unprocessed_body="#### Later thing [later]\nSome rationale.\n"):
    return (
        "# QUEUE\n\n"
        "Intro prose that must survive untouched.\n\n"
        "## Processed\n\n"
        + processed_body
        + "\n## Unprocessed\n\n"
        + unprocessed_body
    )


def run(text, *args):
    """Write `text` to a temp QUEUE.md, run the mover, return (rc, stderr, new_text)."""
    d = tempfile.mkdtemp(prefix="reorder-test-")
    path = os.path.join(d, "QUEUE.md")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    proc = subprocess.run(
        [sys.executable, SCRIPT, path] + list(args),
        capture_output=True, text=True,
    )
    with open(path, "r", encoding="utf-8", newline="") as f:
        return proc.returncode, proc.stderr, f.read()


def check(name, condition, detail=""):
    if condition:
        print("  ok   " + name)
    else:
        print("  FAIL " + name + ("\n       " + detail if detail else ""))
        _failures.append(name)


def order_of(text, section="## Processed"):
    """Slugs, in file order, within a section — plus MARKER where it sits."""
    out = []
    inside = False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = line.strip() == section
            continue
        if not inside:
            continue
        if line.strip() == MARKER:
            out.append(MARKER)
        elif line.startswith("#### "):
            out.append(line.rstrip().rsplit("[", 1)[1].rstrip("]"))
    return out


# --- the regression case ------------------------------------------------------

def test_marker_above_all_items():
    """Marker sitting above every item must not block a plain reorder."""
    body = (
        MARKER + "\n\n"
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha")
    check("marker-above-all: exits 0", rc == 0, err)
    check("marker-above-all: no self-check failure", "self-check failed" not in err, err)
    check("marker-above-all: no bogus 'no marker' warning",
          "section has no marker" not in err, err)
    check("marker-above-all: items swapped, marker still at top",
          order_of(new) == [MARKER, "beta", "alpha"], repr(order_of(new)))
    check("marker-above-all: marker appears exactly once",
          new.count(MARKER) == 1, str(new.count(MARKER)))
    check("marker-above-all: block text preserved byte-for-byte",
          "#### First item [alpha]\nRationale for alpha." in new
          and "#### Second item [beta]\nRationale for beta." in new)
    check("marker-above-all: other section untouched", "#### Later thing [later]" in new)


def test_marker_above_all_explicit_placement():
    """With the marker above all items, --marker-after must still be honoured."""
    body = (
        MARKER + "\n\n"
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "alpha", "beta",
                       "--marker-after", "alpha")
    check("marker-above-all + --marker-after: exits 0", rc == 0, err)
    check("marker-above-all + --marker-after: marker moved below alpha",
          order_of(new) == ["alpha", MARKER, "beta"], repr(order_of(new)))


def test_marker_above_all_move_mode():
    """--move mode hits the same split_blocks path and must work too."""
    body = (
        MARKER + "\n\n"
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "--move", "beta", "TOP")
    check("marker-above-all + --move: exits 0", rc == 0, err)
    check("marker-above-all + --move: beta on top, marker still at top",
          order_of(new) == [MARKER, "beta", "alpha"], repr(order_of(new)))


# --- the shapes that already worked, kept so the fix doesn't break them --------

def test_marker_between_items():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        + MARKER + "\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "alpha", "beta")
    check("marker-between: exits 0", rc == 0, err)
    check("marker-between: marker keeps its relative spot",
          order_of(new) == ["alpha", MARKER, "beta"], repr(order_of(new)))


def test_marker_below_all_items():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha")
    check("marker-below-all: exits 0", rc == 0, err)
    # Documented behaviour with no --marker-after: the marker keeps its RELATIVE
    # spot — immediately after whichever slug it currently follows (beta), which
    # after this swap is no longer the bottom.
    check("marker-below-all: marker follows the slug it followed before",
          order_of(new) == ["beta", MARKER, "alpha"], repr(order_of(new)))
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha",
                       "--marker-after", "BOTTOM")
    check("marker-below-all + BOTTOM: pinned to the bottom",
          rc == 0 and order_of(new) == ["beta", "alpha", MARKER],
          err + repr(order_of(new)))


def test_section_with_no_marker():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha")
    check("no-marker: exits 0", rc == 0, err)
    check("no-marker: no marker invented", MARKER not in new)
    check("no-marker: reordered", order_of(new) == ["beta", "alpha"], repr(order_of(new)))


def test_no_marker_with_marker_after_warns():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha",
                       "--marker-after", "alpha")
    check("no-marker + --marker-after: still succeeds", rc == 0, err)
    check("no-marker + --marker-after: warns and ignores",
          "section has no marker" in err, err)


def test_slug_set_mismatch_refuses():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    original = build_queue(body)
    rc, err, new = run(original, "Processed", "beta")
    check("mismatch: exits non-zero", rc != 0, err)
    check("mismatch: file unchanged", new == original)


def main():
    print("reorder_queue.py regression tests")
    for fn in (
        test_marker_above_all_items,
        test_marker_above_all_explicit_placement,
        test_marker_above_all_move_mode,
        test_marker_between_items,
        test_marker_below_all_items,
        test_section_with_no_marker,
        test_no_marker_with_marker_after_warns,
        test_slug_set_mismatch_refuses,
    ):
        print(fn.__name__)
        fn()
    print()
    if _failures:
        print("%d check(s) FAILED: %s" % (len(_failures), ", ".join(_failures)))
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
