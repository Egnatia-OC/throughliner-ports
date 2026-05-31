"""Tests for plugin/hooks/pre_tool_use.py (PreToolUse hook).

Tests each deny path: V29 adoption gate, locked-doc enforcement,
serves-line check, batch boundary check, V39 read-before-edit gate,
V27 test-confirmation gate, and V56 project-boundary check.
Also tests allow paths.
"""

import pytest
from conftest import run_hook, fixture_path


def _edit_input(cwd, file_path, old_string="x", new_string="y", **extra):
    """Build a PreToolUse stdin dict for an Edit tool call."""
    d = {
        "cwd": str(cwd),
        "tool_name": "Edit",
        "tool_input": {
            "file_path": file_path,
            "old_string": old_string,
            "new_string": new_string,
        },
    }
    d.update(extra)
    return d


def _write_input(cwd, file_path, content="hello", **extra):
    d = {
        "cwd": str(cwd),
        "tool_name": "Write",
        "tool_input": {"file_path": file_path, "content": content},
    }
    d.update(extra)
    return d


def _bash_input(cwd, command, tool_name="Bash", **extra):
    """Build a PreToolUse stdin dict for a Bash or PowerShell tool call."""
    d = {
        "cwd": str(cwd),
        "tool_name": tool_name,
        "tool_input": {"command": command},
    }
    d.update(extra)
    return d


def _assert_deny(parsed, fragment=None):
    """Assert that the hook denied and optionally check reason text."""
    assert parsed is not None, "Expected deny output, got nothing"
    hso = parsed["hookSpecificOutput"]
    assert hso["permissionDecision"] == "deny"
    if fragment:
        assert fragment in hso["permissionDecisionReason"]


def _assert_allow(code, raw):
    """Assert that the hook allowed (no output)."""
    assert code == 0
    assert raw == ""


# ---------------------------------------------------------------------------
# Non-writing tools pass through
# ---------------------------------------------------------------------------

class TestPassthrough:
    def test_read_tool_allowed(self, adopted_folder):
        code, parsed, raw = run_hook(
            "pre_tool_use.py",
            {"cwd": str(adopted_folder), "tool_name": "Read",
             "tool_input": {"file_path": "UX.md"}},
        )
        _assert_allow(code, raw)

    def test_grep_tool_allowed(self, adopted_folder):
        code, parsed, raw = run_hook(
            "pre_tool_use.py",
            {"cwd": str(adopted_folder), "tool_name": "Grep",
             "tool_input": {"pattern": "test"}},
        )
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# V29 adoption gate
# ---------------------------------------------------------------------------

class TestV29AdoptionGate:
    def test_edit_non_scaffold_denied(self, unadopted_foreign):
        root = unadopted_foreign
        data = _edit_input(root, str(root / "package.json"))
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "unadopted")

    def test_edit_scaffold_allowed(self, unadopted_foreign):
        root = unadopted_foreign
        data = _edit_input(root, str(root / "CLAUDE.md"))
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_v43_mode_aware_suffix(self, unadopted_foreign):
        root = unadopted_foreign
        data = _edit_input(
            root, str(root / "package.json"), permission_mode="Auto"
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "permission mode")


# ---------------------------------------------------------------------------
# V56 project-boundary check
# ---------------------------------------------------------------------------

class TestProjectBoundary:
    """V91: unconditional project-boundary block removed for Write/Edit/
    MultiEdit. Writes outside project root now fall through to planning/
    build phase checks. Bash write-guard retains its own boundary."""

    def test_edit_outside_project_still_denied(self, adopted_folder):
        """External files still denied by downstream checks, not boundary."""
        outside_path = str((adopted_folder.parent / "other-project" / "file.txt").resolve())
        data = _edit_input(adopted_folder, outside_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "outside the project root" not in reason

    def test_write_outside_project_still_denied(self, adopted_folder):
        outside_path = str((adopted_folder.parent / "other-project" / "file.txt").resolve())
        data = _write_input(adopted_folder, outside_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "outside the project root" not in reason

    def test_edit_inside_project_allowed(self, adopted_folder):
        inside_path = str((adopted_folder / "app" / "src" / "SettingsScreen.kt").resolve())
        data = _edit_input(adopted_folder, inside_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        if raw:
            reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
            assert "outside the project root" not in reason

    def test_edit_project_root_file_allowed(self, adopted_folder):
        root_file = str((adopted_folder / "MANIFEST.md").resolve())
        data = _edit_input(adopted_folder, root_file)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# Locked-doc enforcement
# ---------------------------------------------------------------------------

class TestLockedDocEnforcement:
    def test_edit_ux_denied(self, adopted_folder):
        root = adopted_folder
        ux_path = str((root / "UX.md").resolve())
        data = _edit_input(root, ux_path, old_string="Dashboard", new_string="Home")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "locked source-of-truth")

    def test_edit_backlog_allowed(self, adopted_folder):
        root = adopted_folder
        bl_path = str((root / "BACKLOG" / "INDEX.md").resolve())
        data = _edit_input(root, bl_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_edit_manifest_allowed(self, adopted_folder):
        root = adopted_folder
        path = str((root / "MANIFEST.md").resolve())
        data = _edit_input(root, path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_footer_only_edit_passes_locked_check(self, adopted_folder):
        """Footer-only edit passes the locked-doc check (V38 carve-out) but
        may still be caught by the batch-boundary check if UX.md isn't on
        the active batch's Files: list. The key assertion: the deny reason
        is NOT 'locked source-of-truth' — it's 'not on the current build
        batch' (the downstream check). This confirms the V38 carve-out works."""
        root = adopted_folder
        ux_path = str((root / "UX.md").resolve())
        data = _edit_input(
            root, ux_path,
            old_string="*Sovereign Implementer — Version 50.*",
            new_string="*Sovereign Implementer — Version 52.*",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        if raw:
            reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
            assert "locked source-of-truth" not in reason
            assert "not on the current build batch" in reason

    def test_proposed_edits_section_edit_passes_locked_check(self, adopted_folder):
        """Proposed-edits section edit passes the locked-doc check (V45
        carve-out) but hits the batch-boundary check. Same pattern as
        above — confirm the deny reason is batch-boundary, not locked-doc."""
        root = adopted_folder
        ux_path = str((root / "UX.md").resolve())
        data = _edit_input(
            root, ux_path,
            old_string="## Proposed edits pending\n\n*Sovereign Implementer — Version 52.*",
            new_string=(
                "## Proposed edits pending\n\n"
                "[PROPOSED EDIT PENDING]\n"
                "Origin: mid-build edit attempt — 2026-05-22.\n"
                "Content: New feature.\n\n"
                "*Sovereign Implementer — Version 52.*"
            ),
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        if raw:
            reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
            assert "locked source-of-truth" not in reason
            assert "not on the current build batch" in reason


# ---------------------------------------------------------------------------
# Serves-line check
# ---------------------------------------------------------------------------

class TestServesLineCheck:
    def test_valid_serves_line_allowed(self, adopted_folder):
        root = adopted_folder
        bl_path = str(
            (root / "BACKLOG" / "0001-add-settings-screen.md").resolve()
        )
        data = _edit_input(
            root, bl_path,
            old_string="Serves UX.md: Settings.",
            new_string="Serves UX.md: Settings.",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_invalid_serves_line_denied(self, adopted_folder):
        root = adopted_folder
        bl_path = str(
            (root / "BACKLOG" / "0001-add-settings-screen.md").resolve()
        )
        data = _edit_input(
            root, bl_path,
            old_string="Serves UX.md: Settings.",
            new_string="Serves UX.md: NonexistentFeature.",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "don't exist in `UX.md`")

    def test_non_backlog_edit_skips_serves_check(self, adopted_folder):
        root = adopted_folder
        path = str((root / "MANIFEST.md").resolve())
        data = _edit_input(
            root, path,
            old_string="something",
            new_string="Serves UX.md: Fake.",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_valid_serves_additional_doc_allowed(self, adopted_folder):
        """V54: Serves PATTERNS.md with a valid entry passes."""
        root = adopted_folder
        bl_path = str(
            (root / "BACKLOG" / "0001-add-settings-screen.md").resolve()
        )
        data = _edit_input(
            root, bl_path,
            old_string="Serves UX.md: Settings.",
            new_string="Serves PATTERNS.md: Authentication flow.",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_invalid_serves_additional_doc_denied(self, adopted_folder):
        """V54: Serves PATTERNS.md with a nonexistent entry is denied."""
        root = adopted_folder
        bl_path = str(
            (root / "BACKLOG" / "0001-add-settings-screen.md").resolve()
        )
        data = _edit_input(
            root, bl_path,
            old_string="Serves UX.md: Settings.",
            new_string="Serves PATTERNS.md: Nonexistent pattern.",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "don't exist in `PATTERNS.md`")

    def test_serves_additional_doc_case_insensitive(self, adopted_folder):
        """V54: Serves line matching is case-insensitive for additional docs."""
        root = adopted_folder
        bl_path = str(
            (root / "BACKLOG" / "0001-add-settings-screen.md").resolve()
        )
        data = _edit_input(
            root, bl_path,
            old_string="Serves UX.md: Settings.",
            new_string="Serves PATTERNS.md: authentication flow.",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_serves_writable_doc_skipped(self, adopted_folder):
        """Serves MANIFEST.md or other writable docs are not validated."""
        root = adopted_folder
        bl_path = str(
            (root / "BACKLOG" / "0001-add-settings-screen.md").resolve()
        )
        data = _edit_input(
            root, bl_path,
            old_string="Serves UX.md: Settings.",
            new_string="Serves MANIFEST.md: Anything.",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# Batch file-list boundary check
# ---------------------------------------------------------------------------

class TestBatchBoundary:
    def test_on_list_allowed(self, adopted_folder):
        root = adopted_folder
        target = str((root / "app" / "src" / "SettingsScreen.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_off_list_denied(self, adopted_folder):
        root = adopted_folder
        target = str((root / "app" / "src" / "SomeOtherFile.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "not on the current build batch")


# ---------------------------------------------------------------------------
# V39 read-before-edit gate
# ---------------------------------------------------------------------------

class TestV39ReadBeforeEdit:
    def test_manifest_listed_file_blocked_first_time(self, adopted_folder):
        root = adopted_folder
        target = str((root / "app" / "src" / "DashboardScreen.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "BLOCKED [V39 read-before-edit]")

    def test_spine_doc_exempt(self, adopted_folder):
        root = adopted_folder
        target = str((root / "MANIFEST.md").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# V27 test-confirmation gate (build-phase file edits, reframed V66)
# ---------------------------------------------------------------------------

class TestTestConfirmationGate:
    def test_all_confirmed_allows_build_edit(self, adopted_folder):
        """When all TEST-LOG rows are confirmed, build-phase edits are allowed."""
        root = adopted_folder
        target = str((root / "app" / "src" / "SettingsScreen.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# Malformed / edge-case inputs
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# V67 Phase-aware permission flip — planning phase
# ---------------------------------------------------------------------------

class TestPlanningPhasePermissions:
    """V67: during planning phase (no active batch), source-of-truth docs
    are directly editable and source code is locked."""

    def test_ux_editable_during_planning(self, planning_phase):
        root = planning_phase
        ux_path = str((root / "UX.md").resolve())
        data = _edit_input(root, ux_path, old_string="Dashboard", new_string="Home")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_source_code_locked_during_planning(self, planning_phase):
        root = planning_phase
        target = str((root / "app" / "src" / "DashboardScreen.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "source-code file")

    def test_backlog_editable_during_planning(self, planning_phase):
        root = planning_phase
        bl_path = str((root / "BACKLOG" / "INDEX.md").resolve())
        data = _edit_input(root, bl_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_manifest_editable_during_planning(self, planning_phase):
        root = planning_phase
        path = str((root / "MANIFEST.md").resolve())
        data = _edit_input(root, path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_research_file_editable_during_planning(self, planning_phase):
        root = planning_phase
        path = str((root / "research" / "api-options.md").resolve())
        data = _edit_input(root, path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_test_log_editable_during_planning(self, planning_phase):
        root = planning_phase
        path = str((root / "TEST-LOG.md").resolve())
        data = _edit_input(root, path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_claude_md_editable_during_planning(self, planning_phase):
        root = planning_phase
        path = str((root / "CLAUDE.md").resolve())
        data = _edit_input(root, path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_planning_source_lock_mode_aware(self, planning_phase):
        root = planning_phase
        target = str((root / "app" / "src" / "DashboardScreen.kt").resolve())
        data = _edit_input(root, target, permission_mode="Auto")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "permission mode")


# ---------------------------------------------------------------------------
# V91 Method infrastructure whitelist expansion
# ---------------------------------------------------------------------------

class TestMethodInfraWhitelist:
    """V91: BACKLOG per-batch files, all proxies, and planning/drafts
    are writable during planning phase."""

    def test_build_plan_per_batch_file_allowed(self, planning_phase):
        root = planning_phase
        target = str((root / "BACKLOG" / "0001-add-settings-screen.md").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_proxy_ux_allowed(self, tmp_path):
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "UX.md", "BACKLOG.md": "proxies/backlog.md",\n'
            ' "MANIFEST.md": "MANIFEST.md", "TEST-LOG.md": "TEST-LOG.md",\n'
            ' "BUILD-LOG.md": "proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "proxies").mkdir()
        target = str((root / "proxies" / "ux.md").resolve())
        data = _write_input(root, target, content="<!-- proxy -->")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_proxy_manifest_allowed(self, tmp_path):
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "UX.md", "BACKLOG.md": "proxies/backlog.md",\n'
            ' "MANIFEST.md": "MANIFEST.md", "TEST-LOG.md": "TEST-LOG.md",\n'
            ' "BUILD-LOG.md": "proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "proxies").mkdir()
        target = str((root / "proxies" / "manifest.md").resolve())
        data = _write_input(root, target, content="<!-- proxy -->")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_planning_drafts_allowed(self, tmp_path):
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "UX.md", "BACKLOG.md": "BACKLOG/INDEX.md",\n'
            ' "MANIFEST.md": "MANIFEST.md", "TEST-LOG.md": "TEST-LOG.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "planning" / "drafts").mkdir(parents=True)
        target = str((root / "planning" / "drafts" / "comparison-table.md").resolve())
        data = _write_input(root, target, content="# Draft")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_method_dir_proxies_allowed(self, tmp_path):
        """_method/ layout: proxies are writable during planning."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "_method" / "proxies").mkdir(parents=True)
        target = str((root / "_method" / "proxies" / "ux.md").resolve())
        data = _write_input(root, target, content="<!-- proxy -->")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_method_dir_drafts_allowed(self, tmp_path):
        """_method/ layout: planning/drafts writable during planning."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "_method" / "planning" / "drafts").mkdir(parents=True)
        target = str((root / "_method" / "planning" / "drafts" / "sketch.md").resolve())
        data = _write_input(root, target, content="# Draft")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_method_dir_build_plan_per_batch_allowed(self, tmp_path):
        """_method/ layout: BACKLOG per-batch files writable during planning."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "_method" / "BACKLOG").mkdir(parents=True)
        target = str((root / "_method" / "BACKLOG" / "0001-new-batch.md").resolve())
        data = _write_input(root, target, content="# New batch")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# V91 Heredoc/here-string stripping in Bash write-guard
# ---------------------------------------------------------------------------

class TestHeredocStripping:
    """V91: Bash write-guard strips heredoc/here-string content before
    scanning for file-write targets, preventing false positives."""

    def test_powershell_herestring_no_false_positive(self, planning_phase):
        root = planning_phase
        cmd = (
            "@'\n# UX.md — proxy\nSome content\n'@"
            " | Out-File -Path proxies/ux.md"
        )
        data = _bash_input(root, cmd, tool_name="PowerShell")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        if raw:
            reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
            assert "`#`" not in reason

    def test_bash_heredoc_no_false_positive(self, planning_phase):
        root = planning_phase
        cmd = (
            "cat <<'EOF' > proxies/ux.md\n"
            "# UX.md — proxy\n"
            "Some content\n"
            "EOF"
        )
        data = _bash_input(root, cmd)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        if raw:
            reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
            assert "`#`" not in reason

    def test_python_newline_no_false_positive(self, planning_phase):
        root = planning_phase
        cmd = r'python -c "open(\"proxies/ux.md\",\"w\").write(\"# UX\n\nContent\")"'
        data = _bash_input(root, cmd)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        if raw:
            reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
            assert r"C:\n" not in reason


# ---------------------------------------------------------------------------
# V71 Unadopted planning deny — /setup message
# ---------------------------------------------------------------------------

class TestUnadoptedPlanningDeny:
    """V71: in an unadopted folder (no method footer), the planning-phase
    source lock message says 'run /sovsetup' instead of referencing BACKLOG."""

    def test_unadopted_empty_folder_deny_mentions_setup(self, tmp_path):
        target = tmp_path / "index.html"
        target.write_text("<html></html>")
        data = _edit_input(tmp_path, str(target))
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "/sovsetup")

    def test_unadopted_empty_folder_deny_no_backlog_reference(self, tmp_path):
        target = tmp_path / "index.html"
        target.write_text("<html></html>")
        data = _edit_input(tmp_path, str(target))
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "BACKLOG" not in reason

    def test_adopted_folder_deny_mentions_backlog(self, planning_phase):
        root = planning_phase
        target = str((root / "app" / "src" / "DashboardScreen.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "BACKLOG" in reason

    def test_unadopted_mode_aware(self, tmp_path):
        target = tmp_path / "index.html"
        target.write_text("<html></html>")
        data = _edit_input(tmp_path, str(target), permission_mode="Auto")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "permission mode")


# ---------------------------------------------------------------------------
# Malformed / edge-case inputs
# ---------------------------------------------------------------------------

class TestMalformedInputs:
    def test_empty_dict(self):
        code, parsed, raw = run_hook("pre_tool_use.py", {})
        _assert_allow(code, raw)

    def test_missing_tool_name(self):
        code, parsed, raw = run_hook(
            "pre_tool_use.py", {"cwd": "C:\\fake", "tool_input": {}}
        )
        _assert_allow(code, raw)

    def test_missing_cwd(self, adopted_folder):
        code, parsed, raw = run_hook(
            "pre_tool_use.py",
            {"tool_name": "Edit", "tool_input": {
                "file_path": str(adopted_folder / "UX.md")
            }},
        )
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# V83 Bash write-guard
# ---------------------------------------------------------------------------

class TestBashWriteGuard:
    """V83: Bash/PowerShell commands with file-write patterns are checked
    against existing rules (project boundary, phase-aware locks)."""

    # --- Build-phase tests (adopted_folder has Status: active) ---

    def test_redirect_to_locked_doc_denied(self, adopted_folder):
        """Redirect to UX.md during build phase is denied."""
        data = _bash_input(adopted_folder, 'echo "new content" > UX.md')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "Bash command writes to")

    def test_sed_i_on_locked_doc_denied(self, adopted_folder):
        """sed -i on a locked source-of-truth doc is denied."""
        ux_path = str((adopted_folder / "UX.md").resolve())
        data = _bash_input(adopted_folder, f"sed -i 's/old/new/' {ux_path}")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "Bash command writes to")

    def test_redirect_outside_project_denied(self, adopted_folder):
        """Redirect to a path outside the project root is denied."""
        outside = str((adopted_folder.parent / "other" / "f.txt").resolve())
        data = _bash_input(adopted_folder, f'echo "x" > "{outside}"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "outside the project root")

    def test_redirect_to_batch_file_allowed(self, adopted_folder):
        """Redirect to a file on the batch's Files: list passes."""
        target = str((adopted_folder / "app" / "src" / "SettingsScreen.kt").resolve())
        data = _bash_input(adopted_folder, f'echo "x" > "{target}"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_redirect_to_off_list_file_denied(self, adopted_folder):
        """Redirect to a file not on the batch's Files: list is denied."""
        data = _bash_input(
            adopted_folder, 'echo "x" > app/src/SomeOtherFile.kt'
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "not on the current build batch")

    def test_tee_to_locked_doc_denied(self, adopted_folder):
        """tee to a locked doc is denied."""
        data = _bash_input(adopted_folder, 'echo "x" | tee UX.md')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "Bash command writes to")

    def test_cp_to_locked_doc_denied(self, adopted_folder):
        """cp with locked doc as destination is denied."""
        data = _bash_input(adopted_folder, "cp other.md UX.md")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "Bash command writes to")

    def test_mv_to_locked_doc_denied(self, adopted_folder):
        """mv with locked doc as destination is denied."""
        data = _bash_input(adopted_folder, "mv other.md UX.md")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "Bash command writes to")

    # --- PowerShell-specific ---

    def test_set_content_on_locked_doc_denied(self, adopted_folder):
        """Set-Content targeting a locked doc is denied."""
        data = _bash_input(
            adopted_folder,
            'Set-Content -Path UX.md -Value "new"',
            tool_name="PowerShell",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "Bash command writes to")

    def test_out_file_on_locked_doc_denied(self, adopted_folder):
        """Out-File targeting a locked doc is denied."""
        data = _bash_input(
            adopted_folder,
            '"content" | Out-File UX.md',
            tool_name="PowerShell",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "Bash command writes to")

    # --- Planning-phase tests ---

    def test_redirect_to_source_code_denied_during_planning(self, planning_phase):
        """Redirect to a source file during planning is denied."""
        data = _bash_input(
            planning_phase,
            'echo "x" > app/src/DashboardScreen.kt',
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "source-code file locked during the planning")

    def test_redirect_to_method_doc_allowed_during_planning(self, planning_phase):
        """Redirect to a method doc (BACKLOG) during planning is allowed."""
        bl_path = str(
            (planning_phase / "BACKLOG" / "0001-add-settings-screen.md").resolve()
        )
        data = _bash_input(planning_phase, f'echo "x" > "{bl_path}"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    # --- False-positive regression ---

    def test_no_write_pattern_allowed(self, adopted_folder):
        """Bash commands without write patterns pass through immediately."""
        data = _bash_input(adopted_folder, "git status")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_npm_start_allowed(self, adopted_folder):
        """dev server commands are not blocked."""
        data = _bash_input(adopted_folder, "npm start")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_redirect_to_dev_null_allowed(self, adopted_folder):
        """Redirect to /dev/null is not a write target."""
        data = _bash_input(adopted_folder, "some_cmd > /dev/null 2>&1")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_redirect_to_ps_null_allowed(self, adopted_folder):
        """Redirect to $null in PowerShell is not a write target."""
        data = _bash_input(
            adopted_folder,
            "Get-Process > $null",
            tool_name="PowerShell",
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_redirect_to_backlog_allowed(self, adopted_folder):
        """Redirect to BACKLOG (always writable) during build is allowed."""
        bl_path = str(
            (adopted_folder / "BACKLOG" / "INDEX.md").resolve()
        )
        data = _bash_input(adopted_folder, f'echo "x" > "{bl_path}"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_redirect_to_manifest_allowed(self, adopted_folder):
        """Redirect to MANIFEST.md (always writable) during build is allowed."""
        path = str((adopted_folder / "MANIFEST.md").resolve())
        data = _bash_input(adopted_folder, f'echo "x" > "{path}"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    # --- Skill escape guidance in deny messages ---

    def test_bash_locked_sot_mentions_sovclose(self, adopted_folder):
        """Bash locked-doc deny mentions /sovclose as escape route."""
        data = _bash_input(adopted_folder, 'echo "x" > UX.md')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "/sovclose" in reason

    def test_bash_planning_source_mentions_sovrecap(self, planning_phase):
        """Bash planning-source deny mentions /sovrecap as escape route."""
        data = _bash_input(
            planning_phase, 'echo "x" > app/src/DashboardScreen.kt'
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "/sovrecap" in reason

    def test_bash_mode_aware_suffix(self, adopted_folder):
        """Bash deny messages include mode-aware suffix in permissive modes."""
        data = _bash_input(
            adopted_folder, 'echo "x" > UX.md', permission_mode="Auto"
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "permission mode")


# ---------------------------------------------------------------------------
# 0116 Bug 1: active-build.md creation allowed during planning
# ---------------------------------------------------------------------------

class TestActiveBuildCreation:
    """0116 Bug 1: _method/active-build.md must be writable during planning
    phase. is_method_infra_file must recognise root-level _method/ files."""

    def test_active_build_writable_during_planning(self, tmp_path):
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "_method").mkdir()
        target = str((root / "_method" / "active-build.md").resolve())
        data = _write_input(root, target, content="# Batch snapshot")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_active_build_writable_legacy_layout(self, tmp_path):
        """Root-level active-build.md also handled (legacy layout)."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "UX.md", "BACKLOG.md": "BACKLOG/INDEX.md",\n'
            ' "MANIFEST.md": "MANIFEST.md", "TEST-LOG.md": "TEST-LOG.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        target = str((root / "active-build.md").resolve())
        data = _write_input(root, target, content="# Batch snapshot")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# 0116 Bug 2: test-log/ and build-log/ writable during close (build phase)
# ---------------------------------------------------------------------------

class TestClosePhaseLogWrites:
    """0116 Bug 2: test-log/ and build-log/ must be writable during build
    phase so /sovclose can write outputs."""

    def test_test_log_writable_during_build(self, tmp_path):
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "_method" / "test-log").mkdir(parents=True)
        (root / "_method" / "proxies").mkdir(parents=True)
        # Create snapshot to put project in build phase
        (root / "_method" / "active-build.md").write_text(
            "# Test batch\n\nFiles:\n- [x] `app/main.py` — Main file\n"
        )
        target = str((root / "_method" / "test-log" / "001-test-batch.md").resolve())
        data = _write_input(root, target, content="# Test session")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_build_log_writable_during_build(self, tmp_path):
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "_method" / "build-log").mkdir(parents=True)
        (root / "_method" / "proxies").mkdir(parents=True)
        (root / "_method" / "active-build.md").write_text(
            "# Test batch\n\nFiles:\n- [x] `app/main.py` — Main file\n"
        )
        target = str((root / "_method" / "build-log" / "001-test-batch.md").resolve())
        data = _write_input(root, target, content="# Build log entry")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_test_log_writable_legacy_layout(self, tmp_path):
        """Root-level test-log/ also handled (legacy layout)."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "UX.md", "BACKLOG.md": "BACKLOG/INDEX.md",\n'
            ' "MANIFEST.md": "MANIFEST.md", "TEST-LOG.md": "TEST-LOG.md",\n'
            ' "BUILD-LOG.md": "build-log/INDEX.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "test-log").mkdir()
        (root / "BACKLOG").mkdir()
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Test batch\n\nFiles:\n- [x] `app/main.py` — Main file\n"
        )
        target = str((root / "test-log" / "001-test-batch.md").resolve())
        data = _write_input(root, target, content="# Test session")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_test_log_index_writable_during_build(self, tmp_path):
        """Path-block-resolved TEST-LOG.md (backlog proxy) is writable."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n'
        )
        (root / "_method" / "proxies").mkdir(parents=True)
        (root / "_method" / "active-build.md").write_text(
            "# Test batch\n\nFiles:\n- [x] `app/main.py` — Main file\n"
        )
        target = str((root / "_method" / "proxies" / "backlog.md").resolve())
        data = _write_input(root, target, content="<!-- proxy -->")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)


# ---------------------------------------------------------------------------
# 0116 Bug 3: phase detection with all-ticked batch and Status: active
# ---------------------------------------------------------------------------

class TestPhaseDetectionAllTicked:
    """0116 Bug 3: Status: active must keep phase as 'build' even when all
    files are ticked. The parser returns {} for all-ticked batches, but
    detect_phase must fall back to checking Status: active directly."""

    def test_all_ticked_status_active_stays_build(self, tmp_path):
        """Folder mode: all files ticked + Status: active → build phase.
        Source code edits should be allowed (not blocked by planning lock)."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "UX.md", "BACKLOG.md": "BACKLOG/INDEX.md",\n'
            ' "MANIFEST.md": "MANIFEST.md", "TEST-LOG.md": "TEST-LOG.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n',
            encoding="utf-8",
        )
        (root / "UX.md").write_text(
            "## Functionalities\n\n### Settings\nUser settings.\n"
        )
        (root / "MANIFEST.md").write_text("")
        (root / "TEST-LOG.md").write_text("")
        bp_dir = root / "BACKLOG"
        bp_dir.mkdir()
        (bp_dir / "INDEX.md").write_text(
            "# BACKLOG\n\n## Red flags\n\n## Planning batches\n\n"
            "## Build batches\n\n- `0001-batch.md` — Test batch\n\n"
            "## Open questions\n",
            encoding="utf-8",
        )
        (bp_dir / "0001-batch.md").write_text(
            "# Test batch\n\nStatus: active\n\n"
            "**Goal.** Test.\n\nChanges:\n- [Requested] Change\n\n"
            "Files:\n- [x] `app/main.py` — All done\n\n"
            "Serves UX.md: Settings.\n",
            encoding="utf-8",
        )
        # No active-build.md → legacy path used
        target = str((root / "MANIFEST.md").resolve())
        data = _edit_input(root, target, old_string="", new_string="entry")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_all_ticked_no_active_status_is_planning(self, tmp_path):
        """Sanity check: all ticked + no Status: active → planning phase.
        Source code edits should be blocked."""
        root = tmp_path
        claude_md = root / "CLAUDE.md"
        claude_md.write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "UX.md", "BACKLOG.md": "BACKLOG/INDEX.md",\n'
            ' "MANIFEST.md": "MANIFEST.md", "TEST-LOG.md": "TEST-LOG.md"}\n'
            '```\n\n*Sovereign Implementer — Version 91.*\n',
            encoding="utf-8",
        )
        (root / "UX.md").write_text("## Functionalities\n")
        (root / "MANIFEST.md").write_text("")
        (root / "TEST-LOG.md").write_text("")
        bp_dir = root / "BACKLOG"
        bp_dir.mkdir()
        (bp_dir / "INDEX.md").write_text(
            "# BACKLOG\n\n## Red flags\n\n## Planning batches\n\n"
            "## Build batches\n\n- `0001-batch.md` — Test batch\n\n"
            "## Open questions\n",
            encoding="utf-8",
        )
        (bp_dir / "0001-batch.md").write_text(
            "# Test batch\n\n"
            "**Goal.** Test.\n\nChanges:\n- [Requested] Change\n\n"
            "Files:\n- [x] `app/main.py` — All done\n\n"
            "Serves UX.md: Settings.\n",
            encoding="utf-8",
        )
        (root / "app").mkdir()
        target = str((root / "app" / "main.py").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "source-code file")


# ---------------------------------------------------------------------------
# V83 Skill escape guidance on existing denies
# ---------------------------------------------------------------------------

class TestSkillEscapeGuidance:
    """V83: existing phase-lock deny messages name the skill that unlocks."""

    def test_locked_doc_mentions_sovclose(self, adopted_folder):
        """Locked-doc deny now mentions /sovclose as escape."""
        root = adopted_folder
        ux_path = str((root / "UX.md").resolve())
        data = _edit_input(root, ux_path, old_string="Dashboard", new_string="Home")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "/sovclose" in reason
        assert "/sovplan" in reason

    def test_planning_source_lock_mentions_sovrecap(self, planning_phase):
        """Planning source-lock deny now mentions /sovrecap."""
        root = planning_phase
        target = str((root / "app" / "src" / "DashboardScreen.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "/sovrecap" in reason
        assert "/sovbuild" in reason

    def test_batch_boundary_mentions_sovclose(self, adopted_folder):
        """Batch-boundary deny now mentions /sovclose + /sovplan."""
        root = adopted_folder
        target = str((root / "app" / "src" / "SomeOtherFile.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "/sovclose" in reason
        assert "/sovplan" in reason


# ---------------------------------------------------------------------------
# V132 Unclosed-build commit guard
# ---------------------------------------------------------------------------

class TestUnclosedBuildCommitGuard:
    """V132: git commit blocked when _method/active-build.md exists
    with all Files: ticked (build done, /sovclose not run)."""

    def test_all_ticked_commit_blocked(self, tmp_path):
        """All files ticked + git commit -> denied."""
        root = tmp_path
        (root / "CLAUDE.md").write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 98.*\n',
            encoding="utf-8",
        )
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Test batch\n\nFiles:\n"
            "- [x] `app/main.py` — Main file\n"
            "- [x] `app/utils.py` — Utilities\n",
            encoding="utf-8",
        )
        data = _bash_input(root, 'git commit -m "ship it"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "/sovclose")

    def test_some_unticked_commit_allowed(self, tmp_path):
        """Some files unticked + git commit -> allowed (mid-build)."""
        root = tmp_path
        (root / "CLAUDE.md").write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md", "BACKLOG.md": "_method/proxies/backlog.md",\n'
            ' "MANIFEST.md": "_method/MANIFEST.md", "TEST-LOG.md": "_method/proxies/backlog.md",\n'
            ' "BUILD-LOG.md": "_method/proxies/build-log.md"}\n'
            '```\n\n*Sovereign Implementer — Version 98.*\n',
            encoding="utf-8",
        )
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Test batch\n\nFiles:\n"
            "- [x] `app/main.py` — Main file\n"
            "- [ ] `app/utils.py` — Utilities\n",
            encoding="utf-8",
        )
        data = _bash_input(root, 'git commit -m "wip"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_no_snapshot_commit_allowed(self, tmp_path):
        """No active-build.md + git commit -> allowed (planning phase)."""
        root = tmp_path
        (root / "CLAUDE.md").write_text(
            '## Where the docs live\n\n```json\n'
            '{"UX.md": "_method/UX.md"}\n'
            '```\n\n*Sovereign Implementer — Version 98.*\n',
            encoding="utf-8",
        )
        data = _bash_input(root, 'git commit -m "planning changes"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_non_commit_command_allowed(self, tmp_path):
        """Non-git-commit commands pass through even with ticked snapshot."""
        root = tmp_path
        (root / "CLAUDE.md").write_text(
            '*Sovereign Implementer — Version 98.*\n',
            encoding="utf-8",
        )
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Test batch\n\nFiles:\n- [x] `app/main.py` — Done\n",
            encoding="utf-8",
        )
        data = _bash_input(root, "git status")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_git_commit_with_options_blocked(self, tmp_path):
        """git commit with flags (--amend, etc.) also blocked."""
        root = tmp_path
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Batch\n\nFiles:\n- [x] `f.py` — Done\n",
            encoding="utf-8",
        )
        data = _bash_input(root, "git commit --amend --no-edit")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "orphaned")

    def test_powershell_commit_blocked(self, tmp_path):
        """PowerShell git commit also blocked."""
        root = tmp_path
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Batch\n\nFiles:\n- [x] `f.py` — Done\n",
            encoding="utf-8",
        )
        data = _bash_input(root, 'git commit -m "msg"', tool_name="PowerShell")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "/sovclose")

    def test_mode_aware_suffix(self, tmp_path):
        """Auto mode includes mode-aware suffix in deny message."""
        root = tmp_path
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Batch\n\nFiles:\n- [x] `f.py` — Done\n",
            encoding="utf-8",
        )
        data = _bash_input(root, 'git commit -m "msg"', permission_mode="Auto")
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "permission mode")

    def test_deny_message_content(self, tmp_path):
        """Deny message explains consequences and points at /sovclose."""
        root = tmp_path
        (root / "_method").mkdir()
        (root / "_method" / "active-build.md").write_text(
            "# Batch\n\nFiles:\n- [x] `f.py` — Done\n",
            encoding="utf-8",
        )
        data = _bash_input(root, 'git commit -m "msg"')
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "orphaned" in reason
        assert "/sovclose" in reason
        assert "MANIFEST" in reason
        assert "/sovgit" in reason
