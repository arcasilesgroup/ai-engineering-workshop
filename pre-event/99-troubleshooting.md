# Troubleshooting

> Reference for pre-event setup. If you hit something not listed here, open an issue on this repo with the exact error + your OS.

---

## `ai-eng: command not found`

The `uv tool install` step worked but `~/.local/bin` is not on your `PATH`.

**Fix (bash / zsh):**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
exec "$SHELL" -l
```

**Fix (PowerShell):**

```powershell
[Environment]::SetEnvironmentVariable("Path", "$env:Path;$env:USERPROFILE\.local\bin", "User")
# then restart the terminal
```

Verify:

```bash
which ai-eng           # should print the path
ai-eng version         # should print the version
```

---

## `uv: command not found` after install

The `uv` installer puts the binary at `~/.local/bin/uv`. Same fix as above — add `~/.local/bin` to `PATH`.

---

## `ai-eng install` configuró otro IDE/agente

Re-run the installer from the same folder and select the IDE/agent you actually use when the interactive prompt asks:

```bash
ai-eng install
```

Supported IDEs/agents include Claude Code, OpenAI Codex, Gemini CLI, GitHub Copilot, OpenCode, Cursor and Antigravity.

---

## Git hooks not firing on commit

After `ai-eng install`, check:

```bash
ls -l .git/hooks/pre-commit .git/hooks/commit-msg .git/hooks/pre-push
```

All three should exist and be executable. If they are not:

```bash
ai-eng doctor --phase hooks --fix
```

If you see the hooks but they do not fire, your git might be running with a custom `core.hooksPath`:

```bash
git config --get core.hooksPath
# if this prints anything other than empty, that's your problem
git config --unset core.hooksPath
```

---

## `state.db is locked`

Another process (an editor, an aborted `ai-eng` run) has the SQLite file open.

```bash
# find the holder
lsof | grep state.db          # macOS / Linux
# kill it, or close the editor that has it open
```

Then retry the command.

---

## `gitleaks` is missing or fails on commit

The installer auto-installs `gitleaks` but on first run, your shell may not have re-loaded `PATH`. Fix:

```bash
exec "$SHELL" -l
which gitleaks                # should print a path
```

If still missing:

```bash
brew install gitleaks         # macOS
# or
ai-eng install
```

---

## `/ai-start` or `/ai-brainstorm` does not appear / does nothing

Most of the time, the agent is open in the wrong folder. The slash commands live in the project where you ran `ai-eng install`.

For the pre-event playground, go to the folder where you ran `ai-eng install`:

```bash
cd /ruta/a/tu/carpeta-de-prueba
ai-eng doctor
```

Then open your IDE/agent with **that exact folder** as the project root and type `/ai-start` in the agent chat. Do not open the root of `ai-engineering-workshop` unless that is the project you intentionally want to modify.

---

## Claude Code does not show the `/ai-<name>` slash commands

The skills are present under `.claude/skills/ai-*/SKILL.md` but Claude Code has not picked them up.

1. Close and re-open Claude Code (skills are loaded at start).
2. Run `claude mcp list` to confirm Claude Code can read the config.
3. Verify the skills exist on disk: `ls .claude/skills/`.
4. Ensure you opened Claude Code **inside the project directory** (skills are project-scoped).

---

## "I do not have Claude Code, I have $OTHER_IDE"

The framework supports Claude Code, GitHub Copilot, OpenAI Codex, Gemini CLI, OpenCode, Cursor and Antigravity. Run `ai-eng install` from your project folder and select your IDE/agent when prompted.

The pre-event playground uses Claude Code slash syntax (`/ai-brainstorm`, etc.). The same ai-engineering skills are generated for each supported IDE.

---

## Engram MCP commands return "tool not found"

You installed the binary but did not run the per-IDE setup. Run:

```bash
engram setup claude-code         # or codex, gemini-cli
```

Then restart your IDE.

---

## RTK hook fires but `rtk gain` shows zero

Either no commands have run yet, or the hook is misconfigured. Run:

```bash
rtk init --show
```

If the hook is missing, re-run:

```bash
rtk init -g
```

---

## Squeezr is no longer in the pre-event path

We intentionally removed Squeezr from the recommended pre-event setup. It can be useful for advanced users, but it requires local proxying, CA trust and/or `HTTPS_PROXY` routing that behaves differently across CLI, GUI apps, macOS, Linux and Windows. For a cross-OS workshop, it is too easy to break networking or route unrelated tools through the proxy.

If you already use Squeezr and understand the trade-offs, follow its official docs directly. Otherwise, skip it.

---

## AgentsView opens but shows no sessions

AgentsView only shows sessions that exist on your machine and that it can discover. Try this:

1. Run at least one real session in Claude Code, Codex, Gemini, Cursor, etc.
2. Sync manually:
   ```bash
   agentsview sync
   ```
3. If you are running the web UI from CLI, use a known port:
   ```bash
   agentsview serve --port 9090
   ```
   Then open `http://127.0.0.1:9090`.
4. If your agent stores sessions in a custom location, configure the matching env var, e.g.:
   ```bash
   export CLAUDE_PROJECTS_DIR=~/custom/claude/projects
   export CODEX_SESSIONS_DIR=~/custom/codex/sessions
   agentsview serve --port 9090
   ```
5. Do not expose AgentsView with `--host 0.0.0.0` during the workshop; local session histories may contain prompts, file paths, outputs or secrets pasted into chats.

---

## I just want to nuke everything and restart

```bash
# remove ai-eng globally
uv tool uninstall ai-engineering

# remove the framework clone
rm -rf /path/to/ai-engineering

# remove a per-project install
rm -rf .ai-engineering .claude .codex .gemini .opencode .cursor
git checkout -- .git/hooks/         # if your project uses gitleaks/etc, restore originals
```

Then re-run [pre-event step 1](01-install-ai-engineering.md) from the top.

---

## Still stuck?

Open an issue at <https://github.com/arcasilesgroup/ai-engineering-workshop/issues> with:

- Your OS + version
- Output of `ai-eng doctor --json` (if you got that far)
- The exact command that failed and its full error
