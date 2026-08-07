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
    changed moves it. __pycache__ directories and compiled .pyc files are
    excluded — they're disposable, regenerated by Python, and never shipped
    in the zip, so they must not perturb the stamp. Returns "" on any error
    or a missing root.

    This is the basis the deferred-test roll uses to tell whether host-side
    changes are actually live: the hook stamps the installed host (its own
    CLAUDE_PLUGIN_ROOT) here; in the self-hosting dev project /plan computes
    the target's stamp by calling this same function over plugin/si-plugin/,
    and equal stamps mean the installed host matches the current target. A
    version number can't answer this — a build edits host-side files
    without bumping any version — so the stamp is a content question, not a
    version one.
    """
    if not root or not os.path.isdir(root):
        return ""
    digest = hashlib.sha256()
    try:
        collected = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d != "__pycache__"]
            for filename in filenames:
                if filename.endswith(".pyc"):
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


# The running model's family and major version, e.g. "claude-opus-5" -> ("opus", 5)
# and "claude-haiku-4-5-20251001" -> ("haiku", 4). Anchoring on the FIRST number
# after the family name is what keeps Haiku 4.5 out of the 5-series bucket: its
# major version is 4, and the trailing "-5" is a minor.
#
# The separator is loose (hyphen, space, underscore, dot, or nothing) because
# this regex now reads TWO kinds of input: a model id from the payload
# ("claude-opus-5") and a human answer recorded at /setup ("Opus 5", "Claude
# Sonnet 5"). A hyphen-only pattern silently failed to parse every recorded
# answer and fell back to docset A, which is precisely the inert-selector bug.
_MODEL_FAMILY = re.compile(r"(opus|sonnet|haiku|fable)[\s\-_.]*(\d+)", re.IGNORECASE)

# The two docsets, by directory name under the plugin root.
_DOCSET_A = "docs"
_DOCSET_B = "docs-b"


def _model_id(data):
    """The running model's id from the SessionStart payload, or "".

    SessionStart is the one hook type that can carry a `model` field, but its
    presence is NOT guaranteed (resources/research/sessionstart-hook-model-detection.md),
    which is why every caller must have a defined fallback. The field is
    normally a plain string; some payloads wrap it in an object, so both
    shapes are read rather than assuming one.
    """
    model = data.get("model")
    if isinstance(model, str):
        return model.strip()
    if isinstance(model, dict):
        for key in ("id", "model", "display_name"):
            value = model.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


_RECORDED_MODEL = re.compile(r"^Model:\s*(.+?)\s*$", re.MULTILINE)


def _recorded_model(cwd):
    """The model recorded in the project's CLAUDE.md `Model:` field, or "".

    The payload's `model` field is documented as not guaranteed, and in the
    desktop app it does not arrive at all — so a docset chosen from it alone
    was inert everywhere it mattered. This is the fallback source: an explicit
    project setting the user answered at /setup. `not recorded` (what /setup
    writes when the question is skipped) is treated as absent.
    """
    path = os.path.join(cwd, "CLAUDE.md")
    if not os.path.isfile(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return ""
    match = _RECORDED_MODEL.search(content)
    if not match:
        return ""
    value = match.group(1).strip()
    if value.lower() in ("not recorded", "none", "unknown", ""):
        return ""
    return value


def _record_payload_once(cwd, data):
    """Write the received SessionStart payload to a research file, once.

    Distinguishes an ABSENT field from a malformed one — the question that
    turned a bug hunt into a design decision, and one nothing else can answer
    after the fact. Written only if the file doesn't already exist, so it
    records a real payload without growing each session. Silent on any error:
    a recording step must never be able to break the hook it observes.
    """
    try:
        target_dir = os.path.join(cwd, "resources", "research")
        target = os.path.join(target_dir, "session-start-payload-sample.json")
        if os.path.exists(target) or not os.path.isdir(target_dir):
            return
        with open(target, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True, default=str)
    except (OSError, TypeError, ValueError):
        pass


def _docset_for_model(model_id):
    """Which docset directory serves this model: docs-b for the 5-series, docs otherwise.

    Docset A (docs/) is the heavy, prescriptive docset the method was built on
    and is frozen as the known-good fallback; docset B (docs-b/) is the lighter
    docset authored for the 5-series, which wants less prescription rather than
    more. A is the fallback in every uncertain case — an absent `model` field,
    an id that doesn't parse, or any pre-5 family — because a wrong guess toward
    B strands the session on a docset its model isn't tuned for, while a wrong
    guess toward A only costs verbosity.
    """
    if not model_id:
        return _DOCSET_A
    match = _MODEL_FAMILY.search(model_id)
    if not match:
        return _DOCSET_A
    try:
        major = int(match.group(2))
    except ValueError:
        return _DOCSET_A
    return _DOCSET_B if major >= 5 else _DOCSET_A


def _docset_directive(docset):
    """The injected instruction that points every skill at the active docset.

    Each skill's SKILL.md names its procedure doc under `docs/`, and a hook
    can't rewrite those files — so when the active docset is B, this directive
    is what redirects the read. Emitted only for docset B: docset A needs no
    redirect, since `docs/` is what the skills already name.

    The directive carries its own SELF-CHECK. A redirect only holds while the
    model follows it, and a skimmed redirect leaves a session reading docset A
    while believing it read B — with nothing noticing. Docset B's docs all open
    with a `docset: B` frontmatter line and docset A's docs carry no frontmatter
    at all, so the stamp already exists and costs nothing to consult. Checking
    the stamp of the doc actually opened converts a silent failure into a loud
    one, and it holds whichever way the redirect ever points.
    """
    if docset != _DOCSET_B:
        return ""
    return (
        "ACTIVE DOCSET: docs-b. This session is running a 5-series model, which "
        "the lighter docset B serves. Wherever a skill names a procedure doc at "
        "${CLAUDE_PLUGIN_ROOT}/docs/<name>.md — plan.md, next.md, next-build.md, "
        "next-audit.md, done.md, done-build.md, done-audit.md, done-plan.md, "
        "setup.md, migrate-checklist.md — read "
        "${CLAUDE_PLUGIN_ROOT}/docs-b/<name>.md instead. Both docsets carry the "
        "same method; docset B states it more compactly. Don't mix them: read "
        "one doc from each procedure family, from docs-b only.\n"
        "SELF-CHECK, every time you open one of those docs: its first lines must "
        "carry `docset: B`. Docset A's docs have no frontmatter, so a missing "
        "stamp means you opened the wrong docset — go back and open the docs-b "
        "path before following anything you read. If the docs-b path genuinely "
        "isn't there, say so to the user plainly and name which docset you fell "
        "back to; don't proceed as though the redirect had worked.\n"
        "The routing itself is internal — never narrate it to the user. The "
        "exception is that failure: a mismatch or a missing file is told plainly."
    )


def _behaviour_rules_directive(plugin_root, docset):
    """Instruction to read the behaviour rules from disk, rather than inlining them.

    Hook output is capped at 10,000 characters — documented in the Claude Code
    hooks reference, and confirmed by anthropics/claude-code#44086 and #70460.
    Past that, the harness saves the text to a file and injects a ~2KB preview
    plus a path in its place. `plugin-behaviour.md` is roughly 50KB in docs-b
    and 89KB in docs, so appending it whole blew the cap by a wide margin and
    the rules reached no session at all: only the short state lines above
    survived. The failure was loud in effect and silent in appearance.

    So the rules are pointed at, not pasted. This is a REDIRECT, not progressive
    disclosure — the distinction is load-bearing. Progressive disclosure fails
    for standing behavioural rules because a session has no trigger that would
    make it fetch "lead with the decision"; moving those rules behind an index
    deletes their effect. An unconditional read-this-first instruction defers
    nothing and hides nothing: the file is not split, no rule moves behind an
    index, and the whole of it is read before the session does anything. The
    redirect mechanism is proven in this very payload — the docset directive is
    the one part that reached sessions through the truncation, and it was
    followed.

    The trade is honest: the new failure mode is a skimmed redirect, which is
    quieter than today's. That is why the self-check ships with it rather than
    after it.
    """
    if not plugin_root:
        return ""
    path = "${CLAUDE_PLUGIN_ROOT}/" + docset + "/plugin-behaviour.md"
    stamp = "carries `docset: B` in its frontmatter" if docset == _DOCSET_B else (
        "opens with the heading `# Sovereign Implementer — behaviour rules` and "
        "has no frontmatter"
    )
    return (
        "=== PLUGIN-WIDE BEHAVIOUR RULES — READ THESE FIRST ===\n"
        "The behaviour rules govern every skill and every reply in this session. "
        "They are not included here: they are too large for a hook to inject, so "
        "the harness would silently discard them.\n"
        f"READ {path} IN FULL NOW, before your first reply and before running any "
        "skill. This is not optional and it is not conditional — there is no "
        "trigger that would later remind you to fetch them, so a session that "
        "skips this runs ungoverned for its whole life.\n"
        f"SELF-CHECK: the file you open {stamp}. If it isn't there or doesn't "
        "match, tell the user plainly that the behaviour rules could not be "
        "loaded and name what you found instead — do not carry on as though they "
        "had been.\n"
        "=== END BEHAVIOUR RULES DIRECTIVE ==="
    )


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
    start can surface unaddressed risks first-thing. The two-section work-item
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


_SELF_HOSTING_MARKER = "Self-hosting:"


def self_hosting_state(cwd: str, claude_md: str) -> str:
    """Is this project developing the method itself? 'yes' / 'no' / 'unknown'.

    The TRIGGER is the plugin package living inside the repo the session was
    opened in — the shape only a self-hosting project has.

    The PAYLOAD is suppression, and that is the one thing detection can do that
    ambient CLAUDE.md cannot. Every other candidate payload (a self-hosting
    banner, guarding host/target confusion) is information that could simply be
    written into CLAUDE.md prose. Prose cannot stop a program printing a line.

    The line being stopped: the version-drift report exists to tell a consumer
    their plugin updated. In the project that PRODUCES the versions it is
    meaningless and permanently wrong — .si-version records the version that ran
    /setup while plugin.json carries the current one, and the two can never
    agree again, because every rezip widens the gap by design. So it fired at
    the top of every session, forever, carrying no information.

    Returns 'unknown' when the shape matches but nothing is recorded, so the
    caller can ask ONCE and record the answer. A recorded 'no' is honoured
    permanently — that cleanly covers detected-but-not-wanted, and is what turns
    a would-be per-session nag into a single ask.
    """
    try:
        for line in claude_md.splitlines():
            s = line.strip()
            if s.lower().startswith(_SELF_HOSTING_MARKER.lower()):
                value = s[len(_SELF_HOSTING_MARKER):].strip().lower()
                if value.startswith("yes"):
                    return "yes"
                if value.startswith("no"):
                    return "no"
        # No recorded answer — does the shape match?
        for root, dirs, files in os.walk(cwd):
            dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__")]
            if "plugin.json" in files and os.path.basename(root) == ".claude-plugin":
                # The plugin's own manifest lives inside this project.
                return "unknown"
            # Don't descend further than a few levels; the package sits near the
            # top in every real layout and a deep walk costs more than it earns.
            if root[len(cwd):].count(os.sep) >= 3:
                dirs[:] = []
        return "no"
    except Exception:
        return "no"


def jvm_toolchain_note(cwd: str) -> str:
    """One state line where a JVM/Gradle toolchain is present in the project.

    The desktop app is an MSIX-packaged Windows application, so everything it
    launches inherits a package sandbox that permits *binding* an AF_UNIX
    socket but refuses *connecting* to one — exactly what Java's NIO selector
    needs, and therefore what every Gradle build needs. Plain TCP loopback
    works, which is why the error that surfaces ("Unable to establish loopback
    connection") points away from the real cause, and why one project spent two
    whole sessions on it: one declaring victory on a false positive, one taking
    the failure apart properly.

    The line names the constraint AND THE HAND-OFF IN THE SAME BREATH, because
    the failure here was never a missing explanation. The user did not need the
    sandbox explained; they needed to hear "I can't build this — build it in
    Android Studio" and move on. An explanation delivered at the moment of
    being blocked is what produced the spiralling.

    Worded CONDITIONALLY — "if you're running in the Claude desktop app" — so
    the hook never has to detect its own surface, which is the one genuinely
    undesigned piece here. That costs a clause and sidesteps a guess.
    """
    markers = ("gradlew", "gradlew.bat", "build.gradle", "build.gradle.kts", "pom.xml")
    try:
        if not any(os.path.isfile(os.path.join(cwd, m)) for m in markers):
            return ""
    except OSError:
        return ""
    return (
        "[Sovereign Implementer] This project uses a JVM build tool (Gradle or "
        "Maven). If this session is running inside the Claude desktop app, "
        "Claude cannot run that build: the app's sandbox blocks a socket "
        "operation every JVM toolchain depends on, and the error it produces "
        "(\"Unable to establish loopback connection\") points away from the "
        "real cause. This is a known, already-diagnosed constraint — do not "
        "spend a session rediscovering it, and do not try to work around it. "
        "Hand the build back to whatever the user already builds with (Android "
        "Studio, IntelliJ, their IDE's Build command), ask them to paste back "
        "any errors, and fix those. Say this plainly the first time it comes "
        "up, in one sentence, together with what to do instead — never as a "
        "diagnosis for the user to act on. The full explanation is in the FAQ "
        "for anyone who wants it."
    )


def sweep_stale_editing_markers(cwd: str) -> None:
    """Delete editing-state marker files left behind by dead sessions.

    `.throughliner/editing-<session-id>.json` is written per session by the
    pre/post tool-use hooks. A session that crashes never writes its closing
    marker, so the file survives. This is housekeeping and nothing more — the
    SAFETY is the staleness rule a reader applies (an old timestamp means "not
    editing" whatever the flag says), so nothing depends on this sweep running.
    It exists only so crashed sessions stop leaving litter.

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

    # Which docset serves this session. THREE SOURCES, LAYERED — deliberately
    # not one replacing another:
    #   1. the payload's `model` field, when present. Ground truth about the
    #      session actually running, so it wins wherever the harness supplies
    #      it. Documented as not guaranteed, and absent in the desktop app.
    #   2. the project's recorded `Model:` setting, answered once at /setup.
    #      This is what makes the choice work at all where (1) never arrives.
    #   3. docset A, the known-good fallback, when neither is available.
    # Layering costs nothing, keeps working automatically wherever the field
    # does appear, and never weakens the no-strand guarantee.
    _record_payload_once(cwd, data)
    docset = _docset_for_model(_model_id(data) or _recorded_model(cwd))
    # If the selected docset's folder is missing from the installed plugin, fall
    # back to docset A — but never silently. The directive's own SELF-CHECK (the
    # session telling the user the docs-b path isn't there) ships only WITH the
    # directive, and this branch suppresses the directive — so without this
    # state line the one guard against a mispackaged install is the very thing
    # that goes quiet when it happens.
    docset_fallback_note = ""
    if docset != _DOCSET_A and plugin_root and not os.path.isdir(
        os.path.join(plugin_root, docset)
    ):
        docset_fallback_note = (
            "[Sovereign Implementer] This session picked the lighter instruction "
            f"set ({docset}), but that folder is missing from the installed "
            "plugin — not from your project; the plugin's own installation looks "
            "incomplete. The session runs on the fuller instruction set "
            f"({_DOCSET_A}) instead and everything still works; it will just be "
            "more verbose than intended. Reinstalling or updating the plugin "
            "should restore the missing folder. Mention this state line to the "
            "user plainly, once."
        )
        docset = _DOCSET_A
    docset_directive = _docset_directive(docset)

    behaviour_directive = _behaviour_rules_directive(plugin_root, docset)

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

        # /setup is the skill this branch points at, and it too lives in both
        # docsets — so the redirect has to reach an unadopted folder as well,
        # or a 5-series session would scaffold from docset A while every later
        # session ran docset B.
        if docset_directive:
            msg += "\n\n" + docset_directive
        if docset_fallback_note:
            msg += "\n\n" + docset_fallback_note

        # The behaviour-rules directive reaches an unadopted folder too, by the
        # same reasoning the docset directive above already accepts.
        #
        # The exemption this removes had a stated reason that is now obsolete:
        # the rules "aren't loaded yet" described the OLD delivery model, where
        # this hook inlined them into an adopted project's context. It doesn't
        # any more — it emits a directive telling the session to READ
        # plugin-behaviour.md from the installed plugin, and that file ships
        # with the plugin, readable whether or not anything has been adopted.
        # So the rules were absent not because they were unavailable, but
        # because this branch didn't point at them.
        #
        # The window matters more than its size suggests: it is the moment a
        # folder is adopted and files are created — the highest-consequence
        # moment in the method, and the only one a brand-new user ever sees.
        if behaviour_directive:
            msg += "\n\n" + behaviour_directive

        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": msg,
            }
        }
        json.dump(output, sys.stdout)
        return 0

    # State 2 or 3: Adopted
    # Order matters, and it is not cosmetic. Hook output is capped at 10,000
    # characters; past that the harness keeps a ~2KB preview and files the rest
    # away, so only what sits earliest reaches the session. Everything SHORT and
    # load-bearing goes first (uncleared red flags, project state, host version
    # and build stamp, the docset directive), then the behaviour-rules directive,
    # then the FAQ pointer.
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
    # unmissable at session start. It is the very first thing appended, ahead of
    # everything else including the docset directive — it is the line that can
    # least afford to be cut.
    uncleared_flags = _uncleared_red_flags(queue_path)
    if uncleared_flags:
        context_parts.append(
            "UNCLEARED RED FLAG(S) — unaddressed security, privacy, or data-exposure "
            "risk(s) recorded in this project's queue. Tell the user about these "
            "first, in plain language, before other work:\n"
            + "\n".join(f"- {flag}" for flag in uncleared_flags)
        )

    if docset_directive:
        context_parts.append(docset_directive)
    if docset_fallback_note:
        context_parts.append(docset_fallback_note)

    # Placed high: it is short, load-bearing, and its whole job is to be read
    # BEFORE a session starts trying to build. Arriving late would be arriving
    # after the two sessions it exists to save.
    jvm_note = jvm_toolchain_note(cwd)
    if jvm_note:
        context_parts.append(jvm_note)

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
        # alone can't tell whether host-side changes are live — a build
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

    # The content-level setting top-up USED TO LIVE HERE and has been removed
    # deliberately — it is now /plan's opening read (docs-b/plan.md).
    #
    # Not a retiming: a session-start hook fires BEFORE anything knows what the
    # session is for, so its question cannot choose a good moment. It can only
    # attach itself to whichever command comes first — and it did, repeatedly.
    # The text it injected said "bring it up to date now, before /next or /plan",
    # so it wedged an unrelated question into a close, and on another occasion
    # held a queued /next run (four builds and a walk-through) behind an ask
    # about a setting the method had since retired. That was the mechanism doing
    # exactly what it instructed, which is why retiming it in place would have
    # meant writing a rule telling the hook not to do the thing its position
    # makes it do.
    #
    # The capability is kept rather than dropped: it is the only thing that
    # reaches a project set up weeks ago when the method later adds a setting.
    # It now runs in /plan's opening read, which already reads project state,
    # already folds what it finds into one narration, and is structurally
    # incapable of holding a /next run.
    #
    # The PRESENCE-based missing_scaffold check above stays exactly as it is:
    # it detects whole files or folders absent, is a different check, and gates
    # nothing.

    # Self-hosting detection and its one payload: suppression. In the project
    # that produces the versions, the version-drift report below is meaningless
    # and permanently wrong, so it is not run at all.
    #
    # Suppressed means SILENT — not "reported as suppressed". The behaviour
    # rules are explicit that a silenced check contributes nothing to the
    # opening narration, including no mention that it was silenced.
    claude_md_content = ""
    claude_md_path = os.path.join(cwd, "CLAUDE.md")
    if os.path.isfile(claude_md_path):
        try:
            with open(claude_md_path, "r", encoding="utf-8") as f:
                claude_md_content = f.read()
        except OSError:
            pass

    self_hosting = self_hosting_state(cwd, claude_md_content)
    if self_hosting == "unknown":
        # Ask ONCE and record the answer. The recorded sign is what turns this
        # from a per-session nag into a single question, and it covers the
        # detected-but-not-wanted case cleanly: a recorded "no" is permanent.
        context_parts.append("")
        context_parts.append(
            "[Sovereign Implementer] This project contains the plugin's own "
            "package, which is the shape a project has when it is being used to "
            "develop the method itself rather than to build an app. Ask the user "
            "once, in plain language — \"this looks like you're developing the "
            "method itself rather than building your own project; is that "
            "right?\" — and record the answer in CLAUDE.md as a line reading "
            "`Self-hosting: yes` or `Self-hosting: no`. Once it is recorded this "
            "is never asked again, whichever way they answer."
        )

    # Version-change report: the retained "a plugin update just happened" signal
    # (see version_mismatch above). This is NOT the drift warning — that is
    # presence-based above. Kept as a plain line: the old queue-inspecting
    # confirm nudge is gone, so the report no longer scans the queue.
    if version_mismatch and self_hosting != "yes":
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
