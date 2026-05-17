#!/usr/bin/env python3
"""
PreToolUse hook for the no-code-method plugin.

Runs three checks on every Edit / Write / MultiEdit tool call:

  (1) Locked source-of-truth doc enforcement (V19).
      Locked docs are: UX.md, plus any additional source-of-truth docs declared
      in the project's CLAUDE.md path block. BACKLOG.md and MANIFEST.md are
      explicitly writable. When a writing tool targets a locked doc, the hook
      denies and tells Claude to add a [FOLD-IN PENDING] block to the
      Fold-ins pending section of BACKLOG.md instead.

  (2) Serves-line check on BACKLOG.md build-batch additions (V22).
      When a writing tool targets BACKLOG.md and the proposed new content
      contains one or more `Serves UX.md: <entry name(s)>.` lines, the hook
      verifies that every named entry exists in UX.md's Functionalities
      section. Match is case-insensitive after whitespace-trim (V22 Q3
      decision). A miss denies with a redirect message naming the unmatched
      entries and listing the known UX.md entries so Claude can spot a typo
      or recognise it needs to fold-in first. The check is scoped to
      `Serves UX.md:` only — `Serves <ADDITIONAL>.md:` lines for additional
      source-of-truth docs are out of V22 scope and pass through.

  (3) Batch file-list boundary check (V25).
      When a top unticked build batch exists in BACKLOG.md, the hook blocks
      Edit/Write/MultiEdit on any file that isn't on the batch's `Files:` list.
      Exempts BACKLOG.md and MANIFEST.md (always writable per the editing-
      surfaces rule). Open mode when no batch is active — no enforcement, all
      edits allowed. Uses the shared `parse_backlog.py` parser (the same one
      called by the Stop hook and the `/build` slash-command, per V25 Q1).
      Deny message includes the current batch's Files: list and the
      prerequisite carve-out recovery path.

Mechanisms:

  - Locked-doc rule: NO-CODE-METHOD.md → Editing surfaces.
  - Fold-in block format: DOC-STRUCTURE.md → BACKLOG.md structure → Fold-ins
    pending.
  - Serves-line rule: NO-CODE-METHOD.md → How a new feature enters the
    project, and DOC-STRUCTURE.md → BACKLOG.md structure → Build batches.
  - V22 Q3 (case-insensitive exact match): BUILD-LOG.md → V22.

  The hook doesn't repeat the mechanisms — it names them and lets Claude
  consult those docs (or its own SessionStart-injected rules) for specifics.

The hook is deliberately lenient on edge cases — missing CLAUDE.md, an
unparseable path block, the target file sitting outside the project root,
UX.md missing or unparseable, no Functionalities section: in all such cases
it allows the tool call rather than blocking. A hook that blocks unexpectedly
is far more disruptive than one that occasionally fails to enforce. The
universal-behaviour rules surfaced via the SessionStart hook are the soft-net
for any case this hook can't deterministically catch.

Why three writing tools and not more: the method's locked-docs rule is about
deliberate written changes. NotebookEdit and other adjacent tools are not in
scope for the spine docs.

Output protocol: stdout receives a JSON object with hookSpecificOutput
containing hookEventName ("PreToolUse"), permissionDecision ("deny"), and
permissionDecisionReason (the message Claude reads). For allow-cases, the
hook writes nothing and exits 0 — the absence of a deny is an implicit allow.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# Tools whose calls this hook inspects. Anything outside this set is allowed
# without inspection.
WRITING_TOOLS = {"Edit", "Write", "MultiEdit"}

# Path-block keys treated as writable. Everything else in the path block —
# UX.md, plus any additional source-of-truth docs declared by the project —
# is locked.
WRITABLE_LOGICAL_NAMES = {"BACKLOG.md", "MANIFEST.md"}

# CLAUDE.md's path block is the first fenced JSON code block in the file.
# Match the contents between the opening ```json line and the closing ```.
PATH_BLOCK_PATTERN = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

# --- V22 Serves-line check patterns ---

# The Functionalities section heading in UX.md, bounded by the next ## heading
# (or end of file). Entries inside are ### headings.
FUNCTIONALITIES_SECTION_PATTERN = re.compile(r"^## Functionalities\s*$", re.MULTILINE)
NEXT_SECTION_PATTERN = re.compile(r"^## ", re.MULTILINE)

# Each Functionalities entry is a ### heading. The heading text (after ### )
# is the entry name. Nested-entry names use an arrow, e.g. `Settings → Day
# begins at`; the pattern captures whatever follows the heading marker.
ENTRY_HEADING_PATTERN = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)

# `Serves UX.md: <name(s)>.` line in a build batch. Names may be comma-
# separated (DOC-STRUCTURE.md → BACKLOG.md structure → Build batches: "listing
# the entries it implements"). The trailing period is part of the canonical
# format. The regex tolerates trailing whitespace.
SERVES_UX_PATTERN = re.compile(r"^Serves UX\.md:\s*(.+?)\.\s*$", re.MULTILINE)

# --- V25 batch file-list boundary check ---

# Path to the shared parser. pre_tool_use.py lives at plugin/hooks/; parser at
# plugin/scripts/parse_backlog.py. Duplicated from stop.py for V25; a shared
# helper module is the natural refactor target once a third parser-caller
# accumulates.
PARSER_PATH = Path(__file__).parent.parent / "scripts" / "parse_backlog.py"

# Timeout for the parser subprocess call. Insurance against a stuck process,
# not a tuning parameter — the parser runs in milliseconds on real input.
PARSER_TIMEOUT_SECONDS = 10


def emit_allow() -> int:
    """Allow the tool call by writing nothing. Returns exit code 0."""
    return 0


def emit_deny(reason: str) -> int:
    """Deny the tool call with the given reason text. Returns exit code 0
    (the deny itself communicates the outcome — non-zero exit is reserved
    for hook errors)."""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def parse_input():
    """Read the hook input JSON from stdin. Return dict on success, None on
    any parse failure."""
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def extract_path_block(claude_md_text: str):
    """Extract and parse the first fenced JSON code block from CLAUDE.md.

    Returns the parsed dict, or None if the block is missing or unparseable.
    """
    match = PATH_BLOCK_PATTERN.search(claude_md_text)
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def build_locked_map(project_root: Path) -> dict:
    """Read CLAUDE.md from project_root, parse the path block, and return a
    dict mapping resolved absolute path strings -> logical names for every
    LOCKED doc in the path block.

    Returns an empty dict if CLAUDE.md is missing, has no parseable path
    block, or contains no locked entries. The hook treats an empty locked
    map as "no enforcement applicable" and falls through to allow.
    """
    claude_path = project_root / "CLAUDE.md"
    try:
        text = claude_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    path_block = extract_path_block(text)
    if not path_block:
        return {}

    locked: dict = {}
    for logical_name, relative_path in path_block.items():
        if not isinstance(logical_name, str) or not isinstance(relative_path, str):
            continue
        if logical_name in WRITABLE_LOGICAL_NAMES:
            continue
        try:
            resolved = (project_root / relative_path).resolve()
        except OSError:
            continue
        locked[str(resolved)] = logical_name
    return locked


def make_reason(logical_name: str) -> str:
    """Build the deny-reason text Claude sees when a locked-doc edit is
    blocked. The reason tells Claude exactly where to place the proposed
    change — the *Fold-ins pending* section of BACKLOG.md — so the
    instruction is unambiguous in any project layout."""
    return (
        f"BLOCKED: {logical_name} is a locked source-of-truth doc. It is "
        f"read-only to Claude (the agent); only the user can edit it, by "
        f"hand during a planning session.\n\n"
        f"If you have identified a {logical_name} change that should "
        "happen, do not retry this edit. Instead, add a `[FOLD-IN PENDING]` "
        "block to the *Fold-ins pending* section of BACKLOG.md, with "
        f"destination `{logical_name}` and origin `mid-build edit attempt "
        "— <today's date>`. The user will fold the block into "
        f"{logical_name} by hand during their next planning session, or "
        f"drop it. Surface this addition plainly in your response to the "
        f"user. Canonical block format and section placement: see "
        f"DOC-STRUCTURE.md → BACKLOG.md structure → Fold-ins pending."
    )


# --- V22 Serves-line check helpers ---


def safe_read_text(path: Path):
    """Read a text file; return None on any failure. Used by the Serves-line
    check, which needs to peek at UX.md without raising on missing/locked
    files. Mirrors the helper in session_start.py."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def normalise_entry_name(name: str) -> str:
    """Lowercase, strip leading/trailing whitespace, collapse internal
    whitespace runs to a single space. Used for case-insensitive exact match
    after whitespace-trim (V22 Q3). Returns empty string for empty input.

    Internal-whitespace collapse handles the case where a name picks up
    accidental double-spaces during editing — '`Dark  mode`' should match
    '`Dark mode`'. This is a conservative widening of "exact match" that
    doesn't open the door to ambiguous near-matches."""
    if not isinstance(name, str):
        return ""
    name = name.strip().lower()
    name = re.sub(r"\s+", " ", name)
    return name


def resolve_path_block_entry(project_root: Path, logical_name: str):
    """Resolve a logical name (e.g. 'UX.md') to its absolute Path via
    CLAUDE.md's path block. Returns Path on success, None on any failure
    (missing CLAUDE.md, unparseable path block, name not in block).

    Kept separate from build_locked_map() because the Serves-line check
    needs the writable resolutions too."""
    claude_text = safe_read_text(project_root / "CLAUDE.md")
    if claude_text is None:
        return None
    path_block = extract_path_block(claude_text)
    if not path_block:
        return None
    rel = path_block.get(logical_name)
    if not isinstance(rel, str) or not rel:
        return None
    try:
        return (project_root / rel).resolve()
    except OSError:
        return None


def extract_functionality_entries(ux_text: str):
    """Return the set of entry names from UX.md's Functionalities section,
    normalised for case-insensitive matching (lowercased, whitespace-collapsed).

    Returns the empty set if the Functionalities heading isn't present, or
    if no ### entries exist under it. The check then falls through to allow
    (per the lenient principle — a UX.md with no Functionalities section
    isn't something this hook should adjudicate)."""
    section_match = FUNCTIONALITIES_SECTION_PATTERN.search(ux_text)
    if not section_match:
        return set()
    section_text = ux_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    entries = set()
    for match in ENTRY_HEADING_PATTERN.finditer(section_text):
        name = normalise_entry_name(match.group(1))
        if name:
            entries.add(name)
    return entries


def collect_new_content(tool_name: str, tool_input: dict) -> str:
    """Pull together the proposed new content from the tool input.

    Edit and Write expose the new content directly; MultiEdit exposes a list
    of edits each with their own new_string, which we concatenate. Returns
    an empty string on any structural mismatch — the caller treats that as
    'nothing to check' and falls through to allow.

    The hook checks every Serves UX.md line in the resulting text, which
    means existing (unchanged) Serves lines in a Write or MultiEdit are
    re-validated too. That's a feature, not a bug — UX.md entries can be
    renamed between edits, and a stale Serves line should fail-fast at the
    next touch rather than rot silently."""
    if tool_name == "Edit":
        new_string = tool_input.get("new_string")
        return new_string if isinstance(new_string, str) else ""
    if tool_name == "Write":
        content = tool_input.get("content")
        return content if isinstance(content, str) else ""
    if tool_name == "MultiEdit":
        edits = tool_input.get("edits")
        if not isinstance(edits, list):
            return ""
        chunks = []
        for edit in edits:
            if isinstance(edit, dict):
                new_string = edit.get("new_string")
                if isinstance(new_string, str):
                    chunks.append(new_string)
        return "\n".join(chunks)
    return ""


def extract_serves_ux_names(new_content: str):
    """Find every `Serves UX.md: ...` line in the proposed new content.
    Returns a list of entry-name strings in their original casing, flattened
    across all Serves lines (the caller doesn't care which line each name
    came from — only whether each name matches an existing entry).

    Comma-splits each Serves line so a multi-entry line like
    `Serves UX.md: Dark mode, Settings → Day begins at.` yields two names."""
    names = []
    for match in SERVES_UX_PATTERN.finditer(new_content):
        names_str = match.group(1)
        for raw in names_str.split(","):
            cleaned = raw.strip()
            if cleaned:
                names.append(cleaned)
    return names


def find_missing_serves_names(claimed: list, known_normalised: set):
    """Return the list of claimed names whose normalised form isn't in the
    known-entries set. Preserves the original casing of the missing names so
    the deny message can show what was actually written."""
    missing = []
    for name in claimed:
        if normalise_entry_name(name) not in known_normalised:
            missing.append(name)
    return missing


def make_serves_line_deny_reason(missing_names: list, known_normalised: set) -> str:
    """Build the deny-reason text when one or more Serves UX.md names don't
    match any UX.md entry. Includes the unmatched names and a one-line
    sample of known entries so Claude can spot a typo or recognise it needs
    to route through a planning batch first."""
    missing_str = ", ".join(f"`{n}`" for n in missing_names)
    if known_normalised:
        sample = sorted(known_normalised)[:30]
        known_str = ", ".join(f"`{n}`" for n in sample)
        if len(known_normalised) > 30:
            known_str += f", … ({len(known_normalised) - 30} more)"
        known_block = (
            f"\n\nCurrent `UX.md` Functionalities entries (case-insensitive "
            f"match, whitespace-trimmed): {known_str}."
        )
    else:
        known_block = (
            "\n\nNo Functionalities entries were detected in `UX.md` "
            "(section missing or empty)."
        )
    return (
        f"BLOCKED: a build batch's `Serves UX.md:` line names entries that "
        f"don't exist in `UX.md`: {missing_str}.\n\n"
        "Per NO-CODE-METHOD.md → *How a new feature enters the project*, a "
        "build batch must serve an entry in a source-of-truth doc. If this "
        "is a typo, fix the name. If the entry genuinely doesn't exist "
        "yet, the feature has skipped the planning-batch → fold-in step: "
        "route through a planning batch in BACKLOG.md, fold the answer "
        "into `UX.md` by hand during the next planning session, and "
        "propose the build batch after that."
        + known_block
    )


def check_serves_lines(
    project_root: Path,
    target_path: Path,
    tool_name: str,
    tool_input: dict,
):
    """If the edit targets BACKLOG.md, validate every `Serves UX.md:` line
    in the proposed new content against UX.md's Functionalities entries.

    Returns:
      - None if the check doesn't apply (target isn't BACKLOG.md; UX.md
        can't be resolved or read; no Serves UX.md lines in the new content;
        every name matches an entry).
      - A deny-reason string if one or more names miss.

    The lenient principle applies throughout — anywhere the check can't
    deterministically decide, it returns None and the caller allows."""
    backlog_path = resolve_path_block_entry(project_root, "BACKLOG.md")
    if backlog_path is None or str(target_path) != str(backlog_path):
        return None

    ux_path = resolve_path_block_entry(project_root, "UX.md")
    if ux_path is None:
        return None

    ux_text = safe_read_text(ux_path)
    if ux_text is None:
        return None

    new_content = collect_new_content(tool_name, tool_input)
    claimed_names = extract_serves_ux_names(new_content)
    if not claimed_names:
        return None

    known_normalised = extract_functionality_entries(ux_text)
    missing = find_missing_serves_names(claimed_names, known_normalised)
    if not missing:
        return None

    return make_serves_line_deny_reason(missing, known_normalised)


# --- V25 batch file-list boundary check helpers ---


def run_parser(backlog_path):
    """Invoke parse_backlog.py with backlog_path. Returns the parser's parsed
    JSON output (dict). Returns None on any failure (parser script missing,
    subprocess error, non-zero exit, empty stdout, invalid JSON). Duplicated
    from stop.py for V25; shared helper module is the natural refactor target
    once a third parser-caller accumulates."""
    if not PARSER_PATH.exists():
        return None
    try:
        result = subprocess.run(
            ["python", str(PARSER_PATH), str(backlog_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=PARSER_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    stdout = (result.stdout or "").strip()
    if not stdout:
        return None
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return None


def make_boundary_deny_reason(target_path, batch, files_entries):
    """Build the deny-reason text when a target file isn't on the current
    batch's Files: list. Includes the batch heading, the full Files: list
    with tick state (so Claude sees what IS allowed), and both carve-out
    recovery paths spelled out (prerequisite vs. out-of-scope refactor)."""
    heading = batch.get("batch_heading") or "(unknown)"

    lines = []
    for entry in files_entries:
        if not isinstance(entry, dict):
            continue
        path = entry.get("path", "?")
        ticked = entry.get("ticked", False)
        prereq = entry.get("prerequisite", False)
        marker = "[x]" if ticked else "[ ]"
        prereq_marker = " [Prerequisite, not in plan]" if prereq else ""
        lines.append(f"  - {marker} `{path}`{prereq_marker}")
    file_list_display = "\n".join(lines) if lines else "  (no files declared)"

    return (
        f"BLOCKED: `{target_path}` is not on the current build batch's "
        "`Files:` list and cannot be edited from inside the batch.\n\n"
        f"Current batch: **{heading}**\n\n"
        "`Files:` list (authority for Edit/Write/MultiEdit enforcement):\n"
        f"{file_list_display}\n\n"
        "If this file is a genuine prerequisite — implementation just "
        "revealed it as needed and the batch can't complete or be tested "
        "cleanly without it — halt and surface in chat with a one-line "
        "justification (per NO-CODE-METHOD.md → Prohibited of Claude → "
        "Two exceptions → Prerequisite carve-out). On the user's okay, "
        "append the file to this batch's `Files:` list in BACKLOG.md "
        "with a trailing `[Prerequisite, not in plan]` label, then retry "
        "the edit. The hook re-parses BACKLOG.md at edit time, so the "
        "new entry takes effect immediately.\n\n"
        "If this file is NOT a prerequisite and you were trying to "
        "refactor or 'while you're in there' outside the agreed batch "
        "plan, stop. Finish the current batch, then route the change "
        "through planning per NO-CODE-METHOD.md → How a new feature "
        "enters the project."
    )


def check_batch_file_list(project_root, target_path):
    """V25: enforce the batch file-list boundary on Edit/Write/MultiEdit.

    Returns a deny-reason string if target_path isn't on the current top
    unticked batch's Files: list. Returns None to allow (or to fall
    through silently in lenient cases).

    Behaviour:
      - Exempt: BACKLOG.md and MANIFEST.md (always writable per editing-
        surfaces).
      - Open mode: no active batch (parser returns {}) → allow. The check
        only enforces when there IS a batch to enforce against.
      - Otherwise: target's resolved path must be in the batch's Files:
        set (case-sensitive comparison, matching the locked-doc check)."""
    backlog_path = resolve_path_block_entry(project_root, "BACKLOG.md")
    if backlog_path is None or not backlog_path.exists():
        return None  # lenient: no BACKLOG.md to enforce against

    # Exempt BACKLOG.md (Claude needs to tick files, append [Prerequisite,
    # not in plan] entries, etc.) and MANIFEST.md (always writable).
    if str(target_path) == str(backlog_path):
        return None
    manifest_path = resolve_path_block_entry(project_root, "MANIFEST.md")
    if manifest_path is not None and str(target_path) == str(manifest_path):
        return None

    batch = run_parser(backlog_path)
    if not isinstance(batch, dict) or not batch:
        return None  # open mode: no active batch

    files_entries = batch.get("files") or []
    if not isinstance(files_entries, list) or not files_entries:
        return None  # lenient: malformed batch, nothing to enforce

    allowed_paths = set()
    for entry in files_entries:
        if not isinstance(entry, dict):
            continue
        rel = entry.get("path")
        if not isinstance(rel, str) or not rel:
            continue
        try:
            resolved = (project_root / rel).resolve()
        except OSError:
            continue
        allowed_paths.add(str(resolved))

    if not allowed_paths:
        return None  # lenient: every entry was malformed

    if str(target_path) in allowed_paths:
        return None  # on the list — allow

    return make_boundary_deny_reason(target_path, batch, files_entries)


def main() -> int:
    data = parse_input()
    if not isinstance(data, dict):
        return emit_allow()

    tool_name = data.get("tool_name")
    if tool_name not in WRITING_TOOLS:
        return emit_allow()

    tool_input = data.get("tool_input") or {}
    file_path_str = tool_input.get("file_path")
    if not isinstance(file_path_str, str) or not file_path_str:
        return emit_allow()

    cwd_str = data.get("cwd")
    if not isinstance(cwd_str, str) or not cwd_str:
        return emit_allow()

    try:
        project_root = Path(cwd_str).resolve()
    except OSError:
        return emit_allow()

    target_path = Path(file_path_str)
    try:
        if target_path.is_absolute():
            target_path = target_path.resolve()
        else:
            target_path = (project_root / target_path).resolve()
    except OSError:
        return emit_allow()

    locked_map = build_locked_map(project_root)
    logical_name = locked_map.get(str(target_path)) if locked_map else None
    if logical_name:
        return emit_deny(make_reason(logical_name))

    # V22: Serves-line check fires on BACKLOG.md edits whose new content
    # contains one or more `Serves UX.md: <entry>.` lines. Anywhere the
    # check can't deterministically decide, it returns None and we allow.
    serves_deny_reason = check_serves_lines(
        project_root, target_path, tool_name, tool_input
    )
    if serves_deny_reason:
        return emit_deny(serves_deny_reason)

    # V25: batch file-list boundary check. When a top unticked build batch
    # exists in BACKLOG.md, deny any edit whose target isn't on the batch's
    # `Files:` list (with BACKLOG.md and MANIFEST.md exempt; open mode when
    # no batch is active).
    boundary_deny_reason = check_batch_file_list(project_root, target_path)
    if boundary_deny_reason:
        return emit_deny(boundary_deny_reason)

    return emit_allow()


if __name__ == "__main__":
    sys.exit(main())
