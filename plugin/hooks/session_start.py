#!/usr/bin/env python3
"""
SessionStart hook for the no-code-method plugin.

Runs at the start of every Claude Code session in any folder where the plugin
is installed. Detects whether the folder is a no-code-method project; if so,
injects the universal-behaviour rules and a prose state summary into Claude's
context via the SessionStart hook output protocol.

Three tiers:

  Tier 1 (non-method folder)
    Neither CLAUDE.md nor any spine doc carrying the method's version footer
    is present at the project root. The hook writes nothing and exits 0 —
    the plugin is invisible in folders that aren't method projects.

  Tier 2 (partial method shape)
    Some method-shaped files are present but the project isn't fully set up:
    e.g. CLAUDE.md is missing while spine docs are present, or CLAUDE.md is
    present but its fenced JSON path block can't be parsed. The hook injects
    the universal-behaviour rules plus a single-paragraph gap flag naming
    the specific missing piece and pointing at /init-project or /migrate.

  Tier 3 (complete method project)
    CLAUDE.md is present and its fenced JSON path block parses. The hook
    injects the universal-behaviour rules plus a full state summary:
    resolved doc paths, template-state detection, version-footer mismatch
    tripwire, top build batch (for the resume route), and a reminder that
    route classification of the user's opener stays with Claude.

Why SessionStart and not UserPromptSubmit:
  UserPromptSubmit hooks declared in plugin hooks.json don't execute due to
  GitHub bug anthropics/claude-code#10225. SessionStart works in plugins
  today, and given the no-code method's /clear-after-every-build discipline,
  it's functionally equivalent: every new session re-fires the hook.

Locating the project root:
  Claude Code's hook input protocol passes a JSON object on stdin including
  a `cwd` field containing the project root (verified via the plugin
  hook-development SKILL.md). The CLAUDE_PROJECT_DIR env var is unreliable
  in plugin hooks (anthropics/claude-code#9447) so we don't depend on it.
  os.getcwd() is a safe fallback because the hook process's CWD is also the
  project root.

Output protocol:
  Tier 1: write nothing to stdout, exit 0.
  Tier 2 and 3: write a JSON object to stdout with hookSpecificOutput
  containing hookEventName ("SessionStart") and additionalContext (the
  combined universal rules + tier-specific summary). Exit 0.

  Hook errors (missing universal-behaviour.md, etc.) are surfaced *as*
  additionalContext with a [no-code-method plugin warning] prefix rather
  than dying silently — Claude (and the user) should know if the plugin is
  broken, not see no rules and assume everything is fine.
"""

import json
import os
import re
import sys
from pathlib import Path

# --- Constants ---

# The method version this build of the plugin carries. Bumped each session
# alongside the *No-code method — Version N.* footers on the method files.
# Used by the version-footer mismatch tripwire.
PLUGIN_METHOD_VERSION = 25

# Spine doc filenames the hook scans for at the project root when CLAUDE.md
# is missing — to distinguish tier 1 from tier 2. Detection is tightened by
# requiring the method footer to be present in the file (see has_method_footer).
SPINE_FILENAMES = ("UX.md", "BACKLOG.md", "MANIFEST.md")

# CLAUDE.md's path block is the first fenced JSON code block in the file.
# Same pattern as pre_tool_use.py — see V18's path block format spec.
PATH_BLOCK_PATTERN = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

# Method version footer line at the bottom of every method file and template.
FOOTER_PATTERN = re.compile(r"\*No-code method — Version (\d+)\.\*")

# Strong signal that a doc is still in template form: the literal placeholder
# string used in every template's heading and body.
TEMPLATE_PLACEHOLDER_PATTERN = re.compile(r"\[Project Name\]")

# Heading shape for a build batch in BACKLOG.md.
BUILD_BATCH_HEADING_PATTERN = re.compile(r"^### Batch: (.+)$", re.MULTILINE)

# Heading shape for the Build batches section in BACKLOG.md.
BUILD_BATCHES_SECTION_PATTERN = re.compile(r"^## Build batches\s*$", re.MULTILINE)

# Generic next-section pattern (used to bound the Build batches section).
NEXT_SECTION_PATTERN = re.compile(r"^## ", re.MULTILINE)


# --- File reads ---

def read_universal_rules() -> str:
    """Read universal-behaviour.md (sibling file in hooks/). Preserves V18's
    behaviour: surface a [no-code-method plugin warning] in-context rather
    than silently emitting nothing if the file can't be read."""
    rules_path = Path(__file__).parent / "universal-behaviour.md"
    try:
        return rules_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return (
            "[no-code-method plugin warning] "
            f"universal-behaviour.md not found at {rules_path}. "
            "The universal behavioural rules could not be injected. "
            "This is a plugin installation problem, not a method problem."
        )
    except OSError as exc:
        return (
            "[no-code-method plugin warning] "
            f"Could not read universal-behaviour.md ({exc}). "
            "The universal behavioural rules could not be injected."
        )


def safe_read_text(path: Path):
    """Read a text file; return None on any failure (missing, permissions,
    encoding). Used everywhere the hook needs to peek at a file without
    risking an unhandled exception in the subprocess."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


# --- Stdin / project root ---

def parse_stdin_input():
    """Read hook input JSON from stdin. Returns dict on success, None on any
    failure. Failure is non-fatal — the hook falls back to os.getcwd() for
    project-root detection."""
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def get_project_root(stdin_data) -> Path:
    """Resolve the consumer project's root path.

    Order of preference:
      1. stdin JSON's `cwd` field (the documented hook input contract).
      2. os.getcwd() (also the project root per Claude Code's hook contract).

    Avoids relying on $CLAUDE_PROJECT_DIR — that env var is broken for plugin
    hooks (anthropics/claude-code#9447), and even if/when fixed, the stdin
    contract is the more reliable source."""
    cwd_str = None
    if isinstance(stdin_data, dict):
        candidate = stdin_data.get("cwd")
        if isinstance(candidate, str) and candidate:
            cwd_str = candidate
    if cwd_str is None:
        cwd_str = os.getcwd()
    try:
        return Path(cwd_str).resolve()
    except OSError:
        return Path(cwd_str)


# --- Parsers / detectors ---

def extract_path_block(claude_md_text: str):
    """Extract and parse the fenced JSON path block from CLAUDE.md.
    Returns dict on success; None if absent or unparseable."""
    match = PATH_BLOCK_PATTERN.search(claude_md_text)
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def extract_footer_version(text: str):
    """Return the integer version from the `*No-code method — Version N.*`
    footer; None if not found."""
    match = FOOTER_PATTERN.search(text)
    if not match:
        return None
    try:
        return int(match.group(1))
    except ValueError:
        return None


def has_method_footer(text: str) -> bool:
    """Whether the text carries the method's version footer at all. Used to
    distinguish a method-aware spine doc from an unrelated file that happens
    to share the same name (e.g. a BACKLOG.md from some other project)."""
    return bool(FOOTER_PATTERN.search(text))


def is_template_state(text: str) -> bool:
    """Heuristic: text still contains the `[Project Name]` placeholder that
    every template ships with. Once a project is kicked off, [Project Name]
    is replaced; surviving instances strongly indicate the doc hasn't been
    filled in yet."""
    return bool(TEMPLATE_PLACEHOLDER_PATTERN.search(text))


def find_method_spine_docs(project_root: Path):
    """Return a list of spine doc paths at the project root that carry the
    method footer. Tightens tier 2 detection — an unrelated BACKLOG.md from
    some other context will not falsely trigger method-aware behaviour."""
    found = []
    for name in SPINE_FILENAMES:
        candidate = project_root / name
        text = safe_read_text(candidate)
        if text is not None and has_method_footer(text):
            found.append(candidate)
    return found


def detect_top_build_batch(backlog_text: str):
    """Find the first `### Batch:` heading inside BACKLOG.md's `## Build
    batches` section. Returns the batch title, or None if no real batch is
    present. Template placeholder titles like `[short descriptive name]`
    are filtered out so an unedited BACKLOG.md doesn't trip the resume
    signal."""
    section_match = BUILD_BATCHES_SECTION_PATTERN.search(backlog_text)
    if not section_match:
        return None

    # Bound the search to within the Build batches section.
    section_text = backlog_text[section_match.end():]
    next_section = NEXT_SECTION_PATTERN.search(section_text)
    if next_section:
        section_text = section_text[:next_section.start()]

    batch_match = BUILD_BATCH_HEADING_PATTERN.search(section_text)
    if not batch_match:
        return None

    title = batch_match.group(1).strip()
    # Template placeholder titles look like `[short descriptive name]`.
    if title.startswith("[") and title.endswith("]"):
        return None
    return title


# --- Tier detection ---

def detect_tier(project_root: Path):
    """Determine which tier applies. Returns a 4-tuple:
        (tier_number, claude_text_or_None, path_block_or_None, spine_docs_list)

    Tier 1: no CLAUDE.md, and no spine doc at the project root carries the
            method footer.
    Tier 2: partial shape. Either CLAUDE.md is present but the path block
            isn't parseable, or method-footer spine docs are present without
            a CLAUDE.md.
    Tier 3: CLAUDE.md is present and its fenced JSON path block parses.
    """
    claude_path = project_root / "CLAUDE.md"
    claude_text = safe_read_text(claude_path)
    spine_docs = find_method_spine_docs(project_root)

    if claude_text is None:
        if not spine_docs:
            return 1, None, None, []
        return 2, None, None, spine_docs

    path_block = extract_path_block(claude_text)
    if not path_block:
        return 2, claude_text, None, spine_docs

    return 3, claude_text, path_block, spine_docs


# --- Tier 3 state summary ---

def resolve_path_block_docs(project_root: Path, path_block: dict):
    """Resolve each entry in the path block to an absolute path and read its
    text. Returns (resolved, unresolved) where:
      resolved = {logical_name: (abs_path, text)}
      unresolved = [(logical_name, relative_path)] — entries whose file
                   could not be read.
    """
    resolved = {}
    unresolved = []
    for logical_name, rel_path in path_block.items():
        if not isinstance(logical_name, str) or not isinstance(rel_path, str):
            continue
        try:
            abs_path = (project_root / rel_path).resolve()
        except OSError:
            unresolved.append((logical_name, rel_path))
            continue
        text = safe_read_text(abs_path)
        if text is None:
            unresolved.append((logical_name, rel_path))
        else:
            resolved[logical_name] = (abs_path, text)
    return resolved, unresolved


def collect_template_state_docs(resolved: dict):
    """Return logical names of docs that still look like templates."""
    return [name for name, (_p, text) in resolved.items() if is_template_state(text)]


def collect_footer_mismatches(resolved: dict, claude_text: str):
    """Return [(logical_name, found_version)] for every doc whose footer
    version differs from the plugin's current version. CLAUDE.md is checked
    separately (it isn't a path-block entry against itself)."""
    mismatches = []
    for name, (_p, text) in resolved.items():
        v = extract_footer_version(text)
        if v is None:
            continue
        if v != PLUGIN_METHOD_VERSION:
            mismatches.append((name, v))
    claude_v = extract_footer_version(claude_text)
    if claude_v is not None and claude_v != PLUGIN_METHOD_VERSION:
        mismatches.append(("CLAUDE.md", claude_v))
    return mismatches


def build_state_summary(project_root: Path, claude_text: str, path_block: dict) -> str:
    """Compose the prose state summary for tier 3."""
    resolved, unresolved = resolve_path_block_docs(project_root, path_block)

    lines = ["## Project state (detected by SessionStart hook)", ""]

    lines.append(f"- **Project root:** `{project_root}`")
    lines.append(
        f"- **Path block:** resolved {len(resolved)} of {len(path_block)} entries."
    )

    if unresolved:
        lines.append("- **Unresolved doc paths in CLAUDE.md's path block:**")
        for logical_name, rel_path in unresolved:
            lines.append(f"  - `{logical_name}` → `{rel_path}` (file not found)")
        lines.append(
            "  Per NO-CODE-METHOD.md → *At session start*: search the project "
            "for the file by name, surface the mismatch, and propose updating "
            "the path block. Wait for the user's confirmation before editing."
        )

    template_docs = collect_template_state_docs(resolved)
    if template_docs:
        names_md = ", ".join(f"`{n}`" for n in template_docs)
        lines.append(
            f"- **Template state detected** in {names_md}. The project "
            "hasn't been kicked off yet — these docs still contain template "
            "placeholders. Per NO-CODE-METHOD.md → *Detect template state*: "
            "recommend the user start the new-project route to seed "
            "`UX.md`, `BACKLOG.md`, and the first build batch. Wait for "
            "the user's okay before proceeding."
        )

    footer_mismatches = collect_footer_mismatches(resolved, claude_text)
    if footer_mismatches:
        lines.append(
            f"- **Method version mismatch.** Plugin is at Version "
            f"{PLUGIN_METHOD_VERSION}; some docs carry older footers:"
        )
        for logical_name, v in footer_mismatches:
            lines.append(f"  - `{logical_name}` is at Version {v}")
        lines.append(
            "  This is a tripwire, not an auto-fix. Suggest the user run "
            "`/migrate` if structural drift is suspected, or update the "
            "footers if the content is current."
        )

    backlog_data = resolved.get("BACKLOG.md")
    if backlog_data:
        _path, backlog_text = backlog_data
        top_batch = detect_top_build_batch(backlog_text)
        if top_batch:
            lines.append(
                f"- **Top build batch in BACKLOG.md:** \"{top_batch}\". If "
                "the user's opener implies resume (test notes pointing at "
                "this batch, a 'continue where we left off' phrasing, etc.) "
                "default to *During planning → resume* per NO-CODE-METHOD.md "
                "→ *At session start*. Confirm with the user before "
                "continuing the build."
            )

    lines.append("")
    lines.append(
        "**Routing.** Read the user's opening message and route per "
        "NO-CODE-METHOD.md → *At session start*. This hook does not classify "
        "the user's opener — that's your call based on the user's words and "
        "the structural state listed above."
    )

    return "\n".join(lines)


# --- Tier 2 output ---

def build_tier_2_gap_flag(claude_text, spine_docs) -> str:
    """One-paragraph gap flag identifying which piece of the method shape
    is missing, and pointing at the right next step."""
    has_claude = claude_text is not None
    spine_names = ", ".join(f"`{p.name}`" for p in spine_docs)

    if has_claude and not spine_docs:
        gap = (
            "`CLAUDE.md` is present but its *Where the docs live* path block "
            "can't be parsed as a fenced JSON block, and no method-aware "
            "spine docs (carrying the `*No-code method — Version N.*` "
            "footer) were found at the project root."
        )
        next_step = (
            "Set up `CLAUDE.md`'s path block as fenced JSON (see "
            "`templates/CLAUDE-TEMPLATE.md` in the plugin), or run "
            "`/migrate` to bring an existing project up to spec."
        )
    elif not has_claude and spine_docs:
        gap = (
            f"Spine docs ({spine_names}) carrying the method footer are "
            "present at the project root, but `CLAUDE.md` is missing. The "
            "plugin's hooks rely on `CLAUDE.md`'s path block to locate the "
            "spine docs."
        )
        next_step = (
            "Run `/migrate` to bring this project up to spec — it will "
            "scaffold the missing `CLAUDE.md` and align the existing docs "
            "with the current structural rules."
        )
    elif has_claude and spine_docs:
        gap = (
            "`CLAUDE.md` is present but its *Where the docs live* path "
            f"block can't be parsed as a fenced JSON block. Spine docs "
            f"({spine_names}) are present and carry the method footer."
        )
        next_step = (
            "Either update `CLAUDE.md`'s path block to match the current "
            "fenced-JSON format (see `templates/CLAUDE-TEMPLATE.md`), or "
            "run `/migrate` to bring everything up to spec."
        )
    else:
        gap = (
            "Some method-shaped files were found but the project structure "
            "is incomplete."
        )
        next_step = "Run `/init-project` for a fresh start, or `/migrate` for an existing project."

    return (
        "## No-code-method project state\n\n"
        f"**Partial method shape detected.** {gap}\n\n"
        f"{next_step} No method-aware behaviour beyond the universal "
        "rules above is available until the project's structure is complete."
    )


# --- Main ---

def emit_context(combined: str) -> int:
    """Write the standard hookSpecificOutput JSON to stdout. Exit code 0."""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": combined,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def main() -> int:
    stdin_data = parse_stdin_input()
    project_root = get_project_root(stdin_data)

    tier, claude_text, path_block, spine_docs = detect_tier(project_root)

    if tier == 1:
        # Non-method folder. The plugin is invisible: no output, no rules.
        # This is a deliberate behaviour change from V18, which emitted the
        # universal rules in every Claude Code session regardless of project
        # type. V21 narrows that to method-aware projects only.
        return 0

    # Tier 2 and tier 3 both get the universal rules. The tier-specific
    # state summary is appended after.
    universal_rules = read_universal_rules()

    if tier == 2:
        tier_output = build_tier_2_gap_flag(claude_text, spine_docs)
    else:  # tier == 3
        tier_output = build_state_summary(project_root, claude_text, path_block)

    combined = universal_rules + "\n\n---\n\n" + tier_output
    return emit_context(combined)


if __name__ == "__main__":
    sys.exit(main())
