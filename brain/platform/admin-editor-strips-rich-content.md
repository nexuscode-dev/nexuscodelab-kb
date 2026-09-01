---
id: admin-editor-strips-rich-content
layer: platform
status: draft
confidence: high
decay: volatile
last_verified: 2026-09-02
review_by: 2026-12-01
verified_against: 5d5c879
sources: []
teaches: []
depends_on: [nexuslab-lesson-primitives]
---

**The rule.** A lecture that contains a `<table>` or a ```mermaid``` code fence must never be re-saved through
the admin lecture editor — not even to fix a typo. One "Update Lecture" click with zero edits permanently
deletes both.

**Why.** The admin editor is TipTap registered with only StarterKit + Heading + Image + Youtube
(`apps/admin/src/pages/ManageLecturePage.tsx`); `@tiptap/extension-table` is not installed. On load the editor
parses the stored HTML and silently drops every node it has no extension for; on submit it writes back
`editor.getHTML()` — i.e. only what survived parsing. Tables and mermaid `<pre><code class="language-mermaid">`
blocks do not survive.

**What this means in practice.**

- Seeder-shipped lectures (course 2's appendix and its diagram lectures, and any future rich lecture) are
  edited **in the seeder file and re-seeded**, never in the admin panel.
- The admin app now shows a destructive warning banner when a loaded lecture's fetched content contains
  `<table` or `language-mermaid` (guard added 2026-09-02, platform `develop`). The banner warns; it does not
  block — the rule above is still the protection.
- A lecture authored *in* the admin editor is safe to keep editing there; the trap is only content the editor
  could never have produced.

**Misconception to pre-empt.** "The editor shows the content, so it can round-trip it." The editor shows what
it could parse. What it dropped is invisible precisely because it was dropped — the preview looking fine is not
evidence the save is safe.

**Fix horizon.** Installing and registering `@tiptap/extension-table` (and a mermaid-preserving code-block
node) would retire this note; until a platform change lands, treat this as a standing constraint
(`decay: volatile`, re-verify against the editor's extension list).
