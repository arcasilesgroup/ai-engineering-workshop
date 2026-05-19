# Step 4 — Construye

> **Time budget:** 10 minutes • **Skill:** `/ai-build`

## The command

```text
/ai-build
```

## Qué debe pasar

El agente debe ejecutar el plan, marcar tareas y correr los checks razonables para tu proyecto.

## Qué mirar

- Cambios pequeños y relacionados con el spec.
- Tests/checks ejecutados, si existen.
- Nada de cambios sorpresa fuera del scope.

Comprueba en terminal:

```bash
git status
git diff --stat
```

## Next

→ [Step 5 — Prepara commit/PR con `/ai-pr`](05-pr.md)
