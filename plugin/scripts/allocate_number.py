#!/usr/bin/env python3
"""
allocate_number.py — shared NNNN allocator for the no-code-method plugin.

Scans a directory for files matching the `NNNN-*.md` pattern (4-digit zero-
padded prefix, kebab-case title, .md extension) and returns the next available
number. Numbers are never reused — the allocator finds the highest existing
number and adds 1.

Two call sites:
  - The planning subagent invokes this when creating a new consumer-project
    build batch file inside `BACKLOG/`.
  - Dev-session scope-file creation (manual or future slash command) uses the
    same logic for `planning/sessions/`.

CLI:

    python allocate_number.py <directory>

Output (stdout): the next available 4-digit number, e.g. `0003`.

Exit codes:
    0 — success, number printed.
    1 — directory doesn't exist or isn't a directory.
"""

import re
import sys
from pathlib import Path

NUMBERED_FILE_PATTERN = re.compile(r"^(\d{4})-.+\.md$")


def scan_highest_number(directory: Path) -> int:
    """Return the highest NNNN prefix found among files in directory, or 0
    if no matching files exist."""
    highest = 0
    try:
        for entry in directory.iterdir():
            if not entry.is_file():
                continue
            m = NUMBERED_FILE_PATTERN.match(entry.name)
            if m:
                num = int(m.group(1))
                if num > highest:
                    highest = num
    except OSError:
        pass
    return highest


def allocate_next(directory: Path) -> str:
    """Return the next available 4-digit number as a zero-padded string."""
    highest = scan_highest_number(directory)
    return f"{highest + 1:04d}"


def main():
    if len(sys.argv) < 2:
        print("Usage: allocate_number.py <directory>", file=sys.stderr)
        return 1

    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"Not a directory: {directory}", file=sys.stderr)
        return 1

    print(allocate_next(directory))
    return 0


if __name__ == "__main__":
    sys.exit(main())
