# 2. Engram — memoria entre sesiones (opcional)

> **Tiempo:** ~5 minutos • **Obligatorio:** no • **Oficial:** [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)

`ai-engineering` guarda specs, planes, decisiones y estado dentro del repo. **Engram** añade una memoria MCP para que tu agente recuerde decisiones, bugs, convenciones y handoffs entre sesiones.

Instálalo solo si trabajas mucho con agentes y no quieres reexplicar contexto cada día.

## Instalación rápida

macOS:

```bash
brew install gentleman-programming/tap/engram
engram --version
```

Linux / Windows / otros gestores:

- Sigue la guía oficial: <https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md>

## Conectar con tu agente

Claude Code — ruta recomendada por Engram:

```bash
claude plugin marketplace add Gentleman-Programming/engram
claude plugin install engram
```

Codex:

```bash
engram setup codex
```

Gemini CLI:

```bash
engram setup gemini-cli
```

OpenCode:

```bash
engram setup opencode
```

Otros clientes MCP:

- Sigue la guía oficial de agentes: <https://github.com/Gentleman-Programming/engram/blob/main/docs/AGENT-SETUP.md>

## Verificar

Reinicia tu IDE/agente y prueba una llamada a memoria:

```text
mem_context
```

Si ves historial o una respuesta estructurada, Engram está conectado. Si aparece `tool not found`, el binario existe pero el MCP no está registrado en tu agente.

## Qué cambia en el día a día

Sin Engram | Con Engram
--- | ---
Cada sesión empieza casi desde cero. | `mem_context` recupera contexto relevante.
Las decisiones viven solo si las escribes en archivos. | `mem_save` guarda decisiones y descubrimientos buscables.
Después de una compactación se pierde contexto conversacional. | `mem_session_summary` deja handoffs reutilizables.

## Siguiente

- [3. RTK](03-rtk-optional.md)
- [4. Context7](04-context7-optional.md)
- [5. AgentsView](05-agentsview-optional.md)
- [Playground pre-evento](playground/)
