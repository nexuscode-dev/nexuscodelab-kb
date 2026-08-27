# INDEX

**The retrieval entry point.** One line per note, sectioned by layer. A note without a line here cannot be
retrieved, and a note that cannot be retrieved does not exist (KB_DESIGN_PROPOSAL §3.1). `scripts/check-vault.py`
enforces it.

**Write the line to carry the claim, not the topic.** `— the ceiling on new concepts per lesson, and why` beats
`— about lesson length`. Done properly, a grep of this file alone often answers the question without opening
anything, which is exactly what T1 measures.

Format: `- [id](path) — the claim it makes (status · decay)`

Sectioned by layer so appends don't collide. **This file is the real merge hotspot** — atomic notes barely conflict;
a shared one-line-per-note index does constantly.

---

## Curriculum

The scope decision that L3 is written against. Neither knowledge nor output.

- [web-system-architecture](curriculum/web-system-architecture.md) — v1's course charter: the salesperson spine, the 20-lesson outline, and **what we deliberately decided not to teach** (draft)

## L1 Pedagogy · 0 / 8–10

*How we teach — lesson archetypes, sequencing, outcome verbs, assessment patterns, cognitive load. Tops out at
`reviewed`: these are opinions with no source (§9).*

## L2 Audience · 0 / 3–4

*Who we teach — the three personas, prior knowledge, weekly time budget, motivation, how each fails. Tops out at
`reviewed`.*

## L3 Domain · 0 / 15–20

*What we teach — scoped by the charter above, never by the field. Every note needs a source in L6 and a teaching
angle. 17 candidates are listed in the charter.*

## L4 Platform · 0 / 4–6

*What NexusLab can hold, and its limits. Every note pins `verified_against: <admin-repo SHA>` — a date stamp is
unfalsifiable, and §11 proved it.*

## L5 Style · 0 / 3–5

*How it sounds — voice, language policy, code style, the things we never do.*

## L6 Sources

*The register: id, title, URL, date accessed, licensing stance, and the `quote:` field holding the exact supporting
sentence. A ledger, not capped, and not listed here — source records are reached through a note's `sources:` field,
never by browsing.*

---

## Reading this index when nothing is in it yet

The vault is empty by design as of 2026-08-19. The build order is in HANDOVER §7, and the point of the sequencing is
that **the seed notes are deliberately uneven** — 2 for L2/L4/L5, 3 for L1, 4 for L3 — so that no layer is complete
before the day-3 diagnostic that is supposed to tell us which layer is underfed.

An empty vault passes every mechanical check in `scripts/check-vault.py`. Only the five tests in `tests/` measure
whether it is any good.
