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

**Supports the factual claim that:** in MySQL, `ALTER TABLE` changes the structure of a table — it can add or delete columns, create or destroy indexes, change the type of existing columns, or rename columns or the table. Cited by `a-schema-change-is-not-a-text-edit` for that MySQL behavior only. The page does not generalize beyond MySQL and does not contrast structure with the data a table holds — the generalization to relational databases, the structure-vs-contents contrast, and "not a text edit" are teaching framing, not sourced here.
