# Handover — NexusLab Brain

**Written:** 2026-08-19 · **For:** whoever opens a fresh session in this folder, including future-you.
**Assume no prior context.** This document exists because the session that produced the design lived in a
different project directory, and none of its memory travels here.

---

## 1. What this repo is for

**NexusLab** is a learning platform (separate product; monorepo at `../MyanLearn` =
`github.com/nexuscode-devs/myanlearn` — Laravel API + learner SPA + admin SPA. The `../NexusCodeLabAdmin` folder
is a stale detached fork of just the admin app; never cite it). The team wants a set
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

**Closed 2026-08-19** (all four; full reasoning in proposal §12):

| # | Was open | Decided |
|---|---|---|
| 1 | Layer ownership | **Solo now, staged later.** Proposal §6.4 states which guards survive, which are substituted, and which are labelled `UNMET` rather than faked. Auditor is **rotating, not fourth-hat** — fourth-hat would have slot C auditing the source register it wrote |
| 2 | Course language | **English for v1**, recorded as *English-authoritative, Japanese derived — deferred*. Reopen trigger is a **named person who reads Japanese** committing to be the T2 judge and T5 cold reader — not a date. The whole accommodation is one L5 note: every analogy must survive translation without a rewrite |
| 3 | The CSS-lab fork | **Deferred**, as an L4 note rather than a backlog line (backlogs are not in `INDEX.md`, so T1 never surfaces them). Trigger: the first charter proposing a "learner produces visual output" outcome. **Safe only while course 1 has no visual-output assessment** — a dependency this table previously hid |
| 4 | Which course v1 is scoped to | **The web-system-architecture course.** Recommendation kept, **stated reason rejected** — §7 recommended it for SQL labs, which are unverified. It wins on decay, reusability, and salesperson fit. **Labs are JavaScript** |

**Carried open, with owners** (proposal §12): how a *stored* lab grades a real submission — gates every lab, and
only the backend team can answer · `pass_rate` percentage vs raw count, contradictory in the codebase · whether SQL
labs execute at all · where lecture diagrams are hosted, since images are URL-only.

On language: the platform is already bilingual at the *chrome* level, which will keep making a Japanese course look
cheaper than it is. It is not — no locale field exists on any course object, so "both" means two full course trees
with no platform-level pairing, and the three lesson editors are the only un-translated screens in the app.

## 6. Platform constraints — **re-verified, and the first version was wrong**

**Read `KB_DESIGN_PROPOSAL.md` §11 for the authoritative version.** It is pinned to the platform monorepo
`nexuscode-devs/myanlearn` @ **`3d34a4e`** (`origin/develop`, 2026-07-29). The monorepo is at `../MyanLearn`,
**outside this folder** — a session here needs it added as a working directory, and must read via
`git show origin/develop:<path>` because the working tree is checked out at a January commit.

**This section was wrong twice before it was right, and the second failure is the one to remember.** The first
pass read TypeScript type files. The corrected pass read the editor components — of `../NexusCodeLabAdmin`, which
turned out to be a **detached fork of `apps/admin` frozen 2025-12-24**, seven months before the bilingual work
landed. Reading the right files in the wrong repo produces the same confident wrongness as reading the wrong
files. The 2026-08-24 re-verification against the real backend materially changed: `pass_rate` is a raw count ·
tables and mermaid render natively (the *editor* is the limitation, and destructive) · a curriculum is required
on course create · course/section creation requires Japanese titles · labs execute as Node.js regardless of their
stored language (bug, reported) · the full authoring API is token-scriptable.

**The method finding matters more than any single fact.** The first version of §11 was written from
`src/types/{course,lab}.ts` and `src/constants/course.ts` and was wrong in four material ways. The code had not
changed since 2025-12-24, so this was not drift — it was wrong on the day it was stamped "verified 2026-08-19".
**In that codebase the type files are consistently more optimistic than the code**, carrying fields and enum
members that no schema, component or wire contract ever reads. **The authoring UI is the tiebreaker. Read the
editor components.**

What changed:

| First version said | Actually |
|---|---|
| Quiz supports `multiple_choice` **or `true_false`** | **Multiple choice only, single-answer.** `true_false` occurs once in the codebase and nothing reads it. No multi-select either |
| `i18n/locales/{en,ja}` exist and are **empty** | **Fully populated** — 18 files, ~40KB, real Japanese, working en/ja switcher. But i18n covers admin chrome, **not course content**: no locale field exists on any course object |
| Lecture holds headings, images, **tables, links**, YouTube | **No tables, no link button.** The editor loads StarterKit + Heading + Image + Youtube; the Table and Link packages are installed but never registered |
| **SQL labs work properly** | **Unverified.** `sql` is one string in a flat dropdown beside the two known-broken entries. It also conflicts with the universal `function_name` requirement, since SQL has no function to name |
| Lab = graded by comparing stdout | Half right. Every lab **also requires a function name and a full reference solution, and stores neither** — so nobody can currently say how a *saved* lab grades a real submission |

Still true, and confirmed: the hierarchy (**Course → Section → Lesson**, with Curriculum optional, not mandatory) ·
a lesson is exactly one of Lecture / Quiz / Lab · no free-text or human-graded submission type is reachable ·
a CSS lab is impossible — in fact it cannot even be *authored*, not merely cannot be auto-graded · lecture content
is an HTML blob with no markdown source, which is why `courses/` here must be the authoring source of truth.

**Three limits §11 originally missed that reshape the pedagogy rather than merely bounding it:**

- **No per-question `explanation` field. The platform cannot tell a learner why they were wrong.** Corrective
  teaching has to be pushed into the distractors, so every wrong option must be self-diagnosing.
- **No prerequisites, gating, or locking**, and **unlimited quiz attempts** — sequence is presentational, so a quiz
  cannot gate progress and every lesson must restate its load-bearing prior idea rather than assume it.
- **Progress and analytics are hardcoded mock data.** There is no feedback loop from learners, so the misconception
  catalog must come from pilot sessions run by hand, not from platform evidence.

## 7. Start here

The proposal's timebox (§8) puts the first two days on skeleton + seed notes, and **day 3 on running the tests
against a deliberately thin vault.** That ordering is the point — read it before deviating.

**Day 0 is done** (2026-08-19): the repo is under git with the three original documents committed unmodified as
`baseline`, so every correction since is a reviewable diff. §11 was re-verified and rewritten, both worked examples
were corrected and demoted to `draft`, all four open decisions were closed, and §2.2's T2 rubric was fixed before
any note exists — which is the point of writing it then.

A first session, in order:

1. **Read** `KB_DESIGN_PROPOSAL.md` end to end, starting with the revision note at the top. `CLAUDE.md` is already
   loaded and holds the enforceable rules.
2. **Read `curriculum/web-system-architecture.md`** — the charter. Open question #4 is closed: v1 is the
   architecture course. Note that the *reason* given in the earlier version of this section was rejected — it
   recommended the course for its SQL labs, and SQL labs turned out to be unverified. The course still wins, on
   decay, reusability and salesperson fit. **Labs are JavaScript.**
3. **Write the seed notes** — and note the seeding is deliberately uneven: **2 for L2/L4/L5, 3 for L1, 4 for L3**,
   plus the L6 source records those L3 notes cite. Three per layer would complete L2, L4 and L5 outright *before*
   the day-3 diagnostic that is supposed to guide filling, which wastes the diagnostic. Use §4.3 and §4.4 as the
   pattern — but both are now `status: draft`, and copying an exemplar stamped `verified` is exactly how a
   self-verified note enters the vault.
4. **Run T1 and T2 on the thin vault. Expect failure.** A thin-vault failure is cheap and names exactly which layer
   is underfed. The same failure on day 8 against a full vault is expensive and ambiguous. Record it in
   `tests/audit-log.md` with the date and the auditor-prompt hash.
   **One sharpening:** make the T2 lesson the one most dependent on the KB's own opinion — *"why a schema change is
   not a text edit"* — **not** a section-1 lecture. Section 1 leans on the pre-worked §4.3 note and will pass for
   the wrong reason. The diagnostic is *which layer* the failure names.
5. **Then fill to budget**, guided by what step 4 exposed — not by what feels incomplete.
6. **Run `scripts/check-vault.py` before every commit.** The sibling repo is measured evidence (proposal §7.3) that
   the disciplines embedded in a mechanical check hold at 100% and the ones requiring the author to remember prose
   drift. This is the only enforcement either repo has.

**Solo-run warning:** the stop-early condition (proposal §7.2) matters most when nobody else is present to say
"that's enough." If T2 passes at 28 notes, stop at 28. The budget is a ceiling, not a quota.

**The two things to go and get from a human**, because no amount of solo diligence substitutes for them
(proposal §6.4):

1. **Twenty minutes of any non-author, to read three notes.** That clears T5 outright. A model asked to explain a
   note back is *anti-correlated* with what T5 measures — it already knows the domain, so it succeeds on exactly
   the notes a human finds impenetrable. Simulating T5 does not weaken it, it inverts it.
2. **The backend team's answer on lab grading.** `function_name` is mandatory to author and is never stored, so
   nobody can say how a saved lab grades a real submission — and that gates every lab in v1. Ask in the same
   message whether the runner has, or could gain, a DOM context; that answer prices the CSS-lab fork before its
   trigger ever fires.

## 8. What is settled vs. challengeable

The four decisions in §5's first table are settled; propose a change rather than working around them. The four in
the second table were *closed* on 2026-08-19 with reasoning in proposal §12 — reopen them by proposing a change,
not by treating them as still open. **Everything in the design proposal is challengeable** — including the note
caps, the layer split, and the tests themselves. Several things already were: T1's counting unit, T4's sample size,
§13's definition of done, §8's calendar arithmetic, and this document's own claim about what `nexusbim-brain`'s
dissent norm is. The norm carried
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
| **`verified_against`** | a **myanlearn** commit SHA on any note resting on a platform fact. A date stamp is unfalsifiable; a SHA makes staleness a `git diff` |
| **`review_by`** | a date on `decay: volatile` notes, so "due for re-verification" (retrieval question 9) has a computable answer |
| **The tripwire** | a deliberately corrupted claim planted in every T4 batch. If the batch passes it, the audit did not run — discard the batch and every stamp it would have granted (proposal §6.4) |
| **`UNMET`** | a dated row in `tests/audit-log.md` for a test that genuinely cannot run yet. The honest alternative to quietly loosening what *pass* means |
