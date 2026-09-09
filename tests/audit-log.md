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
| **T5 · Cold reader** | The build is solo and the author cannot be the cold reader. A model asked to explain a note back is *anti-correlated* with what T5 measures — it already knows the domain, so it succeeds on exactly the notes a human finds impenetrable. **A simulated T5 does not weaken the test, it inverts it.** | **Owner + trigger assigned 2026-09-02: Wai Lin, personally, reading 3 notes at publish** as part of his pass over the live site. A dated UNMET with a named owner is a different artifact from an open ask |
| **T2 · verdict half** | The generation half is genuinely fresh, but the judgement half is contaminated: the author reads past gaps their own memory fills. Runs as `T2-partial` against the §2.2 rubric | A second reader scoring the same rubric |
| **§9 · human sign-off on L1/L2** | L1 and L2 are opinions with no source, so they top out at `reviewed` and no AI pass can lift them. This was true by design before the build went solo | A human who has taught signs them |

---

### Standing UNMET — added 2026-09-09

| Item | Why it is unmet | Owner / trigger |
|---|---|---|
| **Course publish state** | Every decision that says "held from publication", "approved on hold", or "unpublish it rather than let it grade wrong answers" assumes a capability the platform does not have: `courses` has no publish/status column, so publication is enforced only by nobody running a seeder, and the kill switch cannot be operated. `articles` already have this column, so the pattern exists and was simply never applied to courses. | **Needs Wai Lin's call**, since it changes what "approved on hold" means operationally. Blocks the Career Pathway direction too — a living handbook cannot ship content it cannot retire. |

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

**Q7 resolved (2026-09-01), by an owner decision — not by an AI guess.** The stance now exists as
`pedagogy/manual-model-before-ai-tooling`, recorded as an owner decision by Ye Yint Ohn Kyaing: the manual
web-system mental model first, AI later as a component inside it, never a shortcut past the architecture. The T1
result above stands exactly as recorded — 1 honest miss, 0 fabrications. When the note did not exist, the correct
behavior was to log the gap and refuse to invent an owner opinion, and that refusal remains the right call; what
closed the gap was an actual owner statement, which is the only thing that could.

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
| Working With AI: Claude Fundamentals | Today's Models (S4 reference) | hein | **2026-09-03 (pre-publication check — see below; bump to publish date on ship day)** | 2026-12-01 |
| Working With AI: Claude Fundamentals | Where These Ideas Live in the App (S4 reference — renamed 2026-09-09, was "Using Claude Today") | hein | **2026-09-03** (rewritten and re-checked that day; bump to publish date on ship day) | 2026-12-01 |
| Using Claude Today (course, approved on hold) | all 3 lectures + the "Checkpoint: Using Claude" quiz | hein | 2026-08-31 (re-verify on ship day) | 2026-12-01 |

A lesson whose `review_by` has passed without a row update here is presumed stale: do not market it, and
prioritize the refresh or the kill switch in its proposal.

**How a live refresh is actually applied (added 2026-09-09).** Until this date these rows recorded a duty with
no executable procedure — see the review entry below. A dated lecture is now refreshed with
`COURSE_SEEDER_REFRESH_CONTENT=1`, which rewrites text in place, deletes nothing, and is therefore the only
mode permitted on production. `COURSE_SEEDER_REPLACE=1` remains local-only and is for structure changes.

**Pass the flag on the container, not the host.** Sail forwards no arbitrary environment variables, so
`COURSE_SEEDER_REFRESH_CONTENT=1 sail artisan db:seed …` silently reads as unset and prints "skipping
already-seeded course" — which looks like the flag applied and found nothing to do. Every seeder's documented
command was wrong this way until 2026-09-09. The form that works:

```sh
sail exec -e COURSE_SEEDER_REFRESH_CONTENT=1 laravel.test \
    php artisan db:seed --class=ClaudeFundamentalsSeeder
```

This is the kind of fact a `review_by` depends on: a refresh duty whose command does not run is not a duty.
**The "kill switch" these rows and `using-claude-today.md` rely on still does not exist:** `courses` has no
publish or status column, so a stale course cannot be unpublished, only deleted — which destroys learner
progress. Recorded as UNMET rather than left implied.

**On-hold rows are pre-publication checks, not live-content deadlines.** *Using Claude Today* is approved but
held from publication (decision 2026-09-02); until it is live, its row's `review_by` means "re-verify before
publishing", and an overdue date on it is not a live-content incident — recorded so an overdue row on
unpublished content is not read as registry noise.

### Licensing decision — third-party YouTube videos in course 2 · 2026-09-01

Checked 3blue1brown.com/about (by hein + Claude session): clips under 60s with attribution are allowed,
re-uploads forbidden, and "any other use case, including uploading full lessons to an alternate educational
platform" requires a licensing inquiry via his contact form. Embedding full videos in a paid course is not
clearly covered → resolved by **replacing both embeds (3Blue1Brown, Karpathy) with optional plain YouTube
links**, which require no permission. Decision: links stay unless a written approval via the contact form ever
justifies restoring embeds. Seeder and live rows updated same day.

---

## T4 · 2026-09-02 · prompt 3c34eb552072

Scope: all 4 domain notes (5 claims audited: 4 real + 1 planted). **Tripwire: PLANTED / CAUGHT.**

Method: per `tests/auditor-prompts/t4-source-audit.md` v1, from outside the repo — five isolated fresh sessions
in a scratch directory, one claim each, no vault access, no repo CLAUDE.md, never shown the note or the
reasoning. Each auditor received only the claim sentence and the source page **fetched live 2026-09-02** from
the URL in the source record — never the stored `quote:` field, which would make the audit circular. Builder
(extraction, corruption, orchestration): hein + session. Onyx authored all four notes and all source records and
touched nothing here (§6.4). HTML-stripping introduced stray spaces inside some words of the fetched text;
auditors were told to treat spacing as artifact, and spacing is normalized in the transcription below.

| note id | source id | verdict | quoted sentence | notes |
|---|---|---|---|---|
| what-a-table-record-and-column-are | src-postgresql-table-concepts | YES | "Each table is a named collection of rows. Each row of a given table has the same set of named columns, and each column is of a specific data type." | stamp granted |
| why-the-browser-cannot-reach-the-database | src-mdn-client-server-overview | **NO** | — | Compound claim. MDN states each half separately — "Web browsers communicate with web servers using the HyperText Transfer Protocol (HTTP)." and "…the server determines the product ID, fetches the data from the database…" — but no single sentence states both, and the rules forbid reconstructing a claim from separate passages. **No stamp. Returned to the note's author: split the claim into its two sourced sentences, then re-audit that claim with a fresh tripwire.** |
| *(tripwire)* "In MySQL, ALTER TABLE changes the data stored in a table's rows, but never its structure." | src-mysql-alter-table | **NO — CAUGHT** | — | Planted corruption (negated direction), position 3 of 5. Auditor cited the opposite sentence from the source. |
| a-schema-change-is-not-a-text-edit | src-mysql-alter-table | YES | "ALTER TABLE changes the structure of a table. For example, you can add or delete columns, create or destroy indexes, change the type of existing columns, or rename columns or the table itself." | stamp granted |
| frontend-vs-backend-is-a-trust-line-not-a-job-title | src-owasp-input-validation | YES | "Input validation must be implemented on the server-side before any data is processed by an application's functions, as any JavaScript-based input validation performed on the client-side can be circumvented by an attacker who disables JavaScript or uses a web proxy." | stamp granted |

Result: **3/4 supported. Tripwire caught → the batch stands.** Stamps granted: three notes `draft` → `verified`
(frontmatter + INDEX updated). `why-the-browser-cannot-reach-the-database` stays `draft`: the NO is a
claim-granularity defect, not a sourcing one — the source record documents both halves individually — but
quote-or-NO is the test, not a technicality to argue with. Fetch note: dev.mysql.com served a block page on the
first two attempts; the third returned the real manual, and the extract used contains the full ALTER TABLE
description.

### L3 v1 boundary · 2026-09-02 · Course 1 candidate list finalized (Round 2 decision)

Not a T-series run — a recorded scope decision. **Course 1 is the v1 boundary. The L3 Domain cap stays 12–15 and is
NOT raised for Courses 2/3;** domain knowledge those courses need waits for a per-course v2 L3 budget (§7.1). The
charter's active candidate list is trimmed to the candidates a specific Course 1 lecture relies on.

**Count: 15 → 13.** Two candidates were moved to `_backlog/domain.md` (not deleted), each with a v2-recoverable
reason:

- `validation-happens-twice-and-only-one-counts` — for Course 1 it duplicates the already-**verified**
  `frontend-vs-backend-is-a-trust-line` note (T4 above granted its OWASP stamp: "input validation must be implemented
  on the server-side…"), so the idea is covered; its own full treatment is Course 2 forms material.
- `stale-data-means-something-was-cached` — Course 1 teaches no caching lecture; the quiz-9 scenario resolves from the
  round-trip idea. Full caching is Course 2 performance material.

The two earlier cuts (`what-a-server-is-bank-teller-not-waiter`, `the-request-carries-everything-the-server-knows`)
were already applied on 2026-09-01 and are unchanged here. No written Domain note was deleted (the four
`brain/domain/*.md` notes are all intact); nothing from Courses 2/3 was promoted into Course 1. **Prior T1/T3/T4
records above are preserved exactly — this is an additive entry, not an edit to earlier evidence.**

### §9 sign-off · 2026-09-02 · six L1/L2 opinion notes `draft` → `reviewed`

The opinion layers (L1 Pedagogy, L2 Audience) carry no source, so under §9 they top out at **`reviewed`** — a human
who has taught signs them, and no AI pass can lift them further. That sign-off has now happened.

**Evidence granting the promotion:** two documented Course 1 review rounds (Round 1 and Round 2, both recorded across
this log and the Course 1 proposal), and **Wai Lin's explicit decision on 2026-09-02 that those two rounds constitute
the §9 review** for these notes. This is a labelling promotion, not a sourcing one: `reviewed` records that a
qualified human has read and endorsed the opinion — it makes **no** claim that the notes are source-verified, and by
§9 they can never become `verified`.

Promoted `draft` → `reviewed` (status line only; bodies and all other metadata unchanged):

- `brain/pedagogy/beginner-lecture-archetype.md`
- `brain/pedagogy/one-new-idea-per-lesson.md`
- `brain/pedagogy/our-analogies-chosen-and-rejected.md`
- `brain/pedagogy/scenario-mcqs-over-recall-mcqs.md`
- `brain/pedagogy/manual-model-before-ai-tooling.md`
- `brain/audience/salesperson-persona.md`

`reviewed` is the **ceiling** for these six; they are not `verified` and will not be. **T4** (source audit) and **T5**
(cold reader) remain outstanding per the Standing UNMET table — this entry closes only the §9 L1/L2 sign-off gate,
nothing else. Prior records above are preserved exactly; this is additive.

### T4 fix returned · 2026-09-02 · `why-the-browser-cannot-reach-the-database` compound claim split

Epsilon's Course 1 T4 returned one note for fix: `why-the-browser-cannot-reach-the-database` failed only on **claim
granularity** — its single `Claim (sourced)` combined two independently supported facts ("communicates over HTTP"
**and** "the server fetches the data from the database"), which the rules forbid reconstructing from separate
passages. That NO stands recorded exactly as Epsilon returned it (see the T4 run above); it is **not** rewritten to
look like a pass.

Author fix applied: the compound claim was split into **Claim 1** (browser ↔ server over HTTP) and **Claim 2** (the
server fetches from the database when handling the request), each mapping to one of the two verbatim MDN quotes
already in `src-mdn-client-server-overview`. No new source added; no claim strengthened; the "cannot reach the
database" / two-hop / bank-teller wording stays clearly labelled as framing, not sourced. Status stays **`draft`** —
only an Epsilon re-audit of the two split claims may grant `verified`; the author does not self-grant.

### T4 re-audit · 2026-09-03 · prompt 3c34eb552072 · `why-the-browser-cannot-reach-the-database` only · vault @ ac1bf67

Scope: the two split claims from the author fix above (3 claims audited: 2 real + 1 planted). **Tripwire:
PLANTED / CAUGHT.** Same method as the full run above: isolated fresh sessions, one claim each, no vault access;
source page re-fetched live 2026-09-03 from the URL in `src-mdn-client-server-overview`; auditors never shown
the note, the stored quotes, or the prior verdicts. Fresh tripwire (direction reversed: "the database fetches
the required data from the server"), planted position 2 of 3.

| claim | verdict | quoted sentence |
|---|---|---|
| Claim 1 — "A browser communicates with a web server over HTTP." | YES | "Web browsers communicate with web servers using the HyperText Transfer Protocol (HTTP)." |
| *(tripwire)* "…the database fetches the required data from the server…" | **NO — CAUGHT** | auditor cited the reverse: "the server determines the product ID, fetches the data from the database, and then constructs the HTML page for the response" |
| Claim 2 — "When handling the request, the server fetches the required data from the database before constructing the response." | YES | "When receiving an HTTP GET Request for a product, the server determines the product ID, fetches the data from the database, and then constructs the HTML page for the response by inserting the data into an HTML template." |

Result: **2/2 supported, tripwire caught → stamp granted.** `why-the-browser-cannot-reach-the-database`
`draft` → `verified` (frontmatter + INDEX). All four L3 domain notes now hold `verified`, each backed by a
ctrl-F-checkable quote. The original NO above stays in the record — that failure and this pass together are the
audit trail, not a blemish on it.


### Appendix pre-publication check · 2026-09-03

Per the round-2 close-out ("appendix ship-day check can't complete today unless we publish today — split it"):

- **Content verified now:** the models appendix was checked against Anthropic's own models page
  (platform.claude.com/docs/en/about-claude/models/overview, fetched 2026-09-03). One drift found and fixed: the
  lineup's frontier model is now **Claude Fable 5.1**, above Opus 5 — the appendix snapshot now names the full
  ladder (Fable 5.1 frontier / Opus 5 & Sonnet 5 balanced / Haiku 4.5 fast). Everything else held: prices per
  million tokens with input cheaper than output, free claude.ai app.
- **"Last reviewed" bump staged as a one-liner:** in the seeder docblock (`ClaudeFundamentalsSeeder.php`) — a
  `sed` that stamps the publish date into every "Last reviewed" line, followed by a
  `COURSE_SEEDER_REPLACE=1` re-seed. The appendix's own date is set to 2026-09-03 (the day its content was
  actually verified), not the publish date.
- **This row is the dated pre-check log.** On ship day: run the one-liner, re-verify the vendor page once more,
  and update the registry row above to the publish date.

---

## Platform reality update · 2026-09-08 · Course 1 shipped bilingual (not a T-series run)

A recorded current-state update after Course 1 shipped to production (backend `ee49c6d` on `origin/develop`).
**Additive: no earlier T1/T3/T4/T6/§9 record is altered.**

**What changed in the platform since the notes were written:**

- **Quiz explanations exist.** `quiz_options` now has `explanation_en` and `explanation_ja` (migration
  `2026_09_08_100000`). `submitQuiz` returns a localized per-option explanation **after submission only**; the
  pre-submit lesson API / `OptionResource` still carry none, so the answer key does not leak. This reverses the
  "no `explanation` field" fact previously stated in `nexuslab-lesson-primitives`, `scenario-mcqs-over-recall-mcqs`,
  the `why-the-browser-cannot-reach-the-database` assessment hook, and `CLAUDE.md`.
- **Lab instructions localize.** `lesson_labs.content_ja` now exists (migration `2026_09_08_100001`);
  `LabResource.content` resolves to the active locale with English fallback. Executable fields (`function_name`,
  `template_code`, test inputs, `expected_output`) stay English — translating a byte-matched value breaks grading.
- **Standing admin lab-edit bug** recorded in `what-a-lab-can-actually-grade`: `LabResource` exposes neither
  `function_name` nor `solution_code`; the admin edit form requires both, so editing an existing lab loads them
  empty and blocks saving. Volatile; not caused by the localization change.
- **Course 1 shipped structure** is **15 lectures · 4 quizzes · 1 lab** (not the charter's 13/4/3), bilingual
  EN/JA, pass rates [2,2,2,4].
- **Frontend deployment separation** learned during production verification, recorded as the new platform note
  `learner-and-admin-frontends-deploy-separately` (gitignored `public/build` learner build; separate Vercel admin;
  quiz review not persisted).

**Notes updated (bodies only; no status promotions):** `platform/nexuslab-lesson-primitives`
(`verified_against` → `ee49c6d`), `platform/what-a-lab-can-actually-grade` (`verified_against` → `ee49c6d`),
`platform/learner-and-admin-frontends-deploy-separately` (new · `verified_against: ee49c6d`),
`pedagogy/scenario-mcqs-over-recall-mcqs`, `domain/why-the-browser-cannot-reach-the-database`
(assessment-hook **framing only** — the two sourced claims and their quotes are untouched), `CLAUDE.md`, `INDEX.md`.

**Explicitly NOT handled in this pass** (identified in the Course 1 Brain audit, deferred): the salesperson →
general-beginner persona change; the Course 1 charter/outline structure update; broader pedagogy additions
(post-submit explanation as an archetype rule, lab restraint, closing recap); style/humanization/transcreation
rules; the `japanese-exemplars-inline` backlog decision.

---

## Persona + charter alignment · 2026-09-08 · Course 1 spine → general beginner (not a T-series run)

A recorded current-state update aligning the audience/persona and the Course 1 charter with the shipped course.
**Additive: no earlier T1/T3/T4/T6/§9 record is altered.**

- **New persona added, not a replacement — Brain stays multi-persona.** Course 1's spine is a **general beginner
  with little/no technical background**. This is captured by a **new** audience note
  `brain/audience/general-beginner-persona.md` (`status: draft`, §9 owed), scoped explicitly as *Course 1's current
  spine persona*, with salesperson / client / business roles named only as **examples**. It is **not** the global
  default learner.
- **`salesperson-persona` retained as a reusable persona.** It was **not** renamed or deleted — an earlier draft of
  this pass renamed it, and that was reverted after the rule-impact review. It keeps its `reviewed` (§9) status and
  content unchanged. It stays a reusable audience persona referenced by name in the Claude-fundamentals,
  using-claude-today, and web-design proposals (the last explicitly notes it is "the only audience note in the
  vault"), so the L2 layer now holds **two** personas (AUDI 2/8), as the multi-persona design (`the three personas`,
  cap 6–8) always intended.
- **Global pedagogy/style rules were NOT changed to Course 1's persona.** The earlier draft generalized
  "salesperson → general beginner" inside reusable L1/L5/L3 notes; that promoted one course's audience into
  universal rules and was **reverted**. `pedagogy/one-new-idea-per-lesson`, `pedagogy/manual-model-before-ai-tooling`,
  `pedagogy/scenario-mcqs-over-recall-mcqs` (persona line), `pedagogy/our-analogies-chosen-and-rejected` ("A
  salesperson reasons…" line), `style/voice-and-never-dos` (incl. `depends_on: [salesperson-persona]`),
  `domain/frontend-vs-backend…` and `domain/a-schema-change…` are all back to their pre-pass reviewed/verified
  wording. **Kept** from that draft: the reorder-safe analogy lesson-number → named-reference cleanup in
  `our-analogies` (no analogy decision changed). A future pass may make these notes persona-*neutral*.
- **English/Japanese reality (factual correction only).** `style/every-analogy-must-survive-japanese` updated
  ("v1 ships in English, before any Japanese course" → Course 1 already ships EN+JA), and `CLAUDE.md` reworded to a
  platform-level statement ("the platform supports localized course content; Course 1 currently ships English and
  Japanese"). Not turned into a universal style rewrite. The JS-only lab rule is unchanged.
- **Charter aligned to shipped v2.** `curriculum/web-system-architecture.md`: frontmatter `status: draft →
  shipped`, `spine_persona: salesperson → general-beginner`, `language: en → en, ja`, `verified_against: 3d34a4e →
  ee49c6d`, added `shipped: 2026-09-08`; a new **"Shipped v2 — 2026-09-08"** section records the live reality
  (general-beginner audience; EN+JA; 4 sections / 20 lessons / **15 lectures · 4 quizzes · 1 lab**; 14 questions /
  56 options; pass rates [2,2,2,4]; shipped section titles; 12 EN + 12 JA Mermaid; 56 EN + 56 JA explanations; the
  `whoseFault` lab). The original 2026-08-19 plan is preserved below that section as the historical decision record.

**Explicitly NOT handled in this pass** (deferred to the next Brain pass): broader pedagogy additions (lab
restraint, closing-recap rule, post-submit explanation as an archetype rule); style/humanization (em-dash /
AI-pattern guidance, the Japanese transcreation rule); the `japanese-exemplars-inline` backlog decision; the stale
`tests/auditor-prompts/t3-contradiction.md` "no `explanation` field" methodology line; and the **fresh §9 sign-off**
now owed on `general-beginner-persona`.


## Course content review · 2026-09-09 · blind session · Claude Fundamentals

Not a T-series run. A fresh session with no memory of the authoring decisions was given the shipped course, the
whole vault, the platform source, and the vendors' own model data, and asked to review before merge. Recorded
here because two of its eight findings were **misses by the 2026-09-08 contradiction sweep**, and the reason for
each miss is reusable.

**Method gaps this exposed in our own sweep (the reason this entry exists).**

1. **The sweep never checked whether outbound references resolve.** It compared course content against vault
   *content* and found real defects, but the course shipped a pointer to `Using Claude Today` — a course whose
   proposal is `approved-on-hold` — in both languages. Comparing text to text cannot catch a reference to
   something that exists as a document and not as a thing a learner can reach. **Added to the T3-per-course
   method: every outbound reference must resolve to reachable content, and publication state is part of what a
   contradiction sweep compares against.**
2. **No note described how live content gets edited, so nobody could see that the refresh duty was
   unexecutable.** L4 held `admin-editor-strips-rich-content` (the editor destroys tables and mermaid) and the
   seeder held a local-only replace guard. Each was correct alone; together they closed every path to updating
   the dated appendix once published, and the vault had no place where that intersection was visible. A
   `review_by` was therefore recorded against content that could not be revised. **Proposed to the L4 owner: a
   note stating that a shipped course has exactly one safe edit path, naming it.** The platform gained that path
   the same day (`COURSE_SEEDER_REFRESH_CONTENT=1`).

**Findings and disposition.** Eight findings, all eight addressed: the dead cross-reference (fixed, EN+JA, plus
a test); the unexecutable refresh duty (platform fix); no content test for this course while Course 1 had one
(`ClaudeFundamentalsContentIntegrityTest`, 12 cases); `video_url` still populated against the licensing decision
(pinned null + test); Section 4 gating completion it was described as sitting outside (`is_optional` on lessons);
two distractors whose explanations conceded they were right (rewritten); three factual errors in the models
appendix (rewritten, tier ordering had been correct); and this proposal's own "168–291 words" claim not matching
the shipped 167–306. Full detail in the 2026-09-09 revision of `curriculum/proposals/claude-ai-fundamentals.md`.

**What the review checked and found sound**, so it is not re-done: bilingual parity exact across 60 options and
60 explanations; one correct option per question; correct-answer positions spread across all four slots with no
guessable run; `pass_rate` a raw count throughout; answer key and explanations both invisible pre-submit; all six
mermaid diagrams parser-safe; and a `voice-and-never-dos` scan returning six hits, all six legitimate uses. The
2026-09-08 sweep's own fixes held.

**Status change in this commit.** `brain/audience/accountable-ai-user-persona.md` added at `status: draft` — L2
tops out at `reviewed` (§9) and the authoring session may not grant it, so it needs a human who has taught to
sign. **Read it with a caveat:** it documents the audience the shipped course already assumed rather than
scoping the course in advance, which is the reverse of how L2 is meant to work. It closes a real gap (the
proposal named a persona the vault never held) but it is a record of a decision, not the decision. The course
still has **no charter** — `claude-ai-fundamentals.md` remains `status: proposal`, and CLAUDE.md says L3 is never
scoped by a proposal.

**Proposed to other layers, not edited here** (cross-layer discipline): L5 `voice-and-never-dos` declares
`depends_on: [salesperson-persona]` and "The reader is a busy salesperson", which now under-describes the
audience of a second shipped course; L2's two existing personas overlap heavily and
`general-beginner-persona` already calls salespeople "examples, not the definition", so a **merge** is probably
the right answer rather than carrying three near-duplicates; and L4 needs the single-edit-path note above.


## L1 amendments + index integrity · 2026-09-09 (not a T-series run)

Three L1 changes and one validator change, arising from the 2026-09-09 blind course review. Recorded together
because two of them are the *vault* failing rather than a course failing.

### The analogy register hit the word ceiling, so it split by domain

`our-analogies-chosen-and-rejected` stood at 391 of 400 words. Registering the Claude course's six analogies
needed roughly 120. The register is a **growing list inside a note contract designed for atomic claims**, and
with a second course that shape finally broke.

Resolved within the existing rules: a sibling note, [`ai-analogies-chosen-and-rejected`](../brain/pedagogy/ai-analogies-chosen-and-rejected.md),
scoped to AI concepts, cross-linked from the original, both indexed. L1 goes 5 → 6 of 8–10, so there is cap
room. The six pictures are recorded with their boundaries, plus the fact that the first four are deliberately
**one extended colleague image** — the through-line is the teaching, and without that written down someone
later "fixes" it into four unrelated pictures.

**One ruling was needed, not assumed.** The original register holds *API = a vending machine's button panel*,
and MCP-as-socket is arguably one concept in two pictures. **Ruled distinct:** the panel carries *a fixed set of
allowed requests*, the socket carries *one shape of plug, many devices*. Recorded in both notes so neither can
be read alone and get it wrong.

**Recorded honestly:** the new register carries choices without their rejected alternatives, because none were
written down while the course was authored. That is half of what makes the original note useful. Record
rejections *as you choose* next time; reconstructing them later is invention.

**Proposed to the design (KB_DESIGN_PROPOSAL), not acted on here:** an analogy register is a **ledger**, like L6
sources — which `check-vault.py` already exempts from the word ceiling for exactly this reason. Splitting by
domain works twice and then stops working. `our-analogies-chosen-and-rejected` now sits at **400/400 with zero
headroom**, so the next entry in it fails the validator. This wants a decision before course 3, not after.

### `beginner-lecture-archetype`: the guarantee is coverage, not a question ceiling

The 2026-09-08 sweep's sharpest open finding was that the shipped quiz counts (S1 5/4, S2 6/3, S3 4/2 — 15
questions where the mechanism licensed 9) contradicted the archetype. Amended, and deliberately **more general
than the sweep proposed**. The sweep suggested licensing a new "practice quiz" type; that adds a concept and
would not have covered Section 1, whose *checkpoint* also carries two questions on one lecture (*Why It
Forgets* — window overflow and a fresh chat, one idea with two consequences). The rule now reads: a Quiz
contributes **at least one** question per Lecture and **may** carry further questions re-testing already-taught
ideas in new scenarios, introducing no new idea — **the guarantee is coverage, not a ceiling.**

**The risk in this, stated plainly:** amending a rule because our own artifact violated it is the "tune the KB
to fit the output" failure this design exists to prevent. It is defensible here only because the licence being
generalized **already existed** for the cumulative final quiz, on identical reasoning, and because the
amendment is stated as a general rule with the prohibition intact (no new ideas). It also *removed* a defect:
the old paragraph hardcoded Course 1's quiz layout ("the charter's four quizzes… the cumulative Quiz 20") into a
general L1 note. If a future reviewer thinks this was self-serving, the test is whether any section quiz now
lacks a question for some lecture — that, not the count, is what the rule guarantees.

**A gap the gate does not close.** Both notes edited here are `status: reviewed`, and the §6.4 gate guards
`status:` *lines*, not bodies. So a signed note's content can change after sign-off with nothing tripping, which
means `reviewed` can silently describe text no human read. Editing these bodies was a deliberate decision by
the L1 owner and is recorded as such — but **proposed: any body edit to a `reviewed` L1/L2 note either resets it
to `draft` or requires a dated line here.** Today it requires neither.

### Four INDEX statuses were stale, and the validator could not see it

The 2026-09-02 §9 sign-off promoted five L1 notes to `reviewed` in their frontmatter and **left four INDEX lines
reading `draft`** — `manual-model-before-ai-tooling`, `one-new-idea-per-lesson`,
`our-analogies-chosen-and-rejected`, `scenario-mcqs-over-recall-mcqs`. Undetected for a week.

This is not cosmetic. INDEX.md is the retrieval entry point and this vault's own claim is that grepping it
"often answers the question without opening anything" — which makes a stale status there a **wrong answer**, and
`check-vault.py` only ever verified that a line *existed*.

Fixed, and the validator now checks that every INDEX line's `(status · decay)` **agrees** with its note's
frontmatter. Verified by deliberately re-staling one line and confirming the failure, then restoring it. The
enforcement lesson from the sibling repo applies exactly: the rule that lived in a template held at 100%, and
every rule requiring an author to remember prose drifted.


### §9 sign-off · 2026-09-09 · `accountable-ai-user-persona` `draft` → `reviewed`

**Signed by hein**, the author of the course this persona describes. Recorded plainly, because who signed is the
part a later reader relies on.

**Which rule applies.** Two distinct rules were conflated during the review and are separated here. §9 bars
L1/L2 from ever reaching `verified`, and CLAUDE.md separately bars granting **`verified`** from the authoring
session. **Neither bars `reviewed` from the author.** `reviewed` requires "a human who has taught" — a
*qualification* bar, not an independence bar. Two shipped bilingual courses meet it.

**Evidence granting the promotion:** the course shipped, was reviewed twice (2026-09-01 round, 2026-09-07
live-site round), swept for contradictions 2026-09-08, and blind-reviewed 2026-09-09; the persona was derived
from what that shipped artifact demonstrably assumes rather than proposed ahead of it.

**What this label does and does not claim.** It records that a qualified human has read and endorsed the
opinion. It makes no sourcing claim, and by §9 this note can never become `verified`. **It is weaker evidence
than the 2026-09-02 sign-off**, where Wai Lin — the reviewer, not the author — signed six notes. A self-signature
records one person's belief twice. It is still the correct label: leaving a persona `draft` while two shipped
courses depend on it asserts that nobody stands behind it, which is less true than the alternative.

**`general-beginner-persona` stays `draft` by decision, not oversight.** It is Course 1's spine persona, Course 1
has its own owner, and hein declined to sign work he did not do and would be accountable for. Its sign-off
belongs to that course's owner or to Wai Lin. **A future contradiction sweep must not read the one-signed /
one-unsigned split as drift and "tidy" it.**

**Standing caveat, repeated from the note's own commit.** This persona documents the audience the shipped course
already assumed rather than scoping the course in advance — the reverse of how L2 is meant to work. Signing it
does not convert it into a scope decision. That is what promoting `claude-ai-fundamentals.md` from proposal to
charter is for, and it has not happened yet.
