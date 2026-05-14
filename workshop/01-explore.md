# Step 1 — Explore the codebase

> **Time budget:** 5 minutes • **Skill:** `/ai-explore`

## What you will learn

- How to map an unfamiliar codebase fast.
- The difference between *exploration* (read-only, throwaway research) and *coding* (write actions tracked by specs).
- Why fresh-context subagents matter.

## The command

```
/ai-explore "Map the myapp CLI. What commands does it expose, what files implement them, and where are the tests?"
```

You can ask any question. The skill dispatches a read-only agent in its own fresh context window — so the agent's research does not pollute your main session.

## What is happening

`/ai-explore` dispatches the `ai-explore` agent (one of 9 first-class agents). The agent:

- Has only **Read, Glob, Grep, Bash** tools — it physically cannot write code.
- Runs in its own context window — its 50k tokens of `grep` output never reach your main session.
- Returns a structured summary with file:line citations.

This pattern — **read-only research delegated to a fresh agent** — is one of the most important muscles to develop. It keeps your main session focused on decisions and code, not on raw file dumps.

## Expected output (abridged)

```markdown
# myapp CLI map

## Entry points

- `src/myapp/cli.py:42` — `main()` registers two subcommands via argparse:
  - `hello` (lines 51-58) — prints a greeting
  - `status` (lines 60-72) — prints a 3-line text summary

## Tests

- `tests/test_cli.py:1` — pytest, covers `hello` (one assertion) and `status` (two assertions)

## Risks / observations

- `status` has no `--format` flag; output is plain text only
- No `--verbose` either
- All argparse parsers live in one function — extending will require careful seam selection
```

## What to watch for

- **File:line citations.** Every claim the agent makes should anchor to a real file. If a claim has no anchor, it is a guess. Push back.
- **Risks / observations.** The agent will often surface things you did not ask about — missing tests, hard-coded values, dead code. Treat these as free intel.
- **No code changes happened.** Confirm: `git status` should be clean.

## A note on cost

Exploration is the cheapest possible thing you can do with AI. A `/ai-explore` call typically costs less than the price of a single API tool call in your main session because the subagent is bounded by the size of its task. Use it liberally — every time you ask yourself "where does X live in this codebase?", run `/ai-explore` first instead of opening files yourself.

## Next

→ [Step 2 — Brainstorm the feature with `/ai-brainstorm`](02-brainstorm.md)
