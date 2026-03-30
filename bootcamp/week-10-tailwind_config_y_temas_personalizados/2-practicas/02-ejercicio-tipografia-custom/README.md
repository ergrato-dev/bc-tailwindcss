# Ejercicio 02 — Tipografía Custom

## 🎯 Objetivo

Registrar fuentes de Google Fonts en la configuración de Tailwind y crear una escala tipográfica extendida con tamaños semánticos propios.

---

## 📋 ¿Qué vas a construir?

Un sistema de tipografía personalizado integrado con Tailwind:
- 2 fuentes de Google Fonts (`Plus Jakarta Sans` para display, `Inter` para body)
- Ambas registradas como `font-display` y `font-body` respectivamente
- Escala extendida con tamaños semánticos: `text-hero`, `text-caption`, `text-label`
- Página de muestra tipográfica (type specimen) que demuestra la jerarquía

---

## 🗂️ Estructura

```
02-ejercicio-tipografia-custom/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados** de forma progresiva:

### BLOQUE 1 — Registrar fuentes en la config CDN

Configura el `tailwind.config` con las dos fuentes y activa el `@import` de Google Fonts.

**Conceptos a observar:**
- `fontFamily.display: ['"Plus Jakarta Sans"', 'Inter', 'sans-serif']`
- Los nombres de fuente con espacios se envuelven en comillas internas dobles
- La lista de `fontFamily` es un fallback: si la primera falla, usa la siguiente
- El `@import url(...)` de Google Fonts va en el `<style>` del HTML, antes de que Tailwind lo procese

**Descomenta** el `<script>tailwind.config = {...}</script>` con la config completa.

---

### BLOQUE 2 — Escala de tamaños custom (`text-hero`, `text-caption`)

Agrega a la config los tamaños de fuente semánticos y verifica que el HTML los usa.

**Conceptos a observar:**
- `fontSize.hero: ['3.5rem', { lineHeight: '1.1', fontWeight: '700' }]`
- Los tamaños custom reciben `[size, { lineHeight, fontWeight, letterSpacing }]`
- Esto evita tener que poner `text-5xl leading-tight font-bold` cada vez
- `text-caption: ['0.6875rem', ...]` — más pequeño que `text-xs` (0.75rem)

**Descomenta** las líneas del BLOQUE 2.

---

### BLOQUE 3 — Type specimen — la jerarquía visual

Construye la página de muestra completa con todos los niveles tipográficos.

**Conceptos a observar:**
- Contraste entre fuente `font-display` (más geométrica) y `font-body` (más legible)
- `tracking-tight` o `letter-spacing: -0.02em` en headings grandes se ve más moderno
- Los textos pequeños (`text-caption`) necesitan `tracking-wide` para legibilidad
- La jerarquía visual se logra variando: tamaño, peso, color y espaciado

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Modo oscuro con tipografía custom

Aplica el modo oscuro con colores que respeten la jerarquía tipográfica.

**Conceptos a observar:**
- `dark:text-gray-100` para headings en dark mode (no blanco puro — reduce el contraste brutal)
- `dark:text-gray-400` para texto secundario en dark (más claro que en light)
- Las fuentes son las mismas — lo que cambia es color y contraste
- Alternancia con un botón de toggle usando `document.documentElement.classList.toggle('dark')`

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de Éxito

Al terminar deberías poder:
- [ ] Diferenciar visualmente `font-display` (Plus Jakarta Sans) y `font-body` (Inter)
- [ ] El heading principal usa `text-hero` (3.5rem) sin escribir `text-5xl leading-tight`
- [ ] Existe un texto caption más pequeño que `text-xs`
- [ ] El toggle de dark mode cambia los colores y la legibilidad se mantiene
- [ ] Las fuentes cargan desde Google Fonts (verificar en DevTools > Network)

---

## 💡 Ayuda

Si las fuentes no cargan: verifica que el `<style>@import url('...')</style>` esté dentro del `<head>` y que tengas conexión a internet. En proyectos Vite, el `@import` va en el CSS principal. Aquí, al usar CDN, va en un `<style>` inline.
