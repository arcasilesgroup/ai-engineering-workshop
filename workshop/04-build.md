# Step 4 — Build with TDD

> **Time budget:** 10 minutes • **Skill:** `/ai-build` • **Agent:** `ai-build` (only agent with code-write permission)

## What you will learn

- How the approved plan becomes real code.
- Why TDD is enforced (RED → GREEN → REFACTOR), not aspirational.
- How the final quality loop catches blockers before you ship.

## The command

```
/ai-build
```

No argument. The skill reads `.ai-engineering/specs/plan.md` from disk and executes it.

## What is happening

`/ai-build` is the implementation gateway:

1. **Pre-flight.** Verifies `plan.md` exists, every task has a gate, and the execution kernel is wired.
2. **Per-task dispatch.** For each unchecked task:
   - Resolves the right stack adapter (`.ai-engineering/overrides/python/` for us).
   - Picks a model tier — `haiku` if the task has a patch hunk, `sonnet` if synthesis is needed.
   - Dispatches a single `ai-build` agent in a fresh context window with a tightly-scoped payload.
   - The agent runs the task (writes the test, applies the patch, runs the gate).
   - On success, the agent ticks the checkbox in `plan.md` *immediately* — not at the end.
3. **Single final quality loop** on the full changeset:
   - `ai-verify` (evidence-first deterministic + judgment specialists).
   - `ai-review` (parallel specialists: architecture, correctness, security, etc.).
   - One round, fail-loud. Blockers stop and ask you.

## What you will see

Live in your terminal:

```
[T-1.1] RED — writing failing test for --format=json on status command
  → dispatching haiku (patch hunk available: false, synthesis needed)
  → wrote tests/test_cli.py
  → pytest tests/test_cli.py::test_status_format_json
    F tests/test_cli.py::test_status_format_json - argparse: unrecognized argument: --format
  → gate: PASS (test failed for expected reason)
  → checkbox ticked

[T-1.2] GREEN — adding --format flag to status command
  → dispatching haiku (patch hunk available: true)
  → applied 1 hunk to src/myapp/cli.py
  → pytest tests/test_cli.py
    ... 3 passed in 0.18s
  → gate: PASS
  → checkbox ticked

[T-1.3] REFACTOR — extracting _gather_status_data helper
  → dispatching haiku (patch hunk available: false, synthesis needed)
  → modified src/myapp/cli.py
  → pytest tests/test_cli.py
    ... 3 passed in 0.18s
  → gate: PASS
  → checkbox ticked

[QUALITY LOOP] running ai-verify and ai-review in parallel
  → ai-verify: deterministic (PASS), governance (PASS), architecture (PASS), feature (PASS)
  → ai-review: 0 blockers, 2 suggestions
  → appending ## Quality Rounds section to plan.md

BUILD COMPLETE → handing off to /ai-pr
```

## What to watch for

- **Checkboxes tick in real time.** If you peek at `plan.md` mid-run, you will see the file mutate. This is by design — it lets you resume mid-task with `/ai-build --resume` if anything goes wrong.
- **RED really fails first.** Look for `gate: PASS (test failed for expected reason)` on task T-1.1. The framework checks that the test failed in the way the spec predicted. A test that passes prematurely is a bug.
- **Blockers stop the loop.** If `ai-verify` finds a real blocker, `/ai-build` halts — no auto-retry. You either fix the root cause and re-run, or formally accept the risk through the ledger (`ai-eng risk accept --finding-id <id>`).
- **`## Quality Rounds`** section is appended to `plan.md` at the end with the full verifier output for the audit trail.

## On disk after this step

```
.ai-engineering/specs/spec.md           (unchanged)
.ai-engineering/specs/plan.md           (all tasks ticked + Quality Rounds section)
src/myapp/cli.py                        (modified)
tests/test_cli.py                       (modified — new test added)
```

`git status` should now show two modified files and no untracked junk.

## A note on cost and time

For our spec the build typically lands in 3–5 minutes of wall-clock, including model latency. The breakdown is roughly:

- T-1.1 RED: 30 seconds
- T-1.2 GREEN: 45 seconds (patch hunk → haiku → fast)
- T-1.3 REFACTOR: 60 seconds
- Final quality loop: 90 seconds (parallel dispatch)

Padding to 10 minutes in this workshop gives us room for one re-run if something hiccups.

## Next

→ [Step 5 — Open the PR with `/ai-pr`](05-pr.md)
