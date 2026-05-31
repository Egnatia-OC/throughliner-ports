#!/usr/bin/env python3
"""
PostToolUse hook for the Sovereign Implementer plugin.

Fires after Edit/Write/MultiEdit completes successfully. Validates
structured method docs at write time — catching shape violations before
they cause silent downstream failures.

Five validation paths (first match wins, except BACKLOG batch files
which run both BACKLOG parse and scope-context checks):

  1. **BACKLOG file** — existing parse validation. If the file has
     unticked file bullets but the parser can't extract a batch, the
     format is likely broken.

  2. **BACKLOG per-batch file** — additionally checks scope-context
     sections (Goal/Outputs/Success criteria).

  3. **TEST-LOG content file** — checks 10-column table row format.

  4. **Build-log entry file** — checks required sections (What shipped,
     Decisions, Pivots). Performance section optional (omitted for
     lighter-close entries).

  5. **Proxy file** — checks HTML comment header format (summary
     proxies only; operational indexes skipped).

All validations are lenient — warnings in additionalContext, not hard
denies. Claude sees the warning and can self-correct.

Output protocol: stdout receives a JSON object with hookSpecificOutput
containing hookEventName ("PostToolUse") and additionalContext (the
warning text Claude reads). For clean cases, the hook writes nothing
and exits 0.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from project_state import (  # noqa: E402
    safe_read_text,
    resolve_path_block_entry,
    is_backlog_file,
    is_backlog_batch_file,
    is_test_log_content_file,
    is_build_log_entry_file,
    is_proxy_file,
    resolve_backlog_dir,
)
from parse_backlog import (  # noqa: E402
    find_top_unticked_batch,
    find_top_unticked_batch_from_path,
    TEMPLATE_PLACEHOLDER_PATTERN,
)
from validate_docs import (  # noqa: E402
    validate_test_log,
    validate_build_log_entry,
    validate_scope_context,
    validate_proxy,
)

WRITING_TOOLS = {"Edit", "Write", "MultiEdit"}

UNTICKED_FILE_BULLET_WITH_PATH = re.compile(
    r"^- \[ \]\s+`([^`]+)`", re.MULTILINE
)


def emit_silent():
    return 0


def emit_warning(message):
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": message,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def has_real_unticked_bullets(text):
    """True if the file has unticked file bullets with non-placeholder
    paths. Searches the full text rather than the Build batches section
    specifically — a corrupted section heading is one of the failure
    modes this hook catches, and section-bounded search would miss it."""
    for m in UNTICKED_FILE_BULLET_WITH_PATH.finditer(text):
        path = m.group(1)
        if not TEMPLATE_PLACEHOLDER_PATTERN.match(path):
            return True
    return False


def check_backlog_parse(target_path, project_root, text):
    """Run the existing BACKLOG parse validation. Returns a warning
    string if the format is broken, None if clean."""
    if not has_real_unticked_bullets(text):
        return None

    backlog_path = resolve_path_block_entry(project_root, "BACKLOG.md")
    if backlog_path is None:
        return None

    folder_mode = resolve_backlog_dir(project_root) is not None

    try:
        if folder_mode:
            result = find_top_unticked_batch_from_path(backlog_path)
        else:
            result = find_top_unticked_batch(text)
    except Exception:
        return (
            "[Sovereign Implementer] WARNING: BACKLOG parse error. The edit "
            "you just made caused the parser to crash. The format is "
            "likely broken — check the Build batches section immediately."
            "\n\n"
            "Expected format for single-file BACKLOG: `### Batch: "
            "<name>` heading, change-list bullets, a `Files:` line, "
            "then file bullets (`- [ ] `path` — summary`).\n"
            "Expected format for folder BACKLOG: `# <name>` heading in "
            "per-batch files, same body structure, INDEX.md with "
            "`` - `NNNN-name.md` `` reference list."
        )

    if isinstance(result, dict) and result:
        return None

    return (
        "[Sovereign Implementer] WARNING: BACKLOG parse failed. The file "
        "contains unticked file entries, but the parser could not "
        "extract a valid batch. The edit you just made likely broke "
        "the format."
        "\n\n"
        "Fix the formatting before continuing. Common causes:\n"
        "  - Batch heading format wrong (`### Batch: <name>` in "
        "single-file; `# <name>` in per-batch file)\n"
        "  - `Changes:` or `Files:` anchor line is missing or "
        "misspelled\n"
        "  - File bullets don't match `- [ ] `path` — summary`\n"
        "  - Template placeholder brackets around a real path or "
        "heading\n"
        "  - In folder mode: batch file not listed in INDEX.md's "
        "Build batches section"
        "\n\n"
        "The `/sovbuild` command and PreToolUse hook both depend on this "
        "parser. A format error here will silently prevent the build "
        "from finding the batch."
    )


def format_doc_warnings(doc_type, warnings):
    """Format a list of validation warnings into a single PostToolUse
    warning message."""
    header = f"[Sovereign Implementer] WARNING: {doc_type} validation issue."
    body = "\n".join(f"  - {w}" for w in warnings)
    return f"{header}\n\n{body}"


def parse_input():
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def main():
    data = parse_input()
    if not isinstance(data, dict):
        return emit_silent()

    tool_name = data.get("tool_name")
    if tool_name not in WRITING_TOOLS:
        return emit_silent()

    tool_input = data.get("tool_input") or {}
    file_path_str = tool_input.get("file_path")
    if not isinstance(file_path_str, str) or not file_path_str:
        return emit_silent()

    cwd_str = data.get("cwd")
    if not isinstance(cwd_str, str) or not cwd_str:
        return emit_silent()

    try:
        project_root = Path(cwd_str).resolve()
    except OSError:
        return emit_silent()

    target_path = Path(file_path_str)
    try:
        if target_path.is_absolute():
            target_path = target_path.resolve()
        else:
            target_path = (project_root / target_path).resolve()
    except OSError:
        return emit_silent()

    text = safe_read_text(target_path)
    if text is None:
        return emit_silent()

    all_warnings = []

    # --- BACKLOG validation (existing + scope-context) ---
    if is_backlog_file(target_path, project_root):
        backlog_warning = check_backlog_parse(target_path, project_root, text)
        if backlog_warning:
            all_warnings.append(backlog_warning)

        if is_backlog_batch_file(target_path, project_root):
            scope_warnings = validate_scope_context(text)
            if scope_warnings:
                all_warnings.append(
                    format_doc_warnings("Scope-context", scope_warnings)
                )

    # --- TEST-LOG validation ---
    elif is_test_log_content_file(target_path, project_root):
        test_warnings = validate_test_log(text)
        if test_warnings:
            all_warnings.append(
                format_doc_warnings("TEST-LOG", test_warnings)
            )

    # --- Build-log entry validation ---
    elif is_build_log_entry_file(target_path, project_root):
        bl_warnings = validate_build_log_entry(text)
        if bl_warnings:
            all_warnings.append(
                format_doc_warnings("Build-log entry", bl_warnings)
            )

    # --- Proxy validation ---
    elif is_proxy_file(target_path, project_root):
        proxy_warnings = validate_proxy(text, target_path.name)
        if proxy_warnings:
            all_warnings.append(
                format_doc_warnings("Proxy", proxy_warnings)
            )

    if not all_warnings:
        return emit_silent()

    return emit_warning("\n\n".join(all_warnings))


if __name__ == "__main__":
    sys.exit(main())
