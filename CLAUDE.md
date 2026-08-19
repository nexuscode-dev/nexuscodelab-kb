# NexusLab Brain — Claude Code Project Memory

Knowledge base ("brain") that beginner tech courses for **NexusLab** are generated from. This repo holds the
knowledge and the generated courses; NexusLab itself is a separate product.

**Read `KB_DESIGN_PROPOSAL.md` before writing anything.** It is the design spec — schema, acceptance tests,
layer definitions, budget, timebox. This file holds only the rules that must be enforced on every turn.
**Read `HANDOVER.md`** for why the design is shaped this way and where to start.

## Layout
```
brain/{pedagogy,audience,domain,platform,style,sources}/   # L1…L6 — the knowledge
brain/_backlog/<layer>.md                                  # deferred ideas (the pressure valve)
courses/<course-slug>/                                     # GENERATED lessons — outputs, not knowledge
tests/{retrieval-questions.md,audit-log.md}                # T1 questions (fixed), T3/T4 results
INDEX.md                                                   # retrieval entry point, sectioned by layer
```

## The note contract (KB_DESIGN_PROPOSAL §4)
Frontmatter on every note: `id · layer · status · confidence · decay · last_verified · sources · teaches`.

Domain-note body, in this order: **Claim → why our learner needs it → how we teach it → the misconception →
minimal example → assessment hook → sources.** A note that only states facts produces a lecture that reads like
Wikipedia; the teaching angle is what makes it a lesson.

## The NEVER list (violating any of these fails review)
- NEVER exceed **400 words** in a note (floor 150). The count holding while notes bloat defeats retrieval, which
  is the whole point of the structure.
- NEVER exceed a layer's note cap (L1 8–10 · L2 3–4 · L3 15–20 · L4 4–6 · L5 3–5). At cap: **merge two notes, or
  file the idea in `brain/_backlog/<layer>.md`.** NEVER raise a cap mid-build — that is a v1-review decision.
- NEVER write a domain note without a source in `brain/sources/`. Claims live in the note, source records live in
  L6.
- NEVER mark an L1 (pedagogy) or L2 (audience) note `verified` — they are opinions with no source to check
  against, so they top out at `reviewed` until a human who has taught signs them.
- NEVER grant `verified` from the session that authored the note. Verification is a **fresh** session, given the
  **source** and asked whether the source supports the claim — never asked whether the claim sounds right.
- NEVER put generated lesson prose in `brain/`. It goes in `courses/`. Mixing them makes retrieval return prose
  instead of principles, and the brain grows without getting smarter.
- NEVER write a domain note for something no planned lesson needs. L3 is scoped by the curriculum, never by the
  field. A note explaining what HTTP is competes with the model's own knowledge and loses.
- NEVER edit another layer to fit your own — propose the change to that layer's owner. Cross-layer edits are how
  a KB silently contradicts itself.
- NEVER use Dataview, Canvas, or plugin syntax. Obsidian is the human editing surface; the files are consumed by
  grep. Plain markdown + frontmatter only.
- NEVER name a file `note-042.md`. Filenames are the primary index — descriptive kebab-case keywords.
- NEVER add a note without adding its line to `INDEX.md` under that layer's section. A note that can't be
  retrieved does not exist.
- NEVER put a version number, price, or model name in a `decay: durable` note. Volatile facts go in
  `decay: volatile` notes so a refresh stays bounded.
- NEVER tune the KB to pass the ten retrieval questions in `tests/retrieval-questions.md`. They are fixed, and
  fitting the vault to them turns the only real test into theatre.

## Adding a note
1. Check the layer's cap and its backlog first — the idea may already be deferred, or a merge may be the answer.
2. Write it to the §4 contract, 150–400 words, `status: draft`.
3. Add the `INDEX.md` line under the right layer section.
4. Domain notes: add or reuse an L6 source record, then queue for a fresh-session verify pass.

## Working rules
- **The design is challengeable, the rules are not silently ignorable.** If the design is wrong, say so and
  propose a change to `KB_DESIGN_PROPOSAL.md` — do not work around it quietly. (Same norm as the
  `nexusbim-brain` repo: the brain is fallible, and disagreement is wanted output.)
- **Definition of done is the five tests, not a note count.** If T2 passes at 28 notes, v1 is done at 28.
- Record test results in `tests/audit-log.md` with the date. An untested claim of reliability is the exact
  failure this design exists to prevent.
