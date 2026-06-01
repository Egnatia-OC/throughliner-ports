#!/usr/bin/env python3
"""
Scaffold the Sovereign Implementer spine docs into the user's project (cwd), and
classify the project root into one of /sovsetup's four cases.

Three modes, each writes a single JSON object to stdout:

  detect-case  V29/V44: classify the current project root into one of
               /sovsetup's cases. Output: {case: 1-4, case_name, target_path,
               details}. No writes. Used by the /sovsetup procedure to dispatch
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

The /sovsetup procedure coordinates: run detect-case on entry, branch to the
right dialogue, then run check + write (cases 1 and 2) or perform
case-specific work (cases 3, 4). This script never asks the user
anything directly — it has no terminal access. Interaction is the
procedure's job.

ADDITIONAL-DOC-TEMPLATE.md is intentionally not scaffolded here. It lands
in projects via /add-sot-doc when the project decides it needs one.

History: forked from plugin/skills/init-project/scripts/scaffold.py
(V19) at V29, when /init-project was renamed and expanded into /sovsetup.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

# Make plugin/scripts/ importable so we can pull in the shared
# project-state helpers (V29 extraction). This script lives at
# plugin/skills/sovsetup/scripts/scaffold.py, so plugin/scripts/ is three
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
)

# Filenames expected inside _method/ (not at project root).
METHOD_DIR_FILENAMES = (
    "MANIFEST.md",
    "UX.md",
)

# Directory names that conflict if they already exist inside _method/.
METHOD_DIR_DIRNAMES = (
    "build-log",
    "test-log",
    "proxies",
)

# The method subfolder name at project root.
METHOD_DIR = "_method"

# Mapping: template filename (in plugin/templates/) -> destination filename.
# CLAUDE.md goes at project root; others go inside _method/.
TEMPLATE_TO_ROOT = (
    ("CLAUDE-TEMPLATE.md", "CLAUDE.md"),
)
TEMPLATE_TO_METHOD_DIR = (
    ("UX-TEMPLATE.md", "UX.md"),
    ("MANIFEST-TEMPLATE.md", "MANIFEST.md"),
    ("BACKLOG-TEMPLATE.md", "BACKLOG.md"),
)

# Proxy templates: .proxies/<name>.md → _method/proxies/<name>.md.
PROXY_TEMPLATES = ("ux.md", "manifest.md", "research.md",
                   "build-log.md")

# Human-readable case name for each case number. Mirrors V29.md's
# *Outputs* → */sovsetup five-case branching* wording for stability in the
# setup procedure dialogue.
CASE_NAMES = {
    ADOPT_CASE_EMPTY: "empty folder",
    ADOPT_CASE_CODE_NO_DOCS: "existing code, no docs",
    ADOPT_CASE_CODE_FOREIGN_DOCS: "existing code, foreign docs",
    ADOPT_CASE_ALREADY_ADOPTED: "already method-managed",
}


def templates_dir() -> Path:
    """Return the bundled templates directory.

    This script lives at plugin/skills/sovsetup/scripts/scaffold.py, so
    plugin/templates/ is three levels up from the script's parent
    directory."""
    return Path(__file__).resolve().parents[3] / "templates"


def find_conflicts(target_dir: Path):
    """Check for existing method files that would conflict with scaffolding.

    Checks for CLAUDE.md at project root and method docs inside _method/.
    Also checks for legacy root-level spine docs (pre-0087 layout).

    Returns a sorted list of paths relative to target_dir, as strings using
    POSIX-style separators for stable display across platforms."""
    conflicts = []

    # CLAUDE.md at project root
    if (target_dir / "CLAUDE.md").is_file():
        conflicts.append("CLAUDE.md")

    method_dir = target_dir / METHOD_DIR
    if method_dir.is_dir():
        # Check for files inside _method/
        for name in METHOD_DIR_FILENAMES:
            if (method_dir / name).is_file():
                conflicts.append(f"{METHOD_DIR}/{name}")
        for dirname in METHOD_DIR_DIRNAMES:
            if (method_dir / dirname).is_dir():
                conflicts.append(f"{METHOD_DIR}/{dirname}")
        if (method_dir / "BACKLOG.md").is_file():
            conflicts.append(f"{METHOD_DIR}/BACKLOG.md")
        if (method_dir / "TEST-LOG.md").is_file():
            conflicts.append(f"{METHOD_DIR}/TEST-LOG.md")

    # Legacy root-level spine docs (pre-0087 layout)
    for name in METHOD_DIR_FILENAMES:
        if (target_dir / name).is_file():
            conflicts.append(name)
    if (target_dir / "TEST-LOG.md").is_file():
        conflicts.append("TEST-LOG.md")
    if (target_dir / "BACKLOG").is_dir():
        conflicts.append("BACKLOG")
    if (target_dir / "build-log").is_dir():
        conflicts.append("build-log")
    if (target_dir / "test-log").is_dir():
        conflicts.append("test-log")
    if (target_dir / "BACKLOG.md").is_file():
        conflicts.append("BACKLOG.md")

    return sorted(set(conflicts))


def emit(payload, *, exit_code: int = 0) -> int:
    """Write the JSON payload to stdout and return the exit code."""
    json.dump(payload, sys.stdout)
    sys.stdout.write("\n")
    return exit_code


def cmd_detect_case(target_dir: Path) -> int:
    """V29/V44: classify target_dir into one of /sovsetup's four cases.

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

    missing = [
        tpl for tpl, _ in TEMPLATE_TO_ROOT
        if not (src_dir / tpl).is_file()
    ]
    missing.extend(
        tpl for tpl, _ in TEMPLATE_TO_METHOD_DIR
        if not (src_dir / tpl).is_file()
    )
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
    method_dir = target_dir / METHOD_DIR
    method_dir.mkdir(exist_ok=True)

    written = []

    for tpl_name, dest_name in TEMPLATE_TO_ROOT:
        content = (src_dir / tpl_name).read_text(encoding="utf-8")
        content = content.replace("[Project Name]", project_name)
        (target_dir / dest_name).write_text(content, encoding="utf-8")
        written.append(dest_name)

    for tpl_name, dest_name in TEMPLATE_TO_METHOD_DIR:
        content = (src_dir / tpl_name).read_text(encoding="utf-8")
        content = content.replace("[Project Name]", project_name)
        (method_dir / dest_name).write_text(content, encoding="utf-8")
        written.append(f"{METHOD_DIR}/{dest_name}")

    build_log_dir = method_dir / "build-log"
    build_log_dir.mkdir(exist_ok=True)

    test_log_dir = method_dir / "test-log"
    test_log_dir.mkdir(exist_ok=True)

    drafts_dir = method_dir / "planning" / "drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)

    research_dir = method_dir / "research"
    research_dir.mkdir(exist_ok=True)

    search_queries_dir = research_dir / "search-queries"
    search_queries_dir.mkdir(exist_ok=True)

    proxies_dir = method_dir / "proxies"
    proxies_dir.mkdir(exist_ok=True)
    proxy_src = src_dir / ".proxies"
    for proxy_name in PROXY_TEMPLATES:
        proxy_tpl = proxy_src / proxy_name
        if proxy_tpl.is_file():
            shutil.copyfile(proxy_tpl, proxies_dir / proxy_name)
            written.append(f"{METHOD_DIR}/proxies/{proxy_name}")

    return emit({
        "written": True,
        "files": written,
        "directories_created": [
            f"{METHOD_DIR}/",
            f"{METHOD_DIR}/build-log/",
            f"{METHOD_DIR}/test-log/",
            f"{METHOD_DIR}/planning/drafts/",
            f"{METHOD_DIR}/research/",
            f"{METHOD_DIR}/research/search-queries/",
            f"{METHOD_DIR}/proxies/",
        ],
        "target_path": str(target_dir),
    })


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold Sovereign Implementer templates into a project, "
                    "and classify project state for /sovsetup.",
    )
    parser.add_argument(
        "mode",
        choices=("detect-case", "check", "write"),
        help=(
            "detect-case: classify project into one of /sovsetup's 4 cases; "
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
