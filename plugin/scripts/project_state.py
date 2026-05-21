#!/usr/bin/env python3
"""
project_state.py — shared helpers for reading project state from disk.

Used by the no-code-method plugin's hooks (pre_tool_use.py, stop.py — and
potentially future hooks, subagents, or skills) to read the project's
state files in a consistent way: CLAUDE.md's path block, BACKLOG.md (via
the parse_backlog.py subprocess), TEST-LOG.md, and BUILD-LOG.md.

Centralised here so the V27 test-confirmation gate logic in pre_tool_use.py
and the V28 TEST-LOG-aware Stop hook in stop.py share one definition of
"how do we know what the project state is right now."

The helpers are all lenient — any I/O or parse failure returns None or
an empty collection rather than raising. Callers (the hooks) treat
lenient-failure as "no signal, fall through to allow" so that a hook
which can't deterministically decide doesn't surprise the user with a
spurious deny.

Mechanisms referenced:
  - Path block format: CLAUDE-TEMPLATE.md (a fenced JSON code block in
    CLAUDE.md mapping logical names → relative paths).
  - TEST-LOG.md row shape: DOC-STRUCTURE.md → *TEST-LOG.md structure*
    (the 8-column data row).
  - BUILD-LOG.md session-heading convention: DOC-STRUCTURE.md →
    *BUILD-LOG.md structure* (newest-first, `## <session-tag>` heading
    at the top of the file).

History:
  - V19 introduced extract_path_block (in pre_tool_use.py).
  - V25 added run_parser as a third caller of parse_backlog.py, with a
    duplicate copy in stop.py — comments noted the extraction was due.
  - V27 added the TEST-LOG / BUILD-LOG helpers (in pre_tool_use.py).
  - V28 extracted everything to this module so stop.py could become
    TEST-LOG-aware without a third copy.
  - V29 added the adoption-state primitives (FOOTER_PATTERN,
    has_method_footer, and the unadopted-folder detection helpers) so
    SessionStart and PreToolUse share one source of truth for "is this
    folder method-managed."
"""

import json
import re
import subprocess
from pathlib import Path


# CLAUDE.md's path block is the first fenced JSON code block in the file.
# Match the contents between the opening ```json line and the closing ```.
PATH_BLOCK_PATTERN = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

# Path to the shared BACKLOG.md parser, resolved relative to THIS module.
# project_state.py lives in plugin/scripts/; parse_backlog.py is alongside.
PARSER_PATH = Path(__file__).parent / "parse_backlog.py"

# Timeout for the parser subprocess call. Insurance against a stuck
# process, not a tuning parameter — the parser runs in milliseconds on
# real input.
PARSER_TIMEOUT_SECONDS = 10

# Match a TEST-LOG.md data row in the 8-column table format.
# Header and separator rows don't match because they don't start with
# a numeric ID.
TEST_LOG_DATA_ROW_PATTERN = re.compile(
    r"^\|\s*(\d+)\s*\|"     # # (numeric ID)
    r"\s*([^|]*?)\s*\|"      # Date
    r"\s*([^|]*?)\s*\|"      # Session
    r"\s*([^|]*?)\s*\|"      # Component
    r"\s*([^|]*?)\s*\|"      # Test Description
    r"\s*([^|]*?)\s*\|"      # Status
    r"\s*([^|]*?)\s*\|"      # Confirmed Explicitly
    r"\s*([^|]*?)\s*\|",     # User Notes
    re.MULTILINE,
)

# BUILD-LOG.md's first `## <token>` heading names the latest (newest-first)
# session. The capture is intentionally permissive — the dev-side
# convention is `## V27 — YYYY-MM-DD — summary`, but a consumer project
# may use any session-tag shape. We just need a string that matches the
# corresponding Session column in TEST-LOG.md.
BUILD_LOG_SESSION_HEADING_PATTERN = re.compile(r"^##\s+(\S+)", re.MULTILINE)

# --- V29 adoption-state primitives ---
#
# Together these answer: is this folder method-managed (adopted)? If not,
# does it have substantial pre-existing work that the plugin would put at
# risk? Both hooks (SessionStart for advisory; PreToolUse for enforcement)
# call into this section.

# The `*No-code method — Version N.*` footer line that every method-side
# file and template carries. Presence of this line in CLAUDE.md is the
# canonical adoption marker — a folder is "adopted" iff its CLAUDE.md
# carries this footer.
FOOTER_PATTERN = re.compile(r"\*No-code method — Version (\d+)\.\*")

# Build-manifest filenames the Q2 detection rule (V29 open question 2)
# treats as definitive "substantial work" signals at the project root.
# Language-agnostic list covering major ecosystems. Presence of any one
# of these alone is enough to trigger the unadopted-with-work advisory
# / enforcement.
BUILD_MANIFEST_NAMES = frozenset({
    "package.json",
    "pyproject.toml",
    "Cargo.toml",
    "build.gradle",
    "build.gradle.kts",
    "Gemfile",
    "pom.xml",
    "go.mod",
    "composer.json",
    "requirements.txt",
    "setup.py",
})

# Recognized source directory names. Presence of any of these at project
# root triggers on its own.
SOURCE_DIR_NAMES = frozenset({"src", "lib", "app"})

# Infrastructure files and directories excluded from the "substantial
# work" file count. Tuned for the no-code-method's typical environment
# (Obsidian is common on Alex's setup).
INFRA_NAMES = frozenset({
    ".git",
    ".gitignore",
    "README.md",
    "LICENSE",
    "LICENSE.md",
    ".obsidian",
    ".no-code-method-skip",
})

# Q2 rule (d) threshold: more than this many non-infra files (recursively,
# skipping INFRA_NAMES at every depth) triggers.
SUBSTANTIAL_WORK_FILE_THRESHOLD = 5


def has_method_footer(text):
    """True if `text` carries the `*No-code method — Version N.*` footer.
    The trust marker for adoption — a folder is adopted iff its CLAUDE.md
    carries this. Used as the primary adoption check by both hooks."""
    if not isinstance(text, str):
        return False
    return bool(FOOTER_PATTERN.search(text))


def extract_footer_version(text):
    """Return the integer version from the footer, or None if not found."""
    if not isinstance(text, str):
        return None
    match = FOOTER_PATTERN.search(text)
    if not match:
        return None
    try:
        return int(match.group(1))
    except ValueError:
        return None


def _count_non_infra_files_exceeds(project_root, threshold):
    """V29 Q2 rule (d) helper. Walk project_root and return True as soon
    as the count of non-infra files exceeds `threshold`. Bounded: stops
    walking the moment the threshold is crossed. Skips INFRA_NAMES at
    every level (so `.git/`, `.obsidian/`, etc. don't contribute to the
    count and aren't recursed into)."""
    count = 0
    stack = [Path(project_root)]
    while stack:
        d = stack.pop()
        try:
            entries = list(d.iterdir())
        except OSError:
            continue
        for e in entries:
            if e.name in INFRA_NAMES:
                continue
            try:
                if e.is_file():
                    count += 1
                    if count > threshold:
                        return True
                elif e.is_dir():
                    stack.append(e)
            except OSError:
                continue
    return False


def has_substantial_work(project_root, claude_text):
    """V29 Q2 detection rule. True if the project root looks like real
    pre-existing work and is not yet method-adopted.

    Caller has already confirmed claude_text either is None (no CLAUDE.md)
    or lacks the method footer (foreign CLAUDE.md). Triggers if ANY of:

      (a) a build-manifest file at root (BUILD_MANIFEST_NAMES)
      (b) a recognized source directory at root (SOURCE_DIR_NAMES)
      (c) a foreign CLAUDE.md present (claude_text is not None)
      (d) more than SUBSTANTIAL_WORK_FILE_THRESHOLD non-infra files
          (recursively, skipping INFRA_NAMES at every depth)

    Conservative bias: false positives are minor friction (the user runs
    /setup and can opt out via cancel/leave-alone); false negatives are
    catastrophic (plugin scaffolds over existing work)."""

    # (c) Foreign CLAUDE.md is a trigger on its own.
    if claude_text is not None:
        return True

    root = Path(project_root)
    try:
        root_entries = list(root.iterdir())
    except OSError:
        return False

    # (a) and (b) — single-pass over project root's direct children.
    for e in root_entries:
        try:
            if e.is_file() and e.name in BUILD_MANIFEST_NAMES:
                return True
            if e.is_dir() and e.name in SOURCE_DIR_NAMES:
                return True
        except OSError:
            continue

    # (d) — bounded recursive file count.
    return _count_non_infra_files_exceeds(
        root, SUBSTANTIAL_WORK_FILE_THRESHOLD
    )


_LEGACY_SKIP_MARKER = ".no-code-method-skip"


def is_unadopted_with_work(project_root):
    """V29 entry point for the adoption check.

    True iff the folder is unadopted (no method footer in CLAUDE.md) AND
    has substantial work. Adopted folders and genuinely-empty unadopted
    folders return False. Per-project opt-out is handled by Claude Code's
    built-in plugin disable (``/plugin`` → Installed → toggle off), which
    prevents the plugin's hooks from firing at all.

    Legacy: the dev project (sovereign-implementer/) keeps a
    .no-code-method-skip file at its root because --plugin-dir plugins
    don't appear in /plugin's Installed tab. This check honours that
    file so the advisory stays quiet during dev sessions.

    Drives SessionStart's advisory emission and PreToolUse's enforcement
    gate. Both hooks call this function — same definition of "unadopted"
    everywhere."""
    root = Path(project_root)

    if (root / _LEGACY_SKIP_MARKER).is_file():
        return False

    claude_text = safe_read_text(root / "CLAUDE.md")

    # Adopted: CLAUDE.md present with method footer.
    if claude_text is not None and has_method_footer(claude_text):
        return False

    return has_substantial_work(root, claude_text)


# V29 /setup case numbers — kept here as named constants so scaffold.py
# and the subagent body don't have to reproduce the magic numbers.
ADOPT_CASE_EMPTY = 1                  # genuinely empty folder
ADOPT_CASE_CODE_NO_DOCS = 2           # existing code, no method docs
ADOPT_CASE_CODE_FOREIGN_DOCS = 3      # existing code, foreign CLAUDE.md
ADOPT_CASE_ALREADY_ADOPTED = 4        # method-footered CLAUDE.md


def detect_adopt_case(project_root):
    """V29/V44: classify the project root into one of /setup's four cases.

    Returns an integer 1–4 corresponding to ADOPT_CASE_* constants:

      1 — empty folder (no CLAUDE.md, no substantial work)
      2 — existing code, no method docs (no CLAUDE.md, substantial work)
      3 — existing code, foreign docs (CLAUDE.md present, no method footer)
      4 — already method-managed (CLAUDE.md present with method footer)

    Per-project opt-out is handled by Claude Code's built-in plugin
    disable (``/plugin`` → Installed → toggle off), which prevents the
    plugin's hooks from firing at all — no case needed here.

    Used by the /setup subagent (case dispatch) and by the scaffold.py
    `detect-case` command. SessionStart and PreToolUse use the coarser
    `is_unadopted_with_work` since they only need yes/no, not the
    specific case."""
    root = Path(project_root)

    claude_text = safe_read_text(root / "CLAUDE.md")

    if claude_text is not None and has_method_footer(claude_text):
        return ADOPT_CASE_ALREADY_ADOPTED

    if claude_text is not None:
        # Foreign CLAUDE.md present (no method footer). This is always
        # case 3 regardless of whether the rest of the folder is empty —
        # an out-of-spec CLAUDE.md is itself the thing to handle.
        return ADOPT_CASE_CODE_FOREIGN_DOCS

    # No CLAUDE.md. Distinguish empty from substantial-work via the Q2 rule.
    if has_substantial_work(root, None):
        return ADOPT_CASE_CODE_NO_DOCS

    return ADOPT_CASE_EMPTY


def safe_read_text(path):
    """Read text from path; return None on any IO/decoding failure."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def extract_path_block(claude_md_text):
    """Extract and parse the first fenced JSON code block from CLAUDE.md.

    Returns the parsed dict, or None if the block is missing or
    unparseable, or if the parsed JSON isn't a dict.
    """
    if not isinstance(claude_md_text, str):
        return None
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


def resolve_path_block_entry(project_root, logical_name):
    """Read CLAUDE.md from project_root, parse its path block, and resolve
    a logical name (e.g. 'UX.md', 'TEST-LOG.md') to its absolute Path.

    Returns Path on success, None on any failure (missing CLAUDE.md,
    unparseable path block, logical_name not in the block, OSError on
    resolution). Generalised helper used wherever a hook needs to find
    a specific spine doc by name.
    """
    text = safe_read_text(Path(project_root) / "CLAUDE.md")
    if text is None:
        return None
    path_block = extract_path_block(text)
    if not path_block:
        return None
    rel = path_block.get(logical_name)
    if not isinstance(rel, str) or not rel:
        return None
    try:
        return (Path(project_root) / rel).resolve()
    except OSError:
        return None


def run_parser(backlog_path):
    """Invoke parse_backlog.py with backlog_path. Returns the parser's
    parsed JSON output (dict).

    Returns None on any failure: parser script missing, subprocess error,
    non-zero exit, empty stdout, invalid JSON. Callers (pre_tool_use.py's
    batch-boundary check, stop.py's redirect decision, and the /build
    slash-command) treat None as "no top batch to act on."
    """
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


def parse_test_log_rows(text):
    """Parse TEST-LOG.md text into a list of row dicts.

    Each dict has keys: id, date, session, component, description, status,
    confirmed_explicitly, user_notes. Whitespace inside cells is trimmed.
    Returns an empty list if the file has no data rows. Malformed rows
    are silently skipped — the parser is lenient, the caller only acts
    on rows it can definitively identify.
    """
    if not isinstance(text, str):
        return []
    rows = []
    for m in TEST_LOG_DATA_ROW_PATTERN.finditer(text):
        rows.append({
            "id": m.group(1).strip(),
            "date": m.group(2).strip(),
            "session": m.group(3).strip(),
            "component": m.group(4).strip(),
            "description": m.group(5).strip(),
            "status": m.group(6).strip(),
            "confirmed_explicitly": m.group(7).strip(),
            "user_notes": m.group(8).strip(),
        })
    return rows


def is_row_confirmed(row):
    """A row is confirmed iff its `Confirmed Explicitly` cell starts with
    `Yes`. Anything else — `No`, blank, or an unrecognised value — counts
    as not confirmed.

    Per Rule 1 (Never infer completion): absence-of-Yes is treated as
    not-confirmed, not as a tacit pass.
    """
    if not isinstance(row, dict):
        return False
    ce = row.get("confirmed_explicitly", "")
    if not isinstance(ce, str):
        return False
    return ce.strip().startswith("Yes")


def identify_previous_session(project_root):
    """Try to identify the previous build batch's session from BUILD-LOG.md.

    Returns a tuple (session_id, status) where status is one of:
      - 'ok' — BUILD-LOG.md found and a session heading parsed
      - 'missing' — BUILD-LOG.md not present in the path block or at
        project root
      - 'unparseable' — BUILD-LOG.md present but no `## <token>` heading
        could be matched

    BUILD-LOG.md is a per-project dev-internal record; consumer projects
    may not keep one. The lookup tries the path block first, then the
    project root as a convention fallback.
    """
    candidate = resolve_path_block_entry(project_root, "BUILD-LOG.md")
    if candidate is None or not candidate.exists():
        candidate = Path(project_root) / "BUILD-LOG.md"
    if not candidate.exists():
        return None, "missing"
    text = safe_read_text(candidate)
    if text is None:
        return None, "unparseable"
    match = BUILD_LOG_SESSION_HEADING_PATTERN.search(text)
    if not match:
        return None, "unparseable"
    return match.group(1).strip(), "ok"


def get_unconfirmed_previous_session_rows(project_root):
    """Read TEST-LOG.md and identify rows from the previous build batch's
    session that are not yet confirmed.

    Returns a tuple (rows, build_log_status, session_id):
      - rows: list of row dicts — the unconfirmed previous-session rows.
        Empty if no unconfirmed rows exist (test session closed) OR
        TEST-LOG.md is missing, unreadable, or empty.
      - build_log_status: 'ok' / 'missing' / 'unparseable' (per
        identify_previous_session). 'missing' is also returned when
        TEST-LOG.md itself can't be resolved or read — the distinction
        between "TEST-LOG missing" and "BUILD-LOG missing" doesn't matter
        to callers (rows is empty in the TEST-LOG-missing case anyway).
      - session_id: the previous session's ID (str) when BUILD-LOG could
        narrow, otherwise None.

    When BUILD-LOG can't narrow (status 'missing' or 'unparseable') AND
    TEST-LOG has rows, the returned rows include every unconfirmed row
    across all sessions — strict fallback per V26 Q3 + V27 Q4
    (safety-by-default: if we can't be sure which session each row belongs
    to, any unconfirmed row signals an open test session).

    Callers:
      - pre_tool_use.py's check_test_confirmation_gate (V27): denies the
        Task → batch-executor invocation when this returns non-empty rows.
      - stop.py's main (V28): exits silent when this returns non-empty
        rows, deferring the batch-executor redirect until the test session
        closes.
    """
    test_log_path = resolve_path_block_entry(project_root, "TEST-LOG.md")
    if test_log_path is None or not test_log_path.exists():
        return [], "missing", None
    text = safe_read_text(test_log_path)
    if text is None:
        return [], "missing", None
    rows = parse_test_log_rows(text)
    if not rows:
        return [], "ok", None

    session_id, build_log_status = identify_previous_session(project_root)
    if build_log_status == "ok":
        unconfirmed = [
            r for r in rows
            if r["session"] == session_id and not is_row_confirmed(r)
        ]
    else:
        unconfirmed = [r for r in rows if not is_row_confirmed(r)]
    return unconfirmed, build_log_status, session_id


def is_test_session_open(project_root):
    """Convenience boolean wrapper around get_unconfirmed_previous_session_rows.

    Returns True iff TEST-LOG.md has at least one unconfirmed previous-session
    row. Returns False on any of the lenient cases: missing or unreadable
    TEST-LOG, empty TEST-LOG, all rows confirmed.

    Used by stop.py (V28) to decide whether to defer the batch-executor
    redirect. The behaviour mirrors the test-confirmation gate's allow/deny
    decision: gate denies iff this would return True.
    """
    unconfirmed, _, _ = get_unconfirmed_previous_session_rows(project_root)
    return bool(unconfirmed)
