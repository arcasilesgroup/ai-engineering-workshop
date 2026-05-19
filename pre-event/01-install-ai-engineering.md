# 1. Instalar y verificar ai-engineering

> **Tiempo:** ~15 minutos • **Obligatorio:** sí • **Verificado:** macOS + `uv` + PyPI/GitHub el 19 mayo 2026.

`ai-engineering` es el framework del evento. Se instala como un CLI llamado `ai-eng`. Lo instalas una vez en tu máquina y luego lo aplicas a cada proyecto con `ai-eng install`.

Los enlaces oficiales de cada herramienta están en [0. Enlaces oficiales](00-official-tooling-links.md). Esta página es la ruta copy/paste para llegar funcionando.

---

## 1.1 — Instala herramientas base

Elige tu sistema operativo. Si ya tienes una herramienta, el comando la actualizará o la dejará como está.

### macOS

```bash
# 1) Homebrew si no lo tienes: https://brew.sh/
# 2) Git, GitHub CLI y uv
brew install git gh uv

# 3) Login en GitHub para poder crear forks/PRs
gh auth login

# 4) Verificación
git --version
gh auth status
uv --version
```

### Linux — Debian / Ubuntu

```bash
sudo apt update
sudo apt install -y git curl ca-certificates wget

# GitHub CLI: paquete oficial de cli.github.com
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg >/dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
  | sudo tee /etc/apt/sources.list.d/github-cli.list >/dev/null
sudo apt update
sudo apt install -y gh

# uv: instalador oficial de Astral
curl -LsSf https://astral.sh/uv/install.sh | sh
exec "$SHELL" -l

# Login + verificación
gh auth login
git --version
gh auth status
uv --version
```

### Windows — PowerShell

```powershell
winget install --id Git.Git -e
winget install --id GitHub.cli -e
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Cierra y abre PowerShell si uv no aparece todavía.
gh auth login
git --version
gh auth status
uv --version
```

---

## 1.2 — Instala ai-engineering

Tienes dos rutas válidas. Usa **PyPI** si quieres la última release publicada. Usa **GitHub** si quieres la última versión disponible en `main`.

### Opción A — PyPI, última release publicada

macOS / Linux:

```bash
uv tool install --force ai-engineering
uv tool update-shell
exec "$SHELL" -l
```

PowerShell:

```powershell
uv tool install --force ai-engineering
uv tool update-shell
# Cierra y abre PowerShell si ai-eng no aparece todavía.
```

### Opción B — GitHub, última versión de `main`

macOS / Linux:

```bash
uv tool install --force 'git+https://github.com/arcasilesgroup/ai-engineering.git'
uv tool update-shell
exec "$SHELL" -l
```

PowerShell:

```powershell
uv tool install --force "git+https://github.com/arcasilesgroup/ai-engineering.git"
uv tool update-shell
# Cierra y abre PowerShell si ai-eng no aparece todavía.
```

### Verifica

```bash
ai-eng version
```

Salida esperada para el evento:

```text
ai-engineering 0.7.0
```

> Si Dachi indica una ruta concreta para el evento, usa esa.

---

## 1.3 — Instala un IDE/agente de IA

Instala **uno**. La ruta principal del evento será Claude Code.

### Opción A — Claude Code (principal)

macOS / Linux:

```bash
curl -fsSL https://claude.ai/install.sh | bash
exec "$SHELL" -l
claude --version
```

Windows PowerShell:

```powershell
winget install Anthropic.ClaudeCode
claude --version
```

### Opción B — OpenAI Codex

```bash
npm install -g @openai/codex
codex --version
```

### Opción C — Gemini CLI

```bash
npm install -g @google/gemini-cli
gemini --version
```

Si usas Cursor, OpenCode, GitHub Copilot o Antigravity, instala tu herramienta desde los enlaces oficiales de [00-official-tooling-links.md](00-official-tooling-links.md). Luego `ai-eng install` detectará tu entorno o te preguntará qué agente quieres configurar.

---

## 1.4 — Ve a la carpeta donde quieras probar ai-engineering

`ai-eng install` se ejecuta **dentro del proyecto o carpeta que quieras gobernar con ai-engineering**.

No lo ejecutes en este repo de documentación salvo que quieras modificar el workshop. Para practicar, ve a cualquier carpeta de prueba o proyecto propio:

```bash
cd /ruta/a/tu/proyecto-o-carpeta-de-prueba
```

PowerShell:

```powershell
Set-Location "C:/ruta/a/tu/proyecto-o-carpeta-de-prueba"
```

Antes de instalar, confirma dónde estás:

```bash
pwd
```

---

## 1.5 — Ejecuta `ai-eng install`

Dentro de esa carpeta, ejecuta:

```bash
ai-eng install
ai-eng doctor
```

`ai-eng install` detectará tu entorno y preparará el proyecto. Si necesita elegir IDE/agente, sigue el prompt interactivo y selecciona el que vayas a usar.

`ai-eng install` creará, dentro de esa carpeta:

- `.ai-engineering/` — configuración, estado, specs y scripts.
- `.claude/`, `.codex/`, `.gemini/`, etc. — skills/agentes para tu IDE.
- `.git/hooks/` — gates de seguridad y calidad.

Si `doctor` muestra algún error reparable:

```bash
ai-eng doctor --fix
```

---

## 1.6 — Abre tu IDE en esa misma carpeta y prueba `/ai-start`

Los comandos `/ai-start`, `/ai-brainstorm`, `/ai-plan`, etc. se escriben **en el chat de tu IDE/agente de IA**, no en la terminal normal.

Abre tu agente con la misma carpeta donde ejecutaste `ai-eng install`.

Ejemplo con Claude Code:

```bash
cd /ruta/a/tu/proyecto-o-carpeta-de-prueba
claude
```

O abre esa carpeta desde Cursor / Codex / Gemini / OpenCode.

Dentro del chat del agente, ejecuta:

```text
/ai-start
```

El dashboard debe mostrar:

- Rama actual.
- Spec activo: ninguno todavía.
- Estado del plan: ninguno todavía.
- Siguiente acción recomendada.

**Ese es el finish line del pre-evento.** Si `/ai-start` aparece limpio dentro de tu carpeta de prueba, estás listo para el playground.

---

## 1.7 — Primeros pasos para jugar

Con el agente abierto en tu carpeta de prueba, sigue esta secuencia:

```text
/ai-start
/ai-explore "Map this project. What files exist, what is implemented, and what is safe to change?"
/ai-brainstorm "I want to make a small, safe improvement in this project. Help me define an MVP spec before changing code."
/ai-plan
/ai-build
/ai-review
/ai-explain "What changed and why?"
```

## Modelo mental rápido

```text
Tu máquina                         Cada proyecto gobernado
──────────                         ───────────────────────
ai-eng (global)      ───────→      .ai-engineering/   políticas + estado
uv / gh / git                      .claude/ o .codex/ skills + agentes
IDE de IA                          .git/hooks/        gates de seguridad
```

## Siguiente paso

- [Playground pre-evento](playground/) si quieres practicar la cadena completa.
- [Troubleshooting](99-troubleshooting.md) si algo falla.
