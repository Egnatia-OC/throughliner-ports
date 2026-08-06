"""Status-line probe for [statusline-context-reader].

Answers one question: does the Claude Code desktop app run a status-line
command at all, and if it does, does the payload actually carry
`context_window.used_percentage`?

Claude Code feeds live context-window usage to exactly one surface — the
status-line command, via a JSON payload on stdin. Hooks receive no context
data at all, so this is the only mechanism available for context-% session
sizing (see resources/research/statusline-context-reader-feasibility.md).

How it is meant to work: this script is registered as the `statusLine`
command in .claude/settings.local.json. Claude Code then runs it on every
status-bar refresh, handing it the payload on stdin. Each run appends one
line to a DURABLE marker file outside the repo, so the record survives a
full app restart — which is the whole point, because the app appears to load
settings only at launch.

Reading the result — the three outcomes the test distinguishes:

    marker file has lines with real percentages
        -> the mechanism works. The feature is buildable; design the
           threshold, remembering that used_percentage UNDERSTATES real
           usage (it excludes tool definitions, CLAUDE.md, MCP configs and
           the system prompt — Anthropic issue #17959), so a naive
           threshold fires far too late.

    marker file has lines, but every value reads "null"
        -> the command runs but the payload does not carry the field. A
           timing or payload-shape problem, not a dead mechanism.

    marker file does not exist, or exists and stays empty
        -> the desktop app does not run status-line commands. The mechanism
           is dead in this environment: delete this probe, and the automated
           half of [session-sizing-and-break-lines] falls back to manual
           session-break lines.

This script is a diagnostic instrument, not part of the shipped plugin. It
lives under resources/testing/ and is host-only.
"""

import datetime
import json
import os
import sys

MARKER = os.path.join(os.path.expanduser("~"), ".claude", "si-statusline-probe.log")


def main() -> int:
    raw = sys.stdin.read()

    used = None
    remaining = None
    parse_error = None

    try:
        payload = json.loads(raw) if raw.strip() else {}
        window = payload.get("context_window") or {}
        used = window.get("used_percentage")
        remaining = window.get("remaining_percentage")
    except Exception as exc:  # a probe never crashes the status bar
        parse_error = f"{type(exc).__name__}: {exc}"

    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    record = f"{stamp}\tused={used}\tremaining={remaining}"
    if parse_error:
        record += f"\tparse_error={parse_error}"
    # Keep the first raw payload around: if the field is absent, its actual
    # shape is the thing a later session needs to see, not our reading of it.
    record += f"\traw_len={len(raw)}"

    try:
        os.makedirs(os.path.dirname(MARKER), exist_ok=True)
        first_write = not os.path.exists(MARKER)
        with open(MARKER, "a", encoding="utf-8") as handle:
            if first_write:
                handle.write(f"# SI status-line probe — first run {stamp}\n")
                handle.write(f"# first raw payload: {raw[:2000]}\n")
            handle.write(record + "\n")
    except Exception:
        pass  # never let a marker-file problem break the user's status bar

    # Visible in the app's status bar, so the test is observable live too.
    if used is None:
        sys.stdout.write("SL-TEST ctx=unavailable")
    else:
        sys.stdout.write(f"SL-TEST ctx={used}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
