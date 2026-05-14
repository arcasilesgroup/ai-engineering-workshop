# Step 2 — Brainstorm the feature

> **Time budget:** 7 minutes • **Skill:** `/ai-brainstorm`

## What you will learn

- Why the framework refuses to let you code before you think.
- How `/ai-brainstorm` interrogates you and produces an approved spec.
- What a spec looks like on disk.

## The command

```
/ai-brainstorm "I want to add a --json flag to the myapp status command, so output can be parsed by other tools."
```

You can pass the raw feature description. The skill will sharpen it for you.

## What is happening

`/ai-brainstorm` runs a structured interrogation:

1. **Prompt-enhance.** Sharpens your input into something specific.
2. **Optional evidence sweep.** Dispatches `ai-explore` to verify your idea fits the existing codebase.
3. **Interrogate** — up to 10 questions, one at a time. Multiple-choice preferred. You answer 3–5 typical.
4. **Propose 2–3 approaches** with trade-offs.
5. **Scope check.** If the change is < 3 files and no architecture decision, the skill proposes a direct resolution and stops — no spec is written. (This is the *trivial fast-path*.)
6. **Draft spec.** If non-trivial, drafts `.ai-engineering/specs/spec.md` validated against the schema.
7. **Review loop.** Up to 3 iterations of "is this spec acceptable?" — you approve or send back.
8. **Lifecycle bootstrap.** On approval, mints the spec sidecar at `.ai-engineering/state/specs/<slug>.json` in DRAFT state.

## Sample interrogation (your numbers may vary)

> **Q1.** What should the JSON envelope look like?
> 1. `{ok: true, command: "status", code: 0, data: {...}, meta: {...}}` (matches the existing CLI exit-code envelope convention)
> 2. Raw status dict, no wrapper
> 3. JSON Lines (one record per line)

You answer `1`.

> **Q2.** Does the existing text output stay the default, or do we make `--format=json` opt-in?
> 1. Text stays the default, `--json` is opt-in.
> 2. JSON becomes the default, `--text` brings the old output back.
> 3. New `--format {text,json}` flag, default `text`.

You answer `3`.

> **Q3.** Do we need backwards-compatibility for callers parsing the current text output?
> 1. No — caller will adopt the new flag.
> 2. Yes — keep the exact text output bit-identical when no flag is passed.

You answer `2`.

The skill then proposes two approaches:

- **A.** Render text and JSON from a shared dict, switch on `args.format`.
- **B.** Two separate render functions, dispatcher picks one.

You pick **A** (simpler, DRY).

## Expected artifact on disk

After you approve the spec, the file lives at:

```
.ai-engineering/specs/spec.md
```

It will contain:

- Frontmatter: `spec: spec-NNN`, `effort: small`, `status: APPROVED`
- Sections: Goal, Non-goals, User-visible behavior, Approach, Risks, Acceptance criteria, Test strategy

And the lifecycle sidecar at:

```
.ai-engineering/state/specs/spec-NNN.json
```

## What to watch for

- **The skill stops after spec approval.** It does NOT call `/ai-plan` automatically. The pause is intentional — you should sleep on a spec or get a teammate to skim it before planning.
- **Interrogation feels slow.** It is supposed to. The whole point is to surface the question you would have answered wrongly in code two days from now.
- **No code changes yet.** `git status` should still be clean except for `.ai-engineering/specs/spec.md` and `.ai-engineering/state/specs/spec-NNN.json` being new.

## Why we did not skip this step

If we had just told `/ai-build` "add a `--json` flag", the framework would have refused. **No implementation without an approved spec** is a hard rule (CONSTITUTION.md, §10.6 SDD). The 7 minutes you just spent are the entire reason the next 30 minutes will go smoothly.

## Next

→ [Step 3 — Plan it out with `/ai-plan`](03-plan.md)
