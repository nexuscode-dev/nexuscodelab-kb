---
id: manual-model-before-ai-tooling
layer: pedagogy
status: reviewed
confidence: high
decay: durable
last_verified: 2026-09-01
sources: []
teaches: []
depends_on: [one-new-idea-per-lesson]
---

**Decision.** Learners build the manual mental model of a web system first — browser, server, API, database, requests, responses, and the trust boundary — before any AI tooling is introduced. AI is then taught as one more component inside that model, not as a shortcut that replaces understanding the underlying architecture.

**Why our learner needs it.** The spine persona is a salesperson with no technical background. If AI arrives before the model, it *becomes* the model: the learner reasons about the whole system as "the AI does it", and every later conversation — what a change costs, whose fault an error is, where the data lives — has no structure to hang on. The architecture is the reusable, durable part; AI is one component that plugs into it. Teaching the component before the frame leaves nothing for it to plug into.

**How we apply it.** Course 1 teaches the full manual model across its first three sections and reaches AI only in the final section, where AI is a service the server calls through an API — the same shape as any rented third-party service. AI is introduced as "another box inside the diagram you already have", never as a replacement for learning how the boxes connect.

**What this decision is not.** A teaching-sequence rule only. It says nothing about prompt engineering, model internals, LLM accuracy or safety, or which vendor or tool to use; those are out of scope here.

**Owner decision.** Recorded by Ye Yint Ohn Kyaing (course owner) on 2026-09-01; this closes retrieval question 7. Like all L1 notes it is a source-free teaching opinion and stays at most `reviewed` until a §9 sign-off by a human who has taught.
