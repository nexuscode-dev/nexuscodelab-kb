---
id: frontend-vs-backend-is-a-trust-line-not-a-job-title
layer: domain
status: draft
confidence: high
decay: durable
last_verified: 2026-08-25
sources: [src-owasp-input-validation, src-mdn-client-server-overview]
teaches: []
depends_on: [why-the-browser-cannot-reach-the-database, nexuslab-lesson-primitives]
---

**Claim (sourced).** Client-side JavaScript validation can be circumvented — by disabling JavaScript or using a web proxy — so input validation must be implemented on the server before any data is processed (`src-owasp-input-validation`). The two sides communicate over HTTP (`src-mdn-client-server-overview`).

**Framing (not sourced).** We read this as a *trust line*, not two job titles: the frontend is the region we cannot trust, and the backend is the first region we can (see "How we teach it"). That the frontend runs on a machine the operator does not control, and that *anything* it sends can be altered, are the reasoning behind the framing — not claims taken from the source above, which speaks only to client-side validation.

**Why our learner needs it.** "Frontend = looks, backend = logic" is the definition every salesperson arrives with, and it collapses the first time they see the same check happening in both places. The trust framing survives that; the job-title framing does not.

**How we teach it (framing, not sourced).** Draw one line, and label it "everything on this side, the user can change." The frontend is not a *role*; it is *the region we cannot trust*. The backend is simply the first region we can. Everything else — where code runs, who wrote it — is downstream of that line.

**The misconception to pre-empt.** That client-side validation is a security feature. It is a convenience: it gives fast feedback, but it can be disabled or bypassed with a proxy, so the server must check again. A learner who believes the browser's check "protects" anything will mis-scope every security conversation they walk into.

**Minimal example.** A price shown as a disabled field in the page can be re-enabled and changed in the browser before it is sent. If the server trusts that number, the checkout is broken. The fix is not a better disabled field; it is the server re-checking the price.

**Assessment hook (single-answer scenario MCQ).** "A form disables the 'total' field in the browser. Where must the total actually be re-checked, and why?" Distractors are the common wrong models (trust the hidden field, trust the disabled field, trust HTTPS to prevent it).

**Sources.** `src-owasp-input-validation` — client-side validation can be circumvented; the server is where trust begins. `src-mdn-client-server-overview` — the client/server split and HTTP as the channel between them.
