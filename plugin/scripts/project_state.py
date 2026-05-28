#!/usr/bin/env python3
"""
project_state.py — shared helpers for reading project state from disk.

Used by the no-code-method plugin's hooks (pre_tool_use.py, session_start.py,
and others) to read the project's state files in a consistent way: CLAUDE.md's
path block, BUILD-PLAN.md (via the parse_backlog.py subprocess), TEST-LOG.md,
and build-log/.

Centralised here so state-reading logic is defined once and shared across
all hooks that need project state.

The helpers are all lenient — any I/O or parse failure returns None or
an empty collection rather than raising. Callers (the hooks) treat
lenient-failure as "no signal, fall through to allow" so that a hook
which can't deterministically decide doesn't surprise the user with a
spurious deny.

Mechanisms referenced:
  - Path block format: CLAUDE-TEMPLATE.md (a fenced JSON code block in
    CLAUDE.md mapping logical names → relative paths).
  - TEST-LOG.md row shape: DOC-STRUCTURE.md → *TEST-LOG.md structure*
    (10-column data row as of V48; backwards-compatible with 8-column
    pre-V48 rows).
  - Build log session-heading convention: DOC-STRUCTURE.md →
    *Build log structure* (folder mode: per-build file with `# <session-tag>`
    heading; legacy single-file: `## <session-tag>` heading).

History:
  - V19 introduced extract_path_block (in pre_tool_use.py).
  - V25 added run_parser as a third caller of parse_backlog.py, with a
    duplicate copy in stop.py — comments noted the extraction was due.
  - V27 added the TEST-LOG / build-log helpers (in pre_tool_use.py).
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

# Path to the shared BUILD-PLAN.md parser, resolved relative to THIS module.
# project_state.py lives in plugin/scripts/; parse_backlog.py is alongside.
PARSER_PATH = Path(__file__).parent / "parse_backlog.py"

# Timeout for the parser subprocess call. Insurance against a stuck
# process, not a tuning parameter — the parser runs in milliseconds on
# real input.
PARSER_TIMEOUT_SECONDS = 10

# Match a TEST-LOG.md data row in the 10-column table format (V48+).
# Also matches the legacy 8-column format (pre-V48) — the last two
# groups (Type, Verifier) will be empty strings for 8-column rows.
# Header and separator rows don't match because they don't start with
# a numeric ID.
TEST_LOG_DATA_ROW_PATTERN = re.compile(
    r"^\|\s*(\d+)\s*\|"     # # (numeric ID)
    r"\s*([^|]*?)\s*\|"      # Date
    r"\s*([^|]*?)\s*\|"      # Session
    r"\s*([^|]*?)\s*\|"      # Component
    r"\s*([^|]*?)\s*\|"      # Test Description
    r"(?:\s*([^|]*?)\s*\|"   # Type (V48+, optional group)
    r"\s*([^|]*?)\s*\|)?"    # Verifier (V48+, optional group)
    r"\s*([^|]*?)\s*\|"      # Status
    r"\s*([^|]*?)\s*\|"      # Confirmed Explicitly
    r"\s*([^|]*?)\s*\|",     # Notes
    re.MULTILINE,
)

# BUILD-LOG session heading patterns. Two formats:
#   Single-file (legacy): `## <token> — YYYY-MM-DD — summary`
#   Per-build file (V50+): `# <token> — YYYY-MM-DD — summary`
# The capture is intentionally permissive — a consumer project may use
# any session-tag shape. We just need a string that matches the
# corresponding Session column in TEST-LOG.md.
BUILD_LOG_SESSION_HEADING_PATTERN = re.compile(r"^##\s+(\S+)", re.MULTILINE)
BUILD_LOG_ENTRY_HEADING_PATTERN = re.compile(r"^#\s+(\S+)", re.MULTILINE)

# build-log/ INDEX.md reference line: `- `NNN-name.md` — ...`
BUILD_LOG_INDEX_REF_PATTERN = re.compile(r"^-\s+`(\d{3}-.+?\.md)`", re.MULTILINE)

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
    /sovsetup and can opt out via cancel/leave-alone); false negatives are
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


# V29 /sovsetup case numbers — kept here as named constants so scaffold.py
# and the setup procedure don't have to reproduce the magic numbers.
ADOPT_CASE_EMPTY = 1                  # genuinely empty folder
ADOPT_CASE_CODE_NO_DOCS = 2           # existing code, no method docs
ADOPT_CASE_CODE_FOREIGN_DOCS = 3      # existing code, foreign CLAUDE.md
ADOPT_CASE_ALREADY_ADOPTED = 4        # method-footered CLAUDE.md


def detect_adopt_case(project_root):
    """V29/V44: classify the project root into one of /sovsetup's four cases.

    Returns an integer 1–4 corresponding to ADOPT_CASE_* constants:

      1 — empty folder (no CLAUDE.md, no substantial work)
      2 — existing code, no method docs (no CLAUDE.md, substantial work)
      3 — existing code, foreign docs (CLAUDE.md present, no method footer)
      4 — already method-managed (CLAUDE.md present with method footer)

    Per-project opt-out is handled by Claude Code's built-in plugin
    disable (``/plugin`` → Installed → toggle off), which prevents the
    plugin's hooks from firing at all — no case needed here.

    Used by the /sovsetup procedure (case dispatch) and by the scaffold.py
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
        return Path(path).read_text(encoding="utf-8-sig")
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
    batch-boundary and test-confirmation checks, and the /sovbuild slash-
    command) treat None as "no top batch to act on."
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

    Each dict has keys: id, date, session, component, description, type,
    verifier, status, confirmed_explicitly, notes. Whitespace inside cells
    is trimmed. Handles both 10-column (V48+) and legacy 8-column formats.
    For 8-column rows, type defaults to "Look and click" and verifier to
    "User". Returns an empty list if the file has no data rows. Malformed
    rows are silently skipped.
    """
    if not isinstance(text, str):
        return []
    rows = []
    for m in TEST_LOG_DATA_ROW_PATTERN.finditer(text):
        test_type = (m.group(6) or "").strip() if m.group(6) is not None else "Look and click"
        verifier = (m.group(7) or "").strip() if m.group(7) is not None else "User"
        if not test_type:
            test_type = "Look and click"
        if not verifier:
            verifier = "User"
        rows.append({
            "id": m.group(1).strip(),
            "date": m.group(2).strip(),
            "session": m.group(3).strip(),
            "component": m.group(4).strip(),
            "description": m.group(5).strip(),
            "type": test_type,
            "verifier": verifier,
            "status": m.group(8).strip(),
            "confirmed_explicitly": m.group(9).strip(),
            "notes": m.group(10).strip(),
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
    """Try to identify the previous build batch's session from the build log.

    Supports two formats:
      - Folder mode (V50+): path block points to `build-log/INDEX.md`.
        Reads the first reference line, opens the referenced per-build
        file, parses its `# <token>` heading.
      - Single-file (legacy): path block points to `BUILD-LOG.md`.
        Parses the first `## <token>` heading directly.

    Returns a tuple (session_id, status) where status is one of:
      - 'ok' — build log found and a session heading parsed
      - 'missing' — build log not present in the path block or at
        project root
      - 'unparseable' — build log present but no session heading could
        be matched
    """
    candidate = resolve_path_block_entry(project_root, "BUILD-LOG.md")
    if candidate is None or not candidate.exists():
        candidate = Path(project_root) / "BUILD-LOG.md"
    if not candidate.exists():
        build_log_dir = Path(project_root) / "build-log" / "INDEX.md"
        if build_log_dir.exists():
            candidate = build_log_dir
        else:
            build_log_dir = Path(project_root) / "_method" / "build-log" / "INDEX.md"
            if build_log_dir.exists():
                candidate = build_log_dir
            else:
                return None, "missing"
    text = safe_read_text(candidate)
    if text is None:
        return None, "unparseable"

    is_index = (candidate.name.upper() == "INDEX.MD"
                or (candidate.name.lower() == "build-log.md"
                    and candidate.parent.name == "proxies"))
    if is_index:
        ref_match = BUILD_LOG_INDEX_REF_PATTERN.search(text)
        if not ref_match:
            return None, "unparseable"
        if (candidate.name.lower() == "build-log.md"
                and candidate.parent.name == "proxies"):
            entry_file = candidate.parent.parent / "build-log" / ref_match.group(1)
        else:
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


def resolve_test_log_dir(project_root):
    """If the TEST-LOG is in folder mode (path block points to
    proxies/test-log.md), return the resolved test-log/ directory path.
    Returns None if single-file mode or path block can't be resolved."""
    test_log_path = resolve_path_block_entry(project_root, "TEST-LOG.md")
    if test_log_path is None:
        return None
    if (test_log_path.name.lower() == "test-log.md"
            and test_log_path.parent.name == "proxies"):
        return test_log_path.parent.parent / "test-log"
    return None


def collect_all_test_log_rows(project_root):
    """Collect all TEST-LOG rows from either folder mode or single file.

    Folder mode: path block points at proxies/test-log.md; per-session
    files live in sibling test-log/ directory. Walks all .md files in
    test-log/ and aggregates rows.

    Single-file mode: path block points at TEST-LOG.md directly; parse
    that one file.

    Returns (rows, is_folder_mode) where rows is a list of row dicts
    (may be empty) and is_folder_mode is True when folder mode was used.
    Returns ([], False) on any resolution failure.
    """
    test_log_path = resolve_path_block_entry(project_root, "TEST-LOG.md")
    if test_log_path is None or not test_log_path.exists():
        return [], False

    if (test_log_path.name.lower() == "test-log.md"
            and test_log_path.parent.name == "proxies"):
        test_log_dir = test_log_path.parent.parent / "test-log"
        if not test_log_dir.is_dir():
            return [], True
        rows = []
        try:
            for entry_file in sorted(test_log_dir.iterdir(), reverse=True):
                if entry_file.suffix.lower() == ".md":
                    text = safe_read_text(entry_file)
                    if text:
                        rows.extend(parse_test_log_rows(text))
        except OSError:
            pass
        return rows, True

    text = safe_read_text(test_log_path)
    if text is None:
        return [], False
    return parse_test_log_rows(text), False


def get_unconfirmed_previous_session_rows(project_root):
    """Read TEST-LOG and identify rows from the previous build batch's
    session that are not yet confirmed.

    Supports two modes:
      - Folder mode (V75+): path block points to proxies/test-log.md;
        per-session files in sibling test-log/ directory.
      - Single-file (legacy): path block points to TEST-LOG.md directly.

    Returns a tuple (rows, build_log_status, session_id):
      - rows: list of row dicts — the unconfirmed previous-session rows.
        Empty if no unconfirmed rows exist (test session closed) OR
        TEST-LOG is missing, unreadable, or empty.
      - build_log_status: 'ok' / 'missing' / 'unparseable' (per
        identify_previous_session). 'missing' is also returned when
        TEST-LOG itself can't be resolved or read.
      - session_id: the previous session's ID (str) when BUILD-LOG could
        narrow, otherwise None.

    When BUILD-LOG can't narrow (status 'missing' or 'unparseable') AND
    TEST-LOG has rows, the returned rows include every unconfirmed row
    across all sessions — strict fallback per V26 Q3 + V27 Q4.

    Callers:
      - pre_tool_use.py's check_test_confirmation_gate (V27, reframed V66):
        denies build-phase file edits when this returns non-empty rows
        and an active batch exists.
    """
    rows, _ = collect_all_test_log_rows(project_root)
    if not rows:
        test_log_path = resolve_path_block_entry(project_root, "TEST-LOG.md")
        if test_log_path is None or not test_log_path.exists():
            return [], "missing", None
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


def resolve_backlog_dir(project_root):
    """If the BUILD-PLAN is in folder mode (path block points to
    BUILD-PLAN/INDEX.md or proxies/build-plan.md), return the resolved
    BUILD-PLAN/ directory path.
    Returns None if single-file mode or path block can't be resolved."""
    backlog_path = resolve_path_block_entry(project_root, "BUILD-PLAN.md")
    if backlog_path is None:
        return None
    if backlog_path.name.upper() == "INDEX.MD":
        return backlog_path.parent
    if (backlog_path.name.lower() == "build-plan.md"
            and backlog_path.parent.name == "proxies"):
        return backlog_path.parent.parent / "BUILD-PLAN"
    return None


def is_backlog_file(target_path, project_root):
    """True if target_path is part of the BUILD-PLAN — either it IS BUILD-PLAN.md
    (single-file mode) or it's a file inside the BUILD-PLAN/ directory (folder
    mode). Used by hooks that need to identify BUILD-PLAN edits."""
    backlog_path = resolve_path_block_entry(project_root, "BUILD-PLAN.md")
    if backlog_path is None:
        return False
    target_str = str(target_path)
    if target_str == str(backlog_path):
        return True
    backlog_dir = resolve_backlog_dir(project_root)
    if backlog_dir is None:
        return False
    try:
        target_path.relative_to(backlog_dir)
        return True
    except ValueError:
        return False


def is_test_session_open(project_root):
    """Convenience boolean wrapper around get_unconfirmed_previous_session_rows.

    Returns True iff TEST-LOG.md has at least one unconfirmed previous-session
    row. Returns False on any of the lenient cases: missing or unreadable
    TEST-LOG, empty TEST-LOG, all rows confirmed.

    Convenience wrapper: returns True iff the test-confirmation gate
    would deny. Used by session_start.py for the TEST-LOG tripwire.
    """
    unconfirmed, _, _ = get_unconfirmed_previous_session_rows(project_root)
    return bool(unconfirmed)


def is_test_log_content_file(target_path, project_root):
    """True if target_path is a TEST-LOG content file — either a per-session
    file inside test-log/ (folder mode) or the flat TEST-LOG.md (single-file
    mode). Excludes the proxy/index at proxies/test-log.md.

    Used by PostToolUse to decide whether to run TEST-LOG validation."""
    test_log_path = resolve_path_block_entry(project_root, "TEST-LOG.md")
    if test_log_path is not None and str(target_path) == str(test_log_path):
        if (test_log_path.name.lower() == "test-log.md"
                and test_log_path.parent.name == "proxies"):
            return False
        return True

    test_log_dir = resolve_test_log_dir(project_root)
    if test_log_dir is not None:
        try:
            target_path.relative_to(test_log_dir)
            return True
        except ValueError:
            pass

    return False


def is_build_log_entry_file(target_path, project_root):
    """True if target_path is a build-log per-entry file (not INDEX.md,
    not a proxy). Used by PostToolUse to decide whether to run build-log
    validation.

    Skips single-file BUILD-LOG.md — multi-entry files need entry-level
    parsing that this function doesn't attempt."""
    build_log_path = resolve_path_block_entry(project_root, "BUILD-LOG.md")
    if build_log_path is None:
        return False

    if target_path.name.upper() == "INDEX.MD":
        return False
    if target_path.parent.name == "proxies":
        return False

    if build_log_path.name.upper() == "INDEX.MD":
        build_log_dir = build_log_path.parent
    elif (build_log_path.name.lower() == "build-log.md"
            and build_log_path.parent.name == "proxies"):
        build_log_dir = build_log_path.parent.parent / "build-log"
    else:
        return False

    try:
        target_path.relative_to(build_log_dir)
        return True
    except ValueError:
        return False


def is_proxy_file(target_path, project_root):
    """True if target_path is inside a proxies/ directory.
    Used by PostToolUse to decide whether to run proxy validation."""
    return target_path.parent.name == "proxies"


def is_backlog_batch_file(target_path, project_root):
    """True if target_path is a BUILD-PLAN per-batch file (not INDEX.md).
    Per-batch files are NNNN-name.md files inside BUILD-PLAN/.
    Used by PostToolUse for scope-context validation."""
    backlog_dir = resolve_backlog_dir(project_root)
    if backlog_dir is None:
        return False
    try:
        target_path.relative_to(backlog_dir)
    except ValueError:
        return False
    if target_path.name.upper() == "INDEX.MD":
        return False
    return True
