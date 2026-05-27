#!/usr/bin/env python3
"""
parse_backlog.py — shared BUILD-PLAN parser for the no-code-method plugin.

Locates the top unticked build batch and emits its data as JSON on stdout.
The "top unticked batch" is the first build batch (in priority order) whose
`Files:` sub-section contains at least one `- [ ]` bullet. Batches with
`Status: shipped` or `Status: parked` are skipped. Batches that are
placeholders (no `Files:` section or empty `Files:` list) and batches
that are complete (all `- [x]`) are also skipped past.

Supports two BUILD-PLAN formats (auto-detected):

  **Single-file (legacy):** A single `BUILD-PLAN.md` with full batch content
  inline in the `## Build batches` section. Detected when the section
  contains `### Batch:` headings.

  **Folder (V48+):** A `BUILD-PLAN/` folder with `INDEX.md` (carrying the
  build-order list as backtick-wrapped filenames) and per-batch `.md`
  files. Detected when `## Build batches` contains reference lines
  (`` - `NNNN-name.md` ``) instead of `### Batch:` headings.

Three call sites consume this parser (V25, extended V46, V66):

  - The `/sovbuild` slash-command embeds the JSON payload when the user
    invokes a build manually.
  - The PreToolUse hook calls the parser at edit-time to look up the
    current batch's declared file list for the boundary check, and for
    the test-confirmation gate's active-batch detection.
  - The PostToolUse hook (V46) imports `find_top_unticked_batch` directly
    (not subprocess) to validate BUILD-PLAN format after each edit.

The parser is deliberately lenient: any failure (missing file, unparseable
section, malformed batch) results in `{}` on stdout and exit 0. Callers
treat empty output as "no top unticked batch found" — `/sovbuild` reports
nothing to build, and the PreToolUse hook falls through to allow.

CLI:

    python parse_backlog.py <path/to/BUILD-PLAN.md>
    python parse_backlog.py <path/to/BUILD-PLAN/INDEX.md>

Output (stdout, JSON, compact):

    {}  — when no top unticked batch is found.

    Otherwise:

    {
      "batch_heading": "<batch name>",
      "batch_file":    "<filename — only present in folder mode>",
      "status":        "<queued|active|parked|shipped — default: queued>",
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

Spec: DOC-STRUCTURE.md → BUILD-PLAN structure → Build batches, the
**`Changes:` delimiter** (V47), and the **`Files:` sub-section**.
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

# Batch heading: `### Batch: <name>`. Captures the name. (Single-file mode.)
BATCH_HEADING_PATTERN = re.compile(r"^### Batch:\s*(.+?)\s*$", re.MULTILINE)

# Per-batch file H1 heading: `# <name>`. Captures the name. (Folder mode.)
BATCH_FILE_H1_PATTERN = re.compile(r"^# (.+?)\s*$", re.MULTILINE)

# Batch reference line in INDEX.md: `- `NNNN-name.md`` with optional description.
BATCH_REF_PATTERN = re.compile(r"^-\s+`(\d{4}-.+?\.md)`", re.MULTILINE)

# `Changes:` sub-section anchor (V47 — separates scope sections from change list).
CHANGES_LINE_PATTERN = re.compile(r"^Changes:\s*$", re.MULTILINE)

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

# Template placeholder detection: matches strings entirely wrapped in
# square brackets, like `[path/to/file]` or `[short descriptive name]`
# from BUILD-PLAN-TEMPLATE.md. Real batch headings and real file paths
# never match. Legitimate bracket labels ([Requested], [Suggested],
# [Prerequisite, not in plan]) live in build recaps or file summaries,
# not in batch headings or file paths — outside this pattern's scope.
TEMPLATE_PLACEHOLDER_PATTERN = re.compile(r"^\[[^\]]+\]$")

# `Status:` line — batch lifecycle state. Four values: queued, active,
# parked, shipped. Absent = queued (default).
STATUS_LINE_PATTERN = re.compile(r"^Status:\s*(\w+)\s*$", re.MULTILINE)

SKIP_STATUSES = frozenset(("shipped", "parked"))


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
        summary = summary.replace(PREREQ_LABEL, "").rstrip(" —-").rstrip()
    return {
        "path": path,
        "summary": summary,
        "ticked": tick_char.lower() == "x",
        "prerequisite": prerequisite,
    }


def parse_batch_body(heading, body):
    """Parse the body of one batch (everything after the heading, up to
    the next batch or end-of-section/file). Returns dict on success, None
    on malformed/placeholder batches (no `Files:` section or empty file
    list). Works for both single-file mode (body from `### Batch:` region)
    and folder mode (body from per-batch file after `# <name>`)."""
    files_match = FILES_LINE_PATTERN.search(body)
    if not files_match:
        return None

    status_match = STATUS_LINE_PATTERN.search(body)
    status = status_match.group(1).lower() if status_match else "queued"

    changes_match = CHANGES_LINE_PATTERN.search(body)
    if changes_match and changes_match.start() < files_match.start():
        change_region = body[changes_match.end():files_match.start()]
    else:
        change_region = body[:files_match.start()]
    change_list = extract_change_bullets(change_region)
    after_files = body[files_match.end():]

    files = []
    for line in after_files.splitlines():
        entry = parse_file_bullet(line)
        if entry:
            files.append(entry)

    if not files:
        return None

    if TEMPLATE_PLACEHOLDER_PATTERN.match(heading.strip()):
        return None
    for f in files:
        if TEMPLATE_PLACEHOLDER_PATTERN.match(f["path"]):
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
            continue
        serves_doc.append({"doc": doc, "content": content.strip()})

    return {
        "batch_heading": heading.strip(),
        "status": status,
        "change_list": change_list,
        "files": files,
        "serves_ux": serves_ux,
        "serves_doc": serves_doc,
    }


def parse_batch_file(batch_path: Path):
    """Parse a per-batch file (folder mode). The file starts with
    `# <batch name>` and the rest is batch body. Returns dict on
    success (with `batch_file` key added), None on any failure."""
    text = safe_read_text(batch_path)
    if text is None:
        return None

    h1_match = BATCH_FILE_H1_PATTERN.search(text)
    if not h1_match:
        return None

    heading = h1_match.group(1)
    body = text[h1_match.end():]
    result = parse_batch_body(heading, body)
    if result is not None:
        result["batch_file"] = batch_path.name
    return result


# --- Single-file mode (legacy) ---


def find_top_unticked_batch(text):
    """Walk the `## Build batches` section top-to-bottom and return the
    first batch with at least one `- [ ]` file. Returns {} if no qualifying
    batch is found, or if the section is missing or empty.

    Auto-detects format: if the section contains `### Batch:` headings,
    uses single-file mode (inline batches). If it contains backtick
    reference lines, uses folder mode — but folder mode requires a path
    to resolve batch files, so this text-only function falls back to
    single-file parsing. Callers that have a path should use
    `find_top_unticked_batch_from_path` instead."""
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
            continue
        if batch["status"] in SKIP_STATUSES:
            continue
        if all(f["ticked"] for f in batch["files"]):
            continue
        return batch

    return {}


# --- Folder mode ---


def resolve_backlog_dir_from_index(index_path: Path) -> Path:
    """Resolve the BUILD-PLAN/ directory that holds per-batch files.

    When the index is INDEX.md inside BUILD-PLAN/, the dir is the parent.
    When the index is a proxy at proxies/build-plan.md, the BUILD-PLAN/ dir
    is a sibling of the proxies/ directory (i.e. _method/BUILD-PLAN/).
    Falls back to the index's parent if neither pattern matches."""
    if index_path.name.upper() == "INDEX.MD":
        return index_path.parent
    if (index_path.name.lower() == "build-plan.md"
            and index_path.parent.name == "proxies"):
        return index_path.parent.parent / "BUILD-PLAN"
    return index_path.parent


def find_top_unticked_batch_folder(index_path: Path):
    """Folder mode: read the index (INDEX.md or proxies/build-plan.md),
    extract the ordered list of batch file references from
    `## Build batches`, read each batch file in order, and return the
    first with unticked files. Returns {} if none found."""
    text = safe_read_text(index_path)
    if text is None:
        return {}

    bounds = find_section_bounds(
        text, BUILD_BATCHES_SECTION_PATTERN, NEXT_TOP_SECTION_PATTERN
    )
    if bounds is None:
        return {}
    section_text = text[bounds[0]:bounds[1]]

    batch_refs = BATCH_REF_PATTERN.findall(section_text)
    if not batch_refs:
        return {}

    backlog_dir = resolve_backlog_dir_from_index(index_path)
    for filename in batch_refs:
        batch_path = backlog_dir / filename
        batch = parse_batch_file(batch_path)
        if batch is None:
            continue
        if batch["status"] in SKIP_STATUSES:
            continue
        if all(f["ticked"] for f in batch["files"]):
            continue
        return batch

    return {}


# --- Auto-detecting entry point ---


def is_folder_mode(index_path: Path) -> bool:
    """Detect whether the BUILD-PLAN is in folder mode. True if the file is
    a proxy-as-index (build-plan.md in a proxies/ dir) or named INDEX.md
    inside a directory, AND the `## Build batches` section contains batch
    reference lines OR no `### Batch:` headings (empty or reference-only).
    Falls back to single-file mode on any ambiguity."""
    name_upper = index_path.name.upper()
    if name_upper != "INDEX.MD" and name_upper != "BUILD-PLAN.MD":
        return False
    if name_upper == "BUILD-PLAN.MD" and index_path.parent.name != "proxies":
        return False
    text = safe_read_text(index_path)
    if text is None:
        return False
    bounds = find_section_bounds(
        text, BUILD_BATCHES_SECTION_PATTERN, NEXT_TOP_SECTION_PATTERN
    )
    if bounds is None:
        return False
    section_text = text[bounds[0]:bounds[1]]
    if BATCH_HEADING_PATTERN.search(section_text):
        return False
    return True


def find_top_unticked_batch_from_path(path: Path):
    """Auto-detecting entry point. Accepts a path to either BUILD-PLAN.md
    (single-file) or BUILD-PLAN/INDEX.md (folder mode). Returns the same
    dict shape as `find_top_unticked_batch`."""
    if is_folder_mode(path):
        return find_top_unticked_batch_folder(path)

    text = safe_read_text(path)
    if text is None:
        return {}
    return find_top_unticked_batch(text)


def main():
    if len(sys.argv) < 2:
        json.dump({}, sys.stdout)
        return 0

    path = Path(sys.argv[1])
    result = find_top_unticked_batch_from_path(path)
    json.dump(result, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
