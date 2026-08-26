---
id: a-schema-change-is-not-a-text-edit
layer: domain
status: draft
confidence: high
decay: durable
last_verified: 2026-08-25
sources: [src-mysql-alter-table]
teaches: []
depends_on: [nexuslab-lesson-primitives]
---

**Claim (sourced).** Adding or changing a field in a relational database changes the table's *structure*, not its contents. It is an `ALTER TABLE` operation — "add or delete columns, create or destroy indexes, change the type of existing columns" (`src-mysql-alter-table`) — a different kind of act from editing the data inside a row.

**Why our learner needs it.** "Can you just add a field?" is a sentence a salesperson says weekly. Understanding why the honest answer is often "that touches the structure" is the difference between scoping a change credibly and promising something that quietly is not small.

**How we teach it (framing, not sourced).** Editing data is writing in a form's existing boxes. A schema change is **renovating the building**: adding a room changes the floor plan every other room was laid out against. The data did not change; the shape that holds it did — and everything built on the old shape has to be checked.

**The misconception to pre-empt.** That a database is a spreadsheet, where a new column is one click. In a spreadsheet, structure and data are the same surface. In a running system, structure is a contract the application code and the existing rows both depend on, which is why a field is rarely "just" added.

**Minimal example.** Adding a "phone number" field is not one edit. Existing rows have no value for it (is it required?), forms and validation must learn it exists, and code that read the old shape must be checked. None of that is typing a value into a cell.

**Assessment hook (single-answer scenario MCQ).** "A client asks to 'just add a field' mid-project. Which of these is the reason it is not a one-line change?" Distractors are the spreadsheet model, the "developers are slow" model, and the "it is only slow because of testing" model.

**Sources.** `src-mysql-alter-table` — adding or changing a column is an `ALTER TABLE`, a change to the table's structure.
