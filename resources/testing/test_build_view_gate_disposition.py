#!/usr/bin/env python3
"""A cleared item with a `Rule gate:` line in its prose produces a view block
carrying it — including the bolded label form.

Run as a plain script: py resources/testing/test_build_view_gate_disposition.py
(never through pytest — see CLAUDE.md's scripting constraints).
"""

import os
import subprocess
import sys
import tempfile

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding='utf-8', errors='replace')
    except (AttributeError, ValueError, OSError):
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SCRIPT = os.path.join(ROOT, "plugin", "throughliner", "scripts",
                      "generate_build_view.py")

QUEUE = """# QUEUE

## Processed

#### Amend a standing rule somewhere [rule-item]
Some rationale prose.
Rule gate: run — admitted as an amendment to the parent rule
--- Build block ---
Changes: `docs/example.md` — one clause added.
Acceptance: the clause is present.
--- End build block ---

#### Another rule item with a bolded label [bold-item]
**Rule gate:** not needed — typo fix
FAQ: not needed because nothing user-facing changes
--- Build block ---
Changes: `docs/other.md` — a word.
Acceptance: fine.
--- End build block ---

--- Cleared to run above this line ---

## Unprocessed

#### A capture [some-capture]
Prose.
"""

failures = []


def check(name, cond, detail=""):
    if cond:
        print("PASS  " + name)
    else:
        failures.append(name)
        print("FAIL  " + name + ("  — " + detail if detail else ""))


def main():
    with tempfile.TemporaryDirectory() as td:
        qpath = os.path.join(td, "QUEUE.md")
        with open(qpath, "w", encoding="utf-8") as f:
            f.write(QUEUE)
        out = os.path.join(td, "BUILD-VIEW.md")
        proc = subprocess.run(
            [sys.executable, SCRIPT, qpath, "--out", out],
            capture_output=True, encoding="utf-8")
        check("script exits 0", proc.returncode == 0, proc.stderr)
        with open(out, encoding="utf-8") as f:
            view = f.read()

        rule_section = view.split("### [rule-item]")[1].split("### [")[0]
        check("plain Rule gate line appears in its item's block",
              "Rule gate: run — admitted as an amendment to the parent rule"
              in rule_section)

        bold_section = view.split("### [bold-item]")[1].split("## Everything")[0]
        check("bolded Rule gate label is normalised into the block",
              "Rule gate: not needed — typo fix" in bold_section)
        check("FAQ disposition travels too",
              "FAQ: not needed because nothing user-facing changes"
              in bold_section)
        check("bold markers do not survive into the emitted line",
              "**Rule gate:**" not in bold_section)

    if failures:
        print("\n%d failure(s)" % len(failures))
        sys.exit(1)
    print("\nall passed")


if __name__ == "__main__":
    main()
