---
id: ai-era-engineering-judgment
slug: ai-era-engineering-judgment
status: proposal            # NOT a charter — awaits team approval. L3 is never scoped by a proposal.
proposed_by: hein
date: 2026-09-11
course_slot: 3 (proposed)
spine_persona: delegating-engineer (draft, pending sign-off)
language: en, ja
length_weeks: 3
pathway: AI-Era Software Engineering
verified_against: 0232881
---

# Course proposal — AI-Era Engineering Judgment

This is not a note and is exempt from the 150–400 word cap. It is the **scope decision** for course 3 —
neither knowledge (`brain/`) nor output (`courses/`).

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
