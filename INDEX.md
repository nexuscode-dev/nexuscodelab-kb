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

## L1 Pedagogy · 5 / 8–10

*How we teach — lesson archetypes, sequencing, outcome verbs, assessment patterns, cognitive load. Tops out at
`reviewed`: these are opinions with no source (§9).*

- [beginner-lecture-archetype](brain/pedagogy/beginner-lecture-archetype.md) — the fixed section order of a beginner Lecture, and how it contributes one question to its section's Quiz, so two authors write recognizably similar lessons (draft · durable)
- [one-new-idea-per-lesson](brain/pedagogy/one-new-idea-per-lesson.md) — a lesson introduces exactly one new idea; everything else is scaffolding for it (draft · durable)
- [our-analogies-chosen-and-rejected](brain/pedagogy/our-analogies-chosen-and-rejected.md) — one house analogy per concept, chosen for its boundary, with the rejected ones and why (draft · durable)
- [scenario-mcqs-over-recall-mcqs](brain/pedagogy/scenario-mcqs-over-recall-mcqs.md) — every quiz question asks for a judgement about a situation, never a definition (draft · durable)
- [manual-model-before-ai-tooling](brain/pedagogy/manual-model-before-ai-tooling.md) — build the manual web-system model first; AI is taught later as a component inside it, never a shortcut past the architecture (draft · durable)

## L2 Audience · 1 / 6–8

*Who we teach — the three personas, prior knowledge, weekly time budget, motivation, how each fails. Tops out at
`reviewed`.*

- [salesperson-persona](brain/audience/salesperson-persona.md) — the spine persona: a non-technical salesperson to be made conversant and correctly-modelled, never able to build (draft · durable)

## L3 Domain · 4 / 12–15

*What we teach — scoped by the charter above, never by the field. Every note needs a source in L6 and a teaching
angle. 17 candidates are listed in the charter.*

- [what-a-table-record-and-column-are](brain/domain/what-a-table-record-and-column-are.md) — a table is rows sharing the same named columns; a column is a labelled slot every row has, not one cell's value (verified · durable)
- [why-the-browser-cannot-reach-the-database](brain/domain/why-the-browser-cannot-reach-the-database.md) — the browser talks to a server over HTTP and the server fetches from the database; "cannot reach it directly" is the teaching frame (draft · durable)
- [frontend-vs-backend-is-a-trust-line-not-a-job-title](brain/domain/frontend-vs-backend-is-a-trust-line-not-a-job-title.md) — client-side JavaScript validation can be circumvented, so the server must validate before using data; we teach the split as a trust line (verified · durable)
- [a-schema-change-is-not-a-text-edit](brain/domain/a-schema-change-is-not-a-text-edit.md) — in MySQL, adding a field is an ALTER TABLE that changes the table's structure; "not a text edit" is the teaching frame (verified · durable)

## L4 Platform · 3 / 4–6

*What NexusLab can hold, and its limits. Every note pins `verified_against: <myanlearn monorepo SHA>` — a date
stamp is unfalsifiable, and §11 proved it.*

- [nexuslab-lesson-primitives](brain/platform/nexuslab-lesson-primitives.md) — a lesson is exactly one of Lecture/Quiz/Lab, and the hard limits of each (draft · volatile)
- [what-a-lab-can-actually-grade](brain/platform/what-a-lab-can-actually-grade.md) — one JS buffer, stdout byte-matched; no browser/DOM/packages, ten runs a day charged per test case (draft · volatile)
- [admin-editor-strips-rich-content](brain/platform/admin-editor-strips-rich-content.md) — one admin-editor save deletes tables and mermaid; rich lectures are edited in the seeder, never the panel (draft · volatile)

## L5 Style · 2 / 3–5

*How it sounds — voice, language policy, code style, the things we never do.*

- [voice-and-never-dos](brain/style/voice-and-never-dos.md) — plain voice for a busy non-technical reader, and the list of things we never write (draft · durable)
- [every-analogy-must-survive-japanese](brain/style/every-analogy-must-survive-japanese.md) — an analogy is approved only if it still carries the concept after translation to Japanese (draft · durable)

## L6 Sources

*The register: id, title, URL, date accessed, licensing stance, and the `quote:` field holding the exact supporting
sentence. A ledger, not capped, and not listed here — source records are reached through a note's `sources:` field,
never by browsing.*

---

## Reading this index when nothing is in it yet

The vault is deliberately thin (the live per-layer counts are in the section headers above) so that no layer is
complete before the thin-vault diagnostic that tells us which layer is underfed — the build order is in HANDOVER §7.

An empty vault passes every mechanical check in `scripts/check-vault.py`. Only the five tests in `tests/` measure
whether it is any good.
