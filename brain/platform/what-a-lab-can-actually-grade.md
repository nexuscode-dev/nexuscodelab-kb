---
id: what-a-lab-can-actually-grade
layer: platform
status: draft
confidence: high
decay: volatile
last_verified: 2026-09-08
review_by: 2026-12-08
verified_against: ee49c6d
sources: []
teaches: []
depends_on: [nexuslab-lesson-primitives]
---

**What a lab really is.** A learner submission is one code string, run once and graded by comparing its printed output to an expected string. Nothing else.

**It runs as JavaScript, always.** The learner path hardcodes `language_id: 63` (Node.js) on managed RapidAPI Judge0 (`LessonController.php:292`), regardless of the lab's stored `language`. The admin *preview* maps other languages, so a non-JS lab passes preview and mis-grades every learner. Until fixed, **labs are JavaScript, full stop** — no SQL runtime exists.

**Instructions localize; executable parts don't.** `content` (English) and `content_ja` (Japanese, EN fallback) hold the prose; `function_name`, `template_code`, test inputs and `expected_output` stay literal — translating a byte-matched value breaks grading.

**Grading is byte-exact string match.** The learner's stdout is CRLF-normalized and outer-trimmed, then compared with `===` — case-sensitive, internal whitespace significant. `expected_output` is a short column (VARCHAR, ~255 chars), so the answer must be one short scalar line.

**What a lab cannot do.** No stdin, network, files, or installed packages — none is sent to Judge0, so it cannot fetch a URL, read input, or import a library. It **cannot run a browser, DOM, Playwright, Puppeteer, or grade CSS/visual output** — a managed CE instance hosts no browser and no custom image. Learners can *model* a request in pure JS; never make one.

**Limits.** Free learners get ten executions per day, **charged per test case** — so a five-case lab is two full attempts.

**`function_name` is used, not decorative.** The column is nullable, but the learner runtime *calls* it: the wrapper invokes `function_name` with the test input, so inputs plus a null name build an invalid wrapper that fails every learner. Seeders persist it, but the admin create/update payload omits it, so a fresh admin lab can save null. **Admin edit is worse:** `LabResource` exposes neither `function_name` nor `solution_code` (the latter is admin-only test scaffolding, not a stored column), yet the edit form requires both — opening an existing lab loads them empty and blocks saving unrelated edits (a standing bug, not from localization). Because `LabResource` hides `function_name` from learners, **every lab must state its function name in the instructions and the starter template.**

**Consequence for authoring.** Design every lab as one function, a JSON-shaped input, one short printed line as the answer. Anything needing a browser, package, or multi-line output belongs in a Lecture or Quiz, not a Lab.

Verified against `nexuscode-devs/myanlearn` @ `ee49c6d` (`origin/develop`); reported as a platform bug.
