#!/usr/bin/env python3
"""Generate all content files for week-02."""

import os

BASE = "bootcamp/week-02-entorno_y_filosofia_utility_first"

files = {}

# ─────────────────────────────────────────────────────────────────────────────
# RÚBRICA
# ─────────────────────────────────────────────────────────────────────────────
files["rubrica-evaluacion.md"] = '''# 📊 Rúbrica de Evaluación — Semana 2

**Bootcamp TailwindCSS Zero to Hero** | Semana 2: Entorno de Desarrollo y Filosofía Utility-First

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Filosofía Utility-First** | Explica con precisión las ventajas de utility-first vs BEM/CSS modules y cuándo NO usarlo | Entiende el concepto pero no puede argumentar sus ventajas en un contexto real | Confunde utility-first con CSS inline o no comprende su propósito |
| **Instalación Vite + Tailwind** | Explica cada devDependency, el rol de PostCSS y por qué se usa `@import "tailwindcss"` | Sabe los pasos pero no puede explicar qué hace cada uno | No recuerda los comandos de instalación o confunde la configuración |
| **Estructura del Proyecto** | Explica el rol de `vite.config.js`, `postcss.config.js`, `main.css` y cómo Tailwind genera CSS | Conoce los archivos principales pero no sabe cómo interactúan | No sabe dónde va la configuración de Tailwind |
| **JIT y Purging** | Explica qué es JIT, cómo detecta clases usadas y el resultado de `pnpm build` | Sabe que Tailwind elimina clases no usadas pero no sabe cómo | Desconoce el concepto de purging o cree que incluye todo Tailwind |
| **IntelliSense** | Usa IntelliSense correctamente; sabe cómo activarlo y para qué sirve cada sugerencia | Tiene IntelliSense instalado pero no lo usa activamente | No tiene IntelliSense o no lo ha configurado |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Setup del Entorno** | Proyecto Vite + Tailwind v4 creado e iniciado en < 5 min sin errores; HMR funcionando | Proyecto creado pero con algún error menor resuelto con ayuda | No logra levantar el servidor de desarrollo |
| **Utility vs CSS** | Replica el mismo diseño en menos clases Tailwind que propiedades CSS; explica las diferencias | Replica el diseño con Tailwind pero necesita guía para algunas clases | No puede traducir propiedades CSS a clases Tailwind |
| **Primeras Clases** | Usa correctamente: color, bg, padding, margin, text-size, font-weight, rounded, border | Usa la mayoría correctamente; pocos errores de sintaxis (e.g. `p-4` en lugar de `pt-4`) | Más de la mitad de las clases tienen errores o no corresponden |
| **Componente Básico** | Badge/pill con variantes de color usando solo clases Tailwind; código semántico | Badge funcional pero sin variantes o con CSS inline adicional | No logra construir el componente |

---

## 📦 Producto (30%)

**Proyecto: Tarjeta de Perfil**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Setup Correcto** | `@import "tailwindcss"` en main.css; sin `@tailwind base/utilities` legacy | Usa el import correcto pero con archivos de configuración desorganizados | Usa el CDN o la API legacy de Tailwind v3 |
| **Diseño con Tailwind** | Toda la estiización con clases Tailwind; cero CSS personalizado; orden de clases correcto | Principalmente Tailwind; algún estilo inline o CSS externo menor | Mezcla considerable de CSS propio y Tailwind |
| **Responsive** | Se ve bien en mobile y desktop; usa al menos un breakpoint (`md:` o `lg:`) | Funciona en desktop; en mobile hay overflow o elementos rotos | Solo diseñado para un tamaño de pantalla |
| **HTML Semántico** | Usa `article`, `header`, `footer`, `img` con `alt`, `address` o `dl` donde aplica | HTML funcional con algún `div` innecesario | Solo `div`s sin semántica |
| **Calidad Visual** | Diseño equilibrado: espaciado consistente, tipografía legible, jerarquía visual clara | Diseño funcional con alguna inconsistencia de espaciado | Elementos sin espaciado o visualmente desorganizados |

---

## 📈 Cálculo de Calificación

```
Nota final = (Conocimiento × 30%) + (Desempeño × 40%) + (Producto × 30%)
```

**Mínimo para aprobar**: 70% en cada tipo de evidencia.
'''

# ─────────────────────────────────────────────────────────────────────────────
# TEORÍA
# ─────────────────────────────────────────────────────────────────────────────
files["1-teoria/01-filosofia-utility-first.md"] = '''# ⚗️ Filosofía Utility-First

## 🎯 Objetivos

- Entender qué significa "utility-first" y por qué existe
- Comparar utility-first con CSS tradicional, BEM y CSS Modules
- Identificar cuándo utility-first es la mejor elección
- Desmitificar las críticas más comunes

---

## 📋 Contenido

### 1. El Problema que Resuelve

Cuando escribes CSS tradicional, enfrentas estos problemas constantemente:

**Naming fatigue** — ¿Cómo llamo a esta clase?
```css
/* ¿Es .card-header? ¿.product-card__title? ¿.featured-item-heading? */
.????? {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
}
```

**Specificity wars** — Las reglas se pisan entre sí:
```css
.card h2 { color: blue; }
.sidebar .card h2 { color: red; }  /* tengo que ser más específico */
.sidebar .card.featured h2 { color: green; }  /* ...y más... */
```

**CSS crece, nunca decrece** — Una vez que agregas una regla, rara vez la eliminas por miedo a romper algo.

**Context switching** — Vas de HTML → CSS → HTML → CSS constantemente.

---

### 2. Utility-First: El Paradigma

**Utility-first** significa que en lugar de abstraer estilos en componentes CSS con nombres, aplicas clases de propósito único directamente en el HTML:

```html
<!-- CSS tradicional -->
<div class="product-card">
  <h2 class="product-title">Zapatillas Running</h2>
  <p class="product-price">$89.99</p>
</div>
```

```css
.product-card {
  background: white;
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.product-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
}
.product-price {
  font-size: 1.5rem;
  font-weight: 700;
  color: #0369a1;
  margin-top: 0.5rem;
}
```

```html
<!-- Utility-first con Tailwind -->
<div class="rounded-lg bg-white p-6 shadow-sm">
  <h2 class="text-lg font-semibold text-gray-900">Zapatillas Running</h2>
  <p class="mt-2 text-2xl font-bold text-sky-700">$89.99</p>
</div>
```

**¿Qué cambia?**
1. No hay archivo CSS separado que mantener
2. No hay que inventar nombres de clases
3. Cambiar el estilo = cambiar las clases en el HTML
4. Los estilos no tienen scope global → no hay effecto sorpresa

---

### 3. Utility-First vs Otros Enfoques

| Enfoque | Ventajas | Desventajas |
|---------|----------|-------------|
| **CSS Propio** | Total control, CSS mínimo si se hace bien | Naming, especificidad, crece con el tiempo |
| **BEM** | Nomenclatura estructurada, menos conflictos | Verbose, sigue teniendo los mismos problemas de CSS |
| **CSS Modules** | Scope local automático | Requiere bundler, separación HTML/CSS |
| **Utility-First (Tailwind)** | Sin naming, predecible, diseño consistente, IntelliSense | HTML verboso, curva de aprendizaje de clases |
| **CSS-in-JS** | Scope dinámico, variables JS | Runtime overhead, no estándar |

---

### 4. Las Críticas Más Comunes

**"El HTML queda muy largo y feo"**
```html
<!-- Sí, las clases son largas... -->
<button class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-medium text-white hover:bg-sky-600 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50">
  Enviar
</button>
```
Pero: los IDEs con IntelliSense hacen esto manejable. Y si este botón se repite, puedes extraerlo a un componente (React, Vue, etc.) o usar `@apply`.

**"No es diferente a estilos inline"**
No es así. Las clases Tailwind:
- Tienen valores del sistema de diseño (escala consistente)
- Soportan estados (`hover:`, `focus:`, `dark:`, responsive)
- Generan clases CSS reales (no `style=""`)
- Tienen IntelliSense completo

**"El CSS generado es enorme"**
Con JIT (Just-in-Time), Tailwind v4 genera **solo las clases que usas**. Un proyecto real tiene entre 10-50KB de CSS purgeado.

---

### 5. Cuándo Usar (y No Usar) Utility-First

✅ **Ideal para:**
- Proyectos con diseño consistente (design system)
- Equipos donde cada dev escribe sus propios estilos
- Prototipos rápidos
- Sitios con mucha variación de componentes

⚠️ **Considera alternativas cuando:**
- El proyecto tiene muy pocos componentes y CSS simple
- El equipo prefiere CSS arquitectural (ITCSS, etc.)
- Necesitas generar clases dinámicamente en tiempo de ejecución

---

## ✅ Checklist de Verificación

- [ ] Puedo explicar la diferencia entre utility-first y BEM sin mirar notas
- [ ] Entiendo por qué las clases Tailwind no son iguales a estilos inline
- [ ] Conozco al menos 3 ventajas concretas de utility-first
- [ ] Sé cuándo utility-first podría NO ser la mejor opción
'''

files["1-teoria/02-instalacion-vite-tailwind.md"] = '''# ⚙️ Instalación: Vite + TailwindCSS v4

## 🎯 Objetivos

- Crear un proyecto Vite desde cero con pnpm
- Instalar y configurar TailwindCSS v4
- Entender qué hace cada archivo de configuración
- Levantar el servidor de desarrollo con HMR

---

## 📋 Contenido

### 1. Prerequisitos

Antes de continuar, verifica que tienes:

```bash
# Node.js 22+
node --version   # debe mostrar v22.x.x o superior

# pnpm
pnpm --version   # debe mostrar 9.x o superior

# Si no tienes pnpm:
npm install -g pnpm
```

---

### 2. Crear el Proyecto con Vite

```bash
# Crear proyecto vanilla JS con Vite
pnpm create vite@latest mi-proyecto-tailwind -- --template vanilla

# Entrar al directorio
cd mi-proyecto-tailwind

# Instalar dependencias base
pnpm install
```

**`--template vanilla`** crea un proyecto JavaScript puro, sin framework.
Más adelante en el bootcamp usaremos `--template react` para React.

---

### 3. Instalar TailwindCSS v4

TailwindCSS v4 usa el plugin oficial de Vite (no PostCSS separado):

```bash
# Instalar Tailwind + su plugin para Vite
pnpm add -D tailwindcss @tailwindcss/vite
```

- **`tailwindcss`** — El motor de Tailwind (CLI y CSS processing)
- **`@tailwindcss/vite`** — Integración directa con Vite (maneja el build automáticamente)
- **`-D`** — Son devDependencies: solo se necesitan para desarrollo, no en producción

> ⚠️ En v4 **NO necesitas** `postcss` ni `autoprefixer` como paquetes separados. El plugin `@tailwindcss/vite` los maneja internamente.

---

### 4. Configurar Vite

Edita `vite.config.js` para agregar el plugin de Tailwind:

```js
// vite.config.js
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
```

---

### 5. Crear el CSS de Entrada

Tailwind v4 usa una sola directiva en el CSS:

```css
/* src/style.css (o src/main.css) */
@import "tailwindcss";

/* Tus estilos personalizados van aquí, después del import */
```

> 🚀 **Tailwind v4 vs v3**: En v3 necesitabas tres directivas:
> ```css
> /* ❌ API legacy - NO usar en v4 */
> @tailwind base;
> @tailwind components;
> @tailwind utilities;
> ```
> En v4, una sola línea `@import "tailwindcss"` lo hace todo.

---

### 6. Conectar CSS al HTML

En `index.html`, asegúrate de que el CSS ya está importado a través del `main.js`:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="es" class="h-full">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mi Proyecto Tailwind</title>
  </head>
  <body class="h-full bg-gray-50">
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

```js
// src/main.js
import './style.css'  // Importa el CSS (Vite procesa @import "tailwindcss")

document.querySelector('#app').innerHTML = `
  <h1 class="text-4xl font-bold text-sky-500">¡Tailwind v4 funcionando!</h1>
`
```

---

### 7. Levantar el Servidor de Desarrollo

```bash
pnpm dev
```

Abre el browser en `http://localhost:5173` y verás el texto en azul sky.

**HMR (Hot Module Replacement)**: Cada vez que guardas un archivo, el browser se actualiza instantáneamente sin recargar la página completa.

---

### 8. Build de Producción

```bash
pnpm build
```

Genera la carpeta `dist/` con:
- `index.html` — HTML optimizado
- `assets/index-[hash].css` — Solo las clases Tailwind que usas (~10-50KB)
- `assets/index-[hash].js` — JavaScript minificado

---

## 📁 Estructura Final del Proyecto

```
mi-proyecto-tailwind/
├── index.html          ← Punto de entrada HTML
├── package.json        ← Dependencias y scripts
├── pnpm-lock.yaml      ← Lockfile (no editar)
├── vite.config.js      ← Configuración de Vite + Tailwind plugin
├── src/
│   ├── main.js         ← Punto de entrada JS (importa CSS)
│   └── style.css       ← @import "tailwindcss" + estilos custom
└── public/             ← Archivos estáticos (favicons, etc.)
```

---

## ✅ Checklist de Verificación

- [ ] `pnpm dev` levanta el servidor sin errores
- [ ] El browser muestra el texto con clases Tailwind aplicadas
- [ ] IntelliSense autocompleta clases Tailwind en VS Code
- [ ] `pnpm build` genera la carpeta `dist/` con CSS purgado
- [ ] Entiendo para qué sirve cada archivo de configuración
'''

files["1-teoria/03-estructura-proyecto.md"] = '''# 🏗️ Estructura del Proyecto Tailwind + Vite

## 🎯 Objetivos

- Entender qué hace cada archivo de un proyecto Vite + Tailwind
- Saber dónde va cada tipo de código
- Entender el flujo de build: source → bundle → output

---

## 📋 Contenido

### 1. Mapa del Proyecto

```
mi-proyecto/
├── index.html            ← Punto de entrada del browser
├── package.json          ← Metadatos, dependencias, scripts npm
├── pnpm-lock.yaml        ← Versiones exactas de dependencias instaladas
├── vite.config.js        ← Configuración del bundler (plugins, alias, etc.)
├── .gitignore            ← Archivos que Git ignora (node_modules, dist)
│
├── src/                  ← Todo tu código fuente
│   ├── main.js           ← Punto de entrada JavaScript
│   ├── style.css         ← CSS principal (con @import "tailwindcss")
│   └── components/       ← (opcional) HTML/JS de componentes
│
└── public/               ← Archivos estáticos copiados tal cual al build
    └── favicon.ico
```

---

### 2. `index.html` — La Raíz

A diferencia de Webpack, Vite usa `index.html` como punto de entrada real, no como template:

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mi App</title>
    <!-- Vite maneja el CSS automáticamente a través de los imports en JS -->
  </head>
  <body>
    <div id="app"></div>
    <!-- Este script es el punto de entrada: Vite lo procesa -->
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

---

### 3. `package.json` — El Mapa de Dependencias

```json
{
  "name": "mi-proyecto",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",         // pnpm dev → servidor de desarrollo
    "build": "vite build", // pnpm build → bundle de producción
    "preview": "vite preview" // pnpm preview → previsualizar build local
  },
  "devDependencies": {
    "tailwindcss": "^4.0.0",     // Motor de Tailwind
    "@tailwindcss/vite": "^4.0.0", // Plugin Vite para Tailwind
    "vite": "^6.0.0"             // Bundler
  }
}
```

**devDependencies vs dependencies**: Todo en Tailwind es devDependency porque genera CSS en tiempo de build, no en tiempo de ejecución.

---

### 4. `vite.config.js` — El Motor

```js
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),  // Activa el procesamiento de @import "tailwindcss"
  ],
  // Otras opciones útiles:
  // base: '/mi-repo/',        // Si usas GitHub Pages con subdirectorio
  // build: {
  //   outDir: 'dist',         // Carpeta de output (default: 'dist')
  //   assetsDir: 'assets',    // Subcarpeta para assets
  // }
})
```

---

### 5. `src/style.css` — El CSS de Entrada

```css
/* La directiva principal — importa todo Tailwind */
@import "tailwindcss";

/* Aquí van tus estilos personalizados */

/* Ejemplo: var CSS para design tokens */
@theme {
  --color-brand: #0ea5e9;
  --font-display: 'Inter', sans-serif;
}

/* Ejemplo: utilidades custom */
@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}
```

---

### 6. `src/main.js` — El Punto de Entrada JS

```js
// Importar CSS (Vite lo procesa y genera el bundle)
import './style.css'

// Importar componentes
import { setupCounter } from './counter.js'

// Tu aplicación
document.querySelector('#app').innerHTML = `
  <main class="min-h-screen bg-gray-50 py-16">
    <div class="mx-auto max-w-2xl px-4">
      <h1 class="text-4xl font-bold tracking-tight text-gray-900">
        Hola Tailwind
      </h1>
    </div>
  </main>
`
```

---

### 7. El Flujo de Build

```
src/style.css  →  @tailwindcss/vite escanea HTML+JS  →  genera clases usadas
src/main.js    →  Vite bundlea y minifica             →  dist/assets/index.js
index.html     →  Vite procesa imports y hashes       →  dist/index.html
                                                      →  dist/assets/index.css (purgado)
```

**Resultado final en `dist/`:**
- Solo clases Tailwind que aparecen en tu código
- CSS minificado y optimizado
- Listo para subir a servidor o CDN

---

## ✅ Checklist de Verificación

- [ ] Entiendo para qué sirve cada archivo del proyecto
- [ ] Sé dónde agregar nuevos estilos CSS
- [ ] Comprendo la diferencia entre `dev` y `build`
- [ ] Puedo explicar por qué las devDependencies no van a producción
'''

files["1-teoria/04-primeras-clases-utilidad.md"] = '''# 🎨 Primeras Clases de Utilidad

## 🎯 Objetivos

- Dominar las categorías más usadas de clases Tailwind
- Entender el patrón de nomenclatura de las utilidades
- Aplicar texto, colores, fondo, espaciado, tamaño y bordes básicos

---

## 📋 Contenido

### 1. El Patrón de Nomenclatura

Las clases Tailwind siguen un patrón consistente:

```
[variante:]propiedad-valor
```

Ejemplos:
- `text-lg` → font-size: 1.125rem
- `bg-sky-500` → background-color: sky 500
- `p-4` → padding: 1rem (4 × 0.25rem)
- `hover:bg-sky-600` → bg-sky-600 al hacer hover
- `md:text-xl` → text-xl en pantallas ≥ 768px

---

### 2. Tipografía

```html
<!-- Tamaño de texto -->
<p class="text-xs">text-xs — 12px</p>
<p class="text-sm">text-sm — 14px</p>
<p class="text-base">text-base — 16px (default)</p>
<p class="text-lg">text-lg — 18px</p>
<p class="text-xl">text-xl — 20px</p>
<p class="text-2xl">text-2xl — 24px</p>
<p class="text-3xl">text-3xl — 30px</p>
<p class="text-4xl">text-4xl — 36px</p>

<!-- Peso de fuente -->
<p class="font-thin">font-thin — 100</p>
<p class="font-light">font-light — 300</p>
<p class="font-normal">font-normal — 400</p>
<p class="font-medium">font-medium — 500</p>
<p class="font-semibold">font-semibold — 600</p>
<p class="font-bold">font-bold — 700</p>
<p class="font-black">font-black — 900</p>

<!-- Alineación y decoración -->
<p class="text-left">Alineado izquierda</p>
<p class="text-center">Centrado</p>
<p class="text-right">Alineado derecha</p>
<p class="uppercase">MAYÚSCULAS</p>
<p class="lowercase">minúsculas</p>
<p class="capitalize">Capitalizado</p>
<p class="underline">Subrayado</p>
<p class="line-through">Tachado</p>
<p class="italic">Cursiva</p>
<p class="truncate">Texto muy largo que se trunca con elipsis...</p>
```

---

### 3. Colores de Texto y Fondo

Tailwind tiene una paleta de colores con escala del 50 (más claro) al 950 (más oscuro):

```html
<!-- Colores de texto -->
<p class="text-gray-900">Texto casi negro</p>
<p class="text-gray-600">Texto secundario</p>
<p class="text-gray-400">Texto deshabilitado</p>
<p class="text-sky-500">Texto azul cielo</p>
<p class="text-emerald-600">Texto verde esmeralda</p>
<p class="text-red-500">Texto de error</p>
<p class="text-amber-500">Texto de advertencia</p>
<p class="text-white">Texto blanco</p>

<!-- Colores de fondo -->
<div class="bg-white">Fondo blanco</div>
<div class="bg-gray-50">Fondo gris muy claro</div>
<div class="bg-gray-100">Fondo gris claro</div>
<div class="bg-sky-500">Fondo azul cielo</div>
<div class="bg-slate-900">Fondo oscuro</div>

<!-- Combinación texto + fondo -->
<div class="bg-sky-500 text-white">Badge azul con texto blanco</div>
<div class="bg-emerald-100 text-emerald-800">Badge verde</div>
```

---

### 4. Espaciado (Padding y Margin)

La escala de espaciado: cada unidad = 4px (0.25rem).

```html
<!-- Padding (espacio interior) -->
<div class="p-4">p-4 = padding 1rem en todos los lados</div>
<div class="px-4">px-4 = padding horizontal (left + right)</div>
<div class="py-4">py-4 = padding vertical (top + bottom)</div>
<div class="pt-2 pb-6 pl-4 pr-8">Padding individual por lado</div>

<!-- Margin (espacio exterior) -->
<div class="m-4">m-4 = margin en todos los lados</div>
<div class="mx-auto">mx-auto = centrar horizontalmente</div>
<div class="mt-8">mt-8 = margin-top 2rem</div>
<div class="mb-4">mb-4 = margin-bottom 1rem</div>

<!-- Espaciado entre hijos -->
<ul class="space-y-2">
  <li>Elemento 1</li>  <!-- gap vertical de 0.5rem entre children -->
  <li>Elemento 2</li>
  <li>Elemento 3</li>
</ul>

<!-- Referencia de la escala -->
<!-- 
  0 = 0px       4 = 1rem (16px)   8 = 2rem (32px)
  1 = 0.25rem   5 = 1.25rem       10 = 2.5rem
  2 = 0.5rem    6 = 1.5rem        12 = 3rem
  3 = 0.75rem   7 = 1.75rem       16 = 4rem
-->
```

---

### 5. Bordes y Bordes Redondeados

```html
<!-- Border básico -->
<div class="border">Border 1px solid</div>
<div class="border-2">Border 2px</div>
<div class="border-4">Border 4px</div>

<!-- Color del borde -->
<div class="border border-gray-200">Borde gris claro</div>
<div class="border border-sky-500">Borde azul</div>
<div class="border border-red-300">Borde rojo claro</div>

<!-- Border por lado -->
<div class="border-t">Solo arriba</div>
<div class="border-b">Solo abajo</div>
<div class="border-l-4 border-sky-500">Borde izquierdo azul grueso</div>

<!-- Bordes redondeados -->
<div class="rounded-sm">rounded-sm — 2px</div>
<div class="rounded">rounded — 4px (default)</div>
<div class="rounded-md">rounded-md — 6px</div>
<div class="rounded-lg">rounded-lg — 8px</div>
<div class="rounded-xl">rounded-xl — 12px</div>
<div class="rounded-2xl">rounded-2xl — 16px</div>
<div class="rounded-full">rounded-full — 9999px (círculo/pill)</div>
```

---

### 6. Ancho y Alto

```html
<!-- Ancho fijo -->
<div class="w-8">w-8 = 2rem</div>
<div class="w-16">w-16 = 4rem</div>
<div class="w-32">w-32 = 8rem</div>
<div class="w-64">w-64 = 16rem</div>

<!-- Ancho relativo -->
<div class="w-full">w-full = 100%</div>
<div class="w-1/2">w-1/2 = 50%</div>
<div class="w-1/3">w-1/3 = 33.33%</div>
<div class="w-2/3">w-2/3 = 66.66%</div>

<!-- Ancho viewport y container -->
<div class="w-screen">w-screen = 100vw</div>
<div class="max-w-2xl mx-auto">max-w-2xl + centrado</div>

<!-- Alto -->
<div class="h-8">h-8 = 2rem</div>
<div class="h-screen">h-screen = 100vh</div>
<div class="min-h-screen">min-h-screen = min-height: 100vh</div>
```

---

### 7. Primer Componente Completo

Combinando todo lo anterior:

```html
<!-- Tarjeta de notificación -->
<div class="max-w-sm rounded-xl border border-gray-200 bg-white p-4 shadow-sm">
  <!-- Header de la tarjeta -->
  <div class="flex items-start gap-3">
    <!-- Icono de estado -->
    <span class="mt-0.5 rounded-full bg-emerald-100 p-1">
      <span class="block h-4 w-4 rounded-full bg-emerald-500"></span>
    </span>
    <!-- Contenido -->
    <div>
      <p class="text-sm font-semibold text-gray-900">Pago recibido</p>
      <p class="mt-0.5 text-sm text-gray-500">Tu pago de $89.99 fue procesado.</p>
    </div>
  </div>
  <!-- Acción -->
  <div class="mt-4 text-right">
    <button class="text-sm font-medium text-sky-600 hover:text-sky-700">
      Ver detalles →
    </button>
  </div>
</div>
```

---

## ✅ Checklist de Verificación

- [ ] Puedo aplicar cualquier tamaño de texto y peso de fuente
- [ ] Entiendo el sistema de escalas numéricas de Tailwind (4 = 1rem)
- [ ] Sé aplicar colores de texto y fondo con cualquier tono de la paleta
- [ ] Controlo padding y margin con precisión por lado
- [ ] Puedo crear bordes con ancho, color y radio específicos
- [ ] Construyo un componente completo sin consultar documentación básica
'''

files["1-teoria/05-tailwind-play.md"] = '''# ▶️ Tailwind Play — El Sandbox Online

## 🎯 Objetivos

- Usar Tailwind Play para experimentar sin instalar nada
- Compartir código con compañeros mediante links
- Usar Play como herramienta de debugging y prototipado rápido

---

## 📋 Contenido

### 1. ¿Qué es Tailwind Play?

**Tailwind Play** (`play.tailwindcss.com`) es un editor online que:
- Corre Tailwind completo en el browser en tiempo real
- Permite compartir código con una URL única
- Actualiza el preview al escribir (igual que un editor local)
- Soporta Tailwind v4 y todas sus variantes

Es perfecto para:
- Probar una idea rápido antes de escribirla en tu proyecto
- Reportar bugs o mostrar ejemplos a otros
- Experimentar con clases sin configurar nada

---

### 2. La Interfaz

```
┌─────────────────────────────────────────────────────────┐
│  [HTML]  [Config]                    [Share] [Copy CSS] │
├────────────────────────────┬────────────────────────────┤
│                            │                            │
│   Editor HTML              │   Preview en tiempo real   │
│                            │                            │
│   <div class="...">        │   ┌─────────────────────┐  │
│     ...                    │   │ Tu componente aquí  │  │
│   </div>                   │   └─────────────────────┘  │
│                            │                            │
└────────────────────────────┴────────────────────────────┘
```

- **Panel HTML**: Donde escribes tu HTML con clases Tailwind
- **Panel Config**: Para agregar configuración custom (colores, fuentes)
- **Preview**: Se actualiza en tiempo real
- **Share**: Genera una URL única para compartir tu código

---

### 3. Tu Primer Experimento

Abre [play.tailwindcss.com](https://play.tailwindcss.com) y reemplaza el contenido con:

```html
<div class="min-h-screen bg-slate-900 flex items-center justify-center p-8">
  <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-md w-full">

    <!-- Header de la card -->
    <div class="bg-sky-500 px-6 py-8 text-center">
      <div class="mx-auto h-20 w-20 rounded-full bg-white/20 ring-4 ring-white/30"></div>
      <h2 class="mt-4 text-2xl font-bold text-white">Tu Nombre</h2>
      <p class="mt-1 text-sky-100">Desarrollador Frontend</p>
    </div>

    <!-- Cuerpo de la card -->
    <div class="p-6 space-y-4">

      <!-- Estadísticas -->
      <div class="grid grid-cols-3 gap-4 text-center">
        <div>
          <p class="text-2xl font-bold text-gray-900">42</p>
          <p class="text-xs text-gray-500">Proyectos</p>
        </div>
        <div>
          <p class="text-2xl font-bold text-gray-900">1.2k</p>
          <p class="text-xs text-gray-500">Seguidores</p>
        </div>
        <div>
          <p class="text-2xl font-bold text-gray-900">348</p>
          <p class="text-xs text-gray-500">Siguiendo</p>
        </div>
      </div>

      <!-- Botón -->
      <button class="w-full rounded-lg bg-sky-500 py-2.5 text-sm font-semibold text-white hover:bg-sky-600 transition-colors">
        Seguir
      </button>

    </div>
  </div>
</div>
```

Observa cómo el preview se actualiza con cada cambio.

---

### 4. Experimentar con Variantes

En Play es seguro experimentar. Prueba cambiar:
- `bg-slate-900` por `bg-gray-100` — tema claro
- `bg-sky-500` por `bg-violet-500` — color diferente
- `rounded-2xl` por `rounded-none` — sin bordes redondeados
- Agregar `dark:bg-gray-800` y activar dark mode desde Config

---

### 5. Compartir Código

1. Haz clic en **Share** (esquina superior derecha)
2. Copia la URL generada: `https://play.tailwindcss.com/aBcDeFgH`
3. Comparte en Discord, Slack o con tu instructor

Cada URL preserva exactamente tu código HTML y config.

---

### 6. Limitaciones de Play

Play es estupendo para prototipos rápidos, pero:
- ❌ No tiene IntelliSense completo como VS Code
- ❌ No puedes dividir en múltiples archivos
- ❌ No está disponible offline
- ❌ No se integra con frameworks (React, Vue, etc.)

Para proyectos reales, siempre usa el entorno local con Vite.

---

## ✅ Checklist de Verificación

- [ ] He abierto Tailwind Play y creado un componente básico
- [ ] Experimenté cambiando colores y variantes en tiempo real
- [ ] Compartí un enlace de Play con alguien
- [ ] Entiendo cuándo usar Play vs el entorno local
'''

# ─────────────────────────────────────────────────────────────────────────────
# EJERCICIOS
# ─────────────────────────────────────────────────────────────────────────────
files["2-practicas/01-ejercicio-setup/README.md"] = '''# Ejercicio 01: Setup del Entorno — Vite + TailwindCSS v4

## 🎯 Objetivo

Crear un proyecto Vite + TailwindCSS v4 desde cero, verificar que funciona y entender qué hace cada archivo de configuración.

---

## 🛠️ Configuración

No necesitas clonar nada. Vas a crear el proyecto desde cero.

---

## 📋 Instrucciones

### Paso 1: Crear el Proyecto Vite

Crea un proyecto JavaScript vanilla con Vite:

```bash
pnpm create vite@latest perfil-card -- --template vanilla
cd perfil-card
pnpm install
```

**¿Qué creó Vite?** Observa la estructura:
```
perfil-card/
├── index.html
├── package.json
├── vite.config.js
├── src/
│   ├── counter.js
│   ├── main.js
│   ├── style.css
│   └── javascript.svg
└── public/
    └── vite.svg
```

**Abre `starter/index.html`** — el ejercicio empieza aquí. Descomenta el **bloque 1** para ver la estructura base.

---

### Paso 2: Instalar Tailwind

Sigue las instrucciones comentadas en `starter/index.html` bloque 2.

El comando es:
```bash
pnpm add -D tailwindcss @tailwindcss/vite
```

---

### Paso 3: Configurar vite.config.js

Descomenta el **bloque 3**. Muestra la configuración correcta de `vite.config.js`.

---

### Paso 4: Actualizar el CSS

Descomenta el **bloque 4**. Muestra cómo actualizar `src/style.css` con `@import "tailwindcss"`.

---

### Paso 5: Primera Clase Tailwind

Descomenta el **bloque 5**. Agrega un texto simple con clases Tailwind para verificar que funciona.

Ejecuta `pnpm dev` y verifica en el browser.

---

## ✅ Verificación

El ejercicio está completo cuando:
- `pnpm dev` inicia sin errores en la consola
- El browser muestra el texto con estilos Tailwind aplicados
- IntelliSense autocompleta clases en VS Code al escribir `class="`
- `pnpm build` genera la carpeta `dist/` sin errores
'''

files["2-practicas/01-ejercicio-setup/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 01 — Setup Vite + Tailwind</title>
  </head>
  <body>

    <!-- ============================================ -->
    <!-- BLOQUE 1: Estructura base del proyecto       -->
    <!-- ============================================ -->
    <!-- Este archivo muestra la estructura estándar.  -->
    <!-- Tu proyecto real está en la carpeta que       -->
    <!-- creaste con pnpm create vite@latest           -->
    <!--                                               -->
    <!-- Descomenta las siguientes líneas para ver     -->
    <!-- documentado qué hace cada parte:              -->

    <!-- <div id="info" class="p-8 font-mono text-sm"> -->
    <!--   <h1 class="text-2xl font-bold mb-4">Setup Checklist</h1> -->
    <!--   <p class="mb-2">✅ index.html — Punto de entrada HTML</p> -->
    <!--   <p class="mb-2">✅ vite.config.js — Bundler config</p> -->
    <!--   <p class="mb-2">✅ src/main.js — Punto de entrada JS</p> -->
    <!--   <p class="mb-2">✅ src/style.css — CSS con Tailwind</p>  -->
    <!-- </div>                                                      -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Verificación de instalación        -->
    <!-- ============================================ -->
    <!-- Después de ejecutar: pnpm add -D tailwindcss @tailwindcss/vite -->
    <!-- Tu package.json devDependencies debe tener:  -->
    <!--                                              -->
    <!-- "tailwindcss": "^4.x.x"                      -->
    <!-- "@tailwindcss/vite": "^4.x.x"               -->
    <!-- "vite": "^6.x.x"                            -->
    <!--                                              -->
    <!-- Descomenta para ver la visualización:        -->

    <!-- <div class="mt-6 rounded-lg border border-gray-200 bg-gray-50 p-4"> -->
    <!--   <p class="font-semibold text-gray-700">package.json devDeps:</p> -->
    <!--   <pre class="mt-2 text-xs text-sky-700">                          -->
    <!-- "tailwindcss": "^4.0.0",                                           -->
    <!-- "@tailwindcss/vite": "^4.0.0",                                     -->
    <!-- "vite": "^6.0.0"                                                   -->
    <!--   </pre>                                                            -->
    <!-- </div>                                                              -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: vite.config.js correcto            -->
    <!-- ============================================ -->
    <!-- Este es el contenido que debe tener tu vite.config.js: -->
    <!--                                                          -->
    <!-- import { defineConfig } from 'vite'                      -->
    <!-- import tailwindcss from '@tailwindcss/vite'             -->
    <!--                                                          -->
    <!-- export default defineConfig({                            -->
    <!--   plugins: [ tailwindcss() ],                            -->
    <!-- })                                                        -->
    <!--                                                          -->
    <!-- Descomenta el bloque visual:                             -->

    <!-- <div class="mt-4 rounded-lg border border-emerald-200 bg-emerald-50 p-4"> -->
    <!--   <p class="font-semibold text-emerald-700">vite.config.js ✅</p>         -->
    <!--   <pre class="mt-2 text-xs text-gray-700">                                -->
    <!-- import { defineConfig } from 'vite'                                        -->
    <!-- import tailwindcss from '@tailwindcss/vite'                               -->
    <!--                                                                            -->
    <!-- export default defineConfig({                                             -->
    <!--   plugins: [tailwindcss()],                                               -->
    <!-- })                                                                         -->
    <!--   </pre>                                                                   -->
    <!-- </div>                                                                     -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: src/style.css correcto             -->
    <!-- ============================================ -->
    <!-- Tu src/style.css solo debe tener esta línea:            -->
    <!-- @import "tailwindcss";                                   -->
    <!--                                                          -->
    <!-- ¡Elimina todo el CSS de ejemplo que Vite pone por defecto! -->
    <!-- Luego agrega tus estilos personalizados DESPUÉS del import -->
    <!--                                                          -->
    <!-- Descomenta:                                              -->

    <!-- <div class="mt-4 rounded-lg border border-sky-200 bg-sky-50 p-4"> -->
    <!--   <p class="font-semibold text-sky-700">src/style.css ✅</p>       -->
    <!--   <pre class="mt-2 text-xs text-gray-700">                         -->
    <!-- @import "tailwindcss";                                              -->
    <!--                                                                     -->
    <!-- /* Tus estilos custom aquí */                                       -->
    <!--   </pre>                                                            -->
    <!-- </div>                                                              -->


    <!-- ============================================ -->
    <!-- BLOQUE 5: Primera clase Tailwind funcionando -->
    <!-- ============================================ -->
    <!-- Si ves este texto con estilo, ¡Tailwind funciona! -->
    <!-- Descomenta:                                        -->

    <!-- <div class="mt-8 flex flex-col items-center justify-center gap-4"> -->
    <!--   <div class="rounded-2xl bg-sky-500 px-8 py-4 shadow-lg">        -->
    <!--     <p class="text-2xl font-bold text-white">                      -->
    <!--       ¡Tailwind v4 funcionando! 🚀                                 -->
    <!--     </p>                                                           -->
    <!--   </div>                                                           -->
    <!--   <p class="text-sm text-gray-500">                                -->
    <!--     Si ves este cuadro azul, el setup está completo.               -->
    <!--   </p>                                                             -->
    <!-- </div>                                                             -->

    <script type="module" src="/src/main.js"></script>
  </body>
</html>
'''

files["2-practicas/02-ejercicio-utility-vs-css/README.md"] = '''# Ejercicio 02: Utility-First vs CSS Tradicional

## 🎯 Objetivo

Construir el mismo componente dos veces: una con CSS propio y otra con clases Tailwind. Comparar verbosidad, mantenibilidad y velocidad de desarrollo.

---

## 🛠️ Configuración

Necesitas el proyecto de Vite + Tailwind del ejercicio anterior corriendo con `pnpm dev`.

Copia `starter/index.html` a tu proyecto y ábrelo en el browser.

---

## 📋 Instrucciones

### Paso 1: El diseño objetivo

El componente es una **tarjeta de alerta** con:
- Icono de color (círculo)
- Título en negrita
- Mensaje descriptivo
- Botón de acción

Descomenta el **bloque 1** para ver el diseño objetivo con imagen referencial.

---

### Paso 2: Versión CSS Tradicional

Descomenta el **bloque 2** para ver la versión con CSS propio (`.alert-card`, `.alert-icon`, etc.).

Observa cuántas líneas de CSS requiere.

---

### Paso 3: Versión Tailwind

Descomenta el **bloque 3** para ver la misma tarjeta implementada solo con clases Tailwind.

Observa que **no requiere ningún CSS adicional**.

---

### Paso 4: Comparación

Descomenta el **bloque 4** para ver ambas versiones lado a lado con métricas.

Reflexiona:
- ¿Cuántas líneas de CSS eliminó Tailwind?
- ¿Cuánto tiempo tardaste en entender cada versión?
- ¿Qué es más fácil de modificar?

---

## ✅ Verificación

El ejercicio está completo cuando:
- Ves ambas tarjetas visualmente idénticas en el browser
- Puedes explicar qué clase Tailwind corresponde a cada propiedad CSS
- Modificas el color de una clase en la versión Tailwind sin tocar CSS
'''

files["2-practicas/02-ejercicio-utility-vs-css/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 02 — Utility vs CSS</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body class="min-h-screen bg-gray-100 p-8">

    <h1 class="mb-8 text-2xl font-bold text-gray-900">
      Utility-First vs CSS Tradicional
    </h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Descripción del componente objetivo -->
    <!-- ============================================ -->
    <!-- El target: una tarjeta de alerta de éxito    -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <div class="mb-8 rounded-lg border border-dashed border-gray-300 bg-white p-4"> -->
    <!--   <p class="text-sm text-gray-500 font-medium">Target: Alert Card</p>           -->
    <!--   <p class="mt-1 text-xs text-gray-400">                                        -->
    <!--     Una card con: icono verde + título + mensaje + botón                        -->
    <!--   </p>                                                                          -->
    <!-- </div>                                                                          -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Versión CSS Tradicional            -->
    <!-- ============================================ -->
    <!-- Requiere la clase .alert-card en styles.css  -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-8">                                                             -->
    <!--   <h2 class="mb-3 text-lg font-semibold text-gray-700">CSS Tradicional</h2>      -->
    <!--   <div class="alert-card">                                                         -->
    <!--     <div class="alert-icon-wrapper">                                              -->
    <!--       <span class="alert-icon"></span>                                            -->
    <!--     </div>                                                                        -->
    <!--     <div class="alert-content">                                                   -->
    <!--       <p class="alert-title">Pago procesado exitosamente</p>                     -->
    <!--       <p class="alert-message">Tu orden #1234 fue confirmada y será entregada.</p> -->
    <!--     </div>                                                                        -->
    <!--     <button class="alert-btn">Ver orden</button>                                 -->
    <!--   </div>                                                                          -->
    <!-- </section>                                                                         -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Versión Tailwind                   -->
    <!-- ============================================ -->
    <!-- Exactamente el mismo diseño, cero CSS propio -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-8">                                                                                 -->
    <!--   <h2 class="mb-3 text-lg font-semibold text-gray-700">Tailwind CSS</h2>                             -->
    <!--   <div class="flex items-start gap-4 rounded-xl bg-white p-4 shadow-sm">                             -->
    <!--     <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-emerald-100">    -->
    <!--       <span class="block h-4 w-4 rounded-full bg-emerald-500"></span>                               -->
    <!--     </div>                                                                                            -->
    <!--     <div class="flex-1">                                                                              -->
    <!--       <p class="font-semibold text-gray-900">Pago procesado exitosamente</p>                        -->
    <!--       <p class="mt-0.5 text-sm text-gray-500">Tu orden #1234 fue confirmada y será entregada.</p>   -->
    <!--     </div>                                                                                            -->
    <!--     <button class="shrink-0 rounded-lg border border-gray-200 px-3 py-1.5 text-sm font-medium text-gray-700 hover:bg-gray-50"> -->
    <!--       Ver orden                                                                                       -->
    <!--     </button>                                                                                         -->
    <!--   </div>                                                                                              -->
    <!-- </section>                                                                                            -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Comparación de métricas            -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="rounded-xl border border-gray-200 bg-gray-50 p-6">                -->
    <!--   <h2 class="mb-4 text-lg font-semibold text-gray-700">📊 Comparación</h2>       -->
    <!--   <div class="grid grid-cols-2 gap-4">                                            -->
    <!--     <div class="rounded-lg bg-white p-4 shadow-sm">                              -->
    <!--       <p class="font-medium text-gray-900">CSS Tradicional</p>                   -->
    <!--       <p class="mt-2 text-2xl font-bold text-red-500">~30 líneas CSS</p>         -->
    <!--       <p class="mt-1 text-sm text-gray-500">+ nombres de clases inventados</p>   -->
    <!--       <p class="mt-1 text-sm text-gray-500">+ riesgo de conflictos globales</p>  -->
    <!--     </div>                                                                        -->
    <!--     <div class="rounded-lg bg-white p-4 shadow-sm">                              -->
    <!--       <p class="font-medium text-gray-900">Tailwind</p>                          -->
    <!--       <p class="mt-2 text-2xl font-bold text-emerald-500">0 líneas CSS</p>       -->
    <!--       <p class="mt-1 text-sm text-gray-500">sin nombres de clases propios</p>    -->
    <!--       <p class="mt-1 text-sm text-gray-500">sin riesgo de conflictos</p>         -->
    <!--     </div>                                                                        -->
    <!--   </div>                                                                          -->
    <!-- </section>                                                                        -->

  </body>
</html>
'''

files["2-practicas/02-ejercicio-utility-vs-css/starter/styles.css"] = '''/* CSS para el ejercicio de comparación */

/* ============================================ */
/* BLOQUE 2 CSS: Versión CSS Tradicional        */
/* Descomenta para la versión con CSS propio:   */
/* ============================================ */

/* .alert-card {                                       */
/*   display: flex;                                    */
/*   align-items: flex-start;                          */
/*   gap: 1rem;                                        */
/*   background: white;                                */
/*   border-radius: 0.75rem;                           */
/*   padding: 1rem;                                    */
/*   box-shadow: 0 1px 3px rgba(0,0,0,0.1);           */
/* }                                                   */
/*                                                     */
/* .alert-icon-wrapper {                               */
/*   display: flex;                                    */
/*   align-items: center;                              */
/*   justify-content: center;                          */
/*   width: 2.5rem;                                    */
/*   height: 2.5rem;                                   */
/*   border-radius: 9999px;                            */
/*   background: #d1fae5;                              */
/*   flex-shrink: 0;                                   */
/* }                                                   */
/*                                                     */
/* .alert-icon {                                       */
/*   display: block;                                   */
/*   width: 1rem;                                      */
/*   height: 1rem;                                     */
/*   border-radius: 9999px;                            */
/*   background: #10b981;                              */
/* }                                                   */
/*                                                     */
/* .alert-content {                                    */
/*   flex: 1;                                          */
/* }                                                   */
/*                                                     */
/* .alert-title {                                      */
/*   font-weight: 600;                                 */
/*   color: #111827;                                   */
/*   margin: 0;                                        */
/* }                                                   */
/*                                                     */
/* .alert-message {                                    */
/*   font-size: 0.875rem;                              */
/*   color: #6b7280;                                   */
/*   margin-top: 0.125rem;                             */
/* }                                                   */
/*                                                     */
/* .alert-btn {                                        */
/*   flex-shrink: 0;                                   */
/*   padding: 0.375rem 0.75rem;                        */
/*   font-size: 0.875rem;                              */
/*   font-weight: 500;                                 */
/*   color: #374151;                                   */
/*   border: 1px solid #e5e7eb;                        */
/*   border-radius: 0.5rem;                            */
/*   background: white;                                */
/*   cursor: pointer;                                  */
/* }                                                   */
/*                                                     */
/* .alert-btn:hover {                                  */
/*   background: #f9fafb;                              */
/* }                                                   */
'''

files["2-practicas/03-ejercicio-primeras-clases/README.md"] = '''# Ejercicio 03: Primeras Clases de Utilidad

## 🎯 Objetivo

Practicar las categorías fundamentales de clases Tailwind: tipografía, colores, espaciado, bordes y dimensiones.

---

## 🛠️ Configuración

Necesitas tu proyecto Vite + Tailwind corriendo con `pnpm dev`.

---

## 📋 Instrucciones

Trabaja en `starter/index.html`. Cada sección tiene un título descriptivo y código comentado para descomentar.

### Paso 1: Tipografía

Descomenta el **bloque 1** para practicar tamaños, pesos y alineación de texto.

Observa cómo funcionan las escalas `text-sm`, `text-base`, `text-lg`, etc.

---

### Paso 2: Paleta de Colores

Descomenta el **bloque 2** para ver la paleta completa en acción.

Nota cómo los números del 50 al 950 representan luminosidad.

---

### Paso 3: Espaciado

Descomenta el **bloque 3** para ver el sistema de padding y margin.

Recuerda: 4 = 1rem = 16px.

---

### Paso 4: Bordes y Radios

Descomenta el **bloque 4** para practicar bordes y border-radius.

---

### Paso 5: Dimensiones

Descomenta el **bloque 5** para ver width, height y max-width en acción.

---

## ✅ Verificación

El ejercicio está completo cuando:
- Todos los bloques están descomentados y se ven correctamente
- Puedes adivinar el valor CSS de cualquier clase Tailwind sin consultar documentación
- Construyes un componente propio usando solo las clases aprendidas
'''

files["2-practicas/03-ejercicio-primeras-clases/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 03 — Primeras Clases</title>
  </head>
  <body class="min-h-screen bg-gray-50 p-8">

    <h1 class="mb-10 text-3xl font-bold text-gray-900">
      Catálogo de Clases Fundamentales
    </h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Tipografía                         -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-10">                                                    -->
    <!--   <h2 class="mb-4 border-b pb-2 text-xl font-semibold text-gray-700">    -->
    <!--     1. Tipografía                                                          -->
    <!--   </h2>                                                                   -->
    <!--   <div class="space-y-2 bg-white p-6 rounded-xl">                        -->
    <!--     <p class="text-xs text-gray-500">text-xs = 12px</p>                  -->
    <!--     <p class="text-sm text-gray-500">text-sm = 14px</p>                  -->
    <!--     <p class="text-base text-gray-700">text-base = 16px (default)</p>    -->
    <!--     <p class="text-lg text-gray-700">text-lg = 18px</p>                  -->
    <!--     <p class="text-xl font-medium text-gray-900">text-xl = 20px</p>      -->
    <!--     <p class="text-2xl font-semibold text-gray-900">text-2xl = 24px</p>  -->
    <!--     <p class="text-4xl font-bold text-gray-900">text-4xl = 36px</p>      -->
    <!--     <p class="text-sm italic text-gray-400">font-style: italic</p>       -->
    <!--     <p class="text-sm uppercase tracking-widest text-gray-400">uppercase + tracking-widest</p> -->
    <!--     <p class="text-base font-thin">font-thin — 100</p>                   -->
    <!--     <p class="text-base font-bold">font-bold — 700</p>                   -->
    <!--     <p class="text-base font-black">font-black — 900</p>                 -->
    <!--   </div>                                                                   -->
    <!-- </section>                                                                 -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Paleta de Colores                  -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                        -->
    <!--   <h2 class="mb-4 border-b pb-2 text-xl font-semibold text-gray-700">        -->
    <!--     2. Colores (texto y fondo)                                                 -->
    <!--   </h2>                                                                       -->
    <!--   <div class="grid grid-cols-5 gap-2">                                        -->
    <!--     <div class="rounded-lg bg-sky-100 p-3 text-center text-xs text-sky-700">sky-100</div>   -->
    <!--     <div class="rounded-lg bg-sky-300 p-3 text-center text-xs text-sky-900">sky-300</div>   -->
    <!--     <div class="rounded-lg bg-sky-500 p-3 text-center text-xs text-white">sky-500</div>      -->
    <!--     <div class="rounded-lg bg-sky-700 p-3 text-center text-xs text-white">sky-700</div>      -->
    <!--     <div class="rounded-lg bg-sky-900 p-3 text-center text-xs text-white">sky-900</div>      -->
    <!--     <div class="rounded-lg bg-violet-100 p-3 text-center text-xs text-violet-700">violet-100</div> -->
    <!--     <div class="rounded-lg bg-violet-300 p-3 text-center text-xs text-violet-900">violet-300</div> -->
    <!--     <div class="rounded-lg bg-violet-500 p-3 text-center text-xs text-white">violet-500</div>      -->
    <!--     <div class="rounded-lg bg-violet-700 p-3 text-center text-xs text-white">violet-700</div>      -->
    <!--     <div class="rounded-lg bg-violet-900 p-3 text-center text-xs text-white">violet-900</div>      -->
    <!--     <div class="rounded-lg bg-emerald-100 p-3 text-center text-xs text-emerald-700">emerald-100</div> -->
    <!--     <div class="rounded-lg bg-emerald-300 p-3 text-center text-xs text-emerald-900">emerald-300</div> -->
    <!--     <div class="rounded-lg bg-emerald-500 p-3 text-center text-xs text-white">emerald-500</div>      -->
    <!--     <div class="rounded-lg bg-emerald-700 p-3 text-center text-xs text-white">emerald-700</div>      -->
    <!--     <div class="rounded-lg bg-emerald-900 p-3 text-center text-xs text-white">emerald-900</div>      -->
    <!--   </div>                                                                                               -->
    <!-- </section>                                                                                            -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Espaciado                          -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                           -->
    <!--   <h2 class="mb-4 border-b pb-2 text-xl font-semibold text-gray-700">           -->
    <!--     3. Espaciado — padding y margin                                               -->
    <!--   </h2>                                                                          -->
    <!--   <div class="flex flex-wrap gap-4">                                             -->
    <!--     <div class="bg-sky-100 p-0"><span class="bg-sky-300 block text-xs">p-0 = 0px</span></div>   -->
    <!--     <div class="bg-sky-100 p-1"><span class="bg-sky-300 block text-xs">p-1 = 4px</span></div>   -->
    <!--     <div class="bg-sky-100 p-2"><span class="bg-sky-300 block text-xs">p-2 = 8px</span></div>   -->
    <!--     <div class="bg-sky-100 p-4"><span class="bg-sky-300 block text-xs">p-4 = 16px</span></div>  -->
    <!--     <div class="bg-sky-100 p-6"><span class="bg-sky-300 block text-xs">p-6 = 24px</span></div>  -->
    <!--     <div class="bg-sky-100 p-8"><span class="bg-sky-300 block text-xs">p-8 = 32px</span></div>  -->
    <!--   </div>                                                                                          -->
    <!--   <div class="mt-4 space-y-2">                                                                    -->
    <!--     <p class="bg-emerald-100 px-4 py-1 text-sm">px-4 py-1 = padding horizontal + vertical</p>   -->
    <!--     <p class="bg-emerald-100 pl-8 pr-2 py-1 text-sm">pl-8 pr-2 = distintos por lado</p>         -->
    <!--     <div class="flex gap-4">                                                                       -->
    <!--       <p class="bg-amber-100 mt-4 text-sm">mt-4 (margin-top)</p>                                 -->
    <!--       <p class="bg-amber-100 mb-8 text-sm">mb-8 (margin-bottom)</p>                              -->
    <!--     </div>                                                                                         -->
    <!--   </div>                                                                                           -->
    <!-- </section>                                                                                         -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Bordes y Radios                    -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                             -->
    <!--   <h2 class="mb-4 border-b pb-2 text-xl font-semibold text-gray-700">             -->
    <!--     4. Bordes y border-radius                                                       -->
    <!--   </h2>                                                                            -->
    <!--   <div class="flex flex-wrap gap-4">                                               -->
    <!--     <div class="border p-4 text-xs">border (1px)</div>                            -->
    <!--     <div class="border-2 border-sky-400 p-4 text-xs">border-2 sky-400</div>       -->
    <!--     <div class="border-4 border-violet-500 p-4 text-xs">border-4 violet-500</div> -->
    <!--     <div class="border-l-4 border-emerald-500 bg-emerald-50 p-4 text-xs">border-l-4</div> -->
    <!--   </div>                                                                             -->
    <!--   <div class="mt-4 flex flex-wrap gap-4">                                          -->
    <!--     <div class="bg-sky-500 p-4 text-xs text-white rounded-sm">rounded-sm</div>    -->
    <!--     <div class="bg-sky-500 p-4 text-xs text-white rounded">rounded</div>          -->
    <!--     <div class="bg-sky-500 p-4 text-xs text-white rounded-lg">rounded-lg</div>    -->
    <!--     <div class="bg-sky-500 p-4 text-xs text-white rounded-2xl">rounded-2xl</div>  -->
    <!--     <div class="bg-sky-500 px-4 py-2 text-xs text-white rounded-full">rounded-full</div> -->
    <!--   </div>                                                                             -->
    <!-- </section>                                                                           -->


    <!-- ============================================ -->
    <!-- BLOQUE 5: Dimensiones                        -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                          -->
    <!--   <h2 class="mb-4 border-b pb-2 text-xl font-semibold text-gray-700">          -->
    <!--     5. Dimensiones — w, h, max-w                                                 -->
    <!--   </h2>                                                                         -->
    <!--   <div class="space-y-2">                                                       -->
    <!--     <div class="h-4 bg-sky-200">h-4 = 1rem</div>                               -->
    <!--     <div class="w-1/4 bg-sky-300 p-1 text-xs">w-1/4 = 25%</div>               -->
    <!--     <div class="w-1/2 bg-sky-400 p-1 text-xs text-white">w-1/2 = 50%</div>    -->
    <!--     <div class="w-3/4 bg-sky-500 p-1 text-xs text-white">w-3/4 = 75%</div>    -->
    <!--     <div class="w-full bg-sky-600 p-1 text-xs text-white">w-full = 100%</div>  -->
    <!--     <div class="mx-auto max-w-sm bg-violet-100 p-2 text-center text-xs">       -->
    <!--       max-w-sm mx-auto = contenedor estrecho centrado                           -->
    <!--     </div>                                                                       -->
    <!--   </div>                                                                         -->
    <!-- </section>                                                                       -->

  </body>
</html>
'''

files["2-practicas/04-ejercicio-componente-basico/README.md"] = '''# Ejercicio 04: Componente Básico — Badge y Pill

## 🎯 Objetivo

Construir un sistema de badges, pills y tags reutilizables usando solo clases Tailwind. Primer componente UI completo de la semana.

---

## 🛠️ Configuración

Necesitas tu proyecto Vite + Tailwind corriendo con `pnpm dev`.

---

## 📋 Instrucciones

### Paso 1: Badge Básico

Un badge es un pequeño indicador de estado. Descomenta el **bloque 1** para ver los badges básicos de colores.

---

### Paso 2: Variantes de Tamaño

Descomenta el **bloque 2** para ver cómo escalar el mismo componente con diferentes tamaños.

---

### Paso 3: Badges con Punto de Estado

Descomenta el **bloque 3** para ver badges con un círculo de color indicando estado (activo, inactivo, pendiente).

---

### Paso 4: Pills de Categoría

Descomenta el **bloque 4** para construir pills tipo etiqueta (como los tags de un blog).

---

### Paso 5: Badge con Número

Descomenta el **bloque 5** para crear el clásico badge de notificaciones de un ícono.

---

## ✅ Verificación

El ejercicio está completo cuando:
- Todos los bloques están descomentados y los componentes se ven correctamente
- Puedes crear un nuevo badge de color diferente en < 30 segundos
- Entiendes por qué `rounded-full` crea el efecto pill
'''

files["2-practicas/04-ejercicio-componente-basico/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 04 — Badge y Pill</title>
  </head>
  <body class="min-h-screen bg-slate-100 p-8">

    <h1 class="mb-8 text-2xl font-bold text-gray-900">Sistema de Badges</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Badges básicos de color            -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-8">                                                                         -->
    <!--   <h2 class="mb-3 text-sm font-semibold uppercase tracking-wider text-gray-500">Badges básicos</h2> -->
    <!--   <div class="flex flex-wrap gap-2">                                                            -->
    <!--     <span class="rounded-full bg-sky-100 px-3 py-1 text-xs font-medium text-sky-700">Info</span>     -->
    <!--     <span class="rounded-full bg-emerald-100 px-3 py-1 text-xs font-medium text-emerald-700">Éxito</span> -->
    <!--     <span class="rounded-full bg-amber-100 px-3 py-1 text-xs font-medium text-amber-700">Advertencia</span> -->
    <!--     <span class="rounded-full bg-red-100 px-3 py-1 text-xs font-medium text-red-700">Error</span>    -->
    <!--     <span class="rounded-full bg-violet-100 px-3 py-1 text-xs font-medium text-violet-700">Nuevo</span> -->
    <!--     <span class="rounded-full bg-gray-100 px-3 py-1 text-xs font-medium text-gray-600">Default</span> -->
    <!--   </div>                                                                                         -->
    <!-- </section>                                                                                       -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Variantes sólidas                  -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-8">                                                                          -->
    <!--   <h2 class="mb-3 text-sm font-semibold uppercase tracking-wider text-gray-500">Sólidos</h2>  -->
    <!--   <div class="flex flex-wrap gap-2">                                                            -->
    <!--     <span class="rounded-full bg-sky-500 px-3 py-1 text-xs font-medium text-white">Info</span>     -->
    <!--     <span class="rounded-full bg-emerald-500 px-3 py-1 text-xs font-medium text-white">Éxito</span> -->
    <!--     <span class="rounded-full bg-amber-500 px-3 py-1 text-xs font-medium text-white">Advertencia</span> -->
    <!--     <span class="rounded-full bg-red-500 px-3 py-1 text-xs font-medium text-white">Error</span>    -->
    <!--     <span class="rounded-full bg-violet-500 px-3 py-1 text-xs font-medium text-white">Nuevo</span>  -->
    <!--     <span class="rounded-full bg-gray-700 px-3 py-1 text-xs font-medium text-white">Default</span>  -->
    <!--   </div>                                                                                          -->
    <!-- </section>                                                                                        -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Badges con punto de estado         -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-8">                                                                            -->
    <!--   <h2 class="mb-3 text-sm font-semibold uppercase tracking-wider text-gray-500">Con estado</h2> -->
    <!--   <div class="flex flex-wrap gap-2">                                                              -->
    <!--     <span class="flex items-center gap-1.5 rounded-full bg-emerald-50 px-3 py-1 text-xs font-medium text-emerald-700"> -->
    <!--       <span class="h-1.5 w-1.5 rounded-full bg-emerald-500"></span> Activo                       -->
    <!--     </span>                                                                                        -->
    <!--     <span class="flex items-center gap-1.5 rounded-full bg-red-50 px-3 py-1 text-xs font-medium text-red-700">   -->
    <!--       <span class="h-1.5 w-1.5 rounded-full bg-red-500"></span> Inactivo                         -->
    <!--     </span>                                                                                        -->
    <!--     <span class="flex items-center gap-1.5 rounded-full bg-amber-50 px-3 py-1 text-xs font-medium text-amber-700"> -->
    <!--       <span class="h-1.5 w-1.5 rounded-full bg-amber-500"></span> Pendiente                      -->
    <!--     </span>                                                                                        -->
    <!--   </div>                                                                                           -->
    <!-- </section>                                                                                         -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Pills tipo etiqueta de blog        -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-8">                                                                             -->
    <!--   <h2 class="mb-3 text-sm font-semibold uppercase tracking-wider text-gray-500">Tags de blog</h2> -->
    <!--   <div class="flex flex-wrap gap-2">                                                               -->
    <!--     <a href="#" class="rounded-full border border-gray-200 bg-white px-3 py-1 text-xs font-medium text-gray-600 transition hover:border-sky-300 hover:text-sky-600">TailwindCSS</a> -->
    <!--     <a href="#" class="rounded-full border border-gray-200 bg-white px-3 py-1 text-xs font-medium text-gray-600 transition hover:border-sky-300 hover:text-sky-600">CSS</a>         -->
    <!--     <a href="#" class="rounded-full border border-gray-200 bg-white px-3 py-1 text-xs font-medium text-gray-600 transition hover:border-sky-300 hover:text-sky-600">Frontend</a>    -->
    <!--     <a href="#" class="rounded-full border border-gray-200 bg-white px-3 py-1 text-xs font-medium text-gray-600 transition hover:border-sky-300 hover:text-sky-600">UI Design</a>   -->
    <!--   </div>                                                                                            -->
    <!-- </section>                                                                                         -->


    <!-- ============================================ -->
    <!-- BLOQUE 5: Badge de notificación sobre ícono  -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-8">                                                                                     -->
    <!--   <h2 class="mb-3 text-sm font-semibold uppercase tracking-wider text-gray-500">Notificación</h2>        -->
    <!--   <div class="flex gap-8">                                                                                 -->
    <!--     <div class="relative inline-flex">                                                                     -->
    <!--       <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-gray-200">                     -->
    <!--         <svg class="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">         -->
    <!--           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"                            -->
    <!--             d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /> -->
    <!--         </svg>                                                                                              -->
    <!--       </div>                                                                                               -->
    <!--       <span class="absolute -right-1.5 -top-1.5 flex h-5 w-5 items-center justify-center rounded-full bg-red-500 text-xs font-bold text-white">3</span> -->
    <!--     </div>                                                                                                  -->
    <!--   </div>                                                                                                    -->
    <!-- </section>                                                                                                  -->

  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# PROYECTO
# ─────────────────────────────────────────────────────────────────────────────
files["3-proyecto/tarjeta-de-perfil/README.md"] = '''# Proyecto Semana 2: Tarjeta de Perfil

## 📋 Descripción

Construye una **tarjeta de perfil** estilo GitHub/LinkedIn usando exclusivamente clases TailwindCSS v4 en un proyecto Vite. Este es tu primer proyecto real con Tailwind.

---

## 🎯 Objetivos

- Configurar y usar correctamente Vite + TailwindCSS v4
- Aplicar las clases aprendidas para construir un UI completo
- Diseñar un componente responsive que funcione en mobile y desktop
- Usar HTML semántico con Tailwind

---

## 📐 Diseño Esperado

```
┌─────────────────────────────┐
│    [ Avatar circular ]      │  ← bg-color + rounded-full
│                             │
│    Nombre Completo          │  ← text-xl font-bold
│    @usuario · rol           │  ← text-sm text-gray-500
│                             │
│    Bio corta del usuario    │  ← text-sm text-center
│                             │
│  [ Repos ] [ Stars ] [ PRs ]│  ← grid stats
│                             │
│  [ Siguiente →   ]          │  ← botón de acción
└─────────────────────────────┘
```

---

## 📁 Estructura

```
3-proyecto/tarjeta-de-perfil/
├── README.md
└── starter/
    └── index.html
```

> Nota: No hay `solution/` — es acceso solo para instructores.

---

## 🚀 Instrucciones

### 1. Crear el proyecto

```bash
pnpm create vite@latest tarjeta-perfil -- --template vanilla
cd tarjeta-perfil
pnpm install
pnpm add -D tailwindcss @tailwindcss/vite
```

### 2. Configurar

Actualiza `vite.config.js` y `src/style.css` como aprendiste en la teoría y ejercicios.

### 3. Implementar la tarjeta

Abre `starter/index.html` y completa todos los `<!-- TODO -->`.

### 4. Verificar

```bash
pnpm dev
```

---

## 📋 Requisitos del Proyecto

### HTML Semántico

- [ ] La tarjeta usa `<article>` como elemento contenedor
- [ ] La imagen del avatar tiene `alt` descriptivo
- [ ] Las estadísticas usan `<dl>`, `<dt>`, `<dd>` o elementos semánticos equivalentes

### Tailwind

- [ ] `@import "tailwindcss"` en el CSS (no `@tailwind` legacy)
- [ ] 0 líneas de CSS personalizado (todo con clases Tailwind)
- [ ] Clases en orden: layout → sizing → spacing → typography → colors → effects

### Responsive

- [ ] En mobile (< 640px): tarjeta a ancho completo
- [ ] En desktop (≥ 640px): tarjeta centrada con `max-w-sm`

### Diseño

- [ ] Avatar circular con `rounded-full`
- [ ] Nombre con tipografía prominente
- [ ] Al menos 3 estadísticas numéricas
- [ ] Botón de acción con hover visible

---

## 🎨 Recursos de Inspiración

- [GitHub Profile](https://github.com/) — Para el estilo de las estadísticas
- [Tailwind Play](https://play.tailwindcss.com/) — Para experimentar rápido
'''

files["3-proyecto/tarjeta-de-perfil/starter/index.html"] = '''<!DOCTYPE html>
<!--
  Proyecto Semana 2: Tarjeta de Perfil
  Usa SOLO clases TailwindCSS. Zero CSS personalizado.
  Asegúrate de tener @import "tailwindcss" en tu src/style.css
-->
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tarjeta de Perfil</title>
  </head>
  <body>

    <!-- ============================================ -->
    <!-- TODO: Contenedor de página                   -->
    <!-- Pistas:                                      -->
    <!--   - min-h-screen para ocupar toda la altura  -->
    <!--   - bg-slate-100 o bg-gray-100 de fondo      -->
    <!--   - flex items-center justify-center para    -->
    <!--     centrar la card vertical y horizontal     -->
    <!--   - p-4 o p-8 de padding para mobile         -->
    <!-- ============================================ -->
    <div class="???">


      <!-- ============================================ -->
      <!-- TODO: Tarjeta principal (article semántico)  -->
      <!-- Pistas:                                      -->
      <!--   - max-w-sm w-full para el ancho             -->
      <!--   - bg-white                                  -->
      <!--   - rounded-2xl o rounded-xl                 -->
      <!--   - shadow-md o shadow-lg                     -->
      <!--   - overflow-hidden                           -->
      <!-- ============================================ -->
      <article class="???">


        <!-- ============================================ -->
        <!-- TODO: Sección header de la card             -->
        <!-- (fondo de color con avatar centrado)        -->
        <!-- Pistas:                                      -->
        <!--   - bg-sky-500 (o el color que prefieras)   -->
        <!--   - px-6 pt-8 pb-12 para espaciado           -->
        <!--   - text-center                              -->
        <!-- ============================================ -->
        <div class="???">

          <!-- TODO: Avatar circular                     -->
          <!-- Pistas:                                   -->
          <!--   - mx-auto para centrar                  -->
          <!--   - h-20 w-20 para el tamaño              -->
          <!--   - rounded-full para círculo             -->
          <!--   - ring-4 ring-white/30 borde translúcido -->
          <!--   - bg-white/20 fondo translúcido si no   -->
          <!--     tienes imagen real                    -->
          <div class="???"></div>

          <!-- TODO: Nombre y username                   -->
          <!-- <h1 class="mt-4 text-xl font-bold text-white">...</h1> -->
          <!-- <p class="mt-1 text-sm text-sky-100">@usuario · Desarrollador</p> -->

        </div>


        <!-- ============================================ -->
        <!-- TODO: Cuerpo de la card                      -->
        <!-- Pistas: p-6 para el padding interior         -->
        <!-- ============================================ -->
        <div class="???">

          <!-- TODO: Bio breve                            -->
          <!-- text-sm text-gray-600 text-center          -->
          <!-- -mt-6 relative z-10 para que suba sobre   -->
          <!-- el header de color si usas margin negativo -->
          <p class="???">...</p>


          <!-- TODO: Estadísticas (grid de 3 columnas)   -->
          <!-- Contenedor: grid grid-cols-3 gap-4 my-6   -->
          <!-- Cada stat: text-center                    -->
          <!-- Número: text-xl font-bold text-gray-900   -->
          <!-- Etiqueta: text-xs text-gray-500 mt-0.5    -->
          <div class="???">
            <div class="???">
              <p class="???">12</p>
              <p class="???">Repos</p>
            </div>
            <!-- TODO: Agregar 2 stats más (Stars, PRs) -->
          </div>


          <!-- TODO: Botón de acción                     -->
          <!-- w-full rounded-lg py-2.5                  -->
          <!-- bg-sky-500 hover:bg-sky-600                -->
          <!-- text-sm font-semibold text-white           -->
          <!-- transition-colors                          -->
          <button class="???">
            Seguir
          </button>

        </div>

      </article>

    </div>

    <script type="module" src="/src/main.js"></script>
  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# GLOSARIO
# ─────────────────────────────────────────────────────────────────────────────
files["5-glosario/README.md"] = '''# Glosario — Semana 2: Entorno de Desarrollo y Filosofía Utility-First

Términos técnicos clave de la semana, ordenados alfabéticamente.

---

## B

### Bundle
Archivo(s) final(es) generado(s) por un bundler (como Vite) que combina múltiples módulos de código fuente en uno o pocos archivos optimizados para el navegador. TailwindCSS genera un bundle CSS que solo contiene las clases usadas.

### Bundler
Herramienta que empaqueta módulos JavaScript, CSS y otros assets en archivos optimizados para producción. Vite es el bundler utilizado en este bootcamp.

---

## C

### CDN (Content Delivery Network)
Red de servidores que distribuye archivos estáticos. TailwindCSS tiene un CDN de play (`cdn.tailwindcss.com`), pero **no se recomienda en producción** porque incluye todo Tailwind sin purging.

### CSS-in-JS
Paradigma que escribe CSS usando JavaScript (ej: styled-components). Es una alternativa a utility-first, con pros/contras diferentes.

---

## D

### devDependency
Dependencia de desarrollo listada en `package.json` bajo `devDependencies`. Solo se necesita para el proceso de build, no en el runtime del navegador. `tailwindcss` y `@tailwindcss/vite` son devDependencies porque generan CSS en tiempo de build.

---

## H

### HMR (Hot Module Replacement)
Funcionalidad de Vite que actualiza el navegador automáticamente cuando cambias un archivo, sin recargar la página completa. Mantiene el estado de la aplicación entre cambios.

---

## I

### IntelliSense (Tailwind)
Extensión de VS Code (`Tailwind CSS IntelliSense`) que añade autocompletado, documentación inline y resaltado de errores para clases Tailwind. Esencial para trabajar eficientemente.

---

## J

### JIT (Just-in-Time Compiler)
Motor de Tailwind (activo por defecto desde v3, mejorado en v4) que genera clases CSS bajo demanda mientras detecta qué clases usas en tus archivos. Resultado: CSS final ligerísimo.

---

## P

### pnpm
Gestor de paquetes Node.js alternativo a `npm` y `yarn`. Más rápido y eficiente en espacio de disco gracias al almacenamiento de paquetes como links simbólicos. Es el gestor recomendado en este bootcamp.

### PostCSS
Transformador de CSS usado internamente por TailwindCSS para procesar los imports y directivas. En Tailwind v4 + Vite, el plugin `@tailwindcss/vite` gestiona esto automáticamente.

### Purging
Proceso por el cual Tailwind escanea tus archivos de código y elimina del CSS final todas las clases que no usas. Convierte ~3MB de CSS completo en ~10-50KB. También llamado "tree-shaking" para CSS.

---

## U

### Utility-First
Filosofía de diseño CSS donde se aplican clases de propósito único (utilidades) directamente al HTML en lugar de crear clases de componentes con nombres abstractos. Tailwind es el framework utility-first más usado.

---

## V

### Variante (Tailwind)
Prefijo que condiciona cuándo aplica una clase. Ejemplos: `hover:` (al hacer hover), `md:` (en pantallas ≥ 768px), `dark:` (modo oscuro), `focus:` (al recibir foco). Sintaxis: `variante:clase`.

### Vite
Bundler y servidor de desarrollo extremadamente rápido para proyectos frontend. Usa ES Modules nativos del browser en desarrollo para eliminar el tiempo de bundle, y Rollup para el build de producción.

---

## `@import "tailwindcss"`
La directiva CSS que activa TailwindCSS en tu archivo CSS principal en Tailwind v4. Reemplaza las tres directivas legacy de v3 (`@tailwind base`, `@tailwind components`, `@tailwind utilities`).
'''

# ─────────────────────────────────────────────────────────────────────────────
# RECURSOS
# ─────────────────────────────────────────────────────────────────────────────
files["4-recursos/ebooks-free/README.md"] = '''# Libros y Ebooks Gratuitos — Semana 2

---

## TailwindCSS y Utility-First

### 📘 Refactoring UI (preview gratuito)
- **Autores**: Adam Wathan & Steve Schoger
- **Enlace**: [https://www.refactoringui.com/](https://www.refactoringui.com/)
- **Qué encontrarás**: Los creadores de Tailwind explican principios de diseño UI; capítulos gratuitos disponibles
- **Nivel**: Principiante - Intermedio

### 📘 JavaScript Notes for Professionals
- **Fuente**: GoalKicker.com
- **Enlace**: [https://books.goalkicker.com/JavaScriptBook/](https://books.goalkicker.com/JavaScriptBook/)
- **Qué encontrarás**: Referencia de JavaScript útil para el contexto de Vite y configuraciones
- **Nivel**: Principiante - Avanzado

---

## Herramientas de Build

### 📘 Vite Guide (documentación oficial)
- **Enlace**: [https://vitejs.dev/guide/](https://vitejs.dev/guide/)
- **Qué encontrarás**: Todo sobre Vite: configuración, plugins, build, optimización
- **Nivel**: Principiante - Avanzado
- **Recomendado**: Sección "Why Vite" para entender la filosofía del bundler

---

## Nota

Todos los enlaces son a materiales de libre acceso o documentación oficial.
'''

files["4-recursos/videografia/README.md"] = '''# Videos y Tutoriales — Semana 2

---

## TailwindCSS Setup

### 🎥 Tailwind CSS v4 Full Course
- **Canal**: Tailwind Labs (oficial)
- **Dónde buscar**: YouTube → "Tailwind CSS v4 tutorial"
- **Qué aprenderás**: Instalación completa, configuración, primeras clases
- **Duración estimada**: 1-2 horas

### 🎥 Vite Crash Course
- **Canal**: Traversy Media o Fireship
- **Dónde buscar**: YouTube → "Vite crash course"
- **Qué aprenderás**: Por qué Vite es rápido, configuración, plugins
- **Duración estimada**: 20-30 min

---

## Filosofía Utility-First

### 🎥 "Why I use Tailwind CSS"
- **Dónde buscar**: YouTube → "why tailwind css utility first"
- **Qué aprenderás**: Argumentos reales de desarrolladores que usan Tailwind en producción
- **Duración estimada**: 10-15 min por video

---

## Recomendación de la Semana

> Busca "Tailwind CSS in 100 seconds" de Fireship en YouTube.
> Es un resumen perfecto de 2 minutos de la filosofía.
'''

files["4-recursos/webgrafia/README.md"] = '''# Recursos Web — Semana 2

---

## Documentación Oficial

### TailwindCSS v4
- **Installation**: [https://tailwindcss.com/docs/installation](https://tailwindcss.com/docs/installation)
- **Utility-First Fundamentals**: [https://tailwindcss.com/docs/utility-first](https://tailwindcss.com/docs/utility-first)
- **Editor Setup**: [https://tailwindcss.com/docs/editor-setup](https://tailwindcss.com/docs/editor-setup)

### Vite
- **Getting Started**: [https://vitejs.dev/guide/](https://vitejs.dev/guide/)
- **Why Vite**: [https://vitejs.dev/guide/why.html](https://vitejs.dev/guide/why.html)
- **Configuring Vite**: [https://vitejs.dev/config/](https://vitejs.dev/config/)

### pnpm
- **Documentación**: [https://pnpm.io/](https://pnpm.io/)
- **Installation**: [https://pnpm.io/installation](https://pnpm.io/installation)

---

## Herramientas Online

- **Tailwind Play**: [https://play.tailwindcss.com/](https://play.tailwindcss.com/) — Sandbox sin instalación
- **Tailwind Cheat Sheet**: Busca "Tailwind CSS cheat sheet" en Google para refencia rápida de clases

---

## Artículos Recomendados

- **"Tailwind CSS vs otras soluciones"**: Busca artículos actualizados (2024-2025) que comparen utilility-first con BEM y CSS Modules
- **"The Case for Atomic/Utility-First CSS"**: [https://johnpolacek.github.io/the-case-for-atomic-css/](https://johnpolacek.github.io/the-case-for-atomic-css/)

---

## VS Code

- **Extensión Tailwind CSS IntelliSense**: [https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)
'''

# Write all files
for rel_path, content in files.items():
    full_path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {full_path}")

print(f"\n✅ Week 02 complete: {len(files)} files created.")
