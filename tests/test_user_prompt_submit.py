"""Tests for the UserPromptSubmit hook (plugin/hooks/user_prompt_submit.py)."""

import os
import tempfile

from conftest import run_hook


def _make_input(prompt, transcript_content=""):
    """Build a UserPromptSubmit hook input dict with an optional transcript."""
    # Write transcript content to a temp file so the hook can read it.
    tf = tempfile.NamedTemporaryFile(
        mode="w", suffix=".jsonl", delete=False, encoding="utf-8"
    )
    tf.write(transcript_content)
    tf.close()
    return {
        "cwd": ".",
        "hook_event_name": "UserPromptSubmit",
        "prompt": prompt,
        "transcript_path": tf.name,
        "permission_mode": "default",
        "session_id": "test-session",
    }, tf.name


def _cleanup(path):
    try:
        os.unlink(path)
    except OSError:
        pass


# --- Test notes classification ---

def test_classifies_test_notes():
    """Should classify prompts with Pass/Fail keywords as test notes."""
    data, tf = _make_input(
        "Here are my test results: #001 Pass, #002 Fail — the login "
        "screen didn't load properly. #003 Skipped because I couldn't "
        "test on mobile."
    )
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "opener classification" in ctx
        assert "test" in ctx.lower()
        assert "planning" in ctx.lower()
    finally:
        _cleanup(tf)


def test_classifies_setup_request():
    """Should classify /setup requests."""
    data, tf = _make_input("/setup")
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "setup" in ctx.lower()
    finally:
        _cleanup(tf)


def test_classifies_new_project():
    """Should classify 'new project' as setup."""
    data, tf = _make_input("I want to start a new project for a recipe app")
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "setup" in ctx.lower()
    finally:
        _cleanup(tf)


def test_classifies_resume():
    """Should classify resume requests."""
    data, tf = _make_input("Let's resume the build where we left off")
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "resume" in ctx.lower()
    finally:
        _cleanup(tf)


# --- No-op cases ---

def test_silent_on_ambiguous_prompt():
    """Should not classify ambiguous prompts — let Claude decide."""
    data, tf = _make_input("What's the current state of the project?")
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is None
    finally:
        _cleanup(tf)


def test_silent_on_feature_request():
    """Feature requests don't have strong enough keyword signals."""
    data, tf = _make_input("I want to add a dark mode toggle to settings")
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is None
    finally:
        _cleanup(tf)


def test_silent_on_subsequent_prompt():
    """Should no-op when the classification marker is already in the transcript."""
    marker = "[No-code method — opener classification]"
    data, tf = _make_input(
        "Here are test results: Pass, Fail, Skipped for #001 #002",
        transcript_content=f'{{"role":"assistant","content":"{marker}"}}'
    )
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is None
    finally:
        _cleanup(tf)


def test_silent_on_empty_prompt():
    """Should no-op on empty prompts."""
    data, tf = _make_input("")
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is None
    finally:
        _cleanup(tf)


def test_silent_on_missing_prompt():
    """Should no-op when prompt field is missing."""
    data = {
        "cwd": ".",
        "hook_event_name": "UserPromptSubmit",
        "session_id": "test",
    }
    code, parsed, raw = run_hook("user_prompt_submit.py", data)
    assert code == 0
    assert parsed is None


# --- Edge cases ---

def test_setup_priority_over_test_notes():
    """Setup should win when both signals are present (priority rule)."""
    data, tf = _make_input(
        "/setup — also here are my test results: Pass Fail #001"
    )
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        assert code == 0
        assert parsed is not None
        ctx = parsed["hookSpecificOutput"]["additionalContext"]
        assert "setup" in ctx.lower()
    finally:
        _cleanup(tf)


def test_single_test_keyword_not_enough():
    """A single test keyword shouldn't trigger classification."""
    data, tf = _make_input("The build passed review")
    try:
        code, parsed, raw = run_hook("user_prompt_submit.py", data)
        # "passed" doesn't match \bPass\b (different word form).
        # Even if it did, 1 hit < threshold of 2.
        assert code == 0
        assert parsed is None
    finally:
        _cleanup(tf)
