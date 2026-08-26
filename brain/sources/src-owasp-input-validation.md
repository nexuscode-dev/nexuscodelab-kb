---
id: src-owasp-input-validation
layer: source
status: reviewed
confidence: high
decay: volatile
last_verified: 2026-08-25
review_by: 2026-11-23
sources: []
teaches: []
depends_on: []
---

**Source.** OWASP Cheat Sheet Series — "Input Validation".
URL: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

**Verbatim quote (the exact supporting sentence):**

> "Input validation must be implemented on the server-side before any data is processed by an application's functions, as any JavaScript-based input validation performed on the client-side can be circumvented by an attacker who disables JavaScript or uses a web proxy."

**Supports the factual claim that:** client-side controls can be circumvented, so validation must happen on the server. Cited by `frontend-vs-backend-is-a-trust-line-not-a-job-title` and `why-the-browser-cannot-reach-the-database` for the trust-boundary claim — the frontend runs where the user can change or bypass anything, so nothing it sends can be believed. The "trust line, not a job title" phrasing is teaching, not sourced.
