# Step 0 — Warm-up + dashboard

> **Time budget:** 3 minutes • **Skill:** `/ai-start`

## What you will learn

- What `/ai-start` does and when to run it.
- How the framework's session dashboard looks.
- How to re-orient yourself after a context reset.

## The command

Inside the starter project (`resources/starter/`), open Claude Code and type:

```
/ai-start
```

That is the whole command. No arguments.

## What is happening under the hood

`/ai-start` runs a single deterministic Python script that gathers:

- The current git branch + last 5 commits.
- The active spec (if any) from `.ai-engineering/specs/spec.md`.
- The active plan (if any) from `.ai-engineering/specs/plan.md`.
- Recent board items (cached for speed).
- Active decisions from `state.db`.
- A "next action" pointer.

It then prints a Markdown dashboard. The skill does zero AI synthesis — it is a fast, cheap orientation card.

## Expected output (yours will differ in details)

```markdown
# ai-engineering — session dashboard

**Branch:** main
**Active spec:** none — start with /ai-brainstorm
**Active plan:** none
**Board:** 0 in-progress, 0 in-review

## Recent commits

- chore: bootstrap starter project (HEAD)
- feat: initial myapp scaffold

## Next action

→ /ai-brainstorm "describe what you want to build"
```

## What to watch for

- **"Active spec: none"** means we have a clean slate — exactly where we want to be.
- The **"Next action"** arrow always points at the next chain command. The framework is opinionated about this. Trust it.
- If you see **"ai-start unavailable — run ai-eng install"** instead of the dashboard, you skipped or broke pre-event step 1. Go back and run `ai-eng doctor`.

## When to run `/ai-start` in real life

- At the start of every coding session.
- After `/clear` (when you intentionally drop your conversation context).
- After lunch, after a meeting, any time you have lost track of where you were.

It is cheap, fast, and always safe to re-run.

## Next

→ [Step 1 — Explore the codebase with `/ai-explore`](01-explore.md)
