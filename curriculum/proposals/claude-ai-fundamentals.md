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

3 weeks · **4 sections · 15 lessons — 12 Lecture · 3 Quiz · no lab** (revised 2026-09-07, below).
S1 "What the machine is actually doing" (opens with a Start Here orientation lesson) → S2 "Getting good work out
of it" (closes with the Prompt Clinic scenario quiz) → S3 "AI connected to real systems" → **S4 "Reference
(dated)"**, holding the two perishable lectures — the models snapshot and the one-lesson "Using Claude Today"
orientation — outside the learning path, with no quiz on them.

## Platform fit

Mostly Lecture + scenario MCQ — a genuine fit, since the teaching is conceptual. **One hard limit shapes
everything: labs have no network access (§11.4), so a lab can never call an AI model.** Hands-on Claude use
happens through out-links to claude.ai, not graded labs. The one lab that works is pure-JS context-budget
arithmetic — deterministic, stdout-matched. Mermaid covers all architecture visuals natively (§11.2).
**Superseded 2026-09-07:** that lab was cut and no lab replaces it — see the revision note below.

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
4. **Reuse dependency** — **corrected 2026-09-08 after a contradiction sweep.** As written this said "S3 leans
   on course 1's API and client-server notes". The shipped course does not: a grep of the learner-facing tree
   returns zero occurrences of API, browser, HTTP or request/response, because the course deliberately avoids
   web-architecture vocabulary for a non-technical reader. Course 1 remains the recommended *sequence*
   (`manual-model-before-ai-tooling`), but this course does not depend on its notes and stands alone. The
   claim, not the course, was wrong.

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


## Revision after the live-site review — 2026-09-07

Wai Lin walked the published courses as a student and reported: no course-level introduction, no opening hook,
abrupt lesson flow, lectures **too detailed**, and code labs inappropriate in a beginner AI course. Applied:

- **New orientation lesson** opens S1 ("Start Here: What This Course Changes for You") — states what the learner
  will be able to do, how the course runs, and pre-empts "I need to be technical for this". It carries a
  misconception and takeaway like every other lecture, but contributes no quiz question: its idea is orientation,
  not course content. Flagged to the archetype's owner rather than amending `beginner-lecture-archetype` here.
- **Every lecture cut to a ~3-minute read** (168–291 words, was 500–800), one idea each, plainer wording for a
  learner with no prior AI experience. Structure per the archetype is unchanged; only the detail is gone.
- **The lab is removed, and no lab replaces it.** A Lab on this platform is JavaScript graded on stdout and
  cannot call a model (`what-a-lab-can-actually-grade`), so the only lab this subject admits is code — which is
  exactly the objection. Prompt practice now runs as the **"Prompt Clinic: Fix the Brief"** scenario quiz (6
  briefs to diagnose, no code) plus an **ungraded try-it-in-claude.ai exercise** inside the Asking Well lecture.
  Note this reverses a decision round 1 praised ("the one lab is correctly chosen and correctly reasoned"); the
  reversal is Wai Lin's call, and the same question applies to Course 1's three optional labs.
- **Perishable content moved to S4, a dated reference section** after the last checkpoint, so the learning path
  ends on the S3 quiz and no quiz sits on model or product facts.
- **Course description rewritten** outcome-first, since that is the pre-enrolment surface that answers "what is
  this course about".
- **Per-option quiz explanations adopted.** `explanation_en` landed on `quiz_options` the same day
  (migration `2026_09_08_100000`), so all 60 options here now carry a one-sentence post-submit explanation
  following Course 1's pattern: correct options confirm the reasoning, wrong ones name the misconception. This
  retires the old constraint that all teaching had to be smuggled into distractor wording, and it is what makes
  shorter lectures safe — the detail now arrives at the moment the learner is actually wrong.
- **Japanese localization shipped (2026-09-08).** Full coverage following Course 1's `localizeJapanese()`
  pattern — course title/description, 4 section titles, 15 lesson titles, 12 lecture bodies, 3 quiz
  instructions, 15 question texts, 60 option texts and all 60 explanations — applied positionally after the
  English tree with count guards that throw rather than localize the wrong lesson. The shared curriculum row has
  no `*_ja` columns, so it stays English.
  **One lesson is deliberately not a translation:** the tokenization lecture teaches "one token is about four
  characters", which is an English fact. Japanese tokenizes far more densely, so the Japanese version carries
  its own example, its own rule of thumb, and the two practical consequences (context fills sooner, cost per
  page is higher). A literal translation would have taught Japanese readers something false about their own
  language — this is `every-analogy-must-survive-japanese` catching a real defect, not a stylistic preference.
  The remaining analogies (colleague answering from memory, USB socket, junior colleague with logins) are plain
  images and survive unchanged. **Awaiting sign-off from a Japanese-reading reviewer** — recorded in the
  seeder's method docblock; the author of a translation is not its reviewer, same principle as T4.
- **Frontend build is a separate deploy track.** The explanations were invisible on a local site whose
  `public/build` predated the feature by six days — `learner-and-admin-frontends-deploy-separately` catching
  exactly what it describes, one day after it was written. Merging the seeder does not ship the learner
  frontend: `public/build` is gitignored, so whoever deploys must rebuild it there.
- **Consistency question for the team:** Course 1 v2 keeps one optional JS lab while this course now has none.
  Whether a beginner course may contain a code lab at all should be one decision, not two.


## Pre-review contradiction sweep — 2026-09-08

Run before submitting for review rather than after, by a fresh session with no memory of the authoring
decisions, against the whole of `brain/` + `curriculum/` (the T3 method applied to one course). Recorded in
full because a found-and-fixed conflict is worth more than a clean claim.

**Fixed in the course (platform `develop`):**

- **Never-do words in the author's own voice** (`voice-and-never-dos`): "an **obvious** question follows" (MCP
  hook, and its Japanese 「当然の疑問」), "a document you can **simply** read" and "The text **simply** fell
  outside the window" (both in quiz explanations — my own earlier grep missed them because it scanned lecture
  bodies only). Allowed uses were correctly left alone: the quoted learner belief "so it can obviously handle an
  easy one", and "just as wrong" / "the case it just named" (different senses).
- **Analogy before the plain statement** (archetype §2→3, and `voice-and-never-dos`: "Never the reverse").
  *Asking Well* opened on the briefing-a-colleague analogy and *MCP* opened on the USB socket, both before
  saying plainly what the thing was. Both reordered, EN and JA.
- **A definition question dressed as a scenario** (`scenario-mcqs-over-recall-mcqs`: "None asks for a
  definition"). S3 Q1 asked "what does that actually describe?" over four definitions of *agent* — while the S1
  instructions promise "nothing here is a definition". Replaced with a judgement call: a colleague dismisses the
  tool as "a chatbot with a fancy name"; is the colleague right?
- **Filler distractors** ("this does not license a filler distractor"): "Someone tampered with the assistant",
  "It cannot — tools make no difference", and "Access limits are unnecessary" were all self-refuting in their own
  explanations. Replaced with real folk theories — it searched and the page was taken down; the model still
  writes the final answer so the number can still be wrong; start with full access and tighten later.
- **Hook grounding** (archetype §1: "never … a claim about how the audience behaves, unless the Brain grounds
  it"). "You have probably used an AI assistant at least once", "Two things you will notice every week", "People
  who get the most out of AI work in a loop", "usually two or three rounds", "change several times a year",
  "Every major AI company" — all rewritten as neutral statements, EN and JA.
- **Takeaway no longer closes the lecture** (archetype §6: "Close with one sentence"). Two lectures continued
  past it into optional out-links; the links now sit above the takeaway.
- **Registry date mismatch**: the S4 orientation lecture shipped "Last reviewed: 3 September 2026" while its
  registry row still read 2026-08-31. Row corrected — on a decay record the date is the part someone relies on.

**Open, and needing a decision rather than an edit:**

1. **Quiz question counts contradict the archetype's core mechanism — the sharpest finding.** The archetype
   requires each Lecture to contribute *one* question to its section's quiz, and licenses surplus questions in
   exactly one place: the cumulative final quiz, which this course does not have. Shipped counts are S1 5/4,
   S2 6/3, S3 4/2, S4 0/2 — 15 questions where the mechanism licenses 9. This is not accidental: the Prompt
   Clinic replaced the removed lab, so it is *practice*, and practice needs more than one question per idea.
   **Proposed amendment to `beginner-lecture-archetype`** (its owner's note, so proposed and not edited here):
   license a **practice quiz** in a section, which may re-test that section's taught ideas in *new* scenarios —
   the same licence the cumulative quiz already has, on the same reasoning ("re-testing a taught idea in a new
   scenario is not a new idea"). If the amendment is rejected, the fix is to cut the Prompt Clinic to three
   questions, which loses most of what the live-site feedback asked for.
2. **The Agentic lecture teaches two ideas.** Idea one: an agent is the same model in a loop with tools. Idea
   two: an agent needs scoped access and human confirmation — met for the first time in that lecture's
   misconception paragraph, and given its own quiz question, which by the note's own clause proves it is a
   second idea. Options: split it into two short lectures (+1 lesson), or demote the access point to
   scaffolding and drop its question. Recommend the split; it is the more useful of the two ideas to a
   salesperson.
3. **No L3 domain note exists for any AI concept**, so no distractor in this course can carry the provenance
   `scenario-mcqs-over-recall-mcqs` requires ("the one the matching Domain note names"). This is not fixable at
   the course level and is already governed by a decision: the L3 cap stays 12–15 and is not raised for a second
   course, with per-course L3 budgets deferred to a v2 review. Recording it so the gap is not read as an
   oversight.
4. **Six analogies are not in the register** (`our-analogies-chosen-and-rejected`: "recorded once, not
   reinvented per lesson"). Proposed for the register, with boundaries: **prediction vs lookup = a well-read
   colleague answering from memory, no phone and no notes** (carries the boundary: fluent, usually right,
   occasionally mistaken without noticing); **prompting = briefing a capable colleague who missed the meeting**;
   **iterating = judging a colleague by their first rough draft**; **an agent = a new junior colleague with
   logins** (deliberately the same colleague image, extended, since an agent *is* the same model given tools);
   **MCP = a standard socket, like USB**; **model tiers = a three-step ladder**. One overlap needs the owner's
   call: the register already holds **API = a vending machine's button panel**, and MCP-as-socket is arguably
   the same concept in a different picture. My reading is that they differ — the panel carries "a fixed set of
   allowed requests", the socket carries "one shape of plug, many devices" — but it is exactly the case the
   note exists to catch, so it should be decided rather than assumed.
5. **The proposal named a persona the vault has never described** ("the career-switcher and student from our
   persona set"). `brain/audience/` holds only `salesperson-persona` and `general-beginner-persona`. Until a
   note exists, this course is written against `salesperson-persona`, which is what its voice and examples
   actually assume.
6. **Two-sentence explanations** where this proposal said "a one-sentence post-submit explanation". The longer
   ones are where a wrong answer needs its misconception named *and* the correct behaviour stated. Either the
   proposal's wording relaxes to "one or two sentences", or those options get trimmed; recommend relaxing the
   wording, since the second sentence is doing teaching work.
