"""Tests for plugin/hooks/session_start.py (SessionStart hook).

Each test pipes synthetic JSON into the hook subprocess and asserts on
the exit code and stdout JSON shape.
"""

import pytest
from conftest import run_hook, fixture_path


class TestTier1Silent:
    """Tier 1 (genuinely empty folder) — hook writes nothing, exit 0."""

    def test_empty_folder_silent(self, empty_folder):
        code, parsed, raw = run_hook(
            "session_start.py", {"cwd": str(empty_folder)}
        )
        assert code == 0
        assert raw == ""


class TestTier2GapFlag:
    """Tier 2 (partial method shape) — hook emits additionalContext."""

    def test_no_claude_md(self, tier2_no_claude):
        code, parsed, raw = run_hook(
            "session_start.py", {"cwd": str(tier2_no_claude)}
        )
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "Partial method shape" in ctx
        assert "/setup" in ctx

    def test_bad_path_block(self, tier2_bad_pathblock):
        code, parsed, raw = run_hook(
            "session_start.py", {"cwd": str(tier2_bad_pathblock)}
        )
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "Partial method shape" in ctx


class TestTier3StateSummary:
    """Tier 3 (complete method project) — hook emits full state summary."""

    def test_adopted_folder_emits_state(self, adopted_folder):
        code, parsed, raw = run_hook(
            "session_start.py", {"cwd": str(adopted_folder)}
        )
        assert code == 0
        assert parsed is not None
        hso = parsed["hookSpecificOutput"]
        assert hso["hookEventName"] == "SessionStart"
        ctx = hso["additionalContext"]
        assert "Project state" in ctx
        assert "Path block" in ctx

    def test_adopted_single_file_emits_state(self, adopted_single_file):
        code, parsed, raw = run_hook(
            "session_start.py", {"cwd": str(adopted_single_file)}
        )
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "Project state" in ctx

    def test_top_build_batch_mentioned(self, adopted_folder):
        code, parsed, _ = run_hook(
            "session_start.py", {"cwd": str(adopted_folder)}
        )
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "Add settings screen" in ctx

    def test_red_flags_surfaced(self, adopted_folder):
        """V54: Non-empty Red flags section triggers a prominent warning."""
        code, parsed, _ = run_hook(
            "session_start.py", {"cwd": str(adopted_folder)}
        )
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "Active Red flags" in ctx
        assert "API tokens stored in plain text" in ctx

    def test_red_flags_empty_no_warning(self, adopted_single_file):
        """Red flags section that's empty produces no warning."""
        code, parsed, _ = run_hook(
            "session_start.py", {"cwd": str(adopted_single_file)}
        )
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "Active Red flags" not in ctx


class TestV29UnadoptedAdvisory:
    """V29 — unadopted folder with work emits advisory."""

    def test_unadopted_foreign_emits_advisory(self, unadopted_foreign):
        code, parsed, raw = run_hook(
            "session_start.py", {"cwd": str(unadopted_foreign)}
        )
        assert code == 0
        assert parsed is not None
        assert "systemMessage" in parsed
        assert "/setup" in parsed["systemMessage"]
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "unadopted" in ctx.lower()


class TestMalformedInput:
    """Hook handles bad stdin gracefully."""

    def test_empty_stdin(self):
        code, parsed, raw = run_hook("session_start.py", {})
        assert code == 0

    def test_non_dict_cwd(self):
        code, parsed, raw = run_hook("session_start.py", {"cwd": 42})
        assert code == 0
