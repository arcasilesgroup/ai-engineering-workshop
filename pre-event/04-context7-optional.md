# 4. Context7 — live library docs MCP (optional)

> **Time:** ~3 minutes • **Required:** No • **Works with:** Claude Code, OpenAI Codex, Cursor

Your model has a training cutoff. Real library APIs change after that cutoff. **Context7** is an MCP server that fetches current, version-accurate documentation on demand — for React, Next.js, Prisma, Express, Tailwind, Django, Spring Boot, FastAPI, and thousands of other libraries.

When wired correctly, your IDE will call Context7 automatically whenever you ask about a library, *before* answering from training data.

---

## Pros

- **No more "confident but wrong" library answers.** API renames, deprecated flags, new options — Context7 reads the current docs.
- **Trimmed snippets, not full docs.** The server returns only the relevant section, so token cost stays low.
- **Passive activation.** Once the rule file is in place, your IDE invokes it without you typing anything.
- **Multi-IDE.** Works with Claude Code, Codex (via `~/.codex/config.toml`), and Cursor (via `.cursor/mcp.json`).

---

## Install for Claude Code

```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp
```

That is it. The MCP is now configured at the user level (works in every project).

> If you are using the Claude Code plugin marketplace, you can also install Context7 via `/plugins` → search "context7" → install. Either path works; the marketplace install just writes the same MCP entry.

---

## Install for OpenAI Codex

Edit `~/.codex/config.toml`:

```toml
[mcp_servers.context7]
url = "https://mcp.context7.com/mcp"
transport = "http"
```

---

## Install for Cursor

Edit `.cursor/mcp.json` in your project root (or `~/.cursor/mcp.json` for user-wide):

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "transport": "http"
    }
  }
}
```

---

## Auto-invocation rule (Claude Code)

For the IDE to call Context7 *automatically* when you ask about a library — without you typing the MCP tool name — drop this into `~/.claude/rules/context7.md`:

```markdown
Use Context7 MCP to fetch current documentation whenever the user asks about
a library, framework, SDK, API, CLI tool, or cloud service — even well-known
ones like React, Next.js, Prisma, Express, Tailwind, Django, or Spring Boot.

Steps:
1. Call `resolve-library-id` with the library name.
2. Call `query-docs` with the chosen ID and the user's full question.
3. Answer using the fetched docs.

Do not use for: refactoring, writing scripts from scratch, debugging business
logic, code review, or general programming concepts.
```

For Codex and Cursor, equivalent rules live in their own rules/instructions files.

---

## Verify

Restart your IDE. In a fresh session, ask something library-specific:

> "What is the latest API for streaming responses in the Anthropic SDK?"

You should see the IDE call `mcp__context7__resolve-library-id` followed by `mcp__context7__query-docs` before answering.

If it does not, double-check:

1. The MCP was added (`claude mcp list` should show `context7`).
2. The rule file exists at `~/.claude/rules/context7.md`.
3. You restarted the IDE (MCPs are loaded at start).

---

## Cost

Context7 hosted is free for individual use at the time of writing. Check <https://context7.com/> for current limits and any paid tiers.

---

## Next

- [The workshop](../workshop/) — you are ready.
- [Troubleshooting](99-troubleshooting.md) if anything from steps 1–4 is not working.
