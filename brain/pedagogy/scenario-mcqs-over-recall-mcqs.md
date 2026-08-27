---
id: scenario-mcqs-over-recall-mcqs
layer: pedagogy
status: draft
confidence: high
decay: durable
last_verified: 2026-08-25
sources: []
teaches: []
depends_on: [nexuslab-lesson-primitives]
---

**Rule.** Every quiz question describes a situation and asks for a judgement. None asks for a definition.

**Why our learner needs it.** A recall question measures whether the salesperson read the page. A scenario question measures whether the model in their head works — which is the only thing worth testing for a reader who will never write code but must reason about systems in a sales conversation.

**Why the platform forces our hand.** Single-answer multiple choice is the only question type NexusLab can author — no true/false, no multi-select, and **no per-answer explanation**, so nothing follows the click (see `nexuslab-lesson-primitives`). That constraint tempts authors toward easy recall questions; this rule pushes back.

**Form.** Symptom → "which layer is at fault?" · artefact → "what happens next?" · change → "what breaks?"

**Anti-examples.** "What does API stand for?" · "Which of these best defines statelessness?" — both pass a learner who understood nothing.

**Rewrites.** "The page shows yesterday's price after you clicked refresh — which is the likeliest cause?" · "You log in, then open a second tab and you're logged in there too — what must be travelling with the second tab's requests?"

**The distractor rule — load-bearing, not stylistic.** Because there is no `explanation` field, a wrong answer is the *only* teaching a mistake ever receives. Every distractor must therefore be a real misconception — the one the matching Domain note names in its "misconception to pre-empt" section — and self-diagnosing: a learner who picks it should be able to see which belief led them there. A wrong answer nobody would pick teaches nothing and makes the question easier than it looks.

**The misconception this pre-empts (in us).** That a quiz certifies coverage. A quiz certifies a working model or it certifies nothing; recall questions quietly do the second while looking like the first.
