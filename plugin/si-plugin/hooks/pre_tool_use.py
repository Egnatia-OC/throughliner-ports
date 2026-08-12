#!/usr/bin/env python3
"""
PreToolUse hook — enforces three rules:

4. With NO build running (a planning or freeform session), a write outside
   the quiet list — QUEUE.md, SPEC.md, LOG/, the session's own notes — asks
   the user first. Ask, never deny. An unscoped build (a working file with
   no Files: section) is surfaced once for the same reason.

1. During a build, the session's own build working file
   (_build-<session-id>.md) has a Files: section governing which files are
   editable (method docs — QUEUE.md, LOG/, that working file — plus the user's
   memory dir, resources/research/, the session scratchpad dir, and any
   project's INBOX/ are always editable). Tri-state:
   no Files: section = no enforcement;
   section present but empty = method docs only; entries listed = only
   those files. SPEC.md is not a method doc, so a build can edit it only
   when it's explicitly listed in Files: — a batch that needs to change
   SPEC lists it; a feature build that doesn't name SPEC can't touch it,
   so scope-lock alone keeps SPEC read-only for any build that doesn't
   name it.
2. Git safety: block git reset --hard, git push --force, blanket
   staging (git add -A / --all / .), and git commit -a / -am.
3. Subagent cost ask-gate: the Task tool (spawning a subagent) returns
   permissionDecision "ask" — never "deny" — so the user is always
   prompted before a subagent runs, but keeps full choice. A subagent
   burns tokens fast and a single run can exhaust the user's usage, so
   the spawn must never be silent. Fires wherever the plugin is
   installed, independent of project adoption.

For Task: checks rule 3 (cost ask-gate).
For Edit/Write/MultiEdit: checks rule 1, and publishes the editing-state
signal (see write_editing_marker) — not a rule, a side effect that can
never block or fail a tool call.
For Bash/PowerShell: checks rule 2 (git safety) only.
"""

import json
import os
import re
import sys


# --- Git safety patterns ---

RESET_HARD = re.compile(r"\bgit\b.*\breset\b.*--hard\b")
# PUSH_FORCE is anchored to `git push` as the actual subcommand (git then
# whitespace then push), not `push` appearing anywhere after git. Without the
# anchor, `\bgit\b.*\bpush\b` let an unrelated `push` token satisfy the rule —
# e.g. a staged filename like `rezip-push-cli-flow.md`, where `\bpush\b` matches
# `-push-`. Combined with per-segment scanning (see _split_segments), this stops
# a `push`-bearing filename in one part of a compound command from pairing with
# a `-f` (e.g. an `rm -f`) elsewhere to trigger a false denial.
PUSH_FORCE = re.compile(r"\bgit\s+push\b.*(?:--force(?!-with-lease)\b|-f\b)")
# Blanket-add boundaries: a bare "." token only (explicit paths like
# ./scripts/x.py or .gitignore must pass), -A/--all as standalone flags.
BLANKET_ADD = re.compile(r'\bgit\b.*\badd\b.*(?:\s-A\b|\s--all\b|\s\.(?=\s|$|[;&|"\')]))')
# Commit boundaries: --amend and --allow-empty must not match -a / --all.
COMMIT_ALL = re.compile(r"\bgit\b.*\bcommit\b.*\s(?:-a\b|-am\b|--all\b)")

# Shell control operators that separate independent command segments. The
# git-safety patterns are applied to each segment alone (see _split_segments),
# so tokens from unrelated segments can't combine across an `&&` / `;` / `|`.
# Order in the alternation matters: the two-char operators (`&&`, `||`) come
# before the single-char ones so `&&` isn't split as two empty `&` halves.
SEGMENT_SPLIT = re.compile(r"&&|\|\||[;|\n]")

# Appended to every git-safety denial: the patterns match command text,
# not intent, so a denial can fire on a command that only carries the
# pattern as data.
# --- Structured shell writes ---
#
# A scripted write to a project file bypasses the editing tools entirely. It
# has happened repeatedly here — a heredoc'd Python splice used to remove work
# items from QUEUE.md because the edit looked too awkward to do by hand.
#
# So this catches the STRUCTURED forms only — a write whose target path is
# literally present and extractable. General shell parsing was considered and
# rejected: it is fragile, and false denials train workarounds, which is the
# worse failure. Anything that does not parse cleanly PASSES, and that limit is
# stated in the denial text rather than hidden.
#
# Matched: a Python invocation (heredoc or -c) containing a write-mode open() or
# a pathlib write_text/write_bytes.
#
# A LITERAL path is checked against the protected set and denied if it lands
# inside the project. A COMPUTED path — a variable, an f-string, a concatenation
# — used to fail open, and that fail-open was the whole cost of a real
# corruption: `python -c` with `p='QUEUE.md'` assigned one line earlier slipped
# straight past, matched a structural marker against the wrong occurrence, and
# wrote a QUEUE.md with six work items still in it. A later heredoc against the
# same file, this time with the path written out, was blocked correctly. One
# variable assignment was the entire difference. The same slip then recurred in
# the very session that diagnosed it, which is the strongest evidence available
# that knowing about a gap does not close it.
#
# So a computed target now DENIES rather than passing. The reasoning is that the
# guard cannot tell whether an unreadable target is protected, and "cannot tell"
# must not resolve to "allow" for a check whose whole job is preventing a
# silent clobber. It does not guess at the path — it says plainly that the
# target is unreadable and names the two ways forward.
#
# Accepted cost, stated rather than discovered: a python script writing to the
# session scratchpad with a computed path is denied too, and must write its path
# out literally. That is a small, visible tax; the alternative was a silent hole.
#
# Invoking a SCRIPT FILE is unaffected — this check reads the command's text,
# and `python scripts/reorder_queue.py QUEUE.md ...` contains no write call at
# all. The mover stays the sanctioned route for awkward queue edits.
PY_INVOCATION = re.compile(r"\bpython[0-9.]*\b|\bpy\s+-[0-9]")
PY_OPEN_WRITE = re.compile(
    r"""\bopen\s*\(\s*(?P<q>['"])(?P<path>[^'"]+)(?P=q)\s*,\s*['"][waxr]*[wax]b?\+?['"]"""
)
PY_PATH_WRITE = re.compile(
    r"""\bPath\s*\(\s*(?P<q>['"])(?P<path>[^'"]+)(?P=q)\s*\)\s*\.\s*write_(?:text|bytes)\s*\("""
)

# The same two shapes with the path left unconstrained. Used only to spot a
# write call the literal patterns above could not read a path out of.
PY_OPEN_WRITE_ANY = re.compile(
    r"""\bopen\s*\(\s*(?P<arg>[^,()]+?)\s*,\s*['"][waxr]*[wax]b?\+?['"]"""
)
PY_WRITE_METHOD_ANY = re.compile(r"""\.\s*write_(?:text|bytes)\s*\(""")

PATTERN_AS_DATA_NOTE = (
    "\n\nNote: this check matches the command's text, not its intent — a "
    "command that merely contains the pattern as data (a test string, "
    "quoting, documentation) is denied too. Assemble such strings at "
    "runtime instead of writing the pattern out literally."
)


# --- Helpers ---

def _deny(reason: str) -> int:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def _ask(reason: str) -> int:
    """Surface a permission prompt the user approves or declines.

    Unlike _deny, "ask" does not block — it hands the decision to the user
    with the reason shown. Used by the subagent cost gate so a subagent
    spawn is never silent, while the user keeps full choice.
    """
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def _split_segments(command: str) -> list[str]:
    """Split a compound command into independent segments on shell control
    operators (`&&`, `||`, `;`, `|`, newlines).

    The git-safety patterns are matched per segment so a token in one segment
    can't pair with a token in another to satisfy a pattern — the cross-segment
    false-denial bug (a `push`-bearing filename in a `git add` segment combining
    with an `rm -f` segment to trigger PUSH_FORCE). Splitting is deliberately
    naive about quoting and escaping: an operator inside a quoted string would
    over-split, but over-splitting only ever narrows what each pattern sees, so
    it can cause a missed denial in a contrived case, never a new false one —
    the fail-safe direction for a guard whose job is removing false denials.
    """
    return SEGMENT_SPLIT.split(command)


def _parse_build_files(build_path: str) -> list[str] | None:
    """Extract file paths from the build working file's Files: section.

    Returns None when no Files: section exists (no enforcement),
    an empty list when a section exists but lists nothing
    (method docs only), or the listed paths.

    Robust to a stray, content-bearing `Files: a, b, c` line — e.g. one
    copied into the Entry field from a batch's own text. Such a line used
    to shadow the real section: the parser latched onto the FIRST line
    starting with `Files:`, found no bare-path bullets beneath it, broke at
    the next prose line, and returned an empty list — which locked the build
    out of its own files (method docs only). Two changes fix that, and the
    pair is the fail-safe choice (a malformed file can never silently turn
    the lock off):

      - EVERY `Files:` line contributes; the scan never stops at the first.
        A non-bullet line ends only the current bullet run, not the whole
        scan, so a structured `Files:` section further down is still read.
      - A content-bearing `Files: a, b, c` line is not ignored — its
        comma-separated paths after the colon are taken directly. So even
        when an inline line is the ONLY `Files:` present, it yields a
        non-empty list (lock on, scoped) rather than None (lock off).

    A bare `Files:` header (nothing after the colon) opens a bullet section
    whose `- path` bullets are collected. found_section is set by any
    `Files:` line, so the None (no-enforcement) return is reserved for a
    file carrying no `Files:` line at all. Over-collecting is safe: an extra
    path only widens the allow-list to a file the build named anyway, never
    grants access to an unrelated file.
    """
    files = []
    try:
        with open(build_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return None

    in_bullets = False
    found_section = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("files:"):
            found_section = True
            inline = stripped[len("files:"):].strip()
            if inline:
                # Content-bearing line: take the comma-separated paths after
                # the colon. It does not open a bullet section — any bullets
                # that follow belong to a later bare `Files:` header.
                in_bullets = False
                for part in inline.split(","):
                    entry = part.strip()
                    if entry:
                        files.append(entry)
            else:
                # Bare header: the bullets beneath it are the paths.
                in_bullets = True
            continue
        if in_bullets:
            if stripped.startswith("- "):
                # Entries are taken whole after the leading "- " marker.
                # No annotation stripping: a Files: line is a bare path,
                # nothing else, so any trailing text becomes part of the
                # path and breaks the match — which is what the denial
                # message teaches. A genuine path containing " - " is no
                # longer truncated.
                file_entry = stripped[2:].strip()
                if file_entry:
                    files.append(file_entry)
            elif stripped and not stripped.startswith("-"):
                # End of this bullet run — but keep scanning: a later
                # `Files:` header (the real structured section) may follow.
                in_bullets = False
    if not found_section:
        return None
    return files


def _normalise(path: str) -> str:
    """Normalise a path for comparison."""
    return os.path.normcase(os.path.normpath(path))


def _is_inside(filepath: str, cwd: str) -> bool:
    """Check if a path sits inside the project folder.

    Used by the structured-shell-write check, which denies a scripted write to
    any project file rather than consulting the build's Files list. Paths
    outside the project are somebody else's business and pass.
    """
    norm = _normalise(filepath)
    root = _normalise(cwd)
    return norm == root or norm.startswith(root + os.sep)


def structured_write_targets(command: str) -> list:
    """Literal file paths a structured shell write names as its target.

    Deliberately narrow. Returns paths only where the command is recognisably a
    Python invocation AND the write call carries a literal quoted path. Anything
    else returns nothing and the command passes — a form that does not parse
    cleanly is never guessed at.
    """
    if not PY_INVOCATION.search(command):
        return []
    targets = []
    for pattern in (PY_OPEN_WRITE, PY_PATH_WRITE):
        for m in pattern.finditer(command):
            path = m.group("path").strip()
            # A path carrying substitution syntax is computed, not literal —
            # the ambiguity case, so it is dropped rather than resolved.
            if path and "$" not in path and "{" not in path:
                targets.append(path)
    return targets


def has_computed_write_target(command: str) -> bool:
    """True if a Python invocation writes to a path this check cannot read.

    The counterpart to structured_write_targets(): that function returns the
    targets it CAN read, this one reports that a write call exists whose target
    it CANNOT. A caller denies on either — one because the target is protected,
    the other because whether it is protected is unknowable.

    Deliberately does not attempt to resolve the path. Guessing at a variable's
    value is the fragile general-parsing this module rejects; refusing to guess
    and saying so is not.
    """
    if not PY_INVOCATION.search(command):
        return False

    for m in PY_OPEN_WRITE_ANY.finditer(command):
        arg = m.group("arg").strip()
        quoted = len(arg) >= 2 and arg[0] in "'\"" and arg[-1] == arg[0]
        if not quoted:
            return True
        # A quoted string carrying shell or format substitution is computed
        # too — the literal extractor drops these for the same reason.
        if "$" in arg or "{" in arg:
            return True

    # Every literal Path("...").write_text( is also a .write_text( , so an
    # excess of the general shape means at least one call on a receiver whose
    # path could not be read.
    if len(PY_WRITE_METHOD_ANY.findall(command)) > len(
        PY_PATH_WRITE.findall(command)
    ):
        return True

    return False


def safe_session_id(session_id: str) -> str:
    """A session id reduced to filename-safe characters.

    Identical to the editing marker's sanitiser, deliberately: the working
    files and the marker are the same kind of per-session artifact, and a
    second convention for the same job is how two things that must agree
    drift apart.
    """
    return re.sub(r"[^A-Za-z0-9._-]", "_", session_id or "unknown")


def working_file(cwd: str, kind: str, session_id: str) -> str:
    """This session's build or plan working file.

    Working files are per SESSION, not per project. They used to sit at
    `_build.md` and `_plan.md` in the project root, which made every check
    that keys on their existence ask "is there a build?" when it meant "is
    there a build FOR THIS SESSION?". The behaviour rules explicitly permit a
    planning session in one chat alongside a build in another, so a planning
    session would find `_build.md` present, conclude it was inside a build,
    and have the build's file list applied to writes it never agreed to.

    The name follows the editing marker's `<name>-<safe id>` shape rather
    than a per-session directory, and stays in the project root because that
    is where the docs and the FAQ already tell users to look.
    """
    return os.path.join(cwd, f"_{kind}-{safe_session_id(session_id)}.md")


def _is_method_doc(filepath: str, cwd: str, session_id: str = "") -> bool:
    """Check if a path is a method doc (QUEUE.md, LOG/, this session's working files)."""
    norm = _normalise(filepath)

    if norm == _normalise(os.path.join(cwd, "QUEUE.md")):
        return True

    for kind in ("build", "plan"):
        if norm == _normalise(working_file(cwd, kind, session_id)):
            return True

    log_dir = _normalise(os.path.join(cwd, "LOG"))
    if norm.startswith(log_dir + os.sep) or norm == log_dir:
        return True

    return False


def _is_memory_dir(filepath: str) -> bool:
    """Check if a path is under the user's Claude memory directory.

    Claude's memory lives at a path shaped like `.../.claude/.../memory/...`
    — a `memory` directory somewhere beneath a `.claude` directory. Matched
    by path shape, never a hardcoded machine path, so it holds for every
    consumer regardless of where their home or project lives. Memory writes
    (user preferences, working style, communication feedback) are allowed at
    any time per the memory-boundary rules, so the scope-lock must not block
    them — this exemption mirrors the method-docs one.
    """
    norm = _normalise(filepath)
    parts = norm.split(os.sep)
    if ".claude" not in parts:
        return False
    claude_idx = parts.index(".claude")
    return "memory" in parts[claude_idx + 1:]


def _is_research_dir(filepath: str, cwd: str) -> bool:
    """Check if a path is under the project's resources/research/ folder.

    Research notes are filed under resources/research/<topic>.md the moment a
    finding is produced (skill-nonspecific-rules.md Research > Filing), and that
    filing is open to every session type — build, test, or audit. The
    scope-lock must not block it, so this folder is always editable, mirroring
    the method-docs and memory exemptions. Matched relative to the project
    root, so it holds wherever the project lives.
    """
    norm = _normalise(filepath)
    research_dir = _normalise(os.path.join(cwd, "resources", "research"))
    return norm.startswith(research_dir + os.sep) or norm == research_dir


def _is_retired_terms_file(filepath: str, cwd: str) -> bool:
    """Check if a path is the project's resources/retired-terms.md.

    Exempt for a structural reason, not a convenient one. The method requires a
    session that retires a term to append it to this file. Retirement is
    discovered DURING a build — you find out a term is retired by retiring it —
    so it can never appear in a `Files:` list that /next computed from the work
    items before the build started. No amount of better self-scoping can fix
    that; the write is unschedulable by construction.

    Without this, the obligation was satisfiable only in a narrow undocumented
    window: denied during the build and anywhere in the close before the
    working file is deleted, and working only after, by accident of ordering.
    A session that hit the denial mid-close was told to ask the user to widen
    scope, which is a bad trade for a bookkeeping append.

    Two alternatives were weighed and lost. Stating the ordering in done.md
    works but leaves a trap for anyone who reorders the close, and the ordering
    that currently works is an accident rather than a design. Having /next
    widen `Files:` whenever a run touches rule-bearing files is more machinery
    than the problem deserves, and it guesses.

    This ships to consumers, who will never have the file. Accepted knowingly:
    a host-only branch inside a shipped hook costs more than an inert path
    check. Matched relative to the project root, like the research exemption.

    Note what is deliberately NOT swept in. SPEC.md is also outside the exempt
    set, and correctly so — a build may edit SPEC only by naming it in
    `Files:`, which is the whole point of the SPEC gate. It is not a second
    instance of this problem.
    """
    return _normalise(filepath) == _normalise(
        os.path.join(cwd, "resources", "retired-terms.md"))


def _is_inbox_dir(filepath: str) -> bool:
    """Check if a path is inside any project's INBOX folder.

    Two directions, and both must pass the scope-lock. Inbound: this project's
    own `INBOX/`, where an arriving message is archived after being triaged.
    Outbound: another project's `INBOX/`, which is where a message is delivered
    — that path sits outside this project entirely, so no cwd-relative check
    could recognise it. Matching on an `INBOX` path segment covers both.

    The scope-lock is not what protects the user here. Every outbound message
    is shown and approved before it is written (skill-nonspecific-rules.md, the
    cross-project INBOX channel) — a message leaving this project is an
    outward-facing action, and the user's approval is the backstop, exactly as
    it is for a feedback report.
    """
    norm = _normalise(filepath)
    parts = norm.replace("/", os.sep).split(os.sep)
    return _normalise("INBOX") in parts


def _is_scratchpad_dir(filepath: str, cwd: str) -> bool:
    """Check if a path is under the session's scratchpad directory.

    The harness gives each session a scratchpad directory OUTSIDE the repo,
    shaped like `<temp>/claude/<project-slug>/<session-id>/scratchpad/...` —
    a `scratchpad` directory sitting beneath a `claude` temp directory.
    skill-nonspecific-rules.md's Temporary-files rule actively instructs Claude to
    route scratch scripts and working files there, so the scope-lock must not
    block those writes — this exemption mirrors the method-docs, memory, and
    research exemptions.

    Matched tightly by path SHAPE, never a hardcoded machine path, so it holds
    for every consumer wherever their temp dir lives. Three conditions must all
    hold, keeping the whitelist scoped to the actual scratchpad and nowhere
    else: (1) a `scratchpad` path segment; (2) a `claude` segment somewhere
    above it (the harness scratchpad always sits under a `claude` temp dir);
    and (3) the path is OUTSIDE the project repo — scratch is never in-tree, so
    an in-repo `scratchpad/` folder stays under the normal scope-lock. Requiring
    all three keeps the scope-lock's containment value everywhere else.
    """
    norm = _normalise(filepath)
    parts = norm.split(os.sep)
    if "scratchpad" not in parts:
        return False
    sp_idx = parts.index("scratchpad")
    if "claude" not in parts[:sp_idx]:
        return False
    cwd_norm = _normalise(cwd)
    if norm == cwd_norm or norm.startswith(cwd_norm + os.sep):
        return False
    return True


def write_editing_marker(cwd: str, session_id: str, filepath: str, active: bool) -> None:
    """Publish the editing-state signal a companion app reads. Never raises.

    A live Markdown reader/editor open on the same file as Claude needs to know
    when Claude is writing, so the two don't land on each other mid-sentence.
    Inferring that from file-modification times was rejected: a watcher can see
    THAT a file changed but not WHO changed it, and can never tell "finished"
    from "paused to think" — and a wrong guess locks the user out of their own
    document.

    So this is a HEARTBEAT, not a lock. The marker always carries a fresh
    timestamp, and a reader treats a stale marker as "not editing" whatever the
    flag says. That staleness rule is the safety property: a session that
    crashes between starting a write and finishing one leaves a flag stuck on,
    and without staleness the reader would lock the user out permanently —
    reintroducing the exact harm the timing-guess approach was rejected for.

    One file PER SESSION, `editing-<session-id>.json`, because two Claude
    sessions in one project is a supported shape. With a single shared file,
    session A finishing a write would clear the flag while session B was still
    writing. Per-session files make the reader's rule trivially correct:
    editing is happening if ANY file here is active and fresh.

    Errors are swallowed in full: a companion-app convenience must never be able
    to block or fail the user's actual work.
    """
    try:
        import datetime

        marker_dir = os.path.join(cwd, ".throughliner")
        os.makedirs(marker_dir, exist_ok=True)
        safe_id = re.sub(r"[^A-Za-z0-9._-]", "_", session_id or "unknown")
        # Project-relative path, forward slashes, no leading "./" — version 2's
        # contract. Relative paths carry no account name (the privacy reason
        # this changed: the folder syncs, and gitignore never stopped that) and
        # resolve correctly against a synced copy on another machine. A file
        # outside the project falls back to its absolute path — a marker must
        # never lie about which file is being edited.
        if filepath:
            rel = os.path.relpath(os.path.abspath(filepath), cwd)
            marker_path = (
                os.path.abspath(filepath)
                if rel.startswith("..")
                else rel.replace(os.sep, "/")
            )
            files = [marker_path]
        else:
            files = []
        payload = {
            # `version` leads and is non-negotiable: another application is
            # built against this contract, so it must be able to recognise a
            # format it doesn't understand and fall back safely. A reader that
            # cannot parse this field defaults to 1, so version 2's
            # project-relative paths MUST NOT ship under a version-1 stamp —
            # they would resolve against the wrong root and hold nothing,
            # silently. Bumped to 2 when `files` went project-relative.
            "version": 2,
            # Must be a real boolean. A reader skips the marker entirely if
            # this is absent, the string "true", or 1.
            "active": bool(active),
            # Named for what it is safe to use it for: diagnosis. Freshness
            # comes from the marker file's own local mtime, never this field —
            # a synced marker carries another machine's clock, and comparing
            # that against the local clock fails closed (a dead session looks
            # permanently current). The old name `updated` invited exactly
            # that comparison. Nothing reads this field.
            "written_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            # Must be a list. Absent or non-list reads as empty.
            "files": files,
            # A format constant naming what wrote the marker, deliberately the
            # format's own name rather than the plugin slug so a product
            # rename never breaks a published value. `pid` and `session` were
            # dropped at version 2: written by these hooks, read by nothing —
            # pid is unusable across machines and redundant on one, session
            # restates the filename.
            "producer": "throughliner",
        }
        with open(
            os.path.join(marker_dir, f"editing-{safe_id}.json"), "w", encoding="utf-8"
        ) as f:
            json.dump(payload, f)
    except Exception:
        return


def _is_plan_quiet_path(filepath: str, cwd: str) -> bool:
    """True for the files a session with no build working file writes by design.

    The quiet list is the planning session's own working surface: QUEUE.md,
    SPEC.md, LOG/, and the session's own planning notes. Writing to these is what
    a planning session IS, so asking about them would be pure noise on every
    write. Everything else gets an ask — never a denial.

    Ask-never-deny is load-bearing and must not be "improved" into a denial. In a
    build there is a file list agreed in advance, so a surprise write means drift
    and denying is right. Here there is no agreed list, the user is present, and a
    legitimate write is authorised in one word. The gate's job is visibility, not
    containment: it doesn't stop you doing something urgent, it stops you doing it
    unremarked.

    Keyed on the build working file being absent rather than on "a planning
    session", because absence is what the code can actually see — and that is also
    what makes the gate cover a freeform session, which has the same condition.
    """
    if not _is_inside(filepath, cwd):
        return False
    # Build the relative path from paths that have NOT been normcased, then
    # normcase each side of the comparison instead. `_normalise` lowercases on
    # Windows, so feeding it in here produced `queue.md`, which could never
    # match the literals below — the gate was inverted on Windows for every
    # user of it. `os.path.relpath` compares case-insensitively internally on
    # Windows while returning the original components, so passing raw paths is
    # safe. `os.path.normcase` is the identity on POSIX, so exact matching is
    # preserved there.
    rel = os.path.relpath(os.path.normpath(filepath), os.path.normpath(cwd))
    rel = os.path.normcase(rel).replace("\\", "/")
    quiet_files = ("QUEUE.md", "SPEC.md")
    if rel in tuple(os.path.normcase(name) for name in quiet_files):
        return True
    # A working file, whichever session owns it. Matched by shape rather than
    # by this session's id: writing to another session's working file should be
    # rare, but it is a planning-note write either way and the quiet list is
    # about noise, not about scope. The scope-lock is what enforces ownership.
    if re.match(r"^_(build|plan)-[a-z0-9._-]+\.md$", rel):
        return True
    if rel.startswith(os.path.normcase("LOG") + "/"):
        return True
    return False


def _fire_once(cwd: str, session_id: str, marker_name: str) -> bool:
    """True the first time a session asks for `marker_name`, False after.

    Used for the unscoped-build surfacing, which describes a standing condition
    rather than one write — repeating it on every edit would train the user to
    dismiss it unread. Never raises: if the marker cannot be written, the caller
    gets True and the notice simply fires again, which is the safe direction.
    """
    try:
        marker_dir = os.path.join(cwd, ".throughliner")
        os.makedirs(marker_dir, exist_ok=True)
        safe_id = re.sub(r"[^A-Za-z0-9._-]", "_", session_id or "unknown")
        path = os.path.join(marker_dir, f"fired-{marker_name}-{safe_id}")
        if os.path.exists(path):
            return False
        with open(path, "w", encoding="utf-8") as f:
            f.write("1")
        return True
    except OSError:
        return True


def _is_build_file(filepath: str, cwd: str, build_files: list[str]) -> bool:
    """Check if a path is in the build's file list."""
    norm = _normalise(filepath)
    for bf in build_files:
        # Build files can be relative to project root
        candidate = _normalise(os.path.join(cwd, bf))
        if norm == candidate:
            return True
    return False


# --- Main ---

def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return 0

    if not isinstance(data, dict):
        return 0

    cwd = data.get("cwd", "")
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input") or {}

    # --- Subagent (Agent / Task): cost ask-gate ---
    # A subagent run burns tokens fast and a single run can exhaust the
    # user's usage, so every spawn gets a permission prompt before it starts.
    # "ask", never "deny": the user keeps full choice — the cost just stops
    # being a silent surprise. Checked before the cwd / SPEC.md gates below,
    # because the cost protection is universal: a subagent is as expensive in
    # an unadopted folder as an adopted one. Pairs with the hardened
    # "Tool use" rule in skill-nonspecific-rules.md — the rule steers, the gate
    # guarantees.
    #
    # Both names are matched deliberately: current Claude Code names the
    # subagent tool "Agent", older harnesses name it "Task". Matching only
    # "Task" is how this gate was silently dead — registered, firing, and
    # never recognising the tool it exists to guard.
    if tool_name in ("Task", "Agent"):
        return _ask(
            "[Sovereign Implementer] Claude wants to start a subagent. "
            "Subagents burn tokens fast — a single run can use up your usage "
            "for the session. Approve if this genuinely needs wide, "
            "open-ended exploration; decline to have Claude do the work "
            "directly instead. Declining is a normal, safe choice."
        )

    if not cwd:
        return 0

    # Only enforce in adopted projects (SPEC.md exists)
    spec_path = os.path.join(cwd, "SPEC.md")
    if not os.path.isfile(spec_path):
        return 0

    # THIS session's build working file. The scope-lock must answer "is there a
    # build for this session?", not "is there a build?" — a planning session
    # running alongside a build in another chat used to inherit that build's
    # file list.
    build_path = working_file(cwd, "build", data.get("session_id", ""))
    has_active_build = os.path.isfile(build_path)

    # --- Bash/PowerShell: git safety ---
    if tool_name in ("Bash", "PowerShell"):
        command = tool_input.get("command", "")
        if not isinstance(command, str):
            return 0

        # Match each git-safety pattern per segment, never against the whole
        # compound command, so tokens from unrelated segments can't combine
        # across a shell operator (the cross-segment false-denial bug).
        for segment in _split_segments(command):
            if RESET_HARD.search(segment):
                return _deny(
                    "[Sovereign Implementer] BLOCKED: `git reset --hard` destroys "
                    "uncommitted work and cannot be undone.\n\n"
                    "Safer alternatives:\n"
                    "- `git stash` — saves changes for later.\n"
                    "- `git checkout -- <file>` — discards one file's changes.\n"
                    "- `git reset HEAD~1` — moves HEAD back, keeps working tree."
                    + PATTERN_AS_DATA_NOTE
                )

            if PUSH_FORCE.search(segment):
                return _deny(
                    "[Sovereign Implementer] BLOCKED: `git push --force` can "
                    "overwrite remote commits.\n\n"
                    "Use `git push --force-with-lease` instead — it refuses to "
                    "push if the remote has commits you haven't fetched."
                    + PATTERN_AS_DATA_NOTE
                )

            if BLANKET_ADD.search(segment):
                return _deny(
                    "[Sovereign Implementer] BLOCKED: blanket adds (`git add -A`, "
                    "`git add --all`, `git add .`) stage everything in the tree, "
                    "including files never meant for the commit.\n\n"
                    "Stage explicitly — name each path: `git add <path> <path>`."
                    + PATTERN_AS_DATA_NOTE
                )

            if COMMIT_ALL.search(segment):
                return _deny(
                    "[Sovereign Implementer] BLOCKED: `git commit -a` / `-am` "
                    "auto-stages every modified file, including changes never "
                    "meant for the commit.\n\n"
                    "Stage explicitly, then commit: `git add <path> <path>`, "
                    'then `git commit -m "<message>"`.'
                    + PATTERN_AS_DATA_NOTE
                )

        # --- Structured shell writes to project files ---
        #
        # The denial had two reasons and they come apart. The scope-lock reason
        # genuinely does not apply to an in-scope target. The stale-view reason
        # does: a shell's view of a file can be stale, so a scripted write can
        # silently clobber work the edit tools would have refused to. That half
        # is unconditional, which is why this check is too — it does not consult
        # the Files list.
        #
        # What still passes, by construction: the session scratchpad (outside
        # the repo, sanctioned scratch space), the user's memory directory, and
        # anything outside the project — but only where the target is READABLE.
        # A write call whose target cannot be read is denied outright below,
        # scratchpad included, because an unreadable target cannot be shown to
        # be safe. Invoking the queue mover is unaffected: the command text is
        # just a script path and carries no write call.
        for target in structured_write_targets(command):
            resolved = target if os.path.isabs(target) else os.path.join(
                cwd, target
            )
            if _is_memory_dir(resolved) or _is_scratchpad_dir(resolved, cwd):
                continue
            if not _is_inside(resolved, cwd):
                continue
            return _deny(
                "[Sovereign Implementer] BLOCKED: this command writes to a file "
                f"through a script rather than through the editing tools.\n\n"
                f"Target: {target}\n\n"
                "The shell reads the file through a mount that can hold a stale "
                "view, so a scripted write can silently overwrite work the "
                "editing tools would have refused to clobber. That is true "
                "whatever the file is and whether or not it is in this build's "
                "scope, which is why this check does not consult the Files "
                "list.\n\n"
                "Use Edit or Write instead. If the edit is a large or awkward "
                "one (removing a whole work item from the queue is the usual "
                "case), there is a purpose-built tool for it: the queue mover, "
                "reorder_queue.py, which moves and deletes queue items "
                "byte-for-byte, addressed by slug. It ships inside the plugin, "
                "under the plugin root's scripts/ folder — search for the "
                "filename rather than assuming a path, since where the plugin "
                "is installed differs on every machine. If you genuinely need "
                "scratch space, the session scratchpad sits outside the repo "
                "and still passes.\n\n"
                "Note the honest limit of this check: it reads the command's "
                "text, not its behaviour. A write buried inside a script FILE "
                "this command merely invokes is not seen."
            )

        if has_computed_write_target(command):
            return _deny(
                "[Sovereign Implementer] BLOCKED: this command writes to a file "
                "through a script, and the target path is computed at runtime "
                "rather than written out, so this check cannot tell what it "
                "writes to.\n\n"
                "An unreadable target cannot be shown to be safe, so it is "
                "denied rather than allowed. This is not a rule about where the "
                "file is — it is that nobody can say where the file is.\n\n"
                "Three ways forward. Use Edit or Write, which is the right "
                "answer almost every time. If the edit is a large or awkward "
                "one — removing a whole work item from the queue is the usual "
                "case — the queue mover, reorder_queue.py, moves and deletes "
                "queue items byte-for-byte, addressed by slug. It ships inside "
                "the plugin, under the plugin root's scripts/ folder — search "
                "for the filename rather than assuming a path, since where the "
                "plugin is installed differs on every machine. If you need a "
                "script, write the target path out literally so it can be "
                "checked; a scratchpad path written literally still passes.\n\n"
                "Why this is strict: a computed target slipped past an earlier "
                "version of this check and silently corrupted QUEUE.md, and the "
                "only difference from the version that was correctly blocked "
                "was one variable assignment."
            )

        return 0

    # --- Edit/Write/MultiEdit: file-scope enforcement ---
    if tool_name not in ("Edit", "Write", "MultiEdit"):
        return 0

    filepath = tool_input.get("file_path", "")
    if not filepath:
        return 0

    # Publish the editing-state signal: a write is about to happen, on this
    # file, now. Placed before the scope checks so the marker is up before the
    # write, which is the whole point; if the write is then denied, the marker
    # simply goes stale and the reader treats it as not-editing. Cannot block
    # or fail the tool call — see write_editing_marker. Reached only after the
    # SPEC.md gate above, so the signal exists only in adopted projects.
    write_editing_marker(cwd, data.get("session_id", ""), filepath, True)

    # Rule 1: the working file's Files: section governs editability. Tri-state:
    # no section = skip enforcement, present but empty = method docs only,
    # entries listed = enforce the list.
    if has_active_build:
        build_files = _parse_build_files(build_path)

        if build_files is None:
            # An UNSCOPED build: a build working file with no Files: section at
            # all. It fails open, and from the inside it is indistinguishable
            # from a properly contained build — nothing marks the difference, so
            # the containment can be absent for a whole run with nobody noticing.
            # Surface it once, then get out of the way.
            if _fire_once(cwd, data.get("session_id", ""), "unscoped-build"):
                return _ask(
                    "[Sovereign Implementer] This build's working file has no "
                    "Files: section, so nothing is limiting which files it can "
                    "change. That may be exactly right — an audit lists no "
                    "files — but it is worth knowing rather than assuming.\n\n"
                    "Proceed, or stop and give the build a file list first?"
                )
            return 0

        if _is_method_doc(filepath, cwd):
            return 0

        if _is_memory_dir(filepath):
            return 0

        if _is_research_dir(filepath, cwd):
            return 0

        if _is_retired_terms_file(filepath, cwd):
            return 0

        if _is_scratchpad_dir(filepath, cwd):
            return 0

        if _is_inbox_dir(filepath):
            return 0

        if not build_files:
            return _deny(
                "[Sovereign Implementer] BLOCKED: this session's build working "
                f"file ({os.path.basename(build_path)}) lists no editable "
                "files, so only QUEUE.md, LOG/, and the working file itself "
                "can be edited. Audit and test sessions "
                "don't edit source files — route findings to Captures in "
                "QUEUE.md instead. If a file genuinely needs editing, halt "
                "and add it to the working file's Files: section with the "
                "user's approval."
            )

        if not _is_build_file(filepath, cwd, build_files):
            return _deny(
                "[Sovereign Implementer] BLOCKED: this file is not in the "
                f"current build's file list.\n\n"
                f"{os.path.basename(build_path)} allows: {', '.join(build_files)}\n\n"
                "Files: lines must be bare paths — one path per line, "
                "nothing else on the line. A note or annotation on a line "
                "becomes part of the path and silently breaks the match, so "
                "if this file looks listed above, check its line for "
                "trailing text.\n\n"
                "If this file genuinely needs editing, halt the build and, "
                "with the user's approval, add it to the working file's Files: "
                "section."
            )

    else:
        # Rule 4: no build working file, so no scope-lock is engaged. This is a
        # planning or freeform session. Writes to its own working surface pass
        # silently; anything else ASKS — never denies. See _is_plan_quiet_path
        # for why the ask must not become a denial.
        if not (
            _is_plan_quiet_path(filepath, cwd)
            or _is_memory_dir(filepath)
            or _is_research_dir(filepath, cwd)
            or _is_scratchpad_dir(filepath, cwd)
            or _is_inbox_dir(filepath)
        ):
            return _ask(
                "[Sovereign Implementer] This session has no build running, so "
                "nothing is limiting which files get changed — and this write is "
                "outside the files a planning session normally touches "
                f"(QUEUE.md, SPEC.md, LOG/).\n\nAbout to edit: {filepath}\n\n"
                "This isn't a refusal and there's nothing wrong with saying yes. "
                "Go ahead?"
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
