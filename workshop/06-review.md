# Step 6 — Multi-specialist code review

> **Time budget:** 5 minutes • **Skill:** `/ai-review`

## What you will learn

- How the framework runs a real, parallel, multi-specialist code review.
- Why specialist context isolation produces better findings than one big "review my code" prompt.
- How to use review as a *learning tool*, not just a quality gate.

## The command

```
/ai-review
```

If your PR is still open, the skill picks it up automatically. To review a specific PR or diff:

```
/ai-review --pr <number>
/ai-review --files src/myapp/cli.py
```

## What is happening

`/ai-review` is an **orchestrator** that dispatches up to 10 specialist agents in parallel via the Agent tool. Each specialist:

- Has its own fresh context window (their reviews do not contaminate each other).
- Has a focused prompt: only one concern.
- Reads only the diff + the minimum supporting files to judge that concern.

The specialists relevant to our `--format=json` change:

| Specialist | Looking for |
|---|---|
| `reviewer-context` | Pre-review: gathers architectural context so other specialists do not have to. |
| `reviewer-correctness` | Does the code do what the PR claims? Does the JSON envelope shape match the spec? |
| `reviewer-maintainability` | Is the code readable, well-named, simple? |
| `reviewer-architecture` | Is this the right approach? Is there an established pattern we should follow? |
| `reviewer-testing` | Does the test cover the new behavior + edge cases? |
| `reviewer-compatibility` | Does this break existing callers parsing the text output? |
| `reviewer-security` | Any injection / leak risks in the new JSON path? |
| `reviewer-performance` | Any O(n²) or unbounded work introduced? |
| `reviewer-validator` | Adversarial: receives only the findings, tries to disprove them. |

After all specialists return, the orchestrator deduplicates, merges, and ranks findings by severity.

## Expected output

```markdown
# Review — PR #1 — feat(cli): add --format flag to myapp status

**Blockers:** 0
**Major:** 0
**Minor:** 2
**Suggestions:** 3

## Minor

### 1. Missing test for invalid --format value (testing)

`tests/test_cli.py` covers `--format=text` (default) and `--format=json` but no test
asserts behavior on `--format=yaml` (an invalid choice). argparse will reject it with
exit code 2, but a test pinning that behavior would prevent silent regression if
choices change later.

→ Suggested test in [tests/test_cli.py:25](...).

### 2. JSON envelope `meta` field is empty (correctness)

The spec calls for `{ok, command, code, data, meta}` with `meta` populated by `timestamp`
or `version` at minimum. Current impl always emits `"meta": {}`. Either populate meta
or update the spec to mark it as a reserved-empty placeholder.

## Suggestions

1. Add `--format=json-lines` as a future-proof option (deferred — not in scope, but worth a follow-up spec).
2. Consider extracting `_render_text(data)` and `_render_json(data)` into a small render module for symmetry.
3. The `Conventional Commit` subject could be `feat(cli)` not just `feat:` — current scope is implicit.
```

## What to watch for

- **The blockers count is 0.** If it were > 0, the framework would expect you to address them before considering the PR shippable.
- **Findings cite line numbers.** Click through one to see the agent's reasoning.
- **The validator agent runs LAST.** It tries to disprove findings — if a finding is wrong, the validator removes it. This is the framework's adversarial-truth check.

## Why this beats "review my code, please"

A single-prompt review of a code change is rate-limited by how many concerns the model can keep in its head at once. Five distinct concerns (security, performance, correctness, etc.) compete for attention. By dispatching one specialist per concern with a tightly-scoped prompt and a fresh context, each concern gets full focus. The result: more findings, fewer false positives, less noise.

## Real-world use

- Run `/ai-review` **after** `/ai-pr` opens the draft PR — find issues before reviewers do.
- Run `/ai-review --pr 123` on a teammate's PR to get a second opinion before approving.
- Run `/ai-review --files src/big-rewrite/` as a sanity pass before opening any PR at all.

## Next

→ [Step 7 — Learn what was built with `/ai-explain`](07-explain.md)
