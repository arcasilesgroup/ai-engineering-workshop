# Exercise spec — reference output of `/ai-brainstorm` for the workshop

> **Spoiler warning.** This is the spec we expect `/ai-brainstorm` to produce during the workshop, given the prompt suggested in [`workshop/02-brainstorm.md`](../workshop/02-brainstorm.md). Read it **after** the workshop to compare against what you got, or **never** if you want the discovery to be clean. The point of the workshop is to derive this yourself with the framework's help.

---

```yaml
---
spec: spec-001-status-json-format
title: Add --format flag to myapp status command
status: APPROVED
effort: small
created: 2026-05-15
---
```

## Goal

Allow callers of `myapp status` to request machine-readable JSON output by passing `--format=json`. Preserve the existing plain-text output as the default.

## Non-goals

- We are **not** changing the data that `status` reports (still `branch` + `uncommitted`).
- We are **not** adding `--format` to other subcommands in this spec — they get their own future specs.
- We are **not** introducing a richer envelope (`error`, `warnings`, etc.) — `meta` stays empty for now, reserved for future use.

## User-visible behavior

```
$ myapp status
branch: main
uncommitted: 0

$ myapp status --format=text
branch: main
uncommitted: 0

$ myapp status --format=json
{"ok": true, "command": "status", "code": 0, "data": {"branch": "main", "uncommitted": 0}, "meta": {}}

$ myapp status --format=yaml
usage: myapp status [-h] [--format {text,json}]
myapp status: error: argument --format: invalid choice: 'yaml' (choose from 'text', 'json')
```

## Approach

Approach A — DRY: gather data once into a dict, branch only on rendering.

```python
def _status(args):
    data = {"branch": _branch(), "uncommitted": _uncommitted_count()}
    if args.format == "json":
        envelope = {"ok": True, "command": "status", "code": 0, "data": data, "meta": {}}
        print(json.dumps(envelope))
        return
    for k, v in data.items():
        print(f"{k}: {v}")
```

## Risks

- **Backwards compatibility.** The current text output is what existing shell pipelines parse. With `--format=text` as the default, the text output stays bit-identical. The risk is low.
- **JSON shape contract.** Once we ship `{ok, command, code, data, meta}`, callers will pin it. Future commands must use the same envelope or break the implicit contract. We accept this as the deliberate design: the envelope IS the contract.
- **Argparse exit codes.** Bad `--format` values exit with code 2 (argparse default). Not the framework's `_exit_codes.py` `INVALID_USAGE`. Acceptable — argparse-native behavior is the principle of least surprise.

## Acceptance criteria

- [ ] `myapp status` (no flag) emits the exact pre-change text output. Existing test passes unchanged.
- [ ] `myapp status --format=text` emits the same text output.
- [ ] `myapp status --format=json` emits a single line of valid JSON parsing to `{ok: true, command: "status", code: 0, data: {branch: str, uncommitted: int}, meta: {}}`.
- [ ] `myapp status --format=yaml` exits with code 2 and a helpful argparse error.
- [ ] `pytest tests/test_cli.py` — 3 passing tests (one pre-existing, two new for `--format`).

## Test strategy

Three pytest cases, no fixtures, no mocks:

1. `test_status_default_text` — captures stdout, asserts both lines present.
2. `test_status_format_json` — captures stdout, `json.loads` it, asserts the envelope schema.
3. `test_status_format_invalid` — uses `pytest.raises(SystemExit)`, asserts exit code 2.

## Decisions

- D-001-01 — Use `--format` with `choices=["text", "json"]`, not `--json`. Reason: leaves room for `--format=yaml/toml/etc` without flag soup.
- D-001-02 — Envelope shape locked at `{ok, command, code, data, meta}`. Reason: matches the framework's `_exit_codes.py` convention and gives every future command the same outer schema.
- D-001-03 — `meta` stays empty for now, dict not omitted. Reason: callers can rely on the key existing.

---

## Notes for the workshop

- The spec above is what we expect after **3 interrogation questions** (envelope shape, default behavior, back-compat).
- A spec like this should take 5–7 minutes to derive interactively. If yours took longer, the interrogation was probably too open-ended; if shorter, you may have skipped a question worth answering.
- This spec is small enough that `/ai-plan` will classify the pipeline as **trivial** and produce a 3-task plan (T-1.1 RED, T-1.2 GREEN, T-1.3 REFACTOR).
