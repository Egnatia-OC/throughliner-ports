#!/usr/bin/env python3
"""Measure how long this project's written shapes have grown over time.

Host-only dev artifact — not shipped in the plugin package.

Run:  py resources/measure_written_shape_length.py .
      py resources/measure_written_shape_length.py . --bands

Four shapes, each reported as a LENGTH AGAINST A DATE and nothing more:

    captures          word count of an item's block the first time it appears
                      in QUEUE.md at all, against the date it appeared
    work items        word count of the same item's block while it sits in
                      Processed, against date, and against its own first-filed
                      length — the growth an item accrues between capture and
                      being built
    LOG entries       word count per entry file, against the date in its name,
                      split by flavor (a planning session's entry versus a
                      build's) — preceded by the PRE-SPLIT BASELINE, every entry
                      in the combined `log.md` / `log-v*.md` files measured as
                      one undifferentiated group, since flavor was not recorded
                      in that era. That baseline is the era before the growth,
                      so without it the growth is only ever reported from
                      inside the period it happened in.
    LOG index lines   word count per index line, against date, beside the word
                      count of the entry that line points at — the inflation
                      path the user named: a longer index line implies a longer
                      entry

The default report invents no threshold and passes no judgment on any figure. It
prints a distribution, and no band may be read off the middle of it: this corpus
is the bloated one, so its typical length is not a target.

`--bands` is the separate mode, added once the bands existed. It reports the
project's current written shapes against the bands shipped in
`skill-nonspecific-rules.md`, which were derived from JULY's medians — the
measured record before the August doubling — and not from this corpus's middle.
The two modes must stay separate: a band printed inside the distribution report
would be a threshold read off the thing being questioned.

Method: the queue's own patch history is replayed from git, one blob per commit
that touched QUEUE.md, through a single `git cat-file --batch` rather than a
`git show` per commit. The LOG is read straight off disk, since entries are
immutable once written and their date is in the filename.
"""

import os
import re
import subprocess
import sys
from collections import defaultdict

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass

SLUG_RE = re.compile(r"\[([a-z0-9][a-z0-9-]*)\]\s*$")
ITEM_RE = re.compile(r"^####\s+\S")
# Matched as a whole line, never as a substring — an item's prose may quote the
# marker text, and a substring test would read that sentence as the readiness
# line. Same anchored predicate reorder_queue.py uses.
MARKER_RE = re.compile(r"^---\s*Cleared to run above this line\s*---\s*$")
LOG_ENTRY_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-([a-z0-9][a-z0-9-]*)\.md$")
INDEX_LINE_RE = re.compile(r"^-\s+(.*?)\s*(?:→|->)\s*([0-9a-z._-]+\.md)\s*$")


def words(text):
    return len(text.split())


# --- git ---------------------------------------------------------------------

def queue_history(root):
    """[(date, blob_text)] for every commit that touched QUEUE.md, oldest first."""
    try:
        log = subprocess.run(
            ["git", "log", "--reverse", "--format=%H|%as", "--", "QUEUE.md"],
            cwd=root, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            encoding="utf-8", errors="replace", timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    if log.returncode != 0 or not log.stdout.strip():
        return []

    commits = []
    for line in log.stdout.splitlines():
        if "|" in line:
            sha, date = line.split("|", 1)
            commits.append((sha.strip(), date.strip()))

    request = "".join(f"{sha}:QUEUE.md\n" for sha, _ in commits).encode("utf-8")
    try:
        batch = subprocess.run(
            ["git", "cat-file", "--batch"],
            cwd=root, input=request,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=180,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    if batch.returncode != 0:
        return []

    out, buf, i = [], batch.stdout, 0
    for _, date in commits:
        nl = buf.find(b"\n", i)
        if nl == -1:
            break
        header = buf[i:nl].decode("utf-8", "replace").split()
        i = nl + 1
        # "<oid> missing" — the file did not exist at that commit.
        if len(header) < 3:
            continue
        size = int(header[2])
        out.append((date, buf[i:i + size].decode("utf-8", "replace")))
        i += size + 1
    return out


# --- queue snapshots ----------------------------------------------------------

def items_in(text):
    """{slug: (section, cleared, word_count)} for one QUEUE.md snapshot."""
    found, section, cleared, slug, block = {}, None, True, None, []

    def flush():
        if slug:
            found[slug] = (section, cleared, words("\n".join(block)))

    for raw in text.splitlines():
        line = raw.strip()
        if re.match(r"^##\s+Processed\b", line, re.IGNORECASE):
            flush()
            section, cleared, slug, block = "Processed", True, None, []
            continue
        if re.match(r"^##\s+Unprocessed\b", line, re.IGNORECASE):
            flush()
            section, slug, block = "Unprocessed", None, []
            continue
        if MARKER_RE.match(line.strip()):
            cleared = False
            continue
        if ITEM_RE.match(line):
            flush()
            match = SLUG_RE.search(line)
            slug, block = (match.group(1) if match else None), []
            continue
        if slug:
            block.append(line)
    flush()
    return found


def queue_lengths(root):
    """(captures, growth) — first-filed lengths, and capture-to-Processed growth."""
    history = queue_history(root)
    captures, processed_now = {}, {}
    for date, text in history:
        for slug, (section, _cleared, count) in items_in(text).items():
            captures.setdefault(slug, (date, count, section))
            if section == "Processed":
                processed_now[slug] = count

    growth = []
    for slug, (date, first, _section) in captures.items():
        if slug in processed_now:
            growth.append((date, slug, first, processed_now[slug]))
    return captures, growth


# --- the LOG ------------------------------------------------------------------

def log_entries(root):
    """{filename: (date, flavor, word_count)} for every per-entry LOG file."""
    folder = os.path.join(root, "LOG")
    out = {}
    try:
        names = os.listdir(folder)
    except OSError:
        return out
    for name in names:
        match = LOG_ENTRY_RE.match(name)
        if not match:
            continue
        date, slug = match.group(1), match.group(2)
        try:
            with open(os.path.join(folder, name), "r", encoding="utf-8") as f:
                body = f.read()
        except OSError:
            continue
        # A planning session's entry is named for the session, not for a work
        # item, so the slug is where the flavor is legible without opening it.
        flavor = "plan" if slug == "plan" or slug.startswith("plan-") else "build"
        out[name] = (date, flavor, words(body))
    return out


# An entry heading in a pre-split combined log: `## <hash> — <title>`.
LEGACY_FILE_RE = re.compile(r"^log(-v[0-9][0-9a-z.]*)?\.md$")
LEGACY_HEADING_RE = re.compile(r"^##\s+\S")


def legacy_entries(root):
    """[(filename, title, word_count)] for every entry in the combined logs.

    Measured as ONE undifferentiated group, with no plan/build split. Flavor was
    not recorded in that era, and inferring it from a title's wording would be
    guesswork printed as measurement.
    """
    folder = os.path.join(root, "LOG")
    out = []
    try:
        names = sorted(os.listdir(folder))
    except OSError:
        return out
    for name in names:
        if not LEGACY_FILE_RE.match(name):
            continue
        try:
            with open(os.path.join(folder, name), "r", encoding="utf-8") as f:
                body = f.read()
        except OSError:
            continue
        title, block = None, []
        for raw in body.splitlines():
            if LEGACY_HEADING_RE.match(raw):
                if title is not None:
                    out.append((name, title, words("\n".join(block))))
                title, block = raw.lstrip("# ").strip(), []
                continue
            if title is not None:
                block.append(raw)
        if title is not None:
            out.append((name, title, words("\n".join(block))))
    return out


def index_lines(root, entries):
    """[(date, line_words, entry_words, filename)] for LOG/index.md."""
    path = os.path.join(root, "LOG", "index.md")
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError:
        return []
    out = []
    for raw in lines:
        match = INDEX_LINE_RE.match(raw.strip())
        if not match:
            continue
        name = match.group(2)
        entry = entries.get(name)
        if not entry:
            continue
        out.append((entry[0], words(match.group(1)), entry[2], name))
    return out


# --- reporting ----------------------------------------------------------------

def by_month(rows, value):
    """{YYYY-MM: [values]} — a month is a grouping, not a threshold."""
    buckets = defaultdict(list)
    for row in rows:
        buckets[row[0][:7]].append(value(row))
    return buckets


def describe(buckets):
    out = []
    for month in sorted(buckets):
        vals = sorted(buckets[month])
        n = len(vals)
        median = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) // 2
        out.append(
            f"| {month} | {n} | {min(vals)} | {median} | {sum(vals) // n} | {max(vals)} |"
        )
    return out


TABLE_HEAD = ["| month | n | min | median | mean | max |",
              "|---|---|---|---|---|---|"]


def report(root):
    lines = ["# Written-shape length growth", "",
             "**Measured**, by `resources/measure_written_shape_length.py`. "
             "Every figure is a word count against a date. No threshold is "
             "stated here and none may be read off the middle of these "
             "distributions — this is the corpus the measurement exists to "
             "question, so its typical length is not a target.", ""]

    captures, growth = queue_lengths(root)
    if not captures:
        lines += ["## Queue", "", "No git history for QUEUE.md — nothing measured.", ""]
    else:
        rows = [(date, count) for _slug, (date, count, _s) in captures.items()]
        history = queue_history(root)
        first_commit = history[0][0] if history else "?"
        earliest = min(r[0] for r in rows)
        lines += ["## Captures — length when first filed", "",
                  f"{len(rows)} items, first appearance in QUEUE.md.", ""]
        if earliest > first_commit:
            lines += [
                f"**Coverage limit.** QUEUE.md's history starts {first_commit}, "
                f"but the earliest item this reads is {earliest}. The queue used "
                "a different section structure before the two-section model, so "
                "snapshots older than that parse to no items and contribute "
                "nothing. Read the earliest month as the start of the "
                "measurable record, not the start of the project.", ""]
        lines += TABLE_HEAD + describe(by_month(rows, lambda r: r[1])) + [""]

        lines += ["## Work items — growth from first filing to Processed", "",
                  f"{len(growth)} items currently in Processed, each compared "
                  "against its own first-filed length. Grouped by the month it "
                  "was FIRST filed.", ""]
        lines += TABLE_HEAD[:1] + ["|---|---|---|---|---|---|"]
        lines += describe(by_month(growth, lambda r: r[3] - r[2]))
        lines += ["", "Per item, largest growth first:", ""]
        for date, slug, first, now in sorted(growth, key=lambda r: r[2] - r[3])[:15]:
            lines.append(f"- [{slug}] filed {date}: {first} -> {now} words")
        lines.append("")

    entries = log_entries(root)
    if not entries:
        lines += ["## LOG entries", "", "No per-entry LOG files found.", ""]
    else:
        rows = list(entries.values())
        split = min(r[0] for r in rows)
        legacy = legacy_entries(root)
        lines += ["## LOG entries — the pre-split baseline", ""]
        if not legacy:
            lines += ["No combined log files found under LOG/.", ""]
        else:
            counts = sorted(w for _f, _t, w in legacy)
            n = len(counts)
            median = (counts[n // 2] if n % 2
                      else (counts[n // 2 - 1] + counts[n // 2]) // 2)
            lines += [
                f"{n} entries in `LOG/log.md` and `LOG/log-v*.md`, the era before "
                f"entries became one file each (per-entry files start {split}). "
                "Measured as ONE group: flavor was not recorded then, and "
                "inferring it from a title would be guesswork printed as "
                "measurement. This is the baseline the later tables are read "
                "against.", "",
                "| group | n | min | median | mean | max |",
                "|---|---|---|---|---|---|",
                f"| pre-split | {n} | {counts[0]} | {median} | "
                f"{sum(counts) // n} | {counts[-1]} |", "",
                "Longest pre-split entries:", ""]
            for name, title, count in sorted(legacy, key=lambda r: -r[2])[:10]:
                head = title if len(title) <= 80 else title[:80].rstrip() + "…"
                lines.append(f"- {count} words ({name}): {head}")
            lines.append("")

        lines += ["## LOG entries — by flavor, per-entry era", "",
                  f"{len(rows)} entries, each its own file, from {split} onward.",
                  ""]
        for flavor in ("plan", "build"):
            subset = [r for r in rows if r[1] == flavor]
            if not subset:
                continue
            lines += [f"### {flavor} entries — {len(subset)}", ""]
            lines += TABLE_HEAD + describe(by_month(subset, lambda r: r[2])) + [""]

        idx = index_lines(root, entries)
        lines += ["## LOG index lines — line length, and the entry it points at", "",
                  f"{len(idx)} index lines resolved to an entry file.", ""]
        lines += TABLE_HEAD + describe(by_month(idx, lambda r: r[1])) + [""]
        lines += ["Longest index lines, with the entry each points at:", ""]
        for date, line_w, entry_w, name in sorted(idx, key=lambda r: -r[1])[:15]:
            lines.append(f"- {date}: index line {line_w} words -> entry {entry_w} words ({name})")
        lines.append("")

    return "\n".join(lines)


# --- bands --------------------------------------------------------------------

# Floor at half July's median, band top at July's median, ceiling at 1.5x.
# July is the measured record before the August doubling; the three multipliers
# are the one judgment. Canonical statement: docs-b/skill-nonspecific-rules.md.
BANDS = {
    "capture":     (90, 177, 265, "file the reasoning as research, cite it"),
    "work item":   (115, 229, 345, "split into two items"),
    "build entry": (115, 229, 345, "split per item built"),
    "plan entry":  (160, 323, 485, "split per decision"),
    "index line":  (20, 40, 60, "the line is restating its entry"),
}


def band_status(count, shape):
    floor, top, ceiling, _action = BANDS[shape]
    if count > ceiling:
        return "OVER CEILING"
    if count > top:
        return "over band"
    if count < floor:
        return "under band"
    return "in band"


def current_shapes(root):
    """{shape: [(name, word_count)]} for the project as it stands today."""
    out = {shape: [] for shape in BANDS}

    try:
        with open(os.path.join(root, "QUEUE.md"), "r", encoding="utf-8") as f:
            queue = f.read()
    except OSError:
        queue = ""
    for slug, (section, _cleared, count) in items_in(queue).items():
        if section == "Unprocessed":
            out["capture"].append((slug, count))
        elif section == "Processed":
            out["work item"].append((slug, count))

    entries = log_entries(root)
    for name, (_date, flavor, count) in entries.items():
        out["plan entry" if flavor == "plan" else "build entry"].append((name, count))

    for _date, line_w, _entry_w, name in index_lines(root, entries):
        out["index line"].append((name, line_w))

    return out


def bands_report(root):
    lines = ["# Written shapes against their bands", "",
             "**Bands are the ones shipped in `docs-b/skill-nonspecific-rules.md`**, "
             "derived from July's medians. This reports the project as it stands "
             "today. Advisory: a breach names an action, it blocks nothing.", ""]

    shapes = current_shapes(root)
    for shape in ("capture", "work item", "build entry", "plan entry", "index line"):
        floor, top, ceiling, action = BANDS[shape]
        rows = sorted(shapes[shape], key=lambda r: -r[1])
        lines += [f"## {shape} — band {floor}-{top}, ceiling {ceiling}", "",
                  f"On breach: {action}.", ""]
        if not rows:
            lines += ["Nothing found.", ""]
            continue
        counts = [c for _n, c in rows]
        counts_sorted = sorted(counts)
        n = len(counts_sorted)
        median = (counts_sorted[n // 2] if n % 2
                  else (counts_sorted[n // 2 - 1] + counts_sorted[n // 2]) // 2)
        over = [r for r in rows if r[1] > ceiling]
        above = [r for r in rows if top < r[1] <= ceiling]
        lines += [f"{n} measured, median {median}. "
                  f"{len(over)} over ceiling, {len(above)} over band.", ""]
        for name, count in rows:
            status = band_status(count, shape)
            if status in ("in band", "under band"):
                continue
            lines.append(f"- {status}: {count} words — {name}")
        lines.append("")

    return "\n".join(lines)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    root = os.path.abspath(args[0] if args else ".")
    if not os.path.isfile(os.path.join(root, "QUEUE.md")):
        print(f"measure_written_shape_length: no QUEUE.md under {root}", file=sys.stderr)
        return 1
    print(bands_report(root) if "--bands" in flags else report(root))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
