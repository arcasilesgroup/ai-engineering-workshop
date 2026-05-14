# ai-engineering Workshop

> 45-minute hands-on workshop that takes you from zero to a merged PR through the canonical AI-governed chain: `/ai-start → /ai-brainstorm → /ai-plan → /ai-build → /ai-pr`.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![ai-engineering](https://img.shields.io/badge/built%20on-ai--engineering-7c3aed.svg)](https://github.com/arcasilesgroup/ai-engineering)

## What you will learn

By the end of the 45-minute session you will have:

- Installed and verified `ai-engineering` on your laptop.
- Bootstrapped a fresh project as a governed AI workspace.
- Driven a real feature through `/ai-brainstorm → /ai-plan → /ai-build → /ai-pr`.
- Watched a parallel multi-specialist code review run via `/ai-review`.
- Used `/ai-explain` to learn what the framework just built.

This is *not* a slideshow. You will be typing.

## Two parts to this repo

### 1. [Pre-event setup](pre-event/) — do this 1 week before the workshop

Arrive with `ai-eng` working on your laptop. We will not debug Python or `uv` together during the workshop — there is not enough time. Optional helper tools (Engram, RTK, Squeezr, Context7) are documented separately so you can pick what fits you.

| Step | Time | Required? |
|------|------|-----------|
| [1. Install ai-engineering](pre-event/01-install-ai-engineering.md) | 10 min | **Yes** |
| [2. Engram (cross-session memory)](pre-event/02-engram-optional.md) | 5 min | Optional |
| [3. RTK + Squeezr (token savings)](pre-event/03-rtk-squeezr-optional.md) | 10 min | Optional |
| [4. Context7 (live library docs)](pre-event/04-context7-optional.md) | 3 min | Optional |
| [5. Troubleshooting](pre-event/99-troubleshooting.md) | as needed | reference |

### 2. [Workshop](workshop/) — what we will do together (45 minutes)

A step-by-step path you can follow live, on stream, or solo. Every step has the exact commands and an expected output snippet so you can confirm you are on track.

| Step | Skill | Time |
|------|-------|------|
| [0. Warm-up + dashboard](workshop/00-warmup.md) | `/ai-start` | 3 min |
| [1. Explore your codebase](workshop/01-explore.md) | `/ai-explore` | 5 min |
| [2. Brainstorm the feature](workshop/02-brainstorm.md) | `/ai-brainstorm` | 7 min |
| [3. Plan it out](workshop/03-plan.md) | `/ai-plan` | 7 min |
| [4. Build with TDD](workshop/04-build.md) | `/ai-build` | 10 min |
| [5. Open the PR](workshop/05-pr.md) | `/ai-pr` | 6 min |
| [6. Multi-specialist review](workshop/06-review.md) | `/ai-review` | 5 min |
| [7. Learn what you built](workshop/07-explain.md) | `/ai-explain` | 2 min |
| **Total** | | **45 min** |

## Resources

- [Cheatsheet](resources/cheatsheet.md) — one-page command reference
- [Starter project](resources/starter/) — the tiny CLI we will modify together
- [Exercise spec](resources/exercise-spec-example.md) — the feature we will build, written as a real ai-engineering spec

## What is ai-engineering?

`ai-engineering` is an MIT-licensed framework that turns any repository into a governed AI workspace: policies, skills, agents, runbooks, and specs as versioned files. No hosted control plane. One canonical chain across Claude Code, GitHub Copilot, OpenAI Codex, Gemini CLI, OpenCode, Cursor, and Antigravity.

See the [upstream repo](https://github.com/arcasilesgroup/ai-engineering) for the full framework.

## Who runs this workshop?

[Arcasiles Group](https://github.com/arcasilesgroup) — we design and produce experiences that connect technology, culture, and community. This workshop is one of the free events we run for engineers who want to ship AI-assisted code without losing control of their codebase.

## License

[MIT](LICENSE). Fork it, run it at your meet-up, send the diff back. Pull requests welcome.
