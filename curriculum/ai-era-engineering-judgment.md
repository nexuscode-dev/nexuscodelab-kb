---
id: ai-era-engineering-judgment
slug: ai-era-engineering-judgment
status: shipped             # published 2026-09-14
proposed_by: hein
date: 2026-09-11
promoted: 2026-09-14
shipped: 2026-09-14
course_slot: 3
spine_persona: delegating-engineer
language: en, ja
length_weeks: 3
pathway: AI-Era Software Engineering
verified_against: d653bf3
---

# Course proposal — AI-Era Engineering Judgment

This is not a note and is exempt from the 150–400 word cap. It is the **scope decision** for course 3 —
neither knowledge (`brain/`) nor output (`courses/`).

This is not a note and is exempt from the 150–400 word cap. It is the **scope decision** — neither knowledge
(`brain/`) nor output (`courses/`). L3 for this course's concepts is scoped by this file and by nothing else.
Promoted from proposal on 2026-09-14, alongside signing `delegating-engineer-persona`.

**Published 2026-09-14**, by a human running `db:seed --class=AiEraEngineeringJudgmentSeeder` against
production — the first time that path has been exercised (`docs/course-1-publish-checkpoint.md` had recorded it
as never used). Merging publishes nothing here: no course seeder is registered in `DatabaseSeeder`, nothing runs
`db:seed` automatically, and there is no CI. Publishing is that command and nothing else.

**Ship-day duties completed:** Section 4's "Last reviewed" bumped to 14 September 2026 in both languages after
re-reading it (it names no product and quotes no price, so nothing had gone stale); `verified_against` moved to
`d653bf3`; the content-review registry row updated. **Standing:** the Japanese ships unreviewed by decision, and
that debt is now live rather than pending.

## Current shape — 2026-09-14 (supersedes the rough structure below)

- **Spine persona.** `delegating-engineer-persona`, signed `reviewed` 2026-09-14. An engineer who reads and
  writes code, hands substantial implementation to an AI tool, and merges the result under their own name. The
  pathway's first persona that is *not* its entry persona.
- **Structure.** 4 sections · **16 lessons — 12 Lecture · 3 Quiz · 1 Lab.** Quizzes hold **14 questions / 56
  options**, every option with a post-submit explanation in both languages. Lectures run 155–278 words.
- **The lab ships deliberately broken in exactly one case** — `averageRating` passes the happy paths and fails
  on the empty list. The defect *is* the exercise. **Three test cases, not four**: each case costs a free
  learner one of ten daily code executions, and this lab's method is run → read the failure → fix → run. Four
  cases bought two attempts a day; three buys three.
- **Section 4 is a dated reference lecture** outside the learning path, with no quiz on it. Registry row and
  `review_by` in `tests/audit-log.md`.
- **Analogies.** Five recorded in `delegation-and-review-analogies` *with their rejected alternatives* — the
  discipline the sibling register asked the next course to start. Two more are reused unchanged from
  `ai-analogies-chosen-and-rejected` rather than reinvented, which is the registers working as designed.
- **Japanese ships unreviewed.** Decision 2026-09-14: publish, and a Japanese-reading reviewer signs off after
  the fact. A recorded debt, not a satisfied gate — and it is now outstanding on two courses.

## L3 and the cap decision this still forces

**Zero L3 notes exist for this course's concepts**, so no distractor here carries the provenance
`scenario-mcqs-over-recall-mcqs` requires; they are drawn from the persona note instead. Promoting this charter
makes such notes *legitimate* to write and does not make room for them: L3's cap is 12–15, Course 1 holds 13, and
there are now **two charters** queued behind that cap rather than one. A cap is never raised mid-build
(KB_DESIGN_PROPOSAL §7.1), so this is a v1-review decision, and it has gone from one course's problem to a
standing block on the pathway.

## Where it came from

The 2026-09-10 internal meeting on the platform's shift toward career pathways divided the new course work by
**stage of work**, so three courses can be written in parallel without overlapping:

| Course | Stage | Author |
|---|---|---|
| AI-Era Software Engineering Workflow | the whole chain, end to end | Astro |
| AI-Era Solutions Architect | architecture and design | Onyx |
| **AI-Era Engineering Judgment** | **delegation, review, iteration** | hein |

The stage this course takes is the one the direction-setting message singled out: *"the engineer's value is
increasingly in engineering judgment: knowing what to build, how to build it, what to delegate to AI, and
critically evaluating whether the result is actually correct, useful, secure, maintainable and aligned with the
client's needs."*

## Target learner

`delegating-engineer-persona` — an engineer who reads and writes code, hands substantial implementation to an
AI coding tool, and merges the result under their own name. **Not `accountable-ai-user-persona`**, which is
explicitly "never a builder" and "will never need … API code". That persona is the pathway's entry point and the
spine of Claude Fundamentals; this one is the next step along the same pathway.

The persona note ships `status: draft` and is flagged for human sign-off, the gate `accountable-ai-user-persona`
went through. Its standing caveat applies: it was written alongside this course rather than ahead of it.

## Why this course

Two reasons, and the second is the one that makes it durable.

Every organisation using these tools has acquired a review problem it has not named: output arrives faster, in
larger pieces, and more uniformly polished than review habits built on human code can handle. Nothing on the
market teaches the review side; the material all teaches generation.

And unlike most of what the pathway direction proposes — tool lists, prompt libraries, MCP recommendations,
industry updates — **judgement criteria do not rot.** "Delegate what you can check on arrival" will be true
after the current tool generation is forgotten. This course is deliberately on the durable side of the pathway,
which is also why it can afford to be built once and left alone.

## What learners will learn

Delegate by verifiability rather than by boredom · the brief is the spec, and everything unstated was decided
for you · how AI output fails differently from a colleague's · read the diff, not the explanation · spend
scrutiny at the seams · why tests written by the same tool prove very little · the four things AI output misses
most (secrets, input, failure, reach) · steer rather than regenerate · when to stop delegating · that merging is
signing.

## Rough structure

4 sections · 16 lessons — 12 Lecture · 3 Quiz · **1 Lab**. Same size and archetype as Claude Fundamentals, EN +
JA in one tree, every quiz option carrying a post-submit explanation in both languages.

S1 "What to delegate, and what never to" (opens with a Start Here orientation lesson) → S2 "Reviewing what comes
back" (closes with the Review Clinic practice quiz) → S3 "Iterating and owning it" (holds the lab) → S4
"Reference (dated)", one perishable lecture outside the learning path with no quiz on it.

## Platform fit

**The lab is the notable difference from Claude Fundamentals, and both decisions follow from the same rule.**
A Lab here is JavaScript graded on stdout and cannot call a model (`what-a-lab-can-actually-grade`), so any lab
is a coding exercise. That was wrong for a non-technical persona and right for this one. The lab ships plausible
AI-written code whose happy path passes and whose empty-list seam does not; the learner has to find that by
reading. A test asserts the shipped template fails exactly one case, because that defect *is* the teaching.

Quiz shape is single-answer MCQ with `pass_rate` as a raw count. The Review Clinic carries six questions for
three lectures, which `beginner-lecture-archetype` now licenses directly — "the guarantee is coverage … not a
question ceiling" — rather than needing an amendment after the fact, as the Prompt Clinic did.

## What we deliberately are not teaching

Prompt engineering as a subject (Claude Fundamentals covers the useful half; the rest is folklore) · how to
build agents or frameworks · model internals or benchmarks · specific product tutorials, which live in the dated
S4 page and nowhere else · the workflow and architecture stages, which belong to Astro's and Onyx's courses ·
anything requiring monthly updates outside S4.

## Open questions / risks

1. **The persona needs a human sign-off** before this is promoted. Everything else here is downstream of it: if
   the audience is wrong, the course is wrong.
2. **L3 provenance gap, declared.** `scenario-mcqs-over-recall-mcqs` wants each distractor to be the
   misconception a matching Domain note names, and no L3 note exists for these concepts. It *cannot* exist yet —
   "L3 is never scoped by a proposal" — so distractors come from the persona note's misconception list instead.
   This closes the way Claude Fundamentals' did: on promotion to charter. Candidate L3 notes are then
   delegation-by-verifiability, the explanation-is-not-evidence property, and same-author test dependence.
3. **Overlap risk with Astro's workflow course** is real and mitigated only by the stage split agreed in the
   meeting. Worth one cross-read between the two courses before either is promoted.
4. **Japanese awaits a reviewer**, as with course 2. Written alongside the English; the author of a translation
   is not its reviewer.
5. **Level.** Shipped as `intermediate` rather than `beginner` — the first of my courses not aimed at a
   beginner. Whether the pathway wants that gradient, or wants everything reachable from zero, is a product
   decision I have not taken.
