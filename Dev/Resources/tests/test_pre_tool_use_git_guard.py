"""Tests for plugin/hooks/pre_tool_use_git_guard.py (V34 git safety guard)."""

import pytest
from conftest import run_hook


def _bash_input(command, permission_mode=""):
    d = {
        "tool_name": "Bash",
        "tool_input": {"command": command},
    }
    if permission_mode:
        d["permission_mode"] = permission_mode
    return d


def _assert_deny(parsed, fragment=None):
    assert parsed is not None, "Expected deny output, got nothing"
    hso = parsed["hookSpecificOutput"]
    assert hso["permissionDecision"] == "deny"
    if fragment:
        assert fragment in hso["permissionDecisionReason"]


def _assert_allow(code, raw):
    assert code == 0
    assert raw == ""


class TestResetHard:
    def test_blocked(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git reset --hard HEAD~1"),
        )
        _assert_deny(parsed, "git reset --hard")

    def test_soft_reset_allowed(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git reset --soft HEAD~1"),
        )
        _assert_allow(code, raw)

    def test_mixed_reset_allowed(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git reset HEAD~1"),
        )
        _assert_allow(code, raw)


class TestPushForce:
    def test_blocked(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git push --force origin main"),
        )
        _assert_deny(parsed, "git push --force")

    def test_short_flag_blocked(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git push -f origin main"),
        )
        _assert_deny(parsed, "git push --force")

    def test_force_with_lease_allowed(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git push --force-with-lease origin main"),
        )
        _assert_allow(code, raw)

    def test_normal_push_allowed(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git push origin main"),
        )
        _assert_allow(code, raw)


class TestModeAwareSuffix:
    def test_auto_mode_includes_suffix(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git reset --hard", permission_mode="Auto"),
        )
        _assert_deny(parsed, "permission mode")

    def test_default_mode_no_suffix(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("git reset --hard"),
        )
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "permission mode" not in reason


class TestPassthrough:
    def test_non_git_command(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            _bash_input("ls -la"),
        )
        _assert_allow(code, raw)

    def test_empty_command(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            {"tool_name": "Bash", "tool_input": {"command": ""}},
        )
        _assert_allow(code, raw)

    def test_missing_command(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py",
            {"tool_name": "Bash", "tool_input": {}},
        )
        _assert_allow(code, raw)

    def test_malformed_input(self):
        code, parsed, raw = run_hook(
            "pre_tool_use_git_guard.py", {}
        )
        _assert_allow(code, raw)
