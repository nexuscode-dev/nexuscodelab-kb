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

### T3 · 2026-08-27 · **PASS** (on the fifth run — the four failures below are the evidence the test works) · prompt adapted from t3-contradiction.md v1 (05998d7465e3) · vault @ 659c4ef

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

**Re-run 2 · 2026-08-27 (later) · fresh session · vault @ 307d89e (PR #2 head): quiz model CLEAN, 2 new conflicts — both mine.**
The previously failing site is fully resolved and verified sentence-by-sentence: section quizzes = one question
per lecture, the cumulative Quiz 20 is licensed ("re-testing a taught idea in a new scenario is not a new idea"),
and no remaining sentence mischaracterizes the split. **The two conflicts found are artifacts of the 2026-08-26
budget rebalance, which updated the validator and two docs but missed the backlog headers, three proposal prose
passages, and the charter's candidate-count line** — the vault disagreed with itself about its own caps
(15–20 vs 12–15 for L3; 3–4 vs 6–8 for L2). Fixed same day, and the drift class is now mechanically closed:
`check-vault.py` gains a rule that fails the build when a backlog header or CLAUDE.md's cap line disagrees with
the CAPS the script enforces (tested by breaking a header on purpose). Charter consequence made explicit: 17 L3
candidates against a 12–15 cap means at least two get merged or backlogged at fill time — candidate 2 (now
duplicating the L1 analogies note) and the four ⚠ candidates are first in line.
**Entry flips to PASS only after a zero-conflict sweep on merged main, post-PR #2.**

**Re-run 3 · 2026-08-27 · fresh session · vault @ 4415414 (merged main): 1 conflict** — the last stale cap literal,
in a backlog *row* one paragraph below the header the previous fix corrected. Fixed in `83aea5b`; the validator's
cap check widened to scan every prose mention in brain/ and curriculum/, tested by planting a stale literal.

**Re-run 4 · 2026-08-27 · fresh session · vault @ 83aea5b: ZERO CONFLICTS — T3 PASSES.**
All six probe sites confirmed clean by a session with no memory of any earlier run: personas, platform-legal
hooks, one-analogy-per-concept, depends_on integrity at `3d34a4e`, the quiz model (section checkpoints +
licensed cumulative Quiz 20), and every cap literal in every file agreeing at 8–10 / 6–8 / 12–15 / 4–6 / 3–5.

**What the five-run trail bought:** two cross-author quiz-model conflicts caught before merge, one residual at
the cumulative quiz, and two cap-literal drifts from an half-applied budget change — each converted into either
a fixed sentence or a new mechanical check (cap literals are now build-enforced, and probe sites 5 and 6 are
permanent additions to the sweep prompt). Every failure made the next sweep harder to pass.

### T6 (refusal) · 2026-08-28 · **PASS** · fresh session · vault @ d8c33a0

Asked, under the standard grounding rules, to write "What DNS is" — a topic Claude knows cold, and one the vault
deliberately excludes. **It refused, with the right citations**: the charter's out-of-scope table (DNS is on the
deliberate not-taught list, load-bearing for retrieval Q10), the backlog's deferral record with its exact
reasoning ("a salesperson needs 'the name points at the machine', which is one sentence inside lesson 6, not a
note"), and a vault-wide grep confirming zero grounding material. It then stated the sanctioned path to reverse
the decision (amend charter → promote the backlog note with an L6 source → generate). This is the "confidently
wrong and nobody knows" failure mode tested directly, and the grounding rules held under pressure.

### T2 comparison pair · 2026-08-28 · staged for human review

The no-brain control twin of Lesson 13 is generated (fresh session, empty directory, identical brief) and saved
at `reviews/t2/lesson-13-no-brain-twin.md` beside the with-brain version. **Honest pre-read for reviewers:** the
twin is *good* — it independently converged on the spreadsheet misconception and a construction analogy (a close
cousin of our recorded renovation analogy). On a topic this well-trodden, unaided Claude is strong. The delta to
score for is therefore NOT surface quality but: (1) does the with-brain version use *our exact recorded* analogy
rather than a fresh one each generation — consistency across 20 lessons; (2) does every claim trace to a note —
auditable vs unfalsifiable; (3) scope discipline — the twin has no mechanism to refuse out-of-scope requests
(see T6 above, which the vault passed). If reviewers judge on prose quality alone, the pair will read as a tie —
and that reading, honestly recorded, would itself be a week-1 finding about where the brain does and does not
add value. Verdict half remains with the human reviewers (handed to Leon as rubric owner).

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

---

## Content review registry — dated course lessons

Course content has no `review_by` frontmatter the way Brain notes do, so decay ownership for dated lessons is
recorded here (per the 2026-09-01 course 2 review, "Decay ownership is still unassigned"). One row per dated
lesson; update `last_reviewed` on every re-verification, and on ship day set it to the publish date.

| Course | Lesson | Owner | last_reviewed | review_by |
|---|---|---|---|---|
| Working With AI: Claude Fundamentals | Appendix: Today's Models | hein | 2026-08-31 (re-verify on ship day) | 2026-12-01 |
| Working With AI: Claude Fundamentals | Using Claude Today (orientation lecture) | hein | 2026-08-31 (re-verify on ship day) | 2026-12-01 |
| Using Claude Today (course, proposal-stage) | all 3 lectures | hein | 2026-08-31 (re-verify on ship day) | 2026-12-01 |

A lesson whose `review_by` has passed without a row update here is presumed stale: do not market it, and
prioritize the refresh or the kill switch in its proposal.
