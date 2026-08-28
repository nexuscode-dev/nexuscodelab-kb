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

3 weeks · 3 sections · ~14 lessons — 10 Lecture · 3 Quiz · 1 optional JS lab.
S1 "What the machine is actually doing" → S2 "Getting good work out of it" → S3 "AI connected to real systems",
plus the volatile appendix as one clearly-dated lecture.

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
2. **Commoditization** — why ours over Anthropic's free one? Our answer must be: sequenced for *our* personas,
   in our learners' context, and built on course 1's foundations. If that isn't credible, this course shouldn't
   exist.
3. **Decay** — the appendix needs a standing `review_by` and a named owner, or it ships stale within a quarter.
4. **Reuse dependency** — S3 leans on course 1's API and client-server notes (the brain thesis paying off), so
   this course generates **second**, never in parallel with course 1.
