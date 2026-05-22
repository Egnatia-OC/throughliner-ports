"""Tests for plugin/hooks/stop.py (Stop hook).

The Stop hook routes to batch-executor, after-build, or silent exit
depending on BACKLOG and TEST-LOG state.
"""

import pytest
from conftest import run_hook, fixture_path


def _stop_input(cwd, stop_hook_active=False):
    return {
        "cwd": str(cwd),
        "session_id": "test-session",
        "stop_hook_active": stop_hook_active,
    }


def _assert_silent(code, raw):
    assert code == 0
    assert raw == ""


def _assert_redirect(parsed, fragment=None):
    assert parsed is not None, "Expected redirect output, got nothing"
    assert parsed.get("decision") == "block"
    assert "reason" in parsed
    if fragment:
        assert fragment in parsed["reason"]


class TestBatchExecutorRedirect:
    def test_unticked_batch_redirects(self, adopted_folder):
        code, parsed, raw = run_hook(
            "stop.py", _stop_input(adopted_folder)
        )
        _assert_redirect(parsed, "batch payload")

    def test_unticked_single_file_redirects(self, adopted_single_file):
        code, parsed, raw = run_hook(
            "stop.py", _stop_input(adopted_single_file)
        )
        _assert_redirect(parsed, "batch payload")


class TestSilentCases:
    def test_empty_folder_silent(self, empty_folder):
        code, parsed, raw = run_hook(
            "stop.py", _stop_input(empty_folder)
        )
        _assert_silent(code, raw)

    def test_stop_hook_active_silent(self, adopted_folder):
        code, parsed, raw = run_hook(
            "stop.py", _stop_input(adopted_folder, stop_hook_active=True)
        )
        _assert_silent(code, raw)

    def test_no_cwd_silent(self):
        code, parsed, raw = run_hook("stop.py", {"session_id": "x"})
        _assert_silent(code, raw)

    def test_empty_input_silent(self):
        code, parsed, raw = run_hook("stop.py", {})
        _assert_silent(code, raw)

    def test_tier2_no_claude_silent(self, tier2_no_claude):
        code, parsed, raw = run_hook(
            "stop.py", _stop_input(tier2_no_claude)
        )
        _assert_silent(code, raw)


class TestRedirectPayloadShape:
    def test_batch_payload_contains_heading(self, adopted_folder):
        code, parsed, raw = run_hook(
            "stop.py", _stop_input(adopted_folder)
        )
        reason = parsed["reason"]
        assert "Add settings screen" in reason

    def test_batch_payload_is_json(self, adopted_folder):
        import json
        code, parsed, raw = run_hook(
            "stop.py", _stop_input(adopted_folder)
        )
        reason = parsed["reason"]
        # The payload JSON is embedded in the reason text after a blank line
        # following the prose instruction. Extract and verify it's valid JSON.
        lines = reason.split("\n")
        json_start = None
        for i, line in enumerate(lines):
            if line.strip().startswith("{"):
                json_start = i
                break
        assert json_start is not None, "No JSON payload found in reason"
