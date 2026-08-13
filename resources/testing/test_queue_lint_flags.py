#!/usr/bin/env python3
"""Fixture suite for the queue lint's never-fired flags.

Run: py resources/testing/test_queue_lint_flags.py
(Plain script, never pytest — see CLAUDE.md's scripting constraints.)

Why a fixture rather than an observation. Only the blocked-by flag has ever
fired in practice, because the real queue has never contained the other faults:
a work-item heading with no slug, a missing section heading, a red-flag state
that is neither cleared nor uncleared, and prose sitting under no work item.
Exercising those means writing bad queue lines on purpose. An unexercised check
is not a passing check — it is a check nobody has ever seen work.

One correction to the item that asked for this. It listed "missing provenance"
as a fourth lint flag. There is no such check and there should not be:
provenance is a prose convention, and the rules state explicitly that it is not
a lint-checked field. Orphaned prose is the fourth check that had never fired,
so it is what this suite covers in its place.
"""

import importlib.util
import os
import sys

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass

HOOK = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "plugin", "throughliner", "hooks", "post_tool_use.py",
)

failures = []


def check(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + ("" if ok else f" — {detail}"))
    if not ok:
        failures.append(label)


def load_lint():
    spec = importlib.util.spec_from_file_location("post_tool_use", HOOK)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.lint


CLEAN = """# QUEUE

## Processed

#### A perfectly ordinary work item [alpha]
Filed by Claude. Rationale for alpha.

--- Cleared to run above this line ---

## Unprocessed

#### Another ordinary work item [beta]
Filed by Claude. Rationale for beta.
"""


def test_clean_queue_is_silent():
    """The control. A suite that fires on correct input proves nothing."""
    lint = load_lint()
    warnings = lint(CLEAN)
    check("a well-formed queue produces no warnings", not warnings,
          f"got: {warnings}")


def test_slugless_heading_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("#### A perfectly ordinary work item [alpha]",
                        "#### A work item nobody gave a slug")
    warnings = lint(bad)
    hit = any("no [slug]" in w for w in warnings)
    check("a heading with no slug is flagged", hit, f"got: {warnings}")


def test_missing_section_heading_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("## Unprocessed\n", "")
    warnings = lint(bad)
    hit = any("Unprocessed' section heading is missing" in w for w in warnings)
    check("a missing section heading is flagged", hit, f"got: {warnings}")


def test_invalid_red_flag_state_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("Rationale for beta.",
                        "Rationale for beta.\nRed flag · State: probably fine")
    warnings = lint(bad)
    hit = any("cleared / uncleared" in w for w in warnings)
    check("a red-flag state outside cleared/uncleared is flagged", hit,
          f"got: {warnings}")


def test_valid_red_flag_states_are_not_flagged():
    """The other half of the same check — it must not fire on correct markers."""
    lint = load_lint()
    for state in ("cleared", "uncleared"):
        ok = CLEAN.replace("Rationale for beta.",
                           f"Rationale for beta.\nRed flag · State: {state}")
        warnings = [w for w in lint(ok) if "cleared / uncleared" in w]
        check(f"'{state}' is accepted as a red-flag state", not warnings,
              f"got: {warnings}")


def test_orphaned_prose_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("## Processed\n",
                        "## Processed\n\nProse belonging to no work item.\n")
    warnings = lint(bad)
    hit = any("no #### heading" in w or "belongs to no work item" in w
              for w in warnings)
    check("prose under no work item is flagged", hit, f"got: {warnings}")


if __name__ == "__main__":
    print("test_queue_lint_flags")
    test_clean_queue_is_silent()
    test_slugless_heading_is_flagged()
    test_missing_section_heading_is_flagged()
    test_invalid_red_flag_state_is_flagged()
    test_valid_red_flag_states_are_not_flagged()
    test_orphaned_prose_is_flagged()
    print(f"\n{len(failures)} failure(s)" if failures else "\nall passed")
    sys.exit(1 if failures else 0)
