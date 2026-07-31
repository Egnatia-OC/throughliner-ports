#!/usr/bin/env python3
"""
PostToolUse hook — advisory lint of QUEUE.md structure after edits.

Fires after Edit/Write/MultiEdit lands on the project's QUEUE.md. Reads
the file from disk and flags known format violations against the
two-section work-item model:

  1. A work item whose description heading doesn't end in a [slug]. A
     work item renders as a #### heading under ## Processed or
     ## Unprocessed; the slug at the end of that heading is what lets a
     later LOG entry name the work precisely.
  2. A missing section heading — both ## Processed and ## Unprocessed
     must be present. They are the two sections the whole model runs on.
  3. A red-flag marker line ("Red flag · State: ...") whose state isn't
     one of cleared / uncleared. A red flag is an ordinary work
     line carrying this one extra marker; the state must be valid.

Provenance is NOT linted. The old model required every work item to
carry a "captured by you" / "by Claude" label; that requirement is
gone. The convention is now asymmetric and default-AI: an unmarked item
is assumed to come from the AI, and an explicit "captured by you" credit
is written only when the user personally raised, pushed through, or
wrote the item. No AI-authorship label is ever written. Because a
user-credit is optional and an AI label is absent by design, there is
nothing to enforce — so the lint neither requires a label nor forbids
one (a leftover "by Claude" on an old item is harmless).

Deny-list by design: only known violations are flagged; unknown or
novel structure passes in silence, so the format can evolve (new
sections, new line shapes) without fighting the linter. All findings
are advisory — fed back to Claude as context next to the tool result,
never blocking: the edit has already landed, and judging whether a
flag is real stays with the session.
"""

import json
import os
import re
import sys


# A work item renders as a #### heading; its slug sits at the end of that
# heading line (processed and unprocessed work show this way, so the list
# — including anything below the cleared-to-run line — is navigable from
# an editor outline). The heading line is the work item's description line.
WORKLINE_HEADING = re.compile(r"^####\s+\S")

# The trailing [slug] on a work-item heading: lowercase kebab, two chars
# minimum, so a stray [x] tick or an [PROMPT]-style token never counts.
SLUG_AT_END = re.compile(r"\[[a-z0-9][a-z0-9-]+\]\s*$")

# A red-flag marker line: "Red flag · State: <state>". The middle dot is
# U+00B7 and is matched leniently (optional) so a spacing slip still reads
# as a marker and its state still gets validated.
RED_FLAG_MARKER = re.compile(r"^Red flag\s*·?\s*State:\s*(.*)$", re.IGNORECASE)

# The two sections the whole model runs on.
WORK_SECTIONS = ("Processed", "Unprocessed")

VALID_FLAG_STATES = {"cleared", "uncleared"}


def _normalise(path: str) -> str:
    return os.path.normcase(os.path.normpath(path))


def _annotate(content: str):
    """Yield (index, stripped line, current h2, is_heading) per line.

    h2 is the nearest preceding `## ` heading (the section the line sits
    in); is_heading is true for any markdown heading line (`#`..`######`).
    """
    h2 = None
    out = []
    for i, raw in enumerate(content.splitlines()):
        stripped = raw.strip()
        is_heading = bool(re.match(r"#{1,6}\s", raw))
        if raw.startswith("## ") and not raw.startswith("### "):
            h2 = raw[3:].strip()
        out.append((i, stripped, h2, is_heading))
    return out


def _workline_blocks(annotated):
    """Group each #### work item under a work section with its own block.

    A block is the heading line plus every following line up to the next
    #### heading, the next heading of any level, or a section change. Lines
    outside the Processed/Unprocessed sections are ignored entirely, so a
    #### heading elsewhere in the file is never treated as a work item.
    """
    blocks = []
    current = None
    for i, line, h2, is_heading in annotated:
        if h2 not in WORK_SECTIONS:
            if current:
                blocks.append(current)
                current = None
            continue
        if WORKLINE_HEADING.match(line):
            if current:
                blocks.append(current)
            current = {"idx": i, "heading": line, "lines": [line]}
        elif is_heading:
            # Any other heading (a section change, a stray sub-heading) ends
            # the current work-item block.
            if current:
                blocks.append(current)
                current = None
        elif current is not None:
            current["lines"].append(line)
    if current:
        blocks.append(current)
    return blocks


def _check_slugs(blocks, warnings):
    """Check 1: every work-item heading ends in a [slug]."""
    for b in blocks:
        if not SLUG_AT_END.search(b["heading"]):
            warnings.append(
                f"line {b['idx'] + 1}: work item {b['heading'][:60]!r} has no "
                "[slug] at the end of its description line — every work item "
                "needs one so a later LOG entry can name it."
            )


def _check_sections(annotated, warnings):
    """Check 2: both ## Processed and ## Unprocessed headings are present."""
    present = {h2 for _i, _l, h2, _ih in annotated if h2}
    for name in WORK_SECTIONS:
        if name not in present:
            warnings.append(
                f"the '## {name}' section heading is missing — the queue holds "
                "two sections, Processed (discussed, kept work) and Unprocessed "
                "(captured, not yet fully processed)."
            )


def _check_red_flag_states(annotated, warnings):
    """Check 3: a red-flag marker line names a valid state.

    Scans every line, not only work-item blocks: a marker is only ever
    valid under a work item, but validating it wherever it appears is the
    fail-safe direction — a stray marker with a bad state still gets caught.
    """
    for i, line, _h2, _ih in annotated:
        match = RED_FLAG_MARKER.match(line)
        if not match:
            continue
        rest = match.group(1).strip()
        token = rest.split()[0].strip(".,;:—–-").lower() if rest else ""
        if token not in VALID_FLAG_STATES:
            shown = rest[:30] if rest else "(none)"
            warnings.append(
                f"line {i + 1}: red-flag marker has state {shown!r}, but a red "
                "flag's state must be one of cleared / uncleared."
            )


def lint(content: str) -> list[str]:
    annotated = _annotate(content)
    blocks = _workline_blocks(annotated)
    warnings = []
    _check_slugs(blocks, warnings)
    _check_sections(annotated, warnings)
    _check_red_flag_states(annotated, warnings)
    return warnings


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return 0

    if not isinstance(data, dict):
        return 0

    cwd = data.get("cwd", "")
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input") or {}

    if tool_name not in ("Edit", "Write", "MultiEdit"):
        return 0

    filepath = tool_input.get("file_path", "")
    if not filepath or not cwd:
        return 0

    # Only the project-root QUEUE.md, only in adopted projects.
    if _normalise(filepath) != _normalise(os.path.join(cwd, "QUEUE.md")):
        return 0
    if not os.path.isfile(os.path.join(cwd, "SPEC.md")):
        return 0

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return 0

    warnings = lint(content)
    if not warnings:
        return 0

    message = (
        "[Sovereign Implementer] QUEUE.md structure lint (advisory). "
        "These flag known violations only — novel structure is allowed "
        "and never flagged. Judge each one: fix what's genuinely wrong "
        "in a follow-up edit, leave what isn't.\n"
        + "\n".join(f"- {w}" for w in warnings)
    )
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": message,
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
