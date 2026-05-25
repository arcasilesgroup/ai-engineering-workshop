# Arcasiles — Mini guía de marca

Hola 👋

Esto es un extracto de la identidad visual de **Arcasiles** para que puedas usarla libremente en la app que montes durante la Batalla de IA de hoy, si te apetece darle un aire de marca. No es obligatorio — es una caja de herramientas.

> **Lo único que pedimos**: no modifiques el logo, no inventes colores fuera de esta paleta, y si usas el nombre Arcasiles que sea con cariño 🙂

---

## Colores

### Primarios

| Nombre | Hex | Uso |
|---|---|---|
| Arcasiles Yellow | `#f9be4a` | Acento principal: destacados, botones, highlights |
| Arcasiles Dark | `#272727` | Titulares, cuerpo de texto, fondos oscuros |

### Secundarios

| Nombre | Hex | Uso |
|---|---|---|
| Lila | `#674a98` | Badges, etiquetas, bordes, segundo acento |
| Pink-Lila | `#e887a7` | Complemento suave al lila |

### Neutros

| Nombre | Hex | Uso |
|---|---|---|
| Light | `#faf9f7` | Fondo de página |
| White | `#f5f5f5` | Secciones claras |
| Gray | `#e9e9e9` | Bordes y divisores |
| Dark Gray | `#afafaf` | Texto secundario, pies de foto |

### Refuerzo (si los necesitas)

| Nombre | Hex | Uso |
|---|---|---|
| Green | `#7fbf80` | Comunidad, cultura |
| Blue | `#2797c4` | Enlaces, acentos tech |

### Reglas simples

- **Textos**: dark (`#272727`) sobre fondo claro, white (`#f5f5f5`) sobre fondo oscuro.
- **Amarillo nunca como texto sobre blanco** (no se lee). Úsalo como fondo, highlight o sobre dark.
- **Enlaces**: azul `#2797c4`.
- **Jerarquía de acentos**: amarillo primero, lila después. Evita mezclar los dos con la misma fuerza.

---

## Tipografía

Dos familias y nada más:

### BDSupperBold

Para titulares grandes, números y cifras destacadas. Tiene carácter, úsalo con medida. *No la uses para body ni para títulos muy largos.*

Archivo: `BDSupperBold.ttf` (te lo pasamos si lo quieres).

### Lexend

Para todo lo demás: subtítulos, body, labels, navegación, botones. Pesos 300 a 700.

Carga desde Google Fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

Si no puedes cargar fuentes externas, fallback a `Arial` o `sans-serif` del sistema. No uses ninguna otra.

---

## Logos

### Variantes

| Archivo | Cuándo usarlo |
|---|---|
| `Arcasiles_Group_White.svg` | Sobre fondos oscuros o de color sólido (amarillo, lila, dark) |
| `Arcasiles_Group_272727.svg` | Sobre fondos claros |

### Reglas

- No lo recrees con texto — usa el SVG/PNG real.
- No le cambies el color, no lo deformes, no lo pongas en cursiva, no lo gires.
- Deja aire alrededor: mínimo un 20% del ancho del logo por cada lado.

---

## Tono y lenguaje

Si tu app muestra textos, que suenen como Arcasiles:

- **Directo y cercano.** Sin rodeos corporativos.
- **Natural, no robótico.** Si suena a plantilla genérica, reescríbelo.
- **Castellano claro**, sin anglicismos innecesarios ("descargar" antes que "download", "comunidad" antes que "community", "evento" antes que "meetup"). Los términos técnicos que ya están adoptados (IA, login, feed) sí se aceptan.
- **Humano primero.** Arcasiles existe para conectar personas. Si puedes recordárselo al usuario sin ser pesado, mejor.

---

## Ejemplo rápido (CSS)

Si quieres un punto de partida plug-and-play, este bloque te deja la paleta lista:

```css
:root {
  --arc-yellow:     #f9be4a;
  --arc-dark:       #272727;
  --arc-lila:       #674a98;
  --arc-pink-lila:  #e887a7;
  --arc-light:      #faf9f7;
  --arc-white:      #f5f5f5;
  --arc-gray:       #e9e9e9;
  --arc-dark-gray:  #afafaf;
  --arc-blue:       #2797c4;

  --font-display: 'BDSupperBold', 'Arial Black', sans-serif;
  --font-body:    'Lexend', 'Arial', sans-serif;
}

body {
  background: var(--arc-light);
  color: var(--arc-dark);
  font-family: var(--font-body);
}

h1, h2 {
  font-family: var(--font-display);
}

a {
  color: var(--arc-blue);
}

.highlight {
  background: var(--arc-yellow);
  padding: 2px 8px;
  border-radius: 4px;
}

.badge {
  background: var(--arc-lila);
  color: #fff;
  padding: 4px 12px;
  border-radius: 100px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
```

---

## Qué hay y dónde

En la carpeta de Drive del evento tienes:

- Logos (SVG y PNG, variantes blanca y oscura)
- BDSupperBold.ttf
- Banners de los retos A y B
- Este documento

Si necesitas algo más, escribe a `info@arcasiles.com` o directamente a Dachi.

---

**Suerte en la batalla. Que gane el reto que mejor se explique. 🥊**

*Arcasiles × ERNI · Batalla de IA · 23 abril 2026*
