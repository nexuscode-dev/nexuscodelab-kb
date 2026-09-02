---
id: using-claude-today
status: approved-on-hold    # approved by Wai Lin 2026-09-02; publication held — see Decision below
proposed_by: hein
date: 2026-09-01
course_slot: TBD (short companion to claude-ai-fundamentals)
---

# Course proposal — Using Claude Today

## Decision — 2026-09-02 (Wai Lin)

**Approved, with two conditions:**

1. **Publication is held** until *Working With AI: Claude Fundamentals* is live and has real learners — this
   course only makes sense to someone who already has the concepts, and every month unpublished is a month of
   refresh debt not paid. Enforced in code: `UsingClaudeTodaySeeder` is not registered in `DatabaseSeeder` and
   stays that way until the hold lifts.
2. **Hard cap: 4 lessons** (the current 3 lectures + 1 quiz). This is the content type that grows; the cap is
   the defence. Growing it requires a new decision, not an edit.

The deliberately perishable half of the Claude pair. `claude-ai-fundamentals` teaches the durable concepts and
is designed never to need re-shooting; this course shows where the buttons live today, and is designed to be
re-shot wholesale each quarter. Splitting them is what keeps the durable course durable — the 2026-09-01 review
of course 2 sent its embedded product-tour section back for exactly this reason.

## Target learner

Anyone who finished (or is finishing) `claude-ai-fundamentals` — including the salesperson persona, since no
lesson here requires code. Standalone use is possible but the lectures constantly map back to the fundamentals
course's concepts, which is where the durable value lives.

## Rough structure

1 section · 4 lessons — 3 Lecture · 1 Quiz. All three lectures carry a **"Last reviewed"** date stamp:

1. **The Claude App: Chats, Models, Documents** — claude.ai / apps, free tier, model picker as the ladder,
   attaching documents as the "give it the source" habit.
2. **Projects and Memory: Beating the Empty Window** — both features explained honestly as the app re-inserting
   text into the context window, never the model remembering.
3. **Search, Artifacts, and the Wider Claude Family** — web search as the hallucination antidote for fresh
   facts, Artifacts as the draft-and-steer loop made tangible, connectors as MCP in product clothes, Claude
   Code in one paragraph.
4. **Checkpoint: Using Claude** — scenario MCQ. The questions test durable *behaviors* (context re-insertion,
   search-then-verify, tier choice, the agent loop), **not** UI-button facts, so the quiz survives product
   releases even when the lectures need refreshing.

Lectures follow `beginner-lecture-archetype` (Misconception + Takeaway in all three).

## Platform fit

Lecture + one scenario quiz; no labs (labs cannot call a model — see `what-a-lab-can-actually-grade`). Hands-on
use happens through out-links to claude.ai. Ships via seeder (`UsingClaudeTodaySeeder.php`, already drafted on
platform `develop`, gated: **local seeding only until this proposal is approved**).

## Decay contract (the point of this course)

- **Cadence:** every lecture re-walked against the live claude.ai UI **quarterly**; "Last reviewed" set to the
  walk date. Registry row in `tests/audit-log.md` (owner: hein · review_by 2026-12-01).
- **Budget:** the whole refresh is a one-person afternoon — three lectures, no quiz edits expected. If a
  refresh ever needs quiz changes, that question was testing UI facts and should be rewritten to test behavior.
- **Kill switch:** if two consecutive quarterly reviews find the course fully stale and nobody refreshes it,
  unpublish it rather than let it grade wrong answers. The fundamentals course loses nothing when this one is
  offline — that is the split working as designed.

## What we deliberately are not teaching

Pricing numbers (change too fast even for this course) · plan-tier comparisons · UI walkthrough screenshots
(rot fastest of all; prose descriptions only) · anything already taught as a concept in the fundamentals course.

## Open questions / risks

1. **Slot & pricing** — free beside the fundamentals course (acquisition logic says yes)? Leon's call.
2. **Quarterly ownership** — hein is the named owner today; this needs a succession answer if ownership moves.
3. **Vendor coupling** — a Claude-only product course deepens single-vendor coupling; acceptable while the
   fundamentals course stays vendor-neutral, but worth restating at each refresh.
