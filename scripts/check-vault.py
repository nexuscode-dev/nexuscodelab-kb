#!/usr/bin/env python3
"""Contract validator for the NexusLab brain. Run before every commit.

Exists because of measured evidence, not tidiness. In the team's `nexusbim-brain`, the one rule that lived inside a
copy-pasted template block held at 100% (frontmatter, 170/170 notes) while every rule that required the author to
remember prose drifted (95% of notes blew through a 400-word ceiling; a four-state status ladder ended up 167
`developing`, 4 `planned`, zero `seed`, zero `mature`). KB_DESIGN_PROPOSAL §4.2 calls the body contract "more
important than the frontmatter" — which makes the more important half the one with no defense. This is the defense.

Usage:
    python3 scripts/check-vault.py            # check the working tree
    python3 scripts/check-vault.py --staged   # also enforce the status-upgrade gate on staged changes
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# KB_DESIGN_PROPOSAL §7 — per layer, never global. A global cap gets eaten by whoever writes fastest, always L3.
CAPS = {
    "pedagogy": (8, 10),
    "audience": (3, 4),
    "domain": (15, 20),
    "platform": (4, 6),
    "style": (3, 5),
    "sources": (0, 10_000),  # a register, not capped (§7)
}

# §4.2 — the floor binds domain notes, where a thin note means a thin lesson. L4/L5/L6 have a ceiling and no floor:
# forcing 150 words onto a platform constraint or a source record produces padding, and padding defeats retrieval.
WORD_FLOOR = {"pedagogy": 150, "audience": 150, "domain": 150}
WORD_CEILING = 400
CEILING_EXEMPT = {"sources"}  # register entries are ledger rows, not notes

REQUIRED_KEYS = ["id", "layer", "status", "confidence", "decay", "last_verified", "sources", "teaches"]
VALID = {
    "status": {"draft", "reviewed", "verified"},
    "confidence": {"high", "medium", "low"},
    "decay": {"durable", "volatile"},
}

FM = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)
SHA = re.compile(r"\A[0-9a-f]{7,40}\Z")

problems: list[str] = []
notes_by_layer: dict[str, list[Path]] = {layer: [] for layer in CAPS}


def fail(path: Path, msg: str) -> None:
    problems.append(f"{path.relative_to(ROOT)}: {msg}")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | None:
    m = FM.match(text)
    if not m:
        return None
    fields: dict[str, str] = {}
    for line in m.group(1).split("\n"):
        line = line.split(" #")[0].rstrip()  # strip trailing comments, keep '#' inside values
        if not line or line.startswith("#") or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, m.group(2)


def check_note(path: Path, layer: str) -> None:
    text = path.read_text(encoding="utf-8")
    parsed = parse_frontmatter(text)
    if parsed is None:
        fail(path, "no YAML frontmatter — frontmatter is the query language (§3.1)")
        return
    fields, body = parsed

    for key in REQUIRED_KEYS:
        if key not in fields:
            fail(path, f"frontmatter missing required key `{key}`")

    for key, allowed in VALID.items():
        if key in fields and fields[key] not in allowed:
            fail(path, f"`{key}: {fields[key]}` is not one of {sorted(allowed)}")

    if fields.get("id") and fields["id"] != path.stem:
        fail(path, f"`id: {fields['id']}` does not match the filename `{path.stem}`")

    if fields.get("layer") and fields["layer"] not in (layer, "source"):
        fail(path, f"`layer: {fields['layer']}` but the note lives in brain/{layer}/")

    # §9 — L1 and L2 are opinions with no source to check against. They top out at `reviewed` until a human who has
    # taught signs them. This is a labelling discipline: the risk is someone later reading an opinion as sourced fact.
    if layer in {"pedagogy", "audience"} and fields.get("status") == "verified":
        fail(path, "L1/L2 notes can never be `verified` — they are opinions with no source (§9). Cap at `reviewed`")

    # §4.1 — a date stamp is unfalsifiable; a SHA makes staleness a `git diff`. §11 was stamped "verified" twice
    # and was wrong both times — first from type files, then from a stale fork of apps/admin. The SHA is of the
    # platform monorepo (nexuscode-devs/myanlearn), read at origin/develop.
    if layer == "platform" and not SHA.match(fields.get("verified_against", "")):
        fail(path, "platform notes need `verified_against: <myanlearn commit SHA>`, not just a date (§4.1)")

    # §4.1 — retrieval question 9 asks which notes are "due" for re-verification. Without a date, "due" has no answer.
    if fields.get("decay") == "volatile" and "review_by" not in fields:
        fail(path, "`decay: volatile` needs `review_by: <date>` or retrieval question 9 is unanswerable (§4.1)")

    # §5.1 / CLAUDE.md — volatile facts go in volatile notes so a refresh stays bounded.
    if fields.get("decay") == "durable":
        for pattern, what in ((r"\bv?\d+\.\d+", "a version number"), (r"[$¥]\s?\d", "a price")):
            if re.search(pattern, body):
                fail(path, f"`decay: durable` note contains {what} — volatile facts belong in a volatile note (§5.1)")
                break

    # CLAUDE.md — claims live in the note, source records live in L6. A domain claim with no source is unverifiable,
    # which is the failure mode this whole design targets.
    if layer == "domain" and fields.get("sources", "[]").strip() in {"[]", ""}:
        fail(path, "domain note has no source — every domain claim needs an L6 source record")

    words = len(body.split())
    floor = WORD_FLOOR.get(layer)
    if floor and words < floor:
        fail(path, f"{words} words, below the {floor}-word floor (§4.2)")
    if layer not in CEILING_EXEMPT and words > WORD_CEILING:
        fail(path, f"{words} words, over the {WORD_CEILING}-word ceiling — retrieval is what this protects (§4.2)")


def check_index(index_text: str) -> None:
    """A note with no INDEX.md line cannot be retrieved, and a note that cannot be retrieved does not exist (§3.1)."""
    for layer, paths in notes_by_layer.items():
        if layer == "sources":
            continue  # L6 records are reached through a note's `sources:` field, not by browsing the index
        for path in paths:
            if path.stem not in index_text:
                fail(path, "no line in INDEX.md — a note that cannot be retrieved does not exist (§3.1)")


def check_status_gate() -> None:
    """§6.4 — no commit may change a `status:` line without also touching tests/audit-log.md.

    Solo, this is what makes "a claim of reliability is backed by a test that ran" true of the commit graph rather
    than merely stated.
    """
    try:
        diff = subprocess.run(
            ["git", "diff", "--cached", "-U0", "--", "brain/"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
        staged = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.split()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return

    changed_status = [
        line for line in diff.split("\n")
        if line.startswith(("+status:", "-status:")) or re.match(r"^[+-]status:", line)
    ]
    if changed_status and "tests/audit-log.md" not in staged:
        problems.append(
            "a staged commit changes a `status:` line without touching tests/audit-log.md — "
            "a status upgrade needs the test that granted it (§6.4)"
        )


def check_hook_wiring() -> None:
    """The check cannot enforce its own distribution, so it makes its own absence loud.

    A hook in `.git/hooks/` is untracked and guards exactly one working copy. This repo had one, and
    a clone was tested on 2026-08-19: it committed a note violating six rules without complaint. The
    hook now lives in `hooks/` and is reached via core.hooksPath, which is per-clone config — so the
    first manual run of this script on a new machine is what reveals the hook is not wired.
    """
    try:
        path = subprocess.run(
            ["git", "config", "--get", "core.hooksPath"],
            cwd=ROOT, capture_output=True, text=True,
        ).stdout.strip()
    except FileNotFoundError:
        return
    if path != "hooks":
        problems.append(
            "core.hooksPath is not set to `hooks` — the pre-commit check is not installed on this "
            "clone. Run: git config core.hooksPath hooks   (see hooks/README.md)"
        )


def main() -> int:
    brain = ROOT / "brain"
    if not brain.is_dir():
        print("no brain/ directory — nothing to check")
        return 0

    for layer in CAPS:
        layer_dir = brain / layer
        if not layer_dir.is_dir():
            continue
        for path in sorted(layer_dir.glob("*.md")):
            # CLAUDE.md — filenames are the primary index, so they must be descriptive kebab-case keywords.
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", path.stem):
                fail(path, "filename must be descriptive kebab-case — filenames are the primary index (§3.1)")
            if re.fullmatch(r"note-?\d+", path.stem):
                fail(path, "never name a file note-042.md")
            notes_by_layer[layer].append(path)
            check_note(path, layer)

    for layer, (lo, hi) in CAPS.items():
        count = len(notes_by_layer[layer])
        if count > hi:
            problems.append(
                f"brain/{layer}/ has {count} notes, over its cap of {hi} — "
                f"merge two notes or defer to brain/_backlog/{layer}.md. Never raise a cap mid-build (§7.1)"
            )

    index = ROOT / "INDEX.md"
    if index.is_file():
        check_index(index.read_text(encoding="utf-8"))
    else:
        problems.append("INDEX.md is missing — it is the retrieval entry point (§3)")

    for layer in CAPS:
        if not (brain / "_backlog" / f"{layer}.md").is_file():
            problems.append(f"brain/_backlog/{layer}.md is missing — the pressure valve is mandatory (§7.1)")

    check_hook_wiring()

    if "--staged" in sys.argv:
        check_status_gate()

    total = sum(len(v) for v in notes_by_layer.values())
    if problems:
        print(f"FAIL — {len(problems)} problem(s) across {total} note(s):\n")
        for p in problems:
            print(f"  - {p}")
        return 1

    counts = " · ".join(f"{k[:4].upper()} {len(v)}/{CAPS[k][1]}" for k, v in notes_by_layer.items() if k != "sources")
    print(f"OK — {total} notes. {counts}")
    if total == 0:
        print("\n  (An empty vault passes every check. The tests in tests/ are what actually measure it.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
