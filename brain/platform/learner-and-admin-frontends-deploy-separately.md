---
id: learner-and-admin-frontends-deploy-separately
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

**What this note fixes.** A green backend deploy does not mean the app users see is current. The backend, the learner frontend, and the admin frontend ship on three separate tracks, and each must be verified on its own.

**Learner frontend.** Built by Laravel Vite into `public/build` (`vite.config.js`, input `resources/ts/index.tsx`). `public/build` is **gitignored**, so a `git` fast-forward on the server updates source only — the served bundle stays whatever was last built. Updating the learner UI needs an **explicit production build** on the Laravel host (design system first, then the client). Confirmed 2026-09-08: after the Course 1 backend deploy, the live site kept serving the prior day's bundle until a manual rebuild, so quiz explanations were live in the API but invisible in the UI.

**Admin frontend.** A **separate Vercel deployment** (`apps/admin`, `apps/admin/vercel.json`), with its own branch and lifecycle. Backend HEAD says nothing about whether the admin bundle is current; a change on `develop` is not live in admin until Vercel builds the branch it tracks.

**Operational rule.** After any deploy, verify the **backend, the learner frontend, and the admin frontend separately** — never infer one from another.

**Quiz review is not persisted.** `submitQuiz` stores only lesson completion (`lesson_progress.completed_at`); the picked answers, score, and per-option explanations are returned once in the response and never saved. On reload the quiz re-fetches fresh (unanswered) while the sidebar still shows Completed. Restoring a prior review would need a new attempts table (schema) + a persist-and-fetch endpoint (backend) + hydration on load (frontend); it is intentionally absent today.
