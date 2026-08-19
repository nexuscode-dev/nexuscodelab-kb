# NexusLab Knowledge Base — Design Proposal

**Status:** for team review
**Date:** 2026-08-19
**Scope:** how the knowledge base is built so it can be trusted. Not the knowledge base itself, and not the curriculum.
**Read before:** writing the first note.

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
| T1 | **Retrieval** | 10 fixed questions a course author would really ask (§2.1) | a fresh session finds the right note in ≤3 tool calls, 9/10 |
| T2 | **Sufficiency** | fresh session, vault only, write one lesson | shippable without a rewrite — human judges |
| T3 | **Contradiction sweep** | fresh session whose *only* job is to find conflicting claims | zero conflicts |
| T4 | **Source audit** | sample 10 domain notes; check the source actually says it | 10/10, no drift |
| T5 | **Cold reader** | a human who didn't build the KB reads 3 notes | can explain the concept back |

**T2 is the headline test.** The others catch the specific ways a KB rots. A KB that passes T2 and fails T3 will
produce good lessons that quietly disagree with each other.

Every test is run by someone who did not author the layer under test. A layer owner testing their own layer
reproduces the AI-reviewing-AI problem one level up, at the human level.

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
  courses/
    <course-slug>/           # generated lessons: the source of truth for what's published
  tests/
    retrieval-questions.md   # T1, fixed
    audit-log.md             # T3/T4 results, dated
```

**`brain/` and `courses/` are siblings, never mixed.** Generated lessons are *outputs* of the brain, not part of
it. Mixing them does two kinds of damage: retrieval starts returning lesson prose instead of principles, and the
brain grows without getting smarter. This split also gives a clean versioning answer — `courses/` is the source of
truth for what is published on NexusLab, `brain/` is the source of truth for *why it is written that way*.

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
sources: [src-mdn-http-overview]
teaches: [web-architecture/module-2]    # empty = not yet backing any course
---
```

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
status: verified
confidence: high
decay: durable
last_verified: 2026-08-19
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

**Assessment hook (MCQ, scenario form).** "A login form has a hidden field `role=user`. Which of these can the
user change before it reaches the server?" — tests the trust boundary rather than the vocabulary.
```

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

**Why.** Multiple choice and true/false are the only question types NexusLab has (see
[[nexuslab-lesson-primitives]]). Recall questions are what that constraint tempts you into, and they measure
whether the learner read the page. Scenario questions measure whether the model in their head works.

**Form.** Symptom → "which layer is at fault?" · artefact → "what happens next?" · change → "what breaks?"

**Anti-examples.** "What does API stand for?" · "HTTP is stateless: true or false?" — both pass a learner who
understood nothing.

**Rewrites of those two.** "The page shows yesterday's price after you clicked refresh. Which is the likeliest
cause?" · "You log in, then open a second tab and you're logged in there too. What must be travelling with the
second tab's requests?"

**Distractor rule.** Every wrong answer is a real misconception from the misconception catalog, never filler. A
wrong answer nobody would pick teaches nothing and makes the question easier than it looks.
```

---

## 5. The six layers

| Layer | Holds | Explicitly does **not** hold |
|---|---|---|
| **L1 Pedagogy** | lesson archetypes, sequencing rules, outcome verbs, assessment patterns for an MCQ+stdout platform, misconception catalog, cognitive-load rules | subject matter |
| **L2 Audience** | the three personas, prior knowledge, weekly time budget, motivation, how each fails | teaching technique (that's L1) |
| **L3 Domain** | concept notes **scoped by the curriculum**, each with source + teaching angle + misconception | anything no planned lesson needs |
| **L4 Platform** | NexusLab primitives and their limits, verified against the admin app | course content |
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
3. **Dissent is recorded in the note, not silently overwritten** — extending the norm already agreed for
   `nexusbim-brain`: the brain is fallible, and disagreement is wanted output rather than friction.
4. **Owner rotation is a v2 question.** Not designed now.

---

## 7. Note budget

A pre-declared cap, fixed **before research starts, while nobody is invested.** It converts "are we done?" from a
judgement call made under sunk-cost pressure into an arithmetic check.

| Layer | Notes |
|---|---|
| L1 Pedagogy | 8–10 |
| L2 Audience | 3–4 |
| L3 Domain | 15–20 |
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

**Calendar conversion, stated honestly:** at ~25% capacity alongside the hardening cycles, 8 working days is
**2.5–3 calendar weeks.** Quote the calendar number to the team — "8 days" will be heard as calendar days.

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
- T4 samples 10 notes rather than auditing all of them. Sampling catches systematic drift, which is the failure
  that matters; exhaustive audit costs more than it returns.

---

## 10. Failure modes and guards

| Failure | Guard |
|---|---|
| Sprawl — infinite research, no convergence | §7 budget, §8 timebox, L3 scoped by curriculum |
| Contradiction drift (silent) | one owner per layer, atomic notes, T3 sweep |
| Hallucination baked in, then repeated by every course | mandatory sources on domain claims, `confidence` + `status`, T4 |
| Staleness | `decay` + `last_verified`; volatile content isolated so a refresh is bounded |
| The right note exists but is never found | INDEX.md, filename discipline, T1 |
| AI reviewing its own work | fresh verifying session, source-first questioning, human sign-off gate on L1/L2 |
| The KB nobody updates | tie the update ritual to course revision — something that already happens — never a standalone discipline |

---

## 11. Platform constraints (input to L4, verified 2026-08-19)

Read from the NexusLab admin app (`NexusCodeLabAdmin`). These bound what any course can be:

- Hierarchy: **Curriculum → Course → Section → Lesson.**
- A lesson is exactly one of three things: **Lecture** (a single TipTap HTML blob — headings, images, tables,
  links, YouTube embed) · **Quiz** (`multiple_choice` or `true_false` only, plus a pass rate) · **Lab** (Monaco
  editor + template code + language + test cases, graded by comparing stdout to expected output).
- **No free-text or human-graded submission type exists** anywhere in the model.
- `html` and `css` appear in the lab language list, but grading compares stdout and there is no render or DOM
  assertion — **a CSS lab cannot be auto-graded.** Open product decision.
- **SQL labs work properly**, so a database module can be genuinely hands-on at no extra cost.
- Lecture content is stored as an HTML blob with no markdown source, which is why `courses/` in this repo must be
  the authoring source of truth (§3) — otherwise updating a course means hand-editing rich text in a browser
  forever, with no diff and no review.
- `i18n/locales/{en,ja}` exist but are empty.

---

## 12. Decisions

**Taken (2026-08-19 meeting):**

1. Build the knowledge base first — but design it for reliability before building.
2. Vault lives in **its own private repo**, not inside `nexusbim-brain`.
3. The KB is written in **English**.
4. `verified` by **second AI pass** for now, with the §9 limits.

**Open — needed before or during v1:**

1. **Ownership arrangement** — slot assignment, and auditor as fourth-hat vs rotating (§6).
2. **Course language** (ja / en / both) — separate from the KB language, and still undecided. If courses go
   Japanese, L5 must carry **Japanese exemplars inline** even inside English notes; translated pedagogy phrasing
   loses exactly the nuance being captured.
3. **The CSS-lab fork** — build a render/assertion lab type, or design course 3 around the limitation.
4. **Which course v1 is scoped to.** The budget assumes one.

---

## 13. Definition of done for v1

**Not a note count.** v1 is done when:

1. All five tests pass, with results dated in `tests/audit-log.md`.
2. One complete lesson has been generated from the vault by a fresh session and judged shippable without a rewrite.
3. Every domain note is `verified` or explicitly marked `confidence: low` with a reason.
4. Each layer's backlog file exists and is non-empty — an empty backlog means people were smuggling content into
   notes instead of deferring it.

If the tests pass at 28 notes, v1 is done at 28 notes.
