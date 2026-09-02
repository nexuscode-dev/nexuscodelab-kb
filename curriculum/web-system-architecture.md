---
id: web-system-architecture
slug: web-system-architecture
status: draft
decided: 2026-08-19
spine_persona: salesperson
language: en
length_weeks: 4
verified_against: 3d34a4e
---

# Course charter — How a Web System Works

**Working title:** *How a Web System Works: From Click to Database and Back*

This is not a note and is exempt from the 150–400 word cap. It is the **scope decision** — neither knowledge
(`brain/`) nor output (`courses/`). L3 is scoped by this file and by nothing else (KB_DESIGN_PROPOSAL §3.3, §5).

## Why this course, and not the other two

Decided 2026-08-19, closing open question #4. The handover recommended this course **because it "can use SQL labs
for a genuinely hands-on module" — that reason is rejected**: SQL cannot execute at all, since the learner runner
is hardcoded to Node.js and no SQL id exists in the language map (§11.4). The course still wins, on three better
grounds:

- **Decay.** A *Claude 101* course is almost entirely `volatile` — model names, prices, feature lists — which §5.1
  requires be isolated in volatile notes. This one is nearly all `durable`; HTTP's shape has not moved in a decade.
- **Reusability.** Its notes are the substrate for courses 2 and 3. A tool course's notes are throwaway the moment
  the tool ships a release.
- **Persona fit.** The salesperson is the audience the team named most specifically, and this is the only one of the
  three candidates that is genuinely *for* them rather than adapted to them.

It also avoids the CSS-lab fork entirely (open decision #7), which the *Web Design & Development* course would have
walked straight into — labs execute on managed RapidAPI Judge0 with no browser and no custom images, so a visual
lab can never be auto-graded (§11.4).

## The title is load-bearing

A course record carries a `level` field — `beginner` / `intermediate` / `advanced`, and Course 1 is `beginner` —
alongside title, description, thumbnail, curriculum id, and order, but **no audience or tags** (§11.6). `level` is a
coarse catalogue bucket: `beginner` says nothing about *who* the beginner is, so it cannot express this course's
specific target learner — a non-technical salesperson who is not expected to write code. Persona targeting therefore
still lives in the title and description strings, which is why the L5 titling note matters more than it looks.
Description has a 10-character minimum.

## Spine persona

**The salesperson with no technical background**, who needs to understand web development and system architecture
at an overview level.

The student and career-switcher personas are served by **three optional labs**, not by a second track. This is safe
because sequence is presentational only — no prerequisites, no gating, no locking (§11.1) — so a skippable lesson
costs a skipping learner nothing.

## Shape

**4 weeks · ~2–3 h/week · 4 sections · 20 lessons — 13 Lecture · 4 Quiz · 3 Lab (all optional).**

All four section titles clear the admin UI's **10-character floor** (§11.6 — UI-only; the API allows 1–255),
which forbids "Intro" and "Setup" for anyone editing by hand.

### S1 · The Two Machines — the client/server split and the trust boundary

| # | Type | Lesson |
|---|---|---|
| 1 | Lecture | What is actually on your screen — the browser is a program on *your* machine |
| 2 | Lecture | The other machine: what a server is (bank teller, **not** waiter) |
| 3 | Lecture | Why the browser cannot reach the database |
| 4 | Quiz | scenario MCQs on the trust boundary |
| 5 | Lab *(opt, javascript)* | given a submitted payload containing `role`, return whether the server should trust it |

**Lesson 3 weighting.** One lesson, not two. The two-hop model (browser → server → database) is *setup*; the **trust boundary** is the main takeaway. Do not generate it as two equally weighted ideas or split it into a second lesson.

### S2 · The Round Trip — why a page is slow, and whose fault an error is

| # | Type | Lesson |
|---|---|---|
| 6 | Lecture | One click, one round trip |
| 7 | Lecture | Why the page is slow — latency vs bandwidth |
| 8 | Lecture | Status codes as shared vocabulary: whose fault is it? |
| 9 | Quiz | "the page shows yesterday's price after you clicked refresh" |
| 10 | Lab *(opt, javascript)* | given a status code, return which side is at fault |

### S3 · Where the Data Lives — state, sessions, and the cost of change

| # | Type | Lesson |
|---|---|---|
| 11 | Lecture | What a database actually is, and what it isn't |
| 12 | Lecture | Statelessness, and why you stay logged in |
| 13 | Lecture | **"Can you just add a field?"** — why a schema change is not a text edit |
| 14 | Quiz | scenario MCQs |
| 15 | Lab *(opt, javascript)* | given a list of records, return the one matching a key — models a query without SQL |

### S4 · The Pieces Around It — APIs, third parties, and AI

| # | Type | Lesson |
|---|---|---|
| 16 | Lecture | What an API is, in the only sense that matters |
| 17 | Lecture | Build vs rent — third-party services |
| 18 | Lecture | Handling more users: more copies, not a bigger machine |
| 19 | Lecture | What AI changes in a web system, and what it does not |
| 20 | Quiz | cumulative scenario quiz |

**Lesson 13 is the course's centre of gravity.** It is the one lesson a salesperson will use the week after
finishing, and the one least derivable from the model's own knowledge — which makes it the honest choice for the
day-3 T2 run (HANDOVER §7 step 4).

**Lesson 18 weighting.** One lesson, not two. **Scaling** (more copies, not a bigger machine) is the main idea.
Deployment is *orientation only* — one line, so the reader recognizes the word. Resilience (one copy can fail while
the others carry on) is an *orientation detail supporting scaling* — a subordinate consequence of running more copies,
not a co-equal second idea, and it gets **no separate analogy** (checkout lanes stays the only one). No implementation
detail.

## Why the labs are JavaScript and not SQL

**The learner runner executes every submission as Node.js** — `language_id: 63` is hardcoded in the learner path
(§11.4), and no SQL id exists in the language map at all. A SQL lab would pass the author's preview (which does
map languages) and then silently mis-grade for every learner. JavaScript is not a preference here; it is the only
language that grades correctly until the platform bug is fixed.

All three labs are one-buffer JavaScript whose stdout is compared byte-exactly (≤255 chars) — "complete the
template so it prints X", with the scaffold in `template_code`. They stay optional: the 10-execution daily limit
(§11.4) means each must be passable in a few tries, and none is on the course's critical path.

## Candidate L3 notes — 13 within a cap of 12–15 (Course 1 = the v1 boundary)

Filenames are the primary index, so these are descriptive kebab-case (CLAUDE.md).

```
 1  the-browser-is-a-program-on-the-users-machine.md
 2  why-the-browser-cannot-reach-the-database.md          # worked in §4.3 — needs a real T4 pass first
 3  frontend-vs-backend-is-a-trust-line-not-a-job-title.md    # answers retrieval Q5
 4  one-click-is-one-round-trip.md                        # ⚠ model knows the fact
 5  latency-is-distance-not-bandwidth.md
 6  status-codes-tell-you-whose-fault-it-is.md            # ⚠ model knows the fact
 7  what-a-database-is-and-why-it-is-not-a-spreadsheet.md # ⚠ model knows the fact
 8  http-is-stateless-so-something-must-carry-identity.md
 9  a-schema-change-is-not-a-text-edit.md                 # highest-value note in the set
10  scaling-means-more-copies-not-a-bigger-computer.md
11  an-api-is-a-contract-between-two-teams.md             # ⚠ model knows the fact
12  build-versus-rent-third-party-services.md
13  what-ai-changes-in-a-web-system-and-what-it-does-not.md
```

**Thirteen candidates, within the cap (12–15) — each backs a specific Course 1 lecture; the list is not padded to
the cap.** The cap is **not** raised for later courses: Course 1 is the v1 boundary, and domain knowledge that only
Courses 2/3 need waits for a per-course v2 L3 budget (KB_DESIGN_PROPOSAL §7.1). Four candidates were cut across the
cleanup, each moved to `_backlog/domain.md` rather than deleted:

- *what-a-server-is-bank-teller-not-waiter* — the analogy is governed by `pedagogy/our-analogies-chosen-and-rejected`;
  its rejected waiter image should not become a Domain note, and learner-facing Course 1 no longer teaches the rejection.
- *the-request-carries-everything-the-server-knows* — it backed HTTP headers / request-body internals, now out of scope.
- *validation-happens-twice-and-only-one-counts* — for Course 1 it duplicates the written `frontend-vs-backend-is-a-
  trust-line` note (which already carries the OWASP-sourced "the server must validate" claim); its full client/server
  validation treatment is Course 2 (Web Design) forms material, deferred to v2.
- *stale-data-means-something-was-cached* — Course 1 teaches no caching lecture (S2 is round trip → latency → status
  codes); the quiz-9 scenario is answered from the round-trip idea and lesson 6 carries a one-sentence orientation only.
  Full caching/staleness is Course 2 performance material, deferred to v2.

**The ⚠ notes earn their place only as misconception + teaching angle, never as definition** (§5). A note explaining
what HTTP *is* competes with the model's own knowledge and loses. **If a draft of one of these reads as a
definition, cut it.** The sharper test: if retrieval question 8 ("what is our source for the claim that X?") has no
interesting answer, the note should not exist.

Note 5 (latency) is the borderline case worth keeping anyway, because "just add more bandwidth" is the densest
misconception a salesperson carries into a delivery conversation.

## Out of scope, and why

**This section answers retrieval question 10** — *"What did we deliberately decide not to teach in course 1?"* —
which is one of the ten fixed T1 questions and is unanswerable without a written scope boundary.

| Not taught | Why |
|---|---|
| HTML / CSS / JavaScript syntax | This is an architecture course. The salesperson will never write any |
| Any framework by name (React, Rails, Django…) | Vocabulary churn with no explanatory power at this level; pure `volatile` content |
| Any cloud provider, or its pricing | `volatile`, and it dates the course within a quarter |
| SQL syntax | The data module models a query without teaching one. SQL cannot execute — the runner is Node.js-only (§11.4) |
| `git`, environments, "works on my machine" | Developer culture, not a salesperson need. Deferred to `_backlog/domain.md` |
| DNS, TCP, anything below HTTP | One layer below the useful abstraction. Deferred |
| HTTPS beyond "the padlock means the pipe is private" | The trust boundary is the security concept this course teaches. Deferred |
| Security beyond the trust boundary | Whole-course material; teaching it partially is worse than not at all |
| Prompt engineering | Lesson 19 is about what AI changes *architecturally*, not how to use a tool |
| Deployment as a practice | Folded into lesson 18 as one paragraph |
| HTTP headers and request-body internals | One layer below the useful abstraction for this beginner; the envelope-vs-contents analogy is reserved for a future course |

## Open questions this charter depended on — answered 2026-08-24 (§12)

1. **How a stored lab grades a real submission** → one JS buffer, run as Node.js on managed Judge0, stdout
   `===`-compared. Labs below are designed to that shape.
2. **Where lecture diagrams are hosted** → nowhere: ` ```mermaid ` fences render as live diagrams in the learner
   app. Every diagram in this course is authored as mermaid text.
3. **`pass_rate` semantics** → a raw count of correct questions. Each quiz below fixes its question count and
   threshold together (e.g. pass 3 of 4).

Still open: a staging smoke test of the authoring API before the publisher script is trusted (§12).
