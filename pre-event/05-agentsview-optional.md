# 5. AgentsView — visor local de sesiones de agentes (opcional)

> **Tiempo:** ~5–10 minutos • **Obligatorio:** no • **Oficial:** [agentsview.io](https://www.agentsview.io/)

**AgentsView** es una app local-first para explorar, buscar y analizar sesiones pasadas de agentes de coding: Claude Code, Codex, Gemini, Copilot, Cursor, OpenCode y otros. Sirve para ver qué hizo el agente, buscar conversaciones antiguas y consultar uso/coste de tokens.

## Por qué lo usamos

- Ver sesiones de varios agentes en una interfaz común.
- Buscar en historial local por proyecto, agente, fecha o contenido.
- Revisar tool calls, mensajes y resultados después de una sesión.
- Consultar uso de tokens/coste en Claude Code y Codex cuando haya datos disponibles.

> Privacidad: AgentsView lee historiales locales de agentes. Es local-first y usa SQLite por defecto, pero esas sesiones pueden contener prompts, rutas, outputs y secretos pegados accidentalmente. No lo expongas fuera de `localhost` ni actives sync remoto/PostgreSQL durante el pre-evento salvo que entiendas la configuración de acceso.

## Opción A — Desktop app recomendada

Descarga la última release para tu sistema:

- macOS: `.dmg`
- Windows: `.exe`
- Linux: `.AppImage`

Releases: <https://github.com/wesm/agentsview/releases>

La app de escritorio viene empaquetada y arranca sola.

## Opción B — Ejecutarlo con `uvx`

Si ya tienes `uv`, puedes probarlo sin instalación permanente:

```bash
uvx agentsview serve --port 9090
```

Abre:

```text
http://127.0.0.1:9090
```

AgentsView hará un sync inicial de los directorios de sesiones que detecte y luego quedará observando cambios.

## Opción C — Instalar CLI permanentemente

```bash
pip install agentsview
agentsview serve --port 9090
```

Comandos útiles:

```bash
agentsview sync          # sincroniza sesiones y sale
agentsview usage daily   # reporte de uso/coste reciente
agentsview stats         # resumen de base local
```

## Verificar

1. Abre AgentsView.
2. Comprueba que aparecen sesiones de Claude/Codex/Gemini/etc.
3. Si no aparece nada, ejecuta al menos una sesión real de tu agente y luego:
   ```bash
   agentsview sync
   ```
4. Si usas directorios custom, revisa la configuración oficial: <https://www.agentsview.io/configuration/>

## Siguiente

- [Playground pre-evento](playground/)
- [Troubleshooting](99-troubleshooting.md)
