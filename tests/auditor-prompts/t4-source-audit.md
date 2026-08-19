# Auditor prompt — T4, source audit

**Version 1 · 2026-08-19.** Versioned because the substitute for a non-author reviewer is an auditor that can be
re-instantiated identically. Changing this file changes the test — record the new hash in `audit-log.md`.

## How to run it — and the one rule that matters most

**Run this from OUTSIDE the repo.** Open a session in a scratch directory with no access to `nexuslab-brain`.

`CLAUDE.md` auto-loads for any session opened in the repo folder and hands over the note contract, the layer model,
and the design's intent — which primes agreement. That is fine for T1 and T2, where the real generation session will
have the same context. **It is fatal for a source audit**, whose entire job is to be unpersuaded.

Give the auditor **only** the extracted claim sentence and the source text. Never the note, never the vault, never
the reasoning behind the claim.

## The prompt

> You are checking whether a source supports a claim. You have no other context and you do not need any.
>
> **CLAIM:** `<the single claim sentence, extracted verbatim from the note>`
>
> **SOURCE:** `<the source text, or the fetched page>`
>
> Does this source state this claim?
>
> **Answer in one of exactly two forms:**
> 1. `YES — "<the exact sentence from the source that states it>"`
> 2. `NO`
>
> Rules:
> - Quote only. Do not paraphrase the source, and do not reconstruct the claim from several separate passages.
> - If the source implies the claim but does not state it, that is **NO**.
> - If the source states something adjacent, stronger, or narrower, that is **NO** — say which in one line.
> - Do not assess whether the claim is *true*. You are not being asked. A true claim with no support in this
>   source is **NO**.

## Why the question is shaped this way

§9: the verifier "is given the source, and asked whether the source supports the claim. It is *not* asked whether
the claim sounds right. **Asking a model to agree with a plausible claim is not a test.**"

Quote-or-NO makes agreement expensive and disagreement cheap — the opposite of the default incentive. And the stored
quote stays checkable by a human later with ctrl-F, which a verdict alone never is.

## The tripwire — do not skip this

**Every batch carries one extra claim the builder has deliberately corrupted.** Flip a number, reverse a direction,
or negate the assertion. Plant it in the middle of the batch, not at the end.

**If the batch passes everything including the corrupted claim, the audit did not run.** Discard the whole batch and
every status stamp it would have granted, and record that in `audit-log.md` — a caught-nothing row is more valuable
than a clean one, because it is the only evidence the audit has any power.

This costs about two minutes per batch and it tests the test, which is the thing nobody else checks. Its necessity
is not hypothetical: §11 of the design carried a "verified" stamp and was wrong in four material ways.
