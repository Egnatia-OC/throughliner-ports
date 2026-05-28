"""Tests for plugin/scripts/validate_docs.py (structured-markdown validator).

Unit tests for each validator function. Uses inline strings, no fixture
directories needed.
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "plugin" / "scripts"))
from validate_docs import (
    validate_test_log,
    validate_build_log_entry,
    validate_scope_context,
    validate_proxy,
)


# --- TEST-LOG validator ---


class TestValidateTestLog:
    WELL_FORMED = (
        "| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed Explicitly | Notes |\n"
        "|---|------|---------|-----------|------------------|------|----------|--------|---------------------|-------|\n"
        "| 001 | 2026-05-20 | B001 | Widget | Widget renders | Look and click | User | Pass | Yes (2026-05-21) | |\n"
    )

    def test_well_formed_no_warnings(self):
        assert validate_test_log(self.WELL_FORMED) == []

    def test_missing_column_warns(self):
        bad_row = (
            "| # | Date | Session | Component | Test Description | Type | Verifier | Status | Notes |\n"
            "|---|------|---------|-----------|------------------|------|----------|--------|-------|\n"
            "| 001 | 2026-05-20 | B001 | Widget | Widget renders | Look and click | User | Pass | |\n"
        )
        warnings = validate_test_log(bad_row)
        assert len(warnings) == 3
        assert "9 columns" in warnings[0]

    def test_extra_column_warns(self):
        bad_row = (
            "| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed | Notes | Extra |\n"
            "|---|------|---------|-----------|------------------|------|----------|--------|-----------|-------|-------|\n"
        )
        warnings = validate_test_log(bad_row)
        assert len(warnings) == 2
        assert "11 columns" in warnings[0]

    def test_non_table_lines_ignored(self):
        text = "# Title\n\nSome paragraph.\n\n- bullet\n"
        assert validate_test_log(text) == []

    def test_empty_string(self):
        assert validate_test_log("") == []

    def test_none_input(self):
        assert validate_test_log(None) == []

    def test_mixed_good_and_bad_rows(self):
        text = (
            "| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed Explicitly | Notes |\n"
            "|---|------|---------|-----------|------------------|------|----------|--------|---------------------|-------|\n"
            "| 001 | 2026-05-20 | B001 | Widget | Renders | Look and click | User | Pass | Yes | |\n"
            "| 002 | 2026-05-20 | B001 | Widget | Broken row missing cols |\n"
        )
        warnings = validate_test_log(text)
        assert len(warnings) == 1
        assert "Line 4" in warnings[0]

    def test_single_pipe_not_table(self):
        text = "Some text | with a pipe\n"
        assert validate_test_log(text) == []


# --- Build-log entry validator ---


class TestValidateBuildLogEntry:
    WELL_FORMED = (
        "# B001 — 2026-05-20 — First batch\n\n"
        "**What shipped.** Dashboard screen.\n\n"
        "**Decisions taken and why.** Simple layout.\n\n"
        "**Pivots and surprises.** None.\n\n"
        "## Performance\n"
        "- **Batch completion:** Complete\n"
        "- **Files in batch:** 2\n"
    )

    def test_well_formed_no_warnings(self):
        assert validate_build_log_entry(self.WELL_FORMED) == []

    def test_missing_performance_warns(self):
        no_perf = (
            "# B001 — 2026-05-20\n\n"
            "**What shipped.** Something.\n\n"
            "**Decisions taken and why.** Some.\n\n"
            "**Pivots and surprises.** None.\n"
        )
        warnings = validate_build_log_entry(no_perf)
        assert len(warnings) == 1
        assert "Performance" in warnings[0]

    def test_missing_what_shipped_warns(self):
        text = (
            "# B001\n\n"
            "**Decisions taken and why.** Some.\n\n"
            "**Pivots and surprises.** None.\n\n"
            "## Performance\n"
        )
        warnings = validate_build_log_entry(text)
        assert len(warnings) == 1
        assert "What shipped" in warnings[0]

    def test_missing_multiple_sections(self):
        text = "# B001\n\nSome text.\n"
        warnings = validate_build_log_entry(text)
        assert len(warnings) == 4

    def test_empty_string(self):
        assert validate_build_log_entry("") == []

    def test_none_input(self):
        assert validate_build_log_entry(None) == []

    def test_case_insensitive_match(self):
        text = (
            "# B001\n\n"
            "**what shipped.** Something.\n\n"
            "**decisions taken and why.** Some.\n\n"
            "**pivots and surprises.** None.\n\n"
            "## Performance\n"
        )
        assert validate_build_log_entry(text) == []


# --- Scope-context validator ---


class TestValidateScopeContext:
    WELL_FORMED = (
        "# Add settings screen\n\n"
        "Status: active\n\n"
        "**Goal.** Add a settings screen.\n\n"
        "**Outputs.** A new settings screen.\n\n"
        "**Success criteria.** User can open settings.\n\n"
        "Changes:\n"
        "- [Requested] Add settings screen\n"
    )

    def test_well_formed_no_warnings(self):
        assert validate_scope_context(self.WELL_FORMED) == []

    def test_missing_goal_warns(self):
        text = (
            "# Add feature\n\n"
            "**Outputs.** Something new.\n\n"
            "**Success criteria.** It works.\n\n"
            "Changes:\n- [Requested] Do it\n"
        )
        warnings = validate_scope_context(text)
        assert len(warnings) == 1
        assert "Goal" in warnings[0]

    def test_missing_all_scope_sections(self):
        text = (
            "# Add feature\n\n"
            "Changes:\n"
            "- [Requested] Do something\n\n"
            "Files:\n"
            "- [ ] `app/main.py` — Main file\n"
        )
        warnings = validate_scope_context(text)
        assert len(warnings) == 3

    def test_heading_only_no_warnings(self):
        text = "# Add feature\n"
        assert validate_scope_context(text) == []

    def test_no_heading_no_warnings(self):
        text = "Some random text without a heading.\n"
        assert validate_scope_context(text) == []

    def test_empty_string(self):
        assert validate_scope_context("") == []

    def test_none_input(self):
        assert validate_scope_context(None) == []

    def test_minimal_content_skipped(self):
        text = "# Batch\n\nStatus: queued\n"
        assert validate_scope_context(text) == []


# --- Proxy validator ---


class TestValidateProxy:
    WELL_FORMED = (
        "<!-- proxy | source: UX.md | generated: 2026-05-20 -->\n\n"
        "# UX — Test Project\n\n"
        "2 principles, 3 functionalities.\n\n"
        "## Entries\n\n"
        "- L5 **Principle 1** — summary\n"
    )

    def test_well_formed_no_warnings(self):
        assert validate_proxy(self.WELL_FORMED, "ux.md") == []

    def test_missing_header_warns(self):
        text = (
            "# UX — Test Project\n\n"
            "## Entries\n\n"
            "- L5 **Principle 1** — summary\n"
        )
        warnings = validate_proxy(text, "ux.md")
        assert len(warnings) == 1
        assert "proxy header" in warnings[0].lower()

    def test_operational_proxy_skipped(self):
        text = "# BACKLOG — Test Project\n\nSome index content.\n"
        assert validate_proxy(text, "backlog.md") == []
        assert validate_proxy(text, "build-log.md") == []

    def test_no_filename_checks_header(self):
        text = "# Some proxy\n\nNo header here.\n"
        warnings = validate_proxy(text)
        assert len(warnings) == 1

    def test_empty_string(self):
        assert validate_proxy("") == []

    def test_none_input(self):
        assert validate_proxy(None) == []

    def test_malformed_header_warns(self):
        text = "<!-- proxy | source: UX.md -->\n\n# UX\n"
        warnings = validate_proxy(text, "ux.md")
        assert len(warnings) == 1

    def test_header_with_extra_spaces_ok(self):
        text = "<!--  proxy  |  source:  UX.md  |  generated:  2026-05-20  -->\n"
        assert validate_proxy(text, "ux.md") == []
