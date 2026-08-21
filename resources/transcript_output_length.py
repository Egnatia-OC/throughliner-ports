#!/usr/bin/env python3
"""Measure how much Claude actually SAYS, per assistant message, from raw
session transcripts.

    py resources/transcript_output_length.py [project-slug-or-path] [--limit N]

WHAT THIS IS, AND WHEN IT GOES AWAY. A one-off instrument for
[brevity-amendment-outcome] — the audit that reads a before-and-after
measurement and says whether the brevity amendment moved anything. DELETE THIS
FILE once that audit has reported. It is wired into nothing: no close, no
session opening, no check, and no other script imports it. Nothing in the
repository calls it.

It prints a distribution and NO threshold, NO target and NO verdict. That is
deliberate and it is the whole discipline of the thing. A measurement with a
standard attached becomes a standard the moment a session reads its median as a
norm, which is the circularity SPEC records against the retired word bands. If
you find yourself wanting a band printed here, that is the failure this header
is warning about.

WHAT IT COUNTS. Assistant message TEXT only — what the user actually reads in
chat. `thinking` blocks and `tool_use` blocks are dropped, and `tool_result`
never appears on an assistant record at all. Content blocks belonging to one
message arrive as separate transcript lines sharing a message id, so they are
regrouped before counting: one row per message the user saw, not per block.

A message that emitted no text at all (pure tool calls) counts as zero words and
is reported separately, because a run's silent turns are a real part of its
shape and averaging them in would hide both halves.

WHY THE RAW FILE. `CLAUDE.md` records that asking Claude to summarise a session
is lossy and reads Claude-authored content as fact. These files are the
unedited record.

Standard library only.
"""

import argparse
import json
import os
import re
import sys

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding='utf-8', errors='replace')
    except (AttributeError, ValueError, OSError):
        # Python < 3.7, or a stream that cannot be reconfigured (redirected to
        # a pipe or replaced by a test harness). Messages then behave as before
        # — degraded, never fatal.
        pass

PROJECTS_DIR = os.path.join(os.path.expanduser("~"), ".claude", "projects")
COMMAND_RE = re.compile(r"<command-name>\s*(/[^<\s]+)\s*</command-name>")


def resolve_project(arg):
    """Accept a slug, a full path to a projects/ subfolder, or nothing."""
    if arg and os.path.isdir(arg):
        return arg
    if arg:
        candidate = os.path.join(PROJECTS_DIR, arg)
        if os.path.isdir(candidate):
            return candidate
        sys.exit(f"no such project transcript folder: {arg}")
    cwd = os.path.abspath(os.getcwd())
    # Claude Code's own slug: every character outside [A-Za-z0-9] becomes a
    # dash, so drive colons, separators and spaces all collapse the same way.
    slug = re.sub(r"[^A-Za-z0-9]", "-", cwd)
    candidate = os.path.join(PROJECTS_DIR, slug)
    if os.path.isdir(candidate):
        return candidate
    sys.exit(
        "could not derive this project's transcript folder from the working "
        f"directory.\nLooked for: {candidate}\n"
        "Pass the slug or path as the first argument."
    )


def words(text):
    return len(text.split())


def read_session(path):
    """Return (rows, skill_of_row) for one transcript file.

    A row is the total words of text in one assistant message. Blocks are
    regrouped by message id because the transcript writes one line per block.
    """
    by_id = {}
    order = []
    skill_at = {}
    current_skill = None
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("isSidechain"):
                # Subagent output. The user never reads it, so it is not what
                # this is measuring.
                continue
            kind = rec.get("type")
            msg = rec.get("message") or {}
            if kind == "user":
                content = msg.get("content")
                text = ""
                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    text = " ".join(
                        b.get("text", "") for b in content
                        if isinstance(b, dict) and b.get("type") == "text")
                found = COMMAND_RE.search(text)
                if found:
                    current_skill = found.group(1)
                continue
            if kind != "assistant":
                continue
            mid = msg.get("id") or rec.get("uuid")
            if mid not in by_id:
                by_id[mid] = 0
                order.append(mid)
                skill_at[mid] = current_skill
            content = msg.get("content")
            if not isinstance(content, list):
                continue
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    by_id[mid] += words(block.get("text", ""))
    return [(mid, by_id[mid], skill_at[mid]) for mid in order]


def percentile(sorted_values, fraction):
    if not sorted_values:
        return 0
    index = int(round(fraction * (len(sorted_values) - 1)))
    return sorted_values[index]


def describe(label, values):
    if not values:
        print(f"{label}: no messages")
        return
    ordered = sorted(values)
    total = sum(ordered)
    print(f"{label}")
    print(f"  messages          {len(ordered)}")
    print(f"  total words       {total}")
    print(f"  median            {percentile(ordered, 0.50)}")
    print(f"  25th / 75th       {percentile(ordered, 0.25)} / "
          f"{percentile(ordered, 0.75)}")
    print(f"  10th / 90th       {percentile(ordered, 0.10)} / "
          f"{percentile(ordered, 0.90)}")
    print(f"  min / max         {ordered[0]} / {ordered[-1]}")


def histogram(values):
    bands = [(0, 0), (1, 25), (26, 75), (76, 150), (151, 300),
             (301, 600), (601, 10 ** 9)]
    counts = [sum(1 for v in values if low <= v <= high) for low, high in bands]
    # Scale to the largest band rather than clipping at a fixed width, or every
    # band above the cap draws the same bar and the shape disappears.
    widest = max(counts) or 1
    print("\ndistribution (words per message)")
    for (low, high), count in zip(bands, counts):
        if high == 0:
            name = "0 (no text)"
        elif high >= 10 ** 9:
            name = f"{low}+"
        else:
            name = f"{low}-{high}"
        bar = "#" * round(60 * count / widest)
        print(f"  {name:>12}  {count:>5}  {bar}")


def main():
    parser = argparse.ArgumentParser(
        description="Report words per assistant message from raw transcripts. "
                    "Prints no threshold, target or verdict.")
    parser.add_argument("project", nargs="?", default=None,
                        help="transcript folder slug or path "
                             "(default: derived from the working directory)")
    parser.add_argument("--limit", type=int, default=0,
                        help="use only the N most recently modified sessions")
    args = parser.parse_args()

    folder = resolve_project(args.project)
    files = [os.path.join(folder, n) for n in os.listdir(folder)
             if n.endswith(".jsonl")]
    files.sort(key=os.path.getmtime, reverse=True)
    if args.limit:
        files = files[:args.limit]
    if not files:
        sys.exit(f"no .jsonl transcripts in {folder}")

    rows = []
    for path in files:
        rows.extend(read_session(path))

    all_values = [w for _, w, _ in rows]
    spoke = [w for w in all_values if w > 0]

    print(f"transcript folder   {folder}")
    print(f"sessions read       {len(files)}")
    print()
    describe("all assistant messages", all_values)
    print()
    describe("messages that said something (text > 0)", spoke)
    silent = len(all_values) - len(spoke)
    print(f"\nsilent messages (tool calls only)   {silent}")
    histogram(all_values)

    by_skill = {}
    for _, value, skill in rows:
        by_skill.setdefault(skill or "(no skill running)", []).append(value)
    print("\nby skill running at the time")
    for skill in sorted(by_skill, key=lambda k: -len(by_skill[k])):
        values = sorted(by_skill[skill])
        said = [v for v in values if v > 0]
        print(f"  {skill:<28} {len(values):>5} msgs   "
              f"median {percentile(values, 0.50):>5}   "
              f"median when speaking {percentile(sorted(said), 0.50) if said else 0:>5}")

    print("\nNo figure above is a limit, a target or a breach. "
          "This reports what was said and nothing else.")


if __name__ == "__main__":
    main()
