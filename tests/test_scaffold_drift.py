"""Scaffold drift detection — keeps case 1 output in sync with case 4 migrations.

When scaffold.py write gains a new file or directory, the registry
test fails. The developer must then:
1. Update EXPECTED_FILES / EXPECTED_DIRS below.
2. Add a corresponding case-4 migration to plugin/docs/procedures/setup.md.

The registry is the enforcement mechanism. It catches what the developer
forgets — which is the goal of batch 0109.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
SCAFFOLD_SCRIPT = (
    REPO_ROOT / "plugin" / "skills" / "sovsetup" / "scripts" / "scaffold.py"
)

# --- Registry: canonical case-1 scaffold output ---------------------------
#
# Every file scaffold.py write creates. Paths use forward slashes,
# relative to the project root.
#
# When adding an entry: also add a case-4 migration to
# plugin/docs/procedures/setup.md → Case 4 → Option 1.

EXPECTED_FILES = frozenset({
    "CLAUDE.md",
    "_method/UX.md",
    "_method/MANIFEST.md",
    "_method/proxies/ux.md",
    "_method/proxies/manifest.md",
    "_method/proxies/research.md",
    "_method/proxies/backlog.md",
    "_method/proxies/build-log.md",
})

# Every directory scaffold.py write creates (including implicit parents).
EXPECTED_DIRS = frozenset({
    "_method",
    "_method/BACKLOG",
    "_method/build-log",
    "_method/test-log",
    "_method/planning",
    "_method/planning/drafts",
    "_method/research",
    "_method/research/search-queries",
    "_method/proxies",
})


# --- Helpers ---------------------------------------------------------------

def run_scaffold_write(target_dir: Path) -> dict:
    """Run scaffold.py write with cwd set to target_dir."""
    result = subprocess.run(
        [sys.executable, str(SCAFFOLD_SCRIPT), "write"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=str(target_dir),
        timeout=10,
    )
    assert result.returncode == 0, (
        f"scaffold.py write failed (exit {result.returncode}):\n{result.stderr}"
    )
    return json.loads(result.stdout.strip())


def collect_structure(root: Path):
    """Return (files, dirs) as sets of POSIX-style paths relative to root."""
    files = set()
    dirs = set()
    for item in root.rglob("*"):
        rel = item.relative_to(root).as_posix()
        if item.is_file():
            files.add(rel)
        elif item.is_dir():
            dirs.add(rel)
    return files, dirs


# --- Tests -----------------------------------------------------------------

class TestScaffoldRegistry:
    """Compare scaffold.py write output against the hardcoded registry."""

    def test_files_match_registry(self, tmp_path):
        run_scaffold_write(tmp_path)
        actual_files, _ = collect_structure(tmp_path)

        missing = EXPECTED_FILES - actual_files
        extra = actual_files - EXPECTED_FILES

        parts = []
        if missing:
            parts.append(
                f"Registry lists files scaffold.py no longer creates:\n"
                f"  {sorted(missing)}\n"
                f"Remove them from EXPECTED_FILES."
            )
        if extra:
            parts.append(
                f"scaffold.py creates files not in the registry:\n"
                f"  {sorted(extra)}\n"
                f"Add them to EXPECTED_FILES in this test AND add a case-4\n"
                f"migration to plugin/docs/procedures/setup.md → Case 4."
            )
        assert not parts, "\n\n".join(parts)

    def test_dirs_match_registry(self, tmp_path):
        run_scaffold_write(tmp_path)
        _, actual_dirs = collect_structure(tmp_path)

        missing = EXPECTED_DIRS - actual_dirs
        extra = actual_dirs - EXPECTED_DIRS

        parts = []
        if missing:
            parts.append(
                f"Registry lists dirs scaffold.py no longer creates:\n"
                f"  {sorted(missing)}\n"
                f"Remove them from EXPECTED_DIRS."
            )
        if extra:
            parts.append(
                f"scaffold.py creates dirs not in the registry:\n"
                f"  {sorted(extra)}\n"
                f"Add them to EXPECTED_DIRS in this test AND add a case-4\n"
                f"migration to plugin/docs/procedures/setup.md → Case 4."
            )
        assert not parts, "\n\n".join(parts)


class TestScaffoldJsonOutput:
    """Verify scaffold.py's JSON output is consistent with the filesystem."""

    def test_reported_files_match_disk(self, tmp_path):
        output = run_scaffold_write(tmp_path)
        actual_files, _ = collect_structure(tmp_path)
        reported = set(output["files"])

        unreported = actual_files - reported
        phantom = reported - actual_files

        parts = []
        if unreported:
            parts.append(f"Files on disk not in JSON output: {sorted(unreported)}")
        if phantom:
            parts.append(f"Files in JSON output not on disk: {sorted(phantom)}")
        assert not parts, "\n".join(parts)

    def test_reported_dirs_cover_disk(self, tmp_path):
        """Every actual directory should be a listed dir or a parent of one."""
        output = run_scaffold_write(tmp_path)
        _, actual_dirs = collect_structure(tmp_path)
        reported = {d.rstrip("/") for d in output["directories_created"]}

        uncovered = set()
        for d in actual_dirs:
            if d in reported:
                continue
            if any(r.startswith(d + "/") for r in reported):
                continue
            uncovered.add(d)

        assert not uncovered, (
            f"Directories on disk not covered by JSON output: {sorted(uncovered)}"
        )


class TestScaffoldContent:
    """Spot-check template content after scaffolding."""

    def test_project_name_replaced(self, tmp_path):
        run_scaffold_write(tmp_path)
        claude_md = (tmp_path / "CLAUDE.md").read_text(encoding="utf-8")
        assert "[Project Name]" not in claude_md
        assert tmp_path.name in claude_md

    def test_method_footer_present(self, tmp_path):
        run_scaffold_write(tmp_path)
        claude_md = (tmp_path / "CLAUDE.md").read_text(encoding="utf-8")
        assert "No-code method" in claude_md
        assert "Version" in claude_md

    def test_path_block_points_to_method_dir(self, tmp_path):
        run_scaffold_write(tmp_path)
        claude_md = (tmp_path / "CLAUDE.md").read_text(encoding="utf-8")
        assert '"_method/' in claude_md
