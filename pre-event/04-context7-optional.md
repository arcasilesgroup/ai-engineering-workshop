# 4. Context7 — documentación actualizada vía MCP (opcional)

> **Tiempo:** ~3 minutos • **Obligatorio:** no • **Oficial:** [Context7 docs](https://context7.com/docs)

Context7 permite que tu agente consulte documentación actual de librerías, SDKs y CLIs antes de responder. Es útil para evitar respuestas obsoletas sobre APIs que cambian rápido.

Instalación oficial: <https://context7.com/docs/installation>

## Ruta recomendada — setup automático

La forma más fácil es usar el CLI oficial `ctx7`:

```bash
npx ctx7 setup
```

Cuando pregunte:

1. **How should your agent access Context7?** → elige **MCP server**.
2. **Which agents do you want to set up?** → selecciona los que uses: Claude Code, Cursor, OpenCode, Codex, Gemini CLI.
3. Se abrirá el navegador para login. Completa OAuth.
4. Espera a ver `Context7 setup complete`.

El setup automático configura, según los agentes seleccionados:

- Servidor MCP con API key.
- Regla de auto-invocación para usar Context7 cuando preguntes por librerías, SDKs, APIs, CLIs o servicios cloud.
- Skill/contexto local de Context7 para el agente.

Ejemplo de archivos que puede tocar:

| Agente | Configuración típica |
|---|---|
| Claude Code | `~/.claude.json`, `~/.claude/rules/context7.md`, `~/.claude/skills/context7-mcp/` |
| Cursor | `~/.cursor/mcp.json`, `~/.cursor/rules/context7.mdc`, `~/.cursor/skills/context7-mcp/` |
| OpenCode | `~/.config/opencode/opencode.json`, `~/.config/opencode/AGENTS.md` |
| Codex | `~/.codex/config.toml`, `~/.codex/AGENTS.md` |
| Gemini CLI | `~/.gemini/settings.json`, `~/.gemini/GEMINI.md` |

## Setup para un solo agente

Si no quieres configurar todos, puedes apuntar a uno concreto:

```bash
npx ctx7 setup --claude
npx ctx7 setup --cursor
npx ctx7 setup --opencode
```

## Verificar

Reinicia el agente y pregunta algo de una librería concreta, por ejemplo:

```text
What is the current uv command to install a tool from a GitHub repository?
```

Deberías ver llamadas a `resolve-library-id` y `query-docs` antes de la respuesta, o una indicación clara de que Context7 está usando documentación actual.

## Desinstalar

Si necesitas revertir la configuración:

```bash
npx ctx7 remove
```

## Siguiente

- [5. AgentsView](05-agentsview-optional.md)
- [Playground pre-evento](playground/)
- [Troubleshooting](99-troubleshooting.md)
