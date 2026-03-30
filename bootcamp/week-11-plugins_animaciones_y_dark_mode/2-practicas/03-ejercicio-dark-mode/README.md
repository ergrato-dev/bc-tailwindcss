# Ejercicio 03 — Dark Mode con Toggle

## 🎯 Objetivo

Implementar dark mode completo con la estrategia `class` de Tailwind: configurar el toggle de JavaScript, aplicar la variante `dark:` en todos los elementos, persistir la preferencia en `localStorage` y detectar la preferencia del sistema operativo en la primera carga.

---

## 🛠️ Qué vas a construir

Una UI completa con toggle de dark mode funcional en cuatro etapas:
1. Configuración básica de `darkMode: 'class'` y toggle simple
2. Layout completo con variantes `dark:` en todos los componentes
3. Toggle persistente con `localStorage` y fallback a `prefers-color-scheme`
4. Dark mode con CSS variables (tokens semánticos)

---

## 📁 Estructura

```
03-ejercicio-dark-mode/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

Abre `starter/index.html` y descomenta cada bloque en orden.

---

### 🔵 BLOQUE 1 — `darkMode: 'class'` y toggle básico

**Concepto**: Con la estrategia `class`, Tailwind aplica la variante `dark:` cuando el elemento `<html>` tiene la clase `dark`. Un JS mínimo puede toglear esto.

```html
<script>
  tailwind.config = { darkMode: 'class' }
</script>

<!-- Fondo y texto con variante dark: -->
<body class="bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100">

<!-- Toggle básico -->
<button onclick="document.documentElement.classList.toggle('dark')">
  Toggle
</button>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — UI completa con variantes `dark:`

**Concepto**: Cada elemento de UI necesita su variante `dark:`. Se establece siempre en el orden: primero el valor para modo claro, luego el valor para modo oscuro.

Componentes con sus variantes:

```html
<!-- Navbar -->
<header class="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700">

<!-- Card -->
<div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl">

<!-- Badge -->
<span class="bg-sky-100 dark:bg-sky-900/30 text-sky-700 dark:text-sky-400">

<!-- Input -->
<input class="bg-white dark:bg-gray-800 border-gray-300 dark:border-gray-600
              text-gray-900 dark:text-gray-100">

<!-- Texto secundario -->
<p class="text-gray-600 dark:text-gray-400">
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — `localStorage` y `prefers-color-scheme`

**Concepto**: El toggle debe persistir entre sesiones (localStorage) y detectar la preferencia del SO en la primera visita.

```javascript
// Inicializar al cargar
function initTheme() {
  const stored = localStorage.getItem('theme')
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
  if (stored === 'dark' || (!stored && prefersDark)) {
    document.documentElement.classList.add('dark')
  }
}

// Toggle con persistencia
function toggleTheme() {
  const isDark = document.documentElement.classList.toggle('dark')
  localStorage.setItem('theme', isDark ? 'dark' : 'light')
  // Actualizar ícono del botón
  document.getElementById('theme-icon').textContent = isDark ? '☀️' : '🌙'
}
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3.

---

### 🔵 BLOQUE 4 — Dark mode con CSS Variables

**Concepto**: Usar CSS variables como tokens semánticos que cambian con `.dark`. Esto reduce la cantidad de clases `dark:` necesarias en el HTML.

```html
<style>
  :root {
    --color-bg:      #f9fafb;
    --color-surface: #ffffff;
    --color-text:    #111827;
    --color-border:  #e5e7eb;
    --color-accent:  #0ea5e9;
  }
  .dark {
    --color-bg:      #030712;
    --color-surface: #111827;
    --color-text:    #f9fafb;
    --color-border:  #374151;
    --color-accent:  #38bdf8;
  }
</style>

<!-- Elemento que usa los tokens en lugar de dark: individuales -->
<div style="background: var(--color-surface);
            color: var(--color-text);
            border-color: var(--color-border)">
  Se adapta automáticamente
</div>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Criterios de Verificación

- [ ] Al hacer click en el toggle, el fondo del body cambia entre claro y oscuro
- [ ] Al recargar la página, el modo seleccionado se mantiene
- [ ] En sistema con dark mode activado (sin haber visitado la página antes), carga en modo oscuro
- [ ] Los textos segundarios son legibles en ambos modos (contraste ≥4.5:1)
- [ ] El ícono del toggle cambia entre ☀️ y 🌙 según el modo activo
- [ ] Los elementos del BLOQUE 4 se adaptan al dark mode sin necesitar `dark:` en el HTML
