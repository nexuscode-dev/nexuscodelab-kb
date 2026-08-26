---
id: a-schema-change-is-not-a-text-edit
layer: domain
status: draft
confidence: high
decay: durable
last_verified: 2026-08-25
sources: [src-mysql-alter-table]
teaches: []
depends_on: [what-a-table-record-and-column-are, nexuslab-lesson-primitives]
---

**Claim (sourced).** In MySQL, adding or changing a column is an `ALTER TABLE` statement, which changes the *structure* of a table — you can "add or delete columns, create or destroy indexes, change the type of existing columns" (`src-mysql-alter-table`).

**Framing (not sourced).** We generalize this to relational databases in the course, and we contrast it with editing data: a schema change alters the *shape* that holds the rows, not the values in them. The source supports the MySQL `ALTER TABLE` behavior only; the generalization beyond MySQL, the structure-vs-contents contrast, and "not a text edit" are teaching framing.

**The single new idea.** The table's structure is a shared agreement, so changing it means checking everything that relied on it.

**Why our learner needs it.** "Can you just add a field?" is a sentence a salesperson says weekly. Understanding why the honest answer is often "that touches the structure" is the difference between scoping a change credibly and promising something that quietly is not small.

**How we teach it (framing, not sourced).** Editing data is writing in a form's existing boxes. A schema change is **renovating the building**: adding a room changes the floor plan every other room was laid out against. The data did not change; the shape that holds it did — and everything built on the old shape has to be checked.

**The misconception to pre-empt.** That a database is a spreadsheet, where a new column is one click. In a spreadsheet, structure and data are the same surface. In a running system, structure is a contract the application code and the existing rows both depend on, which is why a field is rarely "just" added.

**Minimal example.** Adding a "phone number" field is not one edit. Existing rows have no value for it (is it required?), forms and validation must learn it exists, and code that read the old shape must be checked. None of that is typing a value into a cell.

**Assessment hook (single-answer scenario MCQ).** "A client asks to 'just add a field' mid-project. Which of these is the reason it is not a one-line change?" Distractors are the spreadsheet model, the "developers are slow" model, and the "it is only slow because of testing" model.

**Sources.** `src-mysql-alter-table` — in MySQL, adding or changing a column is an `ALTER TABLE`, which changes the table's structure.
