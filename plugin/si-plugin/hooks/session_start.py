#!/usr/bin/env python3
"""
SessionStart hook — detect project state, orient Claude.

Three states:
  1. Not adopted (no SPEC.md) → suggest /setup.
  2. Adopted, _build.md exists → active build, offer resume with /next.
  3. Adopted, no active build → ready for /plan or /next.
"""

import hashlib
import json
import os
import re
import subprocess
import sys

# A placeholder counts only in hash position: an entry heading line
# ("## [HASH] — title") or the start of an index line ("- [HASH] — text").
# Body prose may mention the token literally and must never match — the
# pattern anchors on line shape, not on today's file layout, so the LOG
# structure can change without reworking this.
_HASH_POSITION = re.compile(r"^(?P<prefix>#{1,6}\s+|-\s+)\[HASH\](?P<sep>\s+[—–-]\s+)")


def _oldest_commit_for(cwd, entry_title):
    """Hash of the oldest commit that introduced `entry_title` under LOG/.

    Oldest, never newest: later commits (caps, renames, sweeps) also touch
    entry text, and the newest match would return the wrong hash for
    archived files.
    """
    try:
        result = subprocess.run(
            ["git", "log", "-S", entry_title, "--pretty=%h", "--", "LOG/"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    if result.returncode != 0:
        return ""
    hashes = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return hashes[-1] if hashes else ""


def _file_is_committed(cwd, relpath):
    """True if `relpath` has at least one commit in git history.

    Used to tell an unresolved placeholder that *should* have resolved (its
    entry file is already committed, so `git log -S` should have found it)
    from the normal case (the current session's own entry, not yet committed).
    """
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%h", "--", relpath],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0 and bool(result.stdout.strip())


def backfill_log_hashes(cwd):
    """Fill hash placeholders across LOG/*.md in place.

    Returns a one-line report for additionalContext, or "" when nothing
    was filled. Placeholders whose entry isn't committed yet resolve to
    no commit and stay in place for a later session.
    """
    log_dir = os.path.join(cwd, "LOG")
    if not os.path.isdir(log_dir):
        return ""
    try:
        names = sorted(os.listdir(log_dir))
    except OSError:
        return ""
    filled = 0
    touched_files = []
    # Placeholders that stayed unresolved even though their entry file is
    # already committed — these SHOULD have resolved, so surface them loudly
    # instead of the silent skip that let scrolly-thing's failure accumulate
    # unnoticed. Keyed by file so each anomalous file is named once.
    unresolved_committed = []
    for name in names:
        if not name.endswith(".md"):
            continue
        path = os.path.join(log_dir, name)
        relpath = "LOG/" + name
        try:
            with open(path, "r", encoding="utf-8", newline="") as f:
                lines = f.read().splitlines(keepends=True)
        except (OSError, UnicodeDecodeError):
            continue
        changed = False
        file_flagged = False
        for i, line in enumerate(lines):
            match = _HASH_POSITION.match(line)
            if not match:
                continue
            entry_title = line[match.end():].strip()
            if not entry_title:
                continue
            commit = _oldest_commit_for(cwd, entry_title)
            if not commit:
                # An unresolved placeholder is normal for the current session's
                # own entry (not committed yet). But if this entry file is
                # already committed, it should have resolved — flag it.
                if not file_flagged and _file_is_committed(cwd, relpath):
                    unresolved_committed.append(name)
                    file_flagged = True
                continue
            lines[i] = (
                match.group("prefix") + commit + match.group("sep") + line[match.end():]
            )
            changed = True
            filled += 1
        if changed:
            try:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write("".join(lines))
            except OSError:
                continue
            touched_files.append(name)
    anomaly = ""
    if unresolved_committed:
        anomaly = (
            f" Note: {len(unresolved_committed)} committed entry file(s) still "
            f"carry an unfilled hash placeholder ({', '.join(unresolved_committed)}) "
            "— these should have resolved, so the backfill may be failing (e.g. an "
            "index summary reworded since it was committed). Worth checking."
        )
    if not filled:
        if anomaly:
            return "[Sovereign Implementer] Log housekeeping:" + anomaly
        return ""
    return (
        f"[Sovereign Implementer] Log housekeeping: filled {filled} commit-hash "
        f"placeholder(s) in {', '.join(touched_files)}. This is an uncommitted "
        "working-tree edit — fold it into this session's commit." + anomaly
    )


def content_stamp(root):
    """Short content stamp over a plugin directory's own files.

    Walks `root`, hashes each file's bytes in sorted relative-path order,
    and returns a short hex stamp. Two directories with byte-identical
    tracked contents produce the same stamp; any file added, removed, or
    changed moves it. __pycache__ directories, compiled .pyc files and the
    plugin CLI's `.in_use` bookkeeping marker are excluded — they're runtime
    artifacts, not part of the package, and never shipped in the zip, so they
    must not perturb the stamp. Returns "" on any error or a missing root.

    `.in_use` earns its place on that list the hard way: the CLI writes it
    into whichever installed build is active and removes it again, so with it
    included the installed host's stamp changed between two session starts
    with no reinstall in between, and a host byte-identical to the target
    reported as stale. That false reading was acted on — it argued for
    deferring a merge on the grounds that the branch's plugin changes were not
    live, when they were.

    It is a DIRECTORY holding one marker file per live session, not a single
    file, and it is excluded on both limbs because the first attempt excluded
    only the filename and therefore did nothing — the walk descended into it
    and hashed its contents, so the stamp then moved with the number of open
    sessions. That shipped and was reported as verified, because the test
    accompanying it created `.in_use` as a file: it asserted the assumption
    rather than the world. The test now builds the real shape.

    This is the basis /plan's below-line revisit uses to tell whether host-side
    changes are actually live: the hook stamps the installed host (its own
    CLAUDE_PLUGIN_ROOT) here; in the self-hosting dev project /plan computes
    the target's stamp by calling this same function over plugin/si-plugin/,
    and equal stamps mean the installed host matches the current target. A
    version number can't answer this — a build batch edits host-side files
    without bumping any version — so the stamp is a content question, not a
    version one.
    """
    if not root or not os.path.isdir(root):
        return ""
    digest = hashlib.sha256()
    try:
        collected = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [
                d for d in dirnames if d not in ("__pycache__", ".in_use")
            ]
            for filename in filenames:
                if filename.endswith(".pyc") or filename == ".in_use":
                    continue
                full = os.path.join(dirpath, filename)
                rel = os.path.relpath(full, root).replace(os.sep, "/")
                collected.append((rel, full))
        for rel, full in sorted(collected):
            digest.update(rel.encode("utf-8"))
            digest.update(b"\0")
            with open(full, "rb") as f:
                digest.update(f.read())
            digest.update(b"\0")
    except OSError:
        return ""
    return digest.hexdigest()[:12]


def _dirty_tree_count(cwd):
    """Count files with uncommitted changes via `git status --porcelain`.

    Returns the count, or 0 on any error or a clean tree.
    """
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return 0
    if result.returncode != 0:
        return 0
    return len([line for line in result.stdout.splitlines() if line.strip()])


def _uncleared_red_flags(queue_path):
    """Descriptions of work items carrying `Red flag · State: uncleared`.

    A red flag is an ordinary work item (a #### heading) with a
    `Red flag · State: <state>` marker beneath it. This returns the cleaned
    heading text of every such line whose state is uncleared, so session
    start can surface unaddressed risks first-thing. The two-section work-line
    model has no pinned Red flags section, so this scan is what keeps an
    uncleared risk unmissable. Returns [] on any error or when none are
    uncleared.
    """
    try:
        with open(queue_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except (OSError, UnicodeDecodeError):
        return []
    uncleared_flags = []
    current_heading = None
    for raw in lines:
        stripped = raw.strip()
        if re.match(r"^####\s+\S", stripped):
            current_heading = stripped
            continue
        if re.match(r"^Red flag\s*·?\s*State:\s*uncleared\b", stripped, re.IGNORECASE):
            desc = current_heading if current_heading else stripped
            # Strip the leading #### and the trailing [slug] for a clean read.
            desc = re.sub(r"^#+\s+", "", desc)
            desc = re.sub(r"\s*\[[a-z0-9][a-z0-9-]+\]\s*$", "", desc)
            uncleared_flags.append(desc.strip())
    return uncleared_flags


def sweep_stale_editing_markers(cwd: str) -> None:
    """Delete editing-state marker files left behind by dead sessions.

    `.throughliner/editing-<session-id>.json` is written per session by the
    pre/post tool-use hooks. A session that crashes never writes its closing
    marker, so the file survives. This is housekeeping and nothing more — the
    SAFETY is the staleness rule a reader applies (an old timestamp means "not
    editing" whatever the flag says), so nothing depends on this sweep running.
    It exists so crashed sessions stop leaving litter: a reader re-reads the
    whole directory once a second per watched project, so unbounded growth is
    unbounded work on a one-second timer, and the directory syncs even though
    it is gitignored, so dead markers replicate rather than sitting locally.

    An hour is deliberately far longer than any reader's staleness window
    (~30 seconds), so this can never delete a marker a live session is still
    refreshing. Errors are swallowed: tidying must never break a session start.
    """
    try:
        import time

        marker_dir = os.path.join(cwd, ".throughliner")
        if not os.path.isdir(marker_dir):
            return
        cutoff = time.time() - 3600
        for name in os.listdir(marker_dir):
            if not (name.startswith("editing-") and name.endswith(".json")):
                continue
            path = os.path.join(marker_dir, name)
            try:
                if os.path.getmtime(path) < cutoff:
                    os.remove(path)
            except OSError:
                continue
    except Exception:
        return


def _waiting_inbox_messages(cwd):
    """Message files waiting in this project's own INBOX.

    Another project this user runs can write a message file straight into
    `INBOX/`. This hook surfaces what's waiting; nothing here reads a message's
    contents, and nothing scans any other project's folder — a project only
    ever reads its own mailbox. `INBOX/archive/` holds messages already
    handled, so it is skipped. Errors are swallowed: a mailbox scan must never
    be able to break a session start.
    """
    try:
        inbox = os.path.join(cwd, "INBOX")
        if not os.path.isdir(inbox):
            return []
        names = []
        for name in sorted(os.listdir(inbox)):
            if name.startswith("."):
                continue
            if os.path.isfile(os.path.join(inbox, name)):
                names.append(name)
        return names
    except OSError:
        return []


def _behaviour_rules_directive(plugin_root):
    """Instruction to read the behaviour rules from disk, rather than inlining them.

    Hook output is capped at 10,000 characters — documented in the Claude Code
    hooks reference, and confirmed by anthropics/claude-code#44086 and #70460.
    Past that, the harness saves the text to a file and injects a ~2KB preview
    plus a path in its place. `plugin-behaviour.md` is tens of kilobytes, so
    appending it whole blew the cap by a wide margin and the rules reached no
    session at all: only the short state lines above survived. The failure was
    loud in effect and silent in appearance.

    So the rules are pointed at, not pasted. This is a REDIRECT, not progressive
    disclosure — the distinction is load-bearing. Progressive disclosure fails
    for standing behavioural rules because a session has no trigger that would
    make it fetch "lead with the decision"; moving those rules behind an index
    deletes their effect. An unconditional read-this-first instruction defers
    nothing and hides nothing: the file is not split, no rule moves behind an
    index, and the whole of it is read before the session does anything.

    The trade is honest: the new failure mode is a skimmed redirect, which is
    quieter than the old one. That is why the self-check ships with it rather
    than after it. The self-check reads the `docset: B` frontmatter stamp the
    docs already carry, so it costs nothing and converts a silent
    wrong-file-opened failure into a loud one.
    """
    if not plugin_root:
        return ""
    path = "${CLAUDE_PLUGIN_ROOT}/docs-b/plugin-behaviour.md"
    return (
        "=== PLUGIN-WIDE BEHAVIOUR RULES — READ THESE FIRST ===\n"
        "The behaviour rules govern every skill and every reply in this session. "
        "They are not included here: they are too large for a hook to inject, so "
        "the harness would silently discard them.\n"
        f"READ {path} IN FULL NOW, before your first reply and before running any "
        "skill. This is not optional and it is not conditional — there is no "
        "trigger that would later remind you to fetch them, so a session that "
        "skips this runs ungoverned for its whole life.\n"
        "SELF-CHECK: the file you open carries `docset: B` in its frontmatter. If "
        "it isn't there or doesn't match, tell the user plainly that the "
        "behaviour rules could not be loaded and name what you found instead — do "
        "not carry on as though they had been.\n"
        "=== END BEHAVIOUR RULES DIRECTIVE ==="
    )


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return 0

    cwd = data.get("cwd", "")
    if not cwd or not os.path.isdir(cwd):
        return 0

    sweep_stale_editing_markers(cwd)

    spec_path = os.path.join(cwd, "SPEC.md")
    queue_path = os.path.join(cwd, "QUEUE.md")
    build_path = os.path.join(cwd, "_build.md")
    plan_state_path = os.path.join(cwd, "_plan.md")
    faq_index_path = os.path.join(cwd, "FAQ", "index.md")
    si_version_path = os.path.join(cwd, ".si-version")

    has_spec = os.path.isfile(spec_path)
    has_queue = os.path.isfile(queue_path)
    has_active_build = os.path.isfile(build_path)
    has_plan_state = os.path.isfile(plan_state_path)
    has_faq_index = os.path.isfile(faq_index_path)

    # `has_faq_index` is read for two jobs: the one-line pointer near the end of
    # this function, and the scaffold-drift check further down (a project with no
    # FAQ folder is behind). The index's CONTENTS used to be appended whole —
    # 2.3KB of question titles and anchors, larger than the whole surviving
    # preview once the payload was truncated. Unlike the behaviour rules, the FAQ
    # genuinely has a trigger: a session that needs an answer can open faq.md. So
    # the only thing the injection has to do is make the session aware the FAQ
    # exists, and that is one sentence.
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    behaviour_directive = _behaviour_rules_directive(plugin_root)

    plugin_version = ""
    if plugin_root:
        plugin_json_path = os.path.join(plugin_root, ".claude-plugin", "plugin.json")
        if os.path.isfile(plugin_json_path):
            try:
                with open(plugin_json_path, "r", encoding="utf-8") as f:
                    plugin_data = json.load(f)
                    plugin_version = plugin_data.get("version", "")
            except (OSError, json.JSONDecodeError):
                pass

    project_version = ""
    if os.path.isfile(si_version_path):
        try:
            with open(si_version_path, "r", encoding="utf-8") as f:
                project_version = f.read().strip()
        except OSError:
            pass

    # Version comparison is retained only for the separate "a plugin update just
    # happened" signal (a future consumer). It is NOT the user-facing "your project
    # is behind" warning anymore — that is now presence-based (see missing_scaffold
    # below), because the version bumps on every release and most releases add
    # nothing a project needs, so a version check cries wolf.
    version_mismatch = has_spec and plugin_version and project_version != plugin_version

    # State 1: Not adopted
    if not has_spec:
        # Check if there's substantial work here (not an empty folder)
        has_work = False
        nested_si = []
        try:
            entries = os.listdir(cwd)
            non_infra = [
                e for e in entries
                if e not in {
                    ".git", ".gitignore", "CLAUDE.md", ".claude",
                    "__pycache__", "node_modules", ".venv",
                }
            ]
            has_work = len(non_infra) > 3
            # Nested SI projects: child folders that are themselves set up
            # (they hold a SPEC.md or QUEUE.md). If the user opened a parent
            # folder by mistake, running /setup here would adopt the parent —
            # so name what we see and let them course-correct, rather than
            # scanning into a child to work there or adopting over the top of
            # them. Detection only; the choice stays the user's.
            for e in non_infra:
                child = os.path.join(cwd, e)
                if os.path.isdir(child) and (
                    os.path.isfile(os.path.join(child, "SPEC.md"))
                    or os.path.isfile(os.path.join(child, "QUEUE.md"))
                ):
                    nested_si.append(e)
        except OSError:
            pass

        if has_work:
            msg = (
                "[Sovereign Implementer] This folder has files but no SI docs yet. "
                "If it's a fresh project, run /setup to get started. If it already "
                "has planning or spec docs under other names — from another tool or "
                "an older version — /setup can treat it as a migration and map them "
                "into the method's docs."
            )
        else:
            msg = (
                "[Sovereign Implementer] Empty project folder. "
                "Run /setup to scaffold the project docs and describe what you're building."
            )

        if nested_si:
            msg += (
                " Heads up: this folder contains what look like separate Sovereign "
                "Implementer projects of their own (" + ", ".join(sorted(nested_si)) + "). "
                "If you meant to work in one of those, open it directly rather than this "
                "parent folder — running /setup here would adopt this parent folder, not "
                "them. Tell the user this plainly so they can course-correct before "
                "anything is adopted."
            )

        # Everything a hook feeds back must be nested under hookSpecificOutput
        # with its hookEventName — see resources/testing/hook_schema_check.py.
        # A top-level additionalContext is the flat legacy shape Claude Code
        # discards silently, and it is the exact defect this project shipped.
        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": msg,
            }
        }
        json.dump(output, sys.stdout)
        return 0

    # State 2 or 3: Adopted
    #
    # Order matters, and it is not cosmetic. Hook output is capped at 10,000
    # characters; past that the harness keeps a ~2KB preview and files the rest
    # away, so only what sits earliest reaches the session. Everything SHORT and
    # load-bearing goes first (uncleared red flags, project state, host version
    # and build stamp), then the behaviour-rules directive, then the FAQ pointer.
    #
    # Nothing appended here is bulky any more — the two things that used to be
    # (plugin-behaviour.md whole, and the FAQ index whole) are now pointers, and
    # the payload sits comfortably inside the cap. The ordering is kept anyway:
    # it costs nothing and it is what makes adding a line safe. The history is
    # worth remembering — with the rules pasted first they consumed the entire
    # surviving payload and every state line, red-flag surfacing included, fell
    # in the discarded remainder.
    context_parts = []

    # Uncleared red flags first-thing: the two-section model has no pinned Red
    # flags section, so this scan is what keeps an unaddressed data-exposure risk
    # unmissable at session start. Surfaced ahead of ordinary project state.
    uncleared_flags = _uncleared_red_flags(queue_path)
    if uncleared_flags:
        context_parts.append(
            "UNCLEARED RED FLAG(S) — unaddressed security, privacy, or data-exposure "
            "risk(s) recorded in this project's queue. Tell the user about these "
            "first, in plain language, before other work:\n"
            + "\n".join(f"- {flag}" for flag in uncleared_flags)
        )

    # Waiting mail, surfaced in one line. Short and state-bearing, so it sits up
    # here with the rest of the project state rather than at the bottom.
    waiting = _waiting_inbox_messages(cwd)
    if waiting:
        count = len(waiting)
        context_parts.append(
            f"[Sovereign Implementer] {count} message"
            f"{'' if count == 1 else 's'} waiting in this project's INBOX: "
            + ", ".join(waiting)
            + ". Mention this to the user in one line. When one is opened, route "
            "it through the three-way triage (work to do → a capture in "
            "Unprocessed; a finding → the LOG; evidence to re-read → resources/), "
            "then move the file to INBOX/archive/ so it stops being surfaced."
        )

    context_parts.append("[Sovereign Implementer] Project is set up.")
    context_parts.append(f"  SPEC.md: {'found' if has_spec else 'MISSING'}")
    context_parts.append(f"  QUEUE.md: {'found' if has_queue else 'MISSING'}")

    # Surface the installed host version (the version of the plugin actually
    # running this session, test suffix included). This is the always-correct
    # source for "what host is installed?" — it runs inside the installed host,
    # unlike any hand-maintained record, which goes stale the moment the user
    # reinstalls without Claude in the loop. Surfaced so the deferred-test roll
    # can resolve whether a host-side change has gone live mechanically instead
    # of interrogating the user. Version only — the host-vs-target comparison is
    # Claude's reasoning (a consumer project has no target to compare against).
    if plugin_version:
        context_parts.append(
            f"  Installed plugin (host) version: {plugin_version} — the version "
            "running this session. Use it to judge whether a host-side deferred "
            "test has gone live, instead of asking the user what's installed."
        )
        # Content stamp of the installed host's own files. The version number
        # alone can't tell whether host-side changes are live — a build batch
        # edits a hook or a doc without bumping any version, so the installed
        # host and the target can show the same version while the host is stale.
        # The stamp answers the real (content) question. In the self-hosting dev
        # project the deferred-test roll compares this against the target's stamp
        # (computed the same way over plugin/si-plugin/); a consumer never has a
        # target to compare against, so this is informational there.
        host_stamp = content_stamp(plugin_root)
        if host_stamp:
            context_parts.append(
                f"  Installed host build stamp: {host_stamp} — a content hash of "
                "the installed plugin's files. To tell whether a host-side change "
                "is actually live, compare this against the target's current stamp "
                "(in the dev project, run this hook's content_stamp() over "
                "plugin/si-plugin/): stamps match means the installed host carries "
                "the latest files; stamps differ means it hasn't been reinstalled "
                "since the most recent host-side change, so host-side tests aren't "
                "live yet. This catches edits that bump no version."
            )

    # Presence-based drift: a project is "behind" only when it's actually missing
    # files/folders the current plugin scaffolds. A higher plugin version with
    # everything present is not drift. Scope: missing files/folders only —
    # content-level drift (a file exists but lacks a newer section) is out of scope.
    missing_scaffold = []
    if not has_queue:
        missing_scaffold.append("QUEUE.md (your work queue)")
    if not os.path.isfile(os.path.join(cwd, "LOG", "index.md")):
        missing_scaffold.append("the LOG folder (your session records)")
    if not has_faq_index:
        missing_scaffold.append("the FAQ folder (workflow help)")
    if not os.path.isfile(si_version_path):
        missing_scaffold.append(
            "the .si-version marker (records which plugin version set the project up)"
        )

    if missing_scaffold:
        context_parts.append("")
        context_parts.append(
            "PROJECT OUT OF DATE — the current plugin creates files and folders this "
            "project doesn't have yet: " + "; ".join(missing_scaffold) + ". "
            "Because there is a real gap, you must open your first reply by telling the "
            "user plainly, in everyday language, which parts are missing, and offer to "
            "bring the project up to date by running /setup — it adds what's missing "
            "without touching their existing work. State this as your own first message "
            "before doing anything else; don't bury it in other output or wait to be "
            "asked, because a note the user never reads leaves the project drifting."
        )

    # Content-level top-up: a scaffolded file exists but is missing a setting the
    # current templates add. This is distinct from missing_scaffold above (whole
    # files/folders absent) — here the file is present but predates a newer setting,
    # so a project set up weeks ago silently misses it and the user never knows to
    # re-run setup. Add-only by design: the injected instruction tells Claude to
    # *add* the missing setting, never to rewrite or clobber what the user wrote.
    # Built as a list so future settings join by adding one entry. The risky case —
    # rewriting content whose template wording changed — is deliberately excluded
    # (parked as [scaffolding-resync]). The missing-file path (missing_scaffold)
    # owns a project with no CLAUDE.md at all, so we don't double-flag: each check
    # only fires when its host file is present.
    claude_md_path = os.path.join(cwd, "CLAUDE.md")
    claude_md_content = ""
    if os.path.isfile(claude_md_path):
        try:
            with open(claude_md_path, "r", encoding="utf-8") as f:
                claude_md_content = f.read()
        except OSError:
            pass

    # Each entry: the file that must already exist, its loaded content, the marker
    # whose absence means the setting is missing, and the plain-English instruction
    # to inject. "needs_answer" instructions open with a one-line question and write
    # the user's answer; a setting that needs no answer would be added silently with
    # a note (none yet — the list is built to hold both kinds).
    missing_settings = []
    setting_checks = [
        {
            "file_present": bool(claude_md_content),
            "marker": "## Editor",
            "instruction": (
                "Your CLAUDE.md is missing the Editor setting, added to the method "
                "since this project was set up. It records the .md editor you work "
                "in, which lets the plugin save tokens by pointing at a doc instead "
                "of re-pasting it. Open your first reply by asking, in one line, "
                "which editor the user works in here (they can say to skip if they "
                "don't use one). Then write their answer into a new '## Editor' "
                "section of CLAUDE.md, matching the template's format. Add only that "
                "section — change nothing else the user has written."
            ),
        },
    ]
    for check in setting_checks:
        if check["file_present"] and check["marker"] not in claude_md_content:
            missing_settings.append(check["instruction"])

    if missing_settings:
        context_parts.append("")
        context_parts.append(
            "PROJECT MISSING NEWER SETTINGS — this project was set up before the "
            "method added one or more settings it now expects. Bring it up to date "
            "now, before /next or /plan, adding only what's missing:"
        )
        for instruction in missing_settings:
            context_parts.append("- " + instruction)

    # Version-change report: the retained "a plugin update just happened" signal
    # (see version_mismatch above). This is NOT the drift warning — that is
    # presence-based above. Kept as a plain line: the old queue-inspecting
    # confirm nudge is gone, so the report no longer scans the queue.
    if version_mismatch:
        context_parts.append("")
        context_parts.append(
            "[Sovereign Implementer] Plugin version changed since this project was "
            f"last set up ({project_version} → {plugin_version}) — an update has been "
            "installed."
        )

    if has_active_build:
        context_parts.append("")
        context_parts.append(
            "ACTIVE BUILD in progress (_build.md exists). "
            "Run /next to resume, or /done if the work is complete. "
            "A planning session (/plan) may run in a separate chat alongside this build — "
            "if this chat was opened to plan, that is allowed; don't refuse it or insist on "
            "resuming or closing the build first."
        )
    else:
        context_parts.append("")
        context_parts.append(
            "Ready. "
            "Run /plan to manage the queue, or /next to start the top work item."
        )

    if has_plan_state:
        context_parts.append("")
        context_parts.append(
            "INTERRUPTED PLANNING SESSION (_plan.md exists). A previous /plan was left "
            "mid-processing. Run /plan to resume from the recorded item and beat, or "
            "/done to close out what was already routed."
        )

    # Dirty-tree warning: uncommitted changes with no active build and no active plan
    # almost always mean a previous session ended without /done — work sitting
    # unrecorded that a non-coder won't notice for weeks. Silent during an active build
    # or an active plan, where dirt is expected mid-session, not orphaned.
    if not has_active_build and not has_plan_state:
        dirty_count = _dirty_tree_count(cwd)
        if dirty_count:
            context_parts.append("")
            context_parts.append(
                f"[Sovereign Implementer] {dirty_count} file(s) have uncommitted "
                "changes from a previous session — /done will pick them up."
            )

    backfill_report = backfill_log_hashes(cwd)
    if backfill_report:
        context_parts.append("")
        context_parts.append(backfill_report)

    # The behaviour-rules directive comes before the FAQ pointer: it is the one
    # instruction the session must not miss, and the documented truncation
    # ordering only protects what sits earlier. Nothing here is bulky any more —
    # the whole payload is now well inside the 10,000-character cap — but the
    # ordering is kept honest so it stays safe as lines are added.
    if behaviour_directive:
        context_parts.append("")
        context_parts.append(behaviour_directive)

    if has_faq_index:
        context_parts.append("")
        context_parts.append(
            "This project has an FAQ covering how the workflow works — the "
            "question list is in FAQ/index.md and the answers in FAQ/faq.md. "
            "Open it when a workflow question comes up, or point the user there."
        )

    # Nested envelope, as above — a top-level additionalContext is discarded.
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "\n".join(context_parts),
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
