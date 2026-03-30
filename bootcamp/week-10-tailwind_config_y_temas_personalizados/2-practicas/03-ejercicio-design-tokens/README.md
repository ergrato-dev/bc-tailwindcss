# Ejercicio 03 — Design Tokens con CSS Variables

## 🎯 Objetivo

Implementar un sistema de design tokens usando CSS custom properties y conectarlos con las clases de Tailwind para crear una UI que soporte cambio de tema claro/oscuro mediante un solo switch.

---

## 📋 ¿Qué vas a construir?

Un sistema de tokens en dos capas (semántico y primitivo) aplicado a una card de usuario:
- Tokens primitivos declarados en CSS: `--primitive-blue-500`, `--primitive-gray-950`
- Tokens semánticos que referencian los primitivos: `--color-primary`, `--color-bg`, etc.
- Card completa que usa tokens a través de clases Tailwind con `bg-[var(--...)]`
- Toggle de tema claro/oscuro que actualiza los tokens en `:root` / `.dark`
- Al cambiar el tema, TODA la card se actualiza sin tocar el HTML

---

## 🗂️ Estructura

```
03-ejercicio-design-tokens/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados** de forma progresiva:

### BLOQUE 1 — Tokens primitivos en CSS

Declara los tokens de color en `:root` sin que tengan significado semántico aún.

**Conceptos a observar:**
- Las variables CSS se declaran con `--nombre-variable: valor;`
- Los "primitivos" son solo valores de color crudos (hex, rgb, hsl)
- Se agrupan por paleta: `--primitive-sky-*`, `--primitive-gray-*`
- Todavía no se usan en el HTML — son la "fuente de verdad" base

**Descomenta** el bloque `<style>` con los primitivos.

---

### BLOQUE 2 — Tokens semánticos y tema oscuro

Declara tokens que usan los primitivos y asígnales un significado de diseño.

**Conceptos a observar:**
- `--color-primary: var(--primitive-sky-500)` — el token semántico apunta al primitivo
- `.dark { --color-bg: var(--primitive-gray-950); }` — en dark solo cambian los semánticos
- Los primitivos nunca cambian; los semánticos sí
- Si cambias un primitivo, todos los semánticos que lo referencian se actualizan

**Descomenta** las líneas del BLOQUE 2.

---

### BLOQUE 3 — Card usando tokens via Tailwind

Construye la card de usuario completa usando los tokens a través de clases con `var()`.

**Conceptos a observar:**
- `bg-[var(--color-surface)]` — clase de Tailwind con valor de token CSS
- `text-[var(--color-text)]` — el color del texto viene del token
- `border-[var(--color-border)]` — el borde también usa token
- El HTML no tiene valores hardcoded de color — todo viene de los tokens

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Toggle de tema y verificación

Agrega el toggle de tema y observa cómo la card completa cambia.

**Conceptos a observar:**
- `document.documentElement.classList.toggle('dark')` — cambia la clase en `<html>`
- Al cambiar a `.dark`, los tokens semánticos toman sus valores dark
- El HTML de la card NO cambia — solo cambian los valores de las variables CSS
- Esto es la ventaja de los tokens: un cambio centralizado, efecto global

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de Éxito

Al terminar deberías poder:
- [ ] Ver claramente la diferencia de apariencia entre tema claro y oscuro
- [ ] El toggle cambia el tema sin recargar la página
- [ ] Todos los elementos de la card (fondo, texto, borde, botón) cambian con el tema
- [ ] El HTML de la card no tiene ningún color hardcoded (sin `bg-gray-900`, solo `bg-[var(--...)]`)
- [ ] Cambiar `--primitive-sky-500` en CSS actualiza todos los elementos primary de la UI

---

## 💡 Ayuda

Si el tema oscuro no funciona: verifica que la clase `.dark` esté en el selector correcto y que tu config de Tailwind tenga `darkMode: 'class'`. En el CDN de Tailwind, esto se hace en el objeto `tailwind.config = { darkMode: 'class' }`.
