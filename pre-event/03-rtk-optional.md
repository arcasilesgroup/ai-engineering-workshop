# 3. RTK — ahorro de tokens en comandos (opcional)

> **Tiempo:** ~5 minutos • **Obligatorio:** no

**RTK** reescribe o compacta la salida de comandos antes de que llegue al modelo: `git diff`, `find`, `grep`, `ls`, salidas de tests, etc. No forma parte de `ai-engineering`; es un companion opcional.

- Oficial: <https://github.com/rtk-ai/rtk>
- Instalación oficial: <https://github.com/rtk-ai/rtk/blob/master/INSTALL.md>

## Instalar

macOS / Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh
exec "$SHELL" -l
rtk gain
```

## Activarlo para Claude Code

Ruta global recomendada:

```bash
rtk init -g
rtk init --show
```

Si prefieres que no edite tu `~/.claude/settings.json`, usa:

```bash
rtk init -g --no-patch
```

Y copia manualmente el snippet que te imprime.

## Verificar

Después de una sesión con algunos comandos de shell:

```bash
rtk gain
```

Deberías ver números distintos de cero si RTK está interceptando outputs.

## Por qué ya no incluimos Squeezr en el pre-evento

Squeezr puede ser útil para usuarios avanzados, pero no es una recomendación segura/sencilla para un pre-evento cross-OS:

- instala/configura un proxy local para llamadas LLM;
- requiere confiar una CA local para algunos flujos;
- para Codex usa un proxy MITM en WebSocket hacia `chatgpt.com`;
- la configuración cambia entre CLI, apps GUI, macOS `launchd`, Windows y Linux;
- una mala configuración de `HTTPS_PROXY` puede afectar otras apps o herramientas.

Para evitar que asistentes lleguen al workshop con networking roto o confianza TLS modificada sin entenderlo, lo sacamos de la ruta documentada. Si alguien ya lo usa y entiende el trade-off, que siga la documentación oficial de Squeezr por su cuenta.

## Siguiente

- [4. Context7](04-context7-optional.md)
- [5. AgentsView](05-agentsview-optional.md)
- [Playground pre-evento](playground/)
