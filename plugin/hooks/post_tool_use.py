#!/usr/bin/env python3
"""
PostToolUse hook for the no-code-method plugin.

Fires after Edit/Write/MultiEdit completes successfully. When the edit
targeted a BACKLOG file, runs the parser to validate structural format.
If the parser can't extract data from what should be a parseable file,
surfaces an immediate warning so Claude can fix the formatting before
continuing.

Supports two BACKLOG formats:

  **Single-file (legacy):** edit targets `BACKLOG.md` directly; the
  hook reads the file and runs the text-only parser.

  **Folder (V48+):** edit targets any file inside `BACKLOG/` (INDEX.md
  or a per-batch `NNNN-name.md` file); the hook reads the edited file
  for the unticked-bullet heuristic and runs the path-aware parser
  against INDEX.md for structural validation.

First line of defence against silent BACKLOG corruption. Without it,
a formatting error introduced by an edit stays invisible until the Stop
hook or `/build` tries to parse and gets empty data ({}), often
several turns later.

Detection heuristic: the edited file contains at least one unticked
file bullet (`- [ ]`) with a non-placeholder path, but the parser
returns {} — meaning it couldn't match the surrounding structure well
enough to extract a batch. The search is deliberately file-wide, not
section-bounded — a corrupted section heading is itself a failure mode
the hook should catch. When no unticked bullets exist, {} is the
expected result (all batches done or none declared) and no warning
fires.

Output protocol: stdout receives a JSON object with hookSpecificOutput
containing hookEventName ("PostToolUse") and additionalContext (the
warning text Claude reads). For clean-parse cases, the hook writes
nothing and exits 0.
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
    resolve_backlog_dir,
)
from parse_backlog import (  # noqa: E402
    find_top_unticked_batch,
    find_top_unticked_batch_from_path,
    TEMPLATE_PLACEHOLDER_PATTERN,
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

    if not is_backlog_file(target_path, project_root):
        return emit_silent()

    backlog_path = resolve_path_block_entry(project_root, "BACKLOG.md")
    if backlog_path is None:
        return emit_silent()

    text = safe_read_text(target_path)
    if text is None:
        return emit_silent()

    if not has_real_unticked_bullets(text):
        return emit_silent()

    folder_mode = resolve_backlog_dir(project_root) is not None

    try:
        if folder_mode:
            result = find_top_unticked_batch_from_path(backlog_path)
        else:
            result = find_top_unticked_batch(text)
    except Exception:
        return emit_warning(
            "[No-code method] WARNING: BACKLOG parse error. The edit "
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
        return emit_silent()

    return emit_warning(
        "[No-code method] WARNING: BACKLOG parse failed. The file "
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
        "The Stop hook and `/build` command both depend on this parser. "
        "A format error here will silently prevent batch-executor from "
        "finding the batch."
    )


if __name__ == "__main__":
    sys.exit(main())
