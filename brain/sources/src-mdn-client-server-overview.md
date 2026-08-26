---
id: src-mdn-client-server-overview
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

**Source.** MDN Web Docs — "Client-server overview" (Learn web development).
URL: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview

**Verbatim quotes (the exact supporting sentences):**

> "Web browsers communicate with web servers using the HyperText Transfer Protocol (HTTP)."

> "When receiving an HTTP GET Request for a product, the server determines the product ID, fetches the data from the database, and then constructs the HTML page for the response by inserting the data into an HTML template."

**Supports the factual claim that:** a browser talks to a server over HTTP, and it is the server — not the browser — that fetches data from the database. Cited by `why-the-browser-cannot-reach-the-database` and `frontend-vs-backend-is-a-trust-line-not-a-job-title` for the two-hop request model only. The "bank teller / vault" framing and the word "cannot" are teaching, not sourced.
