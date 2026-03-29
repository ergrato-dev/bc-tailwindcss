#!/usr/bin/env python3
"""Generate all content files for week-04: Borders, Shadows, Sizing y Estados."""
import os

BASE = "bootcamp/week-04-borders_shadows_sizing_y_estados"
files = {}

# ─────────────────────────────────────────────────────────────────────────────
# RÚBRICA
# ─────────────────────────────────────────────────────────────────────────────
files["rubrica-evaluacion.md"] = '''# 📊 Rúbrica de Evaluación — Semana 4

**Bootcamp TailwindCSS Zero to Hero** | Semana 4: Borders, Shadows, Sizing y Estados

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Borders y Rounded** | Explica `border`, `border-{n}`, `border-{color}`, `rounded-*` y cuándo usar cada uno; entiende la diferencia entre `rounded` y `rounded-full` | Aplica bordes y redondeados básicos sin confundir lados | Confunde `border` (ancho) con `border-color` o aplica mal `rounded` |
| **Shadows** | Domina `shadow-sm` a `shadow-2xl`, `shadow-{color}`, `drop-shadow`; elige la sombra correcta por uso contextual | Aplica sombras comunes (`shadow-sm`, `shadow-md`) sin errores | Aplica sombras al azar sin considerar profundidad visual |
| **Sizing** | Conoce `w-*`, `h-*`, `min/max-w/h`, valores especiales (`full`, `screen`, `fit`, `auto`); opera con el box model | Aplica `w-*` y `h-*` correctamente; confunde `w-full` vs `w-screen` | No puede predecir cómo se verá un elemento con un tamaño dado |
| **Estados interactivos** | Domina `hover:`, `focus:`, `active:`, `disabled:`, `focus-visible:`; explica cuándo usar cada uno con accesibilidad | Usa `hover:` y `focus:` correctamente; confunde `focus` vs `focus-visible` | Solo usa `hover:` sin considerar keyboard nav o disabled states |
| **Group y Peer** | Explica y usa `group`, `group-hover:`, `peer`, `peer-checked:` en componentes reales | Usa `group-hover:` correctamente pero desconoce `peer` | No conoce `group` ni `peer` |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Borders** | Card con bordes, redondeados, dividers y outline de focus completamente correctos | Card con bordes y rounded funcionales, 1-2 detalles menores | Card sin bordes coherentes o con errores de radius |
| **Ejercicio Shadows** | Panel de sombras con escala visible, coloured shadows y hover que eleva la sombra | Sombras básicas aplicadas correctamente | Sombras aplicadas sin escala ni interacción |
| **Ejercicio Sizing** | Grid de componentes con `w-*`, `min-w`, `max-w`, aspect-ratio y viewport units correctos | Sizing básico correcto; 1-2 conflictos de overflow | Overflow no controlado o tamaños inconsistentes |
| **Ejercicio Estados** | Todos los estados (hover, focus, active, disabled, focus-visible) con feedback visual distinto y accesible | Estados hover y focus funcionan; falta disabled o active | Solo hover; sin feedback de focus para teclado |

---

## 📦 Producto (30%)

**Proyecto: Tarjeta de Producto con Interacciones**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Visual Base** | Border correcto, `rounded-xl`, sombra que eleva en hover, imagen con `object-cover` | Card visible con bordes y sombra; hover raro pero funcional | Sin bordes, sin sombra o sin rounded |
| **Sizing** | Ancho controlado `max-w-sm`, altura de imagen fija con `h-48`, texto con `truncate`/`line-clamp` | Tamaños básicos correctos; imagen con overflow visible | Sin control de tamaños; imagen deforma la tarjeta |
| **Estados completos** | Hover eleva (`shadow-lg`, escala), botón con todos los estados (hover/focus/active/disabled) | Hover y focus en botón; falta active o disabled | Solo hover; sin focus visible para teclado |
| **Group hover** | Usa `group` en la card para que la imagen haga zoom y el título cambie de color en hover | Usa `group-hover:` en al menos un elemento | No usa `group` |
| **Accesibilidad** | `focus-visible:ring-*` en botón, `alt` en imagen, contraste WCAG AA en todos los textos | `focus:ring-*` en botón; algún contraste bajo | Sin feedback de foco visible |

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
files["1-teoria/01-borders-y-rounded.md"] = '''# 🔲 Borders y Rounded en Tailwind

## 🎯 Objetivos

- Controlar bordes por lado, color y grosor
- Aplicar border-radius con la escala de Tailwind
- Usar outlines y rings para feedback visual
- Combinar bordes con colores del sistema

---

## 📋 Contenido

![Diagrama de borders, rounded y ring en Tailwind](../0-assets/01-borders-rounded.svg)

### 1. Border Width

```html
<!-- Aplicar borde (requiere border-width + border-color) -->
<div class="border">1px en todos los lados (default: gray-200)</div>
<div class="border-2">2px</div>
<div class="border-4">4px</div>
<div class="border-8">8px</div>
<div class="border-0">Sin borde</div>

<!-- Por lado -->
<div class="border-t">Solo top</div>
<div class="border-b">Solo bottom</div>
<div class="border-l">Solo left</div>
<div class="border-r">Solo right</div>
<div class="border-x">Left + Right</div>
<div class="border-y">Top + Bottom</div>

<!-- Con color -->
<div class="border border-gray-200">Borde sutil</div>
<div class="border border-sky-500">Borde de acento</div>
<div class="border-2 border-red-400">Borde de error</div>

<!-- Borde solo abajo (divider) -->
<div class="border-b border-gray-100 pb-4 mb-4">Sección con divider</div>
```

---

### 2. Border Radius

```html
<!-- Escala completa -->
<div class="rounded-sm">rounded-sm — 2px</div>
<div class="rounded">rounded — 4px (default)</div>
<div class="rounded-md">rounded-md — 6px</div>
<div class="rounded-lg">rounded-lg — 8px · cards comunes</div>
<div class="rounded-xl">rounded-xl — 12px · cards modernas</div>
<div class="rounded-2xl">rounded-2xl — 16px · cards grandes</div>
<div class="rounded-3xl">rounded-3xl — 24px · modals, sheets</div>
<div class="rounded-full">rounded-full — 9999px · pills, avatars, badges</div>
<div class="rounded-none">Sin radio</div>

<!-- Por lado / esquina -->
<div class="rounded-t-xl">Solo esquinas superiores</div>
<div class="rounded-b-lg">Solo esquinas inferiores</div>
<div class="rounded-tl-2xl">Solo esquina top-left</div>

<!-- Patrón: imagen en card con top rounded -->
<div class="overflow-hidden rounded-xl">
  <img class="w-full" src="..." alt="..." />  <!-- imagen no desborda las esquinas -->
</div>
```

**Reglas prácticas:**
- Botones → `rounded-md` o `rounded-lg`
- Cards → `rounded-xl` o `rounded-2xl`
- Pills / badges → `rounded-full`
- Avatares circulares → `rounded-full`
- Inputs → `rounded-lg`

---

### 3. Outline vs Ring vs Border

```html
<!-- Border: ocupa espacio en el layout (afecta box model) -->
<div class="border-2 border-sky-500">Border visible</div>

<!-- Ring: no ocupa espacio (usa box-shadow con offset) — ideal para focus -->
<button class="ring-2 ring-sky-500">Ring visible</button>
<button class="ring-2 ring-sky-500 ring-offset-2">Ring con offset blanco</button>

<!-- Outline: similar a ring pero más básico -->
<button class="outline outline-2 outline-sky-500">Outline</button>
<button class="outline-none focus:outline-none">Sin outline (cuidado: accesibilidad)</button>
```

**Regla de oro:** Usa `focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2` en botones e inputs para feedback de teclado sin afectar el mouse.

---

### 4. Divide (separadores entre hijos)

```html
<!-- divide-y añade border-top a todos los hijos excepto el primero -->
<ul class="divide-y divide-gray-100">
  <li class="py-3">Item 1</li>
  <li class="py-3">Item 2</li>
  <li class="py-3">Item 3</li>
</ul>

<!-- divide-x para columnas -->
<div class="flex divide-x divide-gray-200">
  <div class="px-6">Columna 1</div>
  <div class="px-6">Columna 2</div>
</div>
```

---

## ✅ Checklist de Verificación

- [ ] Uso `border border-gray-200` (no solo `border`) para bordes visibles
- [ ] Los cards tienen `overflow-hidden rounded-xl` para contener imágenes correctamente
- [ ] Los botones tienen `focus-visible:ring-2` (no `focus:ring-2`) para accesibilidad de teclado
- [ ] Uso `divide-y` en listas para separadores más limpios que margin/padding
'''

files["1-teoria/02-shadows.md"] = '''# 🌒 Shadows en Tailwind

## 🎯 Objetivos

- Dominar la escala de box-shadow
- Usar sombras de color para efectos modernos
- Implementar el patrón de "elevación" con hover
- Conocer drop-shadow para elementos sin fondo

---

## 📋 Contenido

### 1. Box Shadow — Escala de Elevación

```html
<!-- Escala completa de sombras -->
<div class="shadow-none">Sin sombra</div>
<div class="shadow-sm">shadow-sm — sombra casi imperceptible (inputs, dividers)</div>
<div class="shadow">shadow — sombra suave (cards base)</div>
<div class="shadow-md">shadow-md — sombra media (cards hover, dropdowns)</div>
<div class="shadow-lg">shadow-lg — sombra pronunciada (modals, tooltips)</div>
<div class="shadow-xl">shadow-xl — sombra grande (drawers, panels flotantes)</div>
<div class="shadow-2xl">shadow-2xl — sombra máxima (sheets, colores vivos)</div>
<div class="shadow-inner">shadow-inner — sombra hacia adentro (inputs activos)</div>
```

---

### 2. Elevación con Hover

El patrón más común: la card "sube" al hacer hover aumentando la sombra y/o la escala.

```html
<!-- Patrón de elevación -->
<div class="shadow-sm transition-shadow duration-200 hover:shadow-md">
  Card con elevación suave
</div>

<!-- Elevación con escala -->
<div class="shadow transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5">
  Card que sube ligeramente
</div>

<!-- Elevación completa con group -->
<div class="group shadow-sm transition-all duration-300 hover:shadow-xl rounded-2xl">
  <img class="transition-transform duration-300 group-hover:scale-105" src="..." alt="..." />
  <div class="p-4">
    <h3 class="text-gray-900 group-hover:text-sky-600 transition-colors">Título</h3>
  </div>
</div>
```

---

### 3. Sombras de Color

Una de las características más potentes de Tailwind v3+: sombras coloreadas.

```html
<!-- Sombras coloreadas -->
<button class="bg-sky-500 text-white shadow-lg shadow-sky-500/50 hover:shadow-sky-500/80">
  Botón con sombra de color
</button>

<button class="bg-violet-600 text-white shadow-lg shadow-violet-600/40">
  Botón violet con glow
</button>

<div class="rounded-xl bg-emerald-500 p-4 shadow-xl shadow-emerald-500/30">
  Card con sombra verde
</div>
```

La sintaxis `shadow-{color}/{opacidad}` combina el color con la sombra base.

---

### 4. Drop Shadow (para elementos sin fondo)

`drop-shadow-*` usa CSS `filter: drop-shadow()` — funciona con PNGs transparentes e íconos SVG.

```html
<!-- drop-shadow en SVG/PNG transparente -->
<img class="drop-shadow-md" src="icon.svg" alt="Ícono con sombra" />

<!-- drop-shadow en texto -->
<h1 class="text-5xl font-black text-white drop-shadow-lg">
  Título con sombra
</h1>

<!-- Escala: drop-shadow-sm, drop-shadow, drop-shadow-md, drop-shadow-lg, drop-shadow-xl, drop-shadow-2xl -->
```

**Diferencia `shadow` vs `drop-shadow`:**
- `shadow-*` → box-shadow, aplica al bounding box del elemento
- `drop-shadow-*` → filter drop-shadow, sigue la forma real del contenido (SVG, PNG transparente)

---

### 5. Patrones de Uso por Componente

| Componente | Sombra base | Sombra hover |
|-----------|------------|-------------|
| Card | `shadow-sm` | `shadow-md` o `shadow-lg` |
| Modal | `shadow-2xl` | — |
| Dropdown | `shadow-lg` | — |
| Input base | `shadow-sm` | — |
| Input focus | → `shadow-inner` | — |
| Botón primario | `shadow-sm` | `shadow-md shadow-{color}/50` |
| Tooltip | `shadow-lg` | — |

---

## ✅ Checklist de Verificación

- [ ] Mis cards tienen `shadow-sm` base y `hover:shadow-md` o mayor
- [ ] Uso `transition-shadow duration-200` para que la transición sea suave
- [ ] Los botones importantes tienen `shadow-{color}/50` para efecto glow
- [ ] Entiendo cuándo `drop-shadow-*` es mejor que `shadow-*`
'''

files["1-teoria/03-sizing.md"] = '''# 📏 Sizing en Tailwind

## 🎯 Objetivos

- Dominar width y height con la escala de Tailwind
- Usar min/max-width y min/max-height correctamente
- Entender los valores especiales: full, screen, fit, auto, svh
- Controlar aspect-ratio y object-fit

---

## 📋 Contenido

### 1. Width y Height — Escala Numérica

La misma escala que spacing (1 = 4px):

```html
<!-- Tamaños fijos -->
<div class="w-4 h-4">16×16px — ícono pequeño</div>
<div class="w-6 h-6">24×24px — ícono medium</div>
<div class="w-8 h-8">32×32px — ícono large</div>
<div class="w-10 h-10">40×40px — avatar small</div>
<div class="w-12 h-12">48×48px — avatar medium</div>
<div class="w-16 h-16">64×64px — avatar large</div>
<div class="w-24 h-24">96×96px</div>
<div class="w-32 h-32">128×128px</div>
<div class="w-48 h-48">192×192px</div>
<div class="w-64 h-64">256×256px</div>
```

---

### 2. Valores Especiales

```html
<!-- Porcentajes -->
<div class="w-1/2">50% del padre</div>
<div class="w-1/3">33.33%</div>
<div class="w-2/3">66.66%</div>
<div class="w-1/4">25%</div>
<div class="w-3/4">75%</div>

<!-- full vs screen -->
<div class="w-full">100% del contenedor padre</div>
<div class="w-screen">100vw (ancho del viewport)</div>
<div class="h-full">100% del alto del padre</div>
<div class="h-screen">100vh</div>
<div class="h-svh">100svh (small viewport height — móvil sin la barra del browser)</div>
<div class="h-dvh">100dvh (dynamic viewport height)</div>

<!-- fit-content -->
<div class="w-fit">Ancho según el contenido</div>
<div class="h-fit">Alto según el contenido</div>

<!-- auto -->
<div class="w-auto">Auto (default para la mayoría)</div>
<div class="mx-auto">Centrar horizontalmente</div>
```

---

### 3. Min y Max Width/Height

```html
<!-- Max width — el más usado para contenedores -->
<div class="max-w-sm">Max 384px</div>
<div class="max-w-md">Max 448px</div>
<div class="max-w-lg">Max 512px</div>
<div class="max-w-xl">Max 576px</div>
<div class="max-w-2xl">Max 672px · prose/texto</div>
<div class="max-w-4xl">Max 896px</div>
<div class="max-w-7xl">Max 1280px · layout de página</div>
<div class="max-w-full">Max 100% del padre</div>
<div class="max-w-none">Sin límite de ancho</div>

<!-- Min width -->
<div class="min-w-0">min-width: 0 (necesario en flex para que truncate funcione)</div>
<div class="min-w-full">min-width: 100%</div>

<!-- Min height -->
<div class="min-h-screen">Mínimo 100vh (para páginas que ocupan todo)</div>
<div class="min-h-0">reset</div>

<!-- Max height -->
<div class="max-h-64">Max height 256px (scroll containers)</div>
<div class="max-h-screen">Max 100vh</div>
<div class="overflow-y-auto max-h-96">Lista scrollable</div>
```

---

### 4. Aspect Ratio

```html
<!-- Relaciones de aspecto —  mantiene proporciones al cambiar ancho -->
<div class="aspect-square">1:1 (cuadrado)</div>
<div class="aspect-video">16:9 (video)</div>
<div class="aspect-[4/3]">4:3 arbitrario</div>

<!-- Caso de uso: thumbnail de video -->
<div class="aspect-video w-full overflow-hidden rounded-lg">
  <img class="h-full w-full object-cover" src="thumbnail.jpg" alt="Video thumb" />
</div>

<!-- Avatar cuadrado que siempre mantiene proporción -->
<div class="aspect-square w-12 overflow-hidden rounded-full">
  <img class="h-full w-full object-cover" src="avatar.jpg" alt="Avatar" />
</div>
```

---

### 5. Object Fit y Object Position

```html
<!-- object-cover: rellena el contenedor recortando (el más común) -->
<img class="h-48 w-full object-cover" src="..." alt="..." />

<!-- object-contain: encuadra el contenido sin recortar -->
<img class="h-48 w-full object-contain" src="..." alt="Logo" />

<!-- object-fill: deforma la imagen para que llene exactamente -->
<img class="h-32 w-full object-fill" src="..." alt="..." />

<!-- object-none: tamaño natural (sin escalar) -->
<img class="h-32 w-32 object-none object-center" src="..." alt="..." />

<!-- Posición de foco -->
<img class="h-48 w-full object-cover object-top" src="portrait.jpg" alt="Retrato" />
<img class="h-48 w-full object-cover object-center" src="landscape.jpg" alt="Paisaje" />
```

---

## ✅ Checklist de Verificación

- [ ] Uso `max-w-*` en contenedores, no `w-*` fijo en elementos responsive
- [ ] Las imágenes en cards tienen `h-48 w-full object-cover`
- [ ] Cuando uso `truncate` en flex, pongo `min-w-0` en el elemento padre flex
- [ ] Uso `aspect-video` o `aspect-square` para mantener proporciones de media
- [ ] Uso `min-h-screen` en el body/wrapper para páginas que deben llenar la pantalla
'''

files["1-teoria/04-estados-interactivos.md"] = '''# 🎯 Estados Interactivos en Tailwind

## 🎯 Objetivos

- Aplicar todos los estados pseudo-class de CSS con variantes de Tailwind
- Distinguir `focus` vs `focus-visible` para accesibilidad
- Implementar estados `disabled` correctamente
- Entender `aria-*` variantes

---

## 📋 Contenido

### 1. Hover

```html
<!-- Hover básico -->
<button class="bg-sky-500 hover:bg-sky-600">Hover cambia fondo</button>
<a class="text-gray-600 hover:text-gray-900">Hover oscurece texto</a>

<!-- Hover con múltiples propiedades -->
<div class="
  rounded-xl border border-gray-200 bg-white shadow-sm
  hover:border-sky-200 hover:shadow-md hover:-translate-y-0.5
  transition-all duration-200
">
  Card con hover completo
</div>

<!-- Hover con opacity -->
<button class="opacity-100 hover:opacity-80 transition-opacity">
  Fade on hover
</button>
```

---

### 2. Focus y Focus-Visible

```html
<!-- focus: activa con click Y con teclado -->
<input class="border border-gray-200 focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20 outline-none rounded-lg px-3 py-2" />

<!-- focus-visible: SOLO activa con teclado (sin anillo con mouse) -->
<button class="rounded-lg bg-sky-500 px-4 py-2 text-white outline-none
  focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2">
  Botón accesible
</button>

<!-- focus-within: el padre reacciona cuando un hijo tiene foco *)
<label class="block rounded-lg border border-gray-200 p-3
  focus-within:border-sky-500 focus-within:ring-1 focus-within:ring-sky-500/30">
  <span class="text-sm text-gray-600">Email</span>
  <input class="block w-full outline-none mt-1" type="email" />
</label>
```

**¿Cuándo usar cada uno?**
- `focus:` → en inputs, donde quieres feedback visual siempre
- `focus-visible:` → en botones, para no mostrar el anillo al hacer click con mouse
- `focus-within:` → en labels/wrappers de input

---

### 3. Active

```html
<!-- Active: mientras el botón está siendo presionado -->
<button class="
  bg-sky-500 hover:bg-sky-600 active:bg-sky-700 active:scale-95
  transition-all duration-75
  text-white px-4 py-2 rounded-lg
">
  Botón responsive al click
</button>

<!-- Link activo -->
<a class="text-gray-600 hover:text-sky-600 active:text-sky-800">Link</a>
```

---

### 4. Disabled

```html
<!-- Botón deshabilitado -->
<button
  disabled
  class="bg-sky-500 text-white px-4 py-2 rounded-lg
         disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none"
>
  Enviando...
</button>

<!-- Input deshabilitado -->
<input
  disabled
  class="border border-gray-200 rounded-lg px-3 py-2
         disabled:bg-gray-50 disabled:text-gray-400 disabled:cursor-not-allowed"
  value="Valor no editable"
/>

<!-- aria-disabled (para elementos que no admiten el atributo disabled) -->
<div
  role="button"
  aria-disabled="true"
  class="aria-disabled:opacity-50 aria-disabled:cursor-not-allowed"
>
  Elemento con aria-disabled
</div>
```

---

### 5. Checked, Selected, Required

```html
<!-- Checkbox con peer — el label reacciona al estado del input -->
<label class="flex items-center gap-2 cursor-pointer">
  <input type="checkbox" class="peer sr-only" />
  <div class="h-5 w-5 rounded border border-gray-300 bg-white
              peer-checked:bg-sky-500 peer-checked:border-sky-500
              transition-colors">
    <!-- custom checkbox visual -->
  </div>
  <span class="text-sm text-gray-700 peer-checked:text-gray-900 peer-checked:font-medium">
    Acepto los términos
  </span>
</label>

<!-- Input requerido -->
<input
  required
  class="border border-gray-200 rounded-lg px-3 py-2
         required:border-red-300 invalid:border-red-400"
  type="email"
  placeholder="correo@ejemplo.com"
/>
```

---

### 6. Group — Reaccionar al Hover del Padre

```html
<!-- group en el padre, group-hover: en los hijos -->
<article class="group relative overflow-hidden rounded-2xl bg-white shadow-sm hover:shadow-xl transition-shadow">

  <!-- La imagen hace zoom cuando la card hace hover -->
  <div class="overflow-hidden">
    <img
      class="h-48 w-full object-cover transition-transform duration-500 group-hover:scale-110"
      src="..."
      alt="..."
    />
  </div>

  <!-- Overlay que aparece al hacer hover -->
  <div class="absolute inset-0 bg-sky-900/0 group-hover:bg-sky-900/20 transition-colors duration-300"></div>

  <div class="p-5">
    <!-- El título cambia de color en hover de la card -->
    <h3 class="font-semibold text-gray-900 group-hover:text-sky-600 transition-colors">
      Título del artículo
    </h3>
    <!-- La flecha aparece en hover -->
    <span class="mt-2 inline-block translate-x-0 opacity-0 text-sky-500 transition-all group-hover:translate-x-1 group-hover:opacity-100">
      Leer más →
    </span>
  </div>
</article>
```

---

## ✅ Checklist de Verificación

- [ ] Todos mis botones tienen `focus-visible:ring-2 focus-visible:ring-{color} focus-visible:ring-offset-2`
- [ ] Los inputs tienen `focus:border-{color} focus:ring-2 focus:ring-{color}/20 outline-none`
- [ ] Los botones deshabilitados tienen `disabled:opacity-50 disabled:cursor-not-allowed`
- [ ] Uso `group` + `group-hover:` para interacciones complejas padre-hijo
- [ ] Mis transiciones tienen `transition-*` y `duration-200` o similar
'''

files["1-teoria/05-group-peer-y-transiciones.md"] = '''# 🔗 Group, Peer y Transiciones

## 🎯 Objetivos

- Usar `group` y `group-hover:` para interacciones padre-hijo
- Aplicar `peer` para que un elemento reaccione al estado de un sibling
- Implementar transiciones suaves con `transition-*` y `duration-*`
- Entender `transform` y sus utilidades

---

## 📋 Contenido

### 1. Group — Interacción Padre-Hijo

```html
<!-- Añadir "group" al padre, usar "group-hover:" en hijos -->
<div class="group cursor-pointer rounded-xl p-4 hover:bg-sky-50 transition-colors">
  <h3 class="font-semibold text-gray-900 group-hover:text-sky-600 transition-colors">
    Título
  </h3>
  <p class="text-sm text-gray-500">Descripción</p>
  <!-- Icono que aparece con hover -->
  <svg class="w-4 h-4 text-gray-300 opacity-0 group-hover:opacity-100 transition-opacity">...</svg>
</div>

<!-- Groups anidados con nombre -->
<div class="group/card hover:bg-sky-50">
  <div class="group/item">
    <!-- reacciona a hover de group/item -->
    <span class="group-hover/item:text-sky-600">Item level</span>
    <!-- reacciona a hover de group/card -->
    <span class="group-hover/card:text-emerald-600">Card level</span>
  </div>
</div>
```

---

### 2. Peer — Elemento Sibling Reactivo

`peer` marca el elemento de referencia, `peer-*:` se aplica al siguiente sibling.

```html
<!-- Toggle switch accesible con peer -->
<label class="flex items-center gap-3 cursor-pointer">
  <input type="checkbox" class="peer sr-only" />
  <div class="
    relative h-6 w-11 rounded-full bg-gray-200
    peer-checked:bg-sky-500
    after:absolute after:top-0.5 after:left-0.5
    after:h-5 after:w-5 after:rounded-full after:bg-white after:shadow
    after:transition-transform
    peer-checked:after:translate-x-5
    transition-colors
  "></div>
  <span class="text-sm text-gray-700 peer-checked:font-semibold peer-checked:text-gray-900">
    Notificaciones activas
  </span>
</label>

<!-- Validación de input con peer -->
<div>
  <input
    type="email"
    class="peer w-full rounded-lg border border-gray-200 px-3 py-2 outline-none
           focus:border-sky-500 invalid:border-red-400"
    placeholder="correo@ejemplo.com"
    required
  />
  <!-- Este mensaje solo aparece cuando el input es inválido Y tiene foco -->
  <p class="mt-1 hidden text-xs text-red-500 peer-invalid:peer-focus:block">
    Ingresa un correo válido
  </p>
</div>
```

---

### 3. Transiciones

```html
<!-- transition-all: anima todas las propiedades cambiadas (evitar en prod) -->
<div class="transition-all duration-300">...</div>

<!-- Más específico (mejor rendimiento) -->
<div class="transition-colors duration-200">Solo anima color</div>
<div class="transition-shadow duration-200">Solo sombra</div>
<div class="transition-transform duration-300">Solo transform</div>
<div class="transition-opacity duration-150">Solo opacidad</div>

<!-- Timing functions -->
<div class="transition-transform duration-300 ease-in">ease-in</div>
<div class="transition-transform duration-300 ease-out">ease-out (más natural)</div>
<div class="transition-transform duration-300 ease-in-out">ease-in-out</div>

<!-- Delay -->
<div class="transition-opacity duration-300 delay-150">Espera 150ms antes de iniciar</div>
```

---

### 4. Transform

```html
<!-- Escala -->
<div class="hover:scale-105 transition-transform">Escala al 105% en hover</div>
<div class="hover:scale-95 transition-transform">Escala al 95% (presionado)</div>

<!-- Traslación -->
<div class="hover:-translate-y-1 transition-transform">Sube 4px en hover</div>
<div class="hover:translate-x-1 transition-transform">Mueve 4px a la derecha</div>

<!-- Rotación -->
<svg class="hover:rotate-45 transition-transform duration-300">...</svg>

<!-- Combinado: card que sube y gana sombra -->
<div class="
  shadow-sm rounded-xl
  hover:-translate-y-1 hover:shadow-md
  transition-all duration-200
">
  Card elevada
</div>
```

---

### 5. Patrón Completo: Card Interactiva

```html
<article class="
  group
  overflow-hidden rounded-2xl border border-gray-100 bg-white
  shadow-sm hover:shadow-xl
  transition-all duration-300
  cursor-pointer
">
  <!-- Imagen con zoom -->
  <div class="overflow-hidden">
    <img
      class="h-48 w-full object-cover
             transition-transform duration-500
             group-hover:scale-110"
      src="cover.jpg"
      alt="Artículo"
    />
  </div>

  <div class="p-5">
    <!-- Badge de categoría -->
    <span class="text-xs font-semibold uppercase tracking-wider text-sky-600">
      Tutorial
    </span>

    <!-- Título que cambia de color -->
    <h2 class="mt-2 text-lg font-bold text-gray-900
               group-hover:text-sky-600
               transition-colors duration-200
               line-clamp-2">
      Título del artículo
    </h2>

    <!-- Flecha que se mueve -->
    <div class="mt-4 flex items-center gap-1 text-sm font-medium text-sky-500
                translate-x-0 opacity-0
                group-hover:translate-x-1 group-hover:opacity-100
                transition-all duration-200">
      Leer más →
    </div>
  </div>
</article>
```

---

## ✅ Checklist de Verificación

- [ ] Uso `group` + `group-hover:` para interacciones en cards y listas
- [ ] Mis transiciones son específicas (`transition-colors`, no `transition-all`) cuando es posible
- [ ] Uso `peer` + `peer-checked:` para custom checkboxes y toggles
- [ ] Las animaciones tienen `duration-200` a `duration-300` (no más largas en UI)
- [ ] El `transform` en hover usa `transition-transform duration-200` para suavidad
'''

# ─────────────────────────────────────────────────────────────────────────────
# EJERCICIOS
# ─────────────────────────────────────────────────────────────────────────────
files["2-practicas/01-ejercicio-borders/README.md"] = '''# Ejercicio 01: Bordes y Redondeados

## 🎯 Objetivo

Explorar bordes, border-radius, rings y dividers construyendo componentes UI reales.

---

## 📋 Instrucciones

### Paso 1: Escala de border-radius

Descomenta el **bloque 1** para ver la escala visual completa de `rounded-*`.

### Paso 2: Card con bordes y overflow-hidden

Descomenta el **bloque 2** para construir una card que usa `overflow-hidden rounded-xl` para contener correctamente una imagen.

### Paso 3: Lista con dividers

Descomenta el **bloque 3** para ver cómo `divide-y` reemplaza los margin-top por separadores limpios.

### Paso 4: Ring de foco accesible

Descomenta el **bloque 4** para implementar el patrón correcto de `focus-visible:ring-*` en botones e inputs.

---

## ✅ Verificación

- Las imágenes dentro de cards no desbordan el border-radius
- El ring de focus solo aparece al navegar con teclado (Tab), no al hacer click
- Los dividers en la lista son uniformes y más limpios que margin-top individual
'''

files["2-practicas/01-ejercicio-borders/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 01 — Borders y Rounded</title>
  </head>
  <body class="min-h-screen bg-gray-50 p-8 font-sans">
    <h1 class="mb-8 text-2xl font-bold text-gray-900">Borders y Rounded</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Escala visual de border-radius     -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-10">                                                                                         -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Escala rounded-*</h2>        -->
    <!--   <div class="flex flex-wrap items-center gap-4">                                                               -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-none flex items-center justify-center">   -->
    <!--       <span class="text-xs text-sky-700">none</span>                                                           -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-sm flex items-center justify-center">     -->
    <!--       <span class="text-xs text-sky-700">sm</span>                                                             -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded flex items-center justify-center">        -->
    <!--       <span class="text-xs text-sky-700">base</span>                                                           -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-md flex items-center justify-center">     -->
    <!--       <span class="text-xs text-sky-700">md</span>                                                             -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-lg flex items-center justify-center">     -->
    <!--       <span class="text-xs text-sky-700">lg</span>                                                             -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-xl flex items-center justify-center">     -->
    <!--       <span class="text-xs text-sky-700">xl</span>                                                             -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-2xl flex items-center justify-center">    -->
    <!--       <span class="text-xs text-sky-700">2xl</span>                                                            -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-3xl flex items-center justify-center">    -->
    <!--       <span class="text-xs text-sky-700">3xl</span>                                                            -->
    <!--     </div>                                                                                                      -->
    <!--     <div class="h-16 w-16 border-2 border-sky-400 bg-sky-50 rounded-full flex items-center justify-center">   -->
    <!--       <span class="text-xs text-sky-700">full</span>                                                           -->
    <!--     </div>                                                                                                      -->
    <!--   </div>                                                                                                        -->
    <!-- </section>                                                                                                      -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Card con overflow-hidden           -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                         -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Card con overflow-hidden</h2> -->
    <!--   <div class="flex gap-6">                                                                                       -->
    <!--                                                                                                                  -->
    <!--     overflow-hidden correcto                                                                                     -->
    <!--     <div class="w-48 overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">                    -->
    <!--       <div class="h-28 bg-gradient-to-br from-sky-400 to-sky-600"></div>                                       -->
    <!--       <div class="p-3">                                                                                          -->
    <!--         <p class="text-sm font-medium">overflow-hidden ✓</p>                                                   -->
    <!--         <p class="text-xs text-gray-500">La imagen respeta el rounded</p>                                      -->
    <!--       </div>                                                                                                     -->
    <!--     </div>                                                                                                       -->
    <!--                                                                                                                  -->
    <!--     sin overflow-hidden — las esquinas de la imagen sobresalen                                                  -->
    <!--     <div class="w-48 rounded-xl border border-gray-200 bg-white shadow-sm">                                    -->
    <!--       <div class="h-28 bg-gradient-to-br from-red-400 to-red-600"></div>                                       -->
    <!--       <div class="p-3">                                                                                          -->
    <!--         <p class="text-sm font-medium">sin overflow-hidden ✗</p>                                               -->
    <!--         <p class="text-xs text-gray-500">Las esquinas sobresalen</p>                                           -->
    <!--       </div>                                                                                                     -->
    <!--     </div>                                                                                                       -->
    <!--   </div>                                                                                                         -->
    <!-- </section>                                                                                                       -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Lista con divide-y                 -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                        -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Lista con divide-y</h2>     -->
    <!--   <div class="max-w-md rounded-xl border border-gray-200 bg-white shadow-sm">                                 -->
    <!--     <ul class="divide-y divide-gray-100">                                                                      -->
    <!--       <li class="flex items-center gap-3 px-4 py-3">                                                          -->
    <!--         <div class="h-8 w-8 rounded-full bg-sky-100 flex items-center justify-center text-sky-600 text-sm">A</div> -->
    <!--         <div>                                                                                                   -->
    <!--           <p class="text-sm font-medium text-gray-900">Ana García</p>                                         -->
    <!--           <p class="text-xs text-gray-500">Diseñadora UX</p>                                                  -->
    <!--         </div>                                                                                                  -->
    <!--       </li>                                                                                                     -->
    <!--       <li class="flex items-center gap-3 px-4 py-3">                                                          -->
    <!--         <div class="h-8 w-8 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600 text-sm">B</div> -->
    <!--         <div>                                                                                                   -->
    <!--           <p class="text-sm font-medium text-gray-900">Bruno López</p>                                        -->
    <!--           <p class="text-xs text-gray-500">Desarrollador Frontend</p>                                         -->
    <!--         </div>                                                                                                  -->
    <!--       </li>                                                                                                     -->
    <!--       <li class="flex items-center gap-3 px-4 py-3">                                                          -->
    <!--         <div class="h-8 w-8 rounded-full bg-violet-100 flex items-center justify-center text-violet-600 text-sm">C</div> -->
    <!--         <div>                                                                                                   -->
    <!--           <p class="text-sm font-medium text-gray-900">Carla Méndez</p>                                       -->
    <!--           <p class="text-xs text-gray-500">Product Manager</p>                                                -->
    <!--         </div>                                                                                                  -->
    <!--       </li>                                                                                                     -->
    <!--     </ul>                                                                                                       -->
    <!--   </div>                                                                                                        -->
    <!-- </section>                                                                                                      -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Focus ring accesible               -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                         -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Focus ring (navega con Tab)</h2> -->
    <!--   <p class="mb-4 text-sm text-gray-600">Haz click normalmente y luego presiona Tab para ver la diferencia.</p> -->
    <!--   <div class="flex flex-wrap gap-4">                                                                            -->
    <!--     <button class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-medium text-white outline-none                -->
    <!--       focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2 transition-shadow">         -->
    <!--       focus-visible:ring (solo teclado)                                                                         -->
    <!--     </button>                                                                                                   -->
    <!--     <input class="rounded-lg border border-gray-200 px-3 py-2 text-sm outline-none w-48                      -->
    <!--       focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20 transition-shadow"                              -->
    <!--       placeholder="Input con focus ring" />                                                                    -->
    <!--     <a href="#" class="rounded text-sky-600 underline outline-none                                             -->
    <!--       focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2">                           -->
    <!--       Link con focus visible                                                                                    -->
    <!--     </a>                                                                                                        -->
    <!--   </div>                                                                                                        -->
    <!-- </section>                                                                                                      -->

  </body>
</html>
'''

files["2-practicas/02-ejercicio-shadows/README.md"] = '''# Ejercicio 02: Sombras y Elevación

## 🎯 Objetivo

Explorar la escala de sombras de Tailwind y construir el patrón de elevación interactivo.

---

## 📋 Instrucciones

### Paso 1: Escala visual de shadow

Descomenta el **bloque 1** para ver la escala completa side-by-side.

### Paso 2: Elevación con hover

Descomenta el **bloque 2** para ver cards que "suben" con hover usando `hover:shadow-*` y `hover:-translate-y-*`.

### Paso 3: Sombras coloreadas

Descomenta el **bloque 3** para aplicar `shadow-{color}/{opacidad}` en botones con efecto glow.

### Paso 4: Drop shadow en SVG

Descomenta el **bloque 4** para comparar `shadow-*` vs `drop-shadow-*`.

---

## ✅ Verificación

- Puedes ver claramente la diferencia entre sm, md, lg, xl y 2xl
- La card tiene transición suave de elevación al hacer hover
- Los botones tienen efecto glow con sombra de color
'''

files["2-practicas/02-ejercicio-shadows/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 02 — Shadows</title>
  </head>
  <body class="min-h-screen bg-slate-100 p-8 font-sans">
    <h1 class="mb-8 text-2xl font-bold text-gray-900">Shadows y Elevación</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Escala de sombras                  -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-12">                                                                                            -->
    <!--   <h2 class="mb-6 text-sm font-semibold uppercase tracking-widest text-gray-400">Escala de box-shadow</h2>      -->
    <!--   <div class="flex flex-wrap gap-6">                                                                               -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                 -->
    <!--       <div class="h-20 w-32 rounded-xl bg-white shadow-none border border-gray-200"></div>                       -->
    <!--       <span class="text-xs text-gray-500">shadow-none</span>                                                     -->
    <!--     </div>                                                                                                          -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                 -->
    <!--       <div class="h-20 w-32 rounded-xl bg-white shadow-sm"></div>                                                -->
    <!--       <span class="text-xs text-gray-500">shadow-sm</span>                                                       -->
    <!--     </div>                                                                                                          -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                 -->
    <!--       <div class="h-20 w-32 rounded-xl bg-white shadow"></div>                                                   -->
    <!--       <span class="text-xs text-gray-500">shadow</span>                                                          -->
    <!--     </div>                                                                                                          -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                 -->
    <!--       <div class="h-20 w-32 rounded-xl bg-white shadow-md"></div>                                                -->
    <!--       <span class="text-xs text-gray-500">shadow-md</span>                                                       -->
    <!--     </div>                                                                                                          -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                 -->
    <!--       <div class="h-20 w-32 rounded-xl bg-white shadow-lg"></div>                                                -->
    <!--       <span class="text-xs text-gray-500">shadow-lg</span>                                                       -->
    <!--     </div>                                                                                                          -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                 -->
    <!--       <div class="h-20 w-32 rounded-xl bg-white shadow-xl"></div>                                                -->
    <!--       <span class="text-xs text-gray-500">shadow-xl</span>                                                       -->
    <!--     </div>                                                                                                          -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                 -->
    <!--       <div class="h-20 w-32 rounded-xl bg-white shadow-2xl"></div>                                               -->
    <!--       <span class="text-xs text-gray-500">shadow-2xl</span>                                                      -->
    <!--     </div>                                                                                                          -->
    <!--   </div>                                                                                                           -->
    <!-- </section>                                                                                                         -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Elevación con hover                -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12">                                                                                           -->
    <!--   <h2 class="mb-6 text-sm font-semibold uppercase tracking-widest text-gray-400">Elevación con hover (pasa el mouse)</h2> -->
    <!--   <div class="flex gap-6">                                                                                        -->
    <!--     <div class="w-44 cursor-pointer rounded-xl bg-white p-5 shadow-sm                                           -->
    <!--            hover:shadow-md hover:-translate-y-0.5 transition-all duration-200">                                  -->
    <!--       <p class="font-semibold text-gray-900">Suave</p>                                                           -->
    <!--       <p class="text-xs text-gray-500 mt-1">shadow-sm → md</p>                                                  -->
    <!--     </div>                                                                                                         -->
    <!--     <div class="w-44 cursor-pointer rounded-xl bg-white p-5 shadow                                              -->
    <!--            hover:shadow-xl hover:-translate-y-1 transition-all duration-200">                                    -->
    <!--       <p class="font-semibold text-gray-900">Pronunciado</p>                                                    -->
    <!--       <p class="text-xs text-gray-500 mt-1">shadow → xl</p>                                                     -->
    <!--     </div>                                                                                                         -->
    <!--     <div class="w-44 cursor-pointer rounded-xl bg-white p-5 shadow                                              -->
    <!--            hover:shadow-2xl hover:-translate-y-2 hover:scale-105 transition-all duration-300">                  -->
    <!--       <p class="font-semibold text-gray-900">Dramático</p>                                                       -->
    <!--       <p class="text-xs text-gray-500 mt-1">shadow → 2xl + scale</p>                                            -->
    <!--     </div>                                                                                                         -->
    <!--   </div>                                                                                                          -->
    <!-- </section>                                                                                                        -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Sombras de color                   -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12">                                                                                               -->
    <!--   <h2 class="mb-6 text-sm font-semibold uppercase tracking-widest text-gray-400">Sombras de color (glow)</h2>      -->
    <!--   <div class="flex flex-wrap gap-4">                                                                                  -->
    <!--     <button class="rounded-lg bg-sky-500 px-5 py-2.5 text-sm font-semibold text-white                              -->
    <!--       shadow-lg shadow-sky-500/50 hover:shadow-sky-500/75 transition-shadow">                                       -->
    <!--       Sky glow                                                                                                        -->
    <!--     </button>                                                                                                          -->
    <!--     <button class="rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white                           -->
    <!--       shadow-lg shadow-violet-600/40 hover:shadow-violet-600/60 transition-shadow">                                 -->
    <!--       Violet glow                                                                                                     -->
    <!--     </button>                                                                                                          -->
    <!--     <button class="rounded-lg bg-emerald-500 px-5 py-2.5 text-sm font-semibold text-white                          -->
    <!--       shadow-lg shadow-emerald-500/40 hover:shadow-emerald-500/60 transition-shadow">                               -->
    <!--       Emerald glow                                                                                                    -->
    <!--     </button>                                                                                                          -->
    <!--     <button class="rounded-lg bg-rose-500 px-5 py-2.5 text-sm font-semibold text-white                             -->
    <!--       shadow-lg shadow-rose-500/40 hover:shadow-rose-500/70 transition-shadow">                                     -->
    <!--       Rose glow                                                                                                       -->
    <!--     </button>                                                                                                          -->
    <!--   </div>                                                                                                               -->
    <!-- </section>                                                                                                             -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Shadow vs Drop-shadow              -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12">                                                                                            -->
    <!--   <h2 class="mb-6 text-sm font-semibold uppercase tracking-widest text-gray-400">shadow-* vs drop-shadow-*</h2> -->
    <!--   <div class="flex gap-8 items-start">                                                                             -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                  -->
    <!--       <div class="h-20 w-20 shadow-xl bg-white rounded-xl"></div>                                                  -->
    <!--       <span class="text-xs text-gray-500">shadow-xl (bounding box)</span>                                          -->
    <!--     </div>                                                                                                           -->
    <!--     <div class="flex flex-col items-center gap-2">                                                                  -->
    <!--       Simula SVG star con clip-path que drop-shadow sigue la forma                                                  -->
    <!--       <div class="h-20 w-20 drop-shadow-xl" style="clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); background: #38bdf8;"></div> -->
    <!--       <span class="text-xs text-gray-500">drop-shadow-xl (sigue forma)</span>                                     -->
    <!--     </div>                                                                                                          -->
    <!--   </div>                                                                                                            -->
    <!-- </section>                                                                                                          -->

  </body>
</html>
'''

files["2-practicas/03-ejercicio-sizing/README.md"] = '''# Ejercicio 03: Sizing — Widths, Heights y Aspect Ratio

## 🎯 Objetivo

Dominar el control de tamaños con `w-*`, `h-*`, `min/max-*` y `aspect-ratio`.

---

## 📋 Instrucciones

### Paso 1: Escala visual de widths

Descomenta el **bloque 1** para ver barras de ancho proporcional.

### Paso 2: Valores especiales

Descomenta el **bloque 2** para comparar `w-full`, `w-fit`, `w-screen`.

### Paso 3: Container con max-width

Descomenta el **bloque 3** para ver el patrón de contenedor centrado con distintos max-w.

### Paso 4: Aspect ratio en cards de media

Descomenta el **bloque 4** para ver thumbnails que mantienen proporciones correctamente.

---

## ✅ Verificación

- Los anchor de aspect-ratio no se deforman al cambiar el ancho de la pantalla
- El contenedor con max-w-7xl + mx-auto está centrado
- Entiendes cuándo usar `w-full` vs `max-w-*`
'''

files["2-practicas/03-ejercicio-sizing/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 03 — Sizing</title>
  </head>
  <body class="min-h-screen bg-gray-50 p-8 font-sans">
    <h1 class="mb-8 text-2xl font-bold text-gray-900">Sizing</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Escala visual de widths            -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-10">                                                                                       -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Escala de width</h2>       -->
    <!--   <div class="space-y-2">                                                                                     -->
    <!--     <div class="flex items-center gap-3">                                                                     -->
    <!--       <span class="w-16 text-right text-xs text-gray-400">w-1/4</span>                                      -->
    <!--       <div class="w-1/4 h-5 rounded bg-sky-300"></div>                                                       -->
    <!--       <span class="text-xs text-gray-400">25%</span>                                                         -->
    <!--     </div>                                                                                                    -->
    <!--     <div class="flex items-center gap-3">                                                                     -->
    <!--       <span class="w-16 text-right text-xs text-gray-400">w-1/2</span>                                      -->
    <!--       <div class="w-1/2 h-5 rounded bg-sky-400"></div>                                                       -->
    <!--       <span class="text-xs text-gray-400">50%</span>                                                         -->
    <!--     </div>                                                                                                    -->
    <!--     <div class="flex items-center gap-3">                                                                     -->
    <!--       <span class="w-16 text-right text-xs text-gray-400">w-3/4</span>                                      -->
    <!--       <div class="w-3/4 h-5 rounded bg-sky-500"></div>                                                       -->
    <!--       <span class="text-xs text-gray-400">75%</span>                                                         -->
    <!--     </div>                                                                                                    -->
    <!--     <div class="flex items-center gap-3">                                                                     -->
    <!--       <span class="w-16 text-right text-xs text-gray-400">w-full</span>                                     -->
    <!--       <div class="w-full h-5 rounded bg-sky-600"></div>                                                      -->
    <!--       <span class="text-xs text-gray-400">100% del padre</span>                                              -->
    <!--     </div>                                                                                                    -->
    <!--   </div>                                                                                                      -->
    <!-- </section>                                                                                                    -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Valores especiales                 -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                         -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Valores especiales</h2>    -->
    <!--   <div class="space-y-3">                                                                                      -->
    <!--     <div class="rounded bg-sky-100 p-3">                                                                      -->
    <!--       <span class="font-mono text-sm text-sky-800">w-full</span>                                             -->
    <!--       <span class="ml-2 text-xs text-gray-500">→ 100% del contenedor padre (se contrae si el padre es pequeño)</span> -->
    <!--     </div>                                                                                                     -->
    <!--     <div class="inline-block rounded bg-emerald-100 p-3">                                                    -->
    <!--       <span class="font-mono text-sm text-emerald-800">w-fit</span>                                         -->
    <!--       <span class="ml-2 text-xs text-gray-500">→ ancho = contenido</span>                                   -->
    <!--     </div>                                                                                                    -->
    <!--     <div>                                                                                                      -->
    <!--       <div class="rounded bg-amber-100 p-3">                                                                  -->
    <!--         <span class="font-mono text-sm text-amber-800">min-w-0</span>                                       -->
    <!--         <span class="ml-2 text-xs text-gray-500">→ necesario para truncate en flex</span>                   -->
    <!--       </div>                                                                                                   -->
    <!--       <div class="mt-2 flex items-center gap-2">                                                              -->
    <!--         <div class="min-w-0 flex-1 truncate rounded bg-gray-200 px-2 py-1 text-sm text-gray-700">           -->
    <!--           Este título muy largo sí se trunca porque el padre tiene min-w-0                                   -->
    <!--         </div>                                                                                               -->
    <!--         <span class="shrink-0 text-xs text-gray-400">meta</span>                                            -->
    <!--       </div>                                                                                                  -->
    <!--     </div>                                                                                                    -->
    <!--   </div>                                                                                                      -->
    <!-- </section>                                                                                                    -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: max-width containers               -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                           -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">max-width containers</h2>    -->
    <!--   <div class="space-y-3">                                                                                        -->
    <!--     <div class="mx-auto max-w-sm rounded-lg bg-sky-100 p-3 text-center text-xs font-medium text-sky-700">      -->
    <!--       max-w-sm · 384px · formularios, widgets                                                                    -->
    <!--     </div>                                                                                                        -->
    <!--     <div class="mx-auto max-w-xl rounded-lg bg-sky-200 p-3 text-center text-xs font-medium text-sky-800">      -->
    <!--       max-w-xl · 576px · modals                                                                                  -->
    <!--     </div>                                                                                                        -->
    <!--     <div class="mx-auto max-w-2xl rounded-lg bg-sky-300 p-3 text-center text-xs font-medium text-sky-900">     -->
    <!--       max-w-2xl · 672px · artículos de blog, prose                                                              -->
    <!--     </div>                                                                                                        -->
    <!--     <div class="mx-auto max-w-4xl rounded-lg bg-sky-400 p-3 text-center text-xs font-medium text-white">       -->
    <!--       max-w-4xl · 896px · dashboards medianos                                                                    -->
    <!--     </div>                                                                                                        -->
    <!--     <div class="mx-auto max-w-7xl rounded-lg bg-sky-600 p-3 text-center text-xs font-medium text-white">       -->
    <!--       max-w-7xl · 1280px · layout de página completo                                                            -->
    <!--     </div>                                                                                                        -->
    <!--   </div>                                                                                                          -->
    <!-- </section>                                                                                                        -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Aspect ratio                       -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                          -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Aspect Ratio</h2>            -->
    <!--   <div class="flex gap-4">                                                                                        -->
    <!--     <div class="w-36">                                                                                            -->
    <!--       <div class="aspect-square w-full overflow-hidden rounded-xl bg-sky-400"></div>                            -->
    <!--       <p class="mt-1 text-center text-xs text-gray-500">aspect-square (1:1)</p>                                -->
    <!--     </div>                                                                                                        -->
    <!--     <div class="w-48">                                                                                            -->
    <!--       <div class="aspect-video w-full overflow-hidden rounded-xl bg-violet-400"></div>                          -->
    <!--       <p class="mt-1 text-center text-xs text-gray-500">aspect-video (16:9)</p>                                -->
    <!--     </div>                                                                                                        -->
    <!--     <div class="w-40">                                                                                            -->
    <!--       <div class="aspect-[4/3] w-full overflow-hidden rounded-xl bg-emerald-400"></div>                        -->
    <!--       <p class="mt-1 text-center text-xs text-gray-500">aspect-[4/3]</p>                                       -->
    <!--     </div>                                                                                                        -->
    <!--   </div>                                                                                                          -->
    <!-- </section>                                                                                                        -->

  </body>
</html>
'''

files["2-practicas/04-ejercicio-estados/README.md"] = '''# Ejercicio 04: Estados Interactivos y Group/Peer

## 🎯 Objetivo

Implementar todos los estados de interacción de Tailwind (hover, focus, active, disabled) y los patrones group/peer.

---

## 📋 Instrucciones

### Paso 1: Sistema de botones con estados completos

Descomenta el **bloque 1** para ver botones con hover, focus-visible, active y disabled.

### Paso 2: Card con group-hover

Descomenta el **bloque 2** para implementar una card donde múltiples elementos reaccionan al hover de la card.

### Paso 3: Toggle con peer

Descomenta el **bloque 3** para crear un toggle switch usando `peer` + `peer-checked:`.

### Paso 4: Input con focus-within

Descomenta el **bloque 4** para ver cómo el label/wrapper reacciona cuando el input tiene foco.

---

## ✅ Verificación

- Los botones tienen feedback visual en todos los estados: hover, focus (teclado), active (click), disabled
- La card reacciona en múltiples puntos al mismo tiempo al hacer hover
- El toggle funciona visualmente al hacer click
- El label del input cambia al hacer focus dentro del campo
'''

files["2-practicas/04-ejercicio-estados/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 04 — Estados Interactivos</title>
  </head>
  <body class="min-h-screen bg-gray-50 p-8 font-sans">
    <h1 class="mb-8 text-2xl font-bold text-gray-900">Estados Interactivos</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Sistema de botones                 -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-10">                                                                                              -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Botones con estados completos</h2> -->
    <!--   <p class="mb-4 text-sm text-gray-500">Usa Tab para ver focus-visible, haz click para ver active, prueba el disabled.</p> -->
    <!--   <div class="flex flex-wrap gap-3">                                                                                  -->
    <!--                                                                                                                       -->
    <!--     Primario — todos los estados                                                                                      -->
    <!--     <button class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white outline-none                   -->
    <!--       hover:bg-sky-600                                                                                                -->
    <!--       active:bg-sky-700 active:scale-95                                                                              -->
    <!--       focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2                                   -->
    <!--       transition-all duration-150">                                                                                   -->
    <!--       Primario                                                                                                        -->
    <!--     </button>                                                                                                         -->
    <!--                                                                                                                       -->
    <!--     Secundario — outline style                                                                                        -->
    <!--     <button class="rounded-lg border border-gray-200 bg-white px-4 py-2 text-sm font-semibold text-gray-700 outline-none -->
    <!--       hover:border-gray-300 hover:bg-gray-50                                                                         -->
    <!--       active:bg-gray-100 active:scale-95                                                                             -->
    <!--       focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2                                   -->
    <!--       transition-all duration-150">                                                                                   -->
    <!--       Secundario                                                                                                      -->
    <!--     </button>                                                                                                         -->
    <!--                                                                                                                       -->
    <!--     Peligro                                                                                                           -->
    <!--     <button class="rounded-lg bg-red-500 px-4 py-2 text-sm font-semibold text-white outline-none                   -->
    <!--       hover:bg-red-600                                                                                                -->
    <!--       active:bg-red-700                                                                                               -->
    <!--       focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:ring-offset-2                                   -->
    <!--       transition-all duration-150">                                                                                   -->
    <!--       Eliminar                                                                                                        -->
    <!--     </button>                                                                                                         -->
    <!--                                                                                                                       -->
    <!--     Disabled                                                                                                          -->
    <!--     <button disabled class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white                      -->
    <!--       disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none">                                 -->
    <!--       Procesando...                                                                                                   -->
    <!--     </button>                                                                                                         -->
    <!--   </div>                                                                                                              -->
    <!-- </section>                                                                                                            -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Card con group-hover               -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                              -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Card con group (pasa el mouse)</h2> -->
    <!--   <article class="group max-w-xs cursor-pointer overflow-hidden rounded-2xl bg-white shadow-sm                    -->
    <!--     hover:shadow-xl transition-all duration-300">                                                                   -->
    <!--                                                                                                                      -->
    <!--     Imagen que hace zoom con group-hover                                                                             -->
    <!--     <div class="overflow-hidden">                                                                                   -->
    <!--       <div class="h-40 bg-gradient-to-br from-sky-400 to-violet-500                                               -->
    <!--         transition-transform duration-500 group-hover:scale-110">                                                  -->
    <!--       </div>                                                                                                        -->
    <!--     </div>                                                                                                           -->
    <!--                                                                                                                      -->
    <!--     <div class="p-5">                                                                                               -->
    <!--       Badge que gana color con group-hover                                                                          -->
    <!--       <span class="text-xs font-semibold uppercase tracking-wider text-gray-400                                    -->
    <!--         group-hover:text-sky-500 transition-colors">Tutorial</span>                                                -->
    <!--                                                                                                                      -->
    <!--       Título que cambia de color                                                                                    -->
    <!--       <h3 class="mt-1 font-bold text-gray-900 group-hover:text-sky-600 transition-colors">                        -->
    <!--         Título del artículo                                                                                          -->
    <!--       </h3>                                                                                                          -->
    <!--                                                                                                                      -->
    <!--       Flecha que aparece y se mueve                                                                                 -->
    <!--       <div class="mt-3 flex items-center gap-1 text-sm font-medium text-sky-500                                   -->
    <!--         translate-x-0 opacity-0 group-hover:translate-x-1 group-hover:opacity-100                                 -->
    <!--         transition-all duration-200">                                                                               -->
    <!--         Leer más →                                                                                                   -->
    <!--       </div>                                                                                                         -->
    <!--     </div>                                                                                                           -->
    <!--   </article>                                                                                                         -->
    <!-- </section>                                                                                                           -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Toggle con peer                    -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                              -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Toggle con peer</h2>             -->
    <!--   <div class="space-y-4">                                                                                            -->
    <!--     <label class="flex cursor-pointer items-center gap-3">                                                          -->
    <!--       <input type="checkbox" class="peer sr-only" />                                                               -->
    <!--       <div class="relative h-6 w-11 flex-shrink-0 rounded-full bg-gray-200                                        -->
    <!--         peer-checked:bg-sky-500                                                                                      -->
    <!--         after:absolute after:left-0.5 after:top-0.5                                                                -->
    <!--         after:h-5 after:w-5 after:rounded-full after:bg-white after:shadow                                         -->
    <!--         after:transition-transform after:duration-200                                                               -->
    <!--         peer-checked:after:translate-x-5                                                                            -->
    <!--         transition-colors duration-200">                                                                             -->
    <!--       </div>                                                                                                         -->
    <!--       <span class="text-sm text-gray-700 peer-checked:font-semibold peer-checked:text-gray-900 transition-all">   -->
    <!--         Notificaciones por email                                                                                     -->
    <!--       </span>                                                                                                        -->
    <!--     </label>                                                                                                         -->
    <!--                                                                                                                      -->
    <!--     <label class="flex cursor-pointer items-center gap-3">                                                          -->
    <!--       <input type="checkbox" class="peer sr-only" checked />                                                       -->
    <!--       <div class="relative h-6 w-11 flex-shrink-0 rounded-full bg-gray-200                                        -->
    <!--         peer-checked:bg-emerald-500                                                                                  -->
    <!--         after:absolute after:left-0.5 after:top-0.5                                                                -->
    <!--         after:h-5 after:w-5 after:rounded-full after:bg-white after:shadow                                         -->
    <!--         after:transition-transform after:duration-200                                                               -->
    <!--         peer-checked:after:translate-x-5                                                                            -->
    <!--         transition-colors duration-200">                                                                             -->
    <!--       </div>                                                                                                         -->
    <!--       <span class="text-sm text-gray-700 peer-checked:font-semibold peer-checked:text-gray-900 transition-all">   -->
    <!--         Modo oscuro automático                                                                                       -->
    <!--       </span>                                                                                                        -->
    <!--     </label>                                                                                                         -->
    <!--   </div>                                                                                                             -->
    <!-- </section>                                                                                                           -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Input con focus-within             -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                              -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Input con focus-within</h2>     -->
    <!--   <div class="max-w-sm space-y-4">                                                                                  -->
    <!--     <label class="block cursor-text rounded-xl border border-gray-200 bg-white px-4 py-3                          -->
    <!--       focus-within:border-sky-500 focus-within:ring-2 focus-within:ring-sky-500/20                               -->
    <!--       transition-all duration-200">                                                                                -->
    <!--       <span class="block text-xs font-medium text-gray-500 focus-within:text-sky-600 transition-colors">Nombre</span> -->
    <!--       <input class="mt-0.5 block w-full text-sm text-gray-900 outline-none" type="text" placeholder="Ana García" /> -->
    <!--     </label>                                                                                                         -->
    <!--     <label class="block cursor-text rounded-xl border border-gray-200 bg-white px-4 py-3                          -->
    <!--       focus-within:border-sky-500 focus-within:ring-2 focus-within:ring-sky-500/20                               -->
    <!--       transition-all duration-200">                                                                                -->
    <!--       <span class="block text-xs font-medium text-gray-500">Email</span>                                           -->
    <!--       <input class="mt-0.5 block w-full text-sm text-gray-900 outline-none" type="email" placeholder="correo@ejemplo.com" /> -->
    <!--     </label>                                                                                                         -->
    <!--   </div>                                                                                                             -->
    <!-- </section>                                                                                                           -->

  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# PROYECTO
# ─────────────────────────────────────────────────────────────────────────────
files["3-proyecto/tarjeta-producto-interactiva/README.md"] = '''# Proyecto Semana 4: Tarjeta de Producto Interactiva

## 📋 Descripción

Construye una **tarjeta de producto** completamente interactiva usando los sistemas de borders, shadows, sizing y estados de TailwindCSS. La tarjeta debe sentirse viva al interactuar con ella.

---

## 🎯 Objetivos

- Aplicar bordes, rounded y sombras de forma contextual
- Implementar transición de elevación en hover
- Usar `group` para interacciones complejas padre-hijo
- Asegurar todos los estados del botón (hover/focus/active/disabled)

---

## 📐 Estructura esperada

```
┌────────────────────────────────┐
│  [Imagen con zoom en hover]    │  ← group-hover:scale-110
│  [Badge de categoría]          │
├────────────────────────────────┤
│  Nombre del producto           │  ← group-hover:text-sky-600
│  Descripción corta (2 líneas)  │  ← line-clamp-2
│  ★★★★☆  128 reseñas           │
├────────────────────────────────┤
│  $99.00   [Agregar al carrito] │  ← botón con todos los estados
└────────────────────────────────┘
```

---

## 📁 Estructura

```
3-proyecto/tarjeta-producto-interactiva/
├── README.md
└── starter/
    └── index.html
```

---

## 📋 Requisitos

### Borders y Rounded
- [ ] Card con `rounded-2xl overflow-hidden`
- [ ] Badge de categoría con `rounded-full`
- [ ] Botón con `rounded-lg`
- [ ] Imagen dentro del card respeta el rounded

### Shadows
- [ ] Card con `shadow-sm` en reposo y `hover:shadow-xl` al hacer hover
- [ ] Botón con `shadow-sm` y `shadow-{color}/50` (glow effect)

### Sizing
- [ ] Imagen con `h-48 w-full object-cover`
- [ ] Card con `max-w-xs` o `max-w-sm`
- [ ] Texto de descripción con `line-clamp-2`

### Estados
- [ ] Botón con `hover:`, `focus-visible:ring-*`, `active:scale-95`, `disabled:opacity-50`
- [ ] Card con `group` y al menos dos elementos con `group-hover:`
- [ ] Transiciones suaves con `transition-*` y `duration-200`-`duration-300`
'''

files["3-proyecto/tarjeta-producto-interactiva/starter/index.html"] = '''<!DOCTYPE html>
<!--
  Proyecto Semana 4: Tarjeta de Producto Interactiva
  Implementa todos los TODO usando SOLO clases TailwindCSS
-->
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tarjeta de Producto — Semana 4</title>
  </head>
  <body class="min-h-screen bg-slate-100 flex items-center justify-center p-8 font-sans">

    <!-- ============================================ -->
    <!-- TODO: card container                         -->
    <!-- max-w-xs | overflow-hidden | rounded-2xl     -->
    <!-- bg-white | shadow-sm | hover:shadow-xl       -->
    <!-- transition-shadow duration-300               -->
    <!-- group cursor-pointer                         -->
    <!-- ============================================ -->
    <article class="???">

      <!-- IMAGE SECTION -->
      <!-- TODO: imagen container — solo overflow-hidden -->
      <div class="???">

        <!-- TODO: reemplaza este div por una imagen real o usa el div de color -->
        <!-- La imagen/div debe tener:                                           -->
        <!-- h-48 w-full object-cover                                            -->
        <!-- transition-transform duration-500 group-hover:scale-110             -->
        <div class="???  bg-gradient-to-br from-sky-400 via-sky-500 to-violet-500"></div>

      </div>

      <!-- CONTENT SECTION -->
      <!-- TODO: padding del contenido — p-5 -->
      <div class="???">

        <!-- BADGE de categoría -->
        <!-- TODO: rounded-full bg-sky-100 px-3 py-0.5 text-xs font-semibold text-sky-700 -->
        <span class="???">Electrónica</span>

        <!-- NOMBRE del producto -->
        <!-- TODO: mt-2 font-bold text-gray-900 line-clamp-2                     -->
        <!--       group-hover:text-sky-600 transition-colors duration-200        -->
        <h2 class="???">
          Auriculares Inalámbricos Premium con Cancelación de Ruido
        </h2>

        <!-- DESCRIPCIÓN -->
        <!-- TODO: mt-1 text-sm text-gray-500 leading-relaxed line-clamp-2 -->
        <p class="???">
          Audio de alta fidelidad con drivers de 40mm, autonomía de 30 horas
          y conexión Bluetooth 5.3 para una experiencia inmersiva sin cables.
        </p>

        <!-- RATING -->
        <!-- TODO: mt-3 flex items-center gap-2 -->
        <div class="???">
          <!-- Estrellas: text-amber-400 text-sm -->
          <span class="???">★★★★☆</span>
          <!-- Reseñas: text-xs text-gray-400 -->
          <span class="???">128 reseñas</span>
        </div>

        <!-- FOOTER: precio + botón -->
        <!-- TODO: mt-4 flex items-center justify-between -->
        <div class="???">

          <!-- Precio -->
          <!-- TODO: text-xl font-extrabold text-gray-900 -->
          <span class="???">$99.00</span>

          <!-- Botón de compra — con TODOS los estados -->
          <!-- TODO:                                                          -->
          <!-- rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white shadow-sm shadpw-sky-500/30 -->
          <!-- hover:bg-sky-600 hover:shadow-sky-500/50                      -->
          <!-- active:bg-sky-700 active:scale-95                             -->
          <!-- focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2 -->
          <!-- disabled:opacity-50 disabled:cursor-not-allowed               -->
          <!-- outline-none transition-all duration-150                      -->
          <button class="???">
            Agregar
          </button>

        </div>

      </div>

    </article>

    <script type="module" src="/src/main.js"></script>
  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# GLOSARIO
# ─────────────────────────────────────────────────────────────────────────────
files["5-glosario/README.md"] = '''# Glosario — Semana 4: Borders, Shadows, Sizing y Estados

Términos técnicos clave de la semana, ordenados alfabéticamente.

---

## A

### `active:`
Variante de Tailwind que aplica estilos mientras el elemento está siendo presionado (mousedown o touchstart). Útil para feedback táctil en botones: `active:scale-95`.

### `aria-disabled`
Atributo ARIA para indicar que un elemento está deshabilitado sin usar el atributo `disabled` nativo. Tailwind soporta la variante `aria-disabled:` para estilizarlo.

### `aspect-ratio`
Propiedad CSS que mantiene la relación de aspecto de un elemento independientemente de su ancho. `aspect-video` = 16/9, `aspect-square` = 1/1.

---

## B

### `border-radius`
Propiedad CSS para redondear las esquinas de un elemento. En Tailwind: `rounded-sm` (2px) hasta `rounded-full` (9999px).

### Box Shadow
Sombra exterior aplicada al bounding box del elemento. `shadow-sm` a `shadow-2xl` en Tailwind. No sigue la forma del contenido.

---

## D

### `disabled:`
Variante de Tailwind que aplica estilos cuando el elemento tiene el atributo `disabled`. Combinar con `cursor-not-allowed` y `opacity-50` es el patrón estándar.

### `divide-y`
Clase de Tailwind que aplica `border-top` a todos los hijos de un contenedor excepto el primero. Equivalente más limpio que `mt-*` en cada hijo para listas.

### Drop Shadow
Sombra que sigue la forma real del contenido usando `filter: drop-shadow()`. Útil para SVGs e imágenes PNG transparentes. En Tailwind: `drop-shadow-*`.

---

## F

### `focus-visible:`
Variante de Tailwind que solo aplica estilos cuando el foco viene del teclado (no del mouse). Es la variante correcta para el anillo de focus en botones. Mejora la accesibilidad sin penalizar al usuario de mouse.

### `focus-within:`
Variante que aplica estilos al elemento padre cuando cualquier descendiente tiene el foco. Ideal para wrappers de inputs.

---

## G

### `group`
Clase especial de Tailwind que marca un elemento como referencia padre. Sus descendientes pueden reaccionar a los estados del padre usando `group-hover:`, `group-focus:`, etc.

---

## O

### `object-cover`
Valor de `object-fit` que escala la imagen para cubrir completamente el contenedor, recortando si es necesario. El comportamiento equivalente a `background-size: cover`.

### `overflow-hidden`
En contenedores redondeados con imágenes internas, `overflow-hidden` asegura que la imagen no desborde los bordes redondeados del contenedor.

---

## P

### `peer`
Clase especial de Tailwind que marca un elemento de formulario como referencia. Sus siguientes hermanos (siblings) pueden reaccionar a su estado usando `peer-checked:`, `peer-focus:`, `peer-invalid:`, etc.

---

## R

### `ring`
Utilidad de Tailwind que genera un outline visual usando `box-shadow` sin afectar el layout. `ring-2 ring-sky-500 ring-offset-2` es el patrón de focus accesible.

---

## T

### `transition-*`
Clases de Tailwind para activar transiciones CSS. `transition-colors` anima color/fondo, `transition-shadow` anima sombras, `transition-transform` anima transforms. Más específico = mejor rendimiento que `transition-all`.

### Transform
Transformaciones 2D/3D en CSS. En Tailwind: `scale-*`, `translate-*`, `rotate-*`. Se activan en hover con `hover:scale-105`, etc.

---

## V

### Viewport Units
Unidades relativas al viewport: `vw` (viewport width), `vh` (viewport height). En Tailwind: `w-screen` = 100vw, `h-screen` = 100vh, `h-svh` = 100svh (sin barra del browser en móvil).
'''

# ─────────────────────────────────────────────────────────────────────────────
# RECURSOS
# ─────────────────────────────────────────────────────────────────────────────
files["4-recursos/ebooks-free/README.md"] = '''# Libros y Ebooks Gratuitos — Semana 4

---

## Interacción y Animaciones

### 📘 Designing Interactions — Bill Moggridge (extractos)
- Fundamentos de cómo los usuarios perciben y esperan feedback visual
- Busca en Google Scholar o ResearchGate

### 📘 Motion for the Web
- Busca "motion design web animations free guide"
- Principios de timing, easing y propósito de las animaciones

---

## Accesibilidad

### 📘 Inclusive Design Patterns — Heydon Pickering (cap. gratuito)
- **Enlace**: Busca "Heydon Pickering inclusive design patterns free"
- Cubre patrones de HTML/CSS accesibles incluyendo estados de foco

### 📘 MDN Accessibility Guide
- **Enlace**: [https://developer.mozilla.org/en-US/docs/Web/Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- Completamente gratuito, referencia definitiva
'''

files["4-recursos/videografia/README.md"] = '''# Videos y Tutoriales — Semana 4

---

## Borders y Shadows en Tailwind

### 🎥 Tailwind CSS Borders Tutorial
- Busca en YouTube: "tailwind css borders rounded shadows tutorial"
- Aprenderás a aplicar bordes y sombras en componentes reales

---

## Estados Interactivos

### 🎥 Tailwind Hover Focus Active States
- Busca: "tailwind css hover focus active disabled states"
- Aprenderás todos los pseudo-states y cuándo usarlos

---

## Group y Peer

### 🎥 Tailwind Group and Peer Variants
- Busca: "tailwind group peer variants tutorial"
- Casos de uso reales: cards interactivas, toggles, validación de forms

---

## Accesibilidad

### 🎥 Accessible Buttons and Focus Management
- Busca: "accessible buttons focus visible tailwind"
- Por qué `focus-visible:` importa y cómo implementarlo
'''

files["4-recursos/webgrafia/README.md"] = '''# Recursos Web — Semana 4

---

## Borders

- **Tailwind Border Width**: [https://tailwindcss.com/docs/border-width](https://tailwindcss.com/docs/border-width)
- **Tailwind Border Radius**: [https://tailwindcss.com/docs/border-radius](https://tailwindcss.com/docs/border-radius)
- **Tailwind Ring Width**: [https://tailwindcss.com/docs/ring-width](https://tailwindcss.com/docs/ring-width)

---

## Shadows

- **Tailwind Box Shadow**: [https://tailwindcss.com/docs/box-shadow](https://tailwindcss.com/docs/box-shadow)
- **Tailwind Box Shadow Color**: [https://tailwindcss.com/docs/box-shadow-color](https://tailwindcss.com/docs/box-shadow-color)
- **Tailwind Drop Shadow**: [https://tailwindcss.com/docs/drop-shadow](https://tailwindcss.com/docs/drop-shadow)

---

## Sizing

- **Tailwind Width**: [https://tailwindcss.com/docs/width](https://tailwindcss.com/docs/width)
- **Tailwind Height**: [https://tailwindcss.com/docs/height](https://tailwindcss.com/docs/height)
- **Tailwind Object Fit**: [https://tailwindcss.com/docs/object-fit](https://tailwindcss.com/docs/object-fit)
- **Tailwind Aspect Ratio**: [https://tailwindcss.com/docs/aspect-ratio](https://tailwindcss.com/docs/aspect-ratio)

---

## Estados y Variantes

- **Tailwind Hover, Focus, and Other States**: [https://tailwindcss.com/docs/hover-focus-and-other-states](https://tailwindcss.com/docs/hover-focus-and-other-states)
- **MDN focus-visible**: [https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible)
- **WCAG 2.5.3 Focus Appearance**: Busca en w3.org/WAI para los requisitos de contraste del ring de focus

---

## Transiciones

- **Tailwind Transition Property**: [https://tailwindcss.com/docs/transition-property](https://tailwindcss.com/docs/transition-property)
- **Tailwind Transform**: [https://tailwindcss.com/docs/scale](https://tailwindcss.com/docs/scale)
'''

# Write all files
for rel_path, content in files.items():
    full_path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {full_path}")

print(f"\n✅ Week 04 complete: {len(files)} files created.")
