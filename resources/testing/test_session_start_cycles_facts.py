#!/usr/bin/env python3
"""Regression tests for session_start.py's cycles facts line.

Host-only dev artifact — not shipped in the plugin package.

Run:  py resources/testing/test_session_start_cycles_facts.py

No test framework, matching the suites alongside it: this project has no test
runner, and `python` on the author's machine resolves to an application's
bundled interpreter that has no pytest.

What this pins is the artifact the due-ness check keys on. The check exists at
three sites and fired at none of them, because nothing in a session opening
said a cycles doc was there — so the absence of this line is exactly the
failure, and a project with no doc getting no line is the other half of it.
"""

import importlib.util
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOOK = os.path.join(ROOT, "plugin", "throughliner", "hooks", "session_start.py")

_spec = importlib.util.spec_from_file_location("session_start", HOOK)
hook = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hook)

_failures = []


def check(name, condition, detail=""):
    if condition:
        print("  ok   " + name)
    else:
        print("  FAIL " + name + ("\n       " + detail if detail else ""))
        _failures.append(name)


def project(cycles_doc=None):
    d = tempfile.mkdtemp(prefix="session-start-cycles-")
    if cycles_doc is not None:
        with open(os.path.join(d, "CYCLES.md"), "w", encoding="utf-8") as f:
            f.write(cycles_doc)
    return d


DEMO = """# CYCLES

## Weekly release [weekly-release]
Steps: bump, sweep, package, publish the pre-release.
Cadence: weekly, declared by the user.
Observable: the newest GitHub release's date — last turn 2026-07-01.

## Posting rhythm [posting-rhythm]
Steps: draft, approve, post, write the register line.
Cadence: fortnightly, derived from the sent register.
Observable: the newest line in INBOX/sent.md
"""


def test_a_doc_produces_a_definition_per_cycle():
    d = project(DEMO)
    facts = hook.cycles_facts(d)
    shutil.rmtree(d, ignore_errors=True)
    check("both definitions are read", facts is not None and len(facts) == 2,
          repr(facts))
    if not facts:
        return
    slugs = [row[0] for row in facts]
    check("the slugs come off the headings",
          slugs == ["weekly-release", "posting-rhythm"], repr(slugs))
    check("the cadence line travels as written",
          facts[0][2] == "weekly, declared by the user.", repr(facts[0][2]))
    check("the observable travels as written",
          facts[0][3].startswith("the newest GitHub release's date"),
          repr(facts[0][3]))
    check("a date inside the observable is surfaced as the last turn",
          facts[0][4] == "2026-07-01", repr(facts[0][4]))
    check("an observable with no date reports none",
          facts[1][4] is None, repr(facts[1][4]))


def test_no_doc_is_silent():
    """A project with no cycles pays nothing — the whole point of the trigger."""
    d = project(None)
    facts = hook.cycles_facts(d)
    shutil.rmtree(d, ignore_errors=True)
    check("no cycles doc returns None rather than an empty report",
          facts is None, repr(facts))


def test_a_doc_with_no_definitions_reports_empty():
    """Present but unparseable is its own case, and must not read as 'no cycles'."""
    d = project("# CYCLES\n\nNotes with no headings carrying a slug.\n")
    facts = hook.cycles_facts(d)
    shutil.rmtree(d, ignore_errors=True)
    check("a doc with no slug headings returns an empty list, not None",
          facts == [], repr(facts))


if __name__ == "__main__":
    print("test_session_start_cycles_facts.py")
    test_a_doc_produces_a_definition_per_cycle()
    test_no_doc_is_silent()
    test_a_doc_with_no_definitions_reports_empty()
    print()
    if _failures:
        print(f"{len(_failures)} failure(s): " + ", ".join(_failures))
        sys.exit(1)
    print("all passed")
