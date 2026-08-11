#!/usr/bin/env python3
"""Stop hook: catch a report that names a work item which isn't there.

The failure this exists for ([write-first-report-without-write]). Under the old
show-first rule the text appeared in chat before the write, so reporting and
showing were one act and a report could not precede its write. Under write-first
the report follows the write — which means a turn that never executes the write
can still emit the report, and the two are indistinguishable to the user. The
live instance: Claude said "Filed as [some-slug]" having made no write at all,
and the user acted on the false report before the item existed.

Sharper wording is a remedy already spent. The write-then-verify-then-point rule
is shipped, always-loaded and correctly worded, and it still failed live. So this
is a mechanism instead.

WHY THIS IS CHECKABLE AT ALL, and why no understanding of meaning is required.
The shipped rule already requires the report to name what landed and where, which
in practice is a fixed shape: "filed as [slug]", "moved to Processed as [slug]".
A slug either exists in QUEUE.md as a `#### ` heading or it does not. So a false
report is not a judgment about meaning — it is a named artifact that is absent.
This is the check-the-world rule the method already applies to `[user]` items,
turned on Claude's own claims.

WHY `Stop` AND NOT `PreToolUse`. `resources/research/hook-enforced-doc-reading.md`
establishes that PreToolUse can read the transcript and deny. That is the wrong
surface here: a false report is text with NO tool call attached, so a hook gated
on tool calls never fires on it. `Stop` fires when Claude finishes responding and
receives `last_assistant_message` — the complete final response text, handed over
directly, so no transcript parsing is needed. Returning
`{"decision": "block", "reason": "..."}` does not end the turn: it feeds the
reason back and the conversation continues, so the write can be made and the
correction can reach the user before they act on the false report.

THE LIMIT, STATED RATHER THAN DISCOVERED. This catches reports that NAME the
artifact. A vague report ("I've written that up") escapes it entirely. That is
acceptable rather than a hole: the shipped rule already requires the report to
name what landed, so the hook enforces the rule as written and no more.

LOOP PROTECTION. A `stop_hook_active`-style flag is not documented, so this
carries its own: it blocks once per identical claim and then downgrades to
non-blocking feedback. A persistent mismatch would otherwise bounce forever.
"""

import json
import os
import re
import sys

# Report-shaped claims that NAME a slug. Deliberately narrow — each requires a
# reporting verb near a bracketed slug, so ordinary prose mentioning an item
# ("as [some-slug] says") does not match.
CLAIM_PATTERNS = [
    # Queue-FILING verbs only. "logged", "recorded" and "wrote" are deliberately
    # absent: /done legitimately says it logged a slug that it then removed from
    # the queue, and a LOG entry is not a QUEUE heading — this check is
    # QUEUE-specific, so those verbs would fire on correct reports.
    re.compile(
        r"\b(filed|captured|appended|created)\b"
        r"[^.\n]{0,80}?\[([a-z0-9][a-z0-9-]*)\]",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(moved|promoted|kept|processed|lifted)\b"
        r"[^.\n]{0,80}?\[([a-z0-9][a-z0-9-]*)\]",
        re.IGNORECASE,
    ),
    re.compile(
        r"\[([a-z0-9][a-z0-9-]*)\][^.\n]{0,40}?\b"
        r"(is now in|has been filed|has been added|landed in)\b",
        re.IGNORECASE,
    ),
]

# Words that mean the sentence is talking ABOUT a slug rather than claiming it
# was just written. Cheap false-positive suppression.
NEGATION_NEAR = re.compile(
    r"\b(will|would|should|could|about to|going to|plan to|propose|"
    r"recommend|suggest|if |once |before |instead of|rather than|not )\b",
    re.IGNORECASE,
)


def _claimed_slugs(message):
    """Slugs the message claims to have just written. Possibly empty."""
    found = set()
    for pattern in CLAIM_PATTERNS:
        for match in pattern.finditer(message):
            groups = [g for g in match.groups() if g]
            # The slug is whichever group looks like a slug, not the verb.
            slug = None
            for group in groups:
                if re.fullmatch(r"[a-z0-9][a-z0-9-]*", group) and "-" in group:
                    slug = group
            if not slug:
                continue
            # Look at the sentence around the match for hedging language.
            start = max(0, match.start() - 60)
            window = message[start:match.end() + 20]
            if NEGATION_NEAR.search(window):
                continue
            found.add(slug)
    return found


def _slugs_in_queue(queue_path):
    """Every slug present in QUEUE.md as a real `#### ` heading."""
    try:
        with open(queue_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except (OSError, UnicodeDecodeError):
        return None
    slugs = set()
    for raw in lines:
        stripped = raw.strip()
        if not stripped.startswith("#### "):
            continue
        match = re.search(r"\[([a-z0-9][a-z0-9-]*)\]\s*$", stripped)
        if match:
            slugs.add(match.group(1))
    return slugs


def _already_blocked(cwd, session_id, slug):
    """True if this exact claim was blocked once already this session.

    The downgrade after one block is the loop protection. Marker files live in
    `.throughliner/`, which the project already gitignores. Never raises: if the
    marker cannot be written, the caller treats the claim as un-blocked, which
    fails toward blocking once rather than never.
    """
    if not session_id:
        return False
    safe_slug = re.sub(r"[^a-z0-9-]", "", slug)[:60]
    marker_dir = os.path.join(cwd, ".throughliner")
    marker = os.path.join(
        marker_dir, "stop-claim-%s-%s.marker" % (session_id[:40], safe_slug)
    )
    try:
        if os.path.exists(marker):
            return True
        os.makedirs(marker_dir, exist_ok=True)
        with open(marker, "w", encoding="utf-8") as f:
            f.write("blocked once\n")
    except OSError:
        return False
    return False


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    message = payload.get("last_assistant_message") or ""
    if not message:
        sys.exit(0)

    cwd = payload.get("cwd") or os.getcwd()
    session_id = payload.get("session_id") or ""
    queue_path = os.path.join(cwd, "QUEUE.md")

    # No QUEUE.md means this isn't a set-up project, or the file is unreadable.
    # Either way there is nothing to check against, and a hook that cannot tell
    # must not block.
    queue_slugs = _slugs_in_queue(queue_path)
    if queue_slugs is None:
        sys.exit(0)

    claimed = _claimed_slugs(message)
    if not claimed:
        # The overwhelming majority of turns. No work done.
        sys.exit(0)

    missing = sorted(slug for slug in claimed if slug not in queue_slugs)
    if not missing:
        sys.exit(0)

    names = ", ".join("[%s]" % slug for slug in missing)
    downgraded = all(_already_blocked(cwd, session_id, slug) for slug in missing)

    reason = (
        "Your last message reported writing %s, but %s not in QUEUE.md as a "
        "work-item heading. Either the write did not happen, or it landed "
        "somewhere else. Make the write now if it is missing, then tell the "
        "user plainly what actually happened — they may already be acting on "
        "the report. If the item genuinely lives elsewhere (an archived "
        "message, another project's queue, a LOG entry), say so in one line and "
        "carry on."
        % (names, "it is" if len(missing) == 1 else "they are")
    )

    if downgraded:
        # Second time on the same claim: feed it back without blocking, so a
        # genuine mismatch cannot bounce the turn forever.
        print(reason, file=sys.stderr)
        sys.exit(0)

    print(json.dumps({"decision": "block", "reason": reason}))
    sys.exit(0)


if __name__ == "__main__":
    main()
