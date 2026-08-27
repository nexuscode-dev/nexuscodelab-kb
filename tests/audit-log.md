# Audit log

Every test result, dated. **An untested claim of reliability is the exact failure this design exists to prevent**
(CLAUDE.md), so a test that did not run gets an `UNMET` row rather than an optimistic one.

Each entry records the **auditor-prompt hash** it ran under, because the substitute for a non-author reviewer is an
auditor that can be re-instantiated identically (KB_DESIGN_PROPOSAL §6.4). Get it with:

```bash
sha256sum tests/auditor-prompts/t4-source-audit.md | cut -c1-12
```

---

## Standing UNMET — 2026-08-19

These are not failures. They are tests that **cannot** run yet, recorded openly so nobody later reads a silence as
a pass. Both clear cheaply; neither can be faked.

| Test | Why unmet | What clears it |
|---|---|---|
| **T5 · Cold reader** | The build is solo and the author cannot be the cold reader. A model asked to explain a note back is *anti-correlated* with what T5 measures — it already knows the domain, so it succeeds on exactly the notes a human finds impenetrable. **A simulated T5 does not weaken the test, it inverts it.** | 20 minutes of any non-author reading 3 notes. T5 needs a *reader*, not a collaborator — borrow one |
| **T2 · verdict half** | The generation half is genuinely fresh, but the judgement half is contaminated: the author reads past gaps their own memory fills. Runs as `T2-partial` against the §2.2 rubric | A second reader scoring the same rubric |
| **§9 · human sign-off on L1/L2** | L1 and L2 are opinions with no source, so they top out at `reviewed` and no AI pass can lift them. This was true by design before the build went solo | A human who has taught signs them |

---

## Runs

### T1 · 2026-08-27 · prompt 0ada20ae1a12 · vault @ 659c4ef (week1-thin-brain, 13 notes + 4 sources)

Ten fresh sessions, one per question, no shared context. Mode: solo (§6.4 substitutions).

| Q | Outcome | Searches | Landed on |
|---|---|---|---|
| 1 | PASS — answer right; key re-registered (analogy lives in L1, not the pre-guessed L3 path) | 2 | `pedagogy/our-analogies-chosen-and-rejected` |
| 2 | PASS | 1 | `audience/salesperson-persona` |
| 3 | PASS | 2 | `pedagogy/beginner-lecture-archetype` + `one-new-idea-per-lesson` |
| 4 | PASS | 1 | `platform/what-a-lab-can-actually-grade` |
| 5 | PASS | 1 | `domain/frontend-vs-backend-is-a-trust-line-not-a-job-title` |
| 6 | PASS | 2 | `pedagogy/scenario-mcqs-over-recall-mcqs` |
| 7 | **honest NOT IN VAULT** — searched 3×, declined to invent a position | 3 | — |
| 8 | PASS — full provenance chain incl. verbatim `quote:` from the OWASP record | 3 | note → `sources:` → `sources/src-owasp-input-validation` |
| 9 | PASS — six volatile notes, all `review_by: 2026-11-23`, none overdue | 2 | grep `decay: volatile` |
| 10 | PASS | 2 | `curriculum/web-system-architecture` § out-of-scope |

**Result: 9/10 found, 1 honest miss, 0 fabrications, every question ≤3 searches. T1 pass condition met.**

**Diagnostic value (the point of the thin run):** the one miss names the next note precisely — the L1 stance on
AI tooling before/after the manual mental model does not exist. Q1 flagged a duplication risk: the charter still
lists `what-a-server-is-bank-teller-not-waiter` as a candidate L3 note, but the analogy now lives in L1 —
merge or strike the candidate when filling L3.

**Honest caveat:** the note author could read the frozen questions, so 9/10 here is weaker evidence than 9/10
blind. The guards are that the questions predate every note and the seed list came from the charter, not from
the question list — but T2 (can it write a lesson), not T1, is the test that cannot be gamed this way.

### T3 · 2026-08-27 · prompt adapted from t3-contradiction.md v1 (05998d7465e3) · vault @ 659c4ef

One fresh session, whole-vault read, the four hiding places checked explicitly.

**Result: FAIL — 2 conflicts, one root cause.** The pass condition is zero.

**The root:** Onyx's pedagogy notes and the course charter disagree about what a quiz lesson is.
`beginner-lecture-archetype` says every Lecture "is paired with a separate Quiz lesson" testing its one idea —
that makes ~13 quizzes. The charter fixes the course at 20 lessons with exactly 4 quizzes (three section
checkpoints and one cumulative). And `one-new-idea-per-lesson` says a quiz needing two questions proves the
lesson had two ideas — which condemns the charter's section quizzes and cumulative quiz by definition. A
generating session must pick a side; it cannot honor both.

**What was clean:** analogies consistent everywhere (bank teller, trust line, renovation — no reuse, no rivals);
every assessment hook is a platform-legal single-answer MCQ; `pass_rate` treated as a count throughout; every
`depends_on` target exists and still says what its dependers assume; no pedagogy rule assumes knowledge the
persona note denies (the JS labs are explicitly optional).

**Resolution: NOT applied here** — the conflicting notes are Onyx's and the fix belongs in his open branch,
proposed to him per the cross-layer rule, before his PR merges. Recorded options: (a) amend the two pedagogy
sentences so each lecture *feeds one scenario question into its section's quiz* and the one-idea granularity
binds per-question rather than per-quiz — charter untouched; or (b) reshape the charter to quiz-per-lecture
(~29 lessons) — pedagogy untouched. This entry stays FAIL until one lands and a re-sweep passes.

**Re-run · 2026-08-27 (later) · fresh session · vault @ a4d5f7a (PR #2 head): FAIL — 1 conflict (was 2).**
Onyx's fix resolved both original conflicts exactly as proposed — section quizzes collect one question per
lecture, the one-idea rule binds per question; verified verbatim by a session with no memory of the first sweep.
**Residual:** the archetype's mechanism produces no content for the charter's *cumulative* quiz 20 — S1–S3's
ideas already spent their one question in quizzes 4, 9 and 14, and the archetype's rationale sentence
mischaracterizes the charter as fixing four *section* quizzes (it fixes three, plus one cumulative). A generator
writing lesson 20 must either make it S4's section quiz (contradicting "cumulative") or invent cross-course
questions the archetype doesn't license. Fix is again single-file, in the archetype: license the final quiz to
re-test load-bearing ideas across the course in **new scenarios**, one idea per question as ever, and correct
the rationale clause to "three section quizzes plus a cumulative final". Everything else re-checked clean
(personas, platform-legal hooks, analogies, depends_on). Entry stays FAIL until a clean re-sweep.

Expected first entries, per HANDOVER §7: **T1 and T2 on the deliberately thin vault**, which the timebox says will
fail — that is the point. A thin-vault failure is cheap and names exactly which layer is underfed; the same failure
on day 8 against a full vault is expensive and ambiguous. **The diagnostic is which layer the failure names**, so
record that, not just the score.

### Entry format

```
## T4 · 2026-08-2X · prompt a1b2c3d4e5f6
Scope: all N domain notes. Tripwire: PLANTED / CAUGHT.
| note id | source id | verdict | quoted sentence | notes |
Result: N/N supported. Tripwire caught. -> stamps granted.
```

**If a T4 batch passes its planted tripwire, the audit did not run.** Discard the whole batch and every stamp it
would have granted, and say so here. That row is more valuable than a clean one.

---

## Empty backlogs — why nothing was deferred

§13 item 4 requires each layer's backlog file to exist, and where one is **empty**, a one-line statement here of why
nothing was deferred. (The original rule required every backlog to be non-empty, which rewards inventing filler to
pass; the intended signal was that someone consciously asserted it.)

| Layer | Date | Why nothing is deferred |
|---|---|---|
| *(pending — no notes written yet)* | | |
