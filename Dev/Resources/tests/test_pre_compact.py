"""Tests for the PreCompact hook (plugin/hooks/pre_compact.py)."""

from conftest import run_hook, fixture_path


def test_blocks_when_active_build(adopted_folder):
    """PreCompact should block when a build batch has unticked files."""
    data = {"cwd": str(adopted_folder), "hook_event_name": "PreCompact"}
    code, parsed, raw = run_hook("pre_compact.py", data)
    assert code == 0
    assert parsed is not None
    assert parsed["decision"] == "block"
    assert "No-code method" in parsed["reason"]
    assert "tokens" in parsed["reason"].lower()
    assert "handoff" in parsed["reason"].lower()


def test_silent_when_no_active_build(empty_folder):
    """PreCompact should allow compaction when no build batch exists."""
    data = {"cwd": str(empty_folder), "hook_event_name": "PreCompact"}
    code, parsed, raw = run_hook("pre_compact.py", data)
    assert code == 0
    assert parsed is None


def test_silent_when_no_cwd():
    """PreCompact should allow compaction when cwd is missing."""
    data = {"hook_event_name": "PreCompact"}
    code, parsed, raw = run_hook("pre_compact.py", data)
    assert code == 0
    assert parsed is None


def test_silent_when_malformed_input():
    """PreCompact should allow compaction on malformed input."""
    data = {"cwd": 12345}
    code, parsed, raw = run_hook("pre_compact.py", data)
    assert code == 0
    assert parsed is None


def test_silent_for_single_file_backlog_with_active_build(adopted_single_file):
    """PreCompact should also detect active builds in single-file BUILD-PLAN."""
    data = {"cwd": str(adopted_single_file), "hook_event_name": "PreCompact"}
    code, parsed, raw = run_hook("pre_compact.py", data)
    assert code == 0
    assert parsed is not None
    assert parsed["decision"] == "block"


def test_block_reason_includes_paste_prompt(adopted_folder):
    """The block reason should include a paste-ready prompt for the user."""
    data = {"cwd": str(adopted_folder), "hook_event_name": "PreCompact"}
    code, parsed, raw = run_hook("pre_compact.py", data)
    assert code == 0
    assert "Copy and paste" in parsed["reason"]
    assert "prepare a handoff" in parsed["reason"]
