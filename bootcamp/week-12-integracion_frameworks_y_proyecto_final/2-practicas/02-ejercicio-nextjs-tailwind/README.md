# Ejercicio 02 — Next.js + Tailwind (simulado con estructura App Router)

## 🎯 Objetivo

Comprender la estructura del App Router de Next.js, la diferencia entre Server y Client Components en relación a Tailwind, y practicar el helper `cn()` y el script anti-flash para dark mode.

---

## 🛠️ Qué vas a construir

Una maqueta HTML que simula la estructura de Next.js App Router con cuatro bloques:
1. Estructura de archivos y el Root Layout con `globals.css`
2. Server Component estático con clases Tailwind
3. Client Component con interactividad (toggle dark mode)
4. Fuentes con variable CSS y script anti-flash

> ⚠️ Este ejercicio usa HTML+CDN para que puedas abrirlo directamente en el browser sin instalar Node. En una práctica real harías `create-next-app`. El objetivo es comprender los patrones, no configurar el entorno.

---

## 📁 Estructura

```
02-ejercicio-nextjs-tailwind/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

---

### 🔵 BLOQUE 1 — Root Layout: estructura de archivos

**Concepto**: En Next.js App Router, `app/layout.jsx` envuelve toda la app. Es donde se importa `globals.css`, se configura el `<html>` con `lang` y dark mode, y se aplican clases al `<body>`.

```jsx
// app/layout.jsx (referencia conceptual)
import './globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body className="min-h-screen bg-white dark:bg-gray-950
                       text-gray-900 dark:text-gray-100
                       transition-colors duration-300">
        {children}
      </body>
    </html>
  )
}
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — Server Component

**Concepto**: Los Server Components (el default en App Router) se renderizan en el servidor. Pueden usar Tailwind normalmente pero NO pueden tener `onClick`, `useState` o `useEffect`.

```jsx
// app/page.jsx — Server Component (sin 'use client')
export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center
                     bg-white dark:bg-gray-950 px-4">
      <h1 className="text-5xl md:text-7xl font-bold text-gray-900 dark:text-white">
        Hola, soy <span className="text-sky-500">tu nombre</span>
      </h1>
      <p className="mt-4 text-xl text-gray-600 dark:text-gray-400">
        Frontend Developer · Next.js · Tailwind
      </p>
    </main>
  )
}
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — Client Component con cn()

**Concepto**: Los Client Components necesitan `'use client'` al inicio del archivo. Usan el helper `cn()` para combinar clases Tailwind con lógica JavaScript.

```jsx
'use client'  // ← declare este componente como Client

import { useState } from 'react'
import { cn } from '@/lib/utils'

export function NavLink({ href, isActive, children }) {
  return (
    <a
      href={href}
      className={cn(
        'px-3 py-2 rounded-md text-sm font-medium transition-colors',
        isActive
          ? 'bg-sky-100 text-sky-700 dark:bg-sky-900 dark:text-sky-300'
          : 'text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white',
      )}
    >
      {children}
    </a>
  )
}
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3.

---

### 🔵 BLOQUE 4 — Script anti-flash y fuentes

**Concepto**: El flash de modo claro al recargar se evita con un script inline que corre antes de que React hidrate la página. Las fuentes se configuran con variables CSS.

```html
<!-- Script anti-flash — antes de <head> o en <html> -->
<script>
  if (localStorage.theme === 'dark' ||
      (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark')
  }
</script>
```

```css
/* globals.css — fuente custom como CSS variable */
@theme {
  --font-sans: 'Inter', system-ui, sans-serif;
}
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Checklist de Verificación

- [ ] BLOQUE 1: `<body>` tiene clases `bg-white dark:bg-gray-950 transition-colors`
- [ ] BLOQUE 2: Hero estático renderizado correctamente sin JavaScript
- [ ] BLOQUE 3: Links de navegación cambian de estilo según su estado activo
- [ ] BLOQUE 4: Al recargar la página no hay flash (el dark mode se aplica instantáneamente)
