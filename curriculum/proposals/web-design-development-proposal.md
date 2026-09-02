# Course Proposal — Web Design & Development

*Grounding: the **Platform Fit** section is read from `myanlearn@origin/develop` via the two L4 notes — the
original read at `3d34a4e`, and the quiz-duration finding at `6e2450f` (round-2 review, 2026-09-02). Everything
under **Course Structure** and **Sample Lesson** was proposed with **no vault knowledge behind
it** — the vault holds zero domain notes and zero sources on design or front-end, and that remains true of the
twenty lessons subsequently built (see **Current Status**). Course order is not assumed here; this is a candidate,
not "course 2".*

## Course Name

Web Design & Development
Working title: *Why the Page Looks Like That: Structure, Rules, and Decisions That Hold Up*

## Target Learner

A career-switcher or student who wants to build and judge web pages — the second and third personas named in the
v1 planning, not the salesperson course 1 was written for.

**This learner has no note.** The only audience note in the vault is `salesperson-persona`. A course written for
someone the vault has never described is a course written from the model's own assumptions, which is the failure
mode T2 exists to catch. One L2 slot has to be spent on it — and the sixteen lectures were generated
without it, so the note is owed retrospectively (Open Question 3).

## Why This Course

- **It consumes course 1 rather than competing with it.** Client/server, the trust line, and the round trip are
  already written; this course spends its lessons on its own subject and points back to them. Course 1's reuse
  argument only pays off if a second course actually draws on it.
- **It is the course people ask for by name.** "Web design" is a thing a learner comes looking for; "system
  architecture" is a thing they discover they needed.
- **Results are visible.** A learner sees a page change, which is motivation course 1 cannot offer.
- **It is mostly durable.** Structure, the cascade, layout, contrast and the box model do not move quarterly.
  Frameworks and tooling do — and those are out of scope below, which is what keeps this course durable.

**The honest counterweight.** This is the one candidate whose central skill — *the learner produces visual output*
— the platform cannot assess at all. See Platform Fit and Open Question 1. That was not a reason to drop the
course; it was the decision that had to be made before building — and the course was built on the answer: no labs.

## Course Goal

The learner can look at a page and explain what it is made of, why it behaves as it does when the screen or the
content changes, and which decisions in it were deliberate. They can make and defend a layout, type, contrast and
responsive decision, and hand work over to a developer without surprises. **Judgement about pages, assessed by
judgement questions — not a portfolio**, because the platform grades no visual artefact.

## Course Structure

4 weeks · about 2–3 hours a week · 4 sections · 20 lessons — 16 Lectures, 4 Quizzes, **no Labs**.

| Section | Covers | Lessons |
|---|---|---|
| S1 · The Page Underneath | HTML as structure, not appearance | 4 lectures, 1 quiz |
| S2 · Rules, Not Pictures | CSS as rules applied to that structure — the cascade and the box | 4 lectures, 1 quiz |
| S3 · Decisions That Hold Up | layout, type, contrast, and the screen you did not design for | 4 lectures, 1 quiz |
| S4 · Design Meets the System | handoff, assets and weight, and what course 1 already explained | 4 lectures, 1 cumulative quiz |

**Why no labs.** A CSS or HTML lab cannot be graded — see Platform Fit. The alternative is up to three optional
JavaScript labs that model design *logic* (which breakpoint applies at a given width; whether a contrast ratio
passes a threshold), which is arithmetic about design, not design. Recommendation: ship without labs, as course 1
did after its own lab withdrawal, and revisit if the grader gains a real language map.

## Sample Lesson

**Built, and still vault-ungrounded.** This section originally proposed no sample: Course 1's Lesson 13 sample
existed only because its domain note existed first, and generating one here would have tested the model's
knowledge of CSS rather than the vault's. The lesson below was written and shipped anyway, as one of the twenty
(see **Current Status**) — so that objection was overtaken rather than answered. It stands as an authored
judgement with no domain note behind it.

The lesson, the structural twin of Lesson 13:

**"Can you just move it a bit?" — why a layout change is not a nudge.** A client asks for one element to move
slightly. The lesson's one idea: a page is a set of rules applied to a structure, not a picture, so a local
change has effects that are not local. It is the highest-value misconception in the course, the one least
derivable from a definition, and the honest choice for a T2 run — for the same reasons Lesson 13 was.

## What We Deliberately Are Not Teaching

| Not taught | Why |
|---|---|
| Any framework or library by name (React, Tailwind, Bootstrap…) | Vocabulary churn with no explanatory power at this level; dates the course within a quarter |
| Build tooling, npm, bundlers | Developer setup, not design or structure. A separate course's subject |
| Design-tool feature tours (which button in which app) | Tool UIs change; the decisions behind them do not |
| Server-side, databases, the trust boundary | Course 1 owns these. This course points at them and does not re-teach them |
| JavaScript behaviour and animation | One lecture's worth of "what moves and who moves it", not a module. Interaction programming is its own course |
| Accessibility as standards conformance | We teach contrast and real structure as design decisions. Auditing against a standard is a professional practice, and partial coverage misleads |
| SEO, analytics, marketing | Not design, not development |
| Hosting, domains, deployment | Folded into one S4 lecture as "where the page ends up", per course 1's precedent |
| Print, brand identity, logo design | Not the web |

## Platform Fit

Every line here is verified against the backend, not assumed.

- **Visual output cannot be graded, at all.** A lab is one JavaScript buffer whose printed text is compared
  byte-exactly; there is no browser, no DOM, no Playwright or Puppeteer, and no custom image on the managed
  Judge0 instance. The central act of this course is unassessable by the platform
  (`what-a-lab-can-actually-grade`).
- **Worse than unassessable — authorable and wrong.** `html` and `css` appear in the admin lab language list,
  while the learner path hardcodes Judge0 `language_id: 63` (Node.js). A CSS lab therefore passes the author's
  preview and silently mis-grades every learner. This is a reported platform bug, not a design choice.
- **Code samples in lectures are a live hazard for this course specifically.** The write path runs
  `html_entity_decode` with no server-side sanitisation, so an escaped tag inside a code sample becomes real
  markup — a sample containing `<h1>` injects a heading into the lesson. A course about HTML and CSS puts tags in
  almost every lecture, so this must be solved and tested before authoring, not during.
- **What lectures *can* carry is unusually good for this subject.** HTML via the authoring API, with images by
  URL or base64, video, tables, links, code blocks, and ` ```mermaid ` fences rendering as live diagrams. No image
  hosting is needed for diagrams. **Never round-trip a lecture through the admin editor** — it destroys tables and
  mermaid fences on re-save, so publishing is API or seeder only (`nexuslab-lesson-primitives`).
- **A lesson is exactly one type** — Lecture, Quiz, or Lab. A lecture cannot contain a question, so each lecture
  contributes one scenario question to its section's quiz.
- **Quizzes are narrow.** Single-answer multiple choice only; no true/false, no multi-select, and **no field to
  explain a wrong answer**, so the wrong options carry all the teaching. **A quiz duration is stored but not
  enforced** — `lesson_quizzes.duration` exists and is populated, but `QuizResource::toArray()` never returns it
  and no backend code checks elapsed time, so learners experience no timer. Every question must be answered or the
  submission is rejected, and **the pass mark is a raw count of correct questions, not a percentage** — 4
  questions pass 3 per section quiz, 8 pass 6 for the cumulative.
- **Which distractor a learner picked is not stored.** No revision loop can depend on item analysis until that
  changes. A platform gap, recorded so nobody plans around data that is not kept.
- **English is required per field, Japanese optional.** No third language slot exists.

## Current Status

*Updated 2026-09-02 to describe what shipped, not what was planned.*

**Done** — the platform read: what a lecture can hold, what a quiz can assess, and the proof that visual labs
cannot work. The code-sample escaping test Open Question 2 called for, run against the running app: a
singly-escaped tag is decoded into live markup and lost, while double-escaping survives the reader's single
decode pass and renders literally — so this course is authorable, and the rule is centralised in one helper.
All **20 lessons — 16 lectures and 4 quizzes, no labs** — are built and merged as
`database/seeders/Course2WebDesignDevelopmentSeeder.php` (PR #53). Round-1 review fixes are in PR #54: a guarded
replace so re-seeding cannot destroy learner progress, a seeded option shuffle, a throwing `curriculumId()`, and
the placeholder thumbnail removed.

**Pending** — PR #54 is open and unmerged. A card image (`THUMBNAIL` is deliberately null until an asset is on the
team bucket, because an unuploaded key renders as a broken image). The **L2 persona note**: Open Question 3 said
no lesson should be generated before it exists, and sixteen lectures now have been. That is the substantive gap.
The L4 note `brain/platform/css-labs-cannot-be-authored.md`, specified by §12 decision 7, is still unwritten.

**Not started** — the charter, and every domain note (**zero exist**) and source record (**zero exist**) for
design or front-end. The twenty shipped lessons are therefore *authored but vault-ungrounded*: the reasoning in
them is deliberate, but its grounding is the model's knowledge of the subject rather than the vault's. Whether
they publish before the v2 notes exist is an open decision that should be taken explicitly, not by drift.

## Open Questions

1. **The assessment fork — resolved in practice, not on the record.** KB_DESIGN_PROPOSAL §12 decision 7 deferred
   the CSS-lab question with a named forcing event: *"the first course charter proposing a lesson whose assessed
   outcome is 'the learner produces visual output'."* This was that proposal. Of the three branches — teach only
   what JavaScript can grade, extend the grader with a real language map, or design the course around having no
   working labs — the course shipped on the third: 16 lectures, 4 quizzes, no labs. The decision was therefore
   taken by building, and **what remains open is recording it.**
   `brain/platform/css-labs-cannot-be-authored.md`, specified by decision 7, still does not exist. Retrieval
   question 4 does land today — on `brain/platform/what-a-lab-can-actually-grade.md`, which states a lab cannot
   grade CSS or visual output — so the missing note is a gap in the §12 record, not in retrieval.
2. **Can code samples containing tags be published safely? — Answered: yes, by double-escaping.** The test ran
   against the running app (see **Current Status**): a singly-escaped tag is decoded into live markup and lost,
   while double-escaping survives the reader's single decode pass and renders literally. S1 and S2 are unblocked,
   and the rule is centralised in one helper rather than left to each author to remember.
3. **Whose course is it? — still open, and now the substantive gap.** A persona note for the career-switcher, or
   an explicit decision that this course is written for the student. Either way it costs one L2 slot. The
   condition attached to it — no lesson generated before it exists — was not met: sixteen lectures were written
   first, so the note now has to be written *and* the lectures checked against it. `INDEX.md` reads
   `L2 Audience · 1 / 6–8`, so the slot is there, and the v2 budget decision below means nothing competes for it.
4. **The note budget does not fit two courses — settled 2026-09-02.** §7 caps L3 at 12–15 notes for v1, four are
   written, and course 1 alone lists 17 candidates against that cap. The resolution is not a raised cap (§7
   forbids that mid-build) but a smaller v1: **v1 closes at Course 1, and courses 2 and 3 get their own per-course
   L3 budgets under a v2 review.** This course's domain notes and its L2 persona note therefore have a home and
   compete with nothing. The sub-question about the backlog files printing different caps is closed too — the
   literals were reconciled on `main` on 2026-08-27, and `check-vault.py`'s `check_cap_literals()` now fails the
   build on any disagreement.
5. **Course order.** Whether this or *Claude 101* follows course 1. This course's argument is that it makes
   course 1's notes pay off; *Claude 101*'s is timeliness, against almost entirely volatile content.
6. **Does a course record carry `level`?** The course-1 charter states courses have no difficulty or level field,
   so persona targeting can live only in the title and description. The later platform verification lists `level`
   (default `beginner`), `duration` and `time_limit` on courses. If the newer read is right, targeting has a real
   field and one charter claim needs correcting.
