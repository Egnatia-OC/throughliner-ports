#!/usr/bin/env python3
"""Regression tests for pre_tool_use.py's structured shell-write matcher.

Host-only dev artifact — not shipped in the plugin package.

Run:  python resources/testing/test_pre_tool_use_shell_writes.py

No test framework, matching test_reorder_queue.py: each case builds a temp
project (SPEC.md + optional _build.md), drives the hook as a subprocess with a
real PreToolUse payload, and asserts on the JSON decision that comes back.

Why this exists ([shell-heredoc-write-immediately-after-authoring-the-rule]):
two live slips in one run reached for `python - <<'PY'` to write shipped docs,
and the matcher that would deny that shape was built in the same run — so its
coverage had never been tested against the commands that actually slipped.
This suite drives those exact shapes.

The finding the first run of this suite established, pinned here so it is not
re-derived: the matcher denies a scripted write only when the target is OUTSIDE
the build's Files list (its denial text names the scope-lock as its reason).
Both real slips wrote files that were IN scope for their run, so the matcher
as built would NOT have caught them. That is asserted below as current
behaviour, not endorsed as correct — whether in-scope scripted writes should
also be denied (the stale-mount overwrite reason applies to them too) is a
hook-behaviour design call routed to the queue, not decided by a test.
"""

import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOOK = os.path.join(ROOT, "plugin", "si-plugin", "hooks", "pre_tool_use.py")

_failures = []


def check(name, condition, detail=""):
    if condition:
        print("  ok   " + name)
    else:
        print("  FAIL " + name + ("  -- " + detail if detail else ""))
        _failures.append(name)


def make_project(build_files=None):
    """Temp project dir: SPEC.md always; _build.md with Files: when given."""
    d = tempfile.mkdtemp(prefix="pretool-test-")
    with open(os.path.join(d, "SPEC.md"), "w", encoding="utf-8") as f:
        f.write("# SPEC\n")
    if build_files is not None:
        lines = ["# Active Build\n\nFiles:\n"]
        for p in build_files:
            lines.append("- " + p + "\n")
        with open(os.path.join(d, "_build.md"), "w", encoding="utf-8") as f:
            f.write("".join(lines))
    return d


def drive(cwd, command):
    """Run the hook with a Bash PreToolUse payload; return the decision dict."""
    payload = {
        "cwd": cwd,
        "tool_name": "Bash",
        "tool_input": {"command": command},
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
    return (out.get("hookSpecificOutput") or {})


def decision(cwd, command):
    return drive(cwd, command).get("permissionDecision", "pass")


# The two shapes that actually slipped, verbatim in structure.
HEREDOC_APPEND = (
    "python - <<'PY'\n"
    "with open('plugin/si-plugin/templates/faq-template.md', 'a') as f:\n"
    "    f.write('new entry')\n"
    "PY"
)
HEREDOC_SUBSTITUTE = (
    "python - <<'PY'\n"
    "p = 'plugin/si-plugin/docs-b/setup.md'\n"
    "text = open(p).read()\n"
    "open('plugin/si-plugin/docs-b/setup.md', 'w').write(text.replace('a', 'b'))\n"
    "PY"
)
COMPUTED_PATH = (
    "python - <<'PY'\n"
    "name = 'faq-template.md'\n"
    "with open(f'plugin/si-plugin/templates/{name}', 'a') as f:\n"
    "    f.write('x')\n"
    "PY"
)


def main():
    print("test_pre_tool_use_shell_writes")

    # 1. The slipped append shape, target OUT of scope during a build -> deny.
    d = make_project(build_files=["plugin/si-plugin/docs-b/plan.md"])
    check(
        "heredoc append to out-of-scope file denied",
        decision(d, HEREDOC_APPEND) == "deny",
        "got: " + decision(d, HEREDOC_APPEND),
    )

    # 2. The slipped substitution shape, out of scope -> deny.
    check(
        "heredoc substitution on out-of-scope file denied",
        decision(d, HEREDOC_SUBSTITUTE) == "deny",
        "got: " + decision(d, HEREDOC_SUBSTITUTE),
    )

    # 3. Computed path -> passes. The deliberate fail-open, pinned as intended
    #    behaviour so it is not "fixed" by someone reading the denial as
    #    incomplete.
    check(
        "computed path passes (deliberate fail-open)",
        decision(d, COMPUTED_PATH) == "pass",
        "got: " + decision(d, COMPUTED_PATH),
    )

    # 4. CURRENT BEHAVIOUR, not endorsement: the same slipped shape against a
    #    file IN the build's Files list passes — which means the matcher would
    #    not have caught the two real slips, whose targets were in scope.
    #    Design question routed to the queue; if the hook is later changed to
    #    deny in-scope scripted writes too, flip this assertion deliberately.
    d2 = make_project(
        build_files=["plugin/si-plugin/templates/faq-template.md"]
    )
    check(
        "in-scope scripted write currently passes (pinned, see header)",
        decision(d2, HEREDOC_APPEND) == "pass",
        "got: " + decision(d2, HEREDOC_APPEND),
    )

    # 5. No active build -> no structured-write check at all.
    d3 = make_project(build_files=None)
    check(
        "no active build: scripted write passes (check is build-scoped)",
        decision(d3, HEREDOC_APPEND) == "pass",
        "got: " + decision(d3, HEREDOC_APPEND),
    )

    # 6. A plain non-writing python invocation passes.
    check(
        "non-writing python command passes",
        decision(d, "python plugin/si-plugin/scripts/reorder_queue.py QUEUE.md --delete x Processed")
        == "pass",
        "",
    )

    print()
    if _failures:
        print("FAILURES: " + ", ".join(_failures))
        return 1
    print("all passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
