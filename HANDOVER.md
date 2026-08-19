# Handover — NexusLab Brain

**Written:** 2026-08-19 · **For:** whoever opens a fresh session in this folder, including future-you.
**Assume no prior context.** This document exists because the session that produced the design lived in a
different project directory, and none of its memory travels here.

---

## 1. What this repo is for

**NexusLab** is a learning platform (separate product; admin app at `../NexusCodeLabAdmin`). The team wants a set
of short, beginner-friendly tech courses on it — 2–4 weeks each, modern, AI-native — aimed at three audiences:

- a high-school or college student starting out,
- a career-switcher with some technical curiosity,
- **a salesperson with no technical background** who needs to understand web development and system architecture
  at an overview level.

Course ideas floated by the team: *"Claude 101 — Everything You Need To Know"*, *"Basic Fundamentals of Web System
Architecture"*, *"Get To Know Web Design & Development"*. Titles are placeholders; the charters are the real work.

**This repo is not the courses.** It is the knowledge base the courses are generated from — the reusable half. The
courses themselves land in `courses/`, generated from `brain/` by a fresh Claude Code session.

## 2. How we got here

- The original proposal was: use Claude Code + Obsidian to deep-research an "experienced IT & CS university
  professor" brain, then generate each course from it in a new session, and refresh both over time.
- That was reviewed and **accepted with two corrections** (§4), then a meeting on **2026-08-19** settled: build
  the knowledge base first, but **design it for reliability before building it.** That design is
  `KB_DESIGN_PROPOSAL.md`.
- The team explicitly does **not** want the courses rushed. Background and design first was a deliberate call, not
  a delay.

## 3. The reasoning that shaped the design

Do not re-derive this. A "professor brain" built by AI research and then used to generate courses has three
failure modes, and every structural choice in the proposal targets one of them:

1. **Unverifiable.** The dominant risk. AI-researched material is plausible, authoritative-looking, and hard to
   check. An error introduced during research gets repeated by every course generated from it, and nothing in the
   pipeline is positioned to catch it — least of all the same AI that wrote it. *Guards:* mandatory sources on
   domain claims, `status`/`confidence` labelling, a fresh-session source audit (T4), and a human sign-off gate on
   the layers that have no sources.
2. **Unbounded.** Research has no natural stopping point; every note suggests three more, each individually
   defensible. Sprawl never feels like sprawl — it feels like thoroughness, right up to week six with no course
   shipped. *Guards:* per-layer note caps, word caps, an overflow rule, backlog files, a timebox, and a
   stop-early condition.
3. **Unfindable.** Claude Code does not load a vault — it greps, globs, and reads whole files. A note that can't
   be retrieved does not exist. *Guards:* atomic notes, descriptive filenames, consistent frontmatter as the query
   language, a sectioned `INDEX.md`, and a fixed retrieval test.

**The load-bearing idea:** reliability means *testability*. "Reliable knowledge base" is an adjective everyone
agrees with and interprets differently, so the design's spine is five acceptance tests declared before any note
exists. Structure follows from the tests.

## 4. The two corrections to the original concept

Worth knowing, because they'll otherwise be re-proposed:

- **Scope the brain to what the model doesn't already know.** A general "IT & CS professor" brain is unbounded, and
  200 researched notes on what HTTP is duplicate what the model already has. The high-value notes are local and
  opinionated: who the learner is, what NexusLab can render, our voice, our examples, assessment patterns for a
  platform whose only primitives are multiple-choice and stdout matching, and the misconceptions our own pilot
  learners show. ~40 notes, not 300.
- **Give the brain a pass/fail test.** A fresh session, given only the vault, produces a lesson we'd ship without
  rewriting. When it can't, fix the brain, not the lesson. Without this, "build the professor brain" is an
  open-ended research project that feels productive and never converges.

## 5. Decisions

**Settled at the 2026-08-19 meeting — do not relitigate without proposing a change:**

| # | Decision |
|---|---|
| 1 | Knowledge base first, designed for reliability before built |
| 2 | Vault lives in **its own private repo** (this one), not inside `nexusbim-brain` |
| 3 | The KB is written in **English** |
| 4 | `status: verified` granted by a **second AI pass** for now — a human reviewer is wanted but has no time |

**Consequence of #4 that must not be lost:** an AI pass can check whether a cited source supports a claim, which
covers L3 well. It cannot verify L1/L2, which are opinions with no source. So **L1 and L2 notes top out at
`reviewed`** until a human who has taught signs them. The KB is fully usable that way — the risk is only that
someone later mistakes an opinion note for sourced fact.

**Open:**

| # | Open question | Blocks |
|---|---|---|
| 1 | Layer ownership: slot assignment across three people, and auditor as fourth-hat vs rotating (proposal §6) | multi-person work, not solo start |
| 2 | **Course language** (ja / en / both) — separate from the KB language, still undecided | L5 style notes |
| 3 | The CSS-lab fork: build a render/assertion lab type, or design that course around the limitation | course 3 only |
| 4 | Which single course v1 is scoped to | L3 domain notes |

If courses go Japanese, L5 must carry **Japanese exemplars inline** even inside English notes — translated
pedagogy phrasing loses exactly the nuance being captured.

## 6. Platform constraints (verified 2026-08-19)

Read from the admin app at `../NexusCodeLabAdmin`, in `src/types/{course,lab}.ts` and `src/constants/course.ts`.
**That path is outside this folder** — a session here needs it added as a working directory to re-verify.

- Hierarchy: **Curriculum → Course → Section → Lesson.**
- A lesson is exactly one of three things: **Lecture** (a single TipTap HTML blob) · **Quiz**
  (`multiple_choice` or `true_false` only, plus a pass rate) · **Lab** (Monaco + template code + language + test
  cases, graded by comparing stdout to expected output).
- **No free-text or human-graded submission type exists** anywhere in the model.
- `html` and `css` are in the lab language list, but grading compares stdout with no render or DOM assertion —
  **a CSS lab cannot be auto-graded.** This is open question #3.
- **SQL labs work properly** — a database module can be hands-on at no extra cost.
- Lecture content is stored as an HTML blob with **no markdown source**, which is why `courses/` here must be the
  authoring source of truth. Otherwise updating a course means hand-editing rich text in a browser forever, with
  no diff and no review.
- `i18n/locales/{en,ja}` exist and are empty.

## 7. Start here

The proposal's timebox (§8) puts the first two days on skeleton + seed notes, and **day 3 on running the tests
against a deliberately thin vault.** That ordering is the point — read it before deviating.

A first session, in order:

1. **Read** `KB_DESIGN_PROPOSAL.md` end to end. `CLAUDE.md` is already loaded and holds the enforceable rules.
2. **Decide open question #4** — which single course v1 is scoped to. Everything in L3 depends on it, and the
   budget assumes one course. Recommended: the architecture course, because it needs no CSS labs and can use SQL
   labs for a genuinely hands-on module.
3. **Create the skeleton** — the directory tree in `CLAUDE.md`, `INDEX.md` with its six layer sections, and an
   empty backlog file per layer.
4. **Copy the ten retrieval questions** from proposal §2.1 into `tests/retrieval-questions.md` and do not touch
   them again.
5. **Write 3 seed notes per layer**, to the §4 contract. Use the two worked examples in proposal §4.3 and §4.4 as
   the pattern — they are complete, not sketches.
6. **Run T1 and T2 on the thin vault. Expect failure.** A thin-vault failure is cheap and names exactly which
   layer is underfed. The same failure on day 8 against a full vault is expensive and ambiguous. Record the result
   in `tests/audit-log.md` with the date.
7. **Then fill to budget**, guided by what step 6 exposed — not by what feels incomplete.

**Solo-run warning:** the stop-early condition (proposal §7.2) matters most when nobody else is present to say
"that's enough." If T2 passes at 28 notes, stop at 28. The budget is a ceiling, not a quota.

## 8. What is settled vs. challengeable

The four decisions in §5 are settled; propose a change rather than working around them. **Everything in the design
proposal is challengeable** — including the note caps, the layer split, and the tests themselves. The norm carried
over from the team's `nexusbim-brain` repo: the brain is fallible, and disagreement is wanted output rather than
friction. Record dissent in the note or the proposal; never silently overwrite.

What is *not* optional is that a claim of reliability be backed by a test that ran. That is the one thing this
whole design exists to guarantee.

## 9. Glossary

| Term | Meaning |
|---|---|
| **L1 Pedagogy** | how we teach — archetypes, sequencing, assessment patterns, misconception catalog |
| **L2 Audience** | who we teach — the three personas, prior knowledge, time budget, failure modes |
| **L3 Domain** | what we teach — concept notes, scoped by the curriculum |
| **L4 Platform** | what NexusLab can hold, and its limits |
| **L5 Style** | how it sounds — voice, language policy, the things we never do |
| **L6 Sources** | the source register: id, title, URL, date accessed, licensing stance |
| **T1–T5** | the five acceptance tests: retrieval · sufficiency · contradiction sweep · source audit · cold reader |
| **`decay`** | `durable` (concepts) vs `volatile` (tool versions, prices, model names) — bounds refresh cost |
| **Overflow rule** | at a layer's cap: merge two notes, or defer to `brain/_backlog/<layer>.md`. Never raise the cap mid-build. |
