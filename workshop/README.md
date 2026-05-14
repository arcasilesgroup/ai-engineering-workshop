# 45-Minute Workshop

> The plan is to take you, in 45 minutes, from a freshly-bootstrapped project to a merged pull request — through the canonical ai-engineering chain. Every step has the exact command to type, an expected-output snippet, and a "what to watch for" pointer.

## Before you start

- You completed [pre-event step 1](../pre-event/01-install-ai-engineering.md) (required).
- You have the starter project cloned and bootstrapped:

  ```bash
  git clone https://github.com/arcasilesgroup/ai-engineering-workshop.git
  cd ai-engineering-workshop/resources/starter
  ai-eng install .
  ```

- Your IDE (Claude Code recommended) is open inside `resources/starter/`.
- You have `gh auth login` working so we can open a real PR.

## The feature we will build

We are going to add a `--json` flag to the `status` command of the starter CLI (`myapp status`). The flag should make `status` emit a machine-readable JSON envelope (`{ok, command, code, data, meta}`) instead of plain text.

This is small enough to ship in 45 minutes, real enough to cross the threshold for a spec, and visual enough to demo the framework's "explain what it built" superpower at the end.

The full spec we will reach is documented at [`resources/exercise-spec-example.md`](../resources/exercise-spec-example.md) — but **do not read it before the workshop**, the whole point is to derive it with `/ai-brainstorm`.

## Schedule

| # | Step | Skill | Time | Cumulative |
|---|------|-------|------|------------|
| 0 | [Warm-up + dashboard](00-warmup.md) | `/ai-start` | 3 min | 3 |
| 1 | [Explore the codebase](01-explore.md) | `/ai-explore` | 5 min | 8 |
| 2 | [Brainstorm the feature](02-brainstorm.md) | `/ai-brainstorm` | 7 min | 15 |
| 3 | [Plan it out](03-plan.md) | `/ai-plan` | 7 min | 22 |
| 4 | [Build with TDD](04-build.md) | `/ai-build` | 10 min | 32 |
| 5 | [Open the PR](05-pr.md) | `/ai-pr` | 6 min | 38 |
| 6 | [Multi-specialist review](06-review.md) | `/ai-review` | 5 min | 43 |
| 7 | [Learn what was built](07-explain.md) | `/ai-explain` | 2 min | 45 |

> **The wall-clock budget is tight.** If you fall behind, do not panic — every step has the exact commands written down so you can catch up between steps or finish on your own afterwards.

## A note on the canonical chain

The skills below are designed to flow into each other. Each one produces an artifact (a spec, a plan, a code change, a PR) that the next one consumes. The contract is enforced by the framework:

```
/ai-start         ── dashboard, no artifact
/ai-brainstorm    → .ai-engineering/specs/spec.md
/ai-plan          → .ai-engineering/specs/plan.md
/ai-build         → source code changes + plan checkboxes ticked
/ai-pr            → branch + GitHub PR + watched until merged
```

If you try to `/ai-build` without an approved plan, the framework will stop and say so. If you try to `/ai-pr` without commits, it will stop and say so. This is not bureaucracy — it is the framework refusing to let you ship code without a paper trail.

[**Start with step 0 →**](00-warmup.md)
