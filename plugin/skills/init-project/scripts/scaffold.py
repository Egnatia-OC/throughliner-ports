#!/usr/bin/env python3
"""
Scaffold the no-code-method spine docs into the user's project (cwd).

Two modes, both write a single JSON object to stdout:

  check  Recursively scan cwd for any file whose name matches one of the
         destination filenames (CLAUDE.md, UX.md, BACKLOG.md, MANIFEST.md).
         No writes. Output: {target_path, conflicts, ready}.

  write  Copy the bundled templates from plugin/templates/ into cwd root,
         renaming each template to its destination filename. Refuses if the
         check step would have reported conflicts. Output: {written, files,
         target_path} on success or {written: false, reason, ...} on failure.

The /init-project skill coordinates: run check, present to user, run write
on confirmation. This script never asks the user anything directly — it has
no terminal access. Interaction is the skill body's job.

ADDITIONAL-DOC-TEMPLATE.md is intentionally not scaffolded here. It lands
in projects via /add-sot-doc when the project decides it needs one.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

# Filenames that the method's runtime expects in a project.
# The recursive scan looks for these names anywhere under cwd.
DESTINATION_FILENAMES = (
    "CLAUDE.md",
    "BACKLOG.md",
    "MANIFEST.md",
    "UX.md",
    "TEST-LOG.md",
)

# Mapping: template filename (in plugin/templates/) -> destination filename
# (in cwd root). Order is preserved for the success report.
TEMPLATE_TO_DESTINATION = (
    ("CLAUDE-TEMPLATE.md", "CLAUDE.md"),
    ("UX-TEMPLATE.md", "UX.md"),
    ("BACKLOG-TEMPLATE.md", "BACKLOG.md"),
    ("MANIFEST-TEMPLATE.md", "MANIFEST.md"),
    ("TEST-LOG-TEMPLATE.md", "TEST-LOG.md"),
)


def templates_dir() -> Path:
    """Return the bundled templates directory.

    This script lives at plugin/skills/init-project/scripts/scaffold.py, so
    plugin/templates/ is three levels up from the script's parent directory.
    """
    return Path(__file__).resolve().parents[3] / "templates"


def find_conflicts(target_dir: Path):
    """Recursively scan target_dir for any file matching DESTINATION_FILENAMES.

    Returns a sorted list of paths relative to target_dir, as strings using
    POSIX-style separators for stable display across platforms.
    """
    target_set = set(DESTINATION_FILENAMES)
    conflicts = []
    for path in target_dir.rglob("*"):
        if path.is_file() and path.name in target_set:
            try:
                rel = path.relative_to(target_dir)
            except ValueError:
                # Shouldn't happen with rglob from target_dir, but guard anyway.
                rel = path
            conflicts.append(rel.as_posix())
    return sorted(conflicts)


def emit(payload, *, exit_code: int = 0) -> int:
    """Write the JSON payload to stdout and return the exit code."""
    json.dump(payload, sys.stdout)
    sys.stdout.write("\n")
    return exit_code


def cmd_check(target_dir: Path) -> int:
    conflicts = find_conflicts(target_dir)
    return emit({
        "target_path": str(target_dir),
        "conflicts": conflicts,
        "ready": not conflicts,
    })


def cmd_write(target_dir: Path) -> int:
    conflicts = find_conflicts(target_dir)
    if conflicts:
        return emit({
            "written": False,
            "reason": "conflicts_found",
            "conflicts": conflicts,
            "target_path": str(target_dir),
        }, exit_code=2)

    src_dir = templates_dir()
    if not src_dir.is_dir():
        return emit({
            "written": False,
            "reason": "templates_directory_missing",
            "expected_at": str(src_dir),
        }, exit_code=3)

    # Verify every template is present before writing any of them, so we
    # don't end up with a half-scaffolded project on a missing-template
    # error.
    missing = [
        tpl for tpl, _ in TEMPLATE_TO_DESTINATION
        if not (src_dir / tpl).is_file()
    ]
    if missing:
        return emit({
            "written": False,
            "reason": "template_files_missing",
            "missing": missing,
            "expected_in": str(src_dir),
        }, exit_code=4)

    written = []
    for tpl_name, dest_name in TEMPLATE_TO_DESTINATION:
        shutil.copyfile(src_dir / tpl_name, target_dir / dest_name)
        written.append(dest_name)

    return emit({
        "written": True,
        "files": written,
        "target_path": str(target_dir),
    })


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold no-code-method templates into a project.",
    )
    parser.add_argument(
        "mode",
        choices=("check", "write"),
        help="check: scan for existing method files; write: copy templates in",
    )
    args = parser.parse_args()

    target_dir = Path.cwd().resolve()
    if args.mode == "check":
        return cmd_check(target_dir)
    return cmd_write(target_dir)


if __name__ == "__main__":
    sys.exit(main())
