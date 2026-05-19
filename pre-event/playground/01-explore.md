# Step 1 — Explora tu carpeta/proyecto

> **Time budget:** 5 minutes • **Skill:** `/ai-explore`

## The command

```text
/ai-explore "Map this project. What files exist, what is implemented, what is missing, and what is safe to change for a tiny first exercise?"
```

## Qué debe producir

Una lectura sin cambios de código:

- Estructura de archivos.
- Qué parece importante.
- Qué riesgos o vacíos hay.
- Ideas de cambios pequeños y seguros.

## Regla

`/ai-explore` no debería modificar archivos. Después puedes comprobar en terminal:

```bash
git status
```

## Next

→ [Step 2 — Define un cambio pequeño con `/ai-brainstorm`](02-brainstorm.md)
