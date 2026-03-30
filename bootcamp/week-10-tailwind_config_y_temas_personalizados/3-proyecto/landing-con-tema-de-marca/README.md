# Proyecto Semana 10 — Landing con Tema de Marca

## 🎯 Objetivo

Construir una **landing page completa** aplicando un sistema de diseño propio:
paleta de marca, tipografías custom, design tokens con CSS variables y utilidades personalizadas con `@layer`.

Esta landing integra **todo lo aprendido en la semana**: no es un ejercicio guiado, sino tu primer proyecto de UI con identidad visual propia.

---

## 📋 Descripción

Diseña y construye una landing page ficticia para un producto digital (app, SaaS, curso, herramienta) completamente branded. La identidad visual debe ser consistente: cada color, fuente y espaciado debe venir de tu configuración de Tailwind.

---

## 🗂️ Estructura de Archivos

```
landing-con-tema-de-marca/
├── README.md          ← estás aquí
└── starter/
    └── index.html     ← tu punto de partida
```

---

## ✅ Requisitos Técnicos

### Configuración (obligatorio)

| Requisito | Descripcion |
|-----------|-------------|
| `tailwind.config` | Definido en un `<script>` antes de `</head>` (CDN) |
| Paleta `brand-*` | Mínimo 7 tonos (50, 100, 300, 500, 600, 700, 900) |
| Fuentes custom | 2 fuentes de Google Fonts: `font-display` y `font-body` |
| Tamaños semánticos | Al menos `fontSize.hero` y `fontSize.caption` en config |
| Spacing semántico | Al menos `py-section` y `px-gutter` funcionales |
| CSS variables | Mínimo 6 tokens en `:root` (colors + bg + surface + text) |
| Dark mode tokens | La misma UI se ve correctamente en modo oscuro |
| `@layer utilities` | Al menos 1 utilidad custom (ej: `.text-gradient-brand`) |
| `@layer components` | Al menos 1 componente (ej: `.btn-brand`) con `@apply` |

### Secciones de la landing (obligatorio)

- **Navbar**: logo + links + CTA button usando `.btn-brand`
- **Hero**: heading con `text-hero`, subheading, CTAs, badge decorativo
- **Features**: grid con mínimo 3 features cards (usa breakpoints `xs`/`sm`/`lg`)
- **CTA section**: llamada a acción con fondo de color de marca
- **Footer**: links, copyright, con branding coherente

### Responsive (obligatorio)

- Mobile-first: funciona en 375px
- Usar breakpoints `xs`, `sm`, `md`, `lg` según necesidad

---

## 🎨 Guía de Identidad Visual

### ¿Cuál paleta uso?

Elige **una** de estas opciones como base, o crea la tuya propia:

| Opción | Tono central | Hex 500 |
|--------|-------------|---------|
| Fuchsia | violeta intenso | `#d946ef` |
| Sky | azul cielo | `#0ea5e9` |
| Emerald | verde esmeralda | `#10b981` |
| Orange | naranja vivo | `#f97316` |
| Rose | rosa intenso | `#f43f5e` |

> Para generar una paleta completa (50→950): [uicolors.app](https://uicolors.app) o [palettte.app](https://palettte.app)

### Fuentes recomendadas (Google Fonts)

| Rol | Fuentes Recomendadas |
|-----|---------------------|
| `font-display` | Plus Jakarta Sans, Sora, DM Sans, Cabinet Grotesk |
| `font-body` | Inter, Geist, IBM Plex Sans, Source Sans 3 |

### Tokens mínimos recomendados

```css
:root {
  --color-primary:        /* tu brand-500 */;
  --color-primary-hover:  /* tu brand-600 */;
  --color-primary-subtle: /* tu brand-50 o brand-950 */;
  --color-bg:             /* white o gray-50 */;
  --color-surface:        /* white */;
  --color-border:         /* gray-200 */;
  --color-text:           /* gray-900 */;
  --color-text-subtle:    /* gray-500 */;
}
```

---

## 📊 Criterios de Evaluación

### Conocimiento (30%)
- ¿Entiende la diferencia entre `theme` y `theme.extend`?
- ¿Sabe cuándo usar `@apply` y cuándo no?
- ¿Comprende la jerarquía primitivos → semánticos → componentes?

### Desempeño (40%)
- La configuración de Tailwind está completa y sin errores
- Los tokens CSS se aplican correctamente en el HTML
- Responsive funciona sin romper el layout

### Producto (30%)
- La landing tiene identidad visual consistente de principio a fin
- Los colores de marca se usan con criterio (no todos los tonos mezclados)
- La UI es legible y accesible (contraste mínimo AA)

---

## 🚀 Cómo Empezar

1. Abre `starter/index.html` en tu editor
2. Revisa los TODOs de cada sección
3. Define primero tu paleta en `tailwind.config` y verifica los swatches
4. Configura tus fuentes e importa de Google Fonts
5. Crea tus tokens CSS en `<style>`
6. Define tus clases en `@layer components` y `@layer utilities`
7. Construye las secciones de arriba a abajo
8. Ajusta el responsive con DevTools en modo móvil

---

## 💡 Pistas y Recursos

- Para la paleta: [uicolors.app](https://uicolors.app) — ingresa un hex y genera los 11 tonos
- Para fuentes: [fonts.google.com](https://fonts.google.com) — filtra por "Display" y "Sans Serif"
- Para referencia de config: [tailwindcss.com/docs/theme](https://tailwindcss.com/docs/theme)
- Para @layer: [tailwindcss.com/docs/adding-custom-styles](https://tailwindcss.com/docs/adding-custom-styles)

---

## 🔗 Navegación

← [Ejercicio 04 — Tema Completo](../../2-practicas/04-ejercicio-tema-completo/README.md)
→ [Semana 11 — Plugins, Animaciones y Dark Mode](../../week-11-plugins_animaciones_y_dark_mode/README.md)
