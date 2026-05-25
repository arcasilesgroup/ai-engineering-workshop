# 0. Enlaces oficiales de herramientas

> Usa esta página para comprobar la fuente oficial. Los comandos copy/paste verificados para el evento están en [1. Instalar y verificar ai-engineering](01-install-ai-engineering.md).

Última revisión de enlaces: **25 mayo 2026**.

## Herramientas base

| Herramienta | Para qué la usamos | README / home oficial | Instalación oficial |
|---|---|---|---|
| ai-engineering | Framework del workshop (`ai-eng`) | [GitHub: arcasilesgroup/ai-engineering](https://github.com/arcasilesgroup/ai-engineering) | [PyPI: ai-engineering](https://pypi.org/project/ai-engineering/) · [README upstream](https://github.com/arcasilesgroup/ai-engineering#install) |
| Git | Clonar repos y trabajar con ramas | [git-scm.com](https://git-scm.com/) | [Installing Git — Pro Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) |
| GitHub CLI (`gh`) | Login, forks, PRs y checks | [GitHub CLI README](https://github.com/cli/cli#readme) | [Installation — GitHub CLI](https://github.com/cli/cli#installation) · [`gh auth login`](https://cli.github.com/manual/gh_auth_login) |
| Python | Runtime requerido por `ai-eng` y proyectos Python | [python.org](https://www.python.org/) | [Python downloads](https://www.python.org/downloads/) |
| uv | Instalar herramientas Python y ejecutar proyectos de prueba | [uv README](https://github.com/astral-sh/uv#readme) | [Installing uv](https://docs.astral.sh/uv/getting-started/installation/) |
| pipx | Alternativa aislada para instalar CLIs Python | [pipx docs](https://pipx.pypa.io/) | [Install pipx](https://pipx.pypa.io/stable/how-to/install-pipx/) |

## IDEs / agentes de IA compatibles

| Superficie | Cuándo elegirla | README / home oficial | Instalación / getting started |
|---|---|---|---|
| Claude Code | Ruta principal del evento | [Claude Code product](https://www.claude.com/product/claude-code) | [Claude Code docs](https://code.claude.com/docs/en/overview) |
| OpenAI Codex | Si trabajas desde Codex CLI/Desktop | [GitHub: openai/codex](https://github.com/openai/codex) | [Codex CLI getting started](https://help.openai.com/en/articles/11096431) |
| GitHub Copilot | Si trabajas en VS Code con Copilot Chat/Agent | [GitHub Copilot](https://github.com/features/copilot) | [GitHub Copilot docs](https://docs.github.com/en/copilot) |
| Cursor | Si usas Cursor Agent / Cursor CLI | [Cursor docs](https://docs.cursor.com/) | [Cursor CLI installation](https://docs.cursor.com/en/cli/installation) |
| OpenCode | Si prefieres agente open-source por terminal | [OpenCode docs](https://dev.opencode.ai/docs/) | [OpenCode CLI docs](https://dev.opencode.ai/docs/cli/) |
| Antigravity | Si usas el IDE agéntico de Google | [Antigravity](https://antigravity.google/) | [Antigravity download](https://antigravity.google/download) |

## Herramientas opcionales

| Herramienta | Para qué sirve | README / home oficial | Instalación oficial |
|---|---|---|---|
| Engram | Memoria persistente para agentes vía MCP | [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram#readme) | [docs/INSTALLATION.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md) · [docs/AGENT-SETUP.md](https://github.com/Gentleman-Programming/engram/blob/main/docs/AGENT-SETUP.md) |
| RTK | Reescritura/compresión de comandos antes de que lleguen al modelo | [rtk-ai/rtk](https://github.com/rtk-ai/rtk#readme) | [INSTALL.md](https://github.com/rtk-ai/rtk/blob/master/INSTALL.md) |
| Context7 | Docs actuales de librerías y SDKs vía MCP | [Context7 docs](https://context7.com/docs) | [Context7 installation](https://context7.com/docs/installation) · [npm: ctx7](https://www.npmjs.com/package/ctx7) |
| AgentsView | Visor local de sesiones e historial de agentes | [agentsview.io](https://www.agentsview.io/) · [GitHub: wesm/agentsview](https://github.com/wesm/agentsview) | [Quick Start](https://www.agentsview.io/quickstart/) · [GitHub Releases](https://github.com/wesm/agentsview/releases) |

## Herramientas avanzadas no incluidas en la ruta del pre-evento

| Herramienta | Por qué no está en la ruta copy/paste | Fuente oficial |
|---|---|---|
| Squeezr | Requiere proxy local, confianza de CA y/o variables `HTTPS_PROXY`; es útil para usuarios avanzados, pero demasiado fácil de romper en una audiencia cross-OS. | [GitHub: sergioramosv/Squeezr](https://github.com/sergioramosv/Squeezr#readme) · [npm: squeezr-ai](https://www.npmjs.com/package/squeezr-ai) |

## Regla de seguridad para instalaciones

Instala solo desde los dominios anteriores o desde los repositorios enlazados ahí. Evita clones, mirrors, instaladores “early access” o scripts encontrados en buscadores si no aparecen en la documentación oficial.

