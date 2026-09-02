---
id: what-a-table-record-and-column-are
layer: domain
status: verified
confidence: high
decay: durable
last_verified: 2026-09-02
sources: [src-postgresql-table-concepts]
teaches: []
depends_on: [nexuslab-lesson-primitives]
---

**Claim (sourced).** A table is a named collection of rows. Every row of a table has the same set of named columns, and each column holds one specific type of value (`src-postgresql-table-concepts`).

**Framing (not sourced).** In everyday speech a row is often called a *record* and a column a *field* — the same things, plainer words. The source uses "row" and "column"; the synonyms and the picture below are teaching.

**Why our learner needs it.** This is the prerequisite for "a schema change is not a text edit." You cannot understand why adding a *field* is structural until you can see that a column is not one value — it is a named slot that every row must have.

**How we teach it.** Picture a customer list. The whole list is the **table**. One customer's line across the page is a **row/record**. "Email address", running down the page as a labelled slot every customer shares, is a **column/field**. The row is a *who*; the column is a *what-about-them*.

**The misconception to pre-empt.** That a "field" is a single box of text — the value in one cell. It is not: a column is the whole labelled slot across every row, which is exactly why adding one is not a one-cell edit. Beginners also assume rows can have different columns; in a table they cannot — the columns are fixed for every row.

**Minimal example.** Add a customer and you add one row, using the columns that already exist. Add "phone number" and you have changed the *set of columns* itself — now every row has that slot. (What that change then forces you to check is a later lesson's idea, not this one.)

**Assessment hook (paired Quiz, single-answer scenario MCQ).** "A spreadsheet-minded colleague says 'a field is just the value in a cell.' Which correction is right?" Distractors are the cell-value model, the row-is-a-field model, and the rows-can-differ model — each a real belief a beginner holds.

**Sources.** `src-postgresql-table-concepts` — a table is a collection of rows; each row shares the same named columns; each column has a data type.
