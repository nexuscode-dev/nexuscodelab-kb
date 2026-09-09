---
id: beginner-lecture-archetype
layer: pedagogy
status: reviewed
confidence: high
decay: durable
last_verified: 2026-08-25
sources: []
teaches: []
depends_on: [one-new-idea-per-lesson, scenario-mcqs-over-recall-mcqs, nexuslab-lesson-primitives]
---

**Rule.** Every beginner Lecture follows the same fixed shape, so two fresh sessions writing the same lesson produce recognizably similar lessons. Only the content changes.

**Length.** Aim for a three-to-five minute read. One Lecture carries exactly one new idea (`one-new-idea-per-lesson`); if it runs long, it is teaching two.

**Section order (always this order):**

1. **Hook.** Open with the reader's own situation or a question they would actually ask — never a definition, never "In this lesson we will…". One or two sentences. **Hooks and examples use neutral hypotheticals** (for example, "A client asks to add a phone-number field") — never an invented date, frequency, statistic, or claim about how the audience behaves, unless the Brain grounds it. A hypothetical scene is fine; an unsupported real-world fact is not.
2. **Plain explanation.** State the idea in the reader's words *before* any analogy or jargon. If they could not repeat it to a colleague, rewrite it.
3. **Analogy.** Add the one house analogy only after the plain statement, and only if it carries the concept's boundary. Skip it if the plain statement already lands.
4. **Diagram (optional).** Include a ```mermaid``` diagram only when the idea is a *structure or a flow* (client↔server, a request's path). For a single distinction, prose is clearer — a decorative diagram costs attention and earns nothing.
5. **Misconception.** Name the specific wrong belief the reader arrives with (from the matching Domain note's "misconception to pre-empt") and take it apart. This is the highest-value paragraph.
6. **Takeaway.** Close with one sentence the reader could say out loud the next day. It restates the idea, not the lesson.

**The paired assessment.** A Lecture cannot contain a question and does **not** get its own Quiz lesson. Each Lecture instead **contributes at least one single-answer scenario question to its section's Quiz** — testing its one idea, with self-diagnosing distractors from the same misconception (`scenario-mcqs-over-recall-mcqs`). A Quiz **may** carry further questions re-testing already-taught ideas in *new* scenarios, and may introduce **no** new idea — the licence a cumulative Quiz already has, on the same reasoning: re-testing a taught idea in a new scenario is not a new idea. **The guarantee is coverage — every Lecture is tested — not a question ceiling.**

**Reproducibility test.** If a second author, given only the Domain note and this archetype, would place the same sections in the same order, the archetype is doing its job.
