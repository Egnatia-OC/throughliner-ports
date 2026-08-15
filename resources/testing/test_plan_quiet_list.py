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

Extended 2026-08-15 ([plan-scope-lock-denies]): the gate no longer asks about a
write outside the list, it DENIES it, on the user's decision that an ask waved
through is not consent. The list itself is unchanged, so the boolean cases below
still pin what they always did — but a suite that only checks the list cannot
tell an ask from a denial, which is now the whole point of the gate. The
end-to-end block at the bottom drives the hook for real and asserts the decision.
"""

import json
import os
import subprocess
import sys
import tempfile

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
    # The build working file is session-scoped: `_build-<session id>.md`. The
    # bare `_build.md` name this case used to assert is the retired shape, and
    # the hook deliberately no longer matches it — a bare name was visible to
    # every session on the project, which is what session-scoping removed.
    # Asserting the current shape is what keeps the suite honest.
    ("_build-3f9c1a2b-7d4e-4c88-b1a0-5e2d6f8c9a01.md", True,
     "the build working file"),
    ("_build.md", False, "the retired bare name is no longer on the list"),
    # The planning working file was deleted from the method on 2026-08-14: a
    # planning session now writes QUEUE.md, SPEC.md and LOG/ and nothing else,
    # so a `_plan-` write is exactly the surprise the gate should surface. This
    # case asserted True until then.
    ("_plan-3f9c1a2b-7d4e-4c88-b1a0-5e2d6f8c9a01.md", False,
     "the retired planning working file is denied"),
    (os.path.join("LOG", "index.md"), True, "the log index"),
    (os.path.join("LOG", "2026-08-11-entry.md"), True, "a log entry file"),
    # FAQ/ is on the list because the close REQUIRES an FAQ disposition, so a
    # denial there would break a mandated step. templates/ is deliberately off
    # it: a template edit changes what every future consumer receives.
    (os.path.join("FAQ", "faq.md"), True, "the FAQ the close must be able to write"),
    (os.path.join("FAQ", "index.md"), True, "the FAQ index"),
    (os.path.join("plugin", "throughliner", "templates", "faq-template.md"), False,
     "a template is denied — it changes what every consumer receives"),
    ("README.md", False, "an ordinary project file is denied"),
    (os.path.join("plugin", "throughliner", "docs-b", "plan.md"), False,
     "a shipped doc is denied"),
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

# --- end to end: the decision itself, not just the list ----------------------
#
# The list has never distinguished an ask from a denial, and from 2026-08-15 the
# difference is the gate. These cases drive the hook as a subprocess with a real
# PreToolUse payload, exactly as test_pre_tool_use_shell_writes.py does, in a
# temp project with NO build working file — which is the condition the planning
# branch keys on.

HOOK = os.path.join(HOOKS, "pre_tool_use.py")


def _decide(cwd, path):
    payload = {
        "cwd": cwd,
        "tool_name": "Write",
        "tool_input": {"file_path": path, "content": "x"},
        "session_id": "test-session",
    }
    proc = subprocess.run(
        [sys.executable, HOOK], input=json.dumps(payload),
        capture_output=True, text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if not proc.stdout.strip():
        return "pass"
    try:
        out = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return "pass"
    return (out.get("hookSpecificOutput") or {}).get("permissionDecision", "pass")


_tmp = tempfile.mkdtemp(prefix="plan-lock-test-")
with open(os.path.join(_tmp, "SPEC.md"), "w", encoding="utf-8") as _f:
    _f.write("# SPEC\n")

E2E = [
    ("README.md", "deny", "a write outside the list is DENIED, not asked"),
    (os.path.join("plugin", "hooks", "thing.py"), "deny",
     "a shipped file is denied in a planning session"),
    ("QUEUE.md", "pass", "the queue passes silently"),
    ("SPEC.md", "pass", "the spec passes silently"),
    (os.path.join("LOG", "2026-08-15-entry.md"), "pass", "a log entry passes"),
    # Load-bearing: the always-loaded rules require a research finding to be
    # filed as part of using it, so denying this path would break a shipped duty.
    (os.path.join("resources", "research", "a-finding.md"), "pass",
     "research is writable in a planning session"),
    (os.path.join("FAQ", "faq.md"), "pass",
     "the FAQ is writable — the close is required to dispose of it"),
]

for rel, expected, what in E2E:
    got = _decide(_tmp, os.path.join(_tmp, rel))
    status = "ok" if got == expected else "FAIL"
    if got != expected:
        failures.append((rel, expected, got, what))
    print(f"[{status}] end-to-end {rel!r} -> {got} ({what})")

print()
if failures:
    print(f"{len(failures)} failure(s):")
    for path, expected, got, what in failures:
        print(f"  {path!r}: expected {expected}, got {got} — {what}")
    sys.exit(1)
print("all cases passed")
