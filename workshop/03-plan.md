# Step 3 — Plan it out

> **Time budget:** 7 minutes • **Skill:** `/ai-plan`

## What you will learn

- How a spec becomes a concrete task list.
- Why every task gets an agent assignment + a principle anchor.
- What a "patch hunk" is and why it lets the next step use a cheaper model.

## The command

```
/ai-plan
```

No argument needed. The skill reads `.ai-engineering/specs/spec.md` from disk.

## What is happening

`/ai-plan` dispatches the `ai-plan` agent (relentless interrogator):

1. **Read the spec.** Parses goal, acceptance criteria, approach.
2. **Read-only codebase sweep** to verify which files will move.
3. **Pipeline classification.** Trivial / hotfix / standard / full — picks the lightest pipeline that satisfies the spec.
4. **Architecture pattern selection** from `architecture-patterns.md`.
5. **Decompose** into bite-sized tasks (2–5 minutes each).
6. **Patch hunks for mechanical edits.** When the change is a deterministic one-liner, the plan ships the actual unified diff. The build step uses that to dispatch a cheaper model tier (`haiku` vs `sonnet`).
7. **Writes `.ai-engineering/specs/plan.md`** and stops.

> **HARD GATE.** You must explicitly approve the plan before `/ai-build` will run.

## Expected output

```markdown
# Plan — spec-NNN — Add --format flag to myapp status

Pipeline: trivial
Pattern: cli-flag-extension

## Phase 1 — Implementation

- [ ] T-1.1 — RED: write failing tests for --format=json on status command
  - Agent: build
  - Files: tests/test_cli.py
  - Principles applied: §10.5 TDD
  - Gate: pytest tests/test_cli.py::test_status_format_json → 1 failed

- [ ] T-1.2 — GREEN: add --format flag to status command
  - Agent: build
  - Files: src/myapp/cli.py
  - Principles applied: §10.1 KISS, §10.3 SOLID (SRP)
  - Patch (deterministic):
    --- a/src/myapp/cli.py
    +++ b/src/myapp/cli.py
    @@ -60,7 +60,9 @@ def _register_status(subparsers):
         p = subparsers.add_parser("status")
    +    p.add_argument("--format", choices=["text", "json"], default="text")
         p.set_defaults(func=_status)
    @@ -68,5 +70,11 @@ def _status(args):
    -    print(f"branch: {branch}")
    +    data = {"branch": _branch(), "uncommitted": _uncommitted_count()}
    +    if args.format == "json":
    +        envelope = {"ok": True, "command": "status", "code": 0, "data": data, "meta": {}}
    +        print(json.dumps(envelope))
    +        return
    +    for k, v in data.items():
    +        print(f"{k}: {v}")
  - Gate: pytest tests/test_cli.py → 3 passed

- [ ] T-1.3 — REFACTOR: extract _gather_status_data helper
  - Agent: build
  - Files: src/myapp/cli.py
  - Principles applied: §10.4 DRY
  - Gate: pytest tests/test_cli.py → 3 passed
```

You approve by typing your approval keyword (default `approved`, configurable).

## What to watch for

- **Every task has an agent assignment** — that is who will execute it.
- **Every task has a `Principles applied:` line.** This is not decoration — the framework's review step checks that the implementation actually followed the principle anchor.
- **Patch hunks make the next step cheap.** When a task has a `Patch (deterministic):` block, `/ai-build` dispatches the haiku tier (fast + cheap) instead of sonnet. For a workshop on a free or low-tier API key this matters a lot.
- **RED / GREEN / REFACTOR triad.** TDD is enforced — the RED test is its own task that runs before the GREEN implementation. The framework will not let you skip this.

## On disk after this step

```
.ai-engineering/specs/spec.md           (unchanged)
.ai-engineering/specs/plan.md           (new, approved)
.ai-engineering/state/specs/spec-NNN.json   (state advanced to APPROVED)
```

## When to push back

If the plan has tasks > 5 minutes, ask `/ai-plan` to split them. If there is no RED/GREEN pairing for code-writing tasks, ask for it. If a deterministic edit is missing its `Patch (deterministic):` block, ask the planner to add one. The plan is a contract — make sure you can live with it.

## Next

→ [Step 4 — Build with TDD using `/ai-build`](04-build.md)
