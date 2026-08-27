# Git hooks

**Wire these once per clone:**

```sh
git config core.hooksPath hooks
```

`scripts/check-vault.py` fails if that is not set, so the first time you run the validator by hand
it tells you the hook is not installed. That is deliberate: the check cannot enforce its own
distribution, so it settles for making its own absence loud.

## Why this directory exists rather than `.git/hooks/`

`.git/` is not tracked. A hook written there guards exactly one working copy and silently vanishes
for anyone who clones the repo — which was true of this repo until 2026-08-19, when a clone was
tested and committed a note that violated six rules without complaint.

## What this still does not solve

`--no-verify` bypasses the hook, and nothing server-side runs the validator. Until one CI job runs
`python3 scripts/check-vault.py` on push, every mechanical guard in this repo is opt-in per machine.
Do not describe the contract as "enforced" until that job exists — describe it as "checked locally
by anyone who wired the hook."
