"""Hermes port test suite.

Drives the real plugin module (vendor/throughliner pristine hooks, spawned as
subprocesses) with synthetic Hermes hook kwargs shaped by the host's
fire sites (agent/shell_hooks.py, hermes_cli/plugins.py, agent/turn_finalizer.py).

Run: python3 -m unittest test.test_hermes -v   (from the repo root)
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VENDOR = REPO / "vendor" / "throughliner"

# Env MUST be set before the plugin module is imported: it resolves the
# vendor root and skills dir at import time.
_TMP_HOME = Path(tempfile.mkdtemp(prefix="tl-hermes-home-"))
os.environ["HOME"] = str(_TMP_HOME)
os.environ["THROUGHLINER_ROOT"] = str(VENDOR)
os.environ["THROUGHLINER_PYTHON"] = sys.executable
os.environ.pop("THROUGHLINER_PYTHON_MISSING", None)


def _load_plugin() -> "module":
    spec = importlib.util.spec_from_file_location("tl_hermes", REPO / "__init__.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FakeCtx:
    def __init__(self) -> None:
        self.hooks: dict[str, list] = {}
        self.sections: dict[str, str] = {}

    def register_hook(self, name, callback) -> None:
        self.hooks.setdefault(name, []).append(callback)

    def register_system_prompt_section(self, id, content, **kwargs) -> None:
        self.sections[id] = content


class HermesPluginTest(unittest.TestCase):
    """Each test gets a fresh scratch project so stop.py markers and
    .throughliner state never leak between cases."""

    def setUp(self) -> None:
        self.proj = Path(tempfile.mkdtemp(prefix="tl-hermes-proj-"))
        (self.proj / "SPEC.md").write_text("# SPEC\n\nA test project.\n", encoding="utf-8")
        (self.proj / "QUEUE.md").write_text(
            "## Processed\n\n#### fix the login bug [fix-login-bug]\n",
            encoding="utf-8",
        )
        build = self.proj / "_build-test-sid.md"
        build.write_text("# Build: fix-login-bug\n\nFiles:\n- src/app.py\n", encoding="utf-8")
        (self.proj / "src").mkdir()
        (self.proj / "src" / "app.py").write_text("print('hi')\n", encoding="utf-8")
        self.cwd = os.getcwd()
        os.chdir(self.proj)

    def tearDown(self) -> None:
        os.chdir(self.cwd)
        shutil.rmtree(self.proj, ignore_errors=True)

    def _plugin_and_ctx(self):
        mod = _load_plugin()
        ctx = FakeCtx()
        mod.register(ctx)
        return mod, ctx

    def _call(self, ctx, name, **kwargs):
        cbs = ctx.hooks.get(name, [])
        self.assertTrue(cbs, f"no callback registered for {name}")
        return cbs[0](**kwargs)

    # -- registration -------------------------------------------------------

    def test_register_hooks_and_brevity(self) -> None:
        _, ctx = self._plugin_and_ctx()
        for name in ("pre_tool_call", "post_tool_call", "pre_llm_call",
                     "post_llm_call", "on_session_end", "pre_verify"):
            self.assertIn(name, ctx.hooks, f"{name} not registered")
        self.assertIn("throughliner-brevity", ctx.sections)
        self.assertIn("non-coder", ctx.sections["throughliner-brevity"])

    def test_skills_materialized(self) -> None:
        self._plugin_and_ctx()
        base = Path(os.environ["HOME"]) / ".hermes" / "skills" / "throughliner"
        for name in ("setup", "plan", "next", "rescan", "done"):
            dest = base / f"tl-{name}" / "SKILL.md"
            self.assertTrue(dest.is_file(), f"missing {dest}")
            text = dest.read_text(encoding="utf-8")
            self.assertRegex(text, rf"^---\nname: tl-{name}\n", "frontmatter name")
            self.assertIn('description: "', text)
            self.assertNotIn("${CLAUDE_PLUGIN_ROOT}", text, "unrewritten env ref")
            self.assertIn(str(VENDOR), text, "vendor path not rewritten in")
            self.assertIn(f"# /tl-{name}", text, "command heading not renamed")
            self.assertNotIn("disable-model-invocation", text, "Claude-only key kept")

    def test_scope_lock_denies_unlisted_file(self) -> None:
        _, ctx = self._plugin_and_ctx()
        res = self._call(ctx, "pre_tool_call", tool_name="write_file",
                         args={"path": "src/other.py"}, session_id="test-sid")
        self.assertEqual(res["action"], "block")
        self.assertIn("[Throughliner]", res["message"])

    def test_fail_open_missing_root(self) -> None:
        old = os.environ["THROUGHLINER_ROOT"]
        os.environ["THROUGHLINER_ROOT"] = "/nonexistent/tl-root"
        try:
            mod = _load_plugin()
            self.assertIsNone(mod.VENDOR_ROOT)
            ctx = FakeCtx()
            mod.register(ctx)
            self.assertEqual(ctx.hooks, {}, "hooks registered without a vendor tree")
        finally:
            os.environ["THROUGHLINER_ROOT"] = old

    # -- pre_tool_call ------------------------------------------------------

    def test_unmapped_tool_allows(self) -> None:
        _, ctx = self._plugin_and_ctx()
        self.assertIsNone(self._call(ctx, "pre_tool_call", tool_name="read_file",
                                     args={"path": "src/app.py"}, session_id="test-sid"))

    def test_scope_lock_allows_listed_file(self) -> None:
        _, ctx = self._plugin_and_ctx()
        self.assertIsNone(self._call(ctx, "pre_tool_call", tool_name="write_file",
                                     args={"path": "src/app.py"}, session_id="test-sid"))

    def test_git_guard_denies_force_push(self) -> None:
        _, ctx = self._plugin_and_ctx()
        res = self._call(ctx, "pre_tool_call", tool_name="terminal",
                         args={"command": "git push --force origin main"}, session_id="test-sid")
        self.assertEqual(res["action"], "block")

    def test_git_guard_allows_commit(self) -> None:
        _, ctx = self._plugin_and_ctx()
        self.assertIsNone(self._call(ctx, "pre_tool_call", tool_name="terminal",
                                     args={"command": "git commit -m x"}, session_id="test-sid"))

    def test_subagent_ask_escalates_to_approve(self) -> None:
        _, ctx = self._plugin_and_ctx()
        res = self._call(ctx, "pre_tool_call", tool_name="delegate_task",
                         args={"description": "research the queue"}, session_id="test-sid")
        self.assertEqual(res["action"], "approve", "the subagent cost gate must escalate to the human gate")

    def test_skill_self_invocation_denied(self) -> None:
        _, ctx = self._plugin_and_ctx()
        res = self._call(ctx, "pre_tool_call", tool_name="skill_view",
                         args={"name": "tl-plan"}, session_id="test-sid")
        self.assertEqual(res["action"], "block")
        self.assertIn("yours to type", res["message"])

    # -- post_tool_call + pre_llm_call --------------------------------------

    def test_lint_findings_parked_then_drained(self) -> None:
        _, ctx = self._plugin_and_ctx()
        # A malformed queue entry: #### heading without a trailing [slug].
        (self.proj / "QUEUE.md").write_text(
            "## Unprocessed\n\n#### a new idea that lost its slug\n",
            encoding="utf-8",
        )
        self._call(ctx, "post_tool_call", tool_name="write_file",
                   args={"path": "QUEUE.md"}, session_id="test-sid",
                   result="", status="ok")
        parked = (self.proj / ".throughliner" / "pending-context.md")
        self.assertTrue(parked.is_file(), "lint findings not parked in .throughliner/")
        res = self._call(ctx, "pre_llm_call", session_id="test-sid", is_first_turn=False)
        self.assertIsNotNone(res, "parked findings not drained into context")
        self.assertIn("notes from earlier activity", res["context"])
        self.assertFalse(parked.exists(), "pending-context not cleared after drain")

    def test_session_start_context_on_first_turn(self) -> None:
        _, ctx = self._plugin_and_ctx()
        res = self._call(ctx, "pre_llm_call", session_id="test-sid", is_first_turn=True)
        self.assertIsNotNone(res, "no session-start context on first turn")
        self.assertTrue(len(res["context"]) > 0)
        # The model cannot know the harness session id natively, so the shim
        # says it — the vendored hooks name per-session files from it.
        self.assertIn("Session ID for this session: test-sid", res["context"])
        self.assertIn("_build-test-sid.md", res["context"])

    def test_no_context_when_nothing_parked(self) -> None:
        _, ctx = self._plugin_and_ctx()
        # Fresh project, no pending file, non-first turn: nothing to inject.
        res = self._call(ctx, "pre_llm_call", session_id="test-sid", is_first_turn=False)
        self.assertIsNone(res)

    # -- stop check ---------------------------------------------------------

    def test_pre_verify_blocks_unfiled_claim(self) -> None:
        _, ctx = self._plugin_and_ctx()
        res = self._call(ctx, "pre_verify", session_id="test-sid", platform="cli",
                         model="test", coding=True, attempt=0,
                         final_response="Done. I filed [ghost-slug] to the queue.",
                         changed_paths=["src/app.py"])
        self.assertEqual(res["decision"], "block", "claimed-but-unfiled slug must block")
        self.assertIn("ghost-slug", res["reason"])

    def test_pre_verify_allows_filed_claim(self) -> None:
        _, ctx = self._plugin_and_ctx()
        res = self._call(ctx, "pre_verify", session_id="test-sid", platform="cli",
                         model="test", coding=True, attempt=0,
                         final_response="Done. I filed [fix-login-bug] to the queue.",
                         changed_paths=["src/app.py"])
        self.assertIsNone(res, "a real filing must not block")

    def test_on_session_end_notes_unfiled_claim(self) -> None:
        _, ctx = self._plugin_and_ctx()
        self._call(ctx, "post_llm_call", session_id="test-sid",
                   assistant_response="Done. I filed [ghost-slug] to the queue.")
        self._call(ctx, "on_session_end", session_id="test-sid", task_id="t",
                   turn_id="turn-1", completed=True, failed=False,
                   interrupted=False, turn_exit_reason="text_response(stop)",
                   model="test", platform="cli")
        parked = (self.proj / ".throughliner" / "pending-context.md")
        self.assertTrue(parked.is_file(), "stop correction not parked for the next turn")
        self.assertIn("ghost-slug", parked.read_text(encoding="utf-8"))

    def test_stop_loop_protection(self) -> None:
        """A second stop check on the same claim/sid does not re-block."""
        _, ctx = self._plugin_and_ctx()
        first = self._call(ctx, "pre_verify", session_id="test-sid", platform="cli",
                           model="test", coding=True, attempt=0,
                           final_response="Done. I filed [ghost-slug] to the queue.",
                           changed_paths=["src/app.py"])
        self.assertEqual(first["decision"], "block")
        second = self._call(ctx, "pre_verify", session_id="test-sid", platform="cli",
                            model="test", coding=True, attempt=0,
                            final_response="Done. I filed [ghost-slug] to the queue.",
                            changed_paths=["src/app.py"])
        self.assertIsNone(second, "loop protection: same claim must not re-block")


if __name__ == "__main__":
    unittest.main(verbosity=2)
