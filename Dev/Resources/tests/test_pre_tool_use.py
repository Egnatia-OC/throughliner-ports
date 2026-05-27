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
    def test_edit_outside_project_denied(self, adopted_folder):
        outside_path = str((adopted_folder.parent / "other-project" / "file.txt").resolve())
        data = _edit_input(adopted_folder, outside_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "outside the project root")

    def test_write_outside_project_denied(self, adopted_folder):
        outside_path = str((adopted_folder.parent / "other-project" / "file.txt").resolve())
        data = _write_input(adopted_folder, outside_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "outside the project root")

    def test_edit_inside_project_allowed(self, adopted_folder):
        inside_path = str((adopted_folder / "app" / "src" / "SettingsScreen.kt").resolve())
        data = _edit_input(adopted_folder, inside_path)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        # Should not be denied by boundary check (may hit other checks)
        if raw:
            reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
            assert "outside the project root" not in reason

    def test_edit_project_root_file_allowed(self, adopted_folder):
        root_file = str((adopted_folder / "MANIFEST.md").resolve())
        data = _edit_input(adopted_folder, root_file)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_allow(code, raw)

    def test_mode_aware_suffix(self, adopted_folder):
        outside_path = str((adopted_folder.parent / "other-project" / "file.txt").resolve())
        data = _edit_input(
            adopted_folder, outside_path, permission_mode="Accept edits"
        )
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        _assert_deny(parsed, "permission mode")


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
        bl_path = str((root / "BUILD-PLAN" / "INDEX.md").resolve())
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
            old_string="*No-code method — Version 50.*",
            new_string="*No-code method — Version 52.*",
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
            old_string="## Proposed edits pending\n\n*No-code method — Version 52.*",
            new_string=(
                "## Proposed edits pending\n\n"
                "[PROPOSED EDIT PENDING]\n"
                "Origin: mid-build edit attempt — 2026-05-22.\n"
                "Content: New feature.\n\n"
                "*No-code method — Version 52.*"
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
            (root / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
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
            (root / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
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
            (root / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
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
            (root / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
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
            (root / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
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
            (root / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
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
        bl_path = str((root / "BUILD-PLAN" / "INDEX.md").resolve())
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
# V71 Unadopted planning deny — /setup message
# ---------------------------------------------------------------------------

class TestUnadoptedPlanningDeny:
    """V71: in an unadopted folder (no method footer), the planning-phase
    source lock message says 'run /sovsetup' instead of referencing BUILD-PLAN."""

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
        assert "BUILD-PLAN" not in reason

    def test_adopted_folder_deny_mentions_backlog(self, planning_phase):
        root = planning_phase
        target = str((root / "app" / "src" / "DashboardScreen.kt").resolve())
        data = _edit_input(root, target)
        code, parsed, raw = run_hook("pre_tool_use.py", data)
        reason = parsed["hookSpecificOutput"]["permissionDecisionReason"]
        assert "BUILD-PLAN" in reason

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
        """Redirect to a method doc (BUILD-PLAN) during planning is allowed."""
        bl_path = str(
            (planning_phase / "BUILD-PLAN" / "0001-add-settings-screen.md").resolve()
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
        """Redirect to BUILD-PLAN (always writable) during build is allowed."""
        bl_path = str(
            (adopted_folder / "BUILD-PLAN" / "INDEX.md").resolve()
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
