"""Shared fixtures and helpers for the no-code-method plugin test suite."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent.parent
PLUGIN_DIR = REPO_ROOT / "plugin"
HOOKS_DIR = PLUGIN_DIR / "hooks"
SCRIPTS_DIR = PLUGIN_DIR / "scripts"
FIXTURES_DIR = Path(__file__).parent / "fixtures"


def run_hook(hook_name: str, stdin_data: dict, timeout: int = 10):
    """Pipe JSON into a hook script and capture its output.

    Returns (exit_code, parsed_json_or_None, raw_stdout).
    parsed_json_or_None is the parsed JSON from stdout, or None if
    stdout was empty or not valid JSON.
    """
    script = HOOKS_DIR / hook_name
    result = subprocess.run(
        [sys.executable, str(script)],
        input=json.dumps(stdin_data),
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=timeout,
    )
    raw = result.stdout.strip()
    parsed = None
    if raw:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            pass
    return result.returncode, parsed, raw


def run_script(script_name: str, args: list = None, timeout: int = 10):
    """Run a script from plugin/scripts/ with optional CLI args.

    Returns (exit_code, raw_stdout, raw_stderr).
    """
    script = SCRIPTS_DIR / script_name
    cmd = [sys.executable, str(script)] + (args or [])
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=timeout,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def fixture_path(name: str) -> Path:
    """Return the absolute path to a named fixture directory."""
    return (FIXTURES_DIR / name).resolve()


@pytest.fixture
def adopted_folder():
    return fixture_path("adopted_folder")


@pytest.fixture
def adopted_single_file():
    return fixture_path("adopted_single_file")


@pytest.fixture
def empty_folder():
    return fixture_path("empty")


@pytest.fixture
def unadopted_foreign():
    return fixture_path("unadopted_foreign_claude")


@pytest.fixture
def tier2_no_claude():
    return fixture_path("tier2_no_claude")


@pytest.fixture
def tier2_bad_pathblock():
    return fixture_path("tier2_bad_pathblock")


@pytest.fixture
def planning_phase():
    return fixture_path("planning_phase")


@pytest.fixture
def unclosed_build():
    return fixture_path("unclosed_build")
