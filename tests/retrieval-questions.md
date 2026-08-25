# T1 — The ten retrieval questions

**These are fixed. Do not edit the questions, and do not tune the vault to them.** They are copied verbatim from
KB_DESIGN_PROPOSAL §2.1. Fitting the vault to them turns the only real test into theatre (CLAUDE.md).

## How T1 is run and scored

**Pass condition: a fresh session cites the registered path in ≤3 retrieval steps, 9 out of 10.**

Two things about that sentence are deliberate, and both were sharpened on 2026-08-19 after the original wording
turned out to be gameable:

- **It scores the *cited path*, not the answer.** A fresh Claude session can answer most of these plausibly from its
  own knowledge without opening a single file — which would score 9/10 against an empty repo. What T1 measures is
  whether the *right note was found*, so the registered path below is the answer key.
- **A "retrieval step" is one distinct search, not one tool call.** A single shell command can chain five greps, so
  counting tool calls lets a session batch its way to a passing score. Count distinct searches.

Run it in a **fresh session** — no memory of authoring the notes. Record the result, the date, and the hash of
`auditor-prompts/t1-retrieval.md` in `audit-log.md`.

## The questions, and the path each must land on

The **Registered path** column is filled in as notes are written, and is itself a useful check: **a question with no
path is a question the vault cannot answer.** Writing these ten paths is the fastest sanity test on the per-layer
caps — if a layer's cap cannot accommodate the note a question demands, the cap or the question set is wrong, and
that is a v1-review conversation rather than a mid-build cap raise.

| # | Question | Layer | Registered path |
|---|---|---|---|
| 1 | What analogy do we use to explain what a server is? | L3 | `brain/domain/what-a-server-is-bank-teller-not-waiter.md` |
| 2 | What does our salesperson persona already know, and what will they never need? | L2 | *(unwritten)* |
| 3 | How long is a lesson, and how many new ideas may one lesson introduce? | L1 | *(unwritten)* |
| 4 | What can a NexusLab lab actually grade? | L4 | *(unwritten)* |
| 5 | What's the common misconception about frontend vs backend, and how do we pre-empt it? | L3 | `brain/domain/frontend-vs-backend-is-a-trust-line-not-a-job-title.md` |
| 6 | How do we write a quiz question that tests understanding rather than recall? | L1 | *(unwritten)* |
| 7 | Where do we stand on introducing AI tooling before or after the manual mental model? | L1 | *(unwritten)* |
| 8 | What is our source for the claim that X? *(pick any domain note)* | L6 | `brain/sources/` + the note's `sources:` field |
| 9 | Which notes are volatile and due for re-verification? | — | `grep -rl "decay: volatile" brain/` then compare `review_by` |
| 10 | What did we deliberately decide *not* to teach in course 1? | — | `curriculum/web-system-architecture.md` § "Out of scope, and why" |

## Notes on three of these

- **Q4** must land on the L4 lab note, and that note has to state the limits honestly: a lab is one JavaScript
  buffer run as Node.js on managed Judge0 (`language_id` 63 hardcoded — non-JS labs silently mis-grade), stdout
  compared byte-exactly to ≤255 chars, no stdin/network/multi-file, 10 executions a day, and a CSS or visual lab
  can never be auto-graded. A note that answers Q4 optimistically is worse than no note.
- **Q9** was unanswerable as originally designed — the vault defined `decay` but no re-verification interval, so
  "due" had no meaning. `review_by` (§4.1) fixes it, and the answer is now one grep.
- **Q10** is why `curriculum/` exists. Without a written scope boundary, one of the ten fixed questions is
  structurally unanswerable no matter how good the vault is.
