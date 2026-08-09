#!/usr/bin/env python3
"""
PostToolUse hook — advisory lint of QUEUE.md structure after edits.

Fires after Edit/Write/MultiEdit lands on the project's QUEUE.md, and after
any Bash/PowerShell command in an adopted project — a shell write bypasses the
editing tools entirely, so an edit-only trigger left that whole class unlinted.
Reads
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
SLUG_AT_END = re.compile(r"\[([a-z0-9][a-z0-9-]+)\]\s*$")

# A red-flag marker line: "Red flag · State: <state>". The middle dot is
# U+00B7 and is matched leniently (optional) so a spacing slip still reads
# as a marker and its state still gets validated.
RED_FLAG_MARKER = re.compile(r"^Red flag\s*·?\s*State:\s*(.*)$", re.IGNORECASE)

# The two sections the whole model runs on.
WORK_SECTIONS = ("Processed", "Unprocessed")

VALID_FLAG_STATES = {"cleared", "uncleared"}

# The single boundary /next runs on, and the shape of any structural
# `--- ... ---` line that legitimately sits between work items.
CLEARED_MARKER = "--- Cleared to run above this line ---"
STRUCTURAL_LINE = re.compile(r"^---\s.*---$")


def write_editing_marker(cwd: str, session_id: str, filepath: str, active: bool) -> None:
    """Clear the editing-state signal after a write. Never raises.

    The closing half of the heartbeat pre_tool_use starts: same file, same
    shape, `active` false and a fresh timestamp, keeping the last-written path
    so a reader can see which document was touched. Kept as a full rewrite
    rather than a patch of the existing file, so a marker left behind by a
    crashed session is replaced wholesale rather than merged with.

    The timestamp still leads on safety: even if this never runs — the session
    dies, the write is denied — the reader treats the stale marker as "not
    editing". Same never-fail rule as the pre-write half: any error here is
    swallowed, because a companion-app convenience must not be able to break
    the user's actual work.
    """
    try:
        import datetime

        marker_dir = os.path.join(cwd, ".throughliner")
        os.makedirs(marker_dir, exist_ok=True)
        safe_id = re.sub(r"[^A-Za-z0-9._-]", "_", session_id or "unknown")
        # Version-2 shape, kept field-for-field with pre_tool_use's opening
        # half: project-relative `files` (forward slashes, no leading "./",
        # absolute fallback for a file outside the project), `written_at` for
        # diagnosis-not-freshness, `producer` constant, pid/session dropped.
        # The version stamp and the path shape must move together — a marker
        # carrying version 2's relative paths under a version-1 stamp resolves
        # against the wrong root and holds nothing, with no error.
        if filepath:
            rel = os.path.relpath(os.path.abspath(filepath), cwd)
            marker_path = (
                os.path.abspath(filepath)
                if rel.startswith("..")
                else rel.replace(os.sep, "/")
            )
            files = [marker_path]
        else:
            files = []
        payload = {
            "version": 2,
            "active": bool(active),
            "written_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "files": files,
            "producer": "throughliner",
        }
        with open(
            os.path.join(marker_dir, f"editing-{safe_id}.json"), "w", encoding="utf-8"
        ) as f:
            json.dump(payload, f)
    except Exception:
        return


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
            current = {"idx": i, "heading": line, "lines": [line], "section": h2}
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


def _check_readiness_marker(annotated, blocks, warnings):
    """Check 4: exactly one readiness marker, in Processed, when work exists.

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


BLOCKED_BY_LINE = re.compile(r"^\*{0,2}Blocked by:?\*{0,2}\s*(.+)$", re.IGNORECASE)
SLUG_REF = re.compile(r"\[([a-z0-9][a-z0-9-]*)\]")


def _check_blocked_by(annotated, blocks, warnings):
    """Check 5: below the line means blocked by a named queue item.

    Below-the-line used to mean "shelved for any reason", with the reason
    written as a prose lift-condition inside the item — a sentence like
    "cleared once [slug] ships" or "after a full computer restart". That model
    failed in a specific, repeated way: a blocker written as a sentence inside
    another item's prose is invisible as work, so nothing ever picks it up. One
    item sat below the line for weeks with a genuine user action buried in its
    lift-condition; the moment it was split out as its own work item it became
    visible immediately.

    So the rule is now exactly one thing: an item sits below the marker if and
    only if a NAMED queue item blocks it. Anything waiting on the world gets
    described as its own item in Unprocessed, where /plan will process it, and
    the blocked item names that item as its blocker. This check is what makes
    the rule real rather than a convention sessions drift from — the below-line
    population becomes derivable instead of remembered.

    Advisory like every other check here: it reports, never blocks or repairs.

    On "sits above": the queue item that decided this asked for a blocker that
    "resolves and sits above the item", which reads naturally but cannot be
    taken as literal file order — Unprocessed sits BELOW Processed in the file,
    and an Unprocessed blocker is the rule's own recommended shape. So above-ness
    is checked only where it means something: within Processed, where position
    is build order. A blocker in Unprocessed is fine by construction.
    """
    marker_idx = next(
        (i for i, line, _h2, _ih in annotated if line == CLEARED_MARKER), None
    )
    if marker_idx is None:
        # A missing marker is already reported by the readiness check, and
        # without one there is no below-the-line to check.
        return

    known = {}
    for b in blocks:
        m = SLUG_AT_END.search(b["heading"])
        if m:
            known[m.group(1)] = b

    for b in blocks:
        if b["section"] != "Processed":
            continue
        below = b["idx"] > marker_idx
        refs = []
        for line in b["lines"][1:]:
            m = BLOCKED_BY_LINE.match(line)
            if m:
                refs.extend(SLUG_REF.findall(m.group(1)))

        if not below:
            if refs:
                warnings.append(
                    f"line {b['idx'] + 1}: {b['heading'][:60]!r} sits ABOVE the "
                    "cleared-to-run marker but carries a 'Blocked by:' line — "
                    "cleared work has nothing blocking it. Either move it below "
                    "the marker or drop the blocker."
                )
            continue

        if not refs:
            warnings.append(
                f"line {b['idx'] + 1}: {b['heading'][:60]!r} sits below the "
                "cleared-to-run marker with no 'Blocked by: [slug]' line. Below "
                "the line means blocked by a named queue item and nothing else "
                "— if nothing in the queue blocks it, move it above the marker; "
                "if it waits on something in the world, file that as its own "
                "item in Unprocessed and name it here."
            )
            continue

        for slug in refs:
            target = known.get(slug)
            if target is None:
                warnings.append(
                    f"line {b['idx'] + 1}: {b['heading'][:60]!r} is blocked by "
                    f"[{slug}], which is not a work item in this queue. A "
                    "blocker must be a real item someone can pick up."
                )
            elif target["idx"] == b["idx"]:
                warnings.append(
                    f"line {b['idx'] + 1}: {b['heading'][:60]!r} names itself "
                    "as its own blocker."
                )
            elif target["section"] == "Processed" and target["idx"] > b["idx"]:
                warnings.append(
                    f"line {b['idx'] + 1}: {b['heading'][:60]!r} is blocked by "
                    f"[{slug}], which sits BELOW it in Processed. Within "
                    "Processed, position is build order, so a blocker must come "
                    "first."
                )


def _check_orphaned_prose(annotated, warnings):
    """Check 5: every non-blank line in a work section belongs to a block.

    A line is orphaned when it sits inside Processed or Unprocessed with no
    #### heading above it (since the section started, or since a non-item
    heading ended the previous block). Structural `--- ... ---` marker lines
    are exempt, and so are blockquote lines (`> ...`): /setup scaffolds each
    work section's description paragraph as a blockquote immediately under the
    section heading — positionally identical to a destroyed first item's
    stranded rationale, so position cannot discriminate; form does. A stranded
    work-item rationale is never a blockquote. One flag per contiguous orphan
    run, so a destroyed heading yields one warning rather than one per
    rationale line.
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
        if not line or STRUCTURAL_LINE.match(line) or line.startswith(">"):
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


def lint(content: str) -> list[str]:
    annotated = _annotate(content)
    blocks = _workline_blocks(annotated)
    warnings = []
    _check_slugs(blocks, warnings)
    _check_sections(annotated, warnings)
    _check_red_flag_states(annotated, warnings)
    _check_readiness_marker(annotated, blocks, warnings)
    _check_blocked_by(annotated, blocks, warnings)
    _check_orphaned_prose(annotated, warnings)
    return warnings


# --- Secret-shape scan ---
#
# Runs over the project's own prose docs (QUEUE.md, SPEC.md, LOG/) because those
# get committed, and a commit is permanent even if the text is deleted later.
#
# HIGH-CONFIDENCE SHAPES ONLY, and that narrowness is the design rather than a
# limitation. This scan's only value is that it is deterministic: it either
# matches a shape or it doesn't, so it never produces false confidence. The
# moment it started guessing at whether prose is sensitive it would become
# another judgment pass wearing a machine's authority.
#
# WHAT IT CANNOT DO, and this must never be sanded off. The thing that actually
# leaks from these docs is ordinary prose about a real person or a real case,
# and no pattern catches that. So this scan must never be described to a user as
# "your files are scrubbed" — a gate that over-claims is worse than no gate,
# because the user publishes more freely believing it worked. The same line the
# method holds on red flags: provide risk-addressing, never promise risk
# management. The prose half is a pre-write checklist Claude runs (see
# plugin-behaviour.md), and the real protection for a public repo is not
# publishing these artifacts at all.
#
# Advisory, like every check in this file. It reports; it never blocks or edits.
#
# Distinct from scripts/scrub_sweep.py, which is an on-demand, human-run,
# whole-repo sweep for OTHER PEOPLE's names. Different question, different
# trigger, and neither replaces the other.
SECRET_SHAPES = (
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "a private-key block"),
    (re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{16,}"), "an Anthropic API key"),
    (re.compile(r"\bsk-[A-Za-z0-9]{32,}"), "an API key"),
    (re.compile(r"\b(?:ghp|gho|ghu|ghs)_[A-Za-z0-9]{20,}"), "a GitHub token"),
    (re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}"), "a GitHub fine-grained token"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "an AWS access key id"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"), "a Slack token"),
    (re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"), "a Google API key"),
    (re.compile(r"\b[0-9a-fA-F]{32,}\b"), "a long hex string"),
    # No `/` in the class, and a digit and a capital are both required. Without
    # those three constraints this matched an ordinary filesystem path in a LOG
    # entry (`~/.claude/plugins/cache/flintcraft/sovereign-implementer`) — a run
    # of forty-odd letters and slashes reads as base64 to a regex. Real base64
    # secrets carry digits and mixed case; prose and paths usually don't.
    (
        re.compile(
            r"\b(?=[A-Za-z0-9+]*[0-9])(?=[A-Za-z0-9+]*[A-Z])"
            r"[A-Za-z0-9+]{40,}={0,2}\b"
        ),
        "a long base64-looking string",
    ),
    (
        re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b"),
        "an email address",
    ),
)

SCANNED_DOCS = ("QUEUE.md", "SPEC.md")


def _is_scannable_doc(filepath: str, cwd: str) -> bool:
    norm = _normalise(filepath)
    for doc in SCANNED_DOCS:
        if norm == _normalise(os.path.join(cwd, doc)):
            return True
    log_dir = _normalise(os.path.join(cwd, "LOG"))
    return norm.startswith(log_dir + os.sep)


def _scan_secrets(path: str) -> list:
    """Report high-confidence secret shapes in a project prose doc."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except (OSError, UnicodeDecodeError):
        return []

    found = []
    for n, line in enumerate(lines, 1):
        for pattern, label in SECRET_SHAPES:
            m = pattern.search(line)
            if m:
                snippet = m.group(0)
                if len(snippet) > 12:
                    snippet = snippet[:6] + "…" + snippet[-4:]
                found.append(
                    f"line {n}: {label} ({snippet}). This file gets committed, "
                    "and a commit keeps the text even if you delete it later."
                )
                break
    return found[:10]


def _emit(message: str) -> int:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": message,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def _lint_queue(queue_path: str) -> int:
    """Lint QUEUE.md at `queue_path` and emit any warnings as advisory context.

    Shared by both entry paths — an edit that landed on QUEUE.md, and any shell
    command in an adopted project. A missing or unreadable file is silently
    fine: this hook is advisory and never fails a tool call.
    """
    try:
        with open(queue_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return 0

    sections = []
    warnings = lint(content)
    if warnings:
        sections.append(
            "[Sovereign Implementer] QUEUE.md structure lint (advisory). "
            "These flag known violations only — novel structure is allowed "
            "and never flagged. Judge each one: fix what's genuinely wrong "
            "in a follow-up edit, leave what isn't.\n"
            + "\n".join(f"- {w}" for w in warnings)
        )

    secrets = _scan_secrets(queue_path)
    if secrets:
        sections.append(_secret_message("QUEUE.md", secrets))

    if not sections:
        return 0
    return _emit("\n\n".join(sections))


def _secret_message(name: str, findings: list) -> str:
    return (
        f"[Sovereign Implementer] Possible secret in {name} (advisory). "
        "These match known credential shapes only — deterministic, no "
        "judgement. Tell the user plainly what was found and where, and let "
        "them decide.\n"
        + "\n".join(f"- {f}" for f in findings)
        + "\n\nSay plainly, if it comes up, that this check finds credential "
        "SHAPES and nothing else. It cannot tell whether ordinary prose here "
        "names a real person or a real case, which is the thing that actually "
        "leaks from these files — so never tell the user their docs are "
        "scrubbed or safe to publish on the strength of it."
    )


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

    if tool_name not in ("Edit", "Write", "MultiEdit", "Bash", "PowerShell"):
        return 0

    if not cwd:
        return 0

    is_adopted = os.path.isfile(os.path.join(cwd, "SPEC.md"))

    # A shell command names no file, so there is nothing to compare against
    # QUEUE.md — the lint simply runs over QUEUE.md whatever the command was.
    #
    # WHY THIS BRANCH EXISTS. The lint used to fire after Edit/Write/MultiEdit
    # only, so a write that reached QUEUE.md through a shell bypassed it
    # entirely. That is not hypothetical: a scripted write corrupted QUEUE.md
    # on 2026-08-09 — duplicating a header fragment and leaving six built work
    # items in place — and nothing surfaced it. It was found several steps
    # later by an unrelated `git status`, and a close would otherwise have
    # committed it. Firing here catches the damage whatever caused it, which is
    # the point: the companion fix in pre_tool_use.py stops one route in, and
    # this stops the class.
    #
    # The cost is one file read and one lint per shell command, and the lint
    # stays ADVISORY exactly as it is after an edit — it reports, never blocks.
    if tool_name in ("Bash", "PowerShell"):
        if not is_adopted:
            return 0
        return _lint_queue(os.path.join(cwd, "QUEUE.md"))

    filepath = tool_input.get("file_path", "")
    if not filepath:
        return 0

    # Clear the editing-state signal for whatever file was just written —
    # every file, not only QUEUE.md, and before the QUEUE.md gate below.
    #
    # Gated on adoption to match pre_tool_use, which returns early with no
    # SPEC.md and so writes the OPENING marker only in adopted projects.
    # Without this the two hooks are asymmetric: an unadopted folder gets a
    # closing marker for a session that never opened one, so marker files
    # accumulate in projects that have nothing to do with this plugin — and
    # no .gitignore covers them, since /setup is what adds that entry and
    # those folders have never run it.
    if is_adopted:
        write_editing_marker(cwd, data.get("session_id", ""), filepath, False)

    if not is_adopted:
        return 0

    # Only the project-root QUEUE.md gets the structure lint. SPEC.md and LOG/
    # entries get the secret scan alone — they have no structure to lint, but
    # they are committed prose exactly like the queue.
    if _normalise(filepath) == _normalise(os.path.join(cwd, "QUEUE.md")):
        return _lint_queue(filepath)

    if _is_scannable_doc(filepath, cwd):
        secrets = _scan_secrets(filepath)
        if secrets:
            return _emit(
                _secret_message(os.path.basename(filepath), secrets)
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
