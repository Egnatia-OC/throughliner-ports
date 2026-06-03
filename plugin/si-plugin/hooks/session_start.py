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
import sys


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
    faq_index_path = os.path.join(cwd, "FAQ", "index.md")
    si_version_path = os.path.join(cwd, ".si-version")

    has_spec = os.path.isfile(spec_path)
    has_queue = os.path.isfile(queue_path)
    has_registry = os.path.isfile(registry_path)
    has_active_build = os.path.isfile(build_path)
    has_faq_index = os.path.isfile(faq_index_path)

    faq_index_content = ""
    if has_faq_index:
        try:
            with open(faq_index_path, "r", encoding="utf-8") as f:
                faq_index_content = f.read()
        except OSError:
            pass

    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    behaviour_path = os.path.join(plugin_root, "docs", "behaviour.md") if plugin_root else ""

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
        context_parts.append(behaviour_rules)

    context_parts.append("[Sovereign Implementer] Project is set up.")
    context_parts.append(f"  SPEC.md: {'found' if has_spec else 'MISSING'}")
    context_parts.append(f"  QUEUE.md: {'found' if has_queue else 'MISSING'}")
    context_parts.append(f"  REGISTRY.md: {'found' if has_registry else 'MISSING'}")

    if version_mismatch:
        context_parts.append("")
        if project_version:
            context_parts.append(
                f"VERSION MISMATCH: project was set up with v{project_version}, "
                f"plugin is now v{plugin_version}. "
                "Run /setup to update project scaffolding."
            )
        else:
            context_parts.append(
                f"VERSION UNKNOWN: no .si-version file found. Plugin is v{plugin_version}. "
                "Run /setup to update project scaffolding."
            )

    if has_active_build:
        context_parts.append("")
        context_parts.append(
            "ACTIVE BUILD in progress (_build.md exists). "
            "Run /next to resume, or /done if the work is complete."
        )
    else:
        context_parts.append("")
        context_parts.append(
            "Ready. "
            "Run /plan to manage the queue, or /next to start the top batch."
        )

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
