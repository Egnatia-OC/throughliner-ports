#!/usr/bin/env python3
"""
Stop hook for the no-code-method plugin.

Fires when Claude's turn ends in Claude Code. If there's an unticked build
batch in BACKLOG.md, returns a `decision: block` redirect that pushes Claude
back into building. Otherwise exits silently — the turn ends normally.

Flow:

  1. Read stdin JSON (cwd, session_id, stop_hook_active).
  2. If `stop_hook_active` is True, exit 0 with no output. The hook has
     already redirected once this user turn; redirecting again would
     create an infinite loop. This is the FIRST check after stdin parse
     — anything that would do work before it risks triggering the loop
     in a bug case.
  3. Resolve project root from cwd. Read CLAUDE.md's path block to find
     BACKLOG.md.
  4. Subprocess-call `plugin/scripts/parse_backlog.py` with the BACKLOG.md
     path. Capture stdout.
  5. If parser returns `{}` (no top unticked batch), exit 0 with no
     output.
  6. Otherwise, emit a `{"decision": "block", "reason": "<text>"}` JSON
     object to stdout. The reason is a short prose instruction wrapping
     the parser's JSON output, telling Claude to invoke the batch-executor
     subagent via the Task tool with the payload.

Lenient throughout: any failure (missing CLAUDE.md, unparseable path
block, parser exits non-zero, parser stdout isn't valid JSON, etc.)
results in exit 0 with no output. A Stop hook that blocks unexpectedly
would interfere with normal session ends in surprising ways; better to
fall silently to "nothing to redirect to."

Output protocol: stdout gets a JSON object with `decision` and `reason`
at the top level. Or nothing, if no redirect is warranted. Exit code is
always 0.

Spec: NO-CODE-METHOD.md → After every build (the auto-continuation
behaviour); V25 chat decisions (Q1: shared parser via `parse_backlog.py`;
this hook is one of three call sites — the other two being the `/build`
slash-command and the PreToolUse batch-boundary check).
"""

import json
import re
import subprocess
import sys
from pathlib import Path


# Path to the shared parser, relative to this hook script.
# stop.py lives at plugin/hooks/stop.py; parser at plugin/scripts/parse_backlog.py.
PARSER_PATH = Path(__file__).parent.parent / "scripts" / "parse_backlog.py"

# CLAUDE.md's path block is the first fenced JSON code block in the file.
PATH_BLOCK_PATTERN = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

# Timeout for the parser subprocess call. The parser runs in milliseconds
# on real input; this is insurance against a stuck process, not a tuning
# parameter.
PARSER_TIMEOUT_SECONDS = 10


def emit_silent():
    """Exit silently — no redirect. The turn ends normally."""
    return 0


def emit_redirect(reason):
    """Emit a Stop-hook `block` decision with the given reason text."""
    output = {
        "decision": "block",
        "reason": reason,
    }
    json.dump(output, sys.stdout)
    return 0


def parse_input():
    """Read and parse the hook input from stdin. Return dict on success,
    None on any parse failure."""
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def safe_read_text(path):
    """Read text from path; return None on any IO/decoding failure. Same
    pattern as pre_tool_use.py and parse_backlog.py."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def extract_path_block(claude_md_text):
    """Extract and parse the first fenced JSON code block from CLAUDE.md.
    Returns the parsed dict, or None if missing or unparseable. Duplicated
    from pre_tool_use.py for V25; a shared helper module is a future
    refactor once a third reader needs it."""
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


def resolve_backlog_path(project_root):
    """Read CLAUDE.md's path block from project_root and resolve BACKLOG.md's
    absolute path. Returns Path on success, None on any failure (missing
    CLAUDE.md, unparseable path block, BACKLOG.md key absent)."""
    text = safe_read_text(project_root / "CLAUDE.md")
    if text is None:
        return None
    path_block = extract_path_block(text)
    if not path_block:
        return None
    rel = path_block.get("BACKLOG.md")
    if not isinstance(rel, str) or not rel:
        return None
    try:
        return (project_root / rel).resolve()
    except OSError:
        return None


def run_parser(backlog_path):
    """Invoke parse_backlog.py with backlog_path. Returns the parser's parsed
    JSON output (dict). Returns None on any failure (parser script missing,
    subprocess error, non-zero exit, empty stdout, invalid JSON)."""
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


def format_reason(batch):
    """Build the redirect reason text Claude sees as its next prompt.
    Wraps the parser's JSON output in a short prose instruction telling
    Claude to invoke the batch-executor subagent via the Task tool.

    The JSON is re-serialised with indent=2 for readability — batch-executor
    parses the same data structure, so the re-serialisation just changes the
    formatting, not the contract."""
    payload = json.dumps(batch, ensure_ascii=False, indent=2)
    return (
        "A build batch is ready in BACKLOG.md. Invoke the batch-executor "
        "subagent (via the Task tool) with the following batch payload:\n\n"
        f"{payload}\n\n"
        "Batch-executor will execute the unticked files only and tick each "
        "one in BACKLOG.md as it completes."
    )


def main():
    data = parse_input()
    if not isinstance(data, dict):
        return emit_silent()

    # First check after stdin parse: respect stop_hook_active to prevent the
    # infinite redirect loop. If this is the second-or-later Stop fire in
    # the same user turn, exit silently. (V25 risk #1.)
    if data.get("stop_hook_active") is True:
        return emit_silent()

    cwd_str = data.get("cwd")
    if not isinstance(cwd_str, str) or not cwd_str:
        return emit_silent()

    try:
        project_root = Path(cwd_str).resolve()
    except OSError:
        return emit_silent()

    backlog_path = resolve_backlog_path(project_root)
    if backlog_path is None or not backlog_path.exists():
        return emit_silent()

    batch = run_parser(backlog_path)
    if not isinstance(batch, dict) or not batch:
        return emit_silent()

    return emit_redirect(format_reason(batch))


if __name__ == "__main__":
    sys.exit(main())
