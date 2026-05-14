# Pre-Event Setup

> Do this **the week before the workshop**, not the morning of.

We have 45 minutes to teach the framework. We do not have 45 minutes to debug Python, fix `PATH`, or chase a missing `uv`. Arrive with `ai-eng` working and you will get the most out of the session.

## Order

| # | Step | Required? | Time |
|---|------|-----------|------|
| 1 | [Install ai-engineering](01-install-ai-engineering.md) | **Yes** | 10 min |
| 2 | [Engram (cross-session memory)](02-engram-optional.md) | Optional | 5 min |
| 3 | [RTK + Squeezr (token savings)](03-rtk-squeezr-optional.md) | Optional | 10 min |
| 4 | [Context7 (live library docs)](04-context7-optional.md) | Optional | 3 min |
| ★ | [Troubleshooting](99-troubleshooting.md) | reference | as needed |

## What you need

- **macOS, Linux, or Windows (WSL2 recommended on Windows).**
- **Git** + **GitHub CLI** (`gh auth login` working).
- **An AI coding IDE.** Workshop uses **Claude Code** as primary; GitHub Copilot, OpenAI Codex, Gemini CLI, OpenCode, and Cursor all work too — just substitute the slash command surface.
- **Python 3.11+** and **uv** (we will install these in step 1 if missing).
- **A free GitHub account** that can push to public repos.

## Confidence check

After completing step 1, you should be able to run this from a fresh terminal and get a non-error response:

```bash
ai-eng version
```

Expected output (version number may differ):

```
ai-eng 0.4.0
```

If that works, you are ready. The optional steps add quality-of-life upgrades but the workshop runs fine without them.
