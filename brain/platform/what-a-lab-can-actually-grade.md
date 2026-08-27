---
id: what-a-lab-can-actually-grade
layer: platform
status: draft
confidence: high
decay: volatile
last_verified: 2026-08-25
review_by: 2026-11-23
verified_against: 3d34a4e
sources: []
teaches: []
depends_on: [nexuslab-lesson-primitives]
---

**What a lab really is.** A learner submission is one code string, run once and graded by comparing its printed output to an expected string. Nothing else.

**It runs as JavaScript, always.** The learner path hardcodes `language_id: 63` (Node.js) on the managed RapidAPI Judge0 endpoint (`LessonController.php:292`), regardless of the lab's stored `language`. The admin *preview* maps other languages, so a non-JS lab passes the author's preview and then silently mis-grades for every learner. Until that is fixed, **labs are JavaScript, full stop** — there is no SQL runtime at all.

**Grading is byte-exact string match.** The learner's stdout is CRLF-normalized and outer-trimmed, then compared with `===` — case-sensitive, internal whitespace significant. `expected_output` is a short column (VARCHAR, ~255 chars), so the answer must be one short scalar line.

**What a lab cannot do.** No stdin, no network, no file input, no multiple files, no installed packages — none of those fields is ever sent to Judge0. A lab cannot fetch a URL, read input, or import a library. It **cannot run a browser, a DOM, Playwright, Puppeteer, or grade CSS or visual output** — a managed CE instance hosts no browser and no custom image. Learners can *model* a request in pure JS; they can never make one.

**Limits.** Free learners get ten executions per day, **charged per test case** — so a five-case lab is two full attempts. `function_name` is nullable and the admin UI fails to persist it, so author labs as "complete the template so it prints X", with the scaffold in `template_code`.

**Consequence for authoring.** Design every lab as: one function, a JSON-shaped input, one short printed line as the answer. Anything that needs a browser, a package, or multi-line output belongs in a Lecture or a Quiz, not a Lab.

Verified against `nexuscode-devs/myanlearn` @ `3d34a4e` (`origin/develop`); reported as a platform bug.
