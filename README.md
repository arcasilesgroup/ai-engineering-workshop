# ai-engineering Workshop

> Preparación pública del evento de **ai-engineering**. Hasta el **lunes 25 de mayo de 2026** este repositorio solo debe enseñar el **pre-evento**: instalación, verificación y un playground opcional para llegar con el entorno funcionando.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![ai-engineering](https://img.shields.io/badge/built%20on-ai--engineering-7c3aed.svg)](https://github.com/arcasilesgroup/ai-engineering)

## Estado de publicación

| Fecha | Qué está publicado | Qué no está publicado todavía |
|---|---|---|
| Ahora → 24 mayo 2026 | Pre-evento + playground de práctica | Casos reales del workshop |
| 25 mayo 2026 | Workshop completo con proyectos reales | — |

El directorio [`workshop/`](workshop/) queda como placeholder público hasta el día del evento. Los materiales reales se publicarán el **25 de mayo de 2026**.

## Qué tienes que hacer antes del evento

Completa [`pre-event/`](pre-event/) en orden:

| # | Paso | Tiempo | Obligatorio |
|---|---|---:|---|
| 0 | [Enlaces oficiales de herramientas](pre-event/00-official-tooling-links.md) | 5 min | Recomendado |
| 1 | [Instalar y verificar ai-engineering](pre-event/01-install-ai-engineering.md) | 15 min | **Sí** |
| 2 | [Engram: memoria entre sesiones](pre-event/02-engram-optional.md) | 5 min | Opcional |
| 3 | [RTK: ahorro de tokens en comandos](pre-event/03-rtk-optional.md) | 5 min | Opcional |
| 4 | [Context7: documentación actualizada](pre-event/04-context7-optional.md) | 3 min | Opcional |
| 5 | [AgentsView: visor local de sesiones](pre-event/05-agentsview-optional.md) | 5–10 min | Opcional |
| 6 | [Playground pre-evento](pre-event/playground/) | 45 min | Opcional |
| ★ | [Troubleshooting](pre-event/99-troubleshooting.md) | según necesidad | Referencia |

### Finish line del pre-evento

Desde la carpeta/proyecto donde hayas ejecutado `ai-eng install`, esto tiene que funcionar antes del evento:

```bash
ai-eng version
ai-eng doctor
```

Y en tu IDE de IA, abierto con esa misma carpeta como raíz, el comando:

```text
/ai-start
```

Tiene que mostrar el dashboard de ai-engineering sin errores.

## Por qué hay un playground en el pre-evento

El material que antes estaba en `workshop/` ahora vive en [`pre-event/playground/`](pre-event/playground/). Úsalo para practicar la cadena canónica:

```text
/ai-start → /ai-explore → /ai-brainstorm → /ai-plan → /ai-build → /ai-pr → /ai-review → /ai-explain
```

El workshop real del 25 de mayo no será este playground. Será una sesión con problemas reales de proyecto y un reto final basado en **La Batalla de las IAs**.

## Qué es ai-engineering

[`ai-engineering`](https://github.com/arcasilesgroup/ai-engineering) convierte un repositorio en un workspace gobernado para trabajar con agentes de IA: políticas, skills, agentes, runbooks y specs versionados junto al código. No hay panel SaaS ni lock-in de proveedor. La misma cadena funciona sobre Claude Code, GitHub Copilot, OpenAI Codex, Gemini CLI, OpenCode, Cursor y Antigravity.

## Quién organiza

[Arcasiles Group](https://github.com/arcasilesgroup) — diseñamos experiencias que conectan tecnología, cultura y comunidad. Este workshop es para equipos que quieren usar IA para construir software sin perder control técnico.

## Licencia

[MIT](LICENSE). Puedes forkearlo, adaptarlo y enviar mejoras.
