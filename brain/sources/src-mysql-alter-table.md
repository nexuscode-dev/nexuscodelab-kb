---
id: src-mysql-alter-table
layer: source
status: reviewed
confidence: high
decay: volatile
last_verified: 2026-08-25
review_by: 2026-11-23
sources: []
teaches: []
depends_on: []
---

**Source.** MySQL Reference Manual — "ALTER TABLE Statement".
URL: https://dev.mysql.com/doc/refman/8.0/en/alter-table.html

**Verbatim quote (the exact supporting sentence):**

> "ALTER TABLE changes the structure of a table. For example, you can add or delete columns, create or destroy indexes, change the type of existing columns, or rename columns or the table itself."

**Supports the factual claim that:** adding or changing a field in a relational database is a change to the table's *structure* (an ALTER TABLE / DDL operation), not an edit to the data it holds. Cited by `a-schema-change-is-not-a-text-edit` for that structural distinction only. The "not a text edit" framing and the cost/effort argument are teaching, not sourced from this page.
