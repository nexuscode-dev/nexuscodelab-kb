# NexusLab Knowledge Base — Design Proposal

**Status:** for team review
**Date:** 2026-08-19 · **revised same day** after re-verifying §11 against the admin app
**Scope:** how the knowledge base is built so it can be trusted. Not the knowledge base itself. The *scope* of the
curriculum now has a home (§3.3), but its content is still out of scope here.
**Read before:** writing the first note.

> **Revision note — 2026-08-19.** §11 was re-derived from the admin app's editor components rather than its type
> files and was **wrong in four material ways**: quizzes cannot do true/false, the i18n locales are fully
> populated, lecture tables are impossible, and "SQL labs work properly" is unsupported by anything in the repo.
> The code had not changed since 2025-12-24, so these were not staleness — they were wrong when stamped
> "verified". Two of the errors had already been copied into the worked examples in §4.3 and §4.4.
>
> Changed in consequence: **§11** rewritten and pinned to a commit SHA · **§2** T1's unit and T4's scope sharpened,
> plus a new **§2.2** T2 rubric fixed before any note exists · **§3.3** a curriculum charter, the artifact L3 is
> scoped by · **§4.1** three new frontmatter fields (`review_by`, `verified_against`, `depends_on`) · **§4.3/§4.4**
> both exemplars corrected and demoted to `draft` · **§6.3** the `nexusbim-brain` citation corrected, having been
> an extension presented as an inheritance · **§6.4** ownership while solo · **§7.3** enforce the contract in a
> script, with measured evidence from the sibling repo · **§8** the calendar conversion, which was ambiguous and
> read solo was off by ~2.4x · **§9** T4 audits all domain notes and logs every pass · **§12** all four open
> decisions closed, four new ones carried with owners · **§13** definition of done made reachable under solo
> without loosening what *pass* means.
>
> **Revision note — 2026-08-24.** §11 re-verified a second time, now against the actual platform monorepo
> (`nexuscode-devs/myanlearn`, `origin/develop` @ `3d34a4e`) — the 2026-08-19 pass had corrected §11 against
> `~/Desktop/NexusCodeLabAdmin`, which turned out to be a **detached fork of `apps/admin` frozen 2025-12-24**.
> Materially changed: `pass_rate` is a raw count (was "ambiguous, default percentage") · tables and mermaid
> diagrams render natively in lectures (was "tables are impossible") — the *editor* is the limitation, and it is
> destructive on re-save · a curriculum is **required** on course create (was "optional") · bilingual is 11
> nullable column pairs on one record, but course/section creation requires Japanese titles · labs run on managed
> RapidAPI Judge0 with `language_id` hardcoded to Node.js in the learner path (two platform bugs reported) · the
> full authoring API is token-scriptable. All four §12 carried-open questions are now answered.

---

## 1. The problem this design exists to solve

A "professor brain" built by AI deep research and then used to generate courses has one dominant failure mode:
it produces material that is **plausible, authoritative-looking, and unverifiable.** An error introduced during
research is repeated by every course generated from it, and nothing in the pipeline is positioned to catch it —
least of all the same AI that wrote it.

Two secondary failure modes matter almost as much:

- **It never converges.** Research has no natural stopping point. Every note suggests three more, and each of
  those is individually defensible. Sprawl never feels like sprawl; it feels like thoroughness.
- **It becomes unfindable.** Claude Code does not load a vault — it greps, globs, and reads whole files. A note
  that cannot be retrieved does not exist, no matter how good it is.

Everything below is aimed at those three: **unverifiable, unbounded, unfindable.**

---

## 2. Reliability means testability

"Reliable knowledge base" is an adjective everyone agrees with and interprets differently. So this design's spine
is the acceptance tests, declared up front. Once we agree on the tests, most of the structure follows mechanically.

| # | Test | Method | Pass condition |
|---|---|---|---|
| T1 | **Retrieval** | 10 fixed questions a course author would really ask (§2.1) | a fresh session cites the registered note path in ≤3 retrieval steps, 9/10 |
| T2 | **Sufficiency** | fresh session, vault only, write one named lesson | shippable without a rewrite — judged against the §2.2 rubric |
| T3 | **Contradiction sweep** | fresh session whose *only* job is to find conflicting claims | zero conflicts |
| T4 | **Source audit** | every domain note; check the source actually says it, quote-or-NO | no drift, plus the §6.4 tripwire caught |
| T5 | **Cold reader** | a human who didn't build the KB reads 3 notes | can explain the concept back |

Three refinements to the wording above, each closing a way a test could pass without meaning anything:

- **T1 counts retrieval steps, not tool calls,** because one shell call can chain five greps. A chained command
  counts one step per distinct search. And the pass condition is *citing the registered path* from
  `tests/retrieval-questions.md`, not answering correctly — a fresh session can answer most of these from its own
  knowledge without opening the vault at all, which would score 9/10 on an empty repo.
- **T4 audits every domain note, not a sample of 10.** §9's sampling rationale was written for a bigger layer than
  L3 actually is: against a cap of 15–20, ten notes is 50–67% of the layer, so sampling buys nothing and costs the
  certainty. What T4 samples instead is *itself* — see the tripwire in §6.4.
- **T2 needs a named lesson and a written rubric before it can be run at all.** See §2.2.

**T2 is the headline test.** The others catch the specific ways a KB rots. A KB that passes T2 and fails T3 will
produce good lessons that quietly disagree with each other.

Every test is run by someone who did not author the layer under test. A layer owner testing their own layer
reproduces the AI-reviewing-AI problem one level up, at the human level. **While the build is solo this is only
partly achievable — §6.4 states exactly which tests keep their force, which are substituted, and which are
labelled `UNMET` rather than faked.**

### 2.2 T2's rubric — written before any note exists

T2 is the headline test and the one most easily passed by a generous reader. Pre-registration is the only
non-author standard a solo build has, so the rubric is fixed now, while nobody is invested in the outcome.

**Fixed before day 1:** one persona (**the salesperson**), one lesson type (**Lecture** — it exercises L1, L2, L3
and L5 at once, where a Quiz or Lab mostly exercises L4), and one named lesson from the course charter.

Each line names the layer accountable for it, so a failure attributes itself instead of reading as "the lesson was
a bit weak":

| # | The generated lesson… | Accountable |
|---|---|---|
| 1 | introduces at most the permitted number of new ideas | L1 |
| 2 | assumes only what the persona note says the learner knows | L2 |
| 3 | uses our analogy for each concept, not a generic one | L1 + L3 |
| 4 | pre-empts the misconception the domain note names | L3 |
| 5 | sounds like us — no hedging, no "in today's fast-paced world" | L5 |
| 6 | fits what a lecture body can hold — HTML via the API: tables, links and mermaid are fine; nothing that needs the admin editor to survive a re-save | L4 |
| 7 | ends in an assessment that is a single-answer scenario MCQ with self-diagnosing distractors | L1 + L4 |
| 8 | **every factual claim traces to a note id** | L3 + L6 |
| 9 | **contains no fact that is not in the vault** | — |
| 10 | needs no rewrite before it could be published to the platform via the API | overall |

Lines 8 and 9 are mechanically checkable and catch T2's real failure mode: a lesson that reads beautifully because
the model filled the gaps from its own knowledge, which is precisely the thing the vault is supposed to be tested
for.

### 2.1 The ten retrieval questions (fixed — do not tune the KB to them after the fact)

1. What analogy do we use to explain what a server is?
2. What does our salesperson persona already know, and what will they never need?
3. How long is a lesson, and how many new ideas may one lesson introduce?
4. What can a NexusLab lab actually grade?
5. What's the common misconception about frontend vs backend, and how do we pre-empt it?
6. How do we write a quiz question that tests understanding rather than recall?
7. Where do we stand on introducing AI tooling before or after the manual mental model?
8. What is our source for the claim that X? (pick any domain note)
9. Which notes are volatile and due for re-verification?
10. What did we deliberately decide *not* to teach in course 1?

If a fresh session can't answer these from the vault, the vault isn't done — regardless of note count.

---

## 3. Repository layout

Decided: **its own private repo**, not a folder inside `nexusbim-brain`.

```
nexuslab-brain/
  KB_DESIGN_PROPOSAL.md      # this file
  INDEX.md                   # the retrieval entry point — one line per note, sectioned by layer
  brain/
    pedagogy/                # L1  how we teach
    audience/                # L2  who we teach
    domain/                  # L3  what we teach
    platform/                # L4  what the platform can hold
    style/                   # L5  how it sounds
    sources/                 # L6  the source register
    _backlog/                # one file per layer — the pressure valve (§7)
  curriculum/
    <course-slug>.md         # the course charter — what L3 is scoped BY (§3.3)
  courses/
    <course-slug>/           # generated lessons: the source of truth for what's published
  tests/
    retrieval-questions.md   # T1, fixed — now with a registered answer path per question
    audit-log.md             # test results, dated, plus the standing UNMET block (§6.4)
    auditor-prompts/         # versioned T1/T3/T4 prompts — the re-instantiable substitute for a person
  scripts/
    check-vault.py           # the contract validator (§7.3)
```

**`brain/` and `courses/` are siblings, never mixed.** Generated lessons are *outputs* of the brain, not part of
it. Mixing them does two kinds of damage: retrieval starts returning lesson prose instead of principles, and the
brain grows without getting smarter. This split also gives a clean versioning answer — `courses/` is the source of
truth for what is published on NexusLab, `brain/` is the source of truth for *why it is written that way*.

### 3.3 The curriculum charter — the artifact L3 is scoped by

§5 scopes L3 "by the curriculum, never by the field", and §7 caps it at 15–20 notes on that basis — but the
original layout held no curriculum anywhere, because this document declared the curriculum out of its own scope.
That was a correct scope boundary for a *design* document and a gap for a *builder*: without the artifact, "scoped
by the curriculum" has no referent, `teaches:` has nothing to point at, T2 has no named lesson to generate, and
retrieval question 10 ("what did we deliberately decide *not* to teach in course 1?") is structurally
unanswerable.

`curriculum/<course-slug>.md` is a sibling of `brain/` and `courses/` — it is neither knowledge nor output, it is
the scope decision. It holds: the working title, the target persona, the length, a section-by-section lesson list
naming which primitive carries each lesson, the outcomes, and an explicit **"Out of scope, and why"** section.
That last section is not documentation courtesy; it is the answer to a fixed test question. It gets its own
`INDEX.md` section and is exempt from the note word caps — it is a charter, not a note.

### 3.1 Why the vault must stay plain markdown

Obsidian is the human editing surface. The files are consumed by grep. So:

- **No Dataview, no Canvas, no plugin syntax.** All noise to a text reader.
- **Frontmatter is the query language.** Consistent fields let `grep` do what a database would; inconsistent
  fields make it useless.
- **Filenames are the primary index.** `why-the-browser-cannot-reach-the-database.md`, never `note-042.md`.
- **Wikilinks are for humans and the graph.** Claude follows them only when told to, so link deliberately.

### 3.2 INDEX.md format

```markdown
## L1 Pedagogy
- [one-new-idea-per-lesson](brain/pedagogy/one-new-idea-per-lesson.md) — the ceiling on new concepts per lesson, and why (reviewed · durable)

## L3 Domain
- [why-the-browser-cannot-reach-the-database](brain/domain/why-the-browser-cannot-reach-the-database.md) — the trust boundary that defines frontend vs backend (verified · durable)
```

Sectioned by layer so appends don't collide. **The index is the real merge hotspot** — atomic notes barely
conflict, a shared one-line-per-note index does constantly.

---

## 4. The note contract

### 4.1 Frontmatter

```yaml
---
id: why-the-browser-cannot-reach-the-database
layer: domain              # pedagogy | audience | domain | platform | style | source
status: draft              # draft | reviewed | verified   (see §9)
confidence: high           # high | medium | low
decay: durable             # durable | volatile
last_verified: 2026-08-19
review_by: 2026-11-17      # REQUIRED on `decay: volatile` notes; omit on durable ones
verified_against: 3d34a4e  # REQUIRED where the claim rests on the platform — a myanlearn commit SHA, not a date
sources: [src-mdn-http-overview]
teaches: [web-architecture/module-2]    # empty = not yet backing any course
depends_on: []             # note ids this note's argument rests on — grep-able, unlike wikilinks
---
```

**Three fields added after the §11 re-verification**, each fixing something the design asked for and had no
mechanism for:

- **`review_by`** — retrieval question 9 asks which notes are "due for re-verification", and the design defined no
  interval, so "due" had no meaning. Set at authoring time on volatile notes; 90 days is a fine default. Q9 is
  then one grep with an unambiguous answer, and §10's staleness guard gains the trigger it lacked.
- **`verified_against`** — a date stamp is unfalsifiable. §11 was stamped "verified 2026-08-19" against code last
  touched 2025-12-24 and was wrong in four material ways; a SHA makes staleness a `git diff` instead of a
  judgement. Required on any note whose claim rests on the platform — and the SHA is of the **monorepo**
  (`nexuscode-devs/myanlearn`, read at `origin/develop`), never of the deprecated `NexusCodeLabAdmin` fork.
- **`depends_on`** — nothing linked a pedagogy or domain note to the platform fact underneath it, so changing an
  L4 note could silently invalidate an L1 rule. Before changing any L4 note, run
  `grep -rl "depends_on:.*<that-id>" brain/` and file the hits. Solo, that grep is the entire mechanism, and it
  costs one command.

### 4.2 Body contract — domain notes

**Claim → why our learner needs it → how we teach it → the misconception → minimal example → assessment hook → sources.**

This contract matters more than the frontmatter. A note that only states facts produces a lecture that reads like
Wikipedia. A note carrying the *teaching angle* produces a lesson. That is the entire difference between a research
pile and a professor's brain.

**Length: 150–400 words.** This cap is part of the budget, not a style preference — see §7.

### 4.3 Worked example — a domain note

```markdown
---
id: why-the-browser-cannot-reach-the-database
layer: domain
status: draft              # an exemplar inside the design doc; `verified` is granted by a fresh session (§9), never here
confidence: high
decay: durable
last_verified: 2026-08-19
verified_against: n/a      # L4-dependent notes pin a myanlearn commit SHA here; see §4.1
sources: [src-mdn-http-overview, src-owasp-top10-a01]
teaches: [web-architecture/module-2]
---

**Claim.** A browser never talks to a database directly. It talks to a server, and the server talks to the
database.

**Why our learner needs it.** This is the load-bearing distinction behind "frontend" and "backend". Get it here
and half the architecture vocabulary stops being arbitrary.

**How we teach it.** Not the restaurant-order analogy — it implies queueing, which isn't the point, and learners
over-extend it. Use a **bank teller**: you can ask for your balance, but you cannot walk into the vault. The
teller checks who you are, decides what you're allowed, then goes in on your behalf. The vault has no public
door on purpose.

**The misconception to pre-empt.** Beginners learn "frontend = display, backend = logic". That's a description,
not a boundary, and it collapses the moment they see validation happening in both places. The sharper line is
**trust**: the frontend runs on a machine we do not control, so nothing it sends can be believed. The backend is
the first place we can trust anything.

**Minimal example.** View source on any site. The database password is not there. That isn't an oversight the
developers got right — there is nowhere in the browser it *could* live safely, because everything the browser
holds, the user holds.

**Assessment hook (single-answer MCQ, scenario form).** "A login form has a hidden field `role=user`. Which of
these can the user change before it reaches the server?" — tests the trust boundary rather than the vocabulary.
Every distractor is a real misconception from the catalog, because the platform has no `explanation` field and
nothing follows the click (§11.3).

**Sources.** `src-mdn-http-overview` (client/server request model) · `src-owasp-top10-a01` (the trust boundary and
why client-supplied authorization cannot be believed).
```

> **Note on this exemplar.** It is `status: draft` deliberately. Copying an exemplar stamped `verified` is how a
> self-verified note enters the vault, which CLAUDE.md forbids. Before it is used as a seed note its claim must
> survive one fresh-session T4 pass, and the result pasted here.

### 4.4 Worked example — a pedagogy note

```markdown
---
id: scenario-mcqs-over-recall-mcqs
layer: pedagogy
status: reviewed          # opinion — cannot reach `verified` under §9
confidence: high
decay: durable
last_verified: 2026-08-19
sources: []
teaches: []
---

**Rule.** Every quiz question describes a situation and asks for a judgement. None asks for a definition.

**Why.** A single-answer multiple choice question is the *only* question type NexusLab can author — no
true/false, no multi-select, and no per-question explanation, so nothing follows the click (see
[[nexuslab-lesson-primitives]], §11.3). Recall questions are what that constraint tempts you into, and they
measure whether the learner read the page. Scenario questions measure whether the model in their head works.

**Form.** Symptom → "which layer is at fault?" · artefact → "what happens next?" · change → "what breaks?"

**Anti-examples.** "What does API stand for?" · "Which of these best defines statelessness?" — both pass a
learner who understood nothing.

**Rewrites of those two.** "The page shows yesterday's price after you clicked refresh. Which is the likeliest
cause?" · "You log in, then open a second tab and you're logged in there too. What must be travelling with the
second tab's requests?"

**Distractor rule — load-bearing, not stylistic.** Every wrong answer is a real misconception from the catalog,
never filler. On this platform the rule is stronger than good practice: there is **no `explanation` field**, so a
wrong answer is the *only* teaching a mistake ever receives. Each distractor must therefore be self-diagnosing —
a learner who picks it should be able to see which belief led them there. A wrong answer nobody would pick
teaches nothing and makes the question easier than it looks.
```

---

## 5. The six layers

| Layer | Holds | Explicitly does **not** hold |
|---|---|---|
| **L1 Pedagogy** | lesson archetypes, sequencing rules, outcome verbs, assessment patterns for an MCQ+stdout platform, misconception catalog, cognitive-load rules | subject matter |
| **L2 Audience** | the three personas, prior knowledge, weekly time budget, motivation, how each fails | teaching technique (that's L1) |
| **L3 Domain** | concept notes **scoped by the curriculum**, each with source + teaching angle + misconception | anything no planned lesson needs |
| **L4 Platform** | NexusLab primitives and their limits, verified against the platform monorepo (`myanlearn`) | course content |
| **L5 Style** | voice, language policy, code style, the things we never do | rules about *what* to teach |
| **L6 Sources** | the register: source id, title, URL, date accessed, licensing stance | claims (claims live in the note that cites the source) |

**L1, L2, L4 and L5 are where reliability is created.** They hold what the model cannot know or invent: our
learner, our voice, our platform, our judgement. **L3 is where sprawl lives** — it must be scoped by the
curriculum, never by the field. A note explaining what HTTP is competes with the model's own knowledge and loses.

### 5.1 What never goes in the vault

Raw source dumps · encyclopedic explanations of well-known public material · tool version numbers and prices
inside `durable` notes (they belong in `volatile` notes, isolated) · generated lesson prose (that's `courses/`).

---

## 6. Ownership

**Owner ≠ sole author.** An owner is the single point of coherence for a layer: they review everything that
enters it and are accountable for it not contradicting itself. Anyone may draft into any layer by PR; the owner
decides whether it lands.

This is not bureaucracy. A knowledge base has no compiler. If two people independently write pedagogy notes they
*will* disagree — one writes a sequencing rule assuming prior knowledge another's persona note says the learner
lacks — and **nothing will tell us.** Generation then silently picks one. Ownership is the only cheap mechanism
that catches this class of fault.

### 6.1 Slots — grouped by coherence risk, not by equal volume

| Slot | Layers | Why grouped | ~Notes | Skill |
|---|---|---|---|---|
| **A** | L1 + L2 | the same act of judgement; splitting them is the likeliest source of contradiction | 12 | teaching instinct, opinion |
| **B** | L3 | the volume job; most AI-assistable and most auditable, since every claim has a source | 18 | breadth, research discipline |
| **C** | L4 + L5 + L6 | platform is small and verifiable against code; style needs *one* voice, so one author; sources is a register the others feed | 10 | verification, provenance |

### 6.2 The role nobody thinks to assign

**Auditor** — runs T1, T3 and T4 against layers they did not write. Two workable arrangements, and the choice
should be made explicitly rather than by default:

- **Fourth hat on slot C** (C is lightest, so it fits). Cost: C's own platform/style notes go unaudited unless A
  spot-checks them.
- **Rotating** — each person audits the slot to their left. No unaudited layers, but nobody is accountable for
  test quality either.

### 6.3 Four cross-layer rules

1. **No cross-layer edits without the owner's review.** A domain note needing a new pedagogy rule proposes it to
   A; it does not add it. This single rule prevents most drift.
2. **INDEX.md is sectioned by layer** so appends don't collide.
3. **Dissent is recorded, never silently overwritten** — the brain is fallible, and disagreement is wanted output
   rather than friction. *Citation corrected 2026-08-19:* this was previously described as "the norm already agreed
   for `nexusbim-brain`", recording dissent *inside* the note. Neither that phrase nor any rule stating it exists
   in that repo — it was our extension presented as an inheritance. What that repo actually does is stronger as
   evidence and different in shape: dissent lives in **dated standalone artifacts** — self-indicting audits, a
   pre-mortem note arguing its own thesis is wrong, owner-question logs, and a commit whose subject line is a
   retraction. Adopt the practised form, which has the track record: dissent as dated standalone documents,
   indexed, that the notes link to. Reserve in-note caveats for a single sentence pointing at the artifact.
4. **Owner rotation is a v2 question.** Not designed now.

---

### 6.4 Ownership while solo (decided 2026-08-19)

§6 assumes three people and an auditor. v1 is being built solo, so this section states which guards survive, which
are substituted, and which are **unmet** — because the alternative is that "all five tests pass" gets satisfied by
quietly loosening what *pass* means, which is the one failure this whole design exists to prevent.

The design conflates two different needs behind "someone who did not author the layer". One is a **different
context**, needed to catch *error*, where something outside both heads settles it — a source, a file, the vault.
The other is a **different mind**, needed to catch *bad judgement*, where nothing external can. **Solo breaks only
the second, and only in two places.**

**Survives intact — no substitute needed.** T1 (a fresh session is genuinely naive about our filenames; the pass
condition is counted, not judged) · T3 (whole-vault read against itself; author knowledge does not help) · T4 (§9
already decided `verified` comes from a fresh AI pass, so the second person was never in this test) · the §9
ceiling holding L1/L2 at `reviewed` (already waiting on "a human who has taught", who does not exist either way) ·
all of §7's caps and §8's timebox, which are arithmetic rather than social.

**Evaporates silently — the dangerous list, because nothing announces these.** "Owner ≠ sole author" inverts
completely: owner = sole author on all six layers, so nothing is reviewed on entry · "draft by PR, the owner
decides whether it lands" · §6.3 rule 1, no cross-layer edits, becomes self-review — and worse than nothing,
because a solo builder can bend an L1 rule to rescue an L3 note and leave no trace · §6.2's auditor
accountability, which presupposes ≥3 people.

**Cannot be substituted — label `UNMET`, never fake.**

- **T5, the cold reader.** A model asked to explain a note back is *anti-correlated* with what T5 measures: it
  already knows the domain, so it succeeds on exactly the notes a human finds impenetrable. A simulated T5 is not
  a weak test, it is a test that reports the opposite of the truth. **But T5 needs a reader, not a collaborator** —
  20 minutes of any non-author clears it. Borrow one; do not simulate one and do not declare it impossible.
- **T2's verdict half.** The generation half is genuinely fresh. The judgement half is contaminated, because the
  author reads past gaps their own memory fills. Records as **T2-partial** against the §2.2 rubric until a second
  reader exists.

**The six substitutions, mechanically.**

1. **`git init` before the skeleton.** Solo, the commit graph *is* the ownership mechanism. One commit touches one
   `brain/<layer>/` plus `INDEX.md`; a commit spanning layers must be titled `cross-layer:` and name in its body
   what it changed elsewhere and why. `git log --format=%s | grep cross-layer` is then the drift report §6.3
   rule 1 was buying with a person.
2. **Versioned auditor prompts, not ad-hoc asks** — `tests/auditor-prompts/`, committed. The substitute for a
   person is an auditor you can re-instantiate identically; each audit-log entry records the prompt file's hash.
3. **Run T4 from outside the repo.** `CLAUDE.md` auto-loads for any session opened in this folder and hands over
   the note contract, the layer model and the design's intent — priming agreement. That is fine for T1 and T2
   (the real generation session will have it too) and fatal for T4. T4 runs in a scratch directory with no repo
   access, given only the extracted claim sentence and the source text, and asked §9's question: **does this
   source state this — quote the sentence that does, or answer NO.** Quote-or-NO makes agreement expensive and
   disagreement cheap, and the stored quote stays checkable by a human later.
4. **The tripwire — the highest-value solo mechanic.** Every T4 batch carries one extra claim the builder has
   deliberately corrupted: flip a number, a direction, or a negation. **If the batch passes everything including
   the corrupted claim, the audit did not run — discard the whole batch and every stamp it would have granted.**
   Two minutes per audit, and it tests the test, which is the thing nobody checks.
5. **Status-upgrade gate.** No commit may change a `status:` line without also touching `tests/audit-log.md`.
   `git show --stat` proves it. This makes "a claim of reliability is backed by a test that ran" literally true of
   the commit graph rather than a stated intention.
6. **The T2 rubric fixed on day 0** (§2.2), before any note exists.

**Why this is not theoretical.** §11 was stamped "verified 2026-08-19" and was wrong in four material ways against
code unchanged since 2025-12-24 — because the verification read the type files and never opened the editors. That
is a solo verification failure that already happened in this repo, before a single note existed, and it was
*error*, not judgement — exactly the class a fresh session fixes and a second mind is not required for.

**When people join.** Keep §6.1's grouping; the §11 failure confirms why C is grouped as it is. Assign **slot C
(L4+L5+L6) to whoever wrote the admin app's lab and quiz editors and its i18n setup** — the one person who would
have caught every §11 error on sight, in minutes. Slot A (L1+L2) stays with the KB author, who also **owns
`tests/`**. Slot B (L3) goes to the third joiner: §6.1 calls it the volume job and the most AI-assistable, which
makes it the right slot for the least-contexted person, because every claim carries a source that makes the work
auditable by someone else. **Recruit in that order** — the marginal value is steeply ordered, and "three people"
is not a precondition for anything except §13's done call.

**Auditor: rotating, with one amendment. Fourth-hat-on-C is structurally wrong** — L6 *is* the source register and
T4 *is* the source audit, so C would be auditing the provenance records C wrote. That is §2's AI-reviewing-AI
problem reproduced at the human level and applied to the highest-risk test. Rotate left: **A audits C, C audits B,
B audits A.** The pairings also hold on skill — the verification specialist audits the sourced layer where T4
bites; the persona owner audits platform and style, which is the real check on whether L4's constraints match what
L1 assumes; B audits the opinion layers, which need no domain expertise because §9 caps them at `reviewed` anyway.
**The amendment fixes §6.2's stated cost of rotating** ("nobody is accountable for test quality") rather than
accepting it: **own the test artifacts, rotate the test running.** A owns `tests/` — the fixed ten questions, the
auditor prompts, the pass rules, the log format. Accountability for test quality then has a name, and no layer is
ever audited by its owner.

## 7. Note budget

A pre-declared cap, fixed **before research starts, while nobody is invested.** It converts "are we done?" from a
judgement call made under sunk-cost pressure into an arithmetic check.

| Layer | Notes |
|---|---|
| L1 Pedagogy | 8–10 |
| L2 Audience | 6–8 |
| L3 Domain | 12–15 |
| L4 Platform | 4–6 |
| L5 Style | 3–5 |
| L6 Sources | register — a ledger, doesn't count against the cap |
| **Total** | **≈ 40, hard cap for v1** |

### 7.1 The four mechanics that make it real

Without these it is decoration:

- **Per-layer, never global.** A global cap gets eaten by whoever writes fastest, which is always L3.
- **Word cap 150–400 per note.** This is the loophole to close explicitly: otherwise the count holds while the
  notes bloat, which defeats retrieval — the thing the whole structure exists to protect.
- **Overflow rule.** At cap you may either merge two existing notes or file the idea in that layer's backlog. You
  may **not** raise the cap mid-build; that is a decision at the v1 review.
- **A backlog file per layer is mandatory.** It is the pressure valve. Without it, people smuggle content into
  existing notes — worse than a new note, because it makes notes non-atomic and degrades retrieval for everything.

### 7.2 Stop-early condition

**If T2 passes at 28 notes, we stop at 28.** The budget is a ceiling, not a quota. Left unsaid, every team treats
a budget as a target and fills it.

---

### 7.3 Enforce the contract in a script, not in a rule

Measured across the team's `nexusbim-brain/bim-vault` on 2026-08-19 — 172 notes built under a documented contract
much like this one:

| What was documented there | What actually happened |
|---|---|
| A four-state maturity ladder (planned → seed → developing → mature) | 167 `developing`, 4 `planned`, **0 `seed`, 0 `mature`** |
| A seven-part mandatory body contract | mean note **667 words**; **95% over 400**; frontmatter **100% complete** |
| A `## Sources` section on every note | **143 of 172** notes carry an unverified-claim flag |
| A continuously updated knowledge base | vault frozen **2026-08-05**; the spec-attached half still moving 2026-08-10 |

Two conclusions, and they are the most useful thing in that repo:

- **The rule that lived inside a copy-pasted template block held at 100%. The rules that required the author to
  remember prose drifted.** §4.2 calls the body contract "more important than the frontmatter" — that is direct
  evidence the more important half is the one with no defense.
- **A status ladder that nothing outside the authoring session can promote becomes 100% present and 0%
  informative.** `draft → reviewed → verified` collapses the same way unless the §9 verify pass actually runs and
  writes back. The verify pass is not a nicety in this design; it is the only thing keeping the field meaningful.

Neither repo has any CI, linter, or validator to copy, so this one gets written. `scripts/check-vault.py` fails on:
a note under 150 or over 400 words · frontmatter missing a required key · a domain note with empty `sources:` · a
layer over its cap · a note with no `INDEX.md` line · a `status:` change in a commit that does not also touch
`tests/audit-log.md`. Roughly 30 lines, and it converts every rule above from an intention into a gate.

## 8. Timebox

**Design: 2 days** — schema, tests, layers, ownership, budget. Output is this document, agreed.

**v1 build: 8 working days**, sequenced deliberately:

| Day | Work |
|---|---|
| 1–2 | repo skeleton, INDEX, and **3 seed notes per layer** — test the schema against reality before scaling it |
| 3 | run T1 + T2 on the deliberately thin vault. **They will fail. That is the point.** |
| 4–7 | fill to budget, guided by what day 3 exposed |
| 8 | full five-test pass, including the second-AI source audit |

**Day 3 is the load-bearing day.** A thin-vault failure is cheap and diagnostic — it names exactly what's
missing. The same failure on day 8 against a full vault is expensive and ambiguous.

**Calendar conversion, stated honestly.** The earlier figure here ("2.5–3 calendar weeks at ~25% capacity") did
not say whether the 8 days were one person's serial effort or ~8 person-days split across the three §6.1 slots,
and the two readings differ by ~2.4x. Stated for both:

| Reading | Arithmetic | Elapsed |
|---|---|---|
| **Solo at ~25% capacity** — the current condition (§6.4) | 8 ÷ 0.25 = 32 working days | **~6.5 calendar weeks** |
| Solo at ~50% capacity | 16 working days | ~3 calendar weeks |
| Three slots in parallel at ~25% each | ~2.7 person-days each | ~2–2.5 calendar weeks |

**Quote the calendar number to the team, and say which reading it assumes** — "8 days" will otherwise be heard as
calendar days. This matters beyond the quote: at ~6.5 weeks the gap between day 2 and day 3 is nearly three
weeks, which destroys the context that makes the day-3 diagnostic cheap. If v1 is genuinely solo, either accept
the ~6.5-week number or raise the capacity — but do not quote 2.5–3.

---

## 9. Verification policy

Decided: **`verified` is granted by a second AI pass for now.** A human reviewer is wanted but has no time.

Rules that make that decision honest:

- The verifying session must be **fresh** — no memory of authoring the note.
- It is given **the source**, and asked whether the source supports the claim. It is *not* asked whether the
  claim sounds right. Asking a model to agree with a plausible claim is not a test.
- **L1 and L2 notes top out at `status: reviewed` and can never reach `verified`.** They are opinions with no
  source to check against; an AI pass cannot verify them. They stay `reviewed` until a human who has taught
  signs them. This is a labelling discipline, not a blocker — the KB is fully usable with L1/L2 at `reviewed`,
  as long as nobody later mistakes them for sourced fact.
- **T4 audits every domain note, and samples itself instead.** *Corrected 2026-08-19:* the original rule sampled
  10 notes on the rationale that "exhaustive audit costs more than it returns" — but against §7's cap of 15–20,
  ten notes is 50–67% of the layer, so sampling saved almost nothing and gave up the certainty. What needs
  sampling is the *auditor*, which is what §6.4's tripwire does.
- **Every verify pass is logged**: note id · source id · verdict · quoted supporting sentence · date · auditor-prompt
  hash, in `tests/audit-log.md`. Without a record, "granted by a fresh session" is unfalsifiable — and §3's
  original scoping of the log to "T3/T4 results" left the per-note verify pass as the one activity in the design
  with no mandated evidence.
- **L6 source records carry a `quote:` field** holding the exact supporting sentence. This makes verification
  checkable offline, makes source drift detectable when a URL changes underneath us, and is an explicit carve-out
  from §5.1's ban on raw source dumps — one sentence per claim is a citation, not a dump.

---

## 10. Failure modes and guards

| Failure | Guard |
|---|---|
| Sprawl — infinite research, no convergence | §7 budget, §8 timebox, L3 scoped by curriculum |
| Contradiction drift (silent) | one owner per layer, atomic notes, T3 sweep |
| Hallucination baked in, then repeated by every course | mandatory sources on domain claims, `confidence` + `status`, T4 |
| Staleness | `decay` + `last_verified` + **`review_by`** (§4.1) and **`verified_against`** a commit SHA, so "due" and "stale" are both computable rather than judged; volatile content isolated so a refresh is bounded |
| The right note exists but is never found | INDEX.md, filename discipline, T1 |
| AI reviewing its own work | fresh verifying session, source-first questioning, human sign-off gate on L1/L2 |
| The KB nobody updates | tie the update ritual to course revision — something that already happens — never a standalone discipline. **Note the platform gives no help here:** progress and analytics are mock data (§11.1), so the misconception catalog cannot be refreshed from learner evidence and must come from pilot sessions run by hand. Measured precedent: in `nexusbim-brain` the spec-attached half of the KB stayed alive while the standalone-research half froze dead (§7.3) |

---

## 11. Platform constraints (input to L4)

**Re-verified 2026-08-24 against the platform monorepo `nexuscode-devs/myanlearn`, `origin/develop` @ `3d34a4e`
(committed 2026-07-29).**

**Read the system of record.** This section has now been wrong twice, for graduated versions of one mistake. v1
read the TypeScript *type files* — which invent fields nothing implements. v2 read the *editor components* — but
of `~/Desktop/NexusCodeLabAdmin`, which turned out to be a **detached fork of `apps/admin` frozen 2025-12-24**,
seven months before the bilingual migrations landed. **Never cite that folder again.** The monorepo is the only
source, with a precedence order inside it: the **backend** (`database/migrations`, `app/Http/Requests`,
`app/Http/Controllers`, `app/Services`) is authoritative for what the platform *is*; `apps/admin` editor
components only for what a human author can do in the UI; type files never — five documented divergences so far
(`explanation`, `points`, `attempts_allowed`, `true_false`, `QuizStats`).

### 11.1 Structure

- Hierarchy: **Curriculum → Course → Section → Lesson**, and **`curriculum_id` is required on course create**
  (`CourseController/CreateRequest.php:22`) — the fork-era claim that a course can exist without a curriculum was
  wrong. v1 therefore needs one curriculum record: single-language by design, thumbnail image required, and
  created by **the same account that will author under it** — row-level ownership 403s everything else
  (`app/Services/OwnershipService.php`).
- A lesson is exactly one of **Lecture (1) · Quiz (2) · Lab (3)** (`category`, validated `in:1,2,3`).
- **No draft state anywhere.** Everything saved is immediately live to learners.
- No prerequisites, gating, or locking; sequence is presentational. `order` is explicit (per-section for lessons)
  and dedicated reorder endpoints exist.
- No free-text or human-graded submission type is reachable.
- **The admin analytics/progress pages are mock, but the data is real**: `course_progress`, `lesson_progress`
  (unique per learner), `code_executions`, certificates. However **quiz submissions are never persisted** — per-
  question accuracy and distractor-selection rates are unobtainable from this platform. The `lesson_questions`/
  `lesson_answers` Q&A API exists but is unused by both frontends (one endpoint is broken); per-lesson
  learner↔instructor `chats` is the only live free-text signal about learner confusion.

### 11.2 Lecture

- One HTML blob per language (`content_en`/`content_ja`, `longText`, **no length cap** — lesson length is a
  pedagogy decision, not a platform one).
- **No server-side sanitisation.** The write path runs `html_entity_decode`, so escaped tags in a code sample
  become *live markup* — a code sample containing `<h1>` injects a phantom heading into the lesson.
- Learner rendering is DOMPurify (defaults + `iframe` re-allowed) → html-react-parser. **Tables, links, images,
  code blocks and iframes all render — and ` ```mermaid ` fences render as live diagrams**
  (`resources/ts/src/components/lesson/Lecture.tsx`). 16 tables and 184 mermaid blocks already ship in seeded
  content. **Architecture diagrams need no image hosting: write them as mermaid.**
- **The admin TipTap editor is strictly less capable than the platform** — it loads only StarterKit + Heading(1-3)
  + Image + Youtube, cannot author tables or tagged code fences, **and destroys them on re-save** (it writes back
  `editor.getHTML()` of what it could parse). Publish via API or seeder; **never round-trip a generated lecture
  through the admin editor.**
- Images by URL or base64; video upload ≤50 MB or `video_url`.

### 11.3 Quiz — narrower than it looks

- **Single-answer MCQ only, locked at three layers**: the submission API takes one scalar `option_id` per question
  (`SubmitQuizRequest.php:23-24`), grading consults only the *first* `is_correct` option
  (`LessonController.php:190`), and the editor enforces exactly-one-correct (`ManageQuizSheet.tsx:60,72`).
  Marking two options correct does not make a multi-select — it makes a silently mis-graded question.
  `true_false` is a dead constant with zero call sites.
- **`pass_rate` is a raw count of questions, not a percentage** — migration comment `'in no. of questions'`,
  grading `if ($passedCount >= $quiz->pass_rate)` (`LessonController.php:215`). Decide the threshold and the
  question count together. The API accepts it (and `duration`) as *strings*.
- **No explanation field. Proven from the schema**: zero occurrences in all 59 migrations, `app/`, and `routes/`.
  The submission response returns per-question `passed` + `correct_option_id` — a learner learns *which* option
  was right, never *why*. **The correct option's text is therefore the de facto explanation surface: write it as
  a complete, self-justifying statement.** Distractors carry all corrective teaching (see the NEVER list).
- No per-question points, no attempt limits, no shuffling, no banks, no partial credit — all phantom type fields.
- Options are plain text, bilingual (`_ja` nullable); the editor requires ≥2 per question.

### 11.4 Lab — one JavaScript buffer, stdout-matched

- A learner submission is **one POST carrying only the code string** (`POST /labs/{id}/submissions`).
- **Execution is the managed RapidAPI Judge0 CE endpoint, not self-hosted** — RapidAPI auth headers, a polling
  workaround written specifically for that host's behaviour, and no judge0 service in `docker-compose.yml`.
- **The learner path hardcodes `language_id: 63` (Node.js)** — `LessonController.php:292` — regardless of the
  lab's stored `language`. The admin *preview* maps javascript/python/cpp/java (`LessonService.php:107`), so a
  non-JS lab passes the author's preview and mis-grades for every learner. **Reported as a platform bug
  2026-08-24. Until fixed: labs are JavaScript, full stop.** No SQL id exists in the map at all.
- **No stdin, no network, no multi-file, no resource limits** — none of those Judge0 fields is ever sent. A lab
  cannot fetch a URL, install a package, or read input. For this course that is the hard boundary: learners can
  *model* a request/response in pure JS, never make one.
- Grading is a strict `===` on CRLF-normalized, outer-trimmed stdout — case-sensitive, internal whitespace
  significant. `expected_output` is `VARCHAR(255)`. Design answers as one short scalar line.
- Rate limit: **10 executions per day** for free learners, charged per test case — labs must be passable in a few
  tries, which argues for small, well-scaffolded exercises.
- `function_name` is **nullable in the API**, and the admin UI fails to persist it. The admin preview wraps a
  named function; the learner path runs the buffer as-is. So author labs as *"complete the template so it prints
  X"*, with the function scaffold living in `template_code`.
- **A CSS or visual-design lab can never be auto-graded on this stack** — a managed CE instance cannot host a
  custom image with a browser. Decision 7 (§12) stands; the Web Design course stays third.

### 11.5 Localization

- **11 `*_en`/`*_ja` column pairs across 8 tables** (migrations 2026-07-19 → 22): courses(title, description) ·
  sections(title) · lessons(title) · lesson_lectures(content) · lesson_quizzes(quiz_instructions) ·
  quiz_questions(question_text) · quiz_options(option_text) · articles(title, excerpt, content). Legacy
  single-language columns dropped 2026-07-22.
- All nullable; `localized()` null-coalesces to the other language, so **an English-only course is fully usable
  by a Japanese-locale learner** — untranslated, not broken. **An empty string defeats the fallback** (`'' ?? x`
  is `''`): omit `_ja` keys entirely, never send `""`.
- **One course record holds both languages** — locked in by a regression test. "Both" = filling a second column,
  never a second course tree.
- But the API **requires** `title_ja` + `description_ja` on course create and `title_ja` on section create
  (lessons, lectures and quizzes are JA-optional) — so even an English-first course owes Japanese for one title,
  one description and each section title.
- **Labs and curricula have no localization columns at all.**
- Locale resolves per request from `Accept-Language` (en/ja, default en). **No completeness check exists
  anywhere** — nothing warns when one language is missing.

### 11.6 Authoring and publishing (the API)

- **The full chain is token-scriptable**: `POST /api/v1/admin/login` → Bearer token (Sanctum, no expiry;
  `teacher` role holds every content permission), then `curricula|courses|sections|lessons /create`. No bulk
  endpoint — but one lesson call carries its whole quiz/lab subtree, so a 40-lesson course is ~50 calls.
- Course and curriculum create are **multipart** (`thumbnail` carries the `image` rule, ≤2 MB). Course `order`
  on create is silently discarded — set it via update or reorder.
- **Verbs are inconsistent and regression-tested that way**: course/curriculum update = `PUT /{id}`;
  section/lesson update = `POST /{id}`.
- **Lesson update upserts nested children by `id`** — keep an id manifest beside the source markdown; re-posting
  without ids appends duplicate questions. Omit `lecture.id` on update (its validation is unscoped).
- **Never address sections or lessons by title** — those lookups validate against columns dropped on 2026-07-22
  and fail at the database. Use ids captured from create responses.
- Swagger is wired but has zero annotations on the authoring endpoints — **the FormRequests are the spec.**
- The admin UI's section dialogs impose a 10-character title floor (UI-only; the API allows 1–255) — via the UI,
  "Intro" is rejected.
- Lesson titles: `max:255` (the fork-era claim of 100 was wrong). A lesson has no description field — outcomes
  live in the lecture's first paragraph; a quiz's only framing is its required `quiz_instructions`.
- *Caveat:* every claim in this section is static code reading; nothing was executed. One smoke call against
  staging (login + one throwaway section) proves the auth chain.

### 11.7 Known platform bugs (reported 2026-08-24)

1. **Learner lab submissions always execute as Node.js** — `language_id: 63` hardcoded in the learner path while
   the preview maps four languages. Any non-JS lab passes preview and fails learners.
2. **The admin lecture editor silently deletes tables and mermaid fences on re-save.** Destructive, not merely
   limited — affects the already-seeded content today.

## 12. Decisions

**Taken (2026-08-19 meeting):**

1. Build the knowledge base first — but design it for reliability before building.
2. Vault lives in **its own private repo**, not inside `nexusbim-brain`.
3. The KB is written in **English**.
4. `verified` by **second AI pass** for now, with the §9 limits.

**Taken (2026-08-19, after the §11 re-verification):**

5. **v1 is scoped to the web-system-architecture course.** Charter in `curriculum/`. The handover's recommendation
   is kept but **its stated reason is rejected** — it recommended this course because it "can use SQL labs for a
   genuinely hands-on module", and SQL cannot execute at all — the learner path runs every submission as
   Node.js and no SQL id exists in the language map (§11.4). It wins on three better grounds: **decay** (a
   Claude 101 course is almost entirely volatile — model names, prices, feature lists — which §5.1 requires be
   isolated), **reusability** (its notes serve courses 2 and 3; a tool course's do not), and **persona fit** for
   the salesperson the team called out most specifically. **Labs are JavaScript, not SQL** — every lab requires a
   named function regardless of language, and SQL has none.
6. **Course language: English for v1.** Recorded as *English-authoritative, Japanese derived — deferred*, not as
   "undecided". The blocker is a review capability the team does not have, so the **reopen trigger is a named
   person who reads Japanese committing to be the T2 judge and T5 cold reader for a Japanese course** — not a
   date and not a market signal. The real constraint is not capability: the platform is already bilingual at the
   chrome level (§11.5), but no locale field exists on any course object, so "both" means two full course trees
   with no platform-level pairing. **The entire accommodation is one L5 note** requiring every analogy and quiz
   scenario to survive translation into Japanese without a rewrite. That costs one slot, requires zero Japanese,
   and is the difference between a later translation project and a re-authoring project. Japanese exemplars go to
   `brain/_backlog/style.md` — they are unverifiable by anyone currently on the team.
7. **The CSS-lab fork: deferred, with a trigger and an L4 note.** Re-framed by verification — a CSS lab cannot be
   *authored*, not merely cannot be auto-graded (§11.4), so there is no partial path and nothing to design around
   inside the lab primitive. Recorded as `brain/platform/css-labs-cannot-be-authored.md` rather than a backlog
   line, because backlog files are not in `INDEX.md` and by §3.1's own rule a note that cannot be retrieved does
   not exist — retrieval question 4 must land on it. **Forcing event:** the first course charter proposing a lesson
   whose assessed outcome is "the learner produces visual output". **Backstop:** re-asked once at the v1 review.
   An event alone can go unnoticed; a date alone slides. **Dependency previously hidden:** this is not independent
   of decision 5 — deferring is safe *only* while course 1 has no visual-output assessment.
8. **Ownership: solo now, staged later.** See §6.4 for the survives / substituted / `UNMET` split, the six
   substitution mechanics, the join order, and the rotating-auditor verdict with its amendment.

**Carried open on 2026-08-19 — all four answered on 2026-08-24** by reading the platform monorepo at
`origin/develop` @ `3d34a4e` (kept here so the answers are traceable):

1. **How a stored lab grades a real learner submission** → the learner posts one code buffer; it runs on managed
   RapidAPI Judge0 as Node.js (hardcoded) and stdout is `===`-compared to `expected_output`. `function_name` is
   nullable and unused at learner runtime — the preview's function harness is preview-only (§11.4).
2. **`pass_rate` semantics** → a **raw count** of correctly answered questions; grading is
   `$passedCount >= $quiz->pass_rate` (§11.3). The fork's "%" label was wrong.
3. **Whether SQL labs execute** → no. No SQL id exists in the language map, and the learner path runs everything
   as Node.js regardless (§11.4).
4. **Where lecture diagrams are hosted** → nowhere: ` ```mermaid ` fences render as live diagrams in the learner
   app, and 184 already ship in seeded content (§11.2). No image pipeline needed.

**Newly open (2026-08-24):**

1. **A staging smoke test of the authoring API** — every §11.6 claim is static code reading; one login + one
   throwaway section proves the auth chain. Owner: whoever holds staging credentials.
2. **The two reported platform bugs** (§11.7) — the hardcoded Node.js runner and the destructive lecture editor.
   Owner: platform team; the KB only tracks whether they are fixed, since both bound course design.

---

## 13. Definition of done for v1

**Not a note count.** v1 is done when:

1. **T1, T3 and T4 pass with dated results** in `tests/audit-log.md`, each naming the auditor-prompt hash it ran
   under, and **T4's tripwire caught** (§6.4). **T2 passes against the §2.2 rubric**, recorded as `T2-partial`
   while solo. **T5 is either run with a borrowed reader or carries a dated `UNMET` row** — never simulated.
   *Amended 2026-08-19:* "all five tests pass" was unreachable under §6.4 and would otherwise have been satisfied
   by quietly loosening what *pass* means, which is the exact failure this design exists to prevent.
2. One complete lesson has been generated from the vault by a fresh session and judged shippable without a rewrite
   against the §2.2 rubric — including its lines 8 and 9, that every claim traces to a note id and no fact appears
   that is not in the vault.
3. Every domain note is `verified` or explicitly marked `confidence: low` with a reason.
4. Each layer's backlog file exists. **Where one is empty, `tests/audit-log.md` carries a one-line statement of why
   nothing was deferred.** *Amended 2026-08-19:* requiring every backlog to be non-empty rewards inventing filler
   to pass. The intended signal was that someone consciously asserted it, and a dated statement carries that
   signal without the incentive.
5. `scripts/check-vault.py` exits clean (§7.3).

If the tests pass at 28 notes, v1 is done at 28 notes.
