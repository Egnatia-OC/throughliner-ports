#!/usr/bin/env python3
"""Regression tests for pre_tool_use.py's planning quiet list.

Host-only dev artifact — not shipped in the plugin package.

Run:  python resources/testing/test_plan_quiet_list.py

No test framework, matching test_reorder_queue.py and
test_pre_tool_use_shell_writes.py: each case calls `_is_plan_quiet_path`
directly and asserts on the boolean.

Why this exists ([plan-quiet-list-case-mismatch]): the function built its
relative path with `_normalise`, which calls `os.path.normcase` — a lowercaser
on Windows and the identity on POSIX. The relative path therefore arrived as
`queue.md` and was compared case-sensitively against `"QUEUE.md"`, which could
never match. The quiet list was inverted on Windows from the day it shipped:
every write to QUEUE.md, SPEC.md and LOG/ in a planning session raised a
permission dialog, including in auto mode. On macOS and Linux `normcase` is the
identity function, so the list matched and the gate behaved as designed — which
is why a POSIX-only test would have passed throughout.

The whole class of defect is invisible without a mixed-case path, so the
mixed-case block below is the point of the file.
"""

import os
import sys

HOOKS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "plugin", "throughliner", "hooks",
)
sys.path.insert(0, HOOKS)

import pre_tool_use  # noqa: E402

CWD = os.path.normpath(r"C:\Users\Someone\Projects\My Project") if os.name == "nt" \
    else "/home/someone/projects/My Project"

CASES = [
    # (relative path, expected, what it pins)
    ("QUEUE.md", True, "the queue itself — the case that was failing"),
    ("SPEC.md", True, "the spec"),
    # Working files are session-scoped: `_plan-<session id>.md`. The bare
    # `_plan.md` / `_build.md` names these cases used to assert are the retired
    # shape, and the hook deliberately no longer matches them — a bare name was
    # visible to every session on the project, which is what session-scoping
    # removed. Asserting the current shape is what keeps the suite honest.
    ("_plan-3f9c1a2b-7d4e-4c88-b1a0-5e2d6f8c9a01.md", True,
     "a planning session's own working file"),
    ("_build-3f9c1a2b-7d4e-4c88-b1a0-5e2d6f8c9a01.md", True,
     "the build working file"),
    ("_build.md", False, "the retired bare name is no longer on the list"),
    (os.path.join("LOG", "index.md"), True, "the log index"),
    (os.path.join("LOG", "2026-08-11-entry.md"), True, "a log entry file"),
    ("README.md", False, "an ordinary project file still asks"),
    (os.path.join("plugin", "throughliner", "docs-b", "plan.md"), False,
     "a shipped doc still asks"),
    ("QUEUEQ.md", False, "a near-miss name is not on the list"),
]

failures = []

for rel, expected, what in CASES:
    got = pre_tool_use._is_plan_quiet_path(os.path.join(CWD, rel), CWD)
    status = "ok" if got == expected else "FAIL"
    if got != expected:
        failures.append((rel, expected, got, what))
    print(f"[{status}] {rel!r} -> {got} ({what})")

# The mixed-case cases. On Windows a caller can hand the hook a path whose
# casing differs from the project root's, and the containment test normcases,
# so the relative path must survive that without being lowercased itself.
if os.name == "nt":
    mixed = [
        (CWD.lower() + os.sep + "queue.md", True, "an all-lowercase absolute path"),
        (CWD.upper() + os.sep + "QUEUE.MD", True, "an all-uppercase absolute path"),
        (CWD + os.sep + "log" + os.sep + "index.md", True, "a lowercased LOG folder"),
        (CWD.lower() + os.sep + "readme.md", False,
         "case-insensitivity must not widen the list"),
    ]
    for path, expected, what in mixed:
        got = pre_tool_use._is_plan_quiet_path(path, CWD)
        status = "ok" if got == expected else "FAIL"
        if got != expected:
            failures.append((path, expected, got, what))
        print(f"[{status}] {path!r} -> {got} ({what})")
else:
    print("[skip] mixed-case cases are Windows-only — "
          "normcase is the identity on this platform")

print()
if failures:
    print(f"{len(failures)} failure(s):")
    for path, expected, got, what in failures:
        print(f"  {path!r}: expected {expected}, got {got} — {what}")
    sys.exit(1)
print("all cases passed")
