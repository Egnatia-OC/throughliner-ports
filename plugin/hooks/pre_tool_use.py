#!/usr/bin/env python3
"""
PreToolUse hook for the no-code-method plugin.

Runs a V29 adoption gate first (across Edit / Write / MultiEdit AND Task),
then three checks on Edit / Write / MultiEdit and one check on Task:

  (1) Locked source-of-truth doc enforcement (V19) — Edit/Write/MultiEdit.
      Locked docs are: UX.md, plus any additional source-of-truth docs declared
      in the project's CLAUDE.md path block. BACKLOG.md, MANIFEST.md, and
      TEST-LOG.md are explicitly writable — the planning, glossary, and
      test-record surfaces Claude edits during the build cycle. (TEST-LOG.md
      is a spine doc since V26, not "additional"; V28 closed the gap by
      adding it to WRITABLE_LOGICAL_NAMES so after-build's row-open writes
      and planning's per-row status updates can land.) When a writing tool
      targets a locked doc, the hook denies and tells Claude to add a
      [FOLD-IN PENDING] block to the Fold-ins pending section of BACKLOG.md
      instead.

  (2) Serves-line check on BACKLOG.md build-batch additions (V22) — Edit/Write/
      MultiEdit. When a writing tool targets BACKLOG.md and the proposed new
      content contains one or more `Serves UX.md: <entry name(s)>.` lines, the
      hook verifies that every named entry exists in UX.md's Functionalities
      section. Match is case-insensitive after whitespace-trim (V22 Q3
      decision). A miss denies with a redirect message naming the unmatched
      entries and listing the known UX.md entries so Claude can spot a typo
      or recognise it needs to fold-in first. The check is scoped to
      `Serves UX.md:` only — `Serves <ADDITIONAL>.md:` lines for additional
      source-of-truth docs are out of V22 scope and pass through.

  (3) Batch file-list boundary check (V25) — Edit/Write/MultiEdit.
      When a top unticked build batch exists in BACKLOG.md, the hook blocks
      Edit/Write/MultiEdit on any file that isn't on the batch's `Files:` list.
      Exempts BACKLOG.md and MANIFEST.md (always writable per the editing-
      surfaces rule). Open mode when no batch is active — no enforcement, all
      edits allowed. Uses the shared `parse_backlog.py` parser (the same one
      called by the Stop hook and the `/build` slash-command, per V25 Q1).
      Deny message includes the current batch's Files: list and the
      prerequisite carve-out recovery path.

  (5) V29 adoption gate — Edit / Write / MultiEdit AND Task. Fires *before*
      checks (1)–(4) so the gate isn't bypassed when the folder is
      unadopted. Denies Edit/Write/MultiEdit on non-scaffold-path files
      and Task invocations of method subagents (planning, before-build,
      batch-executor, after-build) when the folder lacks a method footer
      in CLAUDE.md AND has substantial work AND no `.no-code-method-skip`
      opt-out marker. Allows Task → no-code-method:adopt always (that's
      the resolution mechanism). Allows Edit/Write/MultiEdit on scaffold
      paths (UX.md, BACKLOG.md, MANIFEST.md, TEST-LOG.md, CLAUDE.md, the
      opt-out marker file) so /adopt's scaffolding works. The full V29
      architecture context (why this gate exists in PreToolUse and not at
      SessionStart) is in NO-CODE-METHOD.md → *Detect unadopted folder*.

  (4) Test-confirmation gate (V27) — Task tool with subagent_type
      `no-code-method:batch-executor`. When TEST-LOG.md has rows with
      `Confirmed Explicitly: No` left over from the previous build batch's
      test session, the hook denies the batch-executor invocation. The gate
      identifies the previous session from BUILD-LOG.md when the project
      keeps one; otherwise it falls back to strict mode (any unconfirmed row
      blocks). Strict fallback also fires when BUILD-LOG.md is present but
      unparseable — the deny message names the parse failure so the user can
      fix the right thing. Spec: NO-CODE-METHOD.md → Method contract →
      Prohibited of Claude → Test-confirmation gate.

Mechanisms:

  - Locked-doc rule: NO-CODE-METHOD.md → Editing surfaces.
  - Fold-in block format: DOC-STRUCTURE.md → BACKLOG.md structure → Fold-ins
    pending.
  - Serves-line rule: NO-CODE-METHOD.md → How a new feature enters the
    project, and DOC-STRUCTURE.md → BACKLOG.md structure → Build batches.
  - V22 Q3 (case-insensitive exact match): BUILD-LOG.md → V22.
  - Test-confirmation gate: NO-CODE-METHOD.md → Method contract → Required
    of Claude → Never infer completion (Rule 1) and Prohibited of Claude →
    Test-confirmation gate (Rule 3); TEST-LOG.md column shape in
    DOC-STRUCTURE.md → TEST-LOG.md structure.

  The hook doesn't repeat the mechanisms — it names them and lets Claude
  consult those docs (or its own SessionStart-injected rules) for specifics.

The hook is deliberately lenient on edge cases — missing CLAUDE.md, an
unparseable path block, the target file sitting outside the project root,
UX.md missing or unparseable, no Functionalities section, TEST-LOG.md
missing or empty: in all such cases it allows the tool call rather than
blocking. A hook that blocks unexpectedly is far more disruptive than one
that occasionally fails to enforce. The universal-behaviour rules surfaced
via the SessionStart hook are the soft-net for any case this hook can't
deterministically catch. The one exception is the test-confirmation gate's
strict fallback — when TEST-LOG.md has unconfirmed rows AND BUILD-LOG.md
can't be used for session-narrowing, the gate denies; safe-by-default per
V26 Q3 and V27 Q4.

Why three writing tools and not more: the method's locked-docs rule is about
deliberate written changes. NotebookEdit and other adjacent tools are not in
scope for the spine docs. The Task matcher (V27) is narrower still — it
only inspects calls whose `subagent_type` is `no-code-method:batch-executor`.

Output protocol: stdout receives a JSON object with hookSpecificOutput
containing hookEventName ("PreToolUse"), permissionDecision ("deny"), and
permissionDecisionReason (the message Claude reads). For allow-cases, the
hook writes nothing and exits 0 — the absence of a deny is an implicit allow.
"""

import json
import re
import sys
from pathlib import Path

# Make the sibling plugin/scripts/ directory importable so we can pull in
# the shared project-state helpers. pre_tool_use.py lives at plugin/hooks/;
# project_state.py is at plugin/scripts/. The hook is invoked directly
# (`python plugin/hooks/pre_tool_use.py`), so we add scripts/ to sys.path
# explicitly rather than relying on package imports. (V28 extraction.)
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from project_state import (  # noqa: E402 — must follow sys.path insert
    safe_read_text,
    extract_path_block,
    resolve_path_block_entry,
    run_parser,
    get_unconfirmed_previous_session_rows,
    is_unadopted_with_work,
    OPT_OUT_MARKER_NAME,
)

# Writing tools whose calls this hook inspects via checks (1)-(3). Anything
# outside this set + the Task tool is allowed without inspection.
WRITING_TOOLS = {"Edit", "Write", "MultiEdit"}

# Task invocations targeting this subagent_type are inspected by check (4)
# (V27 test-confirmation gate). Other Task invocations pass through.
BATCH_EXECUTOR_SUBAGENT_TYPE = "no-code-method:batch-executor"

# V29: Task invocations targeting /adopt are always allowed even when the
# folder is unadopted — that's the command users run to RESOLVE the
# unadopted state, so blocking it would be a deadlock.
ADOPT_SUBAGENT_TYPE = "no-code-method:adopt"

# V29: method subagent prefix. Other Task calls (e.g. general-purpose
# agents the user invokes for their own purposes) fall through the V29
# gate so the unadopted-folder check doesn't lock down all subagent use,
# only method ones that would misbehave against an unadopted folder.
METHOD_SUBAGENT_PREFIX = "no-code-method:"

# V29: file names /adopt scaffolds at project root. When folder is
# unadopted, Edit/Write/MultiEdit on these passes the V29 gate so /adopt's
# scaffold writes work. (Other writes are blocked.) This is the V29
# discrimination mechanism — narrower than a runtime flag-file but
# narrow enough that main Claude's "ignore the advisory and edit code"
# attempts get caught.
SCAFFOLD_NAMES = frozenset({
    "UX.md",
    "BACKLOG.md",
    "MANIFEST.md",
    "TEST-LOG.md",
    "CLAUDE.md",
    OPT_OUT_MARKER_NAME,
})

# Path-block keys treated as writable. Everything else in the path block —
# UX.md, plus any additional source-of-truth docs declared by the project —
# is locked.
WRITABLE_LOGICAL_NAMES = {"BACKLOG.md", "MANIFEST.md", "TEST-LOG.md"}

# PATH_BLOCK_PATTERN now lives in project_state.py (V28 extraction).

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

# PARSER_PATH, PARSER_TIMEOUT_SECONDS, TEST_LOG_DATA_ROW_PATTERN, and
# BUILD_LOG_SESSION_HEADING_PATTERN now live in project_state.py
# (V28 extraction); the helpers that use them (run_parser, parse_test_log_rows,
# is_row_confirmed, identify_previous_session) are imported at the top.


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


def build_locked_map(project_root: Path) -> dict:
    """Read CLAUDE.md from project_root, parse the path block, and return a
    dict mapping resolved absolute path strings -> logical names for every
    LOCKED doc in the path block.

    Returns an empty dict if CLAUDE.md is missing, has no parseable path
    block, or contains no locked entries. The hook treats an empty locked
    map as "no enforcement applicable" and falls through to allow.
    """
    text = safe_read_text(project_root / "CLAUDE.md")
    if text is None:
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


# --- V29 adoption-gate helpers ---


def is_scaffold_path(target_path, project_root):
    """V29: True if target_path is a direct child of project_root with one
    of the SCAFFOLD_NAMES. /adopt's scaffolding writes land here; the
    adoption gate exempts these paths so /adopt can do its work without
    needing a runtime flag-file mechanism.

    Direct-child only — a deeper-nested file with one of the scaffold
    names (e.g. `subdir/UX.md`) doesn't qualify."""
    try:
        relative = Path(target_path).relative_to(project_root)
    except ValueError:
        return False
    if len(relative.parts) != 1:
        return False
    return relative.name in SCAFFOLD_NAMES


def make_v29_edit_deny_reason(target_path) -> str:
    """V29: deny-reason for Edit/Write/MultiEdit on a non-scaffold path
    in an unadopted folder. Names the path, points at /adopt, and
    documents the opt-out path so the user has a clear exit."""
    return (
        f"BLOCKED: this folder is unadopted (no `*No-code method — Version "
        "N.*` footer in `CLAUDE.md`), and it contains pre-existing work "
        "that the no-code-method plugin would put at risk if you proceed. "
        f"The Edit/Write/MultiEdit target `{target_path}` is outside the "
        "scaffolding paths the plugin manages.\n\n"
        "Run `/adopt` first. The five-case dialogue routes you to the "
        "right setup: empty folder → new project; existing code with no "
        "docs → scaffold alongside; existing code with foreign `CLAUDE.md` "
        "→ migrate / overwrite / leave; already adopted; opted out.\n\n"
        "If you have deliberately decided NOT to use the method in this "
        "folder, run `/adopt` and pick the cancel option (case 2) or the "
        "leave-alone option (case 3) — both write `.no-code-method-skip` "
        "at the project root, which opts the folder out of method "
        "discipline and stops this gate from firing on future tool calls."
    )


def make_v29_task_deny_reason(subagent_type) -> str:
    """V29: deny-reason for Task invocations of a method subagent (other
    than /adopt itself) in an unadopted folder. The method subagents all
    assume a method-managed project; against an unadopted folder they
    would fail or produce garbage."""
    return (
        f"BLOCKED: this folder is unadopted, so the method subagent "
        f"`{subagent_type}` cannot be invoked. The planning, before-build, "
        "batch-executor, and after-build subagents all assume a method-"
        "managed project (UX.md, BACKLOG.md, MANIFEST.md present and "
        "wired through CLAUDE.md's path block); they would fail or "
        "produce garbage against an unadopted folder.\n\n"
        "Run `/adopt` first. After adoption completes, this subagent "
        "will work normally. To opt out of method discipline for this "
        "folder instead, run `/adopt` and pick the cancel option "
        "(case 2) or leave-alone option (case 3)."
    )


def check_v29_adoption_gate(project_root, tool_name, tool_input):
    """V29: enforce the adoption gate on Edit/Write/MultiEdit and Task
    calls when the folder is unadopted.

    Returns a deny-reason string when the call should be denied, None
    otherwise. None means either (a) the gate doesn't apply (folder is
    adopted, opted out, or genuinely empty), or (b) the gate applies
    but this specific call is exempt (Task → /adopt, Edit/Write on a
    scaffold path, non-method Task call).

    Architecture context (Path D, V29): SessionStart emits an advisory
    when the folder is unadopted; this gate provides the enforcement.
    The two together replace the originally-scoped `systemMessage` halt
    at SessionStart, which Claude Code's hook protocol doesn't support
    (GitHub anthropics/claude-code#10225 → #12151)."""
    if not is_unadopted_with_work(project_root):
        # Adopted, opted out, or genuinely empty — gate doesn't apply.
        # Downstream checks (V19/V22/V25/V27) handle the adopted-folder
        # cases on their own terms.
        return None

    if tool_name == "Task":
        subagent_type = tool_input.get("subagent_type")
        # /adopt is the resolution mechanism — always allowed.
        if subagent_type == ADOPT_SUBAGENT_TYPE:
            return None
        # Other method subagents are blocked.
        if isinstance(subagent_type, str) and subagent_type.startswith(
            METHOD_SUBAGENT_PREFIX
        ):
            return make_v29_task_deny_reason(subagent_type)
        # Non-method Task calls (user-invoked general-purpose agents,
        # etc.) fall through.
        return None

    if tool_name in WRITING_TOOLS:
        file_path = tool_input.get("file_path")
        if not isinstance(file_path, str) or not file_path:
            # Malformed input — be lenient.
            return None
        target = Path(file_path)
        try:
            target = (
                target.resolve()
                if target.is_absolute()
                else (Path(project_root) / target).resolve()
            )
        except OSError:
            return None
        if is_scaffold_path(target, project_root):
            # Scaffold-path write — allowed during unadopted state so
            # /adopt's scaffolding can proceed. Minor coverage gap: main
            # Claude can also write these paths directly without going
            # through /adopt. Accepted per V29 scope (the user reviews
            # any unexpected scaffold output).
            return None
        return make_v29_edit_deny_reason(target)

    return None


# --- V27 test-confirmation gate helpers ---


def make_test_confirmation_deny_reason(unconfirmed_rows, build_log_status, session_id):
    """Compose the deny-reason text. Names the unconfirmed rows by # and
    Test Description, explains which mode the gate is in (narrowed by
    BUILD-LOG.md vs. strict fallback), and points at the read-back."""
    row_lines = []
    for r in unconfirmed_rows:
        component = r.get("component") or "(no component)"
        row_lines.append(
            f"  - #{r['id']} (session `{r['session']}`, component "
            f"`{component}`): {r['description']}"
        )
    rows_block = "\n".join(row_lines) if row_lines else "  (none)"

    if build_log_status == "ok":
        mode_explanation = (
            f"Gate identified the previous build batch's session as "
            f"`{session_id}` (from BUILD-LOG.md). The rows above belong "
            "to that session and are still unconfirmed."
        )
    elif build_log_status == "missing":
        mode_explanation = (
            "BUILD-LOG.md not found — gate is in strict fallback mode: "
            "any row with `Confirmed Explicitly: No` blocks. If this "
            "project keeps a BUILD-LOG.md, add it to CLAUDE.md's path "
            "block (or place it at the project root) so the gate can "
            "narrow to the previous session's rows."
        )
    else:  # 'unparseable'
        mode_explanation = (
            "BUILD-LOG.md present but unparseable — no `## <session-tag>` "
            "heading could be matched at the top of the file. Gate is in "
            "strict fallback mode: any row with `Confirmed Explicitly: "
            "No` blocks. Fix BUILD-LOG.md's heading format (expected "
            "`## <tag> — ...` newest first) or confirm the rows above "
            "to proceed."
        )

    return (
        "BLOCKED: cannot start a new build batch while the previous "
        "batch's test session is still open.\n\n"
        f"{mode_explanation}\n\n"
        f"Unconfirmed TEST-LOG.md rows:\n{rows_block}\n\n"
        "Per NO-CODE-METHOD.md → *Method contract → Prohibited of Claude "
        "→ Test-confirmation gate* (Rule 3), the test-session-close "
        "read-back (Rule 2, first sub-step of *During planning*) must "
        "run before a new build batch starts. Tell the user to /clear "
        "and start a planning session; the planning subagent will walk "
        "each row above asking Pass / Fail / Skipped."
    )


def check_test_confirmation_gate(project_root, tool_input):
    """V27 check (4): test-confirmation gate on Task → batch-executor.

    Returns a deny-reason string if any unconfirmed previous-session rows
    exist in TEST-LOG.md. Returns None to allow.

    The lenient principle applies for the missing-file cases (no
    TEST-LOG.md → allow; no rows → allow). The strict-fallback path only
    fires when TEST-LOG.md exists AND has unconfirmed rows AND BUILD-LOG.md
    can't narrow them to the previous session — safety-by-default per V26
    Q3 + V27 Q4.

    V28: the row-collection + session-narrowing logic moved to
    project_state.get_unconfirmed_previous_session_rows so stop.py's V28
    TEST-LOG-awareness check shares one definition of "test session open."
    This function still composes the deny message — the deny phrasing is
    specific to the pre-tool-use gate's role and stays here.
    """
    subagent_type = tool_input.get("subagent_type")
    if subagent_type != BATCH_EXECUTOR_SUBAGENT_TYPE:
        return None

    unconfirmed, build_log_status, session_id = (
        get_unconfirmed_previous_session_rows(project_root)
    )
    if not unconfirmed:
        return None

    return make_test_confirmation_deny_reason(
        unconfirmed, build_log_status, session_id
    )


def main() -> int:
    data = parse_input()
    if not isinstance(data, dict):
        return emit_allow()

    tool_name = data.get("tool_name")
    tool_input = data.get("tool_input") or {}

    # Anything outside the writing tools + Task passes through without
    # inspection. Cheap exit before the project-root resolution.
    if tool_name not in WRITING_TOOLS and tool_name != "Task":
        return emit_allow()

    cwd_str = data.get("cwd")
    if not isinstance(cwd_str, str) or not cwd_str:
        return emit_allow()
    try:
        project_root = Path(cwd_str).resolve()
    except OSError:
        return emit_allow()

    # V29 check (5): adoption gate. Fires on Edit/Write/MultiEdit and Task
    # calls when folder is unadopted-with-work and not opted out. Returns
    # None for adopted folders, opted-out folders, and genuinely-empty
    # folders — downstream checks then run on their normal terms.
    v29_deny_reason = check_v29_adoption_gate(project_root, tool_name, tool_input)
    if v29_deny_reason:
        return emit_deny(v29_deny_reason)

    # V27 check (4): test-confirmation gate fires on Task invocations
    # targeting the batch-executor subagent. Other Task calls fall through.
    if tool_name == "Task":
        gate_deny_reason = check_test_confirmation_gate(project_root, tool_input)
        if gate_deny_reason:
            return emit_deny(gate_deny_reason)
        return emit_allow()

    # Writing tools (Edit/Write/MultiEdit) run checks (1)-(3).
    file_path_str = tool_input.get("file_path")
    if not isinstance(file_path_str, str) or not file_path_str:
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
