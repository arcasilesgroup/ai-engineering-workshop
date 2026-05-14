# 2. Engram — cross-session memory (optional)

> **Time:** ~5 minutes • **Required:** No • **Works with:** Claude Code, OpenAI Codex, Gemini CLI

`ai-engineering` does not bundle a memory layer. **Engram** is a third-party MCP server that adds persistent memory to your AI assistant: decisions, conventions, bug-fixes, and discoveries survive across sessions. The framework works fine without it — install only if you find yourself re-explaining context every morning.

> **Why this is optional but worth it.** The framework already persists durable state on disk (decisions in `state.db`, specs in `.ai-engineering/specs/`, lessons in `LESSONS.md`). What Engram adds is *automatic injection of that state into your LLM's context*, plus semantic recall of past sessions, plus end-of-session digests. Without it, every session starts cold and you waste tokens re-reading state.

---

## Pros

- **Memory survives sessions and compactions.** Working on a bug yesterday? `mem_search "the auth header regression"` returns the prior session's decision trail today.
- **Mandatory end-of-session digests.** `mem_session_summary` writes Goal / Discoveries / Accomplished / Next Steps / Relevant Files — perfect handoff between work sessions.
- **Proactive saves.** The MCP instructs the model to call `mem_save` after every decision, bug fix, or convention — no need to remember.
- **Cross-IDE.** One memory store; works for Claude Code, Codex, and Gemini CLI in parallel.

---

## Install

### macOS

```bash
brew install engram
```

### Linux

```bash
curl -fsSL https://github.com/Gentleman-Programming/engram/releases/latest/download/engram-linux-x86_64 \
  -o "$HOME/.local/bin/engram"
chmod +x "$HOME/.local/bin/engram"
```

### Windows

```powershell
winget install Engram
```

### Verify

```bash
engram --version
```

---

## Wire it up to your IDE

Run this **once per IDE** (does not need to be re-run per project):

```bash
engram setup claude_code      # Claude Code
engram setup codex             # OpenAI Codex
engram setup gemini_cli        # Gemini CLI
```

GitHub Copilot is **not** supported by Engram (and Engram does not auto-detect that — you just will not use the `mem_*` tools from Copilot sessions).

---

## Verify the MCP is talking

Open your IDE in any project and try:

```
mem_context
```

You should see a structured response with recent session history. If you get "tool not found", Engram is installed on disk but the MCP is not wired — re-run `engram setup <your_ide>`.

You can also run:

```bash
ai-eng doctor
```

The framework's `doctor` command reports Engram status as informational — it never installs or modifies Engram itself.

---

## What changes day-to-day

Without Engram | With Engram
--- | ---
Every new session re-reads `state.db` and recent git log to reconstruct context. | `mem_context` injects ranked prior observations at session start automatically.
A decision you make today is invisible next week unless you committed it to a file. | `mem_save` persists it cross-session, searchable.
You forget what was tried in a stalled spec from 3 weeks ago. | `mem_search "the rate-limit retry approach"` brings it back.
Post-compaction the LLM loses the working context of the current session. | `mem_context` (called post-compaction) restores it.

---

## Removal

```bash
brew uninstall engram          # macOS
winget uninstall Engram        # Windows
rm "$HOME/.local/bin/engram"   # Linux
```

`ai-eng` does not touch Engram state on disk, so removal is a one-step operation.

---

## Next

- [3. RTK + Squeezr](03-rtk-squeezr-optional.md) — for token savings on dev operations.
- [4. Context7](04-context7-optional.md) — live library docs MCP.
- [The workshop](../workshop/) — when you are ready.
