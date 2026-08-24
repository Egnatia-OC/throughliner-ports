#!/usr/bin/env python3
"""Regression tests for pre_tool_use.py's LOG-entry overwrite guard suggestion.

Host-only dev artifact — not shipped in the plugin package.

Run:  py resources/testing/test_pre_tool_use_overwrite_guard.py

No test framework, matching the other suites here: each case builds a temp
project, drives the hook as a subprocess with a real PreToolUse Write payload,
and asserts on the JSON decision that comes back.

Why this exists ([guard-suggests-legacy-record-suffix]): the refusal used to
suggest the legacy numeric `-2` name unconditionally, while the record-naming
rule says a second record carries its session kind (`-plan` / `-build`) and
the number is only the fallback when both are taken. The guard cannot see the
session's kind, so where both kind names are free it names both.
"""

import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOOK = os.path.join(ROOT, "plugin", "throughliner", "hooks", "pre_tool_use.py")

_failures = []


def check(name, condition, detail=""):
    if condition:
        print("  ok   " + name)
    else:
        print("  FAIL " + name + ("  -- " + detail if detail else ""))
        _failures.append(name)


def make_project(log_files=()):
    d = tempfile.mkdtemp(prefix="overwrite-guard-test-")
    with open(os.path.join(d, "SPEC.md"), "w", encoding="utf-8") as f:
        f.write("# SPEC\n")
    os.makedirs(os.path.join(d, "LOG"), exist_ok=True)
    for name in log_files:
        with open(os.path.join(d, "LOG", name), "w", encoding="utf-8") as f:
            f.write("existing record\n")
    return d


def drive_write(cwd, relpath):
    payload = {
        "cwd": cwd,
        "tool_name": "Write",
        "tool_input": {"file_path": os.path.join(cwd, relpath),
                       "content": "new record"},
        "session_id": "test-session",
    }
    proc = subprocess.run(
        [sys.executable, HOOK],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if not proc.stdout.strip():
        return {}
    try:
        out = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {}
    return out.get("hookSpecificOutput") or {}


ENTRY = "2026-08-24-some-slug.md"


def main():
    print("test_pre_tool_use_overwrite_guard")

    # 1. Both kind names free -> refusal offers them, and no bare numeric name.
    d = make_project(log_files=[ENTRY])
    out = drive_write(d, os.path.join("LOG", ENTRY))
    reason = out.get("permissionDecisionReason", "")
    check("collision denies", out.get("permissionDecision") == "deny")
    check("offers -plan when free", "2026-08-24-some-slug-plan.md" in reason,
          reason)
    check("offers -build when free", "2026-08-24-some-slug-build.md" in reason,
          reason)
    check("no numeric name while a kind name is free",
          "2026-08-24-some-slug-2.md" not in reason, reason)
    check("names the record-naming rule", "record-naming rule" in reason,
          reason)

    # 2. One kind name taken -> only the free one is offered.
    d = make_project(log_files=[ENTRY, "2026-08-24-some-slug-plan.md"])
    reason = drive_write(d, os.path.join("LOG", ENTRY)).get(
        "permissionDecisionReason", "")
    check("taken kind name not offered",
          "2026-08-24-some-slug-plan.md or" not in reason, reason)
    check("free kind name still offered",
          "2026-08-24-some-slug-build.md" in reason, reason)

    # 3. Both kind names taken -> numeric fallback offered.
    d = make_project(log_files=[ENTRY, "2026-08-24-some-slug-plan.md",
                                "2026-08-24-some-slug-build.md"])
    reason = drive_write(d, os.path.join("LOG", ENTRY)).get(
        "permissionDecisionReason", "")
    check("numeric only when both kinds taken",
          "2026-08-24-some-slug-2.md" in reason, reason)

    # 4. A genuinely new filename is not denied by this guard.
    d = make_project(log_files=[ENTRY])
    out = drive_write(d, os.path.join("LOG", "2026-08-24-other-slug.md"))
    check("new name passes the guard",
          out.get("permissionDecision") != "deny",
          str(out))

    print()
    if _failures:
        print("FAILURES: %d" % len(_failures))
        sys.exit(1)
    print("all ok")


if __name__ == "__main__":
    main()
