#!/usr/bin/env python3
"""
PostToolUse hook — advisory lint of QUEUE.md structure after edits.

Fires after Edit/Write/MultiEdit lands on the project's QUEUE.md. Reads
the file from disk and flags known format violations:

  1. A batch title line with no **[slug]** marker.
  2. A parked item with no Blocked by:/Parked: header.
  3. The Captures processed/unprocessed divider (a bare ---) deleted.
  4. A Depends on:/Blocks:/Blocked by: header naming a slug defined
     nowhere in the file.
  5. A subheading inside a batch that isn't Build/Spec-edit/Test/Audit
     — catches typos; ALLOWED_SUBHEADINGS must grow when new batch
     types ship.
  6. Batch prose naming a slug that is still defined in the file but
     not carried by the batch's own headers — "dependency or
     citation?", advisory precisely because evidence citations are
     legitimate. References to slugs absent from the file are skipped:
     an absent slug is shipped work, and a reference to shipped work
     can only be a citation (a dry run against the real queue showed
     those make up the bulk of prose references — flagging them buried
     the real signals under ~2.5KB of noise per edit).

Deny-list by design: only known violations are flagged; unknown or
novel structure passes in silence, so the format can evolve (new
sections, new batch types) without fighting the linter. All findings
are advisory — fed back to Claude as context next to the tool result,
never blocking: the edit has already landed, and judging whether a
flag is real stays with the session.
"""

import json
import os
import re
import sys


# A batch title line is entirely bold: one or more **...** segments and
# nothing else. Rationale prose is never a full-bold line.
FULL_BOLD_LINE = re.compile(r"^(?:\*\*[^*]+\*\*)(?:\s+\*\*[^*]+\*\*)*$")

# A slug definition: the bold **[kebab-case]** marker on a title line or
# parked item. Slugs are lowercase kebab, two characters minimum.
SLUG_MARKER = re.compile(r"\*\*\[([a-z0-9][a-z0-9-]+)\]\*\*")

# A slug reference anywhere in text. The (?!\() guard skips markdown
# links; the lowercase-only class skips tokens like [HASH] or [PROMPT];
# the two-character minimum skips checkbox ticks like [x].
SLUG_REF = re.compile(r"\[([a-z0-9][a-z0-9-]+)\](?!\()")

# Dependency headers, matched on the stripped line.
DEP_HEADER = re.compile(r"^(Depends on|Blocks|Blocked by):")

# A batch subheading: a single capitalised word (hyphens allowed, e.g.
# "Spec-edit") and a colon, alone on the line. Multi-word lines with
# colons (e.g. "Depends on: x") and lines with text after the colon
# never match.
SUBHEADING = re.compile(r"^([A-Z][A-Za-z-]*):$")

# Marker lines between batches ("--- Push required before continuing ---",
# plan markers). They separate batch blocks and are never violations.
MARKER_LINE = re.compile(r"^---.+---$")

ALLOWED_SUBHEADINGS = {"Build", "Spec-edit", "Test", "Audit"}


def _normalise(path: str) -> str:
    return os.path.normcase(os.path.normpath(path))


def _annotate(content: str):
    """Yield (index, stripped line, h2, h3, is_heading) per line."""
    h2 = h3 = None
    out = []
    for i, raw in enumerate(content.splitlines()):
        stripped = raw.strip()
        if raw.startswith("### "):
            h3 = raw[4:].strip()
            out.append((i, stripped, h2, h3, True))
        elif raw.startswith("## "):
            h2, h3 = raw[3:].strip(), None
            out.append((i, stripped, h2, h3, True))
        else:
            out.append((i, stripped, h2, h3, False))
    return out


def _check_batch_slugs(annotated, warnings):
    """Check 1: every batch title line carries a **[slug]** marker."""
    for i, line, h2, _h3, is_heading in annotated:
        if is_heading or h2 != "Batches" or not line:
            continue
        if FULL_BOLD_LINE.match(line) and not SLUG_MARKER.search(line):
            warnings.append(
                f"line {i + 1}: batch title {line!r} has no **[slug]** "
                "marker — every batch needs one so other items can "
                "reference it across reorders."
            )


def _check_parked_headers(annotated, warnings):
    """Check 2: every parked item has a Blocked by:/Parked: header."""
    blocks = []
    current = None
    for i, line, _h2, h3, is_heading in annotated:
        if h3 != "Parked" or is_heading:
            if current:
                blocks.append(current)
                current = None
            continue
        starts_item = line.startswith("- ") or bool(
            line and FULL_BOLD_LINE.match(line)
        )
        if starts_item:
            if current:
                blocks.append(current)
            current = (i, [line])
        elif current:
            current[1].append(line)
    if current:
        blocks.append(current)

    for start, lines in blocks:
        if any(l.startswith(("Blocked by:", "Parked:")) for l in lines):
            continue
        snippet = lines[0][:60]
        warnings.append(
            f"line {start + 1}: parked item {snippet!r} has no "
            "Blocked by:/Parked: header — nothing leaves active flow "
            "without a stated reason in one of those two slots."
        )


def _check_captures_divider(annotated, warnings):
    """Check 3: the Captures section keeps its bare --- divider."""
    has_captures = any(h2 == "Captures" for _i, _l, h2, _h3, _ih in annotated)
    if not has_captures:
        return
    for _i, line, h2, h3, is_heading in annotated:
        if h2 == "Captures" and h3 is None and not is_heading and line == "---":
            return
    warnings.append(
        "the Captures processed/unprocessed divider (a line holding just "
        "---) is missing — restore it: processed captures sit above it, "
        "raw captures collect below."
    )


def _check_dangling_refs(annotated, defined_slugs, warnings):
    """Check 4: dependency headers only name slugs defined in the file."""
    for i, line, _h2, _h3, is_heading in annotated:
        if is_heading:
            continue
        match = DEP_HEADER.match(line)
        if not match:
            continue
        for slug in SLUG_REF.findall(line):
            if slug not in defined_slugs:
                warnings.append(
                    f"line {i + 1}: {match.group(1)}: names [{slug}], but "
                    "nothing in this file carries that slug — shipped "
                    "already, renamed, or a typo? A satisfied dependency "
                    "is stale and can come off the header."
                )


def _check_subheadings(annotated, warnings):
    """Check 5: batch subheadings are Build:/Test:/Audit: only."""
    for i, line, h2, _h3, is_heading in annotated:
        if is_heading or h2 != "Batches":
            continue
        match = SUBHEADING.match(line)
        if match and match.group(1) not in ALLOWED_SUBHEADINGS:
            warnings.append(
                f"line {i + 1}: subheading '{line}' isn't one of "
                "Build:/Spec-edit:/Test:/Audit: — a typo, or a new batch type this "
                "lint doesn't know yet? (New types must be added to "
                "ALLOWED_SUBHEADINGS in post_tool_use.py.)"
            )


def _check_prose_refs(annotated, defined_slugs, warnings):
    """Check 6: batch prose naming defined slugs its headers don't carry.

    Only references to slugs still defined in the file are flagged: a
    pending item can be a missed dependency; an absent slug is shipped
    work, and a reference to shipped work can only be a citation.
    """
    blocks = []
    current = None
    for _i, line, h2, _h3, is_heading in annotated:
        if h2 != "Batches" or is_heading:
            if current:
                blocks.append(current)
                current = None
            continue
        if MARKER_LINE.match(line):
            if current:
                blocks.append(current)
                current = None
            continue
        if line and FULL_BOLD_LINE.match(line):
            if current:
                blocks.append(current)
            current = {"title": line, "lines": []}
        elif current is not None:
            current["lines"].append(line)
    if current:
        blocks.append(current)

    findings = []
    for block in blocks:
        own = set(SLUG_MARKER.findall(block["title"]))
        header_slugs = set()
        prose_slugs = []
        for line in block["lines"]:
            refs = SLUG_REF.findall(line)
            if DEP_HEADER.match(line):
                header_slugs.update(refs)
            else:
                prose_slugs.extend(refs)
        unheadered = sorted(
            {
                s
                for s in prose_slugs
                if s in defined_slugs and s not in header_slugs and s not in own
            }
        )
        if unheadered:
            label = sorted(own)[0] if own else block["title"][:40]
            findings.append(
                f"[{label}] names " + ", ".join(f"[{s}]" for s in unheadered)
            )
    if findings:
        warnings.append(
            "prose slug references with no Depends on:/Blocks: header "
            "carrying them — real dependency, or just a citation? "
            "Citations are fine and need no change: "
            + "; ".join(findings)
        )


def lint(content: str) -> list[str]:
    annotated = _annotate(content)
    defined_slugs = set(SLUG_MARKER.findall(content))
    warnings = []
    _check_batch_slugs(annotated, warnings)
    _check_parked_headers(annotated, warnings)
    _check_captures_divider(annotated, warnings)
    _check_dangling_refs(annotated, defined_slugs, warnings)
    _check_subheadings(annotated, warnings)
    _check_prose_refs(annotated, defined_slugs, warnings)
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
