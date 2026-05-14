# Step 7 — Learn what was built

> **Time budget:** 2 minutes • **Skill:** `/ai-explain`

## What you will learn

- How to use the framework as a teaching tool, not just a code generator.
- Why the explanation is anchored to real file:line citations.

## The command

```
/ai-explain "Walk me through the new --format=json path in myapp status. What does the data flow look like, end to end?"
```

You can also point it at a file or a function:

```
/ai-explain src/myapp/cli.py:_status
/ai-explain --depth deep src/myapp/cli.py
```

## What is happening

`/ai-explain` produces engineer-grade explanations with three depth levels:

- `--depth brief` — a one-paragraph TL;DR.
- `--depth standard` (default) — ASCII diagram + key file:line anchors + main control flow.
- `--depth deep` — execution trace, edge cases, design rationale.

## Expected output (standard depth)

```markdown
# How --format=json flows through myapp status

```
$ myapp status --format=json
        │
        ▼
[cli.py:42  main()]                 argparse parses argv → args.format = "json"
        │
        ▼
[cli.py:60  _register_status()]     subparser "status" registered; .func = _status
        │
        ▼
[cli.py:70  _status(args)]          gather data (branch, uncommitted)
        │                            ─ branch via subprocess: git rev-parse --abbrev-ref HEAD
        │                            ─ uncommitted via subprocess: git status --porcelain | wc -l
        │
        ▼
        if args.format == "json":
            envelope = {"ok": True, "command": "status",
                        "code": 0, "data": data, "meta": {}}
            print(json.dumps(envelope))
            return
        else:
            for k, v in data.items():
                print(f"{k}: {v}")
```

## Key design choices

- **Why a single render function, not two?** The plan picked Approach A (DRY). Both paths
  start from the same `data` dict; only the rendering branches. This keeps the data-gathering
  logic in one place and makes adding a future format (yaml, toml) a 3-line patch.

- **Why `meta: {}` and not omitted?** The spec calls for a stable envelope shape across commands.
  Callers can rely on `meta` existing as a dict, even when empty. Future commands may populate it
  (timestamps, durations) without breaking the schema.

- **Where errors land.** No try/except added — argparse rejects bad `--format` values with
  exit code 2 before `_status` is called. The deterministic adapter at
  `.ai-engineering/overrides/python/error_envelope.py` handles process-level error envelopes
  for the JSON path.
```

## What to watch for

- **Diagrams have line numbers.** Every node is clickable. The skill is anchored to actual code, not a hallucinated description.
- **"Key design choices"** trace back to the spec and plan you wrote. The framework remembers *why* the code looks like this, not just *what* it does.

## Why this matters at the end of the workshop

You did not write a single line of code in this 45 minutes. You wrote a spec, approved a plan, and watched a build run. The risk of that workflow is *not understanding what was built*.

`/ai-explain` closes that gap. After `/ai-build` lands and `/ai-pr` ships, you spend 2 minutes asking the framework to teach you back what it did. By the time you walk away, you understand the code as if you had typed it yourself.

## Real-world use

- After any non-trivial `/ai-build`.
- Onboarding a teammate to a module: `/ai-explain --depth deep src/auth/`.
- Code archaeology: `/ai-explain --depth deep --include-history src/payments/charge.py`.

## You finished the workshop

```
3 min   /ai-start         ← you are oriented
5 min   /ai-explore       ← you mapped the codebase
7 min   /ai-brainstorm    ← you have an approved spec
7 min   /ai-plan          ← you have an approved plan
10 min  /ai-build         ← TDD-gated, tests passing
6 min   /ai-pr            ← merged PR
5 min   /ai-review        ← multi-specialist review
2 min   /ai-explain       ← you understand what shipped
─────────
45 min  end to end
```

That is the entire canonical chain. Everything else in `ai-engineering` is a variation on this theme.

## Where to go next

- Read the [cheatsheet](../resources/cheatsheet.md) — pin it somewhere visible.
- Read the [upstream framework repo](https://github.com/arcasilesgroup/ai-engineering) — there are 47 skills total; you used 8 today. The other 39 are waiting.
- Run the same exercise on **your own** project: clone it, `ai-eng install .`, pick a small feature you have been putting off, run the chain.
- Open an issue on this workshop repo if you spot a typo, a stale command, or a gap.

Thanks for showing up.
