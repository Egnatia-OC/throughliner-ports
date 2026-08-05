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
  4. A "Blocked by: [slug]" line naming a slug that doesn't resolve to a
     work item in the file, or that resolves to one sitting BELOW the
     blocked item. This is the one dependency edge the model has, and it
     is linted because wording alone demonstrably failed at it: with no
     explicit field, dependencies were repeatedly written as prose
     conditions naming another item's slug, where nothing could check
     them. Position can't carry a dependency either — it expresses order,
     not why the order is what it is, so a reorder silently inverts it.
  5. The cleared-to-run marker itself. /next's whole run bound is the
     `--- Cleared to run above this line ---` line, and no other check
     looked at it: a queue with no marker, or with two, linted clean.
     Flagged: zero markers while Processed holds work items; more than
     one marker anywhere; a marker sitting in Unprocessed. (The read-side
     protection is next.md's fail-closed rule — no marker means NOTHING
     is cleared; this check is the write-side advisory half.)
  6. Orphaned prose — a non-blank line inside Processed or Unprocessed
     that belongs to no #### work-item block. Every other check validates
     items it can SEE; delete a heading and the item doesn't fail
     validation, it stops existing, its rationale indistinguishable from
     the previous item's. A concurrent session did exactly that — a
     capture write landed on an existing item's heading line and the
     damage reached a commit unnoticed. This check catches it at the
     moment of the write. Not concurrency-specific: any bad edit landing
     on a heading produces it.
  7. A #### heading newly inserted under Processed while a build is
     active (_build.md exists). A /next run REMOVES items from Processed
     and never inserts them — inserting is processing, which is /plan's,
     and a run that meets undesigned work has capture-and-continue as its
     sanctioned move. Checked from the edit's own new/old strings, so it
     only fires on Edit/MultiEdit insertions it can actually attribute.

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

# The one dependency field: "Blocked by: [slug]" on its own line beneath a
# work item's description. Matched leniently on spacing and case so a slip
# still reads as the field and still gets validated rather than silently
# passing as prose.
BLOCKED_BY = re.compile(r"^Blocked by:\s*(.*)$", re.IGNORECASE)

# Slug references inside a Blocked by: line. More than one is allowed —
# each is resolved and positioned independently.
SLUG_REF = re.compile(r"\[([a-z0-9][a-z0-9-]+)\]")

# The readiness marker /next runs on. Matched exactly: this literal is the
# run bound, and near-misses are deliberately not recognised as markers —
# a mangled marker reads as missing (check 5 flags it) rather than as a
# second, looser marker format the docs never defined.
CLEARED_MARKER = "--- Cleared to run above this line ---"

# Structural non-item lines that legitimately sit inside a work section
# without belonging to any #### block: the readiness marker and the
# planning-gate marker (`--- Plan session here: <reason> ---`).
STRUCTURAL_LINE = re.compile(r"^---\s.*---$")


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


def _check_blocked_by(blocks, warnings):
    """Check 4: every `Blocked by: [slug]` resolves, and points upward.

    Two failures, both silent without this check. An unresolvable slug is a
    dependency on nothing — a typo or a deleted item — so the blocked work
    waits forever on something that will never land. A slug resolving to an
    item BELOW the blocked one is a queue that contradicts itself: the thing
    depended on is scheduled after the thing depending on it.

    Advisory like the rest: novel shapes pass, and a flagged line is for the
    session to judge, not for the hook to enforce.
    """
    positions = {}
    for b in blocks:
        m = SLUG_AT_END.search(b["heading"])
        if m:
            positions[m.group(0).strip()[1:-1]] = b["idx"]

    for b in blocks:
        own = SLUG_AT_END.search(b["heading"])
        own_slug = own.group(0).strip()[1:-1] if own else None
        for line in b["lines"][1:]:
            match = BLOCKED_BY.match(line)
            if not match:
                continue
            refs = SLUG_REF.findall(match.group(1))
            if not refs:
                warnings.append(
                    f"line {b['idx'] + 1}: work item {b['heading'][:60]!r} has a "
                    "'Blocked by:' line naming no [slug] — the field takes the "
                    "slug of the queued item this one waits on."
                )
                continue
            for ref in refs:
                if ref == own_slug:
                    warnings.append(
                        f"line {b['idx'] + 1}: work item {b['heading'][:60]!r} is "
                        "blocked by itself."
                    )
                elif ref not in positions:
                    warnings.append(
                        f"line {b['idx'] + 1}: 'Blocked by: [{ref}]' names a slug "
                        "that isn't a work item in this queue — check the spelling, "
                        "or the item may have been deleted or already shipped."
                    )
                elif positions[ref] > b["idx"]:
                    warnings.append(
                        f"line {b['idx'] + 1}: 'Blocked by: [{ref}]' points at an "
                        "item sitting BELOW this one — the work depended on should "
                        "come first. Reorder, or the dependency reads backwards."
                    )


def _check_readiness_marker(annotated, blocks, warnings):
    """Check 5: exactly one readiness marker, in Processed, when work exists.

    The marker is the single boundary /next runs on, so its absence or
    duplication is a structural fault even though every item validates.
    Flagged, not repaired — advisory like the rest. The dangerous half of
    the failure (a missing marker silently clearing everything) is closed
    read-side in next.md, which now treats no-marker as nothing-cleared;
    this check is what makes the fault visible at the moment of the write.
    """
    marker_lines = [
        (i, h2) for i, line, h2, _ih in annotated if line == CLEARED_MARKER
    ]
    processed_has_items = any(
        h2 == "Processed" and WORKLINE_HEADING.match(line)
        for _i, line, h2, _ih in annotated
    )
    if len(marker_lines) > 1:
        lines_shown = ", ".join(str(i + 1) for i, _s in marker_lines)
        warnings.append(
            f"lines {lines_shown}: the cleared-to-run marker appears "
            f"{len(marker_lines)} times — there must be exactly one; /next "
            "runs on a single boundary and two markers make the run bound "
            "ambiguous."
        )
    elif not marker_lines and processed_has_items:
        warnings.append(
            "Processed holds work items but the '--- Cleared to run above "
            "this line ---' marker is missing — /next treats a missing "
            "marker as NOTHING cleared, so no work will run until the "
            "marker is restored."
        )
    for i, h2 in marker_lines:
        if h2 == "Unprocessed":
            warnings.append(
                f"line {i + 1}: the cleared-to-run marker sits in Unprocessed "
                "— it belongs in Processed, where it bounds what /next may "
                "run."
            )


def _check_orphaned_prose(annotated, warnings):
    """Check 6: every non-blank line in a work section belongs to a block.

    A line is orphaned when it sits inside Processed or Unprocessed with no
    #### heading above it (since the section started, or since a non-item
    heading ended the previous block). Structural `--- ... ---` marker lines
    are exempt. One flag per contiguous orphan run, so a destroyed heading
    yields one warning rather than one per rationale line.
    """
    in_block = False
    flagged_run = False
    for i, line, h2, is_heading in annotated:
        if h2 not in WORK_SECTIONS:
            in_block = False
            flagged_run = False
            continue
        if WORKLINE_HEADING.match(line):
            in_block = True
            flagged_run = False
            continue
        if is_heading:
            # A section heading or stray sub-heading ends any block.
            in_block = False
            flagged_run = False
            continue
        if not line or STRUCTURAL_LINE.match(line):
            flagged_run = False if not line else flagged_run
            continue
        if not in_block and not flagged_run:
            warnings.append(
                f"line {i + 1}: prose belongs to no work item — the text "
                f"starting {line[:50]!r} has no #### heading above it in this "
                "section. A destroyed or missing heading leaves an item's "
                "rationale orphaned like this; check whether an item's "
                "heading line was overwritten."
            )
            flagged_run = True


def _added_headings(tool_name: str, tool_input: dict) -> list[str]:
    """Work-item headings this edit ADDED, from its own old/new strings.

    Only Edit and MultiEdit can be diffed this way; a Write replaces the
    whole file and its additions can't be attributed, so it contributes
    nothing (deny-list design: missed cases pass silently).
    """
    pairs = []
    if tool_name == "Edit":
        pairs.append(
            (tool_input.get("old_string") or "", tool_input.get("new_string") or "")
        )
    elif tool_name == "MultiEdit":
        for e in tool_input.get("edits") or []:
            if isinstance(e, dict):
                pairs.append(
                    (e.get("old_string") or "", e.get("new_string") or "")
                )
    added = []
    for old, new in pairs:
        old_heads = {
            ln.strip() for ln in old.splitlines() if WORKLINE_HEADING.match(ln.strip())
        }
        for ln in new.splitlines():
            s = ln.strip()
            if WORKLINE_HEADING.match(s) and s not in old_heads:
                added.append(s)
    return added


def _check_processed_insert_during_build(
    annotated, added_headings, has_active_build, warnings
):
    """Check 7: a run never inserts into Processed.

    Fires only when a build is active AND this edit's own strings show a
    heading being added AND that heading now sits under Processed. A /next
    run removes its items from Processed at scope-lock and appends captures
    to Unprocessed; inserting into Processed is processing, which belongs
    to /plan. (A parallel /plan session editing the queue while a build
    runs elsewhere can trip this — advisory, so the session judges it.)
    """
    if not has_active_build or not added_headings:
        return
    added = {h for h in added_headings}
    for i, line, h2, _ih in annotated:
        if h2 == "Processed" and line in added:
            warnings.append(
                f"line {i + 1}: a work item was INSERTED under Processed while "
                "a build is active — a run removes items from Processed and "
                "never adds them; new work goes to Unprocessed as a capture, "
                "and moving items into Processed is /plan's."
            )


def lint(content: str, tool_name: str = "", tool_input: dict | None = None,
         has_active_build: bool = False) -> list[str]:
    annotated = _annotate(content)
    blocks = _workline_blocks(annotated)
    warnings = []
    _check_slugs(blocks, warnings)
    _check_sections(annotated, warnings)
    _check_red_flag_states(annotated, warnings)
    _check_blocked_by(blocks, warnings)
    _check_readiness_marker(annotated, blocks, warnings)
    _check_orphaned_prose(annotated, warnings)
    _check_processed_insert_during_build(
        annotated,
        _added_headings(tool_name, tool_input or {}),
        has_active_build,
        warnings,
    )
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

    has_active_build = os.path.isfile(os.path.join(cwd, "_build.md"))
    warnings = lint(content, tool_name, tool_input, has_active_build)
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
