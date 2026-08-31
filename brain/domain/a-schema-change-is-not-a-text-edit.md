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

**Claim (sourced, conceptual).** A structural (schema) change alters the table's *definition* itself — which columns exist, and the structural elements attached to the table (such as its indexes) — as opposed to changing a value stored in one row. It is grounded in MySQL's documented structure-changing behaviour (`src-mysql-alter-table`); the exact statement form is a source-register detail, not learner material.

**Framing (not sourced).** We generalize this to relational databases and contrast it with editing data: a schema change alters the *shape* that holds the rows, not the values in them. The generalization beyond MySQL, the structure-vs-contents contrast, and "not a text edit" are teaching framing.

**The single new idea.** The table's structure is a shared agreement, so changing it means checking everything that relied on it.

**Why our learner needs it.** "Can you just add a field?" is a request a salesperson fields from clients. Understanding why the honest answer is often "that touches the structure" is the difference between scoping a change credibly and promising something that quietly is not small.

**How we teach it (framing, not sourced).** A schema change is **renovating the building**: adding a room changes the floor plan every other room was laid out against. The data did not change; the shape that holds it did — and everything built on the old shape has to be checked. Use this one analogy only (`our-analogies-chosen-and-rejected`); do not add a competing "form's boxes" image.

**The misconception to pre-empt.** That a database is a spreadsheet, where a new column is one click. In a spreadsheet, structure and data are the same surface. In a running system, structure is a contract the application code and the existing rows both depend on, which is why a field is rarely "just" added.

**Minimal example.** Adding a "phone number" field is not one edit. Existing rows have no value for it (is it required?), forms and validation must learn it exists, and code that read the old shape must be checked. None of that is typing a value into a cell.

**Assessment hook (single-answer scenario MCQ).** "A client asks to 'just add a field' mid-project. Which of these is the reason it is not a one-line change?" Distractors: the spreadsheet-one-click model, the "developers are slow" model, and the "only the new column changes" model.

**Sources.** `src-mysql-alter-table` — in MySQL, adding or changing a column is an `ALTER TABLE`, which changes the table's structure.
