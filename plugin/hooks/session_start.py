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
    pointing at `/sovsetup`. Advisory only — SessionStart has no halt
    mechanism (the `systemMessage` field is a warning, `continue: false`
    terminates the session entirely, and `UserPromptSubmit`-in-plugins is
    broken per GitHub anthropics/claude-code#10225 → #12151). Real
    enforcement happens in the PreToolUse hook, which denies
    Edit/Write/MultiEdit calls until the folder is adopted. Per-project
    opt-out is handled by Claude
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
        pointing at /sovsetup.

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
# session substantively changes the method or plugin (per session-protocol.md →
# Three numbers to keep distinct) — dev-internal-only sessions do not bump
# this. Used by the version-footer mismatch tripwire to compare each loaded
# doc's footer against the plugin's expected method version.
PLUGIN_METHOD_VERSION = 99

# Spine doc filenames the hook scans for when CLAUDE.md is missing — to
# distinguish tier 1 from tier 2. Checked at both project root (legacy
# layout) and inside _method/ (0087+ layout). Detection is tightened by
# requiring the method footer to be present in the file (see has_method_footer).
SPINE_FILENAMES = ("UX.md", "BACKLOG.md", "MANIFEST.md", "TEST-LOG.md")

# Folder-mode spine doc paths (relative to each scan root — project root
# and _method/). Checked in addition to SPINE_FILENAMES for tier 2 detection.
SPINE_FOLDER_PATHS = (
    Path("BACKLOG") / "INDEX.md",
    Path("build-log") / "INDEX.md",
    Path("proxies") / "backlog.md",
    Path("proxies") / "build-log.md",
)

METHOD_DIR = "_method"

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

# Batch Goal line: `**Goal.** <text>`.
BATCH_GOAL_PATTERN = re.compile(r"^\*\*Goal\.\*\*\s*(.+?)$", re.MULTILINE)

# Files: section entries (ticked or unticked).
BATCH_FILES_ENTRY_PATTERN = re.compile(r"^- \[[ x]\] ", re.MULTILINE)

# Files: section unticked entries only (unclosed-build detection).
BATCH_FILES_UNTICKED_PATTERN = re.compile(r"^- \[ \] ", re.MULTILINE)

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

# Open questions section heading in BACKLOG.
OPEN_QUESTIONS_SECTION_PATTERN = re.compile(r"^## Open questions\s*$", re.MULTILINE)

# OQ heading (### title) — same level as build-batch headings in single-file.
OQ_HEADING_PATTERN = re.compile(r"^### (.+?)$", re.MULTILINE)

# Surfaced line in an OQ body: `**Surfaced.** v71` or `**Surfaced.** v71 (0068)`.
OQ_SURFACED_PATTERN = re.compile(
    r"\*\*Surfaced\.\*\*\s*(.+?)$", re.MULTILINE
)

# Extract session number from a `vNN` tag.
SESSION_TAG_NUMBER_PATTERN = re.compile(r"\bv(\d+)\b")

# Sessions-since-surfaced threshold for OQ staleness warning.
OQ_STALENESS_THRESHOLD = 20

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
        return rules_path.read_text(encoding="utf-8-sig")
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
        return path.read_text(encoding="utf-8-sig")
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
    """Return a list of spine doc paths that carry the method footer.
    Tightens tier 2 detection — an unrelated BACKLOG.md from some other
    context will not falsely trigger method-aware behaviour.

    Checks both the _method/ subdirectory (0087+ layout) and the project
    root (legacy layout). Also checks folder-mode paths (BACKLOG/INDEX.md)
    at both locations."""
    found = []
    scan_roots = [project_root / METHOD_DIR, project_root]
    for scan_root in scan_roots:
        for name in SPINE_FILENAMES:
            candidate = scan_root / name
            text = safe_read_text(candidate)
            if text is not None and has_method_footer(text):
                found.append(candidate)
        for rel_path in SPINE_FOLDER_PATHS:
            candidate = scan_root / rel_path
            text = safe_read_text(candidate)
            if text is not None and has_method_footer(text):
                found.append(candidate)
    return found


def _batch_status(text: str) -> str:
    """Extract the Status: value from batch text. Returns lowercase status
    or 'queued' if absent."""
    m = STATUS_LINE_PATTERN.search(text)
    return m.group(1).lower() if m else "queued"


def _resolve_backlog_dir(backlog_path: Path) -> Path:
    """Resolve the BACKLOG/ directory for per-batch file lookups.

    When the index is INDEX.md inside BACKLOG/, the dir is the parent.
    When the index is a proxy at proxies/backlog.md, the BACKLOG/ dir
    is a sibling of the proxies/ directory (i.e. _method/BACKLOG/).
    Falls back to the path's parent."""
    if backlog_path.name.upper() == "INDEX.MD":
        return backlog_path.parent
    if (backlog_path.name.lower() == "backlog.md"
            and backlog_path.parent.name == "proxies"):
        return backlog_path.parent.parent / "BACKLOG"
    return backlog_path.parent


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
        backlog_dir = _resolve_backlog_dir(backlog_path)
        for ref_match in BATCH_REF_PATTERN.finditer(section_text):
            batch_file = backlog_dir / ref_match.group(1)
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


def count_batch_statuses(backlog_text: str, backlog_path=None) -> dict:
    """Count build batches by status. Returns {queued: N, active: N, parked: N}.
    Shipped batches are excluded (already done). Template placeholders skipped."""
    counts = {"queued": 0, "active": 0, "parked": 0}
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return counts

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

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
            status = _batch_status(body)
            if status in counts:
                counts[status] += 1
        return counts

    if backlog_path is not None:
        backlog_dir = _resolve_backlog_dir(backlog_path)
        for ref_match in BATCH_REF_PATTERN.finditer(section_text):
            batch_file = backlog_dir / ref_match.group(1)
            batch_text = safe_read_text(batch_file)
            if not batch_text:
                continue
            h1_match = BATCH_FILE_H1_PATTERN.search(batch_text)
            if h1_match:
                title = h1_match.group(1).strip()
                if title.startswith("[") and title.endswith("]"):
                    continue
            status = _batch_status(batch_text)
            if status in counts:
                counts[status] += 1

    return counts


def detect_top_batch_details(backlog_text: str, backlog_path=None):
    """Get the top actionable batch's name, goal, and file count.

    Returns dict {name, goal, file_count} or None if no batch found."""
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return None

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    def _extract_details(body, title):
        goal_match = BATCH_GOAL_PATTERN.search(body)
        goal = goal_match.group(1).strip() if goal_match else None
        file_count = len(BATCH_FILES_ENTRY_PATTERN.findall(body))
        return {"name": title, "goal": goal, "file_count": file_count}

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
            return _extract_details(body, title)
        return None

    if backlog_path is not None:
        backlog_dir = _resolve_backlog_dir(backlog_path)
        for ref_match in BATCH_REF_PATTERN.finditer(section_text):
            batch_file = backlog_dir / ref_match.group(1)
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
                return _extract_details(batch_text, title)

    return None


def detect_top_queued_batches(backlog_text: str, backlog_path=None, limit=3):
    """Return up to `limit` queued batch summaries: [{name, goal}].

    Skips shipped, parked, active, and template-placeholder batches.
    Used by the session-open status to give the user enough context to
    pick a topic without reading the full BACKLOG."""
    results = []
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return results

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    def _extract_summary(body, title):
        goal_match = BATCH_GOAL_PATTERN.search(body)
        goal = goal_match.group(1).strip() if goal_match else None
        return {"name": title, "goal": goal}

    batch_matches = list(BUILD_BATCH_HEADING_PATTERN.finditer(section_text))
    if batch_matches:
        for i, batch_match in enumerate(batch_matches):
            if len(results) >= limit:
                break
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
            status = _batch_status(body)
            if status != "queued":
                continue
            results.append(_extract_summary(body, title))
        return results

    if backlog_path is not None:
        backlog_dir = _resolve_backlog_dir(backlog_path)
        for ref_match in BATCH_REF_PATTERN.finditer(section_text):
            if len(results) >= limit:
                break
            batch_file = backlog_dir / ref_match.group(1)
            batch_text = safe_read_text(batch_file)
            if not batch_text:
                continue
            status = _batch_status(batch_text)
            if status != "queued":
                continue
            h1_match = BATCH_FILE_H1_PATTERN.search(batch_text)
            if h1_match:
                title = h1_match.group(1).strip()
                if title.startswith("[") and title.endswith("]"):
                    continue
                results.append(_extract_summary(batch_text, title))

    return results


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


def detect_unclosed_build(backlog_text, backlog_path=None):
    """Detect a batch with Status: active and all Files: ticked.

    This state means the build completed but /sovclose never ran —
    /sovclose is what transitions Status: active → shipped. Returns
    the batch name if found, None otherwise.

    No false positives on mid-build sessions (some files unticked),
    planning sessions (no active batch), or completed builds
    (Status: shipped)."""
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return None

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    def _has_all_files_ticked(body):
        total = len(BATCH_FILES_ENTRY_PATTERN.findall(body))
        if total == 0:
            return False
        unticked = len(BATCH_FILES_UNTICKED_PATTERN.findall(body))
        return unticked == 0

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
            if _batch_status(body) != "active":
                continue
            if _has_all_files_ticked(body):
                return title
        return None

    if backlog_path is not None:
        backlog_dir = _resolve_backlog_dir(backlog_path)
        for ref_match in BATCH_REF_PATTERN.finditer(section_text):
            batch_file = backlog_dir / ref_match.group(1)
            batch_text = safe_read_text(batch_file)
            if not batch_text:
                continue
            if _batch_status(batch_text) != "active":
                continue
            h1_match = BATCH_FILE_H1_PATTERN.search(batch_text)
            if not h1_match:
                continue
            title = h1_match.group(1).strip()
            if title.startswith("[") and title.endswith("]"):
                continue
            if _has_all_files_ticked(batch_text):
                return title

    return None


def detect_mid_build(backlog_text, backlog_path=None):
    """Detect a batch with Status: active and some Files: still unticked.

    This means a build is in progress in another session. Distinct from
    detect_unclosed_build (all ticked = build finished, close skipped).
    Returns the batch name if found, None otherwise."""
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return None

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    def _has_unticked_files(body):
        total = len(BATCH_FILES_ENTRY_PATTERN.findall(body))
        if total == 0:
            return False
        unticked = len(BATCH_FILES_UNTICKED_PATTERN.findall(body))
        return unticked > 0

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
            if _batch_status(body) != "active":
                continue
            if _has_unticked_files(body):
                return title
        return None

    if backlog_path is not None:
        backlog_dir = _resolve_backlog_dir(backlog_path)
        for ref_match in BATCH_REF_PATTERN.finditer(section_text):
            batch_file = backlog_dir / ref_match.group(1)
            batch_text = safe_read_text(batch_file)
            if not batch_text:
                continue
            if _batch_status(batch_text) != "active":
                continue
            h1_match = BATCH_FILE_H1_PATTERN.search(batch_text)
            if not h1_match:
                continue
            title = h1_match.group(1).strip()
            if title.startswith("[") and title.endswith("]"):
                continue
            if _has_unticked_files(batch_text):
                return title

    return None


def format_mid_build_block(batch_name):
    """Compose the additionalContext block for mid-build detection."""
    return (
        "- **Active build in progress.** The batch \""
        + batch_name
        + "\" has `Status: active` with files still unticked — a build "
        "is mid-progress (likely in another session).\n\n"
        "  **Ask the user:** \"A build of *" + batch_name + "* is in "
        "progress — are you resuming this build, or working in parallel?\" "
        "Parallel builds corrupt file state and git history. If resuming, "
        "confirm and continue the build. If working in parallel, only "
        "ideation is safe (writes only to the Ideas section of BACKLOG). "
        "Planning and deliberation carry git risks."
    )


def format_unclosed_build_block(batch_name):
    """Compose the additionalContext block for unclosed-build detection."""
    return (
        "- **Unclosed build detected.** The batch \""
        + batch_name
        + "\" has `Status: active` with all files ticked — the build "
        "finished but `/sovclose` was never run. `/sovclose` handles "
        "MANIFEST updates, TEST-LOG rows, build-log entry, doc-parity "
        "check, and status transition to shipped.\n\n"
        "  **Required action.** Prompt the user to run `/sovclose` before "
        "starting any new work. Do not start a new planning session or "
        "build batch until the close completes."
    )


# --- Build-snapshot detection (V90) ---


def detect_build_snapshot(project_root: Path, resolved: dict):
    """Check for _method/active-build.md — the build-snapshot signal.

    Returns a tuple (state, batch_name) where state is one of:
      None        — no snapshot exists (no build in progress)
      "mid-build" — snapshot exists, some Files: unticked
      "unclosed"  — snapshot exists, all Files: ticked (build done, close skipped)

    Falls back to the legacy Status: active detection in BACKLOG when no
    snapshot exists (for projects that haven't yet run /sovbuild under V90+)."""
    method_dir = project_root / METHOD_DIR
    snapshot_path = method_dir / "active-build.md"
    snapshot_text = safe_read_text(snapshot_path)
    if snapshot_text is None:
        return None, None

    h1_match = BATCH_FILE_H1_PATTERN.search(snapshot_text)
    batch_name = h1_match.group(1).strip() if h1_match else "unknown batch"

    total = len(BATCH_FILES_ENTRY_PATTERN.findall(snapshot_text))
    if total == 0:
        return "mid-build", batch_name

    unticked = len(BATCH_FILES_UNTICKED_PATTERN.findall(snapshot_text))
    if unticked > 0:
        return "mid-build", batch_name
    return "unclosed", batch_name


def format_snapshot_mid_build_block(batch_name):
    """Compose the additionalContext block for snapshot-based mid-build detection."""
    return (
        "- **Active build in progress (snapshot).** The file "
        "`_method/active-build.md` exists with unticked files — batch \""
        + batch_name
        + "\" is mid-build.\n\n"
        "  **Ask the user:** \"A build of *" + batch_name + "* is in "
        "progress — are you resuming this build, or working in parallel?\" "
        "If resuming, invoke `/sovbuild` to continue. If working in parallel, "
        "BACKLOG is unlocked — `/sovplan`, `/sovdeliberate`, and `/sovideate` "
        "are safe."
    )


def format_snapshot_unclosed_block(batch_name):
    """Compose the additionalContext block for snapshot-based unclosed-build detection."""
    return (
        "- **Unclosed build detected (snapshot).** The file "
        "`_method/active-build.md` exists with all files ticked — batch \""
        + batch_name
        + "\" finished but `/sovclose` was never run. `/sovclose` writes "
        "the batch back to BACKLOG as shipped, updates MANIFEST, writes "
        "TEST-LOG rows, and deletes the snapshot.\n\n"
        "  **Required action.** Prompt the user to run `/sovclose` before "
        "starting any new work."
    )


# --- OQ staleness detection ---


def _extract_latest_session_number(project_root, resolved):
    """Extract the highest session number (from vNN tags) available.

    Checks the build-log index for the most recent entry's session tag.
    Returns the number as int, or None if unparseable."""
    session_id, status = identify_previous_session_from_build_log(
        project_root, resolved
    )
    if session_id is None:
        return None
    m = SESSION_TAG_NUMBER_PATTERN.search(session_id)
    return int(m.group(1)) if m else None


def _count_open_questions(backlog_data):
    """Count the total number of OQ headings in the Open Questions section.

    Returns 0 if no BACKLOG data or no Open Questions section."""
    if not backlog_data:
        return 0
    _, backlog_text = backlog_data
    section_match = OPEN_QUESTIONS_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return 0
    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]
    return len(OQ_HEADING_PATTERN.findall(section_text))


def detect_stale_open_questions(backlog_text, latest_session_number):
    """Find OQs whose Surfaced session tag is older than the threshold.

    Returns a list of dicts: [{title, surfaced_tag, sessions_ago}].
    Skips OQs whose Surfaced line doesn't contain a parseable vNN tag."""
    section_match = OPEN_QUESTIONS_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return []

    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    stale = []
    oq_matches = list(OQ_HEADING_PATTERN.finditer(section_text))
    for i, oq_match in enumerate(oq_matches):
        title = oq_match.group(1).strip()
        body_start = oq_match.end()
        body_end = (
            oq_matches[i + 1].start()
            if i + 1 < len(oq_matches)
            else len(section_text)
        )
        body = section_text[body_start:body_end]

        surfaced_match = OQ_SURFACED_PATTERN.search(body)
        if not surfaced_match:
            continue
        surfaced_text = surfaced_match.group(1).strip()
        tag_match = SESSION_TAG_NUMBER_PATTERN.search(surfaced_text)
        if not tag_match:
            continue
        surfaced_number = int(tag_match.group(1))
        sessions_ago = latest_session_number - surfaced_number
        if sessions_ago >= OQ_STALENESS_THRESHOLD:
            stale.append({
                "title": title,
                "surfaced_tag": f"v{surfaced_number}",
                "sessions_ago": sessions_ago,
            })

    return stale


def format_stale_oq_block(stale_oqs):
    """Compose the additionalContext block for stale OQ detection."""
    lines = [
        "- **Stale open questions detected.** The following open questions "
        "have been sitting for " + str(OQ_STALENESS_THRESHOLD) + "+ "
        "sessions without resolution. Consider running a deliberation "
        "session to work through them:"
    ]
    for oq in stale_oqs:
        lines.append(
            f"  - \"{oq['title']}\" — surfaced {oq['surfaced_tag']} "
            f"({oq['sessions_ago']} sessions ago)"
        )
    return "\n".join(lines)


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
        candidate = project_root / METHOD_DIR / "proxies" / "build-log.md"
    if not candidate.exists():
        candidate = project_root / METHOD_DIR / "build-log" / "INDEX.md"
    if not candidate.exists():
        candidate = project_root / "build-log" / "INDEX.md"
    if not candidate.exists():
        candidate = project_root / "BUILD-LOG.md"
    if not candidate.exists():
        return None, "missing"
    text = safe_read_text(candidate)
    if text is None:
        return None, "unparseable"

    # Proxy-as-index (proxies/build-log.md) or folder INDEX.md:
    # both carry reference lines to per-build files.
    if (candidate.name.upper() == "INDEX.MD"
            or (candidate.name.lower() == "build-log.md"
                and candidate.parent.name == "proxies")):
        ref_match = BUILD_LOG_INDEX_REF_PATTERN.search(text)
        if not ref_match:
            return None, "unparseable"
        # Resolve per-build file relative to build-log/ dir.
        if candidate.parent.name == "proxies":
            build_log_dir = candidate.parent.parent / "build-log"
        else:
            build_log_dir = candidate.parent
        entry_file = build_log_dir / ref_match.group(1)
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
    """Find TEST-LOG rows from the previous build batch whose
    `Confirmed Explicitly` column is not `Yes`.

    Supports two modes:
      - Folder mode (V75+): path block points to a proxy in proxies/;
        per-session files in sibling test-log/ directory.
      - Single-file (legacy): path block points to TEST-LOG.md directly.

    Returns a tuple (unconfirmed_rows, build_log_status, session_id):
      - unconfirmed_rows: list of row dicts (possibly empty)
      - build_log_status: 'ok' | 'missing' | 'unparseable'
      - session_id: the identified session string, or None

    Returns ([], 'no_test_log', None) when TEST-LOG is missing or
    unreadable from the path block — there's nothing to trip on.

    Strict-fallback semantics apply when BUILD-LOG can't narrow:
    any row with `Confirmed Explicitly: No` counts as unconfirmed. Same
    rule as the V27 test-confirmation gate (per V26 Q3 + V27 Q4)."""
    test_log_data = resolved.get("TEST-LOG.md")
    if not test_log_data:
        return [], "no_test_log", None
    test_log_path, text = test_log_data

    if Path(test_log_path).parent.name == "proxies":
        test_log_dir = Path(test_log_path).parent.parent / "test-log"
        rows = []
        if test_log_dir.is_dir():
            try:
                for entry_file in sorted(test_log_dir.iterdir(), reverse=True):
                    if entry_file.suffix.lower() == ".md":
                        entry_text = safe_read_text(entry_file)
                        if entry_text:
                            rows.extend(parse_test_log_rows(entry_text))
            except OSError:
                pass
    else:
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

    The block is intentionally directive: it tells Claude to read and
    follow the planning procedure regardless of the opener's
    classification, because the test session is the gate. The procedure's
    first step (per planning.md → *Close the previous build's test
    session*) will walk the rows below."""
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
        "behaviours* → 'Do not start a new build batch', and per "
        "the planning procedure → *Close the previous build's test "
        "session*, the next planning session MUST close the test session "
        "via per-row read-back before any new build batch can start.\n\n"
        f"  {mode_note}\n\n"
        "  Unconfirmed rows:\n"
        f"{rows_block}\n\n"
        "  **Routing override.** Regardless of the user's opener "
        "classification (test notes / feature request / scope question / "
        "conversational), read and follow the planning procedure at "
        "`${{CLAUDE_PLUGIN_ROOT}}/docs/procedures/planning.md`. Open "
        "with: *\"Before we get to your question — N "
        "pending tests from session X to confirm. First: <test description "
        "of row 1>?\"* The procedure's first step is the per-row "
        "read-back; walk each row above asking Pass / Fail / "
        "Skipped, one at a time. Do NOT attempt to start a new build "
        "batch until the read-back closes "
        "the session — the PreToolUse hook will deny build-phase file "
        "edits if you try."
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
    /sovsetup. Pairs with the systemMessage user-visible warning."""
    parent_warning = ""
    parent_claude_dirs = detect_parent_claude_md(project_root)
    if parent_claude_dirs:
        paths_md = ", ".join(f"`{p}`" for p in parent_claude_dirs)
        parent_warning = (
            f"\n\n**Warning:** A CLAUDE.md file was found in a parent "
            f"directory ({paths_md}). Claude Code inherits CLAUDE.md files "
            "from parent directories, which may affect this session. "
            "Consider moving this project to a folder that isn't nested "
            "inside another project's tree."
        )

    return (
        "## No-code-method plugin — unadopted folder\n\n"
        "**This folder has not been adopted by the no-code-method plugin, "
        "and it contains existing work that the plugin would put at risk "
        "if you proceed normally.** No method-aware behaviour is active "
        "until the user runs `/sovsetup`.\n\n"
        f"Project root: `{project_root}`"
        + parent_warning + "\n\n"
        "**Required behaviour for this session:**\n\n"
        "- Direct the user to run `/sovsetup` before doing anything else.\n"
        "- Do NOT attempt Edit, Write, or MultiEdit "
        "tool calls. The PreToolUse hook will deny them anyway, and "
        "attempting them creates confusing churn.\n"
        "- If the user does not want the method in this folder, they can "
        "disable the plugin for this project: type `/plugin`, go to the "
        "Installed tab, and toggle it off. This is a Claude Code built-in "
        "— it stops all plugin hooks from firing in this folder.\n\n"
        "Until `/sovsetup` runs (or the plugin is disabled for this project), "
        "the only useful actions are conversational responses pointing the "
        "user toward `/sovsetup` or explaining how to disable the plugin."
    )


def build_unadopted_system_message() -> str:
    """User-visible warning text for the unadopted-with-work advisory.
    Kept short — system messages are noisier than additionalContext and
    we want this one to land."""
    return (
        "[no-code-method] Folder has work but isn't set up — run /sovsetup "
        "to start, or disable the plugin for this project via /plugin → "
        "Installed → toggle off. Edit/Write/MultiEdit calls will be "
        "denied until /sovsetup completes."
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


def detect_parent_claude_md(project_root: Path) -> list:
    """Walk up from project_root checking each parent for CLAUDE.md.
    Returns a list of parent directory paths that contain one."""
    parents = []
    current = project_root.parent
    try:
        while current != current.parent:
            if (current / "CLAUDE.md").exists():
                parents.append(current)
            current = current.parent
    except OSError:
        pass
    return parents


def format_parent_directory_warning(parents: list) -> str:
    """Compose the advisory text for parent-directory CLAUDE.md files."""
    paths_md = ", ".join(f"`{p}`" for p in parents)
    return (
        f"- **Parent-directory CLAUDE.md detected** at {paths_md}. "
        "Claude Code inherits CLAUDE.md files from parent directories — "
        "instructions from those files will affect this session. If this "
        "project is independent from the parent, consider moving it to a "
        "folder that isn't nested inside another project's tree."
    )


def build_state_summary(project_root: Path, claude_text: str, path_block: dict) -> str:
    """Compose the prose state summary for tier 3."""
    resolved, unresolved = resolve_path_block_docs(project_root, path_block)

    lines = ["## Project state (detected by SessionStart hook)", ""]

    lines.append(f"- **Project root:** `{project_root}`")

    parent_claude_dirs = detect_parent_claude_md(project_root)
    if parent_claude_dirs:
        lines.append(format_parent_directory_warning(parent_claude_dirs))

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
            "rule): recommend `/sovsetup` to seed `UX.md`, `BACKLOG.md`, "
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
            "`/sovsetup` if structural drift is suspected (case 3 — migrate "
            "to current spec), or update the footers if the content is "
            "current."
        )

    backlog_data = resolved.get("BACKLOG.md")
    top_batch = None
    batch_details = None
    batch_counts = None
    top_queued = []
    unclosed_batch = None
    mid_build_batch = None
    if backlog_data:
        backlog_resolved_path, backlog_text = backlog_data
        top_batch = detect_top_build_batch(backlog_text, backlog_resolved_path)
        batch_details = detect_top_batch_details(
            backlog_text, backlog_resolved_path
        )
        batch_counts = count_batch_statuses(
            backlog_text, backlog_resolved_path
        )
        top_queued = detect_top_queued_batches(
            backlog_text, backlog_resolved_path
        )
        if top_batch:
            lines.append(
                f"- **Top build batch in BACKLOG:** \"{top_batch}\". If "
                "the user's opener implies resume (test notes pointing at "
                "this batch, a 'continue where we left off' phrasing, etc.) "
                "default to resume per `universal-behaviour.md` → *Routing "
                "main-Claude's openers* (the unfinished-top-batch row). "
                "Confirm with the user before continuing the build."
            )

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

    # Build-snapshot detection (V90) — check _method/active-build.md first.
    snapshot_state, snapshot_batch = detect_build_snapshot(
        project_root, resolved
    )
    if snapshot_state == "unclosed":
        lines.append(format_snapshot_unclosed_block(snapshot_batch))
        unclosed_batch = snapshot_batch
    elif snapshot_state == "mid-build":
        lines.append(format_snapshot_mid_build_block(snapshot_batch))
        mid_build_batch = snapshot_batch

    # Legacy fallback: Status: active in BACKLOG (pre-V90 projects).
    if backlog_data and snapshot_state is None:
        unclosed_batch = detect_unclosed_build(
            backlog_text, backlog_resolved_path
        )
        if unclosed_batch:
            lines.append(format_unclosed_build_block(unclosed_batch))

        mid_build_batch = detect_mid_build(
            backlog_text, backlog_resolved_path
        )
        if mid_build_batch:
            lines.append(format_mid_build_block(mid_build_batch))

    # OQ staleness detection.
    stale_oqs = []
    if backlog_data:
        _backlog_path, backlog_text = backlog_data
        latest_session = _extract_latest_session_number(
            project_root, resolved
        )
        if latest_session is not None:
            stale_oqs = detect_stale_open_questions(
                backlog_text, latest_session
            )
            if stale_oqs:
                lines.append(format_stale_oq_block(stale_oqs))

    # V27 TEST-LOG tripwire.
    unconfirmed_rows, build_log_status, session_id = detect_unconfirmed_test_rows(
        project_root, resolved
    )
    if unconfirmed_rows:
        lines.append(
            format_test_log_tripwire_block(
                unconfirmed_rows, build_log_status, session_id
            )
        )

    # V74: User-facing session-open status summary.
    lines.append("")
    lines.append("## Session-open status (present to user)")
    lines.append("")
    lines.append(
        "**Mandatory.** Present the following status summary to the user "
        "as your first output in every session — before routing, before "
        "asking questions, before any other action. Keep it concise (the "
        "block below is the ceiling, not a minimum). If batch counts are "
        "zero, say so plainly."
    )
    lines.append("")

    status_lines = []
    if batch_counts:
        parts = []
        active_count = batch_counts["active"]
        if snapshot_state is not None:
            active_count += 1
        if active_count:
            parts.append(f"{active_count} active")
        if batch_counts["queued"]:
            parts.append(f"{batch_counts['queued']} queued")
        if batch_counts["parked"]:
            parts.append(f"{batch_counts['parked']} parked")
        if parts:
            status_lines.append(f"Build batches: {', '.join(parts)}.")
        else:
            status_lines.append("Build batches: none.")
    elif snapshot_state is not None:
        status_lines.append("Build batches: 1 active (in snapshot).")
    else:
        status_lines.append("Build batches: BACKLOG not found or empty.")

    if batch_details:
        goal_part = f" — {batch_details['goal']}" if batch_details["goal"] else ""
        file_part = (
            f" ({batch_details['file_count']} files)"
            if batch_details["file_count"]
            else ""
        )
        status_lines.append(
            f"Next up: \"{batch_details['name']}\"{goal_part}{file_part}."
        )

    if top_queued:
        has_active = batch_counts and batch_counts.get("active", 0) > 0
        upcoming = top_queued if has_active else top_queued[1:]
        if upcoming:
            status_lines.append("Coming up:")
            for tq in upcoming:
                goal_part = f" — {tq['goal']}" if tq.get("goal") else ""
                status_lines.append(f"  - \"{tq['name']}\"{goal_part}")

    if unconfirmed_rows:
        status_lines.append(
            f"Pending tests: {len(unconfirmed_rows)} unconfirmed from "
            "previous build (must close before next build)."
        )

    if backlog_data and red_flags:
        status_lines.append(
            f"Red flags: {len(red_flags)} deferred concern(s) to acknowledge."
        )

    if unclosed_batch:
        status_lines.append(
            f"Unclosed build: \"{unclosed_batch}\" — run /sovclose to complete."
        )

    if mid_build_batch:
        status_lines.append(
            f"Active build: \"{mid_build_batch}\" in progress — "
            "resuming or working in parallel?"
        )

    if stale_oqs:
        status_lines.append(
            f"Stale open questions: {len(stale_oqs)} older than "
            f"{OQ_STALENESS_THRESHOLD} sessions."
        )

    # V90: OQ accumulation nudge — suggest /sovdeliberate when OQs pile up.
    oq_count = _count_open_questions(backlog_data)
    if oq_count >= 3 or stale_oqs:
        nudge_parts = []
        if oq_count >= 3:
            nudge_parts.append(f"{oq_count} open questions")
        if stale_oqs:
            oldest = min(oq["surfaced_tag"] for oq in stale_oqs)
            nudge_parts.append(f"oldest from {oldest}")
        status_lines.append(
            f"OQ nudge: {', '.join(nudge_parts)} — consider /sovdeliberate."
        )

    status_lines.append("Ready to proceed?")

    lines.append("```")
    for sl in status_lines:
        lines.append(sl)
    lines.append("```")

    lines.append("")
    lines.append(
        "**Routing.** After presenting the status, read the user's opening "
        "message and route per `universal-behaviour.md` → *Routing "
        "openers*. This hook does not classify the user's "
        "opener — that's your call based on the user's words and the "
        "structural state listed above. For each phase, read and follow "
        "the matching procedure doc at "
        "`${CLAUDE_PLUGIN_ROOT}/docs/procedures/<phase>.md`. "
        "Exception: when the TEST-LOG "
        "tripwire above fires, the routing override there takes precedence."
    )

    return "\n".join(lines)


# --- Tier 2 output ---

def build_tier_2_gap_flag(claude_text, spine_docs, project_root=None) -> str:
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
            "`/sovsetup` to bring an existing project up to spec."
        )
    elif not has_claude and spine_docs:
        gap = (
            f"Spine docs ({spine_names}) carrying the method footer are "
            "present at the project root, but `CLAUDE.md` is missing. The "
            "plugin's hooks rely on `CLAUDE.md`'s path block to locate the "
            "spine docs."
        )
        next_step = (
            "Run `/sovsetup` to bring this project up to spec — it will "
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
            "run `/sovsetup` to bring everything up to spec."
        )
    else:
        gap = (
            "Some method-shaped files were found but the project structure "
            "is incomplete."
        )
        next_step = "Run `/sovsetup` — it routes to the right case across new-project, migration, and refresh."

    parent_warning = ""
    if project_root is not None:
        parent_claude_dirs = detect_parent_claude_md(project_root)
        if parent_claude_dirs:
            parent_warning = "\n\n" + format_parent_directory_warning(parent_claude_dirs)

    return (
        "## No-code-method project state\n\n"
        f"**Partial method shape detected.** {gap}\n\n"
        f"{next_step} No method-aware behaviour beyond the universal "
        "rules above is available until the project's structure is complete."
        + parent_warning
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
        # folders. They stay silent — unless a parent-directory CLAUDE.md
        # is detected, which could poison the session (V71).
        parent_claude_dirs = detect_parent_claude_md(project_root)
        if parent_claude_dirs:
            return emit_context(format_parent_directory_warning(parent_claude_dirs))
        return 0

    # Tier 2 and tier 3 both get the universal rules. The tier-specific
    # state summary is appended after.
    universal_rules = read_universal_rules()

    if tier == 2:
        tier_output = build_tier_2_gap_flag(claude_text, spine_docs, project_root)
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
