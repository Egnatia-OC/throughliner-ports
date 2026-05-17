#!/usr/bin/env python3
"""
parse_backlog.py — shared BACKLOG.md parser for the no-code-method plugin.

Locates the top unticked build batch in a BACKLOG.md file and emits its data
as JSON on stdout. The "top unticked batch" is the first build batch (in
file order) whose `Files:` sub-section contains at least one `- [ ]` bullet.
Batches that are placeholders (no `Files:` section or empty `Files:` list)
and batches that are complete (all `- [x]`) are skipped past.

Three call sites consume this parser (V25):

  - The Stop hook embeds the JSON payload in its redirect reason to hand
    batch-executor the right batch.
  - The `/build` slash-command embeds the same payload when the user
    invokes a build manually.
  - The PreToolUse hook calls the parser at edit-time to look up the
    current batch's declared file list for the boundary check.

The parser is deliberately lenient: any failure (missing file, unparseable
section, malformed batch) results in `{}` on stdout and exit 0. Callers
treat empty output as "no top unticked batch found" — the Stop hook then
doesn't redirect, `/build` reports nothing to build, and the PreToolUse
hook falls through to allow.

CLI:

    python parse_backlog.py <path/to/BACKLOG.md>

Output (stdout, JSON, compact):

    {}  — when no top unticked batch is found.

    Otherwise:

    {
      "batch_heading": "<text after `### Batch:`>",
      "change_list":   ["<bullet text>", ...],
      "files": [
        {
          "path":         "<path as written between backticks>",
          "summary":      "<one-sentence change summary>",
          "ticked":       false,
          "prerequisite": false
        },
        ...
      ],
      "serves_ux":  ["<entry name>", ...],
      "serves_doc": [{"doc": "<DOC>.md", "content": "<text after the colon>"}, ...]
    }

  Paths are returned relative as-written; callers resolve against the
  project root.

Spec: DOC-STRUCTURE.md → BACKLOG.md structure → Build batches, and the
**`Files:` sub-section** sub-section.
"""

import json
import re
import sys
from pathlib import Path


# --- Patterns ---

# `## Build batches` section heading.
BUILD_BATCHES_SECTION_PATTERN = re.compile(r"^## Build batches\s*$", re.MULTILINE)

# Any other top-level section — bounds the build-batches section.
NEXT_TOP_SECTION_PATTERN = re.compile(r"^## ", re.MULTILINE)

# Batch heading: `### Batch: <name>`. Captures the name.
BATCH_HEADING_PATTERN = re.compile(r"^### Batch:\s*(.+?)\s*$", re.MULTILINE)

# `Files:` sub-section anchor.
FILES_LINE_PATTERN = re.compile(r"^Files:\s*$", re.MULTILINE)

# `Serves UX.md: <name(s)>.` line — names may be comma-separated.
SERVES_UX_PATTERN = re.compile(r"^Serves UX\.md:\s*(.+?)\.\s*$", re.MULTILINE)

# `Serves <DOC>.md: <content>.` line — matches any doc, including UX.md
# (filtered out below to avoid double-capture).
SERVES_DOC_PATTERN = re.compile(
    r"^Serves ([A-Za-z][\w.-]*\.md):\s*(.+?)\.\s*$", re.MULTILINE
)

# `Files:` sub-section bullet. Tick is `- [ ]` or `- [x]` (lower or upper).
# Path is in backticks. Em-dash separator with surrounding whitespace.
FILE_BULLET_PATTERN = re.compile(
    r"^- \[([ xX])\]\s+`([^`]+)`\s+—\s+(.+?)\s*$"
)

# Generic change-list bullet (any `- <text>`). Used to extract the change
# list from the pre-Files: region of a batch body.
CHANGE_BULLET_PATTERN = re.compile(r"^- (.+?)\s*$")

# Prerequisite carve-out label.
PREREQ_LABEL = "[Prerequisite, not in plan]"


# --- Helpers ---


def safe_read_text(path: Path):
    """Read text from path; return None on any IO/decoding failure. Mirrors
    the helper in pre_tool_use.py and session_start.py."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def find_section_bounds(text, heading_pattern, next_pattern):
    """Find the bounds of a section that starts at heading_pattern and ends
    at the next match of next_pattern (or EOF). Returns (start, end) on
    success, None if heading_pattern is missing."""
    m = heading_pattern.search(text)
    if not m:
        return None
    start = m.end()
    next_match = next_pattern.search(text, start)
    end = next_match.start() if next_match else len(text)
    return (start, end)


def extract_change_bullets(text):
    """Return a list of change-description bullets found in text (one per
    line). Used on the body region between the batch heading and the
    `Files:` anchor. Skips blank lines and non-bullet content."""
    bullets = []
    for line in text.splitlines():
        m = CHANGE_BULLET_PATTERN.match(line)
        if m:
            bullets.append(m.group(1).strip())
    return bullets


def parse_file_bullet(line):
    """Parse one `Files:` sub-section bullet. Returns dict on success, None
    on no match. Detects the `[Prerequisite, not in plan]` trailing label and
    strips it from the summary."""
    m = FILE_BULLET_PATTERN.match(line)
    if not m:
        return None
    tick_char, path, summary = m.group(1), m.group(2), m.group(3)
    prerequisite = PREREQ_LABEL in summary
    if prerequisite:
        # Remove the label, then trim trailing separator/whitespace it left
        # behind so the summary reads cleanly without dangling punctuation.
        summary = summary.replace(PREREQ_LABEL, "").rstrip(" —-").rstrip()
    return {
        "path": path,
        "summary": summary,
        "ticked": tick_char.lower() == "x",
        "prerequisite": prerequisite,
    }


def parse_batch_body(heading, body):
    """Parse the body of one batch (everything after the `### Batch:` heading,
    up to the next batch or end-of-section). Returns dict on success, None on
    malformed/placeholder batches (no `Files:` section or empty file list)."""
    files_match = FILES_LINE_PATTERN.search(body)
    if not files_match:
        return None

    change_list = extract_change_bullets(body[:files_match.start()])
    after_files = body[files_match.end():]

    files = []
    for line in after_files.splitlines():
        entry = parse_file_bullet(line)
        if entry:
            files.append(entry)

    if not files:
        return None

    serves_ux = []
    for m in SERVES_UX_PATTERN.finditer(after_files):
        for raw in m.group(1).split(","):
            cleaned = raw.strip()
            if cleaned:
                serves_ux.append(cleaned)

    serves_doc = []
    for m in SERVES_DOC_PATTERN.finditer(after_files):
        doc, content = m.group(1), m.group(2)
        if doc == "UX.md":
            continue  # already captured by SERVES_UX_PATTERN above
        serves_doc.append({"doc": doc, "content": content.strip()})

    return {
        "batch_heading": heading.strip(),
        "change_list": change_list,
        "files": files,
        "serves_ux": serves_ux,
        "serves_doc": serves_doc,
    }


def find_top_unticked_batch(text):
    """Walk the `## Build batches` section top-to-bottom and return the
    first batch with at least one `- [ ]` file. Returns {} if no qualifying
    batch is found, or if the section is missing or empty."""
    bounds = find_section_bounds(
        text, BUILD_BATCHES_SECTION_PATTERN, NEXT_TOP_SECTION_PATTERN
    )
    if bounds is None:
        return {}
    section_start, section_end = bounds
    section_text = text[section_start:section_end]

    batch_matches = list(BATCH_HEADING_PATTERN.finditer(section_text))
    if not batch_matches:
        return {}

    for i, batch_match in enumerate(batch_matches):
        heading = batch_match.group(1)
        body_start = batch_match.end()
        body_end = (
            batch_matches[i + 1].start()
            if i + 1 < len(batch_matches)
            else len(section_text)
        )
        body = section_text[body_start:body_end]

        batch = parse_batch_body(heading, body)
        if batch is None:
            # Placeholder / malformed: try the next batch.
            continue
        if all(f["ticked"] for f in batch["files"]):
            # Batch is complete; try the next one.
            continue
        return batch

    return {}


def main():
    if len(sys.argv) < 2:
        json.dump({}, sys.stdout)
        return 0

    path = Path(sys.argv[1])
    text = safe_read_text(path)
    if text is None:
        json.dump({}, sys.stdout)
        return 0

    result = find_top_unticked_batch(text)
    json.dump(result, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
