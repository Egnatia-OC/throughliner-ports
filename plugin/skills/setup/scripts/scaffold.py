#!/usr/bin/env python3
"""
Scaffold the no-code-method spine docs into the user's project (cwd), and
classify the project root into one of /setup's four cases.

Three modes, each writes a single JSON object to stdout:

  detect-case  V29/V44: classify the current project root into one of
               /setup's cases. Output: {case: 1-4, case_name, target_path,
               details}. No writes. Used by the /setup procedure to dispatch
               to the right dialogue branch on entry.

  check  Recursively scan cwd for any file whose name matches one of the
         destination filenames (CLAUDE.md, UX.md, MANIFEST.md, TEST-LOG.md)
         or directory names (BACKLOG, build-log). No writes. Output:
         {target_path, conflicts, ready}.

  write  Copy the bundled templates from plugin/templates/ into cwd root,
         renaming each template to its destination filename. Refuses if the
         check step would have reported conflicts. Output: {written, files,
         target_path} on success or {written: false, reason, ...} on
         failure.

The /setup procedure coordinates: run detect-case on entry, branch to the
right dialogue, then run check + write (cases 1 and 2) or perform
case-specific work (cases 3, 4). This script never asks the user
anything directly — it has no terminal access. Interaction is the
procedure's job.

ADDITIONAL-DOC-TEMPLATE.md is intentionally not scaffolded here. It lands
in projects via /add-sot-doc when the project decides it needs one.

History: forked from plugin/skills/init-project/scripts/scaffold.py
(V19) at V29, when /init-project was renamed and expanded into /setup.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

# Make plugin/scripts/ importable so we can pull in the shared
# project-state helpers (V29 extraction). This script lives at
# plugin/skills/setup/scripts/scaffold.py, so plugin/scripts/ is three
# levels up from the script's parent directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from project_state import (  # noqa: E402 — must follow sys.path insert
    detect_adopt_case,
    ADOPT_CASE_EMPTY,
    ADOPT_CASE_CODE_NO_DOCS,
    ADOPT_CASE_CODE_FOREIGN_DOCS,
    ADOPT_CASE_ALREADY_ADOPTED,
)

# Filenames and directory names that the method's runtime expects in a project.
# The recursive scan looks for these anywhere under cwd.
DESTINATION_FILENAMES = (
    "CLAUDE.md",
    "MANIFEST.md",
    "UX.md",
    "TEST-LOG.md",
)

# Directory names that conflict if they already exist at the project root.
DESTINATION_DIRNAMES = (
    "BACKLOG",
    "build-log",
)

# Mapping: template filename (in plugin/templates/) -> destination filename
# (in cwd root). Order is preserved for the success report.
# BACKLOG and build-log are handled separately (folder scaffolds).
TEMPLATE_TO_DESTINATION = (
    ("CLAUDE-TEMPLATE.md", "CLAUDE.md"),
    ("UX-TEMPLATE.md", "UX.md"),
    ("MANIFEST-TEMPLATE.md", "MANIFEST.md"),
    ("TEST-LOG-TEMPLATE.md", "TEST-LOG.md"),
)

# BACKLOG folder template: INDEX-TEMPLATE.md → BACKLOG/INDEX.md.
BACKLOG_INDEX_TEMPLATE = "BACKLOG/INDEX-TEMPLATE.md"
BACKLOG_INDEX_DEST = "INDEX.md"

# build-log folder template: INDEX-TEMPLATE.md → build-log/INDEX.md.
BUILD_LOG_INDEX_TEMPLATE = "build-log/INDEX-TEMPLATE.md"
BUILD_LOG_INDEX_DEST = "INDEX.md"

# Proxy templates: .proxies/<name>.md → .proxies/<name>.md (same names).
PROXY_TEMPLATES = ("ux.md", "manifest.md", "test-log.md", "research.md")

# Human-readable case name for each case number. Mirrors V29.md's
# *Outputs* → */setup five-case branching* wording for stability in the
# setup procedure dialogue.
CASE_NAMES = {
    ADOPT_CASE_EMPTY: "empty folder",
    ADOPT_CASE_CODE_NO_DOCS: "existing code, no docs",
    ADOPT_CASE_CODE_FOREIGN_DOCS: "existing code, foreign docs",
    ADOPT_CASE_ALREADY_ADOPTED: "already method-managed",
}


def templates_dir() -> Path:
    """Return the bundled templates directory.

    This script lives at plugin/skills/setup/scripts/scaffold.py, so
    plugin/templates/ is three levels up from the script's parent
    directory."""
    return Path(__file__).resolve().parents[3] / "templates"


def find_conflicts(target_dir: Path):
    """Recursively scan target_dir for any file matching DESTINATION_FILENAMES,
    any BACKLOG.md file, or any BACKLOG/ directory.

    Returns a sorted list of paths relative to target_dir, as strings using
    POSIX-style separators for stable display across platforms."""
    target_set = set(DESTINATION_FILENAMES)
    dir_set = set(DESTINATION_DIRNAMES)
    conflicts = []
    for path in target_dir.rglob("*"):
        if path.is_file() and path.name in target_set:
            try:
                rel = path.relative_to(target_dir)
            except ValueError:
                rel = path
            conflicts.append(rel.as_posix())
        if path.is_file() and path.name == "BACKLOG.md":
            try:
                rel = path.relative_to(target_dir)
            except ValueError:
                rel = path
            conflicts.append(rel.as_posix())
    for dirname in dir_set:
        candidate = target_dir / dirname
        if candidate.is_dir():
            conflicts.append(dirname)
    return sorted(set(conflicts))


def emit(payload, *, exit_code: int = 0) -> int:
    """Write the JSON payload to stdout and return the exit code."""
    json.dump(payload, sys.stdout)
    sys.stdout.write("\n")
    return exit_code


def cmd_detect_case(target_dir: Path) -> int:
    """V29/V44: classify target_dir into one of /setup's four cases.

    Output includes the case number, the human-readable case name, the
    resolved target path, and a `details` dict with case-specific signal
    (e.g. whether a foreign CLAUDE.md was detected for case 3)."""
    case = detect_adopt_case(target_dir)
    details = {
        "claude_md_present": (target_dir / "CLAUDE.md").is_file(),
    }
    return emit({
        "case": case,
        "case_name": CASE_NAMES.get(case, "unknown"),
        "target_path": str(target_dir),
        "details": details,
    })


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
    backlog_index_tpl = src_dir / BACKLOG_INDEX_TEMPLATE
    if not backlog_index_tpl.is_file():
        missing.append(BACKLOG_INDEX_TEMPLATE)
    build_log_index_tpl = src_dir / BUILD_LOG_INDEX_TEMPLATE
    if not build_log_index_tpl.is_file():
        missing.append(BUILD_LOG_INDEX_TEMPLATE)
    for proxy_name in PROXY_TEMPLATES:
        if not (src_dir / ".proxies" / proxy_name).is_file():
            missing.append(f".proxies/{proxy_name}")
    if missing:
        return emit({
            "written": False,
            "reason": "template_files_missing",
            "missing": missing,
            "expected_in": str(src_dir),
        }, exit_code=4)

    project_name = target_dir.name

    written = []
    for tpl_name, dest_name in TEMPLATE_TO_DESTINATION:
        content = (src_dir / tpl_name).read_text(encoding="utf-8")
        content = content.replace("[Project Name]", project_name)
        (target_dir / dest_name).write_text(content, encoding="utf-8")
        written.append(dest_name)

    backlog_dir = target_dir / "BACKLOG"
    backlog_dir.mkdir(exist_ok=True)
    content = backlog_index_tpl.read_text(encoding="utf-8")
    content = content.replace("[Project Name]", project_name)
    (backlog_dir / BACKLOG_INDEX_DEST).write_text(content, encoding="utf-8")
    written.append("BACKLOG/INDEX.md")

    build_log_dir = target_dir / "build-log"
    build_log_dir.mkdir(exist_ok=True)
    content = build_log_index_tpl.read_text(encoding="utf-8")
    content = content.replace("[Project Name]", project_name)
    (build_log_dir / BUILD_LOG_INDEX_DEST).write_text(content, encoding="utf-8")
    written.append("build-log/INDEX.md")

    drafts_dir = target_dir / "planning" / "drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)

    research_dir = target_dir / "research"
    research_dir.mkdir(exist_ok=True)

    search_queries_dir = research_dir / "search-queries"
    search_queries_dir.mkdir(exist_ok=True)

    proxies_dir = target_dir / ".proxies"
    proxies_dir.mkdir(exist_ok=True)
    proxy_src = src_dir / ".proxies"
    for proxy_name in PROXY_TEMPLATES:
        proxy_tpl = proxy_src / proxy_name
        if proxy_tpl.is_file():
            shutil.copyfile(proxy_tpl, proxies_dir / proxy_name)
            written.append(f".proxies/{proxy_name}")

    return emit({
        "written": True,
        "files": written,
        "directories_created": ["BACKLOG/", "build-log/", "planning/drafts/", "research/", "research/search-queries/", ".proxies/"],
        "target_path": str(target_dir),
    })


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold no-code-method templates into a project, "
                    "and classify project state for /setup.",
    )
    parser.add_argument(
        "mode",
        choices=("detect-case", "check", "write"),
        help=(
            "detect-case: classify project into one of /setup's 4 cases; "
            "check: scan for existing method files; "
            "write: copy templates in"
        ),
    )
    args = parser.parse_args()

    target_dir = Path.cwd().resolve()
    if args.mode == "detect-case":
        return cmd_detect_case(target_dir)
    if args.mode == "check":
        return cmd_check(target_dir)
    return cmd_write(target_dir)


if __name__ == "__main__":
    sys.exit(main())
