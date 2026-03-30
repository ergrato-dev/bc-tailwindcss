# Ejercicio 04 — Tema Completo

## 🎯 Objetivo

Crear una configuración de Tailwind completa integrando todos los conceptos de la semana: paleta de colores, tipografía, spacing semántico, breakpoints custom y utilidades personalizadas con `@layer utilities`.

---

## 📋 ¿Qué vas a construir?

Un mini design system completo con config integrada aplicada a una landing page básica:
- Paleta `brand-*` (9 tonos) + `accent-*` (5 tonos) en `theme.extend`
- 2 fuentes registradas: `font-display` y `font-body`
- Spacing semántico: `section-sm / section / section-lg`
- Breakpoint extra: `xs: 375px`
- 2 utilidades custom en `@layer utilities`: `.text-gradient-brand` y `.card-hover`
- 1 componente en `@layer components`: `.btn-brand`
- La landing usa SOLO clases del design system definido

---

## 🗂️ Estructura

```
04-ejercicio-tema-completo/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados** de forma progresiva:

### BLOQUE 1 — Config completa integrada

Activa el `tailwind.config` completo con colores, fuentes, spacing, breakpoints y darkMode.

**Conceptos a observar:**
- El objeto config en CDN puede ser tan complejo como un `tailwind.config.js` real
- `theme.extend.spacing` agrega sin reemplazar el spacing default
- `theme.extend.screens` agrega `xs: '375px'` para móviles muy pequeños
- `darkMode: 'class'` habilita el modo oscuro por clase en Tailwind CDN

**Descomenta** el `<script>tailwind.config = {...}</script>` completo.

---

### BLOQUE 2 — @layer utilities y @layer components en CDN

Activa las utilidades y componentes custom declarados en el `<style>` del HTML.

**Conceptos a observar:**
- En CDN se puede usar `@layer utilities {}` y `@layer components {}` dentro de un `<style type="text/tailwindcss">`
- `.text-gradient-brand` combina `background-clip: text` con el degradé de la paleta
- `.card-hover` encapsula la transición de sombra al hacer hover en una card
- `.btn-brand` usa `@apply` con clases de la paleta brand

**Descomenta** el `<style type="text/tailwindcss">` completo.

---

### BLOQUE 3 — Hero section con design system

Construye el hero de la landing usando exclusivamente clases del design system definido.

**Conceptos a observar:**
- `py-section-lg` usa el spacing semántico definido (no `py-32`)
- `font-display text-hero` usa la fuente y tamaño semánticos
- `text-gradient-brand` usa la utilidad custom — la clase se comporta como nativa
- `btn-brand` — el componente custom limpia el HTML
- `bg-brand-50 dark:bg-brand-950` — el tema oscuro usa los extremos de la paleta

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Cards section y responsive

Construye la sección de features/cards con el grid responsive y `card-hover`.

**Conceptos a observar:**
- `xs:grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` — usa el breakpoint `xs` custom
- `card-hover` — la utilidad custom hace hover sin escribir varias clases
- Los colores de los iconos usan `brand-*` y `accent-*` alternados
- Todo el diseño es coherente: mismas fuentes, mismos radii, misma paleta

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de Éxito

Al terminar deberías poder:
- [ ] Usar `bg-brand-500`, `text-brand-50`, `border-accent-300` como clases normales
- [ ] `font-display` y `font-body` muestran fuentes visualmente diferentes
- [ ] `py-section` aplica un padding vertical de 6rem (visible en DevTools)
- [ ] `text-gradient-brand` muestra texto con gradiente de la paleta
- [ ] El layout es responsive desde 375px (xs) hasta 1280px+
- [ ] El dark mode toggle cambia la apariencia de toda la landing

---

## 💡 Ayuda

En Tailwind CDN, para usar `@layer utilities` y `@apply`, el `<style>` debe tener `type="text/tailwindcss"` en lugar del tipo estándar. Esto le indica a Tailwind que procese ese bloque de estilos con su pipeline (incluidos `@apply`, `@layer`, etc.).
