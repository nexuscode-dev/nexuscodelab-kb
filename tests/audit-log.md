# Audit log

Every test result, dated. **An untested claim of reliability is the exact failure this design exists to prevent**
(CLAUDE.md), so a test that did not run gets an `UNMET` row rather than an optimistic one.

Each entry records the **auditor-prompt hash** it ran under, because the substitute for a non-author reviewer is an
auditor that can be re-instantiated identically (KB_DESIGN_PROPOSAL §6.4). Get it with:

```bash
sha256sum tests/auditor-prompts/t4-source-audit.md | cut -c1-12
```

---

## Standing UNMET — 2026-08-19

These are not failures. They are tests that **cannot** run yet, recorded openly so nobody later reads a silence as
a pass. Both clear cheaply; neither can be faked.

| Test | Why unmet | What clears it |
|---|---|---|
| **T5 · Cold reader** | The build is solo and the author cannot be the cold reader. A model asked to explain a note back is *anti-correlated* with what T5 measures — it already knows the domain, so it succeeds on exactly the notes a human finds impenetrable. **A simulated T5 does not weaken the test, it inverts it.** | 20 minutes of any non-author reading 3 notes. T5 needs a *reader*, not a collaborator — borrow one |
| **T2 · verdict half** | The generation half is genuinely fresh, but the judgement half is contaminated: the author reads past gaps their own memory fills. Runs as `T2-partial` against the §2.2 rubric | A second reader scoring the same rubric |
| **§9 · human sign-off on L1/L2** | L1 and L2 are opinions with no source, so they top out at `reviewed` and no AI pass can lift them. This was true by design before the build went solo | A human who has taught signs them |

---

## Runs

*(No test has been run yet. The vault has no notes.)*

Expected first entries, per HANDOVER §7: **T1 and T2 on the deliberately thin vault**, which the timebox says will
fail — that is the point. A thin-vault failure is cheap and names exactly which layer is underfed; the same failure
on day 8 against a full vault is expensive and ambiguous. **The diagnostic is which layer the failure names**, so
record that, not just the score.

### Entry format

```
## T4 · 2026-08-2X · prompt a1b2c3d4e5f6
Scope: all N domain notes. Tripwire: PLANTED / CAUGHT.
| note id | source id | verdict | quoted sentence | notes |
Result: N/N supported. Tripwire caught. -> stamps granted.
```

**If a T4 batch passes its planted tripwire, the audit did not run.** Discard the whole batch and every stamp it
would have granted, and say so here. That row is more valuable than a clean one.

---

## Empty backlogs — why nothing was deferred

§13 item 4 requires each layer's backlog file to exist, and where one is **empty**, a one-line statement here of why
nothing was deferred. (The original rule required every backlog to be non-empty, which rewards inventing filler to
pass; the intended signal was that someone consciously asserted it.)

| Layer | Date | Why nothing is deferred |
|---|---|---|
| *(pending — no notes written yet)* | | |
