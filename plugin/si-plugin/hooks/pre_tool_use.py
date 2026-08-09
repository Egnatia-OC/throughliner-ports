#!/usr/bin/env python3
"""
PreToolUse hook — enforces three rules:

1. During a build, _build.md's Files: section governs which files are
   editable (method docs — QUEUE.md, LOG/, _build.md — plus the user's
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
# a pathlib write_text/write_bytes on a LITERAL path. A computed path — a
# variable, an f-string, a concatenation — is exactly the ambiguity this fails
# open on.
PY_INVOCATION = re.compile(r"\bpython[0-9.]*\b|\bpy\s+-[0-9]")
PY_OPEN_WRITE = re.compile(
    r"""\bopen\s*\(\s*(?P<q>['"])(?P<path>[^'"]+)(?P=q)\s*,\s*['"][waxr]*[wax]b?\+?['"]"""
)
PY_PATH_WRITE = re.compile(
    r"""\bPath\s*\(\s*(?P<q>['"])(?P<path>[^'"]+)(?P=q)\s*\)\s*\.\s*write_(?:text|bytes)\s*\("""
)

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
    """Extract file paths from _build.md's Files: section.

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


def _is_method_doc(filepath: str, cwd: str) -> bool:
    """Check if a path is a method doc (QUEUE.md, LOG/, _build.md, _plan.md)."""
    norm = _normalise(filepath)

    for doc in ("QUEUE.md", "_build.md", "_plan.md"):
        if norm == _normalise(os.path.join(cwd, doc)):
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
    finding is produced (plugin-behaviour.md Research > Filing), and that
    filing is open to every session type — build, test, or audit. The
    scope-lock must not block it, so this folder is always editable, mirroring
    the method-docs and memory exemptions. Matched relative to the project
    root, so it holds wherever the project lives.
    """
    norm = _normalise(filepath)
    research_dir = _normalise(os.path.join(cwd, "resources", "research"))
    return norm.startswith(research_dir + os.sep) or norm == research_dir


def _is_inbox_dir(filepath: str) -> bool:
    """Check if a path is inside any project's INBOX folder.

    Two directions, and both must pass the scope-lock. Inbound: this project's
    own `INBOX/`, where an arriving message is archived after being triaged.
    Outbound: another project's `INBOX/`, which is where a message is delivered
    — that path sits outside this project entirely, so no cwd-relative check
    could recognise it. Matching on an `INBOX` path segment covers both.

    The scope-lock is not what protects the user here. Every outbound message
    is shown and approved before it is written (plugin-behaviour.md, the
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
    plugin-behaviour.md's Temporary-files rule actively instructs Claude to
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
    # "Tool use" rule in plugin-behaviour.md — the rule steers, the gate
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

    build_path = os.path.join(cwd, "_build.md")
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
        # anything outside the project. The queue mover is untouched because its
        # write target is computed at runtime and this check only ever sees
        # literal paths — the deliberate fail-open, unchanged.
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
                "case), there is a purpose-built tool for it: "
                "scripts/reorder_queue.py moves and deletes queue items "
                "byte-for-byte, addressed by slug. If you genuinely need "
                "scratch space, the session scratchpad sits outside the repo "
                "and still passes.\n\n"
                "Note the honest limit of this check: it recognises script "
                "writes whose target path is written out literally. A command "
                "whose target is computed at runtime is not detected — it is "
                "not a permitted workaround, it is a gap."
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

    # Rule 1: _build.md's Files: section governs editability. Tri-state:
    # no section = skip enforcement, present but empty = method docs only,
    # entries listed = enforce the list.
    if has_active_build:
        build_files = _parse_build_files(build_path)

        if build_files is None:
            return 0

        if _is_method_doc(filepath, cwd):
            return 0

        if _is_memory_dir(filepath):
            return 0

        if _is_research_dir(filepath, cwd):
            return 0

        if _is_scratchpad_dir(filepath, cwd):
            return 0

        if _is_inbox_dir(filepath):
            return 0

        if not build_files:
            return _deny(
                "[Sovereign Implementer] BLOCKED: this session's _build.md "
                "lists no editable files, so only QUEUE.md, LOG/, and "
                "_build.md can be edited. Audit and test sessions "
                "don't edit source files — route findings to Captures in "
                "QUEUE.md instead. If a file genuinely needs editing, halt "
                "and add it to _build.md's Files: section with the user's "
                "approval."
            )

        if not _is_build_file(filepath, cwd, build_files):
            return _deny(
                "[Sovereign Implementer] BLOCKED: this file is not in the "
                f"current build's file list.\n\n"
                f"_build.md allows: {', '.join(build_files)}\n\n"
                "Files: lines must be bare paths — one path per line, "
                "nothing else on the line. A note or annotation on a line "
                "becomes part of the path and silently breaks the match, so "
                "if this file looks listed above, check its line for "
                "trailing text.\n\n"
                "If this file genuinely needs editing, halt the build and, "
                "with the user's approval, add it to _build.md's Files: "
                "section."
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
