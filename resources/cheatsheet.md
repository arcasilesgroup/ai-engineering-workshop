# Cheatsheet

> One page. Pin it. The canonical chain and its closest neighbors, with what each one consumes and produces.

## The canonical chain

```
/ai-start                ← session bootstrap, prints dashboard
   │
   ▼
/ai-brainstorm "<goal>"  ← writes .ai-engineering/specs/spec.md
   │
   ▼
/ai-plan                 ← writes .ai-engineering/specs/plan.md (HARD GATE: you approve)
   │
   ▼
/ai-build                ← writes code, ticks plan checkboxes, runs quality loop
   │
   ▼
/ai-pr                   ← branches, commits, opens PR, watches CI, marks shipped
```

For specs with 3+ concerns or 10+ file changes, wrap with:

```
/ai-autopilot
```

## After-shipping skills

```
/ai-review               ← multi-specialist review of a PR or diff
/ai-explain "<question>" ← engineer-grade explanation with file:line anchors
/ai-debug                ← root-cause loop for test failures and regressions
/ai-test                 ← write tests, enforce TDD, fill coverage gaps
/ai-explore "<query>"    ← read-only codebase research in a fresh context
```

## CLI primitives

```
ai-eng install .                 # bootstrap a project (one-time per project)
ai-eng doctor                    # health check
ai-eng doctor --fix              # interactive remediation
ai-eng update --apply            # update framework files
ai-eng gate run --json           # run all hot-path gates
ai-eng audit query "SELECT ..."  # SQL over the audit index
ai-eng audit replay --session X  # span-tree walk of a session
ai-eng risk accept --finding-id  # formally accept a known risk
ai-eng cleanup                   # prune merged branches, sync to remote
ai-eng version                   # version
```

## Hard rules (CONSTITUTION + §10)

1. **No code without an approved spec.** `/ai-brainstorm` first.
2. **TDD enforced.** RED → GREEN → REFACTOR, each as its own plan task.
3. **No suppression.** No `# noqa`, `# nosec`, `// @ts-ignore`. Refactor or risk-accept.
4. **No back-compat shims.** Hard rename, hard delete, CHANGELOG entry.
5. **Conventional Commits, never `--no-verify`.**
6. **Secrets gate on every commit, push gate before push.**
7. **One commit changes one thing.** Drive-by refactors get their own commit.
8. **No new module without a clear seam.** No abstraction without two callers.

## §10 engineering principles (cited in every plan task)

| § | Principle | One-line |
|---|-----------|----------|
| 10.1 | KISS | The simplest design that satisfies the requirement wins. |
| 10.2 | YAGNI | Build for the spec in front of you. |
| 10.3 | SOLID | SRP / OCP / LSP / ISP / DIP. |
| 10.4 | DRY | Three copies = extract. |
| 10.5 | TDD | RED → GREEN → REFACTOR. |
| 10.6 | SDD | Every implementation traces back to a spec. |
| 10.7 | Clean Code | Names tell the story; functions ≤ 30 lines. |
| 10.8 | Hexagonal | Domain inward, adapters outward. |

## Surfaces (IDE adapters)

| IDE | `--surface` value | Slash syntax |
|-----|-------------------|-------------|
| Claude Code | `claude-code` | `/ai-<name>` |
| GitHub Copilot | `github-copilot` | `/ai-<name>` |
| OpenAI Codex | `codex` | `/ai-<name>` |
| Gemini CLI | `gemini-cli` | `/ai-<name>` |
| OpenCode | `opencode` | `/ai-<name>` |
| Cursor | `cursor` | `/ai-<name>` |
| Antigravity | `antigravity` | `/ai-<name>` |

## Optional helpers

| Tool | Purpose | Install |
|------|---------|---------|
| Engram | Cross-session memory MCP | `brew install engram && engram setup claude_code` |
| RTK | `PreToolUse` hook, 60–90% token savings on dev ops | `brew install rtk`, wire `rtk hook claude` |
| Squeezr | MITM compression proxy for Claude + Codex + Gemini | `npm i -g squeezr-ai && squeezr setup && squeezr start` |
| Context7 | Live library docs MCP | `claude mcp add --transport http context7 https://mcp.context7.com/mcp` |

## What to type when

- Brand new feature → `/ai-brainstorm "<goal>"`
- Bug report → `/ai-debug "<symptom>"`
- Plan rejected → `/ai-plan` (re-runs) or send corrections
- Plan accepted, code not yet written → `/ai-build`
- Code written, want to ship → `/ai-pr`
- Code written, want a second opinion first → `/ai-review`
- Code written, want to understand it → `/ai-explain`
- Lost track of session → `/ai-start`
- "Where does X live?" → `/ai-explore "<question>"`
