#!/usr/bin/env python3
"""Consumer-side close mechanical: bump method-version footers and
regenerate proxy line-number pointers.

Usage:
    python bump_version.py <old> <new>    # bump footers + regen proxies
    python bump_version.py                # regen proxies only

Runs from the consumer project root (cwd). Invoked by the close
procedure's mechanical pass.
"""

import re
import sys
from datetime import date
from pathlib import Path

PROJECT = Path.cwd()

FOOTER_RE = re.compile(r"\*Sovereign Implementer — Version (\d+)\.\*")
PROXY_HEADER_RE = re.compile(
    r"<!-- proxy \| source: (.+?) \| generated: .+? -->"
)
PROXY_ENTRY_RE = re.compile(r"^(- L)(\d+)( \*\*.+)$")
HEADING_RE = re.compile(r"^(#{1,3}) (.+)$")

EXCLUDED_DIRS = {".git", ".claude", "node_modules", "__pycache__", ".obsidian"}


def iter_md_files(root: Path):
    for p in sorted(root.rglob("*.md")):
        if any(part in EXCLUDED_DIRS for part in p.parts):
            continue
        yield p


def bump_footers(old_v: int, new_v: int) -> list[str]:
    old = f"*Sovereign Implementer — Version {old_v}.*"
    new = f"*Sovereign Implementer — Version {new_v}.*"
    changed = []
    for md in iter_md_files(PROJECT):
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        if old in text:
            md.write_text(text.replace(old, new), encoding="utf-8")
            changed.append(str(md.relative_to(PROJECT)))
    return changed


def find_proxy_dir() -> Path | None:
    for candidate in ["_method/proxies", ".proxies"]:
        d = PROJECT / candidate
        if d.is_dir():
            return d
    return None


def build_heading_map(source_path: Path) -> dict[str, int]:
    headings = {}
    for i, line in enumerate(
        source_path.read_text(encoding="utf-8").splitlines(), 1
    ):
        m = HEADING_RE.match(line)
        if m:
            headings[m.group(2).strip()] = i
    return headings


def regenerate_proxy(proxy_path: Path) -> list[str]:
    warnings = []
    text = proxy_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines:
        return [f"  {proxy_path.name}: empty file, skipping"]

    header_match = PROXY_HEADER_RE.match(lines[0])
    if not header_match:
        return []

    source_rel = header_match.group(1)
    source_path = PROJECT / Path(source_rel)

    if not source_path.exists():
        warnings.append(
            f"  {proxy_path.name}: source {source_rel} not found, skipping"
        )
        return warnings

    headings = build_heading_map(source_path)

    today = date.today().isoformat()
    lines[0] = f"<!-- proxy | source: {source_rel} | generated: {today} -->"

    for i, line in enumerate(lines):
        m = PROXY_ENTRY_RE.match(line)
        if not m:
            continue
        prefix = m.group(1)
        bold_and_rest = m.group(3)

        bold_match = re.match(r" \*\*(.+?)\*\*", bold_and_rest)
        if not bold_match:
            continue
        entry_heading = bold_match.group(1)

        new_line_num = None
        if entry_heading in headings:
            new_line_num = headings[entry_heading]
        else:
            for src_heading, src_line in headings.items():
                if src_heading.startswith(entry_heading):
                    new_line_num = src_line
                    break

        if new_line_num is not None:
            lines[i] = f"{prefix}{new_line_num}{bold_and_rest}"
        else:
            warnings.append(
                f"  {proxy_path.name}: heading '{entry_heading}'"
                " not found in source"
            )

    proxy_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return warnings


def regenerate_all_proxies() -> list[str]:
    proxy_dir = find_proxy_dir()
    if proxy_dir is None:
        return ["  No proxy directory found, skipping"]
    warnings = []
    for proxy in sorted(proxy_dir.glob("*.md")):
        w = regenerate_proxy(proxy)
        warnings.extend(w)
        if not w:
            print(f"  {proxy.name}: OK")
    return warnings


def main():
    args = sys.argv[1:]

    if len(args) == 2:
        try:
            old_v = int(args[0])
            new_v = int(args[1])
        except ValueError:
            print("ERROR: old and new must be integers")
            sys.exit(1)
        if new_v <= old_v:
            print(
                f"ERROR: new ({new_v}) must be greater than old ({old_v})"
            )
            sys.exit(1)

        print(f"Bumping method version {old_v} → {new_v}\n")
        changed = bump_footers(old_v, new_v)
        print(f"Footers bumped ({len(changed)} files):")
        for f in changed:
            print(f"  {f}")
        print()

    elif len(args) != 0:
        print("Usage: bump_version.py [<old> <new>]")
        print("  With versions: bump footers + regenerate proxies")
        print("  Without: regenerate proxies only")
        sys.exit(1)

    print("Regenerating proxies...")
    warnings = regenerate_all_proxies()
    if warnings:
        print("\nProxy warnings:")
        for w in warnings:
            print(w)

    print("\nDone. Verify with: git diff")


if __name__ == "__main__":
    main()
