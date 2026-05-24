#!/usr/bin/env python3
"""
SessionStart hook for the no-code-method plugin.

Runs at the start of every Claude Code session in any folder where the plugin
is installed. Two phases:

  Phase 1 (V29) — adoption check
    Before any tier logic, the hook runs `is_unadopted_with_work` against
    the project root. An unadopted folder (no method footer in CLAUDE.md)
    with substantial work (per the Q2 rule: build manifest, source dir,
    foreign CLAUDE.md, or >5 non-infra files recursively) emits the V29
    advisory and short-circuits: `systemMessage` (user-visible warning)
    plus `additionalContext` (directive into Claude's context), both
    pointing at `/setup`. Advisory only — SessionStart has no halt
    mechanism (the `systemMessage` field is a warning, `continue: false`
    terminates the session entirely, and `UserPromptSubmit`-in-plugins is
    broken per GitHub anthropics/claude-code#10225 → #12151). Real
    enforcement happens in the PreToolUse hook, which denies
    Edit/Write/MultiEdit and Task→method-subagent calls from main Claude
    until the folder is adopted. Per-project opt-out is handled by Claude
    Code's built-in plugin disable (/plugin → Installed → toggle off).

  Phase 2 — tier classification (unchanged from V21)
    Runs only on adopted folders and genuinely-empty unadopted folders.
    Three tiers:

      Tier 1 (non-method folder)
        Neither CLAUDE.md nor any spine doc carrying the method's version
        footer is present at the project root. The hook writes nothing
        and exits 0 — the plugin is invisible in folders that aren't
        method projects. With V29 in place, this tier now covers only
        genuinely-empty folders (unadopted-with-
        work folders short-circuit in Phase 1).

      Tier 2 (partial method shape)
        Some method-shaped files are present but the project isn't fully
        set up: e.g. CLAUDE.md is missing while spine docs are present,
        or CLAUDE.md is present but its fenced JSON path block can't be
        parsed. The hook injects the universal-behaviour rules plus a
        single-paragraph gap flag naming the specific missing piece and
        pointing at /setup.

      Tier 3 (complete method project)
        CLAUDE.md is present and its fenced JSON path block parses. The
        hook injects the universal-behaviour rules plus a full state
        summary: resolved doc paths, template-state detection, version-
        footer mismatch tripwire, top build batch (for the resume
        route), and a reminder that route classification of the user's
        opener stays with Claude.

Why SessionStart and not UserPromptSubmit:
  UserPromptSubmit hooks declared in plugin hooks.json don't execute due to
  GitHub bug anthropics/claude-code#10225. SessionStart works in plugins
  today, and given the no-code method's /clear-after-every-build discipline,
  it's functionally equivalent: every new session re-fires the hook.

Locating the project root:
  Claude Code's hook input protocol passes a JSON object on stdin including
  a `cwd` field containing the project root (verified via the plugin
  hook-development SKILL.md). The CLAUDE_PROJECT_DIR env var is unreliable
  in plugin hooks (anthropics/claude-code#9447) so we don't depend on it.
  os.getcwd() is a safe fallback because the hook process's CWD is also the
  project root.

Output protocol:
  Tier 1: write nothing to stdout, exit 0.
  Tier 2 and 3: write a JSON object to stdout with hookSpecificOutput
  containing hookEventName ("SessionStart") and additionalContext (the
  combined universal rules + tier-specific summary). Exit 0.

  Hook errors (missing universal-behaviour.md, etc.) are surfaced *as*
  additionalContext with a [no-code-method plugin warning] prefix rather
  than dying silently — Claude (and the user) should know if the plugin is
  broken, not see no rules and assume everything is fine.
"""

import json
import os
import re
import sys
from pathlib import Path

# Make plugin/scripts/ importable for the shared project-state helpers.
# (Same pattern as pre_tool_use.py — V28 extraction.)
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from project_state import (  # noqa: E402 — must follow sys.path insert
    FOOTER_PATTERN,
    TEST_LOG_DATA_ROW_PATTERN,
    BUILD_LOG_ENTRY_HEADING_PATTERN,
    BUILD_LOG_INDEX_REF_PATTERN,
    has_method_footer,
    extract_footer_version,
    has_substantial_work,
    is_unadopted_with_work,
    parse_test_log_rows,
)

# --- Constants ---

# The method version this build of the plugin carries. Bumped when the
# session substantively changes the method or plugin (per BUILD-METHOD.md →
# Session tag vs. method version) — dev-internal-only sessions do not bump
# this. Used by the version-footer mismatch tripwire to compare each loaded
# doc's footer against the plugin's expected method version.
PLUGIN_METHOD_VERSION = 61

# Spine doc filenames the hook scans for at the project root when CLAUDE.md
# is missing — to distinguish tier 1 from tier 2. Detection is tightened by
# requiring the method footer to be present in the file (see has_method_footer).
# TEST-LOG.md added in V26 (spine-doc promotion) / V27 (detection wiring).
SPINE_FILENAMES = ("UX.md", "BACKLOG.md", "MANIFEST.md", "TEST-LOG.md")

# Folder-mode spine doc paths (relative to project root). Checked in addition
# to SPINE_FILENAMES for tier 2 detection.
SPINE_FOLDER_PATHS = (
    Path("BACKLOG") / "INDEX.md",
    Path("build-log") / "INDEX.md",
)

# CLAUDE.md's path block is the first fenced JSON code block in the file.
# Same pattern as pre_tool_use.py — see V18's path block format spec.
PATH_BLOCK_PATTERN = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

# FOOTER_PATTERN now lives in project_state.py (V29 extraction); imported above.

# Strong signal that a doc is still in template form: the literal placeholder
# string used in every template's heading and body.
TEMPLATE_PLACEHOLDER_PATTERN = re.compile(r"\[Project Name\]")

# V54: Red flag entry pattern — matches `**[RED FLAG]**` followed by the
# one-line description (with or without a blockquote `>` prefix).
RED_FLAG_ENTRY_PATTERN = re.compile(
    r"\*\*\[RED FLAG\]\*\*\s*(.+?)$", re.MULTILINE
)

# V54: Red flags section heading in BACKLOG.
RED_FLAGS_SECTION_PATTERN = re.compile(r"^## Red flags\s*$", re.MULTILINE)

# Heading shape for a build batch in BACKLOG.md (single-file mode).
BUILD_BATCH_HEADING_PATTERN = re.compile(r"^### Batch: (.+)$", re.MULTILINE)

# Heading shape for the Build batches section in BACKLOG.md / INDEX.md.
BUILD_BATCHES_SECTION_PATTERN = re.compile(r"^## Build batches\s*$", re.MULTILINE)

# Generic next-section pattern (used to bound the Build batches section).
NEXT_SECTION_PATTERN = re.compile(r"^## ", re.MULTILINE)

# Batch reference line in INDEX.md (folder mode): `- `NNNN-name.md``.
BATCH_REF_PATTERN = re.compile(r"^-\s+`(\d{4}-.+?\.md)`", re.MULTILINE)

# H1 heading in a per-batch file (folder mode): `# <batch name>`.
BATCH_FILE_H1_PATTERN = re.compile(r"^# (.+?)\s*$", re.MULTILINE)

# Status: line — batch lifecycle state. Shipped/parked batches are skipped.
STATUS_LINE_PATTERN = re.compile(r"^Status:\s*(\w+)\s*$", re.MULTILINE)
_SKIP_STATUSES = frozenset(("shipped", "parked"))

# --- V27 TEST-LOG tripwire patterns ---

# TEST_LOG_DATA_ROW_PATTERN and parse_test_log_rows now imported from
# project_state.py (V48 extraction — the 10-column format made local
# 8-column copies a misparse hazard on new rows).

# Legacy single-file BUILD-LOG.md heading pattern: `## <token>` names the
# latest session (newest-first). Used as fallback when there is no
# build-log/ folder. When neither folder nor file is found, the tripwire
# falls back to "any unconfirmed row" — same strict-fallback semantics as
# the test-confirmation gate (V26 Q3, V27 Q4).
BUILD_LOG_SESSION_HEADING_PATTERN = re.compile(r"^##\s+(\S+)", re.MULTILINE)

# V29 adoption-state constants (BUILD_MANIFEST_NAMES, SOURCE_DIR_NAMES,
# INFRA_NAMES, SUBSTANTIAL_WORK_FILE_THRESHOLD) now live in
# project_state.py — imported above where needed.

# --- File reads ---

def read_universal_rules() -> str:
    """Read universal-behaviour.md (sibling file in hooks/). Preserves V18's
    behaviour: surface a [no-code-method plugin warning] in-context rather
    than silently emitting nothing if the file can't be read."""
    rules_path = Path(__file__).parent / "universal-behaviour.md"
    try:
        return rules_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return (
            "[no-code-method plugin warning] "
            f"universal-behaviour.md not found at {rules_path}. "
            "The universal behavioural rules could not be injected. "
            "This is a plugin installation problem, not a method problem."
        )
    except OSError as exc:
        return (
            "[no-code-method plugin warning] "
            f"Could not read universal-behaviour.md ({exc}). "
            "The universal behavioural rules could not be injected."
        )


def safe_read_text(path: Path):
    """Read a text file; return None on any failure (missing, permissions,
    encoding). Used everywhere the hook needs to peek at a file without
    risking an unhandled exception in the subprocess."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


# --- Stdin / project root ---

def parse_stdin_input():
    """Read hook input JSON from stdin. Returns dict on success, None on any
    failure. Failure is non-fatal — the hook falls back to os.getcwd() for
    project-root detection."""
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def get_project_root(stdin_data) -> Path:
    """Resolve the consumer project's root path.

    Order of preference:
      1. stdin JSON's `cwd` field (the documented hook input contract).
      2. os.getcwd() (also the project root per Claude Code's hook contract).

    Avoids relying on $CLAUDE_PROJECT_DIR — that env var is broken for plugin
    hooks (anthropics/claude-code#9447), and even if/when fixed, the stdin
    contract is the more reliable source."""
    cwd_str = None
    if isinstance(stdin_data, dict):
        candidate = stdin_data.get("cwd")
        if isinstance(candidate, str) and candidate:
            cwd_str = candidate
    if cwd_str is None:
        cwd_str = os.getcwd()
    try:
        return Path(cwd_str).resolve()
    except OSError:
        return Path(cwd_str)


# --- Parsers / detectors ---

def extract_path_block(claude_md_text: str):
    """Extract and parse the fenced JSON path block from CLAUDE.md.
    Returns dict on success; None if absent or unparseable."""
    match = PATH_BLOCK_PATTERN.search(claude_md_text)
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


# extract_footer_version and has_method_footer now live in project_state.py
# (V29 extraction); imported above.


def is_template_state(text: str) -> bool:
    """Heuristic: text still contains the `[Project Name]` placeholder that
    every template ships with. Once a project is kicked off, [Project Name]
    is replaced; surviving instances strongly indicate the doc hasn't been
    filled in yet."""
    return bool(TEMPLATE_PLACEHOLDER_PATTERN.search(text))


def find_method_spine_docs(project_root: Path):
    """Return a list of spine doc paths at the project root that carry the
    method footer. Tightens tier 2 detection — an unrelated BACKLOG.md from
    some other context will not falsely trigger method-aware behaviour.

    Checks both single-file spine docs (UX.md, BACKLOG.md, etc.) and
    folder-mode paths (BACKLOG/INDEX.md)."""
    found = []
    for name in SPINE_FILENAMES:
        candidate = project_root / name
        text = safe_read_text(candidate)
        if text is not None and has_method_footer(text):
            found.append(candidate)
    for rel_path in SPINE_FOLDER_PATHS:
        candidate = project_root / rel_path
        text = safe_read_text(candidate)
        if text is not None and has_method_footer(text):
            found.append(candidate)
    return found


def _batch_status(text: str) -> str:
    """Extract the Status: value from batch text. Returns lowercase status
    or 'queued' if absent."""
    m = STATUS_LINE_PATTERN.search(text)
    return m.group(1).lower() if m else "queued"


def detect_top_build_batch(backlog_text: str, backlog_path=None):
    """Find the first actionable batch name in the `## Build batches` section.

    Skips batches with Status: shipped or Status: parked. In single-file
    mode, searches for `### Batch:` headings inline. In folder mode (when
    `backlog_path` is provided and the section contains batch reference
    lines instead of headings), reads each referenced batch file.

    Returns the batch title, or None if no real batch is present. Template
    placeholder titles like `[short descriptive name]` are filtered out."""
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return None

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    # Single-file mode: inline `### Batch:` headings.
    batch_matches = list(BUILD_BATCH_HEADING_PATTERN.finditer(section_text))
    if batch_matches:
        for i, batch_match in enumerate(batch_matches):
            title = batch_match.group(1).strip()
            if title.startswith("[") and title.endswith("]"):
                continue
            body_start = batch_match.end()
            body_end = (
                batch_matches[i + 1].start()
                if i + 1 < len(batch_matches)
                else len(section_text)
            )
            body = section_text[body_start:body_end]
            if _batch_status(body) in _SKIP_STATUSES:
                continue
            return title
        return None

    # Folder mode: reference lines like `- `0001-name.md``.
    if backlog_path is not None:
        for ref_match in BATCH_REF_PATTERN.finditer(section_text):
            batch_file = backlog_path.parent / ref_match.group(1)
            batch_text = safe_read_text(batch_file)
            if not batch_text:
                continue
            if _batch_status(batch_text) in _SKIP_STATUSES:
                continue
            h1_match = BATCH_FILE_H1_PATTERN.search(batch_text)
            if h1_match:
                title = h1_match.group(1).strip()
                if title.startswith("[") and title.endswith("]"):
                    continue
                return title

    return None


def detect_red_flags(backlog_text: str) -> list:
    """Find non-empty Red flag entries in BACKLOG's top-level Red flags section.

    Returns a list of one-line descriptions (the text after **[RED FLAG]**),
    or empty list if the section is absent or empty. Works for both single-file
    BACKLOG.md and folder-mode INDEX.md (the Red flags section lives in
    INDEX.md in folder mode)."""
    section_match = RED_FLAGS_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return []

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    flags = []
    for match in RED_FLAG_ENTRY_PATTERN.finditer(section_text):
        desc = match.group(1).strip()
        if desc:
            flags.append(desc)
    return flags


# --- V27 TEST-LOG tripwire helpers ---


# parse_test_log_rows imported from project_state.py — see import block above.


def is_row_confirmed(row):
    """A row is confirmed iff its `Confirmed Explicitly` cell starts with
    `Yes`. Per Rule 1 (Never infer completion), absence-of-Yes is not a
    tacit pass."""
    ce = row.get("confirmed_explicitly", "").strip()
    return ce.startswith("Yes")


def identify_previous_session_from_build_log(project_root, resolved):
    """Try to identify the previous build batch's session from the build log.

    Supports folder mode (build-log/INDEX.md → per-build file) and legacy
    single-file mode (BUILD-LOG.md with ## headings).

    Returns (session_id, status) where status is one of 'ok' (heading
    parsed), 'missing' (build log absent), or 'unparseable' (present
    but no session heading matched).

    Looks at the path block first (via `resolved`), then falls back to
    build-log/INDEX.md or BUILD-LOG.md at the project root."""
    candidate = None
    build_log_data = resolved.get("BUILD-LOG.md")
    if build_log_data:
        candidate, _text = build_log_data
    if candidate is None or not candidate.exists():
        candidate = project_root / "build-log" / "INDEX.md"
    if not candidate.exists():
        candidate = project_root / "BUILD-LOG.md"
    if not candidate.exists():
        return None, "missing"
    text = safe_read_text(candidate)
    if text is None:
        return None, "unparseable"

    if candidate.name.upper() == "INDEX.MD":
        ref_match = BUILD_LOG_INDEX_REF_PATTERN.search(text)
        if not ref_match:
            return None, "unparseable"
        entry_file = candidate.parent / ref_match.group(1)
        entry_text = safe_read_text(entry_file)
        if entry_text is None:
            return None, "unparseable"
        heading_match = BUILD_LOG_ENTRY_HEADING_PATTERN.search(entry_text)
        if not heading_match:
            return None, "unparseable"
        return heading_match.group(1).strip(), "ok"

    match = BUILD_LOG_SESSION_HEADING_PATTERN.search(text)
    if not match:
        return None, "unparseable"
    return match.group(1).strip(), "ok"


def detect_unconfirmed_test_rows(project_root, resolved):
    """Find TEST-LOG.md rows from the previous build batch whose
    `Confirmed Explicitly` column is not `Yes`.

    Returns a tuple (unconfirmed_rows, build_log_status, session_id):
      - unconfirmed_rows: list of row dicts (possibly empty)
      - build_log_status: 'ok' | 'missing' | 'unparseable'
      - session_id: the identified session string, or None

    Returns ([], 'no_test_log', None) when TEST-LOG.md is missing or
    unreadable from the path block — there's nothing to trip on.

    Strict-fallback semantics apply when BUILD-LOG.md can't narrow:
    any row with `Confirmed Explicitly: No` counts as unconfirmed. Same
    rule as the V27 test-confirmation gate (per V26 Q3 + V27 Q4)."""
    test_log_data = resolved.get("TEST-LOG.md")
    if not test_log_data:
        return [], "no_test_log", None
    _path, text = test_log_data
    rows = parse_test_log_rows(text)
    if not rows:
        return [], "no_test_log", None

    session_id, build_log_status = identify_previous_session_from_build_log(
        project_root, resolved
    )
    if build_log_status == "ok":
        unconfirmed = [
            r for r in rows
            if r["session"] == session_id and not is_row_confirmed(r)
        ]
    else:
        unconfirmed = [r for r in rows if not is_row_confirmed(r)]
    return unconfirmed, build_log_status, session_id


def format_test_log_tripwire_block(unconfirmed_rows, build_log_status, session_id):
    """Compose the additionalContext block for the TEST-LOG tripwire.

    The block is intentionally directive: it tells main Claude to route
    the next planning-subagent invocation regardless of the opener's
    classification, because the test session is the gate. The planning
    subagent's first sub-step (per planning.md → *Close the previous
    build's test session*) will walk the rows below."""
    row_lines = []
    for r in unconfirmed_rows:
        component = r.get("component") or "(no component)"
        row_lines.append(
            f"  - #{r['id']} (session `{r['session']}`, component "
            f"`{component}`): {r['description']}"
        )
    rows_block = "\n".join(row_lines)

    if build_log_status == "ok":
        mode_note = (
            f"Identified previous build batch's session as `{session_id}` "
            "from the build log. Rows below are unconfirmed from that "
            "session."
        )
    elif build_log_status == "missing":
        mode_note = (
            "Build log not found — strict fallback: every row with "
            "`Confirmed Explicitly: No` is treated as pending."
        )
    else:  # unparseable
        mode_note = (
            "Build log present but unparseable — strict fallback: every "
            "row with `Confirmed Explicitly: No` is treated as pending."
        )

    return (
        "- **TEST-LOG tripwire: previous build batch's test session is "
        "still open.** Per `universal-behaviour.md` → *Prohibited "
        "behaviours* → 'Do not invoke the batch-executor', and per "
        "`planning.md` → *Close the previous build's test session*, "
        "the next planning session MUST close the test session via "
        "per-row read-back before any new build batch can start.\n\n"
        f"  {mode_note}\n\n"
        "  Unconfirmed rows:\n"
        f"{rows_block}\n\n"
        "  **Routing override.** Regardless of the user's opener "
        "classification (test notes / feature request / scope question / "
        "conversational), invoke the planning subagent "
        "(`no-code-method:planning`) as the next action. Begin the "
        "subagent prompt with: *\"Before we get to your question — N "
        "pending tests from session X to confirm. First: <test description "
        "of row 1>?\"* The subagent's first sub-step is the per-row "
        "read-back; it will walk each row above asking Pass / Fail / "
        "Skipped, one at a time. Do NOT attempt to start a new build "
        "batch or invoke any other subagent until the read-back closes "
        "the session — the PreToolUse hook will deny the batch-executor "
        "invocation if you try."
    )


# --- V29 unadopted-folder advisory (output formatting) ---
#
# Detection helpers (has_substantial_work, is_unadopted_with_work) live in
# project_state.py — imported above. The advisory text and JSON-emission
# shape stay here because they're SessionStart-specific (PreToolUse emits
# a different shape).


def build_unadopted_advisory_context(project_root: Path) -> str:
    """Compose the additionalContext block for an unadopted-with-work
    folder. Strong directive: do nothing substantive, route the user to
    /setup. Pairs with the systemMessage user-visible warning."""
    return (
        "## No-code-method plugin — unadopted folder\n\n"
        "**This folder has not been adopted by the no-code-method plugin, "
        "and it contains existing work that the plugin would put at risk "
        "if you proceed normally.** No method-aware behaviour is active "
        "until the user runs `/setup`.\n\n"
        f"Project root: `{project_root}`\n\n"
        "**Required behaviour for this session:**\n\n"
        "- Direct the user to run `/setup` before doing anything else.\n"
        "- Do NOT attempt Edit, Write, MultiEdit, or Task→method-subagent "
        "tool calls. The PreToolUse hook will deny them anyway, and "
        "attempting them creates confusing churn.\n"
        "- If the user does not want the method in this folder, they can "
        "disable the plugin for this project: type `/plugin`, go to the "
        "Installed tab, and toggle it off. This is a Claude Code built-in "
        "— it stops all plugin hooks from firing in this folder.\n\n"
        "Until `/setup` runs (or the plugin is disabled for this project), "
        "the only useful actions are conversational responses pointing the "
        "user toward `/setup` or explaining how to disable the plugin."
    )


def build_unadopted_system_message() -> str:
    """User-visible warning text for the unadopted-with-work advisory.
    Kept short — system messages are noisier than additionalContext and
    we want this one to land."""
    return (
        "[no-code-method] Folder has work but isn't set up — run /setup "
        "to start, or disable the plugin for this project via /plugin → "
        "Installed → toggle off. Edit/Write/MultiEdit calls will be "
        "denied until /setup completes."
    )


def emit_unadopted_advisory(project_root: Path) -> int:
    """Write the V29 unadopted-with-work advisory to stdout. Combines a
    user-visible systemMessage with Claude-facing additionalContext.
    Returns exit code 0 — this is advisory, not a halt (SessionStart
    has no halt mechanism per the V29 research findings)."""
    output = {
        "systemMessage": build_unadopted_system_message(),
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": build_unadopted_advisory_context(project_root),
        },
    }
    json.dump(output, sys.stdout)
    return 0


# --- Tier detection ---

def detect_tier(project_root: Path):
    """Determine which tier applies. Returns a 4-tuple:
        (tier_number, claude_text_or_None, path_block_or_None, spine_docs_list)

    Tier 1: no CLAUDE.md, and no spine doc at the project root carries the
            method footer.
    Tier 2: partial shape. Either CLAUDE.md is present but the path block
            isn't parseable, or method-footer spine docs are present without
            a CLAUDE.md.
    Tier 3: CLAUDE.md is present and its fenced JSON path block parses.
    """
    claude_path = project_root / "CLAUDE.md"
    claude_text = safe_read_text(claude_path)
    spine_docs = find_method_spine_docs(project_root)

    if claude_text is None:
        if not spine_docs:
            return 1, None, None, []
        return 2, None, None, spine_docs

    path_block = extract_path_block(claude_text)
    if not path_block:
        return 2, claude_text, None, spine_docs

    return 3, claude_text, path_block, spine_docs


# --- Tier 3 state summary ---

def resolve_path_block_docs(project_root: Path, path_block: dict):
    """Resolve each entry in the path block to an absolute path and read its
    text. Returns (resolved, unresolved) where:
      resolved = {logical_name: (abs_path, text)}
      unresolved = [(logical_name, relative_path)] — entries whose file
                   could not be read.
    """
    resolved = {}
    unresolved = []
    for logical_name, rel_path in path_block.items():
        if not isinstance(logical_name, str) or not isinstance(rel_path, str):
            continue
        try:
            abs_path = (project_root / rel_path).resolve()
        except OSError:
            unresolved.append((logical_name, rel_path))
            continue
        text = safe_read_text(abs_path)
        if text is None:
            unresolved.append((logical_name, rel_path))
        else:
            resolved[logical_name] = (abs_path, text)
    return resolved, unresolved


def collect_template_state_docs(resolved: dict):
    """Return logical names of docs that still look like templates."""
    return [name for name, (_p, text) in resolved.items() if is_template_state(text)]


def collect_footer_mismatches(resolved: dict, claude_text: str):
    """Return [(logical_name, found_version)] for every doc whose footer
    version differs from the plugin's current version. CLAUDE.md is checked
    separately (it isn't a path-block entry against itself)."""
    mismatches = []
    for name, (_p, text) in resolved.items():
        v = extract_footer_version(text)
        if v is None:
            continue
        if v != PLUGIN_METHOD_VERSION:
            mismatches.append((name, v))
    claude_v = extract_footer_version(claude_text)
    if claude_v is not None and claude_v != PLUGIN_METHOD_VERSION:
        mismatches.append(("CLAUDE.md", claude_v))
    return mismatches


def build_state_summary(project_root: Path, claude_text: str, path_block: dict) -> str:
    """Compose the prose state summary for tier 3."""
    resolved, unresolved = resolve_path_block_docs(project_root, path_block)

    lines = ["## Project state (detected by SessionStart hook)", ""]

    lines.append(f"- **Project root:** `{project_root}`")
    lines.append(
        f"- **Path block:** resolved {len(resolved)} of {len(path_block)} entries."
    )

    if unresolved:
        lines.append("- **Unresolved doc paths in CLAUDE.md's path block:**")
        for logical_name, rel_path in unresolved:
            lines.append(f"  - `{logical_name}` → `{rel_path}` (file not found)")
        lines.append(
            "  Search the project for each file by name, surface the "
            "mismatch (declared path vs. found path), and propose updating "
            "`CLAUDE.md`'s path block. Wait for the user's confirmation "
            "before editing."
        )

    template_docs = collect_template_state_docs(resolved)
    if template_docs:
        names_md = ", ".join(f"`{n}`" for n in template_docs)
        lines.append(
            f"- **Template state detected** in {names_md}. The project "
            "hasn't been kicked off yet — these docs still contain template "
            "placeholders. Per `universal-behaviour.md` → *Routing "
            "main-Claude's openers* (the *Template state* detect-first "
            "rule): recommend `/setup` to seed `UX.md`, `BACKLOG.md`, "
            "and the first build batch. Wait for the user's okay before "
            "proceeding."
        )

    footer_mismatches = collect_footer_mismatches(resolved, claude_text)
    if footer_mismatches:
        lines.append(
            f"- **Method version mismatch.** Plugin is at Version "
            f"{PLUGIN_METHOD_VERSION}; some docs carry older footers:"
        )
        for logical_name, v in footer_mismatches:
            lines.append(f"  - `{logical_name}` is at Version {v}")
        lines.append(
            "  This is a tripwire, not an auto-fix. Suggest the user run "
            "`/setup` if structural drift is suspected (case 3 — migrate "
            "to current spec), or update the footers if the content is "
            "current."
        )

    backlog_data = resolved.get("BACKLOG.md")
    if backlog_data:
        backlog_resolved_path, backlog_text = backlog_data
        top_batch = detect_top_build_batch(backlog_text, backlog_resolved_path)
        if top_batch:
            lines.append(
                f"- **Top build batch in BACKLOG:** \"{top_batch}\". If "
                "the user's opener implies resume (test notes pointing at "
                "this batch, a 'continue where we left off' phrasing, etc.) "
                "default to resume per `universal-behaviour.md` → *Routing "
                "main-Claude's openers* (the unfinished-top-batch row). "
                "Confirm with the user before continuing the build."
            )

        # V54: Red flags non-empty warning. Surface deferred security/
        # privacy/data-integrity concerns prominently at session start.
        red_flags = detect_red_flags(backlog_text)
        if red_flags:
            lines.append(
                "- **Active Red flags in BACKLOG.** The following security, "
                "privacy, or data-integrity concerns are deferred with no "
                "active plan:"
            )
            for flag in red_flags:
                lines.append(f"  - {flag}")
            lines.append(
                "  Surface these at the start of the session before other "
                "work. The user must acknowledge each one — they may choose "
                "to address one now, defer it consciously, or fold it into "
                "the current planning session."
            )

    # V27 TEST-LOG tripwire: if the previous build batch's test session is
    # still open (rows with Confirmed Explicitly: No), inject a routing
    # override directing main Claude to the planning subagent regardless
    # of opener classification. See format_test_log_tripwire_block.
    unconfirmed_rows, build_log_status, session_id = detect_unconfirmed_test_rows(
        project_root, resolved
    )
    if unconfirmed_rows:
        lines.append(
            format_test_log_tripwire_block(
                unconfirmed_rows, build_log_status, session_id
            )
        )

    lines.append("")
    lines.append(
        "**Routing.** Read the user's opening message and route per "
        "`universal-behaviour.md` → *Routing main-Claude's openers*. This "
        "hook does not classify the user's opener — that's your call based "
        "on the user's words and the structural state listed above. "
        "Exception: when the TEST-LOG tripwire above fires, the routing "
        "override there takes precedence."
    )

    return "\n".join(lines)


# --- Tier 2 output ---

def build_tier_2_gap_flag(claude_text, spine_docs) -> str:
    """One-paragraph gap flag identifying which piece of the method shape
    is missing, and pointing at the right next step."""
    has_claude = claude_text is not None
    spine_names = ", ".join(f"`{p.name}`" for p in spine_docs)

    if has_claude and not spine_docs:
        gap = (
            "`CLAUDE.md` is present but its *Where the docs live* path block "
            "can't be parsed as a fenced JSON block, and no method-aware "
            "spine docs (carrying the `*No-code method — Version N.*` "
            "footer) were found at the project root."
        )
        next_step = (
            "Set up `CLAUDE.md`'s path block as fenced JSON (see "
            "`templates/CLAUDE-TEMPLATE.md` in the plugin), or run "
            "`/setup` to bring an existing project up to spec."
        )
    elif not has_claude and spine_docs:
        gap = (
            f"Spine docs ({spine_names}) carrying the method footer are "
            "present at the project root, but `CLAUDE.md` is missing. The "
            "plugin's hooks rely on `CLAUDE.md`'s path block to locate the "
            "spine docs."
        )
        next_step = (
            "Run `/setup` to bring this project up to spec — it will "
            "scaffold the missing `CLAUDE.md` and align the existing docs "
            "with the current structural rules."
        )
    elif has_claude and spine_docs:
        gap = (
            "`CLAUDE.md` is present but its *Where the docs live* path "
            f"block can't be parsed as a fenced JSON block. Spine docs "
            f"({spine_names}) are present and carry the method footer."
        )
        next_step = (
            "Either update `CLAUDE.md`'s path block to match the current "
            "fenced-JSON format (see `templates/CLAUDE-TEMPLATE.md`), or "
            "run `/setup` to bring everything up to spec."
        )
    else:
        gap = (
            "Some method-shaped files were found but the project structure "
            "is incomplete."
        )
        next_step = "Run `/setup` — it routes to the right case across new-project, migration, and refresh."

    return (
        "## No-code-method project state\n\n"
        f"**Partial method shape detected.** {gap}\n\n"
        f"{next_step} No method-aware behaviour beyond the universal "
        "rules above is available until the project's structure is complete."
    )


# --- Main ---

def emit_context(combined: str) -> int:
    """Write the standard hookSpecificOutput JSON to stdout. Exit code 0."""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": combined,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def main() -> int:
    stdin_data = parse_stdin_input()
    project_root = get_project_root(stdin_data)

    # V29 adoption check fires before tier detection. An unadopted-with-work
    # folder short-circuits with the advisory; the existing tier logic only
    # runs on adopted folders and genuinely-empty unadopted folders.
    # PreToolUse enforces what this advises.
    if is_unadopted_with_work(project_root):
        return emit_unadopted_advisory(project_root)

    tier, claude_text, path_block, spine_docs = detect_tier(project_root)

    if tier == 1:
        # Non-method folder. The plugin is invisible: no output, no rules.
        # V29 splits this tier: unadopted-with-work folders short-circuit
        # above with the advisory; what reaches here is genuinely-empty
        # folders. They stay silent.
        return 0

    # Tier 2 and tier 3 both get the universal rules. The tier-specific
    # state summary is appended after.
    universal_rules = read_universal_rules()

    if tier == 2:
        tier_output = build_tier_2_gap_flag(claude_text, spine_docs)
    else:  # tier == 3
        tier_output = build_state_summary(project_root, claude_text, path_block)

    preamble = (
        "**Two-layer permission model.** This project uses the no-code-method "
        "plugin. Some actions are blocked by method rules enforced via "
        "PreToolUse hooks — these blocks apply regardless of your Claude Code "
        "permission mode (including Auto and `--dangerously-skip-permissions`). "
        "Deny messages are prefixed `[No-code method]` and include a "
        "`What to do:` line.\n\n"
    )
    combined = preamble + universal_rules + "\n\n---\n\n" + tier_output
    return emit_context(combined)


if __name__ == "__main__":
    sys.exit(main())
