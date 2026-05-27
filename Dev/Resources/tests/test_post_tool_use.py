"""Tests for plugin/hooks/post_tool_use.py (PostToolUse hook).

The hook fires after Edit/Write/MultiEdit and validates structured
method docs at write time: BUILD-PLAN parse validation, scope-context
checks, TEST-LOG column counts, build-log entry structure, and proxy
format.
"""

import pytest
from conftest import run_hook, fixture_path


def _edit_input(cwd, file_path):
    return {
        "cwd": str(cwd),
        "tool_name": "Edit",
        "tool_input": {"file_path": file_path},
    }


def _assert_silent(code, raw):
    assert code == 0
    assert raw == ""


def _assert_warning(parsed, fragment=None):
    assert parsed is not None, "Expected warning output, got nothing"
    hso = parsed["hookSpecificOutput"]
    assert hso["hookEventName"] == "PostToolUse"
    assert "additionalContext" in hso
    if fragment:
        assert fragment in hso["additionalContext"]


class TestSilentCases:
    def test_non_writing_tool(self, adopted_folder):
        code, parsed, raw = run_hook(
            "post_tool_use.py",
            {"cwd": str(adopted_folder), "tool_name": "Read",
             "tool_input": {"file_path": str(adopted_folder / "UX.md")}},
        )
        _assert_silent(code, raw)

    def test_non_backlog_edit(self, adopted_folder):
        code, parsed, raw = run_hook(
            "post_tool_use.py",
            _edit_input(adopted_folder, str(adopted_folder / "UX.md")),
        )
        _assert_silent(code, raw)

    def test_empty_input(self):
        code, parsed, raw = run_hook("post_tool_use.py", {})
        _assert_silent(code, raw)


class TestValidBacklogEdit:
    def test_valid_folder_mode_edit_silent(self, adopted_folder):
        root = adopted_folder
        target = str(
            (root / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
        )
        code, parsed, raw = run_hook(
            "post_tool_use.py", _edit_input(root, target)
        )
        _assert_silent(code, raw)

    def test_valid_single_file_edit_silent(self, adopted_single_file):
        root = adopted_single_file
        target = str((root / "BUILD-PLAN.md").resolve())
        code, parsed, raw = run_hook(
            "post_tool_use.py", _edit_input(root, target)
        )
        _assert_silent(code, raw)


class TestTestLogValidation:
    def test_well_formed_test_log_silent(self):
        root = fixture_path("adopted_test_log_folder")
        target = str(
            (root / "test-log" / "001-first-batch.md").resolve()
        )
        code, parsed, raw = run_hook(
            "post_tool_use.py", _edit_input(root, target)
        )
        _assert_silent(code, raw)

    def test_flat_test_log_silent(self, adopted_folder):
        root = adopted_folder
        target = str((root / "TEST-LOG.md").resolve())
        code, parsed, raw = run_hook(
            "post_tool_use.py", _edit_input(root, target)
        )
        _assert_silent(code, raw)


class TestBuildLogValidation:
    def test_incomplete_build_log_warns(self):
        root = fixture_path("adopted_test_log_folder")
        target = str(
            (root / "build-log" / "001-first-batch.md").resolve()
        )
        code, parsed, raw = run_hook(
            "post_tool_use.py", _edit_input(root, target)
        )
        _assert_warning(parsed, "Build-log entry")


class TestProxyValidation:
    def test_operational_proxy_silent(self):
        root = fixture_path("adopted_test_log_folder")
        target = str(
            (root / "proxies" / "test-log.md").resolve()
        )
        code, parsed, raw = run_hook(
            "post_tool_use.py", _edit_input(root, target)
        )
        _assert_silent(code, raw)

    def test_operational_backlog_proxy_silent(self):
        root = fixture_path("adopted_test_log_folder")
        target = str(
            (root / "proxies" / "build-plan.md").resolve()
        )
        code, parsed, raw = run_hook(
            "post_tool_use.py", _edit_input(root, target)
        )
        _assert_silent(code, raw)
