"""Unit tests for plugin/scripts/project_state.py."""

import sys
from pathlib import Path

import pytest

# Make plugin/scripts/ importable.
SCRIPTS_DIR = Path(__file__).parent.parent.parent.parent / "plugin" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import project_state as ps
from conftest import fixture_path


# ---------------------------------------------------------------------------
# has_method_footer / extract_footer_version
# ---------------------------------------------------------------------------

class TestFooterDetection:
    def test_footer_present(self):
        assert ps.has_method_footer("*No-code method — Version 52.*")

    def test_footer_absent(self):
        assert not ps.has_method_footer("# My Project\nNo footer here.")

    def test_footer_non_string(self):
        assert not ps.has_method_footer(None)
        assert not ps.has_method_footer(42)

    def test_extract_version_number(self):
        assert ps.extract_footer_version("*No-code method — Version 52.*") == 52

    def test_extract_version_none_when_missing(self):
        assert ps.extract_footer_version("no footer") is None

    def test_extract_version_none_for_non_string(self):
        assert ps.extract_footer_version(None) is None


# ---------------------------------------------------------------------------
# safe_read_text
# ---------------------------------------------------------------------------

class TestSafeReadText:
    def test_reads_existing_file(self):
        p = fixture_path("adopted_folder") / "CLAUDE.md"
        text = ps.safe_read_text(p)
        assert text is not None
        assert "No-code method" in text

    def test_returns_none_for_missing_file(self):
        assert ps.safe_read_text(Path("/nonexistent/file.md")) is None


# ---------------------------------------------------------------------------
# extract_path_block
# ---------------------------------------------------------------------------

class TestExtractPathBlock:
    def test_parses_valid_path_block(self):
        text = fixture_path("adopted_folder") / "CLAUDE.md"
        claude_text = ps.safe_read_text(text)
        block = ps.extract_path_block(claude_text)
        assert isinstance(block, dict)
        assert "UX.md" in block
        assert block["BACKLOG.md"] == "BACKLOG/INDEX.md"

    def test_returns_none_for_no_block(self):
        assert ps.extract_path_block("# Just a heading\nNo code block.") is None

    def test_returns_none_for_non_string(self):
        assert ps.extract_path_block(None) is None

    def test_returns_none_for_non_dict_json(self):
        text = '```json\n["not", "a", "dict"]\n```'
        assert ps.extract_path_block(text) is None


# ---------------------------------------------------------------------------
# resolve_path_block_entry
# ---------------------------------------------------------------------------

class TestResolvePathBlockEntry:
    def test_resolves_ux(self):
        root = fixture_path("adopted_folder")
        result = ps.resolve_path_block_entry(root, "UX.md")
        assert result is not None
        assert result.name == "UX.md"
        assert result.exists()

    def test_resolves_backlog_index(self):
        root = fixture_path("adopted_folder")
        result = ps.resolve_path_block_entry(root, "BACKLOG.md")
        assert result is not None
        assert result.name == "INDEX.md"

    def test_returns_none_for_missing_claude(self):
        root = fixture_path("tier2_no_claude")
        assert ps.resolve_path_block_entry(root, "UX.md") is None

    def test_returns_none_for_bad_path_block(self):
        root = fixture_path("tier2_bad_pathblock")
        assert ps.resolve_path_block_entry(root, "UX.md") is None


# ---------------------------------------------------------------------------
# is_unadopted_with_work
# ---------------------------------------------------------------------------

class TestIsUnadoptedWithWork:
    def test_adopted_folder_returns_false(self):
        assert not ps.is_unadopted_with_work(fixture_path("adopted_folder"))

    def test_empty_folder_returns_false(self):
        assert not ps.is_unadopted_with_work(fixture_path("empty"))

    def test_unadopted_foreign_returns_true(self):
        assert ps.is_unadopted_with_work(fixture_path("unadopted_foreign_claude"))


# ---------------------------------------------------------------------------
# detect_adopt_case
# ---------------------------------------------------------------------------

class TestDetectAdoptCase:
    def test_empty_is_case_1(self):
        assert ps.detect_adopt_case(fixture_path("empty")) == ps.ADOPT_CASE_EMPTY

    def test_unadopted_foreign_is_case_3(self):
        assert ps.detect_adopt_case(
            fixture_path("unadopted_foreign_claude")
        ) == ps.ADOPT_CASE_CODE_FOREIGN_DOCS

    def test_adopted_folder_is_case_4(self):
        assert ps.detect_adopt_case(
            fixture_path("adopted_folder")
        ) == ps.ADOPT_CASE_ALREADY_ADOPTED

    def test_adopted_single_file_is_case_4(self):
        assert ps.detect_adopt_case(
            fixture_path("adopted_single_file")
        ) == ps.ADOPT_CASE_ALREADY_ADOPTED


# ---------------------------------------------------------------------------
# parse_test_log_rows / is_row_confirmed
# ---------------------------------------------------------------------------

class TestTestLogParsing:
    def test_parses_10_column_row(self):
        text = ps.safe_read_text(fixture_path("adopted_folder") / "TEST-LOG.md")
        rows = ps.parse_test_log_rows(text)
        assert len(rows) == 1
        r = rows[0]
        assert r["id"] == "001"
        assert r["session"] == "v1"
        assert r["status"] == "Pass"
        assert r["type"] == "Look and click"
        assert r["verifier"] == "User"

    def test_confirmed_row(self):
        row = {"confirmed_explicitly": "Yes (2026-05-21)"}
        assert ps.is_row_confirmed(row)

    def test_unconfirmed_row(self):
        row = {"confirmed_explicitly": "No"}
        assert not ps.is_row_confirmed(row)

    def test_empty_confirmed_field(self):
        row = {"confirmed_explicitly": ""}
        assert not ps.is_row_confirmed(row)

    def test_empty_text_returns_empty(self):
        assert ps.parse_test_log_rows("") == []

    def test_non_string_returns_empty(self):
        assert ps.parse_test_log_rows(None) == []


# ---------------------------------------------------------------------------
# identify_previous_session (folder-mode build log)
# ---------------------------------------------------------------------------

class TestIdentifyPreviousSession:
    def test_folder_mode(self):
        root = fixture_path("adopted_folder")
        session_id, status = ps.identify_previous_session(root)
        assert status == "ok"
        assert session_id == "v1"

    def test_single_file_mode(self):
        root = fixture_path("adopted_single_file")
        session_id, status = ps.identify_previous_session(root)
        assert status == "ok"
        assert session_id == "v1"

    def test_missing_build_log(self):
        root = fixture_path("empty")
        _id, status = ps.identify_previous_session(root)
        assert status == "missing"

    def test_proxy_mode(self):
        root = fixture_path("adopted_proxy")
        session_id, status = ps.identify_previous_session(root)
        assert status == "ok"
        assert session_id == "B001"


# ---------------------------------------------------------------------------
# get_unconfirmed_previous_session_rows
# ---------------------------------------------------------------------------

class TestGetUnconfirmedRows:
    def test_all_confirmed_returns_empty(self):
        root = fixture_path("adopted_folder")
        rows, _status, _sid = ps.get_unconfirmed_previous_session_rows(root)
        assert rows == []

    def test_missing_test_log_returns_empty(self):
        root = fixture_path("empty")
        rows, status, _sid = ps.get_unconfirmed_previous_session_rows(root)
        assert rows == []
        assert status == "missing"

    def test_folder_mode_finds_unconfirmed(self):
        root = fixture_path("adopted_test_log_folder")
        rows, status, session_id = ps.get_unconfirmed_previous_session_rows(root)
        assert status == "ok"
        assert session_id == "B001"
        assert len(rows) == 1
        assert rows[0]["id"] == "002"
        assert rows[0]["description"] == "Widget handles empty state"

    def test_folder_mode_collect_all_rows(self):
        root = fixture_path("adopted_test_log_folder")
        rows, is_folder = ps.collect_all_test_log_rows(root)
        assert is_folder is True
        assert len(rows) == 2

    def test_resolve_test_log_dir_folder_mode(self):
        root = fixture_path("adopted_test_log_folder")
        d = ps.resolve_test_log_dir(root)
        assert d is not None
        assert d.name == "test-log"

    def test_resolve_test_log_dir_single_file_returns_none(self):
        root = fixture_path("adopted_single_file")
        assert ps.resolve_test_log_dir(root) is None


# ---------------------------------------------------------------------------
# is_backlog_file / resolve_backlog_dir
# ---------------------------------------------------------------------------

class TestBacklogHelpers:
    def test_folder_mode_index_is_backlog(self):
        root = fixture_path("adopted_folder")
        target = root / "BACKLOG" / "INDEX.md"
        assert ps.is_backlog_file(target, root)

    def test_folder_mode_batch_file_is_backlog(self):
        root = fixture_path("adopted_folder")
        target = root / "BACKLOG" / "0001-add-settings-screen.md"
        assert ps.is_backlog_file(target, root)

    def test_single_file_is_backlog(self):
        root = fixture_path("adopted_single_file")
        target = root / "BACKLOG.md"
        assert ps.is_backlog_file(target, root)

    def test_random_file_is_not_backlog(self):
        root = fixture_path("adopted_folder")
        target = root / "UX.md"
        assert not ps.is_backlog_file(target, root)

    def test_resolve_backlog_dir_folder_mode(self):
        root = fixture_path("adopted_folder")
        d = ps.resolve_backlog_dir(root)
        assert d is not None
        assert d.name == "BACKLOG"

    def test_resolve_backlog_dir_single_file_returns_none(self):
        root = fixture_path("adopted_single_file")
        assert ps.resolve_backlog_dir(root) is None

    def test_proxy_as_index_is_backlog(self):
        root = fixture_path("adopted_proxy")
        target = root / "proxies" / "backlog.md"
        assert ps.is_backlog_file(target, root)

    def test_proxy_as_index_batch_file_is_backlog(self):
        root = fixture_path("adopted_proxy")
        target = root / "BACKLOG" / "0001-first-batch.md"
        assert ps.is_backlog_file(target, root)

    def test_resolve_backlog_dir_proxy_mode(self):
        root = fixture_path("adopted_proxy")
        d = ps.resolve_backlog_dir(root)
        assert d is not None
        assert d.name == "BACKLOG"
