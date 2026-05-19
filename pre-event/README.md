# Pre-event setup

> Haz esto antes del workshop, no el mismo día. El objetivo es que el **25 de mayo de 2026** llegues con `ai-eng`, tu IDE y una carpeta de prueba ya verificados.

## Orden recomendado

| # | Paso | Obligatorio | Tiempo |
|---|---|---:|---:|
| 0 | [Enlaces oficiales de herramientas](00-official-tooling-links.md) | Recomendado | 5 min |
| 1 | [Instalar y verificar ai-engineering](01-install-ai-engineering.md) | **Sí** | 15 min |
| 2 | [Engram — memoria entre sesiones](02-engram-optional.md) | No | 5 min |
| 3 | [RTK — ahorro de tokens en comandos](03-rtk-optional.md) | No | 5 min |
| 4 | [Context7 — docs actuales](04-context7-optional.md) | No | 3 min |
| 5 | [AgentsView — visor local de sesiones](05-agentsview-optional.md) | No | 5–10 min |
| 6 | [Playground pre-evento](playground/) | No | 45 min |
| ★ | [Troubleshooting](99-troubleshooting.md) | Referencia | según necesidad |

## Qué necesitas

- macOS, Linux o Windows. `ai-engineering` está pensado para funcionar cross-OS; usa la terminal normal de tu sistema.
- Git y GitHub CLI (`gh auth status` funcionando).
- Un IDE/agente de IA. El evento usará **Claude Code** como ruta principal; también funcionan OpenAI Codex, Gemini CLI, GitHub Copilot, OpenCode, Cursor y Antigravity.
- `uv` para instalar `ai-eng` y las herramientas Python necesarias.
- Una cuenta de GitHub capaz de crear forks y PRs.

## Comprobación de confianza

Después del paso 1, entra en la carpeta donde hayas ejecutado `ai-eng install` y comprueba:

```bash
ai-eng version
ai-eng doctor
```

En tu IDE de IA, abierto dentro de esa misma carpeta:

```text
/ai-start
```

Si todo eso funciona, estás listo para el evento. Los pasos opcionales mejoran la experiencia, pero no bloquean el workshop.

## Playground opcional

[`playground/`](playground/) es una práctica corta para comprobar que `ai-eng`, tu IDE/agente y los comandos básicos funcionan antes del evento.
