# 1. Install ai-engineering

> **Time:** ~10 minutes • **Required:** Yes

`ai-engineering` is the open-source framework we are teaching. It ships as a Python tool called `ai-eng` that you install once globally, then run inside any project to make that project a governed AI workspace.

This guide installs the framework from source (the current, dogfood-tested path). It works on macOS, Linux, and Windows.

---

## Step 1.1 — Install the prerequisites

You need three things on your `PATH`:

- **Git** 2.30+
- **Python 3.11+**
- **uv** (the Python package manager that drives the install)

### macOS

```bash
# git + python (skip if already installed)
brew install git python@3.12

# uv
curl -LsSf https://astral.sh/uv/install.sh | sh
exec "$SHELL" -l         # reload shell so uv is on PATH
```

### Linux (Debian / Ubuntu)

```bash
sudo apt update && sudo apt install -y git python3.12 python3.12-venv
curl -LsSf https://astral.sh/uv/install.sh | sh
exec "$SHELL" -l
```

### Windows (PowerShell)

```powershell
winget install --id Git.Git
winget install --id Python.Python.3.12
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> **Recommended:** on Windows, use **WSL2** with Ubuntu 22.04+. The framework's git hooks, the workshop scripts, and the AI coding IDEs all have a smoother Linux story than native Windows.

### Verify

```bash
git --version       # >= 2.30
python --version    # >= 3.11
uv --version        # any current version
```

---

## Step 1.2 — Clone the framework and install `ai-eng` globally

```bash
git clone https://github.com/arcasilesgroup/ai-engineering.git
cd ai-engineering
bash scripts/dev-setup.sh        # Linux / macOS / WSL
# or:
pwsh scripts/dev-setup.ps1       # native PowerShell on Windows
```

`dev-setup` does one thing: `uv tool install --editable . --force`. This puts the `ai-eng` CLI at `$HOME/.local/bin/ai-eng` (Unix) or `$env:USERPROFILE\.local\bin\ai-eng` (Windows).

If you see a warning that `ai-eng` is not on `PATH`, add the install directory to your shell profile:

```bash
# bash / zsh
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
exec "$SHELL" -l
```

```powershell
# PowerShell — current user
[Environment]::SetEnvironmentVariable("Path", "$env:Path;$env:USERPROFILE\.local\bin", "User")
```

### Verify

```bash
ai-eng version
# expected: ai-eng 0.4.0 (or newer)
```

---

## Step 1.3 — Bootstrap a project

The framework is now globally available. To turn a *specific* project into a governed AI workspace you run `ai-eng install` from inside it.

For the workshop you will use a fresh starter project (see [`resources/starter/`](../resources/starter/) in this repo). Clone it down and bootstrap:

```bash
# pick any working directory you like
git clone https://github.com/arcasilesgroup/ai-engineering-workshop.git
cd ai-engineering-workshop/resources/starter
ai-eng install .
```

The installer:

1. Detects which AI IDEs you have already configured (looks for `.claude/`, `.codex/`, `.gemini/`, `.github/`, `.opencode/`, `.cursor/`, `.agent/`).
2. Asks you a single multi-select question if none are detected: **"Which AI Provider / IDE surfaces do you use?"**
3. Copies the matching skill, agent, and hook trees into your project.
4. Installs git hooks (`pre-commit`, `commit-msg`, `pre-push`) wired to `ai-eng gate`.
5. Auto-installs the deterministic tools the gates need: `gitleaks`, `semgrep`, `jq`, `opa`, `ruff`, `ty`, `pip-audit`, `pytest`.
6. Initializes `.ai-engineering/state/state.db` (SQLite) and `manifest.yml`.

**For the workshop, select `claude-code` when prompted** (you can multi-select more if you want). The walkthrough uses Claude Code commands.

---

## Step 1.4 — Health check

```bash
ai-eng doctor
```

You should see green check marks across **prereqs**, **tools**, **state**, **hooks**, and **surfaces**. If any line is red, run:

```bash
ai-eng doctor --fix
```

`doctor --fix` is interactive — it shows you what it wants to do and asks before doing it.

---

## Step 1.5 — Open your IDE and run `/ai-start`

Open Claude Code (or whichever IDE you picked) inside the starter project. Then:

```
/ai-start
```

You should see a dashboard with:

- Current branch
- Active spec (none yet — that is fine)
- Board state
- A "next action" pointer

**That is your finish line for pre-event setup.** If `/ai-start` renders cleanly, you are ready for the workshop.

---

## What just happened (quick mental model)

```
Your laptop                           Your project
─────────                             ──────────────────
$HOME/.local/bin/ai-eng     ───→      .ai-engineering/        ← governance root
(global CLI, one install)             .claude/ (or other IDE)  ← skills + agents
                                      .git/hooks/              ← gates wired
                                      CONSTITUTION.md          ← project identity
                                      CLAUDE.md / AGENTS.md    ← AI rulebook
```

Every project you want to govern gets its own `ai-eng install .`. The framework itself stays singular and global.

---

## Common issues

See [99-troubleshooting.md](99-troubleshooting.md) for:

- `ai-eng: command not found`
- `uv not on PATH`
- Hooks not firing on commit
- Surface autodetection picked the wrong IDE
- `state.db` is locked

---

## Next

- (Optional) [2. Engram](02-engram-optional.md) — adds cross-session memory.
- (Optional) [3. RTK + Squeezr](03-rtk-squeezr-optional.md) — saves 60–90% of tokens on dev operations.
- (Optional) [4. Context7](04-context7-optional.md) — live, version-accurate library docs as an MCP.
- (When ready) [The workshop](../workshop/) — what we will do together for 45 minutes.
