---
id: claude-ai-fundamentals
status: proposal            # NOT a charter — awaits team + Leon approval; L3 is never scoped by a proposal
proposed_by: hein
date: 2026-08-28
course_slot: 2 (proposed)
---

# Course proposal — Working With AI: Claude Fundamentals

Working title chosen deliberately over "Claude 101" — see risks.

## Target learner

The career-switcher and student from our persona set — people who will build or work alongside AI tools.
The salesperson gets standalone value from weeks 1–2 (how these systems work, how to ask well) and can stop
there; sequence is ungated, so that costs nothing.

## Why this course

Most-requested topic and the strongest acquisition hook — but also the most commoditized (Anthropic ships its
own free Claude course; DeepLearning.AI too) and the fastest-decaying (roughly ten model releases in 24 months).
So it only makes sense built on the **durable core** — how these systems work and how to work with them — with
every perishable fact (model names, prices) isolated in one thin, dated appendix we can refresh without touching
the rest. Inherited recommendation from Leon's design review: consider shipping it **free, as acquisition**,
rather than paid — open question 1.

## What learners will learn

What a model actually does (tokens, context, why it forgets, why it makes things up) · how to ask so it answers
well — patterns, not magic phrases · what "agentic" means: tools, steps, checking its own work · MCP as the
cross-vendor standard for connecting AI to real systems · when *not* to use AI · a dated appendix: today's
models and prices, clearly marked perishable.

## Rough structure

3 weeks · 3 sections · 15 lessons — 11 Lecture · 3 Quiz · 1 optional JS lab.
S1 "What the machine is actually doing" → S2 "Getting good work out of it" → S3 "AI connected to real systems".
The perishable surface is exactly two clearly-dated lectures, both in S3: the models appendix and a one-lesson
"Using Claude Today" orientation that maps product features back to the course's concepts and out-links to the
fuller product-tour course (see `using-claude-today.md`).

## Platform fit

Mostly Lecture + scenario MCQ — a genuine fit, since the teaching is conceptual. **One hard limit shapes
everything: labs have no network access (§11.4), so a lab can never call an AI model.** Hands-on Claude use
happens through out-links to claude.ai, not graded labs. The one lab that works is pure-JS context-budget
arithmetic — deterministic, stdout-matched. Mermaid covers all architecture visuals natively (§11.2).

## What we deliberately are not teaching

Prompt-engineering folklore ("magic words") · API coding (a dev course's job) · model comparisons and benchmarks
(perishable, vendor-marketing territory) · fine-tuning and training · anything that would need updating monthly
outside the appendix.

## Sample lesson idea

*"Why it makes things up"* — the confident-wrong-answer phenomenon explained through the one durable idea: it
predicts plausible text, it does not look things up unless connected to something that does. Scenario MCQ: "The
AI cited a court case that doesn't exist. What happened?" — every distractor a real folk theory.

## Open questions / risks

1. **Free-as-acquisition vs paid** — changes the quality bar and the appendix's refresh duty. Leon's call.
   **DECIDED 2026-09-02 (Wai Lin): free for v1, revisit when billing exists.** Rationale: the goal is onboarding
   test users, and the platform has no billing capability today. This settles the quality bar and refresh duty.
   It does **not** reopen the licensing decision — the videos stay plain links at any price point, because
   3Blue1Brown's licence terms do not turn on our pricing.
2. **Commoditization** — why ours over Anthropic's free one? Our answer must be: sequenced for *our* personas,
   in our learners' context, and built on course 1's foundations. If that isn't credible, this course shouldn't
   exist.
3. **Decay** — the appendix needs a standing `review_by` and a named owner, or it ships stale within a quarter.
4. **Reuse dependency** — S3 leans on course 1's API and client-server notes (the brain thesis paying off), so
   this course generates **second**, never in parallel with course 1.

## Revision after review — 2026-09-01

Updated to match the shipped seeder (`ClaudeFundamentalsSeeder.php` @ platform `develop`) after the 2026-09-01
review of this course:

- The shipped course now carries this proposal's title, **Working With AI: Claude Fundamentals** (an interim
  "Claude 101" title was reverted per this proposal's own commoditization reasoning).
- A four-lesson "Meet Claude" product-tour section that had crept in post-proposal was removed per the review;
  its content moved to a separate proposal, `using-claude-today.md`, so this course's perishable surface stays
  at two dated lectures (~18% of lectures) with no quiz over product-UI facts.
- All lectures now follow `beginner-lecture-archetype` (Misconception + Takeaway present in 11/11).
- Open question 3 (decay ownership) is now answered by the content-review registry in `tests/audit-log.md`
  (owner: hein · review_by 2026-12-01).
- The two YouTube references are now **optional plain links, not embeds** (resolved 2026-09-01): 3Blue1Brown's
  reuse policy (3blue1brown.com/about) asks for a licensing inquiry for course-material use beyond short
  attributed clips, so we link out instead — linking needs no permission. Re-adding embeds requires written
  approval via his contact form first.
