# Backlog — L3 Domain

**Cap for this layer: 12–15 notes.** At cap you may **merge two notes** or defer an idea here. You may **not** raise
the cap mid-build (KB_DESIGN_PROPOSAL §7.1) — that is a v1-review decision.

This file is the pressure valve. Without it, ideas get smuggled into existing notes, which is worse than a new
note: it makes notes non-atomic and degrades retrieval for everything already in them.

A deferred idea needs one line and a reason. If it has no reason, it is not deferred — it is forgotten.

| Idea | Why deferred | Raised |
|---|---|---|
| dns-and-what-a-domain-name-resolves-to | One layer below the useful abstraction for this persona. A salesperson needs "the name points at the machine", which is one sentence inside lesson 6, not a note | 2026-08-19 |
| https-and-what-the-padlock-actually-promises | The trust boundary is the security concept course 1 teaches. Adding a second security idea competes with it for the one-new-idea budget | 2026-08-19 |
| environments-and-why-it-works-on-my-machine | Developer culture, not a salesperson need. Becomes load-bearing the moment a career-switcher course exists | 2026-08-19 |
| deploying-is-copying-not-saving | Merge candidate into `scaling-means-more-copies-not-a-bigger-computer` if it is ever needed. Not worth its own slot at a cap of 12–15 | 2026-08-19 |
| queues-and-why-some-work-happens-later | Genuinely useful for the "why is the report not ready yet" conversation, but it needs the round trip established first. First candidate to promote if a domain slot frees up | 2026-08-19 |
| validation-happens-twice-and-only-one-counts | Deferred at the Course 1 v1 boundary. For Course 1 it duplicates the written `frontend-vs-backend-is-a-trust-line` note, which already carries the OWASP-sourced "the server must validate before use" claim. Its own home is the full client/server-validation treatment (client-side as UX convenience vs server-side as trust) in **Course 2** (Web Design / forms). Reconsider under a v2 per-course L3 budget | 2026-09-02 |
| stale-data-means-something-was-cached | Deferred at the Course 1 v1 boundary. Course 1 teaches no caching lecture — S2 is round trip → latency → status codes — so the quiz-9 "yesterday's price" scenario is answered from the round-trip idea and lesson 6 carries only a one-sentence orientation. Full caching/staleness (what is cached, invalidation, CDNs) is **Course 2** performance material. Reconsider under a v2 per-course L3 budget | 2026-09-02 |
