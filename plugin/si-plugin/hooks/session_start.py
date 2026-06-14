#!/usr/bin/env python3
"""
SessionStart hook — detect project state, orient Claude.

Three states:
  1. Not adopted (no SPEC.md) → suggest /setup.
  2. Adopted, _build.md exists → active build, offer resume with /next.
  3. Adopted, no active build → ready for /plan or /next.
"""

import json
import os
import re
import subprocess
import sys

# A placeholder counts only in hash position: an entry heading line
# ("## [HASH] — title") or the start of an index line ("- [HASH] — text").
# Body prose may mention the token literally and must never match — the
# pattern anchors on line shape, not on today's file layout, so the LOG
# structure can change without reworking this.
_HASH_POSITION = re.compile(r"^(?P<prefix>#{1,6}\s+|-\s+)\[HASH\](?P<sep>\s+[—–-]\s+)")


def _oldest_commit_for(cwd, entry_title):
    """Hash of the oldest commit that introduced `entry_title` under LOG/.

    Oldest, never newest: later commits (caps, renames, sweeps) also touch
    entry text, and the newest match would return the wrong hash for
    archived files.
    """
    try:
        result = subprocess.run(
            ["git", "log", "-S", entry_title, "--pretty=%h", "--", "LOG/"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    if result.returncode != 0:
        return ""
    hashes = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return hashes[-1] if hashes else ""


def backfill_log_hashes(cwd):
    """Fill hash placeholders across LOG/*.md in place.

    Returns a one-line report for additionalContext, or "" when nothing
    was filled. Placeholders whose entry isn't committed yet resolve to
    no commit and stay in place for a later session.
    """
    log_dir = os.path.join(cwd, "LOG")
    if not os.path.isdir(log_dir):
        return ""
    try:
        names = sorted(os.listdir(log_dir))
    except OSError:
        return ""
    filled = 0
    touched_files = []
    for name in names:
        if not name.endswith(".md"):
            continue
        path = os.path.join(log_dir, name)
        try:
            with open(path, "r", encoding="utf-8", newline="") as f:
                lines = f.read().splitlines(keepends=True)
        except (OSError, UnicodeDecodeError):
            continue
        changed = False
        for i, line in enumerate(lines):
            match = _HASH_POSITION.match(line)
            if not match:
                continue
            entry_title = line[match.end():].strip()
            if not entry_title:
                continue
            commit = _oldest_commit_for(cwd, entry_title)
            if not commit:
                continue
            lines[i] = (
                match.group("prefix") + commit + match.group("sep") + line[match.end():]
            )
            changed = True
            filled += 1
        if changed:
            try:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write("".join(lines))
            except OSError:
                continue
            touched_files.append(name)
    if not filled:
        return ""
    return (
        f"[Sovereign Implementer] Log housekeeping: filled {filled} commit-hash "
        f"placeholder(s) in {', '.join(touched_files)}. This is an uncommitted "
        "working-tree edit — fold it into this session's commit."
    )


def _dirty_tree_count(cwd):
    """Count files with uncommitted changes via `git status --porcelain`.

    Returns the count, or 0 on any error or a clean tree.
    """
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return 0
    if result.returncode != 0:
        return 0
    return len([line for line in result.stdout.splitlines() if line.strip()])


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return 0

    cwd = data.get("cwd", "")
    if not cwd or not os.path.isdir(cwd):
        return 0

    spec_path = os.path.join(cwd, "SPEC.md")
    queue_path = os.path.join(cwd, "QUEUE.md")
    registry_path = os.path.join(cwd, "REGISTRY.md")
    build_path = os.path.join(cwd, "_build.md")
    plan_state_path = os.path.join(cwd, "_plan.md")
    faq_index_path = os.path.join(cwd, "FAQ", "index.md")
    si_version_path = os.path.join(cwd, ".si-version")

    has_spec = os.path.isfile(spec_path)
    has_queue = os.path.isfile(queue_path)
    has_registry = os.path.isfile(registry_path)
    has_active_build = os.path.isfile(build_path)
    has_plan_state = os.path.isfile(plan_state_path)
    has_faq_index = os.path.isfile(faq_index_path)

    faq_index_content = ""
    if has_faq_index:
        try:
            with open(faq_index_path, "r", encoding="utf-8") as f:
                faq_index_content = f.read()
        except OSError:
            pass

    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    behaviour_path = os.path.join(plugin_root, "docs", "plugin-behaviour.md") if plugin_root else ""

    behaviour_rules = ""
    if behaviour_path and os.path.isfile(behaviour_path):
        try:
            with open(behaviour_path, "r", encoding="utf-8") as f:
                behaviour_rules = f.read()
        except OSError:
            pass

    plugin_version = ""
    if plugin_root:
        plugin_json_path = os.path.join(plugin_root, ".claude-plugin", "plugin.json")
        if os.path.isfile(plugin_json_path):
            try:
                with open(plugin_json_path, "r", encoding="utf-8") as f:
                    plugin_data = json.load(f)
                    plugin_version = plugin_data.get("version", "")
            except (OSError, json.JSONDecodeError):
                pass

    project_version = ""
    if os.path.isfile(si_version_path):
        try:
            with open(si_version_path, "r", encoding="utf-8") as f:
                project_version = f.read().strip()
        except OSError:
            pass

    # Version comparison is retained only for the separate "a plugin update just
    # happened" signal (a future consumer). It is NOT the user-facing "your project
    # is behind" warning anymore — that is now presence-based (see missing_scaffold
    # below), because the version bumps on every release and most releases add
    # nothing a project needs, so a version check cries wolf.
    version_mismatch = has_spec and plugin_version and project_version != plugin_version

    # State 1: Not adopted
    if not has_spec:
        # Check if there's substantial work here (not an empty folder)
        has_work = False
        try:
            entries = os.listdir(cwd)
            non_infra = [
                e for e in entries
                if e not in {
                    ".git", ".gitignore", "CLAUDE.md", ".claude",
                    "__pycache__", "node_modules", ".venv",
                }
            ]
            has_work = len(non_infra) > 3
        except OSError:
            pass

        if has_work:
            msg = (
                "[Sovereign Implementer] This folder has files but no SPEC.md — "
                "it hasn't been set up with the method yet. "
                "Run /setup to get started."
            )
        else:
            msg = (
                "[Sovereign Implementer] Empty project folder. "
                "Run /setup to scaffold the project docs and describe what you're building."
            )

        output = {
            "additionalContext": msg,
        }
        json.dump(output, sys.stdout)
        return 0

    # State 2 or 3: Adopted
    context_parts = []

    if behaviour_rules:
        context_parts.append(
            "=== PLUGIN-WIDE BEHAVIOUR RULES (active every session, govern every skill) ===\n"
            + behaviour_rules
            + "\n=== END BEHAVIOUR RULES ==="
        )

    context_parts.append("[Sovereign Implementer] Project is set up.")
    context_parts.append(f"  SPEC.md: {'found' if has_spec else 'MISSING'}")
    context_parts.append(f"  QUEUE.md: {'found' if has_queue else 'MISSING'}")
    context_parts.append(f"  REGISTRY.md: {'found' if has_registry else 'MISSING'}")

    # Presence-based drift: a project is "behind" only when it's actually missing
    # files/folders the current plugin scaffolds. A higher plugin version with
    # everything present is not drift. Scope: missing files/folders only —
    # content-level drift (a file exists but lacks a newer section) is out of scope.
    missing_scaffold = []
    if not has_queue:
        missing_scaffold.append("QUEUE.md (your work queue)")
    if not has_registry:
        missing_scaffold.append("REGISTRY.md (your components list)")
    if not os.path.isfile(os.path.join(cwd, "LOG", "index.md")):
        missing_scaffold.append("the LOG folder (your session records)")
    if not has_faq_index:
        missing_scaffold.append("the FAQ folder (workflow help)")
    if not os.path.isfile(si_version_path):
        missing_scaffold.append(
            "the .si-version marker (records which plugin version set the project up)"
        )

    if missing_scaffold:
        context_parts.append("")
        context_parts.append(
            "PROJECT OUT OF DATE — the current plugin creates files and folders this "
            "project doesn't have yet: " + "; ".join(missing_scaffold) + ". "
            "Because there is a real gap, you must open your first reply by telling the "
            "user plainly, in everyday language, which parts are missing, and offer to "
            "bring the project up to date by running /setup — it adds what's missing "
            "without touching their existing work. State this as your own first message "
            "before doing anything else; don't bury it in other output or wait to be "
            "asked, because a note the user never reads leaves the project drifting."
        )

    if has_active_build:
        context_parts.append("")
        context_parts.append(
            "ACTIVE BUILD in progress (_build.md exists). "
            "Run /next to resume, or /done if the work is complete. "
            "A planning session (/plan) may run in a separate chat alongside this build — "
            "if this chat was opened to plan, that is allowed; don't refuse it or insist on "
            "resuming or closing the build first."
        )
    else:
        context_parts.append("")
        context_parts.append(
            "Ready. "
            "Run /plan to manage the queue, or /next to start the top batch."
        )

    if has_plan_state:
        context_parts.append("")
        context_parts.append(
            "INTERRUPTED PLANNING SESSION (_plan.md exists). A previous /plan was left "
            "mid-processing. Run /plan to resume from the recorded item and beat, or "
            "/done to close out what was already routed."
        )

    # Dirty-tree warning: uncommitted changes with no active build and no active plan
    # almost always mean a previous session ended without /done — work sitting
    # unrecorded that a non-coder won't notice for weeks. Silent during an active build
    # or an active plan, where dirt is expected mid-session, not orphaned.
    if not has_active_build and not has_plan_state:
        dirty_count = _dirty_tree_count(cwd)
        if dirty_count:
            context_parts.append("")
            context_parts.append(
                f"[Sovereign Implementer] {dirty_count} file(s) have uncommitted "
                "changes from a previous session — /done will pick them up."
            )

    backfill_report = backfill_log_hashes(cwd)
    if backfill_report:
        context_parts.append("")
        context_parts.append(backfill_report)

    if faq_index_content:
        context_parts.append("")
        context_parts.append(faq_index_content)

    output = {
        "additionalContext": "\n".join(context_parts),
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
