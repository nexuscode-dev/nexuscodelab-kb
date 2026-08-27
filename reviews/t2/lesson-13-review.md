# Lesson 13 — Independent Review Artifact

## Metadata

- Branch: week1-thin-brain
- Brain commit: 307d89ec12298d5454e77129be8891194d324e76
- Purpose: independent T2 second-reader review
- Status: pending independent review
- Review-only artifact, not published course content

Note: the T3 contradiction re-sweep is pending at the time this artifact was prepared.

## Lecture

A client asks to add a phone-number field to the customer record. It sounds like a small change.

### Plain explanation

Take as given what a column already is: not the value in one cell, but a named slot that every row in the table has.

So adding a phone-number field does not write anything into a record. It changes which slots exist — and the set of slots is a shared agreement. Two things were built while that agreement held: every record already stored, which was stored without the new slot, and every piece of code that reads those records, which was written for the old set. The values in the records did not change. The shape that holds them did.

Adding or changing a column is an `ALTER TABLE` statement, and what it changes is the structure of the table — you can add or delete columns, create or destroy indexes, change the type of existing columns. Writing a value into a record that already exists is a different act.

That is the idea of this lesson. The structure is a shared agreement, so changing it means checking everything that relied on it.

### Analogy

Editing data is writing in a form's existing boxes. A schema change is renovating the building, not editing a document. Add a room and you change the floor plan every other room was laid out against. The rooms did not move. The plan they were built to is now a different plan, and each of them has to be checked against it.

### Misconception

The belief to put down is that a database is a spreadsheet, where a new column is one click.

In a spreadsheet the structure and the data are the same surface. In a running system they are not: the structure is a contract that the application code and the existing records both depend on.

Which is why adding the phone-number field is not one edit. Records already in the system have no value for it — so is the field required? The forms, and the checks behind them, have to learn that it exists. And code that read the old shape has to be checked. None of that is typing a value into a cell.

### Takeaway

In a client or delivery conversation, the sentence is: no, that change touches the database structure — it is not a text edit.

## Quiz

Under the current assessment rule, a Lecture cannot contain a question and does not get its own Quiz lesson. Each Lecture contributes one single-answer scenario question to its **section's** Quiz lesson. The question below is Lesson 13's contribution; the section Quiz that holds it also holds the contributions of the other Lectures in its section.

### Lesson 13 contributed scenario question for its section Quiz

A client asks to "just add a field" mid-project. Which of these is the reason it is not a one-line change?

A.
The set of columns is something the records already stored and the code already written both depend on, so both have to be checked.
Correct answer: YES

B.
Adding the column is a one-click change; the time goes on scheduling the work rather than on the change itself.
Correct answer: NO

C.
Development teams take longer on small requests than the size of the request warrants.
Correct answer: NO

D.
Only the new column is affected — it has to be added to every record, and nothing else changes.
Correct answer: NO

On the section Quiz lesson that carries this question, pass*rate is a raw count of correct questions, not a percentage.*

## Independent review checklist

Review this exact artifact against the current 10-line rubric, reproduced below from the Brain commit named in the metadata.

| # | The generated lesson… | Accountable | PASS / FAIL | Short reason |
| --- | --- | --- | --- | --- |
| 1 | introduces at most the permitted number of new ideas | L1 |  |  |
| 2 | assumes only what the persona note says the learner knows | L2 |  |  |
| 3 | uses our analogy for each concept, not a generic one | L1 + L3 |  |  |
| 4 | pre-empts the misconception the domain note names | L3 |  |  |
| 5 | sounds like us — no hedging, no "in today's fast-paced world" | L5 |  |  |
| 6 | fits what a lecture body can hold — HTML via the API: tables, links and mermaid are fine; nothing that needs the admin editor to survive a re-save | L4 |  |  |
| 7 | contributes one single-answer scenario question (with self-diagnosing distractors) to its section's Quiz lesson — a Lecture does not get its own Quiz | L1 + L4 |  |  |
| 8 | **every factual claim traces to a note id** | L3 + L6 |  |  |
| 9 | **every domain / platform / audience factual claim is grounded in the vault; neutral hypothetical scene-setting is allowed only when it asserts no real-world statistic, behaviour pattern, technical fact, or learner fact** | — |  |  |
| 10 | needs no rewrite before it could be published to the platform via the API | overall |  |  |

### Reviewer output fields

- Score: ** / 10**
- Unsupported claims found (list, or "none"): 
- READY / NOT READY: 
- Blockers: 

### Also check

- unsupported domain, platform, audience, or learner claims
- prerequisite vs Lesson 13 concept boundary
- the contributed question's distractors against the Domain-note misconceptions
- Lecture structure against the beginner lecture archetype
- whether the lesson can be published without rewriting

### Do not

- use previous T2 scores as evidence
- rewrite the lesson
- change the Brain
