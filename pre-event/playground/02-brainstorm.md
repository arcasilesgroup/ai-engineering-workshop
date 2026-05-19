# Step 2 — Define un cambio pequeño

> **Time budget:** 7 minutes • **Skill:** `/ai-brainstorm`

## The command

Si ya sabes qué quieres cambiar:

```text
/ai-brainstorm "I want to make this small improvement: <describe tu cambio>. Ask me the questions needed to turn it into an approved MVP spec before changing code."
```

Si no sabes qué cambiar:

```text
/ai-brainstorm "Based on the current project, suggest one tiny safe improvement for a first ai-engineering playground. Keep it small and ask me before approving the spec."
```

## Qué debe pasar

El agente debe hacer preguntas antes de escribir código. El resultado esperado es un spec aprobado en `.ai-engineering/specs/`.

## Qué mirar

- Que el objetivo sea pequeño.
- Que haya no-goals.
- Que los criterios de aceptación sean verificables.
- Que no empiece a implementar todavía.

## Next

→ [Step 3 — Planifica con `/ai-plan`](03-plan.md)
