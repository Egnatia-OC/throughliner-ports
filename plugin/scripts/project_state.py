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
  - Path block format: NO-CODE-METHOD.md → *At session start* (a fenced
    JSON code block in CLAUDE.md mapping logical names → relative paths).
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
