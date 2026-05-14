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

## `ai-eng install .` complains the surface autodetection picked the wrong IDE

Force the surfaces you want:

```bash
ai-eng install . --surface claude-code --surface github-copilot
```

Closed enum: `claude-code, codex, gemini-cli, github-copilot, opencode, cursor, antigravity`.

---

## Git hooks not firing on commit

After `ai-eng install .`, check:

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
ai-eng install . --reinstall-tools
```

---

## Claude Code does not show the `/ai-<name>` slash commands

The skills are present under `.claude/skills/ai-*/SKILL.md` but Claude Code has not picked them up.

1. Close and re-open Claude Code (skills are loaded at start).
2. Run `claude mcp list` to confirm Claude Code can read the config.
3. Verify the skills exist on disk: `ls .claude/skills/`.
4. Ensure you opened Claude Code **inside the project directory** (skills are project-scoped).

---

## "I do not have Claude Code, I have $OTHER_IDE"

The framework supports six surfaces. Re-run `ai-eng install . --surface <name>` for your IDE:

| IDE | `--surface` value |
|-----|-------------------|
| Claude Code | `claude-code` |
| GitHub Copilot | `github-copilot` |
| OpenAI Codex | `codex` |
| Gemini CLI | `gemini-cli` |
| OpenCode | `opencode` |
| Cursor | `cursor` |
| Antigravity | `antigravity` |

The workshop uses Claude Code slash syntax (`/ai-brainstorm`, etc.); the equivalent invocation in each other IDE is documented at the upstream repo.

---

## Engram MCP commands return "tool not found"

You installed the binary but did not run the per-IDE setup. Run:

```bash
engram setup claude_code         # or codex, gemini_cli
```

Then restart your IDE.

---

## RTK hook fires but `rtk gain` shows zero

Either no commands have run yet, or the hook is misconfigured. Check `~/.claude/settings.json` for:

```json
"PreToolUse": [
  { "matcher": "Bash", "hooks": [ { "type": "command", "command": "rtk hook claude" } ] }
]
```

The `matcher` must be exactly `"Bash"` (case-sensitive). Other values silently no-op.

---

## Squeezr dashboard is empty / IDE not routing through it

Squeezr needs both env-var exports AND a launchd-aware launch on macOS.

1. Confirm the env vars in your current shell:
   ```bash
   echo "$ANTHROPIC_BASE_URL"
   echo "$NODE_EXTRA_CA_CERTS"
   ```
   Both should be set.
2. **Always launch your IDE from the same terminal that has the vars loaded** (or use `launchctl setenv` to set them at the launchd level).
3. Confirm Squeezr is running:
   ```bash
   curl http://localhost:8089/squeezr/dashboard | head
   ```

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
