#!/usr/bin/env python3
"""Close-session mechanical: bump method-version footers, plugin.json,
PLUGIN_METHOD_VERSION, and regenerate dev-side proxy line-number pointers.

Usage:
    python bump_version.py <old> <new> --session-tag <tag>   # bump + proxies
    python bump_version.py --session-tag <tag>               # proxies only

Examples:
    python bump_version.py 95 96 --session-tag v123
    python bump_version.py --session-tag v123
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

EXCLUDED_PREFIXES = (
    "tests\\fixtures",
    "tests/fixtures",
)

PROXY_DIR = REPO / "_method" / "proxies"
PROXY_HEADER_RE = re.compile(
    r"<!-- proxy \| source: (.+?) \| generated: .+? \| when: (.+?) -->"
)
PROXY_ENTRY_RE = re.compile(r"^(- L)(\d+)( \*\*.+)$")
HEADING_RE = re.compile(r"^(#{1,3}) (.+)$")


def is_excluded(path: Path) -> bool:
    rel = str(path.relative_to(REPO))
    return any(rel.startswith(p) for p in EXCLUDED_PREFIXES)


def bump_footers(old_v: int, new_v: int) -> list[str]:
    old = f"*No-code method — Version {old_v}.*"
    new = f"*No-code method — Version {new_v}.*"
    changed = []
    for md in sorted(REPO.rglob("*.md")):
        if is_excluded(md):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        if old in text:
            md.write_text(text.replace(old, new), encoding="utf-8")
            changed.append(str(md.relative_to(REPO)))
    return changed


def bump_plugin_json(old_v: int, new_v: int) -> bool:
    pj = REPO / "plugin" / ".claude-plugin" / "plugin.json"
    text = pj.read_text(encoding="utf-8")
    old_ver = f'"0.{old_v}.0"'
    new_ver = f'"0.{new_v}.0"'
    if old_ver in text:
        pj.write_text(text.replace(old_ver, new_ver), encoding="utf-8")
        return True
    print(f"  WARNING: {old_ver} not found in plugin.json", file=sys.stderr)
    return False


def bump_session_start(old_v: int, new_v: int) -> bool:
    ss = REPO / "plugin" / "hooks" / "session_start.py"
    text = ss.read_text(encoding="utf-8")
    old_const = f"PLUGIN_METHOD_VERSION = {old_v}"
    new_const = f"PLUGIN_METHOD_VERSION = {new_v}"
    if old_const in text:
        ss.write_text(text.replace(old_const, new_const), encoding="utf-8")
        return True
    print(f"  WARNING: {old_const} not found in session_start.py", file=sys.stderr)
    return False


def build_heading_map(source_path: Path) -> dict[str, int]:
    """Map heading text -> line number (1-indexed) for # / ## / ### headings."""
    headings = {}
    for i, line in enumerate(source_path.read_text(encoding="utf-8").splitlines(), 1):
        m = HEADING_RE.match(line)
        if m:
            headings[m.group(2).strip()] = i
    return headings


def regenerate_proxy(proxy_path: Path, session_tag: str) -> list[str]:
    """Update one proxy file's header and line-number pointers. Returns warnings."""
    warnings = []
    text = proxy_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines:
        return [f"  {proxy_path.name}: empty file, skipping"]

    header_match = PROXY_HEADER_RE.match(lines[0])
    if not header_match:
        warnings.append(f"  {proxy_path.name}: no proxy header, skipping")
        return warnings

    source_rel = header_match.group(1)
    when_field = header_match.group(2)
    source_path = REPO / Path(source_rel)

    if not source_path.exists():
        warnings.append(f"  {proxy_path.name}: source {source_rel} not found, skipping")
        return warnings

    headings = build_heading_map(source_path)

    today = date.today().isoformat()
    lines[0] = (
        f"<!-- proxy | source: {source_rel} "
        f"| generated: {today} {session_tag} "
        f"| when: {when_field} -->"
    )

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
                f"  {proxy_path.name}: heading '{entry_heading}' not found in source"
            )

    proxy_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return warnings


def regenerate_all_proxies(session_tag: str) -> list[str]:
    warnings = []
    if not PROXY_DIR.exists():
        return ["  Proxy directory not found, skipping"]
    for proxy in sorted(PROXY_DIR.glob("*.md")):
        w = regenerate_proxy(proxy, session_tag)
        warnings.extend(w)
        if not w:
            print(f"  {proxy.name}: OK")
    return warnings


def main():
    parser = argparse.ArgumentParser(
        description="Bump method version and regenerate dev-side proxies."
    )
    parser.add_argument(
        "old", nargs="?", type=int, default=None,
        help="Current method version (e.g. 95). Omit both to run proxies only.",
    )
    parser.add_argument(
        "new", nargs="?", type=int, default=None,
        help="New method version (e.g. 96). Omit both to run proxies only.",
    )
    parser.add_argument(
        "--session-tag", required=True,
        help="Session tag for proxy headers (e.g. v123)",
    )
    args = parser.parse_args()

    do_bump = args.old is not None and args.new is not None
    if (args.old is None) != (args.new is None):
        print("ERROR: provide both old and new versions, or neither")
        sys.exit(1)

    if do_bump:
        if args.new <= args.old:
            print(
                f"ERROR: new version ({args.new}) must be greater "
                f"than old ({args.old})"
            )
            sys.exit(1)

        print(f"Bumping method version {args.old} -> {args.new}\n")

        changed = bump_footers(args.old, args.new)
        print(f"Footers bumped ({len(changed)} files):")
        for f in changed:
            print(f"  {f}")

        print()
        ok = bump_plugin_json(args.old, args.new)
        print(f"plugin.json: {'updated' if ok else 'SKIPPED (see warning)'}")

        ok = bump_session_start(args.old, args.new)
        print(f"PLUGIN_METHOD_VERSION: {'updated' if ok else 'SKIPPED (see warning)'}")
        print()

    print(f"Regenerating proxies ({args.session_tag})...")
    warnings = regenerate_all_proxies(args.session_tag)
    if warnings:
        print("\nProxy warnings:")
        for w in warnings:
            print(w)

    print("\nDone. Verify with: git diff")


if __name__ == "__main__":
    main()
