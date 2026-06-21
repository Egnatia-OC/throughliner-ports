#!/usr/bin/env python3
"""
PostToolUse hook — advisory lint of QUEUE.md structure after edits.

Fires after Edit/Write/MultiEdit lands on the project's QUEUE.md. Reads
the file from disk and flags known format violations:

  1. A batch title line with no **[slug]** marker.
  2. A parked item with no Blocked by:/Parked: header.
  3. The Captures processed/unprocessed divider (a bare ---) deleted.
  4. A Depends on:/Blocks:/Blocked by: header naming a slug that is
     unresolved everywhere — not defined in the file, not staged in
     Deferred tests, and not shipped per LOG/index.md. A slug recorded
     as shipped is a satisfied citation, not a dangling dependency, so
     it isn't flagged (which also stops it re-flagging on every edit).
  5. A subheading inside a batch that isn't Build/Spec-edit/Test/
     Audit/Freeform — catches typos; ALLOWED_SUBHEADINGS must grow
     when new batch types ship.
  6. Batch prose naming a slug that is still defined in the file but
     not carried by the batch's own headers — "dependency or
     citation?", advisory precisely because evidence citations are
     legitimate. References to slugs absent from the file are skipped:
     an absent slug is shipped work, and a reference to shipped work
     can only be a citation (a dry run against the real queue showed
     those make up the bulk of prose references — flagging them buried
     the real signals under ~2.5KB of noise per edit).
  7. A batch whose Depends on: names another active batch positioned
     below it in Batches — an out-of-order dependency /next would trip
     on. Deps that resolve to a Deferred-tests slug (staged) or to
     nothing (shipped) are not ordering errors and aren't flagged.
  8. A batch carrying both a Build and a Spec-edit subheading — a spec
     change gets its own batch; the scope-lock can't catch a folded one
     because listing SPEC.md satisfies it.

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

ALLOWED_SUBHEADINGS = {"Build", "Spec-edit", "Test", "Audit", "Freeform"}


def _normalise(path: str) -> str:
    return os.path.normcase(os.path.normpath(path))


def _annotate(content: str):
    """Yield (index, stripped line, h2, h3, is_heading, indent) per line.

    `indent` is the raw line's leading-whitespace width — used to tell a
    nested sub-bullet (a continuation of an item) from a top-level entry.
    """
    h2 = h3 = None
    out = []
    for i, raw in enumerate(content.splitlines()):
        stripped = raw.strip()
        indent = len(raw) - len(raw.lstrip())
        if raw.startswith("### "):
            h3 = raw[4:].strip()
            out.append((i, stripped, h2, h3, True, indent))
        elif raw.startswith("## "):
            h2, h3 = raw[3:].strip(), None
            out.append((i, stripped, h2, h3, True, indent))
        else:
            out.append((i, stripped, h2, h3, False, indent))
    return out


def _check_batch_slugs(annotated, warnings):
    """Check 1: every batch title line carries a **[slug]** marker."""
    for i, line, h2, _h3, is_heading, _indent in annotated:
        if is_heading or h2 != "Batches" or not line:
            continue
        if FULL_BOLD_LINE.match(line) and not SLUG_MARKER.search(line):
            warnings.append(
                f"line {i + 1}: batch title {line!r} has no **[slug]** "
                "marker — every batch needs one so other items can "
                "reference it across reorders."
            )


def _check_parked_headers(annotated, warnings):
    """Check 2: every parked item has a Blocked by:/Parked: header.

    A line indented under an item (indent > 0) is a continuation of that
    item — a nested sub-bullet, not a standalone parked entry — so only a
    top-level (indent 0) bullet or full-bold line starts a new item. A
    sub-bullet under a parked item used to be read as its own loose entry
    and falsely flagged; requiring indent 0 fixes that.
    """
    blocks = []
    current = None
    for i, line, _h2, h3, is_heading, indent in annotated:
        if h3 != "Parked" or is_heading:
            if current:
                blocks.append(current)
                current = None
            continue
        starts_item = indent == 0 and (
            line.startswith("- ") or bool(line and FULL_BOLD_LINE.match(line))
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
    has_captures = any(h2 == "Captures" for _i, _l, h2, _h3, _ih, _ind in annotated)
    if not has_captures:
        return
    for _i, line, h2, h3, is_heading, _ind in annotated:
        if h2 == "Captures" and h3 is None and not is_heading and line == "---":
            return
    warnings.append(
        "the Captures processed/unprocessed divider (a line holding just "
        "---) is missing — restore it: processed captures sit above it, "
        "raw captures collect below."
    )


def _deferred_slugs(annotated):
    """Slugs referenced in the Deferred tests section.

    A slug staged in Deferred tests is a valid pending trigger, so a
    Blocked by: (or other dependency header) pointing at it is not
    dangling. Deferred-test lines write the slug as a plain [slug]
    reference, not a bold **[slug]** marker, so SLUG_MARKER — and thus
    defined_slugs — never picks them up; this fills that gap for the
    dangling-ref check only. A slug found in neither Batches nor here is
    still flagged: a fully-shipped blocker is a real unpark signal.
    """
    slugs = set()
    for _i, line, h2, _h3, is_heading, _indent in annotated:
        if is_heading or h2 != "Deferred tests":
            continue
        slugs.update(SLUG_REF.findall(line))
    return slugs


def _shipped_slugs(cwd):
    """Slugs recorded as shipped in LOG/index.md.

    A `Blocked by:` (or other dependency header) prose tail often cites a
    prerequisite that has already shipped — work that is done and whose batch
    is long gone from QUEUE.md, so it appears in neither Batches nor Deferred
    tests. That citation is satisfied, not dangling, but the dangling-ref
    check used to flag it anyway (and re-flag it on every QUEUE.md edit,
    forever), because it only resolved against the file in front of it.
    LOG/index.md is the authoritative record of shipped work — one line per
    closed session, each naming its batch slug — so a slug found there is
    resolved and must not flag.

    Read broadly: every [slug] token in the index counts. Over-resolving only
    quiets flags, which is the fail-safe direction here — a satisfied citation
    must never read as dangling. (Under-reading would let it re-flag forever,
    the exact noise this fixes.) Returns an empty set when the index is
    missing or unreadable, so a project without LOG/ simply gains nothing and
    loses nothing.
    """
    index_path = os.path.join(cwd, "LOG", "index.md")
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError):
        return set()
    return set(SLUG_REF.findall(text))


def _check_dangling_refs(annotated, resolved_slugs, warnings):
    """Check 4: dependency headers only name unresolved slugs.

    A slug is resolved — and so never flagged — when it is defined in the
    file (an active batch or parked item), staged in Deferred tests, or
    recorded as shipped in LOG/index.md. Only a slug resolved by none of
    those is a genuine dangling reference worth surfacing.
    """
    for i, line, _h2, _h3, is_heading, _indent in annotated:
        if is_heading:
            continue
        match = DEP_HEADER.match(line)
        if not match:
            continue
        for slug in SLUG_REF.findall(line):
            if slug not in resolved_slugs:
                warnings.append(
                    f"line {i + 1}: {match.group(1)}: names [{slug}], but "
                    "nothing carries that slug — not in this file, not staged "
                    "in Deferred tests, and not shipped per LOG/index.md. "
                    "Renamed, or a typo? A satisfied dependency is stale and "
                    "can come off the header."
                )


def _check_subheadings(annotated, warnings):
    """Check 5: batch subheadings are Build:/Test:/Audit: only."""
    for i, line, h2, _h3, is_heading, _indent in annotated:
        if is_heading or h2 != "Batches":
            continue
        match = SUBHEADING.match(line)
        if match and match.group(1) not in ALLOWED_SUBHEADINGS:
            warnings.append(
                f"line {i + 1}: subheading '{line}' isn't one of "
                "Build:/Spec-edit:/Test:/Audit:/Freeform: — a typo, or a new batch "
                "type this lint doesn't know yet? (New types must be added to "
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
    for _i, line, h2, _h3, is_heading, _indent in annotated:
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


def _check_dep_ordering(annotated, warnings):
    """Check 7: a batch's Depends on: names an active batch ordered below it.

    Only active batches in Batches count. A dependency that resolves to a
    Deferred-tests slug (staged) or to nothing (shipped) is not an ordering
    error — it simply isn't an active batch, so it's never in the position
    map and never flagged here (the dangling-ref check owns the
    resolves-to-nothing case). A parked target is likewise skipped: depending
    on a parked item is a block, not an ordering mistake. Advisory only.
    """
    batches = []
    current = None
    for i, line, h2, h3, is_heading, indent in annotated:
        if h2 != "Batches" or h3 == "Parked" or is_heading:
            if current:
                batches.append(current)
                current = None
            continue
        if MARKER_LINE.match(line):
            if current:
                batches.append(current)
                current = None
            continue
        if indent == 0 and line and FULL_BOLD_LINE.match(line):
            if current:
                batches.append(current)
            current = {"idx": i, "own": set(SLUG_MARKER.findall(line)), "deps": set()}
        elif current is not None:
            mh = DEP_HEADER.match(line)
            if mh and mh.group(1) == "Depends on":
                current["deps"].update(SLUG_REF.findall(line))
    if current:
        batches.append(current)

    position = {}
    for order_i, b in enumerate(batches):
        for s in b["own"]:
            position[s] = order_i

    for order_i, b in enumerate(batches):
        for dep in sorted(b["deps"]):
            if dep in b["own"]:
                continue
            if dep in position and position[dep] > order_i:
                label = sorted(b["own"])[0] if b["own"] else f"line {b['idx'] + 1}"
                warnings.append(
                    f"line {b['idx'] + 1}: [{label}] Depends on: [{dep}], but "
                    f"[{dep}] is ordered below it in Batches — /next would reach "
                    f"[{label}] first. Move [{dep}] above it, or reorder."
                )


def _check_spec_edit_build_mix(annotated, warnings):
    """Check 8: a batch carries both a Build and a Spec-edit subheading.

    A spec edit gets its own batch, separate from a feature build. The
    scope-lock can't catch a folded one (listing SPEC.md satisfies it), so
    this advisory flag backstops the authoring rule in plan.md. Advisory
    only — like the rest of the lint, it flags and never blocks.
    """
    batches = []
    current = None
    for i, line, h2, h3, is_heading, indent in annotated:
        if h2 != "Batches" or h3 == "Parked" or is_heading:
            if current:
                batches.append(current)
                current = None
            continue
        if MARKER_LINE.match(line):
            if current:
                batches.append(current)
                current = None
            continue
        if indent == 0 and line and FULL_BOLD_LINE.match(line):
            if current:
                batches.append(current)
            current = {"idx": i, "title": line, "subs": set()}
        elif current is not None:
            ms = SUBHEADING.match(line)
            if ms:
                current["subs"].add(ms.group(1))
    if current:
        batches.append(current)

    for b in batches:
        if "Build" in b["subs"] and "Spec-edit" in b["subs"]:
            own = sorted(SLUG_MARKER.findall(b["title"]))
            label = own[0] if own else b["title"][:40]
            warnings.append(
                f"line {b['idx'] + 1}: [{label}] carries both a Build and a "
                "Spec-edit subheading — a spec change gets its own batch, "
                "separate from a feature build. Split them."
            )


def lint(content: str, shipped_slugs=frozenset()) -> list[str]:
    annotated = _annotate(content)
    defined_slugs = set(SLUG_MARKER.findall(content))
    deferred_slugs = _deferred_slugs(annotated)
    warnings = []
    _check_batch_slugs(annotated, warnings)
    _check_parked_headers(annotated, warnings)
    _check_captures_divider(annotated, warnings)
    # Dangling-ref check resolves against Batches slugs PLUS Deferred-tests
    # slugs (a staged test is a valid pending trigger) PLUS shipped slugs from
    # LOG/index.md (a satisfied citation of completed work). The prose-ref
    # check deliberately stays on defined_slugs only — adding deferred or
    # shipped slugs there would start flagging citations the absent-slug skip
    # currently quiets.
    _check_dangling_refs(
        annotated, defined_slugs | deferred_slugs | shipped_slugs, warnings
    )
    _check_subheadings(annotated, warnings)
    _check_prose_refs(annotated, defined_slugs, warnings)
    _check_dep_ordering(annotated, warnings)
    _check_spec_edit_build_mix(annotated, warnings)
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

    warnings = lint(content, shipped_slugs=_shipped_slugs(cwd))
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
