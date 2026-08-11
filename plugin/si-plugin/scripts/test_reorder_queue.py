#!/usr/bin/env python3
"""Regression tests for reorder_queue.py's reporting.

Run: python plugin/si-plugin/scripts/test_reorder_queue.py

Why this file exists, and why its sibling defect has no test. Three faults have
now been found in this script's OUTPUT rather than its writes — across every
use, the file operations were correct and every fault was in what the tool said
about them. That matters more than a cosmetic wrong message: the whole point of
the mover is that a session does not have to hand-verify queue structure, so its
messages are trusted and acted on without re-reading the file.

[mover-console-encoding-mangles-output] deliberately shipped without a test,
because the failure would not reproduce in any shell available here. This one
reproduces deterministically from a fixture, so it gets one.
"""

import os
import subprocess
import sys
import tempfile

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reorder_queue.py")

# The fixture that reproduces the bug: a held item whose `Blocked by:` names the
# item being moved. That is not an exotic shape — it is exactly what exists
# whenever the move matters, because clearing an item that other work waits on
# is the case the report is most trusted in.
#
# TWO cleared items, deliberately. An item's block runs to the next heading, so
# "AFTER the last cleared item" spans the marker and legitimately lands the
# moved item below it — the positional ambiguity this report was written to
# surface in the first place. Anchoring to the FIRST of two puts the moved item
# unambiguously above the marker, which is what makes a wrong report wrong
# rather than merely surprising.
FIXTURE = """# QUEUE

## Processed

#### First cleared item [alpha]
Rationale for alpha.

#### Second cleared item [delta]
Rationale for delta.

--- Cleared to run above this line ---

#### A held item [gamma]
Rationale for gamma.
Blocked by: [beta]

## Unprocessed

#### The item being moved [beta]
Rationale for beta.
"""

failures = []


def check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name} {detail}")
        failures.append(name)


def run_move(queue_path):
    return subprocess.run(
        [sys.executable, SCRIPT, queue_path,
         "--move-section", "beta", "Unprocessed", "Processed",
         "--position", "AFTER", "alpha"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )


def test_side_of_marker_report():
    """The moved item lands above the marker, and the report must say so."""
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "QUEUE.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(FIXTURE)

        result = run_move(path)
        output = result.stdout + result.stderr

        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

        marker_i = next(i for i, l in enumerate(lines)
                        if "Cleared to run above this line" in l)
        beta_i = next(i for i, l in enumerate(lines)
                      if l.startswith("#### ") and l.rstrip().endswith("[beta]"))

        check("file places the item above the marker", beta_i < marker_i,
              f"(item at {beta_i}, marker at {marker_i})")
        check("report says ABOVE", "ABOVE" in output, f"got: {output.strip()}")
        check("report does not say BELOW", "BELOW" not in output,
              f"got: {output.strip()}")
        check("report does not call it waiting",
              "NOT cleared to run" not in output, f"got: {output.strip()}")
        check("the held item's Blocked by line survives the move",
              any(l.strip() == "Blocked by: [beta]" for l in lines))


def test_report_agrees_with_file():
    """The tool's claim and the file must never disagree — the real defect."""
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "QUEUE.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(FIXTURE)

        result = run_move(path)
        output = result.stdout + result.stderr

        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        marker_i = next(i for i, l in enumerate(lines)
                        if "Cleared to run above this line" in l)
        beta_i = next(i for i, l in enumerate(lines)
                      if l.startswith("#### ") and l.rstrip().endswith("[beta]"))

        said_above = "ABOVE" in output
        is_above = beta_i < marker_i
        check("report agrees with the file", said_above == is_above,
              f"(said ABOVE={said_above}, actually above={is_above})")


if __name__ == "__main__":
    print("test_reorder_queue")
    test_side_of_marker_report()
    test_report_agrees_with_file()
    print(f"\n{len(failures)} failure(s)" if failures else "\nall passed")
    sys.exit(1 if failures else 0)
