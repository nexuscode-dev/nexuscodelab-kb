---
id: nexuslab-lesson-primitives
layer: platform
status: draft
confidence: high
decay: volatile
last_verified: 2026-09-02
review_by: 2026-11-23
verified_against: 2ee5ffa
sources: []
teaches: []
depends_on: []
---

**What a NexusLab lesson can be.** A lesson is exactly one of three types, chosen by `lessons.category`: Lecture (1), Quiz (2), or Lab (3) — `app/Models/Lesson.php`. There is no fourth type, and no lesson mixes two.

**Lecture.** Body is HTML delivered through the authoring API. Tables, links, and ```` ```mermaid ```` fences render in the learner app. **Do not round-trip a lecture through the admin editor** — it strips tables and mermaid on re-save, so lectures are published by API or seeder only.

**Quiz.** Single-answer multiple choice, and only that. The submission API accepts one `option_id` per question (`SubmitQuizRequest.php:23-24`); grading reads only the first `is_correct` option (`LessonController.php:190`). `true_false` is a dead constant with no grading path. There is **no `explanation` field** anywhere — a learner is told which option was correct, never why. `pass_rate` is a **raw count** of correct questions, not a percentage: grading is `$passedCount >= $quiz->pass_rate` (`LessonController.php:215`), so `70` on a four-question quiz is unpassable. **The answer key is auth-gated:** `is_correct` was once returned to learners in the lesson API — a live answer-key leak — so `OptionResource` now exposes it only to an Admin-authenticated request, while learner (`User`) requests and unauthenticated/non-admin callers fail closed and never receive it (server-side grading still reads the real key from the database at `LessonController.php:190`). Keep this gate — it is load-bearing, not dead code: it lets the admin quiz editor read the key while hiding it from learners, and `QuizAnswerKeyTest` is its regression guard (learner GET hides `is_correct`, admin context still receives it, grading still works), so do not strip it as "unused" on a refactor.

**Lab.** One JavaScript buffer, graded by output. Details and limits: see `what-a-lab-can-actually-grade`.

**Why this note exists.** Every pedagogy and content decision downstream is shaped by these three shapes. An assessment written for a type the platform does not have (multi-select, true/false, per-answer feedback) cannot be authored at all, and a quiz whose `pass_rate` was written as a percentage silently locks every learner out. Notes that rest on any of these facts should `depends_on` this one, so a platform change is a single grep away from every rule it invalidates.

Verified against `nexuscode-devs/myanlearn` @ `2ee5ffa` (`origin/develop`); the backend is authoritative, never the type files or the deprecated admin fork.
