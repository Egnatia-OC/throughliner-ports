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

The finding the first run of this suite established, and what was done about it
([shell-write-matcher-blind-to-in-scope-targets]): the matcher used to deny a
scripted write only when the target was OUTSIDE the build's Files list, and
both real slips wrote files that were IN scope for their run — so the matcher
as built would not have caught either of them. The denial's two reasons come
apart: the scope-lock reason does not apply to an in-scope target, but the
stale-view reason (the shell can read a stale copy and silently clobber work)
applies to every scripted write regardless of scope. So the scope condition was
dropped. A detectable scripted write to ANY file inside the project is now
denied, build or no build; the scratchpad, the memory directory and anything
outside the project still pass, and a computed target path is still the
deliberate fail-open.
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

    # 4. The case this suite's first run exposed, now flipped: the same slipped
    #    shape against a file IN the build's Files list is denied. Both real
    #    slips were of exactly this shape, so this is the assertion that says
    #    the matcher would now catch them.
    d2 = make_project(
        build_files=["plugin/si-plugin/templates/faq-template.md"]
    )
    check(
        "in-scope scripted write denied (scope condition dropped)",
        decision(d2, HEREDOC_APPEND) == "deny",
        "got: " + decision(d2, HEREDOC_APPEND),
    )

    # 5. No active build -> still denied. The stale-view reason does not depend
    #    on a build being open, and the user's standing instruction forbids
    #    shell file-writes unconditionally.
    d3 = make_project(build_files=None)
    check(
        "no active build: scripted write still denied",
        decision(d3, HEREDOC_APPEND) == "deny",
        "got: " + decision(d3, HEREDOC_APPEND),
    )

    # 5b. A scripted write to a method doc is denied too — the old exemption for
    #     detectable shapes is gone. QUEUE.md is exactly the corruption route the
    #     queue mover exists to prevent.
    QUEUE_WRITE = (
        "python - <<'PY'\n"
        "open('QUEUE.md', 'w').write('clobbered')\n"
        "PY"
    )
    check(
        "scripted write to QUEUE.md denied (method-doc exemption removed)",
        decision(d3, QUEUE_WRITE) == "deny",
        "got: " + decision(d3, QUEUE_WRITE),
    )

    # 5c. The scratchpad carve-out stays: sanctioned scratch space, outside the
    #     repo, and named in the denial text as the route when scratch is what
    #     you actually need.
    scratch = os.path.join(
        tempfile.gettempdir(), "claude", "proj", "sess", "scratchpad", "note.md"
    )
    SCRATCH_WRITE = (
        "python - <<'PY'\n"
        "open(%r, 'w').write('x')\n"
        "PY" % scratch.replace("\\", "/")
    )
    check(
        "scratchpad scripted write still passes",
        decision(d3, SCRATCH_WRITE) == "pass",
        "got: " + decision(d3, SCRATCH_WRITE),
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
