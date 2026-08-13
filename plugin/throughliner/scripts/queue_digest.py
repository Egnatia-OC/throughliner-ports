#!/usr/bin/env python3
"""Print a one-line-per-item digest of QUEUE.md.

Sibling to reorder_queue.py: a mechanical reader alongside the mechanical
writer. /plan's read-state runs this instead of paging the whole queue, and
can re-run it at any point in the session.

Why this exists. Reading QUEUE.md whole costs tens of thousands of tokens and
most of it is rationale prose, which queue-wide reasoning never touches — the
droppable skim, the ordering, and the below-line revisit all read headings,
tags, blockers and flags. This prints those and nothing else.

Why it satisfies the page-to-the-end rule rather than trading it away. That
rule exists because a truncated read is indistinguishable from a complete one
to whatever reasons over it. A digest generated from the whole file by code
cannot be silently truncated, so the guarantee is stronger than paging gives.
The field list is fixed by what queue-wide reasoning actually consumes; a step
needing an item's prose reads that item's prose at the moment it presents it.

Usage:
    python queue_digest.py <QUEUE.md path>

Exit codes: 0 on success, 1 on a usage or read error.
"""

import os
import re
import sys

# Force UTF-8 on the console output, once, before anything is printed. The
# digest echoes item headings, which routinely carry em-dashes and arrows; on
# Windows an unconfigured stream falls back to the console code page and a
# heading containing one crashes the run. Same fix, same reason, as
# reorder_queue.py. errors='replace' keeps a console that genuinely cannot
# render a character from turning a cosmetic problem into a crash.
for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        # Python < 3.7, or a stream that cannot be reconfigured (a pipe, or a
        # test harness replacement). Degraded, never fatal.
        pass

SLUG_RE = re.compile(r"\[([a-z0-9][a-z0-9-]*)\]\s*$")
ITEM_RE = re.compile(r"^####\s+\S")
BLOCKED_RE = re.compile(r"^Blocked by:\s*\[([a-z0-9][a-z0-9-]*)\]", re.IGNORECASE)
FLAG_RE = re.compile(r"^Red flag\s*·\s*State:\s*(\w+)", re.IGNORECASE)
FLAVOR_RE = re.compile(r"^\[(audit|user|freeform)\]\s*", re.IGNORECASE)
# "Runs alone" — the item is ready, but /next must not build it alongside other
# work. Printed on the item's digest line because a solo item changes how much
# of the ready region a single run can actually clear, which is exactly what a
# planning session is deciding when it reads the digest.
RUNS_ALONE_RE = re.compile(r"^\**Runs alone\**\s*$", re.IGNORECASE)
MARKER = "Cleared to run above this line"

# Placement-contradiction signals. Each is a contradiction the queue's own text
# already contains, so the check reports something rather than nothing — which
# is why this is a detector and not a duty to review periodically.
#
# An item is examined on the way into Processed and never again. A gate on the
# door and no inspection of the room are two different failures, and only the
# first was built. The live instance that produced these: an item sat cleared to
# run carrying, in its own bold text, "it must not be built as written."
DO_NOT_BUILD_PHRASES = (
    "must not be built as written",
    "must not be built",
    "returned unbuilt",
    "cannot be scoped by a build",
)
# The keep-check's second limb, failing after the fact: an item whose Files line
# names nothing, or whose build list is its own design's output, says outright
# that there is nothing for a build to change.
NO_FILES_PHRASES = (
    "none yet",
    "the design's output",
    "design's output",
)
FILES_LINE_RE = re.compile(r"^\**Files\b[^:]*:\**\s*(.*)$", re.IGNORECASE)

# A research file cited in a work item's prose. Research is filed because it
# will be re-read and reused, so a research file is an upstream dependency of
# everything scoped against it — but citation runs one way. When a finding is
# superseded there is no path back to the decisions built on it, and those
# decisions do not announce that they rest on anything. The convention that
# closes it: a superseded research file gains a `Superseded by:` line at its
# top, written at the moment someone already has the file open to re-validate
# it, and this check reads that line back.
RESEARCH_CITE_RE = re.compile(r"resources/research/([a-z0-9][a-z0-9._-]*\.md)")
SUPERSEDED_RE = re.compile(r"^\**Superseded by:?\**\s*(.+)$",
                           re.IGNORECASE | re.MULTILINE)


def parse(path):
    """Read the queue into a list of item dicts. Raises OSError if unreadable."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    items = []
    section = None
    above_marker = True
    current = None

    for raw in lines:
        stripped = raw.strip()

        if re.match(r"^##\s+Processed\b", stripped, re.IGNORECASE):
            section, above_marker, current = "Processed", True, None
            continue
        if re.match(r"^##\s+Unprocessed\b", stripped, re.IGNORECASE):
            section, current = "Unprocessed", None
            continue
        if MARKER in stripped:
            above_marker, current = False, None
            continue

        if ITEM_RE.match(stripped):
            if section is None:
                current = None
                continue
            heading = re.sub(r"^#+\s+", "", stripped)
            slug_match = SLUG_RE.search(heading)
            slug = slug_match.group(1) if slug_match else None
            heading = SLUG_RE.sub("", heading).strip()
            flavor_match = FLAVOR_RE.match(heading)
            flavor = flavor_match.group(1).lower() if flavor_match else "build"
            heading = FLAVOR_RE.sub("", heading).strip()
            current = {
                "section": section,
                # Only meaningful in Processed; Unprocessed has no marker.
                "cleared": above_marker if section == "Processed" else None,
                "flavor": flavor,
                "heading": heading,
                "slug": slug,
                "blocked_by": None,
                "flag": None,
                "runs_alone": False,
                # Lowercased prose, for the placement-contradiction checks. Not
                # printed — the digest stays one line per item.
                "prose": [],
                "files_line": None,
            }
            items.append(current)
            continue

        if current is not None:
            blocked = BLOCKED_RE.match(stripped)
            if blocked:
                current["blocked_by"] = blocked.group(1)
            flag = FLAG_RE.match(stripped)
            if flag:
                current["flag"] = flag.group(1).lower()
            if RUNS_ALONE_RE.match(stripped):
                current["runs_alone"] = True
            files = FILES_LINE_RE.match(stripped)
            if files and current["files_line"] is None:
                current["files_line"] = files.group(1).lower()
            if stripped:
                current["prose"].append(stripped.lower())

    return items


def _self_referential_phrase(item):
    """A do-not-build phrase this item says about ITSELF, or None.

    Precision matters more than reach here. Queue prose routinely quotes another
    item's text — one item's rationale for building a detector quoted the very
    words the detector looks for — and a flag that fires on a discussion of a
    problem, rather than on the problem, is how a lint becomes noise people learn
    to scroll past. That is the one real cost weighed against building this.

    The discriminator is mechanical: a slug reference appearing BEFORE the phrase
    on the same line means the sentence is about that other item. A slug after
    the phrase is a cross-reference hanging off a statement about this item, so
    it does not suppress.
    """
    for line in item["prose"]:
        for phrase in DO_NOT_BUILD_PHRASES:
            at = line.find(phrase)
            if at == -1:
                continue
            before = line[:at]
            others = [
                s for s in re.findall(r"\[([a-z0-9][a-z0-9-]*)\]", before)
                if s != item["slug"]
            ]
            if others:
                continue
            return phrase
    return None


def _superseded_research(item, root):
    """Research files this item cites that carry a `Superseded by:` line.

    Returns a list of (filename, what superseded it).

    COVERAGE LIMIT, stated here and in the digest's own output because it must
    never be read as complete: this catches only items that NAME the research
    file in their prose. An item scoped on a finding it never cites stays
    invisible, and nothing here reaches it.
    """
    if not root:
        return []
    hits, seen = [], set()
    for line in item["prose"]:
        for name in RESEARCH_CITE_RE.findall(line):
            if name in seen:
                continue
            seen.add(name)
            path = os.path.join(root, "resources", "research", name)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    # The line sits at the top of the file, so reading the
                    # opening is enough and a large file costs nothing.
                    head = f.read(4000)
            except OSError:
                continue
            match = SUPERSEDED_RE.search(head)
            if match:
                # A superseded note legitimately explains WHAT was superseded
                # and what still stands, so it can run to a paragraph. The
                # digest is one line per finding, so show the head of it and
                # let the reader open the file for the rest.
                by = " ".join(match.group(1).split())
                if len(by) > 90:
                    by = by[:90].rstrip() + "…"
                hits.append((name, by))
    return hits


def contradictions(items, root=""):
    """Items whose placement contradicts their own text. Flags, never decides.

    Moving an item out of Processed is a fate decision and stays the user's at
    /plan, so this reports and stops there.
    """
    found = []
    for item in items:
        slug = item["slug"] or "NO-SLUG"

        for name, by in _superseded_research(item, root):
            found.append(
                f"[{slug}] is scoped against resources/research/{name}, which "
                f"is marked superseded by {by} — re-read the item's premise "
                "before building it"
            )

        if item["section"] == "Processed":
            hit = _self_referential_phrase(item)
            if hit:
                found.append(
                    f"[{slug}] sits in Processed but its own text says "
                    f'"{hit}"'
                )

            files_line = item["files_line"]
            if files_line is not None:
                for phrase in NO_FILES_PHRASES:
                    if phrase in files_line:
                        found.append(
                            f"[{slug}] sits in Processed but its Files line "
                            f'says "{phrase}" — nothing for a build to change'
                        )
                        break

        blocker = item["blocked_by"]
        if blocker and locate(blocker, items) == "Processed/held":
            found.append(
                f"[{slug}] is blocked by [{blocker}], which is itself held — "
                "a hold chain, so neither moves until the chain's end does"
            )

    return found


def locate(slug, items):
    """Where a slug sits, for resolving a Blocked by: reference."""
    for item in items:
        if item["slug"] == slug:
            if item["section"] == "Unprocessed":
                return "Unprocessed"
            return "Processed/cleared" if item["cleared"] else "Processed/held"
    return "ABSENT"


def render(items, root=""):
    out = []
    for section in ("Processed", "Unprocessed"):
        in_section = [i for i in items if i["section"] == section]
        out.append(f"## {section} — {len(in_section)} item(s)")
        if section == "Processed":
            cleared = sum(1 for i in in_section if i["cleared"])
            out.append(f"   {cleared} cleared to run, {len(in_section) - cleared} held below the line")
        for item in in_section:
            bits = []
            if section == "Processed":
                bits.append("cleared" if item["cleared"] else "held")
            bits.append(item["flavor"])
            if item["runs_alone"]:
                bits.append("runs alone")
            slug = item["slug"] or "NO-SLUG"
            line = f"- [{slug}] ({', '.join(bits)}) {item['heading']}"
            if item["blocked_by"]:
                line += f"  | Blocked by: [{item['blocked_by']}] -> {locate(item['blocked_by'], items)}"
            if item["flag"]:
                line += f"  | Red flag: {item['flag']}"
            out.append(line)
        out.append("")

    flags = contradictions(items, root)
    out.append(f"## Placement contradictions — {len(flags)}")
    if flags:
        out.extend(f"- {f}" for f in flags)
        out.append(
            "These are flags, not decisions. Moving an item out of Processed is "
            "the user's call at /plan."
        )
    else:
        out.append("- none")
    out.append(
        "Superseded-research flags cover only items that NAME the research file "
        "in their prose. An item scoped on a finding it never cites is not "
        "reached by this check — read it as partial coverage, not a clean bill."
    )
    out.append("")
    return "\n".join(out)


def main(argv):
    if len(argv) != 2:
        print("usage: queue_digest.py <QUEUE.md path>", file=sys.stderr)
        return 1
    try:
        items = parse(argv[1])
    except OSError as exc:
        print(f"queue_digest: cannot read {argv[1]}: {exc}", file=sys.stderr)
        return 1
    # The project root is the queue file's own folder, so the research files an
    # item cites can be opened without asking for a second argument.
    root = os.path.dirname(os.path.abspath(argv[1]))
    print(render(items, root))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
