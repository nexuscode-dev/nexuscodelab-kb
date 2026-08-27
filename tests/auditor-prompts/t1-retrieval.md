# Auditor prompt — T1, retrieval

**Version 1 · 2026-08-19.** Record this file's hash with each run in `audit-log.md`.

## How to run it

A **fresh session** opened in the repo — `CLAUDE.md` auto-loading is correct here, because the real course-generating
session will have it too. Ask the ten questions from `retrieval-questions.md` **one at a time**, in separate turns,
with no hints and no follow-up nudges.

Score against the **Registered path** column, not against whether the answer sounded right.

## The prompt

> Answer using only files in this repository. For each answer, state **the path of the file you got it from**.
>
> If the repository does not contain the answer, say `NOT IN VAULT`. Do not fill the gap from your own knowledge —
> a confident answer with no file behind it is the failure this test exists to find.
>
> **Question:** `<one of the ten, verbatim>`

## Scoring

- **Pass a question** when the cited path matches the registered path and the session used **≤3 retrieval steps**.
- **A retrieval step is one distinct search.** A chained shell command counts once per distinct search, not once per
  command — otherwise a session can batch its way to a passing score.
- **Pass T1 at 9/10.**

Two ways a question fails that are easy to miss and both matter more than the score:

- The session answered **correctly from its own knowledge** without opening the registered note. That is a fail. It
  is also the single most likely way this test flatters an empty vault.
- The session found **a** relevant note but not the registered one. Record which note it landed on instead —
  that usually means two notes overlap and retrieval is splitting between them, which is a merge candidate.
