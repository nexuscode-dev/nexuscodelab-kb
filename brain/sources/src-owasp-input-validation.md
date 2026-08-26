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

**Supports the factual claim that:** (1) JavaScript-based client-side validation can be circumvented — by disabling JavaScript or using a web proxy — and (2) input validation must be implemented on the server-side before any data is processed by an application's functions. Cited by `frontend-vs-backend-is-a-trust-line-not-a-job-title` and `why-the-browser-cannot-reach-the-database` for those two points only. Broader statements — that the frontend runs on a machine the operator does not control, or that *nothing* it sends can be trusted — are teaching framing, not taken from this page, which speaks specifically to client-side validation.
