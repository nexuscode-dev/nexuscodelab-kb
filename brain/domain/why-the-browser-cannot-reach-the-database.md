---
id: why-the-browser-cannot-reach-the-database
layer: domain
status: draft
confidence: high
decay: durable
last_verified: 2026-08-25
sources: [src-mdn-client-server-overview, src-owasp-input-validation]
teaches: []
depends_on: [nexuslab-lesson-primitives]
---

**Claim (sourced).** A browser communicates with a server over HTTP, and the server fetches the data from the database (`src-mdn-client-server-overview`).

**Framing (not sourced).** The title states the consequence we teach: the browser does not reach the database *directly*, so a request makes two hops (browser → server → database). The source establishes the two links only; "cannot reach the database" and "two hops" are our framing of them, not a quoted claim.

**Why our learner needs it.** This is the load-bearing distinction behind "frontend" and "backend". Get it here and half the architecture vocabulary stops being arbitrary.

**How we teach it (framing, not sourced).** Use a **bank teller**, not a waiter: you can ask the teller for your balance, but you cannot walk into the vault. The teller checks who you are, decides what you are allowed, then goes in on your behalf. The vault has no public door on purpose.

**The misconception to pre-empt.** That the browser "has" the data, or could reach the database if it tried. In the model we teach it does not, and that is deliberate: the browser runs on a machine we do not control, so anything it holds, the user holds. Server-side is the first place anything can be trusted — client-side controls can be circumvented by anyone who disables JavaScript or uses a proxy (`src-owasp-input-validation`).

**Minimal example.** View source on any site. The database password is not there. That is not an oversight — there is nowhere in the browser it *could* live safely.

**Assessment hook (single-answer scenario MCQ).** "A login form has a hidden field `role=user`. Which of these can the user change before it reaches the server?" Tests the trust boundary rather than the vocabulary; every distractor is a real misconception, because the platform has no `explanation` field and nothing follows the click (`nexuslab-lesson-primitives`).

**Sources.** `src-mdn-client-server-overview` — browsers talk to servers over HTTP and the server fetches from the database. `src-owasp-input-validation` — client-side controls can be circumvented, so trust begins server-side.
