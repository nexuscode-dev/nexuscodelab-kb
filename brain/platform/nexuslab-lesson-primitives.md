---
id: nexuslab-lesson-primitives
layer: platform
status: draft
confidence: high
decay: volatile
last_verified: 2026-08-25
review_by: 2026-11-23
verified_against: 3d34a4e
sources: []
teaches: []
depends_on: []
---

**What a NexusLab lesson can be.** A lesson is exactly one of three types, chosen by `lessons.category`: Lecture (1), Quiz (2), or Lab (3) — `app/Models/Lesson.php`. There is no fourth type, and no lesson mixes two.

**Lecture.** Body is HTML delivered through the authoring API. Tables, links, and ```` ```mermaid ```` fences render in the learner app. **Do not round-trip a lecture through the admin editor** — it strips tables and mermaid on re-save, so lectures are published by API or seeder only.

**Quiz.** Single-answer multiple choice, and only that. The submission API accepts one `option_id` per question (`SubmitQuizRequest.php:23-24`); grading reads only the first `is_correct` option (`LessonController.php:190`). `true_false` is a dead constant with no grading path. There is **no `explanation` field** anywhere — a learner is told which option was correct, never why. `pass_rate` is a **raw count** of correct questions, not a percentage: grading is `$passedCount >= $quiz->pass_rate` (`LessonController.php:215`), so `70` on a four-question quiz is unpassable.

**Lab.** One JavaScript buffer, graded by output. Details and limits: see `what-a-lab-can-actually-grade`.

**Why this note exists.** Every pedagogy and content decision downstream is shaped by these three shapes. An assessment written for a type the platform does not have (multi-select, true/false, per-answer feedback) cannot be authored at all, and a quiz whose `pass_rate` was written as a percentage silently locks every learner out. Notes that rest on any of these facts should `depends_on` this one, so a platform change is a single grep away from every rule it invalidates.

Verified against `nexuscode-devs/myanlearn` @ `3d34a4e` (`origin/develop`); the backend is authoritative, never the type files or the deprecated admin fork.
