"""Unit tests for plugin/scripts/parse_backlog.py.

Tests both direct function calls (import) and CLI invocation (subprocess).
"""

import json
import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).parent.parent / "plugin" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import parse_backlog as pb
from conftest import fixture_path, run_script


# ---------------------------------------------------------------------------
# parse_file_bullet
# ---------------------------------------------------------------------------

class TestParseFileBullet:
    def test_unticked_bullet(self):
        line = "- [ ] `app/src/Theme.kt` — Add dark mode theme support"
        result = pb.parse_file_bullet(line)
        assert result is not None
        assert result["path"] == "app/src/Theme.kt"
        assert result["ticked"] is False
        assert result["prerequisite"] is False

    def test_ticked_bullet(self):
        line = "- [x] `app/src/Theme.kt` — Theme done"
        result = pb.parse_file_bullet(line)
        assert result is not None
        assert result["ticked"] is True

    def test_prerequisite_label(self):
        line = "- [ ] `lib/util.py` — Add helper [Prerequisite, not in plan]"
        result = pb.parse_file_bullet(line)
        assert result is not None
        assert result["prerequisite"] is True
        assert "[Prerequisite" not in result["summary"]

    def test_non_bullet_returns_none(self):
        assert pb.parse_file_bullet("Just some text") is None

    def test_blank_returns_none(self):
        assert pb.parse_file_bullet("") is None


# ---------------------------------------------------------------------------
# parse_batch_body
# ---------------------------------------------------------------------------

class TestParseBatchBody:
    def test_valid_body(self):
        body = (
            "\n"
            "Changes:\n"
            "- [Requested] Do the thing\n"
            "\n"
            "Files:\n"
            "- [ ] `app/main.py` — Main entry point\n"
            "\n"
            "Serves UX.md: Dashboard.\n"
        )
        result = pb.parse_batch_body("Test batch", body)
        assert result is not None
        assert result["batch_heading"] == "Test batch"
        assert len(result["files"]) == 1
        assert result["files"][0]["path"] == "app/main.py"
        assert result["serves_ux"] == ["Dashboard"]
        assert result["change_list"] == ["[Requested] Do the thing"]

    def test_no_files_line_returns_none(self):
        body = "\nChanges:\n- Something\n"
        assert pb.parse_batch_body("No files", body) is None

    def test_empty_files_returns_none(self):
        body = "\nFiles:\n\nServes UX.md: X.\n"
        assert pb.parse_batch_body("Empty files", body) is None

    def test_template_placeholder_heading_returns_none(self):
        body = "\nFiles:\n- [ ] `real/path.py` — Something\n"
        assert pb.parse_batch_body("[short descriptive name]", body) is None

    def test_template_placeholder_path_returns_none(self):
        body = "\nFiles:\n- [ ] `[path/to/file]` — Something\n"
        assert pb.parse_batch_body("Real batch", body) is None


# ---------------------------------------------------------------------------
# find_top_unticked_batch (single-file text-only)
# ---------------------------------------------------------------------------

class TestFindTopUntickedBatch:
    def test_finds_unticked_batch_single_file(self):
        text = (fixture_path("adopted_single_file") / "BACKLOG.md").read_text(
            encoding="utf-8"
        )
        result = pb.find_top_unticked_batch(text)
        assert result != {}
        assert result["batch_heading"] == "Add dark mode"
        assert len(result["files"]) == 2
        assert all(not f["ticked"] for f in result["files"])

    def test_no_section_returns_empty(self):
        assert pb.find_top_unticked_batch("# No build batches here") == {}

    def test_empty_section_returns_empty(self):
        text = "## Build batches\n\n## Open questions\n"
        assert pb.find_top_unticked_batch(text) == {}

    def test_all_ticked_returns_empty(self):
        text = (
            "## Build batches\n\n"
            "### Batch: Done batch\n\n"
            "Files:\n"
            "- [x] `a.py` — Done\n"
            "- [x] `b.py` — Done\n\n"
            "## Open questions\n"
        )
        assert pb.find_top_unticked_batch(text) == {}


# ---------------------------------------------------------------------------
# find_top_unticked_batch_from_path (auto-detecting, folder mode)
# ---------------------------------------------------------------------------

class TestFindTopUntickedBatchFromPath:
    def test_folder_mode(self):
        index_path = fixture_path("adopted_folder") / "BACKLOG" / "INDEX.md"
        result = pb.find_top_unticked_batch_from_path(index_path)
        assert result != {}
        assert result["batch_heading"] == "Add settings screen"
        assert "batch_file" in result
        assert result["batch_file"] == "0001-add-settings-screen.md"

    def test_single_file_mode(self):
        path = fixture_path("adopted_single_file") / "BACKLOG.md"
        result = pb.find_top_unticked_batch_from_path(path)
        assert result != {}
        assert result["batch_heading"] == "Add dark mode"

    def test_missing_file_returns_empty(self):
        assert pb.find_top_unticked_batch_from_path(Path("/nonexistent.md")) == {}


# ---------------------------------------------------------------------------
# is_folder_mode
# ---------------------------------------------------------------------------

class TestIsFolderMode:
    def test_index_md_is_folder_mode(self):
        index_path = fixture_path("adopted_folder") / "BACKLOG" / "INDEX.md"
        assert pb.is_folder_mode(index_path) is True

    def test_single_file_is_not_folder_mode(self):
        path = fixture_path("adopted_single_file") / "BACKLOG.md"
        assert pb.is_folder_mode(path) is False


# ---------------------------------------------------------------------------
# CLI invocation via subprocess
# ---------------------------------------------------------------------------

class TestCLI:
    def test_folder_mode_cli(self):
        index_path = str(
            fixture_path("adopted_folder") / "BACKLOG" / "INDEX.md"
        )
        exit_code, stdout, stderr = run_script("parse_backlog.py", [index_path])
        assert exit_code == 0
        data = json.loads(stdout)
        assert data.get("batch_heading") == "Add settings screen"

    def test_single_file_cli(self):
        path = str(fixture_path("adopted_single_file") / "BACKLOG.md")
        exit_code, stdout, stderr = run_script("parse_backlog.py", [path])
        assert exit_code == 0
        data = json.loads(stdout)
        assert data.get("batch_heading") == "Add dark mode"

    def test_no_args_returns_empty(self):
        exit_code, stdout, stderr = run_script("parse_backlog.py", [])
        assert exit_code == 0
        assert json.loads(stdout) == {}

    def test_missing_file_returns_empty(self):
        exit_code, stdout, stderr = run_script(
            "parse_backlog.py", ["/nonexistent/BACKLOG.md"]
        )
        assert exit_code == 0
        assert json.loads(stdout) == {}
