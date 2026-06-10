#!/usr/bin/env python3
"""
PreToolUse hook — enforces three rules:

1. SPEC.md is read-only during active builds.
2. During a build, _build.md's Files: section governs which files are
   editable (method docs — QUEUE.md, REGISTRY.md, LOG/, _build.md — are
   always editable). Tri-state: no Files: section = no enforcement;
   section present but empty = method docs only; entries listed = only
   those files.
3. Git safety: block git reset --hard and git push --force.

For Edit/Write/MultiEdit: checks rules 1 and 2.
For Bash/PowerShell: checks rule 3 (git safety) only.
"""

import json
import os
import re
import sys


# --- Git safety patterns ---

RESET_HARD = re.compile(r"\bgit\b.*\breset\b.*--hard\b")
PUSH_FORCE = re.compile(r"\bgit\b.*\bpush\b.*(?:--force(?!-with-lease)\b|-f\b)")


# --- Helpers ---

def _deny(reason: str) -> int:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def _parse_build_files(build_path: str) -> list[str] | None:
    """Extract file paths from _build.md's Files: section.

    Returns None when no Files: section exists (no enforcement),
    an empty list when the section exists but lists nothing
    (method docs only), or the listed paths.
    """
    files = []
    try:
        with open(build_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return None

    in_files = False
    found_section = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("files:"):
            in_files = True
            found_section = True
            continue
        if in_files:
            if stripped.startswith("- "):
                file_entry = stripped[2:].strip()
                # Strip any trailing description after " — " or " - "
                for sep in (" — ", " - ", " – "):
                    if sep in file_entry:
                        file_entry = file_entry[:file_entry.index(sep)].strip()
                if file_entry:
                    files.append(file_entry)
            elif stripped and not stripped.startswith("-"):
                break  # End of Files section
    if not found_section:
        return None
    return files


def _normalise(path: str) -> str:
    """Normalise a path for comparison."""
    return os.path.normcase(os.path.normpath(path))


def _is_method_doc(filepath: str, cwd: str) -> bool:
    """Check if a path is a method doc (QUEUE.md, REGISTRY.md, LOG/, _build.md)."""
    norm = _normalise(filepath)

    for doc in ("QUEUE.md", "REGISTRY.md", "_build.md"):
        if norm == _normalise(os.path.join(cwd, doc)):
            return True

    log_dir = _normalise(os.path.join(cwd, "LOG"))
    if norm.startswith(log_dir + os.sep) or norm == log_dir:
        return True

    return False


def _is_build_file(filepath: str, cwd: str, build_files: list[str]) -> bool:
    """Check if a path is in the build's file list."""
    norm = _normalise(filepath)
    for bf in build_files:
        # Build files can be relative to project root
        candidate = _normalise(os.path.join(cwd, bf))
        if norm == candidate:
            return True
    return False


# --- Main ---

def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return 0

    if not isinstance(data, dict):
        return 0

    cwd = data.get("cwd", "")
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input") or {}

    if not cwd:
        return 0

    # Only enforce in adopted projects (SPEC.md exists)
    spec_path = os.path.join(cwd, "SPEC.md")
    if not os.path.isfile(spec_path):
        return 0

    build_path = os.path.join(cwd, "_build.md")
    has_active_build = os.path.isfile(build_path)

    # --- Bash/PowerShell: git safety ---
    if tool_name in ("Bash", "PowerShell"):
        command = tool_input.get("command", "")
        if not isinstance(command, str):
            return 0

        if RESET_HARD.search(command):
            return _deny(
                "[Sovereign Implementer] BLOCKED: `git reset --hard` destroys "
                "uncommitted work and cannot be undone.\n\n"
                "Safer alternatives:\n"
                "- `git stash` — saves changes for later.\n"
                "- `git checkout -- <file>` — discards one file's changes.\n"
                "- `git reset HEAD~1` — moves HEAD back, keeps working tree."
            )

        if PUSH_FORCE.search(command):
            return _deny(
                "[Sovereign Implementer] BLOCKED: `git push --force` can "
                "overwrite remote commits.\n\n"
                "Use `git push --force-with-lease` instead — it refuses to "
                "push if the remote has commits you haven't fetched."
            )

        return 0

    # --- Edit/Write/MultiEdit: file-scope enforcement ---
    if tool_name not in ("Edit", "Write", "MultiEdit"):
        return 0

    filepath = tool_input.get("file_path", "")
    if not filepath:
        return 0

    # Rule 1: SPEC.md is read-only during active builds
    if has_active_build:
        if _normalise(filepath) == _normalise(spec_path):
            return _deny(
                "[Sovereign Implementer] BLOCKED: SPEC.md is read-only during "
                "an active build.\n\n"
                "Finish the current build with /done first, then edit SPEC.md "
                "in a /plan session. If this is urgent, note it for /plan and "
                "continue building."
            )

    # Rule 2: _build.md's Files: section governs editability. Tri-state:
    # no section = skip enforcement, present but empty = method docs only,
    # entries listed = enforce the list.
    if has_active_build:
        build_files = _parse_build_files(build_path)

        if build_files is None:
            return 0

        if _is_method_doc(filepath, cwd):
            return 0

        if not build_files:
            return _deny(
                "[Sovereign Implementer] BLOCKED: this session's _build.md "
                "lists no editable files, so only QUEUE.md, REGISTRY.md, "
                "LOG/, and _build.md can be edited. Audit and test sessions "
                "don't edit source files — route findings to Captures in "
                "QUEUE.md instead. If a file genuinely needs editing, halt "
                "and add it to _build.md's Files: section with the user's "
                "approval."
            )

        if not _is_build_file(filepath, cwd, build_files):
            return _deny(
                "[Sovereign Implementer] BLOCKED: this file is not in the "
                f"current build's file list.\n\n"
                f"_build.md allows: {', '.join(build_files)}\n\n"
                "If this file genuinely needs editing, halt the build and, "
                "with the user's approval, add it to _build.md's Files: "
                "section."
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
