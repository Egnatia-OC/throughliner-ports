#!/usr/bin/env python3
"""Generate the build view: the cleared region's instructions, and no history.

Why this exists. A run used to read the whole of QUEUE.md to build a handful of
items — tens of thousands of words, most of it decision history that the build
has no use for. That was the cheap reason. The real one is that a build
TRANSCRIBES what it reads: reasoning written into a work item was measured
reaching the method's own shipped documents in near-verbatim form, so the
history was being copied out of the record and into the rules. A build cannot
copy what it was never given.

So each cleared work item carries a delimited BUILD BLOCK, authored at /plan's
keep-step with the user present, holding what changes in which files, how to
tell it worked, any risk it carries, and any option already refused. This script
copies those blocks byte-for-byte, keyed by slug, into a generated view. /next
reads the view; the close resolves each slug back against QUEUE.md as one
targeted read of one entry, so the reasoning still travels into the record.

Refusals travel and the rest of the history does not. A build that cannot see
why an option was rejected proposes it again and stops to ask, which is the one
failure the saving would otherwise buy.

The view also lists EVERY entry in both sections by heading and slug alone,
carrying no reasoning at all, so a build filing something it noticed can still
tell whether that thing is already in the queue. What that does not restore is
knowing what other work DEPENDS on a thing — a heading says an item exists and
nothing more — so a build's captures are weaker at spotting which detail matters
to work already queued. That cost is real and is recorded rather than denied.

This is a PROJECTION and never a deletion. QUEUE.md keeps every item's reasoning
inline and whole, which is what the throughline requires. The view is
regenerated rather than merged, so nothing is ever reconciled back: the only
write-back is deleting the slugs that shipped, which reorder_queue.py already
does.

Contract:
  python generate_build_view.py <queue_path> [--out <path>]

  Writes the view to <project root>/BUILD-VIEW.md unless --out names another
  path. Prints a one-line summary to stdout.

Exit codes: 0 wrote the view, 1 refused (with a reason on stderr).
"""

import os
import re
import sys

# Duplicated from reorder_queue.py deliberately: the hooks and scripts run
# standalone from a copied plugin cache and cannot import a shared module, which
# is also why a shared module was rejected. See CLAUDE.md's scripting
# constraints.
for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding='utf-8', errors='replace')
    except (AttributeError, ValueError, OSError):
        pass

MARKER_RE = re.compile(r'^---\s*Cleared to run above this line\s*---\s*$')
SECTION_RE = re.compile(r'^##\s+(Processed|Unprocessed)\s*$')
HEADING_RE = re.compile(r'^####\s+(.*)$')
SLUG_RE = re.compile(r'\[([^\]]+)\]\s*$')

BLOCK_OPEN = '--- Build block ---'
BLOCK_CLOSE = '--- End build block ---'

# The flavor tag leading a heading, if any. A build view carries build and
# [audit] items; a [user] item is walked through and a [freeform] one halts the
# run, so neither is built from a block — but both are still LISTED, because the
# run has to know they are there.
FLAVOR_RE = re.compile(r'^\[(audit|user|freeform)\]\s+')


def die(msg):
    sys.stderr.write("generate_build_view: " + msg + "\n")
    sys.exit(1)


def heading_slug(text):
    m = SLUG_RE.search(text)
    return m.group(1) if m else None


def without_slug(text):
    """The heading with its trailing `[slug]` removed.

    The slug is printed as the addressable key on its own, so leaving it on the
    end of the description too prints it twice on every line.
    """
    return SLUG_RE.sub("", text).rstrip()


def flavor(text):
    m = FLAVOR_RE.match(text)
    return m.group(1) if m else "build"


def parse(lines):
    """Every entry in the file, with its section, cleared state and body.

    Reads the file end to end. That is the point of doing this in code rather
    than by reading: a script cannot be silently truncated the way a read can,
    so the fields it computes are trustworthy in a way a summary is not.
    """
    entries = []
    section = None
    cleared = True
    current = None
    for i, raw in enumerate(lines):
        line = raw.rstrip('\n')
        sec = SECTION_RE.match(line)
        if sec:
            section = sec.group(1)
            # Each section starts above its own marker; Unprocessed has none,
            # and nothing there is ever cleared.
            cleared = (section == "Processed")
            current = None
            continue
        if MARKER_RE.match(line):
            cleared = False
            current = None
            continue
        if section is None:
            continue
        head = HEADING_RE.match(line)
        if head:
            current = {
                "section": section,
                "cleared": cleared and section == "Processed",
                "heading": head.group(1).strip(),
                "slug": heading_slug(head.group(1).strip()),
                "flavor": flavor(head.group(1).strip()),
                "line": i + 1,
                "body": [],
            }
            entries.append(current)
            continue
        if current is not None:
            current["body"].append(line)
    return entries


RUNS_ALONE_RE = re.compile(r"^\s*(?:\*\*)?Runs alone(?:\*\*)?\s*$")

# The rule-gate disposition (and any FAQ disposition) an item carries in its
# prose, outside the build block. The build is required to TRANSCRIBE these,
# never compose them — so the view must carry them, or a build authoring a rule
# halts on a disposition it cannot see. Tolerates the bolded label form for the
# same reason the LOG rule does: `**Rule gate:**` is the ordinary Markdown
# instinct, and a disposition that silently fails to match is worse than one
# written two ways.
DISPOSITION_RE = re.compile(r"^\s*(?:\*\*)?(Rule gate|FAQ):(?:\*\*)?\s*(.*)$")


def dispositions(entry):
    """Every labelled disposition line in the entry's prose, normalised.

    Read from the whole body, including inside the build block — where a
    keep-step wrote it inside the delimiters it would otherwise appear twice,
    so lines inside the block are skipped (the block already travels verbatim).
    """
    out = []
    inside = False
    for line in entry["body"]:
        stripped = line.strip()
        if stripped == BLOCK_OPEN:
            inside = True
            continue
        if stripped == BLOCK_CLOSE:
            inside = False
            continue
        if inside:
            continue
        m = DISPOSITION_RE.match(line)
        if m:
            out.append("%s: %s" % (m.group(1), m.group(2).strip()))
    return out


def runs_alone(entry):
    """True where the entry carries the `Runs alone` marker on its own line.

    Tolerates the bold form for the same reason the queue lint does: `**Runs
    alone**` is the ordinary Markdown instinct, and a marker that silently fails
    to match is worse than one written two ways.
    """
    return any(RUNS_ALONE_RE.match(line) for line in entry["body"])


# The label leading a [user] item's walk-through steps, bold or plain, with a
# `.` or `:` after the word. Tolerating the bold form for the same reason the
# other labels here do.
WALKTHROUGH_RE = re.compile(r"^\s*\*{0,2}Walkthrough[.:]\*{0,2}", re.IGNORECASE)


def walkthrough(entry):
    """The block led by the entry's Walkthrough label, byte-for-byte, or None.

    A [user] item is driven live from the view, so its steps must travel the
    same way a build item's block does — copied verbatim from the label line to
    the end of the entry, trailing blanks trimmed. Where no label exists the
    caller says so, and the run halts on the item.
    """
    start = None
    for i, line in enumerate(entry["body"]):
        if WALKTHROUGH_RE.match(line):
            start = i
            break
    if start is None:
        return None
    block = entry["body"][start:]
    while block and not block[-1].strip():
        block.pop()
    return block


# A LOG entry filename, and the kind/legacy-numeric suffix a slug's second
# record carries — both duplicated from queue_digest.py, which cannot be
# imported for the standalone-cache reason above. Only these exact suffix
# shapes are stripped; prefix-matching arbitrary suffixes would misattribute a
# slug that extends another slug.
LOG_ENTRY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-([a-z0-9][a-z0-9-]*)\.md$")
RECORD_SUFFIX_RE = re.compile(r"-(?:plan|build|\d+)$")


def records_on_file(root, slug):
    """LOG/ filenames whose slug resolves to this item's, sorted.

    A [user] item's walk-through must resume after what the record shows done,
    and the view is what an unattended run actually reads — so the pointer to
    the records travels in the view rather than relying on the run remembering
    to look.
    """
    if not slug:
        return []
    folder = os.path.join(root, "LOG")
    try:
        names = os.listdir(folder)
    except OSError:
        return []
    found = []
    for name in names:
        m = LOG_ENTRY_RE.match(name)
        if m and RECORD_SUFFIX_RE.sub("", m.group(1)) == slug:
            found.append(name)
    return sorted(found)


def needs_block(entry):
    """True where this cleared entry is one a run builds from a block.

    `[user]` and `[freeform]` items are never built from a block — one is walked
    through, the other halts the run — so counting them among the items that
    need one made the summary's two numbers permanently unequal in any project
    holding either. A completeness test that can never read equal distinguishes
    nothing at the moment it is read.
    """
    return entry["flavor"] not in ("user", "freeform")


def build_block(entry):
    """The entry's build block, verbatim, or None where it carries none.

    Byte-for-byte is not a nicety. The block is the build's whole instruction
    set, so anything that reformats it on the way through is a place where the
    instructions can quietly change between what the user approved at the
    keep-step and what the run acts on.
    """
    out = []
    inside = False
    for line in entry["body"]:
        stripped = line.strip()
        if stripped == BLOCK_OPEN:
            if inside:
                return None, "a second '%s' before the first was closed" % BLOCK_OPEN
            inside = True
            continue
        if stripped == BLOCK_CLOSE:
            if not inside:
                return None, "'%s' with no opening line" % BLOCK_CLOSE
            return out, None
        if inside:
            out.append(line)
    if inside:
        return None, "'%s' with no closing '%s'" % (BLOCK_OPEN, BLOCK_CLOSE)
    return None, None


def render(entries, root):
    out = []
    out.append("# BUILD VIEW — generated, do not edit")
    out.append("")
    out.append(
        "Regenerated from QUEUE.md. Editing this file changes nothing: the next "
        "run overwrites it. The queue itself is where work is changed."
    )
    out.append("")
    out.append(
        "**This carries instructions and no decision history, deliberately.** "
        "Each item below is what the keep-step agreed would change, how to tell "
        "it worked, and any option already refused. Why the work is worth doing "
        "lives in QUEUE.md and is read back at the close, one entry at a time."
    )
    out.append("")

    cleared = [e for e in entries if e["cleared"]]
    out.append("## Cleared to run — %d item(s)" % len(cleared))
    out.append("")
    if not cleared:
        out.append("Nothing is cleared to run. /plan vets work before it reaches here.")
        out.append("")

    problems = []
    for e in cleared:
        slug = e["slug"] or "NO-SLUG"
        out.append("### [%s] %s" % (slug, without_slug(e["heading"])))
        out.append("")
        out.append("Flavor: %s" % e["flavor"])
        out.append("")
        # `Runs alone` is the run's SECOND bound, and it lives outside the build
        # block — so the projection dropped it and a run could not see where it
        # was supposed to stop. Emitted here, beside the block, because that is
        # where the run reads the work it is about to build; putting it only in
        # the by-name listing would separate the bound from the item it bounds.
        if runs_alone(e):
            out.append("Runs alone")
            out.append("")
        # Dispositions travel with the instructions. A build transcribes them
        # (never composes them), so a view without them makes every
        # rule-amending item halt on a disposition the item actually carries.
        dispo = dispositions(e)
        if dispo:
            out.extend(dispo)
            out.append("")
        # A [user] item is not built from a block — it is walked through live,
        # and the steps travel into the view so the run never reads the queue.
        if e["flavor"] == "user":
            # The record check travels with the item: a walk-through resumes
            # after what the record shows done, and the view is what an
            # unattended run reads.
            records = records_on_file(root, e["slug"])
            if records:
                out.append("Records on file: %s" % ", ".join(records))
                out.append("")
            steps = walkthrough(e)
            if steps is None:
                out.append(
                    "**No walkthrough travelled.** This item carries no "
                    "Walkthrough block, so the view has no steps to drive it "
                    "with and the run halts on it."
                )
            else:
                out.extend(steps)
            out.append("")
            continue
        block, err = build_block(e)
        if err:
            problems.append("[%s]: %s" % (slug, err))
        if block is None:
            # Stated in the view rather than omitted silently. A missing block
            # means the run cannot build this item from the view alone, and the
            # run needs to see that where it will act on it — not only in a
            # lint warning nobody carried forward.
            out.append(
                "**No build block.** This item has not been given one at a "
                "keep-step, so the view carries no instructions for it. The run "
                "halts on it as underspecified rather than reading the queue for "
                "the missing detail."
            )
        else:
            out.extend(block)
        out.append("")

    # Every entry, by heading and slug alone. This is what lets a build tell
    # whether something it noticed is already filed, which was the one limb of
    # the capture-quality objection that landed. It restores duplicate
    # detection and nothing else: a heading says an item exists and says
    # nothing about what depends on it.
    out.append("## Everything in the queue, by name only")
    out.append("")
    out.append(
        "Headings and slugs, no reasoning. Enough to tell whether something is "
        "already filed before capturing it again — and not enough to tell what "
        "other work depends on it."
    )
    out.append("")
    for section in ("Processed", "Unprocessed"):
        in_section = [e for e in entries if e["section"] == section]
        out.append("**%s — %d entry(s)**" % (section, len(in_section)))
        out.append("")
        for e in in_section:
            state = ""
            if section == "Processed":
                state = "cleared" if e["cleared"] else "held"
                state = " (%s)" % state
            out.append("- [%s]%s %s"
                       % (e["slug"] or "NO-SLUG", state, without_slug(e["heading"])))
        out.append("")

    return out, problems


def main():
    args = sys.argv[1:]
    if not args:
        die("usage: generate_build_view.py <queue_path> [--out <path>]")
    queue_path = args[0]
    out_path = None
    rest = args[1:]
    while rest:
        if rest[0] == "--out":
            if len(rest) < 2:
                die("--out needs a path")
            out_path = rest[1]
            rest = rest[2:]
        else:
            die("unrecognised argument: %r" % rest[0])

    if not os.path.isfile(queue_path):
        die("no queue at %r" % queue_path)

    with open(queue_path, encoding="utf-8") as f:
        lines = f.readlines()

    entries = parse(lines)
    if not entries:
        die("no entries found in %r — is this a QUEUE.md?" % queue_path)

    body, problems = render(entries,
                            os.path.dirname(os.path.abspath(queue_path)))

    if out_path is None:
        out_path = os.path.join(os.path.dirname(os.path.abspath(queue_path)),
                                "BUILD-VIEW.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(body).rstrip("\n") + "\n")

    # Count only the flavors a run builds from a block. The two numbers are then
    # equal exactly when the migration is complete, which is what the epoch-4
    # completeness test reads them for; counting `[user]` and `[freeform]` items
    # among them made equal unreachable in any project holding one.
    needing = [e for e in entries if e["cleared"] and needs_block(e)]
    blocked = sum(1 for e in needing if build_block(e)[0] is not None)
    exempt = sum(1 for e in entries if e["cleared"] and not needs_block(e))
    summary = ("generate_build_view: wrote %s — %d block-needing cleared "
               "item(s), %d with a build block"
               % (out_path, len(needing), blocked))
    if exempt:
        summary += ("; %d cleared [user]/[freeform] item(s), which need none"
                    % exempt)
    print(summary + "; %d entry(s) listed by name" % len(entries))
    for p in problems:
        # A malformed block is reported and never repaired: the block is the
        # user-approved instruction set, and a script that tidies it is a script
        # that can change what the run builds.
        sys.stderr.write("generate_build_view: malformed block — %s\n" % p)


if __name__ == "__main__":
    main()
