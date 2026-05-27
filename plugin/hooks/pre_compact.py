#!/usr/bin/env python3
"""
PreCompact hook for the no-code-method plugin.

Fires before Claude Code compresses the conversation context (manual or
automatic compaction). When a build batch is in progress (unticked files
in the top BUILD-PLAN batch), blocks compaction and shows the user a message
recommending they ask Claude to prepare a handoff before starting a fresh
session. When no build is in progress, allows compaction silently.

Why block during builds:
  Long sessions cost more tokens and Claude's adherence to the method
  degrades as context grows. A fresh session re-reads the method docs
  from scratch and starts with full adherence. The build batch on disk
  already carries the ticked/unticked file state, but mid-build decisions
  and approach context live only in the conversation. The handoff process
  updates the batch to make it self-documenting about its partial state
  before the user leaves.

Why allow when no build is active:
  Planning and idle sessions keep their state on disk (BUILD-PLAN edits are
  saved as they happen, source-of-truth docs are durable). Compaction is
  acceptable — the method docs survive in compacted form, and there's no
  build-batch handoff to produce.

Output protocol:
  Active build: JSON with decision "block" and reason (user-visible).
  No active build: write nothing, exit 0 (allow compaction).

The reason text is user-facing only — Claude does not see it. The message
includes a paste-ready prompt the user can send to Claude to trigger the
handoff process.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from project_state import (  # noqa: E402
    safe_read_text,
    resolve_path_block_entry,
    resolve_backlog_dir,
)
from parse_backlog import (  # noqa: E402
    find_top_unticked_batch,
    find_top_unticked_batch_from_path,
)

HANDOFF_PROMPT = (
    "The session is getting long. Please prepare a handoff: update the "
    "current build batch so it's clear what's been delivered and what "
    "still needs to be done, then let me know when it's ready."
)


def parse_input():
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def has_active_build(project_root):
    """Check whether a build batch with unticked files exists."""
    backlog_path = resolve_path_block_entry(project_root, "BUILD-PLAN.md")
    if backlog_path is None:
        return False

    folder_mode = resolve_backlog_dir(project_root) is not None

    try:
        if folder_mode:
            result = find_top_unticked_batch_from_path(backlog_path)
        else:
            text = safe_read_text(backlog_path)
            if text is None:
                return False
            result = find_top_unticked_batch(text)
    except Exception:
        return False

    return isinstance(result, dict) and bool(result)


def main():
    data = parse_input()
    if not isinstance(data, dict):
        return 0

    cwd_str = data.get("cwd")
    if not isinstance(cwd_str, str) or not cwd_str:
        return 0

    try:
        project_root = Path(cwd_str).resolve()
    except OSError:
        return 0

    if not has_active_build(project_root):
        return 0

    reason = (
        "[No-code method] Your session is getting long. Long sessions "
        "cost more tokens and Claude follows the method less reliably "
        "as context grows. A fresh session will re-read the method docs "
        "and start with full adherence.\n\n"
        "A build batch is in progress. Before starting a new session, "
        "ask Claude to prepare a handoff so the next session can pick up "
        "cleanly.\n\n"
        "Copy and paste this to Claude:\n\n"
        f"  {HANDOFF_PROMPT}"
    )

    output = {"decision": "block", "reason": reason}
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
