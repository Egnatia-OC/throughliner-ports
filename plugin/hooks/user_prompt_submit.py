#!/usr/bin/env python3
"""
UserPromptSubmit hook for the Sovereign Implementer plugin.

Fires when the user submits a prompt, before Claude processes it.
Classifies the user's first message of a session into one of the routing
categories defined in universal-behaviour.md → "Routing main-Claude's
openers" and injects the classification as additionalContext so Claude
starts with a structural routing hint rather than deriving it from
the prose table alone.

First-prompt detection:
  The hook searches the transcript for its own marker string. If the
  marker is present, the hook has already classified a prompt in this
  session and exits silently. This approach:
    - Doesn't depend on knowing the transcript's JSON schema
    - Naturally resets after /clear (transcript is wiped)
    - Mirrors the pattern pre_tool_use.py uses for V39 block-once

Classification:
  Keyword-based detection for clear signals only. The hook is a hint,
  not a gate — Claude makes the final routing decision. Conservative:
  better to give no hint than a wrong one. When signals are ambiguous
  the hook injects a generic "consult the routing table" reminder.

Output protocol:
  First prompt with clear signals: JSON with hookSpecificOutput
  containing additionalContext (the classification hint). Exit 0.
  Subsequent prompts or no clear signals: write nothing, exit 0.
"""

import json
import re
import sys
from pathlib import Path

CLASSIFICATION_MARKER = "[Sovereign Implementer — opener classification]"

# --- Classification patterns ---

# Test notes: user is pasting outcomes from a previous build's test session.
# Strong signals: TEST-LOG vocabulary, explicit Pass/Fail/Skipped words,
# row references like #001.
TEST_NOTE_PATTERNS = [
    re.compile(r"\b(?:Pass|Fail|Skipped)\b"),
    re.compile(r"#\d{3}\b"),
    re.compile(r"\btest(?:ed|ing|s)?\b", re.IGNORECASE),
    re.compile(r"\bsmoke\s*test", re.IGNORECASE),
    re.compile(r"\bTEST-LOG\b"),
]
TEST_NOTE_THRESHOLD = 2

# Setup signals: user wants to initialise or adopt.
SETUP_PATTERNS = [
    re.compile(r"/sovsetup\b"),
    re.compile(r"\bnew project\b", re.IGNORECASE),
    re.compile(r"\bset (?:this |it )?up\b", re.IGNORECASE),
    re.compile(r"\binitiali[sz]e\b", re.IGNORECASE),
    re.compile(r"\blet'?s start\b", re.IGNORECASE),
]

# Resume signals: user wants to continue an interrupted build.
RESUME_PATTERNS = [
    re.compile(r"\bresume\b", re.IGNORECASE),
    re.compile(r"\bcontinue (?:the |where )", re.IGNORECASE),
    re.compile(r"\bpick up where\b", re.IGNORECASE),
    re.compile(r"\bkeep going\b", re.IGNORECASE),
    re.compile(r"\bfinish (?:the |this )?(?:build|batch)\b", re.IGNORECASE),
]

# V90: Deliberate signals — user wants to work through open questions.
DELIBERATE_PATTERNS = [
    re.compile(r"/sovdeliberate\b"),
    re.compile(r"\bopen questions?\b", re.IGNORECASE),
    re.compile(r"\bwork through .* (?:OQ|question)", re.IGNORECASE),
    re.compile(r"\bdeliberate\b", re.IGNORECASE),
    re.compile(r"\breckon with\b", re.IGNORECASE),
]

# V90: Ideate signals — user has a new idea or wants to brainstorm.
IDEATE_PATTERNS = [
    re.compile(r"/sovideate\b"),
    re.compile(r"\bnew idea\b", re.IGNORECASE),
    re.compile(r"\bbrainstorm\b", re.IGNORECASE),
    re.compile(r"\bwhat if\b", re.IGNORECASE),
    re.compile(r"\bI'?ve been thinking\b", re.IGNORECASE),
    re.compile(r"\bfeature request\b", re.IGNORECASE),
    re.compile(r"\blet'?s add\b", re.IGNORECASE),
]

# V90: Structural planning signals — user wants to reshape the roadmap.
PLAN_STRUCTURAL_PATTERNS = [
    re.compile(r"/sovplan\b"),
    re.compile(r"\breorder\b", re.IGNORECASE),
    re.compile(r"\bsplit (?:the |this )?batch", re.IGNORECASE),
    re.compile(r"\bmerge (?:the |these )?batch", re.IGNORECASE),
    re.compile(r"\brescope\b", re.IGNORECASE),
    re.compile(r"\bplanning session\b", re.IGNORECASE),
    re.compile(r"\breorganis[ez]\b", re.IGNORECASE),
    re.compile(r"\bdependenc(?:y|ies)\b", re.IGNORECASE),
]


def parse_input():
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def already_classified(transcript_path):
    """Check if a classification has already been injected this session."""
    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError):
        return False
    return CLASSIFICATION_MARKER in text


def count_pattern_hits(text, patterns):
    """Count how many distinct patterns match in the text."""
    return sum(1 for p in patterns if p.search(text))


def classify(prompt):
    """Classify the user's prompt. Returns (route, detail) or None."""
    # Setup is highest priority — check first.
    if count_pattern_hits(prompt, SETUP_PATTERNS) >= 1:
        return ("setup", "Detected setup/initialisation request.")

    # Test notes need multiple signals to avoid false positives.
    test_hits = count_pattern_hits(prompt, TEST_NOTE_PATTERNS)
    if test_hits >= TEST_NOTE_THRESHOLD:
        return ("test_notes", f"Detected test-note signals ({test_hits} keyword matches).")

    # Resume.
    if count_pattern_hits(prompt, RESUME_PATTERNS) >= 1:
        return ("resume", "Detected resume/continue request.")

    # V90: Deliberate — OQ work-through.
    if count_pattern_hits(prompt, DELIBERATE_PATTERNS) >= 1:
        return ("deliberate", "Detected OQ deliberation request.")

    # V90: Ideate — new idea or feature request.
    if count_pattern_hits(prompt, IDEATE_PATTERNS) >= 1:
        return ("ideate", "Detected new idea / brainstorm request.")

    # V90: Structural planning — roadmap reshaping.
    if count_pattern_hits(prompt, PLAN_STRUCTURAL_PATTERNS) >= 1:
        return ("plan_structural", "Detected structural planning request.")

    # Not enough signal for confident classification.
    return None


def build_context(route, detail):
    """Build the additionalContext string for the classification."""
    route_instructions = {
        "setup": (
            "Suggested route: recommend /sovsetup. Wait for the user's okay "
            "before proceeding."
        ),
        "test_notes": (
            "Suggested route: read and follow the planning procedure at "
            "${CLAUDE_PLUGIN_ROOT}/docs/procedures/planning.md with "
            "primary_intent: test notes."
        ),
        "resume": (
            "Suggested route: check for _method/active-build.md (snapshot) "
            "or BACKLOG for an unfinished build batch. If one exists, "
            "confirm with the user before continuing the build."
        ),
        "deliberate": (
            "Suggested route: read and follow the deliberate procedure at "
            "${CLAUDE_PLUGIN_ROOT}/docs/procedures/deliberate.md."
        ),
        "ideate": (
            "Suggested route: read and follow the ideate procedure at "
            "${CLAUDE_PLUGIN_ROOT}/docs/procedures/ideate.md."
        ),
        "plan_structural": (
            "Suggested route: read and follow the planning procedure at "
            "${CLAUDE_PLUGIN_ROOT}/docs/procedures/planning.md."
        ),
    }

    instruction = route_instructions.get(route, "")

    return (
        f"{CLASSIFICATION_MARKER}\n"
        f"{detail}\n"
        f"{instruction}\n\n"
        "This is a hint from the UserPromptSubmit hook, not a gate. "
        "If the classification doesn't match the user's intent, "
        "consult the routing table in universal-behaviour.md and "
        "use your own judgement."
    )


def main():
    data = parse_input()
    if not isinstance(data, dict):
        return 0

    prompt = data.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    transcript_path = data.get("transcript_path")
    if isinstance(transcript_path, str) and transcript_path:
        if already_classified(transcript_path):
            return 0

    classification = classify(prompt)
    if classification is None:
        return 0

    route, detail = classification
    context = build_context(route, detail)

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
