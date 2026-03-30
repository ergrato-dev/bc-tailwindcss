#!/usr/bin/env python3
"""Generate all content files for week-05: Responsive Design y Mobile-First."""
import os

BASE = "bootcamp/week-05-responsive_design_y_mobile_first"
files = {}

# ─────────────────────────────────────────────────────────────────────────────
# RÚBRICA
# ─────────────────────────────────────────────────────────────────────────────
files["rubrica-evaluacion.md"] = '''# 📊 Rúbrica de Evaluación — Semana 5

**Bootcamp TailwindCSS Zero to Hero** | Semana 5: Responsive Design y Mobile-First

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Filosofía Mobile-First** | Explica por qué se diseña desde el viewport más pequeño hacia arriba; entiende que las variantes `sm:`, `md:` etc. son **min-width** | Aplica mobile-first correctamente aunque no articule bien el porqué | Confunde mobile-first con max-width o aplica breakpoints de forma aleatoria |
| **Breakpoints de Tailwind** | Memoriza o puede consultar los 6 breakpoints (`sm` 640, `md` 768, `lg` 1024, `xl` 1280, `2xl` 1536) y elige el adecuado para cada componente | Usa `sm:`, `md:`, `lg:` correctamente; confunde `xl` y `2xl` | Aplica un solo breakpoint para todo o los usa al revés (large-first) |
| **Container y Breakpoints** | Sabe usar `container mx-auto px-4 sm:px-6 lg:px-8` y entiende la diferencia entre `container` y `max-w-7xl mx-auto` | Centra contenedores con `mx-auto`; no domina el padding responsivo | No sabe centrar un contenedor o usa padding fijo que rompe en móvil |
| **Visibilidad Responsive** | Usa `hidden sm:block`, `sm:hidden`, `block md:hidden` con claridad; entiende que son combinaciones de display | Oculta/muestra elementos en 2 breakpoints; se confunde en 3+ | Usa `display: none` en CSS externo en lugar de variantes de Tailwind |
| **Estrategia de imágenes responsive** | Aplica `w-full h-auto`, `aspect-ratio` y `object-cover` para imágenes adaptables; conoce el atributo `srcset` | Usa `w-full` en imágenes correctamente; desconoce aspect-ratio responsive | Las imágenes se deforman o desbordan en mobile |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Breakpoints** | Visualizador de breakpoints completamente funcional; el indicador cambia en los 5 puntos correctos | Funciona en 3-4 breakpoints; falla en el más pequeño o más grande | No cambia o todos los breakpoints muestran lo mismo |
| **Ejercicio Layout Responsive** | Grid de 1→2→3→4 columnas según breakpoints; navegación se transforma correctamente | Grid funciona en 2-3 tamaños; navegación mobile parcial | Layout no cambia entre mobile y desktop |
| **Ejercicio Tipografía Responsive** | Texto escala correctamente: `text-2xl md:text-4xl lg:text-6xl`; espaciado también escala | Tipografía escala en 2 tamaños correctamente | Tipografía fija en todos los tamaños |
| **Ejercicio Navegación Responsive** | Navbar con hamburger en mobile, links horizontales en desktop usando solo Tailwind + checkbox hack | Navbar se transforma; hamburger no es completamente funcional | Navbar no cambia; links siempre visibles o siempre ocultos |

---

## 📦 Producto (30%)

**Proyecto: Landing Page Responsive**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Hero Section** | Texto escala con `text-3xl md:text-5xl lg:text-7xl`; layout cambia de columna a fila en `md:`; imagen se posiciona correctamente | Hero funcional en mobile y desktop; tipografía escala en 2 tamaños | Hero roto en mobile o no se adapta |
| **Grid de Features** | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` correctamente aplicado | Grid de 1 a 2 columnas | Sin grid; columna única siempre |
| **Navegación** | Navbar completamente responsive con hamburger funcional | Navbar con logo y links; sin hamburger | Navbar fixed que no funciona en mobile |
| **Footer** | Columnas de footer: `grid-cols-1 md:grid-cols-3`; links se apilan en mobile | Footer con 2 columnas responsive | Footer sin estructura responsive |
| **Mobile-First verificado** | Se puede verificar en DevTools mobile (iPhone SE, Pixel) sin scroll horizontal ni overflow | Funciona en mobile con mínimos problemas | Scroll horizontal en mobile o layout roto |
'''

# ─────────────────────────────────────────────────────────────────────────────
# TEORÍA
# ─────────────────────────────────────────────────────────────────────────────
files["1-teoria/01-filosofia-mobile-first.md"] = '''# 📱 Filosofía Mobile-First

## 🎯 Objetivos

- Entender por qué mobile-first es la estrategia estándar del CSS moderno
- Comprender cómo los breakpoints de Tailwind son min-width
- Distinguir mobile-first de desktop-first

---

## 📋 Contenido

![Filosofía Mobile-First — de menor a mayor viewport](../0-assets/01-mobile-first.svg)

### 1. ¿Por qué Mobile-First?

Mobile-first significa **diseñar primero para el viewport más pequeño** y luego añadir complejidad para pantallas más grandes.

**Razones técnicas:**
- El CSS sin prefijo de breakpoint aplica a **todos los tamaños**
- Los breakpoints de Tailwind son `min-width` — se activan hacia arriba
- El browser carga primero el CSS base; las queries de media se evalúan después
- Mejor rendimiento en dispositivos lentos (menos CSS a procesar)

**Razones de diseño:**
- Fuerza a priorizar el contenido (lo esencial primero)
- Evita el "desktop shrink" — adaptaciones torpes de desktop a mobile
- La mayoría del tráfico web es desde mobile

---

### 2. Breakpoints son Min-Width

```html
<!-- ✅ MOBILE-FIRST — base para mobile, escala hacia arriba -->
<p class="text-sm md:text-base lg:text-lg">
  <!-- text-sm: todos los tamaños (incluyendo mobile)    -->
  <!-- md:text-base: >= 768px                            -->
  <!-- lg:text-lg: >= 1024px                             -->
</p>

<!-- ❌ DESKTOP-FIRST (trampa común) — evitar este patrón -->
<p class="text-lg max-md:text-base max-sm:text-sm">
  <!-- Funciona, pero va contra la filosofía mobile-first -->
  <!-- max-md: <= 768px, max-sm: <= 640px                 -->
</p>
```

**Regla de oro:** El CSS sin prefijo es tu "mobile base". Solo agrega breakpoints cuando el diseño NECESITA cambiar para pantallas más grandes.

---

### 3. Las Reglas en Orden

Mobile-first implica escribir las clases en orden de contexto: base → sm → md → lg → xl:

```html
<!-- Correcto: base mobile, luego escalando -->
<div class="
  block          <!-- mobile: bloque -->
  sm:flex        <!-- ≥ 640px: flex -->
  md:grid        <!-- ≥ 768px: grid -->
">
```

---

### 4. Cuándo NO añadir breakpoints

No todo necesita ser responsive. Pregúntate: "¿Este elemento se ve mal en mobile?". Si la respuesta es no, no añadas un breakpoint solo por añadirlo.

```html
<!-- ✅ Solo un breakpoint donde realmente cambia el layout -->
<article class="p-4 md:p-8">
  <h1 class="text-2xl md:text-4xl font-bold">Título</h1>
  <!-- El color del texto es igual en todos: no necesita breakpoint -->
  <p class="text-gray-600 leading-relaxed">Texto...</p>
</article>
```

---

## ✅ Checklist de Verificación

- [ ] Mis clases base funcionan bien en 320px (iPhone SE)
- [ ] Solo añado breakpoints donde el diseño realmente necesita cambiar
- [ ] Uso `sm:`, `md:`, `lg:` (min-width) no `max-sm:`, `max-md:` (max-width)
- [ ] Verifico el resultado en DevTools con el modo responsive activado
'''

files["1-teoria/02-breakpoints-sistema.md"] = '''# 📐 Sistema de Breakpoints

## 🎯 Objetivos

- Memorizar los 6 breakpoints de Tailwind y sus valores
- Elegir el breakpoint correcto para cada caso
- Usar el container responsive correctamente

---

## 📋 Contenido

![Sistema de breakpoints de Tailwind](../0-assets/02-breakpoints.svg)

### 1. Los 6 Breakpoints

| Prefijo | Min-Width | Dispositivo típico |
|---------|-----------|-------------------|
| (base)  | 0px       | Mobile pequeño (320–639px) |
| `sm:`   | 640px     | Mobile grande / landscape |
| `md:`   | 768px     | Tablet portrait |
| `lg:`   | 1024px    | Tablet landscape / laptop |
| `xl:`   | 1280px    | Desktop |
| `2xl:`  | 1536px    | Desktop grande |

```html
<!-- Ejemplo de uso de todos los breakpoints -->
<div class="
  w-full          <!-- 0-639px: ancho completo -->
  sm:w-1/2        <!-- 640-767px: 50% -->
  md:w-1/3        <!-- 768-1023px: 33% -->
  lg:w-1/4        <!-- 1024-1279px: 25% -->
  xl:w-1/5        <!-- 1280-1535px: 20% -->
  2xl:w-1/6       <!-- ≥ 1536px: 16.6% -->
">...</div>
```

---

### 2. Breakpoints Más Usados en Práctica

En la mayoría de proyectos, usarás principalmente `md:` y `lg:`:

```html
<!-- Layout de 2 columnas en tablet+ -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">...</div>

<!-- Texto hero que escala -->
<h1 class="text-3xl md:text-5xl lg:text-7xl font-black">Hero</h1>

<!-- Padding que aumenta en desktop -->
<section class="px-4 md:px-8 lg:px-16 py-12 md:py-24">...</section>
```

---

### 3. Contenedor Responsive

El patrón de contenedor más usado en Tailwind:

```html
<!-- Opción A: max-w-7xl + mx-auto + padding lateral responsive -->
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
  <!-- Contenido de página -->
</div>

<!-- Opción B: clase container de Tailwind (aplica max-w por breakpoint) -->
<div class="container mx-auto px-4">
  <!-- Contenido -->
</div>
```

**Diferencia:**
- `max-w-7xl mx-auto` → ancho máximo fijo de 1280px
- `container` → usa el max-width del breakpoint actual (sm=640, md=768, etc.)

En la mayoría de proyectos modernos, `max-w-7xl mx-auto` es más predecible.

---

### 4. Breakpoints Arbitrarios

Para casos especiales puedes usar valores arbitrarios:

```html
<!-- Breakpoint personalizado -->
<div class="sm:block [@media(min-width:900px)]:flex">...</div>

<!-- Más limpio con variable de diseño en tailwind.config -->
<!-- Preferir los breakpoints estándar cuando sea posible -->
```

---

## ✅ Checklist de Verificación

- [ ] Conozco los valores numéricos de al menos `sm`, `md`, `lg`, `xl`
- [ ] Mis contenedores usan `mx-auto max-w-7xl px-4 sm:px-6 lg:px-8`
- [ ] Testo en los breakpoints clave: 375px, 768px, 1024px, 1280px
- [ ] No uso más breakpoints de los necesarios (minimalismo responsive)
'''

files["1-teoria/03-layout-responsive.md"] = '''# 🔄 Layout Responsive con Tailwind

## 🎯 Objetivos

- Transformar layouts de una columna a múltiples columnas
- Cambiar de flex-column a flex-row según el breakpoint
- Controlar visibilidad de elementos por breakpoint

---

## 📋 Contenido

### 1. Grid Responsive — El Patrón Más Usado

```html
<!-- De 1 → 2 → 3 columnas según viewport -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
  <div>Card 1</div>
  <div>Card 2</div>
  <div>Card 3</div>
</div>

<!-- De 1 → 2 → 4 (para dashboards) -->
<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4">
  <div>Stat 1</div>
  <div>Stat 2</div>
  <div>Stat 3</div>
  <div>Stat 4</div>
</div>
```

---

### 2. Flex Direction Responsive

```html
<!-- Mobile: columna apilada — Desktop: fila lado a lado -->
<section class="flex flex-col md:flex-row gap-8 items-center">
  <div class="w-full md:w-1/2">
    <h2 class="text-3xl font-bold">Texto de hero</h2>
    <p class="mt-4 text-gray-600">Descripción...</p>
  </div>
  <div class="w-full md:w-1/2">
    <img class="w-full rounded-xl" src="..." alt="Hero image" />
  </div>
</section>

<!-- Invertir orden en mobile (texto encima, imagen abajo en desktop) -->
<section class="flex flex-col-reverse md:flex-row gap-8">
  <img class="w-full md:w-1/2" src="..." alt="..." />
  <div class="w-full md:w-1/2">Contenido</div>
</section>
```

---

### 3. Visibilidad Responsive

```html
<!-- Ocultar en mobile, mostrar en tablet+ -->
<nav class="hidden md:flex gap-8">
  <a href="#">Inicio</a>
  <a href="#">Servicios</a>
  <a href="#">Contacto</a>
</nav>

<!-- Mostrar solo en mobile (hamburger, etc.) -->
<button class="block md:hidden">
  <!-- Icono hamburger -->
  <span class="block w-6 h-0.5 bg-gray-800"></span>
  <span class="block w-6 h-0.5 bg-gray-800 mt-1.5"></span>
  <span class="block w-6 h-0.5 bg-gray-800 mt-1.5"></span>
</button>

<!-- Combinaciones comunes -->
<div class="block sm:hidden">Solo mobile (0-639px)</div>
<div class="hidden sm:block md:hidden">Solo small (640-767px)</div>
<div class="hidden md:block">Tablet y desktop (768px+)</div>
<div class="hidden lg:block">Solo desktop (1024px+)</div>
```

---

### 4. Espaciado y Tipografía Responsive

```html
<!-- Padding que escala con la pantalla -->
<section class="py-12 md:py-20 lg:py-32 px-4 sm:px-6 lg:px-8">
  <!-- Hero -->
</section>

<!-- Tipografía escalable: mobile → tablet → desktop -->
<h1 class="text-2xl sm:text-4xl md:text-5xl lg:text-7xl font-black leading-tight">
  Landing Hero Title
</h1>
<p class="text-base md:text-lg lg:text-xl text-gray-600 max-w-2xl mx-auto">
  Descripción del producto...
</p>

<!-- Gap responsive en grids -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6 lg:gap-8">...</div>
```

---

### 5. Imágenes Responsive

```html
<!-- Imagen que ocupa todo el ancho en mobile, mitad en desktop -->
<img
  class="w-full md:w-1/2 h-auto rounded-xl object-cover"
  src="foto.jpg"
  alt="Descripción"
/>

<!-- Imagen con aspect-ratio fijo responsive -->
<div class="aspect-video w-full overflow-hidden rounded-xl">
  <img class="w-full h-full object-cover" src="..." alt="..." />
</div>

<!-- Avatar responsive -->
<img
  class="w-12 h-12 md:w-16 md:h-16 rounded-full object-cover"
  src="avatar.jpg"
  alt="Foto de perfil"
/>
```

---

## ✅ Checklist de Verificación

- [ ] Mis grids empiezan en `grid-cols-1` y escalan hacia arriba
- [ ] Las secciones hero usan `flex-col md:flex-row`
- [ ] Solo oculto elementos con `hidden md:block` (no con JS cuando es solo visual)
- [ ] El espaciado y la tipografía escalan con breakpoints de forma consistente
'''

files["1-teoria/04-navegacion-responsive.md"] = '''# 🗺️ Navegación Responsive

## 🎯 Objetivos

- Construir un navbar que se adapta de mobile a desktop
- Implementar el hamburger menu con el checkbox hack de CSS puro
- Entender las estrategias de menú mobile sin JavaScript

---

## 📋 Contenido

### 1. Estructura Base del Navbar

```html
<header class="sticky top-0 z-50 border-b border-gray-100 bg-white/90 backdrop-blur-sm">
  <nav class="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6">

    <!-- Logo -->
    <a href="/" class="text-xl font-black text-gray-900">
      Brand
    </a>

    <!-- Links — ocultos en mobile -->
    <ul class="hidden md:flex items-center gap-8">
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Inicio</a></li>
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Servicios</a></li>
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Precios</a></li>
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Blog</a></li>
    </ul>

    <!-- CTA — oculto en mobile pequeño -->
    <div class="hidden md:flex items-center gap-3">
      <a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Ingresar</a>
      <a href="#" class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-600 transition-colors">
        Comenzar gratis
      </a>
    </div>

    <!-- Hamburger — solo visible en mobile -->
    <button class="block md:hidden rounded-lg p-2 text-gray-600 hover:bg-gray-100 transition-colors"
            aria-label="Abrir menú">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </button>

  </nav>

  <!-- Mobile menu — requiere JS o checkbox hack para abrir/cerrar -->
  <div class="hidden border-t border-gray-100 px-4 pb-4 pt-2 md:hidden">
    <ul class="space-y-1">
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Inicio</a></li>
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Servicios</a></li>
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Precios</a></li>
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Blog</a></li>
    </ul>
    <div class="mt-3 border-t border-gray-100 pt-3">
      <a href="#" class="block w-full rounded-lg bg-sky-500 px-4 py-2.5 text-center text-sm font-semibold text-white">
        Comenzar gratis
      </a>
    </div>
  </div>
</header>
```

---

### 2. Checkbox Hack — Menú Mobile sin JavaScript

```html
<!-- El input checkbox es el "estado" del menú -->
<header>
  <!-- Checkbox invisible que guarda el estado abierto/cerrado -->
  <input type="checkbox" id="menu-toggle" class="peer sr-only" />

  <nav class="flex items-center justify-between px-4 py-4">
    <a href="/" class="font-black text-xl">Brand</a>

    <!-- Links desktop -->
    <ul class="hidden md:flex gap-8">
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Servicios</a></li>
    </ul>

    <!-- Label que activa el checkbox (hamburger) -->
    <label for="menu-toggle"
           class="block md:hidden cursor-pointer rounded p-1"
           aria-label="Toggle menú">
      <!-- Icono hamburger -->
      <svg class="w-6 h-6 peer-checked:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </label>
  </nav>

  <!-- Mobile menu — se muestra cuando peer (checkbox) está checked -->
  <!-- hidden por defecto, peer-checked:block cuando el checkbox está marcado -->
  <div class="hidden peer-checked:block md:hidden border-t px-4 pb-4">
    <ul class="space-y-1 pt-2">
      <li><a href="#" class="block py-2 text-gray-700">Inicio</a></li>
      <li><a href="#" class="block py-2 text-gray-700">Servicios</a></li>
    </ul>
  </div>
</header>
```

**Nota:** El `peer` necesita que el checkbox sea un hermano previo del elemento que reacciona. En proyectos con React/Next.js, se usa estado de componente.

---

## ✅ Checklist de Verificación

- [ ] El navbar tiene `sticky top-0 z-50` para que se mantenga visible al hacer scroll
- [ ] Los links usan `hidden md:flex` (ocultos en mobile)
- [ ] El hamburger usa `block md:hidden` (visible solo en mobile)
- [ ] El menú mobile funciona (checkbox hack o JS)
- [ ] Hay `aria-label` en el botón hamburger para accesibilidad
'''

files["1-teoria/05-responsive-avanzado.md"] = '''# 🚀 Técnicas Responsive Avanzadas

## 🎯 Objetivos

- Usar variantes responsive con estados (hover, focus)
- Aplicar orden y alineación responsive en flex/grid
- Manejar text overflow y truncation responsive

---

## 📋 Contenido

### 1. Combinar Responsive con Estados

Los prefijos de breakpoint se pueden combinar con variantes de estado:

```html
<!-- hover solo en desktop (mobile no tiene hover real) -->
<a class="text-gray-600 md:hover:text-sky-600 md:transition-colors">
  Link
</a>

<!-- Focus ring tamaño responsive -->
<button class="focus-visible:ring-1 md:focus-visible:ring-2 focus-visible:ring-sky-500">
  Botón
</button>

<!-- Scale en hover solo en desktop -->
<div class="md:hover:scale-105 md:transition-transform duration-200 rounded-xl">
  Card
</div>
```

---

### 2. Orden en Flex/Grid Responsive

```html
<!-- Imagen primero en desktop, segunda en mobile -->
<div class="flex flex-col md:flex-row gap-8">
  <!-- En mobile: texto arriba (order-1), imagen abajo (order-2) -->
  <!-- En desktop: imagen izquierda, texto derecha (order natural) -->
  <div class="order-2 md:order-1 w-full md:w-1/2">
    <img src="..." alt="..." class="w-full rounded-xl" />
  </div>
  <div class="order-1 md:order-2 w-full md:w-1/2">
    <h2>Título</h2>
    <p>Descripción</p>
  </div>
</div>
```

---

### 3. Tipografía y Truncation Responsive

```html
<!-- Mostrar más texto en pantallas grandes -->
<p class="line-clamp-2 md:line-clamp-3 lg:line-clamp-none text-gray-600">
  Párrafo largo que se recorta diferente según el viewport...
</p>

<!-- Tamaño de fuente y leading responsive -->
<h1 class="text-2xl leading-tight sm:text-4xl sm:leading-tight md:text-6xl md:leading-none font-black">
  Gran Título
</h1>

<!-- Alineación responsive -->
<div class="text-center md:text-left">
  <h2 class="text-2xl font-bold">Sección</h2>
  <p class="text-gray-600">Descripción centrada en mobile, izquierda en desktop</p>
</div>
```

---

### 4. Position y Stack Responsive

```html
<!-- Badge que cambia de posición -->
<div class="relative">
  <img src="..." alt="..." class="w-full rounded-xl" />
  <!-- En mobile: badge dentro del flujo; en desktop: overlay absoluto -->
  <span class="md:absolute md:top-4 md:right-4 inline-block rounded-full bg-sky-500 px-3 py-1 text-xs font-bold text-white">
    Nuevo
  </span>
</div>

<!-- Sidebar responsive: se convierte en tabs en mobile -->
<div class="flex flex-col md:flex-row gap-8">
  <!-- Mobile: tabs horizontales / Desktop: sidebar vertical -->
  <nav class="flex flex-row overflow-x-auto md:flex-col md:w-48 gap-1">
    <a href="#" class="shrink-0 rounded-lg px-3 py-2 text-sm font-medium bg-sky-50 text-sky-700">
      Perfil
    </a>
    <a href="#" class="shrink-0 rounded-lg px-3 py-2 text-sm font-medium text-gray-600 hover:bg-gray-50">
      Seguridad
    </a>
  </nav>
  <main class="flex-1">Contenido</main>
</div>
```

---

### 5. Print Variant

```html
<!-- Ocultar en impresión, mostrar solo en pantalla -->
<nav class="print:hidden">Navegación</nav>
<footer class="print:hidden">Footer con ads</footer>

<!-- Mostrar solo en impresión -->
<div class="hidden print:block">
  <p>Versión para imprimir — URL: ejemplo.com/articulo</p>
</div>

<!-- Ajustar colores para impresión -->
<body class="bg-white text-gray-900 print:text-black">
```

---

## ✅ Checklist de Verificación

- [ ] Combino breakpoints con estados cuando tiene sentido (ej: `md:hover:scale-105`)
- [ ] Uso `order-*` responsive cuando necesito reordenar elementos en mobile
- [ ] `line-clamp-*` responsive para truncar texto de forma diferente según pantalla
- [ ] `text-center md:text-left` en secciones que se centran en mobile
- [ ] Verifico el sitio con DevTools en al menos 3 tamaños: 375px, 768px, 1280px
'''

# ─────────────────────────────────────────────────────────────────────────────
# EJERCICIOS
# ─────────────────────────────────────────────────────────────────────────────
files["2-practicas/01-ejercicio-breakpoints/README.md"] = '''# Ejercicio 01: Visualizador de Breakpoints

## 🎯 Objetivo

Crear un componente que muestra visualmente el breakpoint activo en tiempo real, entendiendo cómo funciona el sistema mobile-first de Tailwind.

---

## 📋 Instrucciones

### Paso 1: Indicador de breakpoint activo

Descomenta el **bloque 1** para ver el indicador que muestra qué breakpoint está activo. Redimensiona la ventana del navegador para ver cómo cambia.

### Paso 2: Colores de fondo por breakpoint

Descomenta el **bloque 2** para ver cómo el fondo de una sección cambia de color en cada breakpoint.

### Paso 3: Grid responsive 1-2-3-4

Descomenta el **bloque 3** para ver un grid que cambia el número de columnas en cada breakpoint.

### Paso 4: Tipografía escalable

Descomenta el **bloque 4** para ver texto que escala de tamaño en cada breakpoint.

---

## ✅ Verificación

- Redimensiona la ventana y el indicador debe mostrar: base → sm → md → lg → xl → 2xl
- El grid debe pasar de 1 → 2 → 3 → 4 columnas al agrandar la ventana
- El título debe verse pequeño en mobile y grande en desktop
'''

files["2-practicas/01-ejercicio-breakpoints/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 01 — Breakpoints</title>
  </head>
  <body class="min-h-screen bg-gray-50 font-sans">


    <!-- ============================================ -->
    <!-- BLOQUE 1: Indicador de breakpoint activo     -->
    <!-- ============================================ -->
    <!-- Redimensiona la ventana y observa el cambio  -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <div class="fixed bottom-4 right-4 z-50 rounded-full px-4 py-2 text-xs font-bold text-white shadow-lg  -->
    <!--   bg-gray-800                                                                                          -->
    <!--   sm:bg-blue-500                                                                                       -->
    <!--   md:bg-violet-500                                                                                     -->
    <!--   lg:bg-emerald-500                                                                                    -->
    <!--   xl:bg-amber-500                                                                                      -->
    <!--   2xl:bg-rose-500">                                                                                    -->
    <!--   <span class="sm:hidden">base (&lt;640px)</span>                                                     -->
    <!--   <span class="hidden sm:inline md:hidden">sm (≥640px)</span>                                         -->
    <!--   <span class="hidden md:inline lg:hidden">md (≥768px)</span>                                         -->
    <!--   <span class="hidden lg:inline xl:hidden">lg (≥1024px)</span>                                        -->
    <!--   <span class="hidden xl:inline 2xl:hidden">xl (≥1280px)</span>                                       -->
    <!--   <span class="hidden 2xl:inline">2xl (≥1536px)</span>                                                -->
    <!-- </div>                                                                                                 -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Fondo por breakpoint               -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="py-16 text-center transition-colors duration-300                                                        -->
    <!--   bg-gray-100                                                                                                            -->
    <!--   sm:bg-blue-50                                                                                                          -->
    <!--   md:bg-violet-50                                                                                                        -->
    <!--   lg:bg-emerald-50                                                                                                       -->
    <!--   xl:bg-amber-50">                                                                                                       -->
    <!--   <p class="text-sm font-medium text-gray-500">El fondo cambia en cada breakpoint</p>                                   -->
    <!--   <p class="mt-1 text-xs text-gray-400">base=gris · sm=azul · md=violeta · lg=verde · xl=ámbar</p>                     -->
    <!-- </section>                                                                                                               -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Grid 1→2→3→4 columnas             -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12">                                                         -->
    <!--   <h2 class="mb-6 text-center text-lg font-bold text-gray-700">Grid Responsive (1→2→3→4 columnas)</h2>                  -->
    <!--   <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">                                     -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 1</div>                          -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 2</div>                          -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 3</div>                          -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 4</div>                          -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 5</div>                          -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 6</div>                          -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 7</div>                          -->
    <!--     <div class="rounded-xl bg-sky-100 p-6 text-center font-semibold text-sky-700">Card 8</div>                          -->
    <!--   </div>                                                                                                                  -->
    <!-- </section>                                                                                                               -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Tipografía escalable               -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mx-auto max-w-4xl px-4 py-16 text-center">                                                              -->
    <!--   <h1 class="font-black leading-tight                                                                                    -->
    <!--     text-3xl                                                                                                             -->
    <!--     sm:text-4xl                                                                                                          -->
    <!--     md:text-5xl                                                                                                          -->
    <!--     lg:text-6xl                                                                                                          -->
    <!--     xl:text-7xl">                                                                                                        -->
    <!--     Título que escala<br/>con el viewport                                                                                -->
    <!--   </h1>                                                                                                                  -->
    <!--   <p class="mt-4 text-gray-500                                                                                          -->
    <!--     text-base                                                                                                            -->
    <!--     md:text-lg                                                                                                           -->
    <!--     lg:text-xl                                                                                                           -->
    <!--     max-w-2xl mx-auto">                                                                                                  -->
    <!--     Este texto también aumenta de tamaño en pantallas más grandes,                                                      -->
    <!--     manteniendo las proporciones de diseño.                                                                              -->
    <!--   </p>                                                                                                                   -->
    <!-- </section>                                                                                                               -->

  </body>
</html>
'''

files["2-practicas/02-ejercicio-layout-responsive/README.md"] = '''# Ejercicio 02: Layout Responsive — Mobile a Desktop

## 🎯 Objetivo

Transformar layouts de una sola columna (mobile) a layouts complejos multi-columna (desktop).

---

## 📋 Instrucciones

### Paso 1: Hero con flex-col a flex-row

Descomenta el **bloque 1** para ver cómo una sección hero pasa de apilada (mobile) a lado-a-lado (desktop).

### Paso 2: Cards de features 1→3 columnas

Descomenta el **bloque 2** para ver el grid de features que escala de 1 a 3 columnas.

### Paso 3: Sidebar + content

Descomenta el **bloque 3** para ver el patrón de sidebar vertical que se convierte en tabs horizontales en mobile.

### Paso 4: Footer multi-columna

Descomenta el **bloque 4** para ver el footer que pasa de apilado a 4 columnas en desktop.

---

## ✅ Verificación

- En mobile (375px): todo en una columna, apilado verticalmente
- En tablet (768px): hero lado a lado, 2 columnas de features
- En desktop (1280px): 3 columnas de features, sidebar a la izquierda
'''

files["2-practicas/02-ejercicio-layout-responsive/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 02 — Layout Responsive</title>
  </head>
  <body class="min-h-screen bg-white font-sans text-gray-900">


    <!-- ============================================ -->
    <!-- BLOQUE 1: Hero — flex-col a flex-row         -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12 md:py-20                                  -->
    <!--   flex flex-col md:flex-row items-center gap-8 md:gap-12">                                              -->
    <!--                                                                                                          -->
    <!--   Texto: ancho completo en mobile, mitad en desktop                                                     -->
    <!--   <div class="w-full md:w-1/2 text-center md:text-left">                                               -->
    <!--     <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-black leading-tight">                 -->
    <!--       Diseño que se<br/>adapta a todo                                                                   -->
    <!--     </h1>                                                                                               -->
    <!--     <p class="mt-4 text-lg text-gray-600 max-w-md mx-auto md:mx-0">                                    -->
    <!--       Una landing page que se ve perfecta en cualquier dispositivo.                                     -->
    <!--     </p>                                                                                               -->
    <!--     <div class="mt-8 flex flex-col sm:flex-row gap-3 justify-center md:justify-start">                 -->
    <!--       <a href="#" class="rounded-lg bg-sky-500 px-6 py-3 text-center font-semibold text-white hover:bg-sky-600 transition-colors">Comenzar gratis</a> -->
    <!--       <a href="#" class="rounded-lg border border-gray-200 px-6 py-3 text-center font-semibold text-gray-700 hover:bg-gray-50 transition-colors">Ver demo</a> -->
    <!--     </div>                                                                                              -->
    <!--   </div>                                                                                               -->
    <!--                                                                                                         -->
    <!--   Imagen: ancho completo en mobile, mitad en desktop                                                   -->
    <!--   <div class="w-full md:w-1/2">                                                                        -->
    <!--     <div class="aspect-video w-full rounded-2xl bg-gradient-to-br from-sky-400 to-violet-500"></div>  -->
    <!--   </div>                                                                                               -->
    <!-- </section>                                                                                              -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Features 1→2→3 columnas            -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="bg-gray-50 py-16">                                                                       -->
    <!--   <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">                                                 -->
    <!--     <h2 class="mb-10 text-center text-2xl sm:text-3xl font-bold">Características</h2>                  -->
    <!--     <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">                                  -->
    <!--       <div class="rounded-2xl bg-white p-6 shadow-sm">                                                  -->
    <!--         <div class="h-10 w-10 rounded-xl bg-sky-100 flex items-center justify-center text-sky-600 text-xl mb-4">⚡</div> -->
    <!--         <h3 class="font-semibold text-gray-900">Velocidad</h3>                                          -->
    <!--         <p class="mt-2 text-sm text-gray-600">Optimizado para cargar rápido en cualquier conexión.</p> -->
    <!--       </div>                                                                                             -->
    <!--       <div class="rounded-2xl bg-white p-6 shadow-sm">                                                  -->
    <!--         <div class="h-10 w-10 rounded-xl bg-emerald-100 flex items-center justify-center text-emerald-600 text-xl mb-4">🔒</div> -->
    <!--         <h3 class="font-semibold text-gray-900">Seguridad</h3>                                          -->
    <!--         <p class="mt-2 text-sm text-gray-600">Cifrado end-to-end en todas tus transacciones.</p>       -->
    <!--       </div>                                                                                             -->
    <!--       <div class="rounded-2xl bg-white p-6 shadow-sm sm:col-span-2 lg:col-span-1">                     -->
    <!--         <div class="h-10 w-10 rounded-xl bg-violet-100 flex items-center justify-center text-violet-600 text-xl mb-4">📊</div> -->
    <!--         <h3 class="font-semibold text-gray-900">Analytics</h3>                                          -->
    <!--         <p class="mt-2 text-sm text-gray-600">Métricas en tiempo real para tomar mejores decisiones.</p> -->
    <!--       </div>                                                                                             -->
    <!--     </div>                                                                                              -->
    <!--   </div>                                                                                                -->
    <!-- </section>                                                                                               -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Sidebar layout                     -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16">                                        -->
    <!--   <div class="flex flex-col md:flex-row gap-8">                                                         -->
    <!--     Mobile: tabs horizontales con overflow / Desktop: sidebar vertical                                  -->
    <!--     <nav class="flex flex-row overflow-x-auto md:flex-col md:w-56 shrink-0 gap-1 pb-2 md:pb-0">       -->
    <!--       <a href="#" class="shrink-0 rounded-lg bg-sky-50 px-4 py-2.5 text-sm font-semibold text-sky-700">Perfil</a> -->
    <!--       <a href="#" class="shrink-0 rounded-lg px-4 py-2.5 text-sm font-medium text-gray-600 hover:bg-gray-50 transition-colors">Seguridad</a> -->
    <!--       <a href="#" class="shrink-0 rounded-lg px-4 py-2.5 text-sm font-medium text-gray-600 hover:bg-gray-50 transition-colors">Notificaciones</a> -->
    <!--       <a href="#" class="shrink-0 rounded-lg px-4 py-2.5 text-sm font-medium text-gray-600 hover:bg-gray-50 transition-colors">Facturación</a> -->
    <!--     </nav>                                                                                               -->
    <!--     <main class="flex-1 rounded-2xl border border-gray-100 bg-white p-6 shadow-sm">                    -->
    <!--       <h2 class="text-lg font-semibold text-gray-900">Configuración de Perfil</h2>                     -->
    <!--       <p class="mt-2 text-sm text-gray-600">Actualiza tu información personal y foto de perfil.</p>   -->
    <!--       <div class="mt-6 h-32 rounded-xl bg-gray-50"></div>                                              -->
    <!--     </main>                                                                                             -->
    <!--   </div>                                                                                               -->
    <!-- </section>                                                                                              -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Footer multi-columna               -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <footer class="border-t border-gray-100 bg-white py-12">                                               -->
    <!--   <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">                                               -->
    <!--     <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 mb-8">                           -->
    <!--       <div>                                                                                             -->
    <!--         <p class="text-xl font-black text-gray-900">Brand</p>                                         -->
    <!--         <p class="mt-2 text-sm text-gray-500">Lo mejor para tu negocio.</p>                           -->
    <!--       </div>                                                                                           -->
    <!--       <div>                                                                                             -->
    <!--         <p class="text-sm font-semibold uppercase tracking-wider text-gray-400">Producto</p>          -->
    <!--         <ul class="mt-3 space-y-2 text-sm text-gray-600">                                             -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Características</a></li>      -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Precios</a></li>              -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Changelog</a></li>            -->
    <!--         </ul>                                                                                          -->
    <!--       </div>                                                                                           -->
    <!--       <div>                                                                                             -->
    <!--         <p class="text-sm font-semibold uppercase tracking-wider text-gray-400">Empresa</p>           -->
    <!--         <ul class="mt-3 space-y-2 text-sm text-gray-600">                                             -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Nosotros</a></li>             -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Blog</a></li>                 -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Trabajos</a></li>             -->
    <!--         </ul>                                                                                          -->
    <!--       </div>                                                                                           -->
    <!--       <div>                                                                                             -->
    <!--         <p class="text-sm font-semibold uppercase tracking-wider text-gray-400">Legal</p>             -->
    <!--         <ul class="mt-3 space-y-2 text-sm text-gray-600">                                             -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Privacidad</a></li>           -->
    <!--           <li><a href="#" class="hover:text-gray-900 transition-colors">Términos</a></li>             -->
    <!--         </ul>                                                                                          -->
    <!--       </div>                                                                                           -->
    <!--     </div>                                                                                             -->
    <!--     <div class="border-t border-gray-100 pt-6 text-center text-sm text-gray-400">                     -->
    <!--       © 2025 Brand, Inc. Todos los derechos reservados.                                               -->
    <!--     </div>                                                                                             -->
    <!--   </div>                                                                                               -->
    <!-- </footer>                                                                                              -->

  </body>
</html>
'''

files["2-practicas/03-ejercicio-navbar-responsive/README.md"] = '''# Ejercicio 03: Navbar Responsive con Hamburger

## 🎯 Objetivo

Construir una barra de navegación que se transforma completamente entre mobile y desktop usando solo Tailwind.

---

## 📋 Instrucciones

### Paso 1: Navbar base — logo + links desktop

Descomenta el **bloque 1** para ver la estructura base: logo a la izquierda, links a la derecha (ocultos en mobile).

### Paso 2: Añadir hamburger button

Descomenta el **bloque 2** para agregar el botón hamburger visible solo en mobile.

### Paso 3: Menú mobile expandible (checkbox hack)

Descomenta el **bloque 3** para implementar el menú que se abre/cierra usando el patrón peer de Tailwind.

### Paso 4: Navbar sticky con backdrop blur

Descomenta el **bloque 4** para agregar el efecto de glassmorphism que hace al navbar "flotar" sobre el contenido al hacer scroll.

---

## ✅ Verificación

- En mobile: solo logo + hamburger. Al hacer click, el menú se despliega
- En tablet/desktop: links y CTA visibles, hamburger oculto
- El navbar permanece visible al hacer scroll (sticky)
'''

files["2-practicas/03-ejercicio-navbar-responsive/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 03 — Navbar Responsive</title>
  </head>
  <body class="font-sans text-gray-900">

    <!-- Contenido de relleno para probar scroll -->
    <div class="h-8 bg-sky-500 text-center text-sm text-white flex items-center justify-center">
      Barra de anuncio — redimensiona para ver el navbar responsive
    </div>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Navbar base                        -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <header class="border-b border-gray-100 bg-white">                                                        -->
    <!--   <nav class="mx-auto flex max-w-7xl items-center justify-between px-4 sm:px-6 py-4">                    -->
    <!--                                                                                                            -->
    <!--     Logo                                                                                                   -->
    <!--     <a href="/" class="text-xl font-black text-gray-900">Brand</a>                                       -->
    <!--                                                                                                            -->
    <!--     Links — ocultos en mobile, visibles en md+                                                            -->
    <!--     <ul class="hidden md:flex items-center gap-8">                                                        -->
    <!--       <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Producto</a></li> -->
    <!--       <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Precios</a></li> -->
    <!--       <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Blog</a></li>    -->
    <!--       <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Empresa</a></li> -->
    <!--     </ul>                                                                                                  -->
    <!--                                                                                                            -->
    <!--     CTA oculto en mobile                                                                                  -->
    <!--     <div class="hidden md:flex items-center gap-3">                                                       -->
    <!--       <a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Ingresar</a>             -->
    <!--       <a href="#" class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-600 transition-colors">Prueba gratis</a> -->
    <!--     </div>                                                                                                 -->
    <!--                                                                                                            -->
    <!--   </nav>                                                                                                   -->
    <!-- </header>                                                                                                  -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Hamburger button                   -->
    <!-- ============================================ -->
    <!-- Reemplaza la etiqueta </header> del bloque 1 -->
    <!-- con este contenido DENTRO del <header>:      -->
    <!-- (descomenta solo si ya tienes el bloque 1)   -->

    <!-- Añade dentro del <nav> antes del cierre </nav>:                                                         -->
    <!-- <button type="button" class="block md:hidden rounded-lg p-2 text-gray-600                               -->
    <!--   hover:bg-gray-100 transition-colors" aria-label="Abrir menú">                                         -->
    <!--   <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">                           -->
    <!--     <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"                               -->
    <!--       d="M4 6h16M4 12h16M4 18h16"/>                                                                      -->
    <!--   </svg>                                                                                                  -->
    <!-- </button>                                                                                                 -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Checkbox hack — menú mobile        -->
    <!-- ============================================ -->
    <!-- Este bloque reemplaza todo el <header> previo -->
    <!-- con la versión completa usando peer            -->

    <!-- <input type="checkbox" id="nav-toggle" class="peer sr-only" />                                            -->
    <!-- <header class="border-b border-gray-100 bg-white">                                                        -->
    <!--   <nav class="mx-auto flex max-w-7xl items-center justify-between px-4 sm:px-6 py-4">                    -->
    <!--     <a href="/" class="text-xl font-black">Brand</a>                                                     -->
    <!--     <ul class="hidden md:flex items-center gap-8">                                                        -->
    <!--       <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Producto</a></li>    -->
    <!--       <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Precios</a></li>     -->
    <!--       <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Blog</a></li>        -->
    <!--     </ul>                                                                                                  -->
    <!--     <a href="#" class="hidden md:inline-flex rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-600">Prueba gratis</a> -->
    <!--     <label for="nav-toggle" class="block md:hidden cursor-pointer rounded-lg p-2 text-gray-600 hover:bg-gray-100" aria-label="Toggle menú"> -->
    <!--       <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">                        -->
    <!--         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/> -->
    <!--       </svg>                                                                                               -->
    <!--     </label>                                                                                              -->
    <!--   </nav>                                                                                                   -->
    <!--   Mobile menu — se muestra con peer-checked                                                              -->
    <!--   <div class="hidden peer-checked:block border-t border-gray-100 md:hidden">                            -->
    <!--     <ul class="space-y-1 px-4 py-3">                                                                     -->
    <!--       <li><a href="#" class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Producto</a></li> -->
    <!--       <li><a href="#" class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Precios</a></li>   -->
    <!--       <li><a href="#" class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Blog</a></li>      -->
    <!--     </ul>                                                                                                  -->
    <!--     <div class="border-t border-gray-100 px-4 py-3">                                                     -->
    <!--       <a href="#" class="block w-full rounded-lg bg-sky-500 py-2.5 text-center text-sm font-semibold text-white">Prueba gratis</a> -->
    <!--     </div>                                                                                                 -->
    <!--   </div>                                                                                                   -->
    <!-- </header>                                                                                                  -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Sticky con backdrop blur           -->
    <!-- ============================================ -->
    <!-- Modifica la clase del <header> del bloque 3  -->
    <!-- añadiendo estas clases al <header>:          -->
    <!-- sticky top-0 z-50 bg-white/80 backdrop-blur-md -->
    <!-- Y elimina la clase bg-white original          -->

    <!-- Página de relleno para probar scroll -->
    <main class="mx-auto max-w-7xl px-4 py-20 space-y-32">
      <section class="h-screen flex items-center justify-center text-center">
        <div>
          <h1 class="text-4xl font-black">Sección Principal</h1>
          <p class="mt-4 text-gray-500">Haz scroll para ver el navbar sticky</p>
        </div>
      </section>
      <section class="h-screen flex items-center justify-center bg-gray-50 rounded-2xl">
        <p class="text-gray-400">Segunda sección</p>
      </section>
    </main>

  </body>
</html>
'''

files["2-practicas/04-ejercicio-imagenes-responsive/README.md"] = '''# Ejercicio 04: Imágenes y Media Responsive

## 🎯 Objetivo

Dominar el control de imágenes responsivas usando `w-full`, `object-fit`, `aspect-ratio` y disposición flexible.

---

## 📋 Instrucciones

### Paso 1: Imagen hero responsive

Descomenta el **bloque 1** para ver una imagen que ocupa todo el ancho en mobile y la mitad en desktop.

### Paso 2: Galería grid responsive

Descomenta el **bloque 2** para ver una galería que pasa de 1 → 2 → 3 columnas con fotos que mantienen `aspect-ratio`.

### Paso 3: Card con imagen — object-cover responsive

Descomenta el **bloque 3** para ver cards donde la imagen tiene altura fija en desktop pero se adapta en mobile.

### Paso 4: Avatar y media escalables

Descomenta el **bloque 4** para ver avatares y thumbnails que escalan con el viewport.

---

## ✅ Verificación

- Las imágenes nunca salen de su contenedor ni se deforman
- La galería pasa de 1 a 3 columnas sin overflow
- Las cards tienen altura de imagen consistente en desktop
'''

files["2-practicas/04-ejercicio-imagenes-responsive/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 04 — Imágenes Responsive</title>
  </head>
  <body class="min-h-screen bg-gray-50 font-sans p-4 sm:p-8">
    <h1 class="mb-8 text-2xl font-bold text-gray-900">Imágenes Responsive</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Imagen hero responsive             -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-12 flex flex-col md:flex-row gap-8 items-center bg-white rounded-2xl p-6 shadow-sm">  -->
    <!--   <div class="w-full md:w-1/2">                                                                           -->
    <!--     <h2 class="text-2xl font-bold">Imagen Hero</h2>                                                     -->
    <!--     <p class="mt-2 text-gray-600">Full-width en mobile, mitad en desktop. object-cover mantiene proporciones.</p> -->
    <!--   </div>                                                                                                   -->
    <!--   Usa un div de color para simular imagen                                                                 -->
    <!--   <div class="w-full md:w-1/2 aspect-video rounded-xl overflow-hidden">                                  -->
    <!--     <div class="w-full h-full bg-gradient-to-br from-sky-400 to-violet-500 object-cover"></div>          -->
    <!--   </div>                                                                                                   -->
    <!-- </section>                                                                                                 -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Galería grid responsive            -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12">                                                                                    -->
    <!--   <h2 class="mb-4 text-lg font-semibold text-gray-700">Galería 1→2→3 columnas</h2>                      -->
    <!--   <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">                                     -->
    <!--     <div class="aspect-square overflow-hidden rounded-xl bg-sky-300"></div>                              -->
    <!--     <div class="aspect-square overflow-hidden rounded-xl bg-violet-300"></div>                           -->
    <!--     <div class="aspect-square overflow-hidden rounded-xl bg-emerald-300"></div>                          -->
    <!--     <div class="aspect-square overflow-hidden rounded-xl bg-amber-300"></div>                            -->
    <!--     <div class="aspect-square overflow-hidden rounded-xl bg-rose-300"></div>                             -->
    <!--     <div class="aspect-square overflow-hidden rounded-xl bg-teal-300"></div>                             -->
    <!--   </div>                                                                                                   -->
    <!-- </section>                                                                                                 -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Cards con imagen object-cover      -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12">                                                                                    -->
    <!--   <h2 class="mb-4 text-lg font-semibold text-gray-700">Cards con imagen — altura consistente</h2>       -->
    <!--   <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">                                     -->
    <!--     <article class="overflow-hidden rounded-2xl bg-white shadow-sm">                                     -->
    <!--       Altura fija de imagen — object-cover recorta sin deformar                                          -->
    <!--       <div class="h-40 sm:h-48 overflow-hidden">                                                        -->
    <!--         <div class="h-full w-full bg-gradient-to-br from-sky-400 to-blue-600"></div>                    -->
    <!--       </div>                                                                                              -->
    <!--       <div class="p-4">                                                                                   -->
    <!--         <h3 class="font-semibold">Artículo 1</h3>                                                        -->
    <!--         <p class="mt-1 text-sm text-gray-500 line-clamp-2">Contenido del artículo con texto de ejemplo.</p> -->
    <!--       </div>                                                                                              -->
    <!--     </article>                                                                                            -->
    <!--     <article class="overflow-hidden rounded-2xl bg-white shadow-sm">                                     -->
    <!--       <div class="h-40 sm:h-48 overflow-hidden">                                                        -->
    <!--         <div class="h-full w-full bg-gradient-to-br from-violet-400 to-purple-600"></div>               -->
    <!--       </div>                                                                                              -->
    <!--       <div class="p-4">                                                                                   -->
    <!--         <h3 class="font-semibold">Artículo 2</h3>                                                        -->
    <!--         <p class="mt-1 text-sm text-gray-500 line-clamp-2">Otro artículo con descripción breve.</p>     -->
    <!--       </div>                                                                                              -->
    <!--     </article>                                                                                            -->
    <!--     <article class="overflow-hidden rounded-2xl bg-white shadow-sm sm:col-span-2 lg:col-span-1">        -->
    <!--       <div class="h-40 sm:h-48 overflow-hidden">                                                        -->
    <!--         <div class="h-full w-full bg-gradient-to-br from-emerald-400 to-teal-600"></div>                -->
    <!--       </div>                                                                                              -->
    <!--       <div class="p-4">                                                                                   -->
    <!--         <h3 class="font-semibold">Artículo 3</h3>                                                        -->
    <!--         <p class="mt-1 text-sm text-gray-500 line-clamp-2">Un tercer artículo con más contenido.</p>    -->
    <!--       </div>                                                                                              -->
    <!--     </article>                                                                                            -->
    <!--   </div>                                                                                                  -->
    <!-- </section>                                                                                                 -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Avatares escalables                -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12 rounded-2xl bg-white p-6 shadow-sm">                                               -->
    <!--   <h2 class="mb-4 text-lg font-semibold text-gray-700">Avatares y media escalables</h2>                 -->
    <!--   <div class="flex items-center gap-4">                                                                   -->
    <!--     Tamaño base en mobile, más grande en desktop                                                         -->
    <!--     <div class="h-10 w-10 sm:h-12 sm:w-12 md:h-16 md:w-16 rounded-full overflow-hidden shrink-0">       -->
    <!--       <div class="h-full w-full bg-sky-400"></div>                                                       -->
    <!--     </div>                                                                                               -->
    <!--     <div class="min-w-0">                                                                                 -->
    <!--       <p class="font-semibold text-gray-900 text-sm sm:text-base truncate">Ana García Rodríguez</p>     -->
    <!--       <p class="text-xs sm:text-sm text-gray-500">Diseñadora Senior · Madrid</p>                        -->
    <!--     </div>                                                                                               -->
    <!--   </div>                                                                                                  -->
    <!-- </section>                                                                                                 -->

  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# PROYECTO
# ─────────────────────────────────────────────────────────────────────────────
files["3-proyecto/landing-page-responsive/README.md"] = '''# Proyecto Semana 5: Landing Page Responsive

## 📋 Descripción

Construye una **landing page completa** que funcione perfectamente en todos los dispositivos: mobile (375px), tablet (768px) y desktop (1280px+). El proyecto integra todos los conceptos de responsive design de la semana.

---

## 🎯 Objetivos

- Implementar mobile-first desde cero
- Navbar responsive con hamburger funcional
- Hero section que cambia de layout en tablet+
- Grid de features 1→2→3 columnas
- Footer multi-columna responsive

---

## 📐 Estructura de la Landing

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR (logo + links desktop | logo + hamburger mobile) │
├─────────────────────────────────────────────────────┤
│  HERO                                               │
│  Mobile: título centrado + botones + imagen abajo   │
│  Desktop: texto izquierda | imagen derecha          │
├─────────────────────────────────────────────────────┤
│  FEATURES  1 col → 2 col → 3 col                   │
│  [⚡ Speed] [🔒 Security] [📊 Analytics]            │
│  [🎯 Focus] [💡 Smart]   [🚀 Scale]                │
├─────────────────────────────────────────────────────┤
│  TESTIMONIAL  centrado en mobile, max-w-2xl         │
├─────────────────────────────────────────────────────┤
│  FOOTER  1 col → 4 col  con nav links               │
└─────────────────────────────────────────────────────┘
```

---

## 📋 Requisitos

### Navbar
- [ ] Logo a la izquierda
- [ ] Links de navegación ocultos en mobile (`hidden md:flex`)
- [ ] Hamburger visible solo en mobile (`block md:hidden`)
- [ ] Menú mobile funcional (checkbox hack o JS)
- [ ] `sticky top-0 z-50` con glassmorphism (`bg-white/80 backdrop-blur`)

### Hero
- [ ] Mobile: layout columna, texto centrado
- [ ] Desktop: `flex-row`, texto izquierda, imagen derecha
- [ ] Tipografía escala: `text-3xl md:text-5xl lg:text-7xl`
- [ ] Botones: columna en mobile, fila en sm+

### Features
- [ ] `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`
- [ ] Al menos 6 cards con icono, título y descripción
- [ ] Gap responsive: `gap-4 md:gap-6`

### Footer
- [ ] `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4`
- [ ] Logo + descripción, 3 columnas de links
- [ ] Línea de copyright al final, centrada

### Verificación Mobile-First
- [ ] Sin scroll horizontal en 375px
- [ ] Legible sin zoom en 320px
- [ ] Verificado en DevTools (modo responsive)
'''

files["3-proyecto/landing-page-responsive/starter/index.html"] = '''<!DOCTYPE html>
<!--
  Proyecto Semana 5: Landing Page Responsive
  Implementa todos los TODO usando SOLO clases TailwindCSS
  Verifica en: 375px (mobile), 768px (tablet), 1280px (desktop)
-->
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Landing Page Responsive — Semana 5</title>
  </head>
  <body class="bg-white font-sans text-gray-900 antialiased">

    <!-- ========================================== -->
    <!-- NAVBAR                                     -->
    <!-- ========================================== -->
    <!-- TODO: sticky top-0 z-50 border-b border-gray-100  -->
    <!-- TODO: bg-white/80 backdrop-blur-md          -->
    <input type="checkbox" id="nav-toggle" class="peer sr-only" />
    <header class="???">

      <!-- TODO: nav container con max-w-7xl + flex + justify-between -->
      <nav class="???  px-4 sm:px-6 py-4">

        <!-- Logo -->
        <!-- TODO: text-xl font-black text-gray-900 -->
        <a href="/" class="???">Acme</a>

        <!-- Nav links — TODO: hidden md:flex gap-8 -->
        <ul class="???">
          <li><a href="#features" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Características</a></li>
          <li><a href="#testimonial" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Testimonios</a></li>
          <li><a href="#pricing" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Precios</a></li>
        </ul>

        <!-- CTA desktop — TODO: hidden md:flex items-center gap-3 -->
        <div class="???">
          <a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Ingresar</a>
          <!-- TODO: rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-600 transition-colors -->
          <a href="#" class="???">Prueba gratis</a>
        </div>

        <!-- Hamburger — TODO: block md:hidden -->
        <label for="nav-toggle" class="???  cursor-pointer rounded-lg p-2 text-gray-600 hover:bg-gray-100 transition-colors" aria-label="Toggle menú">
          <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </label>
      </nav>

      <!-- Mobile menu — TODO: hidden peer-checked:block border-t border-gray-100 md:hidden -->
      <div class="???">
        <ul class="space-y-1 px-4 py-3">
          <li><a href="#features" class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Características</a></li>
          <li><a href="#testimonial" class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Testimonios</a></li>
          <li><a href="#pricing" class="block rounded-lg px-3 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50">Precios</a></li>
        </ul>
        <div class="border-t border-gray-100 px-4 py-3">
          <a href="#" class="block w-full rounded-lg bg-sky-500 py-2.5 text-center text-sm font-semibold text-white">Prueba gratis</a>
        </div>
      </div>
    </header>

    <!-- ========================================== -->
    <!-- HERO                                       -->
    <!-- ========================================== -->
    <!-- TODO: contenedor con py-16 md:py-24 lg:py-32 -->
    <!-- TODO: flex flex-col md:flex-row items-center gap-12 -->
    <section class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8  ???">

      <!-- Texto hero -->
      <!-- TODO: w-full md:w-1/2 text-center md:text-left -->
      <div class="???">
        <span class="inline-block rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold text-sky-700">
          Nuevo — v2.0 disponible
        </span>
        <!-- TODO: text-3xl sm:text-5xl lg:text-7xl font-black leading-tight mt-4 -->
        <h1 class="???">
          Diseña más rápido.<br/>Lanza más lejos.
        </h1>
        <!-- TODO: mt-6 text-lg text-gray-600 max-w-md mx-auto md:mx-0 -->
        <p class="???">
          La plataforma que te permite construir productos digitales increíbles sin fricciones.
        </p>
        <!-- TODO: mt-8 flex flex-col sm:flex-row gap-3 justify-center md:justify-start -->
        <div class="???">
          <a href="#" class="rounded-lg bg-sky-500 px-6 py-3 text-center font-semibold text-white hover:bg-sky-600 transition-colors">
            Comenzar gratis
          </a>
          <a href="#" class="rounded-lg border border-gray-200 px-6 py-3 text-center font-semibold text-gray-700 hover:bg-gray-50 transition-colors">
            Ver demo →
          </a>
        </div>
      </div>

      <!-- Imagen hero -->
      <!-- TODO: w-full md:w-1/2 -->
      <div class="???">
        <!-- TODO: aspect-video w-full rounded-2xl overflow-hidden -->
        <div class="???  bg-gradient-to-br from-sky-400 via-blue-500 to-violet-600 shadow-2xl shadow-sky-500/20"></div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- FEATURES                                   -->
    <!-- ========================================== -->
    <section id="features" class="bg-gray-50 py-16 md:py-24">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <!-- TODO: text-center mb-12 -->
        <div class="???">
          <!-- TODO: text-3xl md:text-4xl font-black -->
          <h2 class="???">Todo lo que necesitas</h2>
          <!-- TODO: mt-4 text-lg text-gray-600 max-w-2xl mx-auto -->
          <p class="???">Herramientas poderosas diseñadas para equipos modernos.</p>
        </div>

        <!-- TODO: grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 -->
        <div class="???">

          <!-- Feature card — repite el patrón para los 6 features -->
          <!-- TODO: rounded-2xl bg-white p-6 shadow-sm hover:shadow-md transition-shadow -->
          <div class="???">
            <div class="h-12 w-12 rounded-xl bg-sky-100 flex items-center justify-center text-2xl mb-4">⚡</div>
            <!-- TODO: font-bold text-gray-900 text-lg -->
            <h3 class="???">Ultra rápido</h3>
            <!-- TODO: mt-2 text-gray-600 text-sm leading-relaxed -->
            <p class="???">Velocidades de carga que sorprenden a tus usuarios desde el primer segundo.</p>
          </div>

          <div class="rounded-2xl bg-white p-6 shadow-sm hover:shadow-md transition-shadow">
            <div class="h-12 w-12 rounded-xl bg-emerald-100 flex items-center justify-center text-2xl mb-4">🔒</div>
            <h3 class="font-bold text-gray-900 text-lg">Seguro</h3>
            <p class="mt-2 text-gray-600 text-sm leading-relaxed">Cifrado de extremo a extremo en todas tus operaciones.</p>
          </div>

          <div class="rounded-2xl bg-white p-6 shadow-sm hover:shadow-md transition-shadow">
            <div class="h-12 w-12 rounded-xl bg-violet-100 flex items-center justify-center text-2xl mb-4">📊</div>
            <h3 class="font-bold text-gray-900 text-lg">Analytics</h3>
            <p class="mt-2 text-gray-600 text-sm leading-relaxed">Métricas en tiempo real para decisiones basadas en datos.</p>
          </div>

          <div class="rounded-2xl bg-white p-6 shadow-sm hover:shadow-md transition-shadow">
            <div class="h-12 w-12 rounded-xl bg-amber-100 flex items-center justify-center text-2xl mb-4">🎯</div>
            <h3 class="font-bold text-gray-900 text-lg">Enfocado</h3>
            <p class="mt-2 text-gray-600 text-sm leading-relaxed">Interfaz limpia diseñada para maximizar tu productividad.</p>
          </div>

          <div class="rounded-2xl bg-white p-6 shadow-sm hover:shadow-md transition-shadow">
            <div class="h-12 w-12 rounded-xl bg-rose-100 flex items-center justify-center text-2xl mb-4">💡</div>
            <h3 class="font-bold text-gray-900 text-lg">Inteligente</h3>
            <p class="mt-2 text-gray-600 text-sm leading-relaxed">IA integrada que aprende de tus patrones de trabajo.</p>
          </div>

          <div class="rounded-2xl bg-white p-6 shadow-sm hover:shadow-md transition-shadow">
            <div class="h-12 w-12 rounded-xl bg-teal-100 flex items-center justify-center text-2xl mb-4">🚀</div>
            <h3 class="font-bold text-gray-900 text-lg">Escalable</h3>
            <p class="mt-2 text-gray-600 text-sm leading-relaxed">Crece desde un usuario hasta millones sin cambiar stack.</p>
          </div>

        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TESTIMONIAL                                -->
    <!-- ========================================== -->
    <section id="testimonial" class="py-16 md:py-24">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <!-- TODO: max-w-2xl mx-auto text-center -->
        <blockquote class="???">
          <p class="text-xl md:text-2xl font-medium text-gray-900 leading-relaxed">
            "Acme redujo nuestro tiempo de lanzamiento en un 60%. El equipo no puede imaginar trabajar sin él."
          </p>
          <footer class="mt-6 flex items-center justify-center gap-3">
            <div class="h-10 w-10 rounded-full bg-sky-300 overflow-hidden"></div>
            <div class="text-left">
              <p class="text-sm font-semibold text-gray-900">María Pérez</p>
              <p class="text-xs text-gray-500">CTO en TechStartup</p>
            </div>
          </footer>
        </blockquote>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- FOOTER                                     -->
    <!-- ========================================== -->
    <!-- TODO: border-t border-gray-100 bg-white py-12 md:py-16 -->
    <footer class="???">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <!-- TODO: grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 mb-10 -->
        <div class="???">

          <!-- Brand column -->
          <div>
            <p class="text-xl font-black text-gray-900">Acme</p>
            <p class="mt-2 text-sm text-gray-500 leading-relaxed">
              La plataforma para equipos que quieren construir sin límites.
            </p>
          </div>

          <!-- Links column 1 -->
          <div>
            <p class="text-xs font-semibold uppercase tracking-wider text-gray-400">Producto</p>
            <ul class="mt-4 space-y-2">
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Características</a></li>
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Precios</a></li>
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Changelog</a></li>
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Docs</a></li>
            </ul>
          </div>

          <!-- Links column 2 -->
          <div>
            <p class="text-xs font-semibold uppercase tracking-wider text-gray-400">Empresa</p>
            <ul class="mt-4 space-y-2">
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Nosotros</a></li>
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Blog</a></li>
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Prensa</a></li>
            </ul>
          </div>

          <!-- Links column 3 -->
          <div>
            <p class="text-xs font-semibold uppercase tracking-wider text-gray-400">Legal</p>
            <ul class="mt-4 space-y-2">
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Privacidad</a></li>
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Términos</a></li>
              <li><a href="#" class="text-sm text-gray-600 hover:text-gray-900 transition-colors">Cookies</a></li>
            </ul>
          </div>

        </div>

        <!-- Copyright -->
        <!-- TODO: border-t border-gray-100 pt-6 text-center text-sm text-gray-400 -->
        <div class="???">
          © 2025 Acme, Inc. Todos los derechos reservados.
        </div>
      </div>
    </footer>

    <script type="module" src="/src/main.js"></script>
  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# GLOSARIO
# ─────────────────────────────────────────────────────────────────────────────
files["5-glosario/README.md"] = '''# Glosario — Semana 5: Responsive Design y Mobile-First

---

## B

### Breakpoint
Punto de quiebre definido por un valor de ancho de viewport en el que el diseño cambia. En Tailwind: `sm` (640px), `md` (768px), `lg` (1024px), `xl` (1280px), `2xl` (1536px). Todos son **min-width**.

### `backdrop-blur`
Efecto de desenfoque de fondo usando `backdrop-filter: blur()`. Usado en navbars con `bg-white/80 backdrop-blur-md` para el efecto glassmorphism.

## C

### Checkbox Hack
Técnica CSS pura para crear menús toggle sin JavaScript. Un `<input type="checkbox">` actúa como estado; su label activa/desactiva la visibilidad de un elemento usando la variante `peer-checked:` de Tailwind.

### `container`
Clase de Tailwind que aplica `max-width` según el breakpoint activo y centra el elemento. Alternativa a `max-w-7xl mx-auto`.

## G

### Glassmorphism
Efecto visual de "vidrio esmerilado" logrado con `bg-white/80 backdrop-blur-md`. Común en navbars sticky.

## M

### Mobile-First
Estrategia de diseño donde el CSS base aplica a pantallas pequeñas y los breakpoints escalan hacia arriba. Las variantes `sm:`, `md:` son **min-width** en Tailwind.

### `min-width` (breakpoint)
Los breakpoints de Tailwind se activan cuando el viewport es **mayor o igual** al valor del breakpoint. Es lo opuesto a `max-width` (desktop-first).

## P

### Progressive Enhancement
Filosofía de desarrollo donde el contenido base funciona en todos los dispositivos y las mejoras visuales/interactivas se añaden progresivamente para dispositivos más capaces. Mobile-first es una aplicación práctica de esta filosofía.

## R

### Responsive Design
Diseño web que adapta el layout, tipografía y componentes al tamaño del viewport, asegurando una experiencia óptima en todos los dispositivos.

## S

### `srcset`
Atributo HTML de `<img>` que permite especificar múltiples fuentes de imagen para diferentes resoluciones o tamaños de viewport. Complemento a `w-full` de Tailwind para imágenes verdaderamente responsive.

### `sticky`
Posicionamiento CSS donde un elemento se comporta como `relative` en el flujo normal pero se adhiere al viewport al hacer scroll. `sticky top-0` en navbars mantiene la barra siempre visible.

## V

### Viewport
El área visible del navegador donde se renderiza la página web. Sus dimensiones (`vw`, `vh`) son la referencia para los breakpoints y unidades como `w-screen`, `h-screen`.

### Visibilidad Responsive
Control de qué elementos son visibles en qué breakpoints usando `hidden md:block` (oculto en mobile, visible en md+) y `block md:hidden` (visible en mobile, oculto en md+).
'''

# ─────────────────────────────────────────────────────────────────────────────
# RECURSOS
# ─────────────────────────────────────────────────────────────────────────────
files["4-recursos/ebooks-free/README.md"] = '''# Libros y Ebooks Gratuitos — Semana 5

---

## Responsive Design

### 📘 Responsive Web Design — Ethan Marcotte
- El artículo original (2010) que definió el concepto: busca "Ethan Marcotte responsive web design A List Apart"
- Lectura histórica fundamental para entender de dónde viene el responsive design

### 📘 Every Layout — Heydon Pickering & Andy Bell (capítulos gratuitos)
- **Enlace**: [every-layout.dev](https://every-layout.dev/)
- Algoritmos de layout CSS modernos; varios capítulos gratuitos
- Técnicas que funcionan responsivamente por diseño, sin breakpoints

### 📘 MDN Responsive Design Guide
- **Enlace**: [https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- Completamente gratuito, referencia técnica con ejemplos

---

## Mobile-First

### 📘 Mobile First — Luke Wroblewski
- Busca "Luke Wroblewski Mobile First free PDF"
- El libro que popularizó la philosophía mobile-first en diseño web
'''

files["4-recursos/videografia/README.md"] = '''# Videos y Tutoriales — Semana 5

---

## Responsive con Tailwind

### 🎥 Tailwind CSS Responsive Design Tutorial
- Busca en YouTube: "tailwind css responsive breakpoints tutorial"
- Aprenderás el sistema de breakpoints en acción

### 🎥 Build a Responsive Landing Page with Tailwind
- Busca: "responsive landing page tailwind css tutorial 2024"
- Proyecto completo de una landing page responsive

---

## Mobile-First CSS

### 🎥 Mobile First CSS — Is It Time to Rethink?
- Busca: "mobile first CSS Kevin Powell"
- Explicación profunda de por qué mobile-first importa

### 🎥 Tailwind Responsive Navbar Tutorial
- Busca: "tailwind responsive navbar hamburger menu tutorial"
- Aprende el patrón de navbar con checkbox hack

---

## DevTools

### 🎥 Chrome DevTools Responsive Design Mode
- Busca: "chrome devtools responsive design mode tutorial"
- Aprende a testear en múltiples dispositivos con DevTools
'''

files["4-recursos/webgrafia/README.md"] = '''# Recursos Web — Semana 5

---

## Tailwind Responsive

- **Responsive Design Docs**: [https://tailwindcss.com/docs/responsive-design](https://tailwindcss.com/docs/responsive-design)
- **Breakpoints Customization**: [https://tailwindcss.com/docs/screens](https://tailwindcss.com/docs/screens)
- **Container**: [https://tailwindcss.com/docs/container](https://tailwindcss.com/docs/container)

---

## Especificaciones

- **MDN Viewport meta tag**: [https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)
- **MDN Media Queries**: [https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries)

---

## Herramientas

- **Responsively App** (gratis): Ver múltiples viewports a la vez — busca "responsively app"
- **Chrome DevTools Responsive Mode**: Integrado en Chrome — F12 → ícono de dispositivo
- **Am I Responsive**: [https://ui.dev/amiresponsive](https://ui.dev/amiresponsive) — mockup de tu página en varios dispositivos

---

## Artículos Recomendados

- "The Many Faces of Themeable Design Systems" — para entender breakpoints de sistema
- "A Complete Guide to CSS Grid" (CSS-Tricks) — grids responsive sin breakpoints
- Busca: "tailwind css responsive design best practices 2024"
'''

# Write all files
for rel_path, content in files.items():
    full_path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ {full_path}")

print(f"\n✅ Week 05 complete: {len(files)} files created.")
