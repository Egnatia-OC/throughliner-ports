#!/usr/bin/env python3
"""
Stop hook for the no-code-method plugin.

Fires when Claude's turn ends in Claude Code. Routes to one of four
outcomes depending on BACKLOG.md, TEST-LOG.md, and BUILD-LOG.md state:

  - **Previous batch's test session still open** → exit silently. (V28.)
    TEST-LOG.md has unconfirmed previous-session rows, which means the
    planning subagent's per-row read-back is in progress (its turn just
    ended asking the user about a row outcome). Redirecting anywhere
    here would derail: redirecting to batch-executor was the V27 bug
    this check fixes; redirecting to planning would re-invoke planning
    and re-ask the same question; redirecting to after-build would skip
    the read-back. Silent exit lets the user respond to the row
    question; main Claude resumes the read-back on the next turn under
    the SessionStart-injected tripwire / planning-subagent context.

  - **Unticked build batch exists** → emit a `decision: block` redirect
    that pushes Claude into the batch-executor subagent with the parsed
    batch payload. (V25.) Only fires after the test-session-open check
    passes — i.e., the previous batch's test session is closed.

  - **No unticked batches AND a fully-ticked batch is sitting in BACKLOG.md
    awaiting after-build** → emit a `decision: block` redirect to the
    after-build subagent (V27). The after-build subagent updates
    MANIFEST.md, generates the build recap, and opens the test session
    (writes blank-Status rows to TEST-LOG.md). "Awaiting after-build" is
    detected via BACKLOG.mtime > TEST-LOG.mtime — when BACKLOG was
    modified more recently than TEST-LOG, a batch tick happened that
    after-build hasn't yet processed. The V28 test-session-open check
    runs first, but in normal flow the test session is opened BY
    after-build itself, so this path fires when after-build hasn't yet
    run on the just-ticked batch.

  - **Otherwise** → exit silently, the turn ends normally.

Flow:

  1. Read stdin JSON (cwd, session_id, stop_hook_active).
  2. If `stop_hook_active` is True, exit 0 with no output. The hook has
     already redirected once this user turn; redirecting again would
     create an infinite loop. This is the FIRST check after stdin parse
     — anything that would do work before it risks triggering the loop
     in a bug case.
  3. Resolve project root from cwd. Read CLAUDE.md's path block to find
     BACKLOG.md (and, for the after-build check, TEST-LOG.md).
  4. (V28) Check whether TEST-LOG.md has unconfirmed previous-session
     rows via `is_test_session_open`. If yes, exit silent — the planning
     read-back is in progress and any redirect would derail it.
  5. Subprocess-call `plugin/scripts/parse_backlog.py` with the BACKLOG.md
     path. Capture stdout.
  6. If parser returns a non-empty batch (unticked batch found), emit the
     batch-executor redirect.
  7. If parser returns `{}` (no top unticked batch), check whether a
     fully-ticked batch exists in BACKLOG.md and BACKLOG.mtime is more
     recent than TEST-LOG.mtime. If so, emit the after-build redirect.
     Otherwise, exit silent.

Lenient throughout: any failure (missing CLAUDE.md, unparseable path
block, parser exits non-zero, parser stdout isn't valid JSON, stat
failures on mtimes, etc.) results in exit 0 with no output. A Stop hook
that blocks unexpectedly would interfere with normal session ends in
surprising ways; better to fall silently to "nothing to redirect to."
The V28 test-session-open check is part of this leniency posture —
absence-of-evidence (no TEST-LOG, unreadable TEST-LOG, empty TEST-LOG)
all count as "no signal, fall through to the normal redirect logic."

Output protocol: stdout gets a JSON object with `decision` and `reason`
at the top level. Or nothing, if no redirect is warranted. Exit code is
always 0.

Spec: NO-CODE-METHOD.md → After every build (the auto-continuation
behaviour and the after-build subagent's role); V25 chat decisions (Q1:
shared parser via `parse_backlog.py`; this hook is one of three call
sites — the other two being the `/build` slash-command and the
PreToolUse batch-boundary check); V27 Q1 (Stop-hook routing for
after-build trigger, with after-build subagent body at
`plugin/agents/after-build.md`); V28 (Stop-hook-vs-tripwire conflict
resolution — test-session-open check defers the batch-executor redirect
in favour of silent exit).
"""

import json
import re
import sys
from pathlib import Path

# Make the sibling plugin/scripts/ directory importable so we can pull in
# the shared project-state helpers. stop.py lives at plugin/hooks/;
# project_state.py is at plugin/scripts/. (V28 extraction — same pattern
# as pre_tool_use.py.)
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from project_state import (  # noqa: E402 — must follow sys.path insert
    safe_read_text,
    resolve_path_block_entry,
    run_parser,
    is_test_session_open,
)


# V27 after-build detection patterns.

# `## Build batches` section heading in BACKLOG.md. Same pattern as
# parse_backlog.py — kept local here for the cheap "is there a ticked
# file anywhere in the section?" scan.
BUILD_BATCHES_SECTION_PATTERN = re.compile(r"^## Build batches\s*$", re.MULTILINE)
NEXT_TOP_SECTION_PATTERN = re.compile(r"^## ", re.MULTILINE)

# Detects a `- [x]` (case-insensitive) file bullet anywhere in the Build
# batches section. Indicates at least one batch has been worked on.
TICKED_FILE_BULLET_PATTERN = re.compile(r"^- \[[xX]\] ", re.MULTILINE)

# Logical name for the after-build subagent. Used in the redirect reason
# so Claude knows which subagent_type to pass to the Task tool.
AFTER_BUILD_SUBAGENT_TYPE = "no-code-method:after-build"


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


# safe_read_text, extract_path_block, resolve_path_block_entry, and run_parser
# now live in project_state.py (V28 extraction). resolve_backlog_path was a
# one-line wrapper that's been removed in favour of an explicit
# `resolve_path_block_entry(project_root, "BACKLOG.md")` call at the use site.


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


# --- V27 after-build redirect helpers ---


def has_ticked_file_in_build_batches(backlog_text):
    """Return True iff the `## Build batches` section contains at least one
    `- [x]` file bullet. Indicates a batch has been worked on and is sitting
    awaiting after-build (or planning). False when the section is missing,
    empty, or contains only unticked bullets."""
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return False
    after_section = backlog_text[section_match.end():]
    next_section = NEXT_TOP_SECTION_PATTERN.search(after_section)
    section_text = (
        after_section[:next_section.start()]
        if next_section
        else after_section
    )
    return bool(TICKED_FILE_BULLET_PATTERN.search(section_text))


def after_build_appears_pending(project_root, backlog_path, backlog_text):
    """Return True iff a fully-ticked batch sits in BACKLOG.md and
    after-build appears not to have run for it yet.

    Heuristic: BACKLOG.mtime > TEST-LOG.mtime → a batch tick happened
    after after-build's last write to TEST-LOG. When TEST-LOG.md is
    missing entirely from the path block, we redirect anyway — the
    after-build subagent will scaffold or warn as appropriate.

    Lenient on stat failures: any OSError → False (no redirect), since
    we can't be sure of the comparison.

    Limitation: a planning session that touches BACKLOG.md after
    after-build ran (e.g. removing the completed batch) advances
    BACKLOG.mtime ahead of TEST-LOG.mtime. The has_ticked_file_in_build_batches
    gate above blocks the false-positive — if planning removed all
    completed batches, no `- [x]` survives and the check returns False
    before this function is consulted."""
    if not has_ticked_file_in_build_batches(backlog_text):
        return False

    test_log_path = resolve_path_block_entry(project_root, "TEST-LOG.md")
    if test_log_path is None or not test_log_path.exists():
        # No TEST-LOG in path block (or path block points to a missing
        # file). Redirect anyway — after-build's first run will write
        # rows or surface the problem.
        return True

    try:
        backlog_mtime = backlog_path.stat().st_mtime
        test_log_mtime = test_log_path.stat().st_mtime
    except OSError:
        return False
    return backlog_mtime > test_log_mtime


def format_after_build_reason():
    """Build the redirect reason text Claude sees when after-build is the
    next action. Generic — the after-build subagent reads BACKLOG.md and
    TEST-LOG.md itself to figure out which batch it's recapping and what
    rows to open."""
    return (
        "A build batch in BACKLOG.md has all its files ticked and "
        f"after-build has not yet run for it. Invoke the `{AFTER_BUILD_SUBAGENT_TYPE}` "
        "subagent (via the Task tool) with a short prose prompt — the "
        "subagent reads BACKLOG.md and TEST-LOG.md itself.\n\n"
        "The subagent will:\n"
        "  1. Update MANIFEST.md silently for anything created, renamed, "
        "or deleted by the batch.\n"
        "  2. Produce a plain-English build recap labelling each change "
        "`[Requested]` / `[Suggested]` per BACKLOG.md.\n"
        "  3. Open the test session by appending blank-Status rows to "
        "TEST-LOG.md — one per user-observable behaviour the recap names.\n"
        "  4. Prompt the user to refresh, test, and bring per-row outcomes "
        "to the next planning session.\n\n"
        "Per NO-CODE-METHOD.md → *After every build*."
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

    backlog_path = resolve_path_block_entry(project_root, "BACKLOG.md")
    if backlog_path is None or not backlog_path.exists():
        return emit_silent()

    # V28: Before any redirect, check whether the previous build batch's
    # test session is still open. If TEST-LOG.md has unconfirmed previous-
    # session rows, the planning subagent's read-back is mid-flight (its
    # turn just ended asking the user about a row) — redirecting now
    # would derail the read-back, the bug this check fixes. Exit silent
    # and let the user answer.
    if is_test_session_open(project_root):
        return emit_silent()

    batch = run_parser(backlog_path)
    if isinstance(batch, dict) and batch:
        # Top unticked batch exists — redirect into batch-executor.
        return emit_redirect(format_reason(batch))

    # V27: no unticked batches. Check whether a fully-ticked batch is
    # sitting in BACKLOG.md awaiting after-build. If so, redirect to the
    # after-build subagent.
    backlog_text = safe_read_text(backlog_path)
    if backlog_text is None:
        return emit_silent()
    if after_build_appears_pending(project_root, backlog_path, backlog_text):
        return emit_redirect(format_after_build_reason())

    return emit_silent()


if __name__ == "__main__":
    sys.exit(main())
