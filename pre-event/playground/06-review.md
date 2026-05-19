# Step 6 — Revisa

> **Time budget:** 5 minutes • **Skill:** `/ai-review`

## The command

Para revisar el diff local:

```text
/ai-review
```

Si quieres acotar a un archivo concreto:

```text
/ai-review --files <path/to/file>
```

## Qué debe producir

Una revisión con findings accionables:

- Blockers.
- Warnings.
- Sugerencias.
- Qué validar antes de considerar el cambio listo.

## Regla

No aceptes sugerencias grandes durante el playground. Si aparece una idea grande, conviértela en futuro spec.

## Next

→ [Step 7 — Entiende lo cambiado con `/ai-explain`](07-explain.md)
