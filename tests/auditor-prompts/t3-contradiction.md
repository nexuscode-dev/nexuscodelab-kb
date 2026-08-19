# Auditor prompt — T3, contradiction sweep

**Version 1 · 2026-08-19.** Record this file's hash with each run in `audit-log.md`.

## How to run it

A **fresh session** whose *only* job is to find conflicting claims. Do not combine it with any other task — a
session asked to both improve and audit will improve, because that feels more productive.

**Pass condition: zero conflicts.**

## The prompt

> Read every file in `brain/` and in `curriculum/`. Your only job is to find **claims that contradict each other**.
> You are not improving anything, not summarising, and not assessing quality. Do not fix what you find.
>
> Report each conflict as: the two note ids · the two claims quoted verbatim · which layers they sit in · and whether
> a course generated from this vault would have to pick one.
>
> If you find none, say so plainly. Do not invent a conflict to appear thorough. But before concluding none exist,
> check the four places they hide:
>
> 1. **A pedagogy rule that assumes knowledge a persona note says the learner lacks.** This is the highest-value
>    class and the reason ownership groups L1 and L2 together.
> 2. **A domain note whose assessment hook needs a platform capability an L4 note says does not exist.** Cross-check
>    every assessment hook against the lesson primitives — single-answer MCQ only, no `explanation` field.
> 3. **Two notes using different analogies for the same concept**, or the same analogy for two concepts.
> 4. **A note whose claim rests on a platform fact that has since been corrected.** Run
>    `grep -rn "depends_on:" brain/` and check each dependency still says what the depending note assumes.

## Why this test exists

A knowledge base has no compiler. Two independently written notes *will* disagree, and **nothing will tell us** —
generation then silently picks one. A vault that passes T2 and fails T3 produces good lessons that quietly
contradict each other, which is harder to detect downstream than a bad lesson.

Solo, this test keeps its full force: it is a whole-vault read against itself, and knowing who wrote what does not
help.
