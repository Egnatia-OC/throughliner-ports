#!/usr/bin/env python3
"""Mechanical QUEUE.md work-item reorder mover.

Why this exists: /plan's close-out reorder re-sorts the queue sections, but the
only editing primitive Claude has is exact-string replace — so moving a work
item means retyping its whole prose block verbatim, twice. Work items run to
several hundred words, so on a long queue the sort silently degrades to a
partial move, and a single transcription slip corrupts an item with no error.
This script moves whole work-item blocks byte-for-byte: Claude supplies only the
desired slug order, the script rewrites the section, and nothing passes through
Claude's hands.

Contract:
  python reorder_queue.py <queue_path> <section> <slug1> <slug2> ... [--marker-after <slug|TOP|BOTTOM>]
  python reorder_queue.py <queue_path> <section> --move <slug> <TOP|BOTTOM> [--marker-after ...]
  python reorder_queue.py <queue_path> <section> --move <slug> <BEFORE|AFTER> <anchor-slug> [--marker-after ...]
  python reorder_queue.py <queue_path> --move-section <slug> <FromSection> <ToSection> [--position <TOP|BOTTOM|BEFORE|AFTER> [anchor-slug]]

  <section>  one of: Processed | Unprocessed
  <slug...>  the FULL desired order of that section's work-item slugs, top to
             bottom. Every slug currently in the section must appear exactly
             once; no extra slugs. (The full-set check stays on this total form
             — it is what guarantees no item is silently lost in a reorder.)
  --move <slug> <TOP|BOTTOM>  single-item-move mode: relocate exactly one item
             to the top or bottom of its section, keeping every other item in
             its current relative order. The caller names only the one slug —
             the script derives the full order from the file — so a common move
             (e.g. /plan's skip-to-defer sending an item to the bottom of
             Unprocessed) needs no hand-typed slug list. The same byte-for-byte
             block preservation and self-checks apply. Mutually exclusive with a
             positional slug list.
  --move <slug> <BEFORE|AFTER> <anchor-slug>  relative form of the same move:
             place the item immediately before/after another item in the same
             section, all other items keeping their relative order. Exists so a
             two-item reorder never demands the section's full slug list.
  --move-section <slug> <From> <To>  cross-section move: relocate one item's
             whole block byte-for-byte from one section to the other — the
             Unprocessed → Processed keep-move is /plan's most frequent
             structural write, and without this it was hand-retyped. Default
             lands at the BOTTOM of the target section; --position overrides
             (TOP, BOTTOM, or BEFORE/AFTER an anchor slug in the target). The
             heading text is NOT rewritten — a processed item's new description
             is a separate deliberate edit, made after the mechanical move.
  --marker-after (Processed only): where the `--- Cleared to run above this
             line ---` marker lands — after the named slug, or TOP / BOTTOM of
             the section. Omit to keep the marker in its current relative spot
             (immediately after whichever slug it currently follows). Ignored
             with a warning if the section has no marker.

The ordering input is ephemeral by design — one rearrange, then discarded. It is
deliberately NOT a persistent queue index: a standing short-line index invites
reasoning from the compressed lines instead of the real work items, the exact
proxy-reasoning the method forbids.

Self-check (refuses to write on any failure, exits non-zero, changes nothing):
  - the multiset of slugs after == before (no item lost, added, or duplicated);
  - each slug's block content is byte-for-byte identical before and after;
  - the marker is present after iff it was present before;
  - everything outside the target section is untouched.
"""

import sys
import re

MARKER_RE = re.compile(r'^---\s*Cleared to run above this line\s*---\s*$')
SECTION_RE = re.compile(r'^##\s+(Processed|Unprocessed)\s*$')
ITEM_RE = re.compile(r'^####\s')
# Slug = the last [bracketed] token on the heading line (a leading [user]/[audit]
# flavor tag never collides — it isn't at end of line).
SLUG_RE = re.compile(r'\[([^\]]+)\]\s*$')


def die(msg):
    sys.stderr.write("reorder_queue: " + msg + "\n")
    sys.exit(1)


def heading_slug(line):
    m = SLUG_RE.search(line.rstrip())
    return m.group(1) if m else None


def parse(lines):
    """Return (before_lines, section_name->(start,end)) index of section body
    line ranges. A section body runs from the line after its `## Name` heading
    up to (not including) the next `## ` heading or EOF."""
    sections = {}
    heading_idx = {}
    for i, line in enumerate(lines):
        m = SECTION_RE.match(line)
        if m:
            heading_idx[m.group(1)] = i
    # compute body ranges
    all_h2 = [i for i, l in enumerate(lines) if l.startswith('## ')]
    for name, hi in heading_idx.items():
        nxt = min([h for h in all_h2 if h > hi], default=len(lines))
        sections[name] = (hi + 1, nxt)
    return sections


def split_blocks(body):
    """Split a section body (list of lines) into a leading preamble (non-item
    lines before the first ####), a list of item blocks, and the marker.

    Returns (preamble_lines, blocks, marker_after_slug_or_None, had_marker).
    Each block is (slug, list_of_lines) covering the #### heading through the
    lines up to the next #### / marker. The marker line and any blank lines
    around it are handled separately so item text stays byte-exact.
    """
    # find first item
    first = next((i for i, l in enumerate(body) if ITEM_RE.match(l)), None)
    if first is None:
        # No items at all: the marker (if any) is still somewhere in the body.
        kept = [l for l in body if not MARKER_RE.match(l)]
        return kept, [], None, len(kept) != len(body)
    # The marker can sit ABOVE every item, in which case it lands in the
    # preamble and the item-scanning loop below never sees it. Scan the
    # preamble for it explicitly and strip it, or the marker's text survives
    # in the preamble while had_marker stays False — reassembly then
    # contradicts itself and the self-check refuses to write.
    preamble = [l for l in body[:first] if not MARKER_RE.match(l)]
    marker_above_all = len(preamble) != first
    blocks = []
    marker_after = None
    had_marker = marker_above_all
    cur_slug = None
    cur = []
    prev_slug = None  # slug of the most-recently-completed block (marker anchor)

    def flush():
        nonlocal cur, cur_slug, prev_slug
        if cur_slug is not None:
            # Strip trailing blank lines — inter-block spacing is regenerated
            # canonically at reassembly, so a block stores only heading + body
            # (internal blank lines within the rationale are kept).
            block = cur[:]
            while block and block[-1].strip() == '':
                block.pop()
            blocks.append((cur_slug, block))
            prev_slug = cur_slug  # last completed item = what a following marker anchors to
        cur, cur_slug = [], None

    for line in body[first:]:
        if MARKER_RE.match(line):
            flush()
            had_marker = True
            marker_after = prev_slug  # None => marker at TOP (before all items)
            continue
        if ITEM_RE.match(line):
            flush()
            cur_slug = heading_slug(line)
            if cur_slug is None:
                die("work item heading has no [slug]: " + line.strip())
            cur = [line]
        else:
            cur.append(line)
    flush()
    return preamble, blocks, marker_after, had_marker


def assemble_section(preamble, elements):
    """Reassemble a section body: preamble, then every element (a block's lines,
    or the marker as its own element) separated by exactly one blank line.
    Returns the list of output lines, starting with the blank line that follows
    the `## Section` heading."""
    pre = list(preamble)
    while pre and pre[0].strip() == '':
        pre.pop(0)
    while pre and pre[-1].strip() == '':
        pre.pop()
    out = ['\n']            # blank line after the `## Section` heading
    if pre:
        out.extend(pre)
        out.append('\n')
    for el in elements:
        out.extend(el)
        out.append('\n')   # one blank line after each element
    return out


def elements_with_marker(new_blocks, had_marker, pref):
    """Order blocks and (if present) the marker into the element list."""
    marker_line = "--- Cleared to run above this line ---\n"
    elements = []
    if had_marker and pref == 'TOP':
        elements.append([marker_line])
    for s, blk in new_blocks:
        elements.append(blk)
        if had_marker and pref == s:
            elements.append([marker_line])
    if had_marker and pref == 'BOTTOM':
        elements.append([marker_line])
    return elements


def move_section(queue_path, slug, sec_from, sec_to, position, anchor):
    """Move one item's block byte-for-byte between sections.

    Same guarantees as a reorder: refuses to write on any failure, block
    content byte-identical, marker presence preserved per section, nothing
    outside the two sections changed.
    """
    for name in (sec_from, sec_to):
        if name not in ('Processed', 'Unprocessed'):
            die("section must be Processed or Unprocessed, got: " + name)
    if sec_from == sec_to:
        die("--move-section needs two different sections; use --move within one")

    with open(queue_path, 'r', encoding='utf-8', newline='') as f:
        lines = f.read().splitlines(keepends=True)
    sections = parse(lines)
    for name in (sec_from, sec_to):
        if name not in sections:
            die("section '%s' not found in %s" % (name, queue_path))

    f_start, f_end = sections[sec_from]
    t_start, t_end = sections[sec_to]
    f_pre, f_blocks, f_marker_after, f_had = split_blocks(lines[f_start:f_end])
    t_pre, t_blocks, t_marker_after, t_had = split_blocks(lines[t_start:t_end])

    f_slugs = [s for s, _ in f_blocks]
    if slug not in f_slugs:
        die("--move-section slug '%s' is not in section %s" % (slug, sec_from))
    if slug in [s for s, _ in t_blocks]:
        die("slug '%s' already exists in section %s" % (slug, sec_to))
    moved = dict(f_blocks)[slug]
    f_new = [(s, b) for s, b in f_blocks if s != slug]

    t_slugs = [s for s, _ in t_blocks]
    if position in ('BEFORE', 'AFTER'):
        if anchor is None:
            die("--position %s needs an anchor slug" % position)
        if anchor not in t_slugs:
            die("anchor slug '%s' is not in section %s" % (anchor, sec_to))
        idx = t_slugs.index(anchor) + (1 if position == 'AFTER' else 0)
    elif position == 'TOP':
        idx = 0
    else:  # BOTTOM (default)
        idx = len(t_blocks)
    t_new = t_blocks[:idx] + [(slug, moved)] + t_blocks[idx:]

    f_pref = 'TOP' if f_marker_after is None else f_marker_after
    t_pref = 'TOP' if t_marker_after is None else t_marker_after
    # The moved item must never silently land above the target's readiness
    # marker: if it was inserted before the marker anchor resolves, the marker
    # keeps its anchor slug, which is unaffected by an insertion.
    f_out = assemble_section(f_pre, elements_with_marker(f_new, f_had, f_pref))
    t_out = assemble_section(t_pre, elements_with_marker(t_new, t_had, t_pref))

    # Rebuild the file: replace both section bodies. Handle either order.
    if f_start < t_start:
        new_lines = (lines[:f_start] + f_out + lines[f_end:t_start] + t_out
                     + lines[t_end:])
    else:
        new_lines = (lines[:t_start] + t_out + lines[t_end:f_start] + f_out
                     + lines[f_end:])

    # ---- Self-checks ----
    new_text = ''.join(new_lines)
    if ''.join(moved) not in new_text:
        die("self-check failed: moved block for [%s] changed content" % slug)
    old_all = sorted(f_slugs + t_slugs)
    new_all = sorted([s for s, _ in f_new] + [s for s, _ in t_new])
    if old_all != new_all:
        die("self-check failed: slug set changed across the two sections")
    for had, out in ((f_had, f_out), (t_had, t_out)):
        if had != any(MARKER_RE.match(l) for l in out):
            die("self-check failed: marker presence changed in a section")

    with open(queue_path, 'w', encoding='utf-8', newline='') as f:
        f.write(new_text)
    sys.stderr.write("reorder_queue: moved [%s] %s -> %s (%s)\n"
                     % (slug, sec_from, sec_to, position or 'BOTTOM'))


def main():
    args = sys.argv[1:]
    marker_pref = None
    if '--marker-after' in args:
        k = args.index('--marker-after')
        try:
            marker_pref = args[k + 1]
        except IndexError:
            die("--marker-after needs a value (a slug, TOP, or BOTTOM)")
        args = args[:k] + args[k + 2:]

    if '--move-section' in args:
        k = args.index('--move-section')
        try:
            ms_slug, ms_from, ms_to = args[k + 1], args[k + 2], args[k + 3]
        except IndexError:
            die("--move-section needs three values: <slug> <FromSection> <ToSection>")
        rest = args[:k] + args[k + 4:]
        position, anchor = 'BOTTOM', None
        if '--position' in rest:
            p = rest.index('--position')
            try:
                position = rest[p + 1]
            except IndexError:
                die("--position needs a value: TOP, BOTTOM, BEFORE, or AFTER")
            if position in ('BEFORE', 'AFTER'):
                try:
                    anchor = rest[p + 2]
                except IndexError:
                    die("--position %s needs an anchor slug" % position)
                rest = rest[:p] + rest[p + 3:]
            elif position in ('TOP', 'BOTTOM'):
                rest = rest[:p] + rest[p + 2:]
            else:
                die("--position must be TOP, BOTTOM, BEFORE, or AFTER, got: " + position)
        if len(rest) != 1:
            die("usage: reorder_queue.py <queue_path> --move-section <slug> "
                "<FromSection> <ToSection> [--position <TOP|BOTTOM|BEFORE|AFTER> [anchor]]")
        move_section(rest[0], ms_slug, ms_from, ms_to, position, anchor)
        return

    move_slug = None
    move_pos = None
    move_anchor = None
    if '--move' in args:
        k = args.index('--move')
        try:
            move_slug = args[k + 1]
            move_pos = args[k + 2]
        except IndexError:
            die("--move needs values: <slug> <TOP|BOTTOM>, or <slug> <BEFORE|AFTER> <anchor-slug>")
        if move_pos in ('BEFORE', 'AFTER'):
            try:
                move_anchor = args[k + 3]
            except IndexError:
                die("--move %s needs an anchor slug" % move_pos)
            args = args[:k] + args[k + 4:]
        elif move_pos in ('TOP', 'BOTTOM'):
            args = args[:k] + args[k + 3:]
        else:
            die("--move position must be TOP, BOTTOM, BEFORE, or AFTER, got: " + move_pos)
    if len(args) < 2:
        # The usage message lists EVERY form the script supports. It used to
        # print only two of the four, and the reader who hit an error learned
        # the tool was less capable than it is — a real close restated a full
        # 23-slug order twice when two relative moves would have done it.
        die("usage: reorder_queue.py <queue_path> <section> <slug...> "
            "[--marker-after <slug|TOP|BOTTOM>]\n"
            "   or: reorder_queue.py <queue_path> <section> --move <slug> "
            "<TOP|BOTTOM> [--marker-after ...]\n"
            "   or: reorder_queue.py <queue_path> <section> --move <slug> "
            "<BEFORE|AFTER> <anchor-slug> [--marker-after ...]\n"
            "   or: reorder_queue.py <queue_path> --move-section <slug> "
            "<FromSection> <ToSection> [--position <TOP|BOTTOM|BEFORE|AFTER> "
            "[anchor-slug]]\n"
            "For one or two items out of place, a relative --move is the "
            "cheap form; the full slug list is only needed when the whole "
            "section genuinely re-sorts.")
    queue_path, section = args[0], args[1]
    desired = args[2:]  # empty in --move mode; derived from the file below
    if move_slug is not None and desired:
        die("--move takes no positional slug list (it derives the order from "
            "the file)")
    if move_slug is None and not desired:
        die("no order supplied: pass a full slug list or use --move")
    if section not in ('Processed', 'Unprocessed'):
        die("section must be Processed or Unprocessed, got: " + section)

    with open(queue_path, 'r', encoding='utf-8', newline='') as f:
        text = f.read()
    lines = text.splitlines(keepends=True)

    sections = parse(lines)
    if section not in sections:
        die("section '%s' not found in %s" % (section, queue_path))
    start, end = sections[section]
    body = lines[start:end]
    preamble, blocks, marker_after, had_marker = split_blocks(body)

    have = [s for s, _ in blocks]

    # In --move mode, derive the desired order from the file: keep every item in
    # its current relative order, with the named slug lifted to TOP or BOTTOM.
    if move_slug is not None:
        if move_slug not in have:
            die("--move slug '%s' is not in section %s" % (move_slug, section))
        rest = [s for s in have if s != move_slug]
        if move_pos == 'TOP':
            desired = [move_slug] + rest
        elif move_pos == 'BOTTOM':
            desired = rest + [move_slug]
        else:  # BEFORE / AFTER an anchor
            if move_anchor == move_slug:
                die("--move anchor cannot be the moved slug itself")
            if move_anchor not in rest:
                die("--move anchor slug '%s' is not in section %s"
                    % (move_anchor, section))
            idx = rest.index(move_anchor) + (1 if move_pos == 'AFTER' else 0)
            desired = rest[:idx] + [move_slug] + rest[idx:]

    if sorted(have) != sorted(desired):
        die("slug set mismatch.\n  in file: %s\n  supplied: %s"
            % (sorted(have), sorted(desired)))
    if len(desired) != len(set(desired)):
        die("duplicate slug in supplied order")

    by_slug = dict(blocks)
    new_blocks = [(s, by_slug[s]) for s in desired]

    # Resolve marker placement.
    marker_line = None
    if had_marker:
        marker_line = "--- Cleared to run above this line ---\n"
        pref = marker_pref if marker_pref is not None else (
            'TOP' if marker_after is None else marker_after)
        if pref not in ('TOP', 'BOTTOM') and pref not in desired:
            die("--marker-after slug '%s' is not in the section" % pref)
    elif marker_pref is not None:
        sys.stderr.write("reorder_queue: warning: section has no marker; "
                         "--marker-after ignored\n")

    # Build the ordered element list and reassemble with canonical spacing —
    # shared with --move-section via the two helpers.
    out = assemble_section(
        preamble,
        elements_with_marker(new_blocks, had_marker,
                             pref if had_marker else None))

    new_lines = lines[:start] + out + lines[end:]

    # ---- Self-checks: refuse to write on any failure ----
    out_text = ''.join(out)
    # 1. every block's content (heading + body, sans trailing blanks) preserved
    for s in desired:
        if ''.join(by_slug[s]) not in out_text:
            die("self-check failed: block for [%s] changed content" % s)
    # 2. marker presence preserved
    has_after = any(MARKER_RE.match(l) for l in out)
    if had_marker != has_after:
        die("self-check failed: marker presence changed")
    # 3. nothing outside the section changed
    if lines[:start] != new_lines[:start] or lines[end:] != new_lines[start + len(out):]:
        die("self-check failed: content outside the section changed")
    new_text = ''.join(new_lines)

    with open(queue_path, 'w', encoding='utf-8', newline='') as f:
        f.write(new_text)
    sys.stderr.write("reorder_queue: %s reordered (%d items)%s\n"
                     % (section, len(desired),
                        "" if not had_marker else ", marker placed"))


if __name__ == '__main__':
    main()
