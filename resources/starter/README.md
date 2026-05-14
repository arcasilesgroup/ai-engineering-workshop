# `myapp` — workshop starter project

> A minimal Python CLI used as the in-class exercise project for the [ai-engineering workshop](../../workshop/). You will install `ai-engineering` on top of this and add a feature.

## What it does

`myapp` is a stand-in for any real CLI. It exposes two subcommands:

- `myapp hello` — prints a greeting.
- `myapp status` — prints the current git branch and the number of uncommitted files.

The whole project is intentionally small (one source file, one test file) so that the workshop time is spent on the framework, not on understanding the starter code.

## Quick start

```bash
# from the workshop repo root
cd resources/starter
uv venv
source .venv/bin/activate          # or: .venv\Scripts\activate on Windows
uv pip install -e .
pytest                              # 2 tests pass
myapp hello
myapp status
```

You should see:

```
$ myapp hello
hello, world

$ myapp status
branch: main
uncommitted: 0
```

## Bootstrap as a governed AI workspace

Once `ai-eng` is on your `PATH` (see [pre-event step 1](../../pre-event/01-install-ai-engineering.md)):

```bash
ai-eng install .
```

This adds:

- `.ai-engineering/` — manifest + state.db + scripts
- `.claude/` (or your IDE's directory) — skills + agents
- `.git/hooks/` — pre-commit, commit-msg, pre-push gates wired to `ai-eng gate`

Now you are ready to run `/ai-start` in your IDE.

## Project layout

```
resources/starter/
├── README.md              ← this file
├── pyproject.toml         ← packaging + entry point
├── src/myapp/
│   ├── __init__.py
│   └── cli.py             ← argparse + the two subcommands
└── tests/
    └── test_cli.py        ← pytest, covers hello + status
```

## License

MIT — same as the workshop repo.
