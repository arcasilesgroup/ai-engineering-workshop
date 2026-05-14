# 3. RTK + Squeezr — token-savings tools (optional)

> **Time:** ~10 minutes • **Required:** No

These two tools sit between your AI IDE and the LLM API, cutting the number of tokens you spend by 60–90% on dev operations (long `git diff`s, `find`/`grep` output, `pytest` failures, etc.). They are **not** part of `ai-engineering` — they are independent open-source companions.

If you are paying per token (API key) or hitting daily caps, install both. If you are not, you can skip this section.

---

## RTK — Rust Token Killer

**What it is.** A native CLI proxy that registers as a `PreToolUse` hook in your AI IDE and intercepts every shell command before its output reaches the LLM. It compresses and filters output for tools that are notoriously verbose: `git status`, `git diff`, `find`, `ls`, `tree`, `grep`, `pytest`, `ruff`, `pnpm`, AWS CLI, `psql`, and more.

**Pros.**

- **Zero-overhead rewrites.** Once wired, every `Bash` call is intercepted at the IDE layer. You do not change a single prompt or command.
- **Measurable savings.** `rtk gain` shows you exactly how many tokens were saved across your sessions.
- **Multi-IDE.** Native processors for **Claude Code, Cursor, Gemini CLI, and Copilot CLI**. (Not Codex — Codex uses Squeezr's HTTPS-proxy route instead.)

### Install (macOS)

```bash
brew install rtk
rtk --version           # should print: rtk 0.X.Y
```

> **Name-collision warning.** Do **not** `cargo install rtk` — that installs a different project (`reachingforthejack/rtk`, Rust Type Kit). Use Homebrew.

### Install (Linux)

Download the latest release binary from <https://github.com/Veraticus/rtk/releases> and put it on `PATH`:

```bash
curl -fsSL https://github.com/Veraticus/rtk/releases/latest/download/rtk-linux-x86_64 \
  -o "$HOME/.local/bin/rtk"
chmod +x "$HOME/.local/bin/rtk"
```

### Wire RTK as a Claude Code `PreToolUse` hook

Edit (or create) `~/.claude/settings.json` and add:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "rtk hook claude" }
        ]
      }
    ]
  }
}
```

For Cursor, Gemini CLI, or Copilot CLI, run `rtk hook --help` to see the per-IDE wiring command. Each has its own settings location.

### Verify

```bash
rtk gain
# expected: a small table with calls, tokens-in, tokens-out, savings %
```

After your next session, `rtk gain` should show non-zero numbers.

---

## Squeezr (`squeezr-ai`)

**What it is.** A Node.js MITM compression proxy that sits between your AI IDE and the Anthropic/OpenAI/Gemini API. It adaptively compresses tool results sent back as context — gentle when your context window is mostly empty, aggressive as it fills up.

**Pros.**

- **Works for Claude Code AND Codex CLI** (the only token-savings tool that wires Codex natively — RTK does not).
- **Adaptive thresholds.** 1500 chars at <50% context fill, drops to 150 chars at >90%.
- **Optional local Ollama model** for AI-assisted compression of long tool results, at no extra API cost.
- **Live dashboard** at `http://localhost:<port>/squeezr/dashboard` showing savings per tool, per session.

### Install

```bash
npm install -g squeezr-ai
squeezr setup           # generates a MITM CA at ~/.squeezr/mitm-ca/bundle.crt
squeezr start           # starts the proxy daemon
```

### Trust the MITM CA

`squeezr setup` will print one command per OS to register its CA with your system trust store. Run that command. On macOS it ends with `security add-trusted-cert ...`; on Linux it copies to `/usr/local/share/ca-certificates/`.

### Wire your IDE

Add these to your shell profile (`~/.zshrc`, `~/.bashrc`):

```bash
# Claude Code — HTTP route
export ANTHROPIC_BASE_URL="http://localhost:8089"
export NODE_EXTRA_CA_CERTS="$HOME/.squeezr/mitm-ca/bundle.crt"

# Codex CLI — MITM HTTPS_PROXY route
# (scope to the codex command only so other tooling is not proxied)
codex() {
  HTTPS_PROXY="http://localhost:8090" command codex "$@"
}

# Gemini CLI — HTTP route
export GEMINI_API_BASE_URL="http://localhost:8089"
```

Then:

```bash
exec "$SHELL" -l
```

> **macOS GUI launch gotcha.** Shell wrappers and exported env vars only apply to terminal-launched sessions. If you launch Claude Code from Spotlight or the Dock, it inherits the launchd environment, not your shell. Either always start Claude Code from a terminal that has the wrappers loaded, or set the env vars at the launchd level with `launchctl setenv`.

### Verify

Open the live dashboard:

```bash
open http://localhost:8089/squeezr/dashboard
```

Run any AI session that triggers a few `Bash` calls. You should see the dashboard fill in with per-tool savings.

---

## RTK vs Squeezr — when to use what

| | RTK | Squeezr |
|---|---|---|
| Where it sits | IDE `PreToolUse` hook | MITM HTTPS proxy |
| Claude Code | ✅ | ✅ |
| Cursor | ✅ | ⚠️ env inheritance |
| Gemini CLI | ✅ | ✅ |
| Copilot CLI | ✅ | ❌ |
| Codex CLI | ❌ | ✅ |
| Aider | ❌ | ✅ |
| Compresses tool *output* | ✅ | ✅ |
| Compresses LLM API *requests* | ❌ | ✅ |
| Setup difficulty | Low (one JSON entry) | Medium (CA trust + env vars) |

**Recommendation for the workshop:** install **RTK** (5 min, hook-only) for the immediate savings on `git status` / `find` / `pytest`. Install Squeezr later if you also use Codex CLI or want adaptive request-level compression.

Both can run side-by-side. They do not conflict.

---

## Next

- [4. Context7](04-context7-optional.md) — live library docs MCP (3 minutes).
- [The workshop](../workshop/) — when you are ready.
