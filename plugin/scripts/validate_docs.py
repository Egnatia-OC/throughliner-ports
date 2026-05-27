#!/usr/bin/env python3
"""
validate_docs.py — structured-markdown validator for no-code-method docs.

Validates shape correctness of method docs at write time (PostToolUse)
and as a standalone planning pre-flight. Four doc types:

  - TEST-LOG: 10-column table row check
  - Build-log entry: required sections (What shipped, Decisions taken
    and why, Pivots and surprises, Carried forward) + Performance section
  - Scope-context: Goal/Outputs/Success criteria in batch files
  - Proxy: HTML comment header format (summary proxies only)

All validators are lenient — warnings, not errors. Each returns a list
of warning strings; empty list = valid. Same philosophy as
parse_backlog.py: malformed input surfaces a warning in PostToolUse's
additionalContext so Claude can self-correct.

Callable from PostToolUse (import) and as standalone CLI:

    python validate_docs.py <file> [--type test-log|build-log|scope|proxy]

Spec: DOC-STRUCTURE.md (TEST-LOG structure, Build log structure,
BUILD-PLAN structure → Build batches, Proxy files).
"""

import re
import sys
from pathlib import Path


# --- TEST-LOG validator ---


def _count_table_columns(line):
    """Count columns in a markdown table row. Returns column count, or 0
    if the line isn't a table row."""
    stripped = line.strip()
    if not stripped.startswith("|"):
        return 0
    parts = stripped.split("|")
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return len(parts)


def validate_test_log(text):
    """Check TEST-LOG table rows have 10 columns.

    Validates every table row (header, separator, data). A row with fewer
    or more columns triggers a warning. Rows with fewer than 2 columns
    are skipped (not a real table row).

    Returns list of warning strings."""
    if not isinstance(text, str):
        return []
    warnings = []
    for i, line in enumerate(text.splitlines(), 1):
        col_count = _count_table_columns(line)
        if col_count < 2:
            continue
        if col_count != 10:
            warnings.append(
                f"Line {i}: table row has {col_count} columns, expected 10."
            )
    return warnings


# --- Build-log entry validator ---


_REQUIRED_BOLD_SECTIONS = (
    "What shipped",
    "Decisions taken and why",
    "Pivots and surprises",
    "Carried forward",
)


def validate_build_log_entry(text):
    """Check a build-log per-entry file for required sections.

    Four bold-label sections (**What shipped.**, etc.) and one heading
    (## Performance). Only fires when the file has a heading and
    substantial content. Returns list of warning strings."""
    if not isinstance(text, str) or not text.strip():
        return []
    if not re.search(r"^# .+", text, re.MULTILINE):
        return []
    warnings = []
    for section in _REQUIRED_BOLD_SECTIONS:
        pattern = re.compile(rf"\*\*{re.escape(section)}\.\*\*", re.IGNORECASE)
        if not pattern.search(text):
            warnings.append(f"Missing required section: **{section}.**")
    if not re.search(r"^## Performance", text, re.MULTILINE):
        warnings.append("Missing required ## Performance section.")
    return warnings


# --- Scope-context validator (batch files) ---


_REQUIRED_SCOPE_SECTIONS = ("Goal", "Outputs", "Success criteria")

_BATCH_HEADING = re.compile(r"^# .+", re.MULTILINE)


def validate_scope_context(text):
    """Check a batch file has Goal/Outputs/Success criteria.

    Only fires when the file has a heading and substantial content
    (more than just a heading line). Returns list of warning strings."""
    if not isinstance(text, str):
        return []
    if not _BATCH_HEADING.search(text):
        return []
    content_lines = [
        l for l in text.splitlines()
        if l.strip() and not l.startswith("# ")
    ]
    if len(content_lines) < 3:
        return []
    warnings = []
    for section in _REQUIRED_SCOPE_SECTIONS:
        pattern = re.compile(
            rf"\*\*{re.escape(section)}\.\*\*", re.IGNORECASE
        )
        if not pattern.search(text):
            warnings.append(
                f"Missing required scope-context section: **{section}.**"
            )
    return warnings


# --- Proxy validator ---


_PROXY_HEADER = re.compile(
    r"^<!--\s*proxy\s*\|\s*source:\s*\S+\s*\|\s*generated:\s*\d{4}-\d{2}-\d{2}\s*-->",
    re.MULTILINE,
)

_OPERATIONAL_PROXIES = frozenset({"build-plan.md", "build-log.md", "test-log.md"})


def validate_proxy(text, filename=None):
    """Check proxy file for HTML comment header.

    Operational index proxies (build-plan.md, build-log.md, test-log.md)
    are directly edited and follow a different format — skipped.
    Summary proxies (ux.md, manifest.md, research.md) must have the
    canonical header.

    Returns list of warning strings."""
    if not isinstance(text, str) or not text.strip():
        return []
    if filename and filename.lower() in _OPERATIONAL_PROXIES:
        return []
    warnings = []
    if not _PROXY_HEADER.search(text):
        warnings.append(
            "Missing proxy header: "
            "<!-- proxy | source: <path> | generated: YYYY-MM-DD -->"
        )
    return warnings


# --- CLI entry point ---


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: validate_docs.py <file> "
            "[--type test-log|build-log|scope|proxy]",
            file=sys.stderr,
        )
        return 1

    path = Path(sys.argv[1])
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return 1

    doc_type = None
    if "--type" in sys.argv:
        idx = sys.argv.index("--type")
        if idx + 1 < len(sys.argv):
            doc_type = sys.argv[idx + 1]

    warnings = []
    if doc_type == "test-log":
        warnings = validate_test_log(text)
    elif doc_type == "build-log":
        warnings = validate_build_log_entry(text)
    elif doc_type == "scope":
        warnings = validate_scope_context(text)
    elif doc_type == "proxy":
        warnings = validate_proxy(text, path.name)
    else:
        name_lower = path.name.lower()
        parent_name = path.parent.name.lower()
        if "test-log" in name_lower or parent_name == "test-log":
            warnings = validate_test_log(text)
        elif parent_name == "build-log" and name_lower != "index.md":
            warnings = validate_build_log_entry(text)
        elif parent_name == "build-plan":
            warnings = validate_scope_context(text)
        elif parent_name == "proxies":
            warnings = validate_proxy(text, path.name)

    if warnings:
        for w in warnings:
            print(f"WARNING: {w}")
    else:
        print("OK: no issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
