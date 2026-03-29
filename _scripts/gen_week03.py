#!/usr/bin/env python3
"""Generate all content files for week-03: Colores, Tipografía y Espaciado."""
import os

BASE = "bootcamp/week-03-colores_tipografia_y_espaciado"

files = {}

# ─────────────────────────────────────────────────────────────────────────────
# RÚBRICA
# ─────────────────────────────────────────────────────────────────────────────
files["rubrica-evaluacion.md"] = '''# 📊 Rúbrica de Evaluación — Semana 3

**Bootcamp TailwindCSS Zero to Hero** | Semana 3: Colores, Tipografía y Espaciado

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Paleta de Colores** | Explica la escala 50-950, sabe elegir tonos para texto/fondo/borde según contraste y rol visual | Usa colores correctamente pero no sabe explicar cuándo usar 100 vs 500 | Usa colores al azar sin considerar contraste ni jerarquía |
| **Tipografía** | Domina font-size, font-weight, line-height, letter-spacing y font-family; explica cuándo usar cada uno | Aplica los más comunes (text-*, font-*) con alguna confusión en line-height | No puede aplicar más de 2-3 clases tipográficas sin documentación |
| **Espaciado** | Explica la escala de 4px, diferencia px/py/px-4 sin consultar; elige espaciado apropiado por contexto | Aplica padding y margin básicos pero confunde px/py o mx/my | No puede predecir el valor en px de una clase de espaciado |
| **space-x / space-y** | Explica cuándo space-* es mejor que gap o margin individual; lo usa correctamente | Usa space-* pero confunde cuándo conviene vs gap | Desconoce space-x / space-y |
| **Sistema de Diseño** | Explica cómo la escala consistente de Tailwind elimina decisiones arbitrarias y mejora coherencia | Entiende el concepto pero no puede argumentarlo con ejemplos concretos | No comprende el valor del sistema de diseño vs valores custom |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Paleta** | Crea paleta de colores semántica (texto, fondo, acento, borde) con contrastes WCAG AA | Crea paleta funcional con algunas combinaciones de bajo contraste | Selecciona colores sin considerar contrastes ni roles |
| **Ejercicio Tipografía** | Sistema tipográfico completo: jerarquía clara, pesos y tamaños coherentes, line-height correcto | Sistema funcional con 1-2 inconsistencias menores | Sin jerarquía visual; pesos o tamaños aplicados al azar |
| **Ejercicio Espaciado** | Layout con espaciado perfecto: padding/margin consistentes, space-y para listas, gap para grids | Espaciado mayormente correcto con algún margen faltante o inconsistente | Elementos apilados sin espaciado o con overflow |
| **Ejercicio Página Info** | Combina los tres sistemas (color, tipografía, espaciado) en una página coherente y legible | Combina los sistemas con 1-2 inconsistencias de jerarquía | No logra integrar los tres sistemas de forma coherente |

---

## 📦 Producto (30%)

**Proyecto: Blog Post Estilizado**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Colores** | Paleta semántica: texto principal/secundario, fondo, badges con colores de categoría, alto contraste | Paleta funcional con pocas inconsistencias de contraste | Colores arbitrarios sin sistema ni consideración de contraste |
| **Tipografía** | Jerarquía clara: h1>h2>h3>body; line-height legible en párrafos; peso correcto por nivel | Jerarquía mayormente correcta con algún nivel confuso | Sin jerarquía tipográfica; todos los textos parecen iguales |
| **Espaciado** | Espaciado consistente: márgenes entre secciones, padding de contenedor, gap entre elementos | Espaciado funcional con algún valor inconsistente | Elementos sin respiro o con valores de espaciado aleatorios |
| **HTML Semántico** | `article`, `h1-h3`, `p`, `time`, `address`, `ul/li`, `blockquote` usados correctamente | HTML funcional con algún elemento semántico faltante u omitido | Solo div/span sin semántica |
| **Legibilidad** | max-width en prose (~65ch), line-height 1.6-1.8 en texto corrido, contraste mínimo WCAG AA | Legible con pocas mejoras necesarias | Texto difícil de leer por falta de ancho máximo, line-height o contraste |

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
files["1-teoria/01-paleta-colores.md"] = '''# 🎨 Paleta de Colores de Tailwind

## 🎯 Objetivos

- Entender la estructura de la paleta: colores × escala numérica
- Saber elegir tonos para texto, fondo, borde y acento
- Aplicar colores con semántica en interfaces reales
- Entender la opacidad con la notación `/`

---

## 📋 Contenido

![Paleta de colores de Tailwind CSS: escala 50 a 950 con usos semánticos](../0-assets/01-paleta-colores.svg)

### 1. Estructura de la Paleta

Tailwind tiene ~22 colores semánticos, cada uno con 11 escalas:

```
{color}-{escala}
  sky-50   → clarísimo (casi blanco)
  sky-100  → muy claro (fondos suaves)
  sky-200  → claro
  sky-300  → claro medio
  sky-400  → medio
  sky-500  → el tono "puro" del color
  sky-600  → oscuro medio
  sky-700  → oscuro (buen contraste sobre blanco)
  sky-800  → muy oscuro
  sky-900  → casi negro (máximo contraste)
  sky-950  → extremadamente oscuro
```

**Colores disponibles:** slate, gray, zinc, neutral, stone, red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose.

---

### 2. Cómo Elegir el Tono Correcto

| Uso | Escala recomendada | Ejemplo |
|-----|-------------------|---------|
| **Fondo de página** | 50 | `bg-gray-50` |
| **Fondo de card** | white o 50 | `bg-white` |
| **Fondo sutil coloreado** | 100 | `bg-sky-100` |
| **Tono de badge** | 100-200 | `bg-emerald-100` |
| **Color acento/botón** | 500-600 | `bg-sky-500` |
| **Hover de botón** | +100 al acento | `hover:bg-sky-600` |
| **Texto sobre fondo claro** | 700-900 | `text-gray-900` |
| **Texto secundario** | 500-600 | `text-gray-600` |
| **Texto deshabilitado** | 400 | `text-gray-400` |
| **Texto sobre fondo oscuro** | white o 50 | `text-white` |
| **Borde sutil** | 200 | `border-gray-200` |
| **Borde de badge** | 200-300 | `border-sky-200` |

---

### 3. Clases de Color

```html
<!-- Texto -->
<p class="text-gray-900">Texto principal</p>
<p class="text-gray-600">Texto secundario</p>
<p class="text-sky-600">Texto de enlace</p>

<!-- Fondo -->
<div class="bg-white">Card blanca</div>
<div class="bg-sky-50">Fondo azul muy suave</div>
<div class="bg-sky-500">Caja azul sólida</div>

<!-- Borde -->
<div class="border border-gray-200">Borde sutil</div>
<div class="border-2 border-sky-500">Borde acento</div>

<!-- Ring (outline tipo focus) -->
<button class="focus:ring-2 focus:ring-sky-500 focus:ring-offset-2">
  Botón con ring
</button>

<!-- Opacidad con "/" -->
<div class="bg-sky-500/20">Fondo sky al 20% de opacidad</div>
<div class="text-gray-900/70">Texto al 70% de opacidad</div>
```

---

### 4. Colores Semánticos (Patrones Comunes)

```html
<!-- Componente de alerta con colores semánticos -->

<!-- Éxito / Success -->
<div class="flex items-center gap-3 rounded-lg bg-emerald-50 border border-emerald-200 p-4">
  <span class="text-emerald-600 font-medium">✓ Guardado correctamente</span>
</div>

<!-- Error / Danger -->
<div class="flex items-center gap-3 rounded-lg bg-red-50 border border-red-200 p-4">
  <span class="text-red-700 font-medium">✕ Error al procesar</span>
</div>

<!-- Advertencia / Warning -->
<div class="flex items-center gap-3 rounded-lg bg-amber-50 border border-amber-200 p-4">
  <span class="text-amber-800 font-medium">⚠ Revisa los datos</span>
</div>

<!-- Información / Info -->
<div class="flex items-center gap-3 rounded-lg bg-sky-50 border border-sky-200 p-4">
  <span class="text-sky-700 font-medium">ℹ Nueva versión disponible</span>
</div>
```

---

### 5. Contraste y Accesibilidad

Para cumplir WCAG AA necesitas una relación de contraste ≥ 4.5:1 para texto normal.

**Reglas prácticas:**
- Texto sobre fondo blanco: usa **600+** (ej: `text-gray-600`)
- Texto sobre fondo oscuro (500+): usa **blanco** (`text-white`) o escala **50**
- Evita combinar escalas similares: `text-gray-400` sobre `bg-gray-300` = bajo contraste

```html
<!-- ✅ Buen contraste -->
<div class="bg-white text-gray-900">Contraste ~17:1 ✓</div>
<div class="bg-sky-600 text-white">Contraste ~5:1 ✓</div>
<div class="bg-gray-100 text-gray-700">Contraste ~8:1 ✓</div>

<!-- ❌ Mal contraste -->
<div class="bg-gray-100 text-gray-400">Contraste ~3:1 ✗</div>
<div class="bg-sky-200 text-sky-400">Contraste ~2:1 ✗</div>
```

---

## ✅ Checklist de Verificación

- [ ] Puedo elegir el tono correcto (50-950) según el uso (fondo, texto, acento)
- [ ] Entiendo la diferencia entre escala 100 (fondo badge) y 500 (botón sólido)
- [ ] Mis combinaciones de color/fondo tienen contraste WCAG AA
- [ ] Uso colores semánticos (emerald=éxito, red=error, amber=advertencia, sky=info)
'''

files["1-teoria/02-tipografia.md"] = '''# 🔤 Tipografía en Tailwind

## 🎯 Objetivos

- Controlar completamente la tipografía con clases Tailwind
- Entender la jerarquía tipográfica visual
- Aplicar font-family, line-height, letter-spacing
- Crear sistemas tipográficos coherentes

---

## 📋 Contenido

### 1. Font Size — La Escala Completa

```html
<p class="text-xs">12px — Etiquetas, badges, notas al pie</p>
<p class="text-sm">14px — Texto auxiliar, captions</p>
<p class="text-base">16px — Cuerpo de texto (default)</p>
<p class="text-lg">18px — Lead paragraph, subtítulos pequeños</p>
<p class="text-xl">20px — Subtítulos de sección</p>
<p class="text-2xl">24px — Títulos de card o widget</p>
<p class="text-3xl">30px — Heading de sección</p>
<p class="text-4xl">36px — Título de página</p>
<p class="text-5xl">48px — Hero headline</p>
<p class="text-6xl">60px — Display grande</p>
<p class="text-7xl">72px — Display extra grande</p>
```

---

### 2. Font Weight

```html
<p class="font-thin">font-thin — 100 · Decorativo</p>
<p class="font-extralight">font-extralight — 200</p>
<p class="font-light">font-light — 300 · Lead text en diseños modernos</p>
<p class="font-normal">font-normal — 400 · Cuerpo de texto</p>
<p class="font-medium">font-medium — 500 · Labels, nav links</p>
<p class="font-semibold">font-semibold — 600 · Títulos de card, subtítulos</p>
<p class="font-bold">font-bold — 700 · Headings, énfasis fuerte</p>
<p class="font-extrabold">font-extrabold — 800</p>
<p class="font-black">font-black — 900 · Impacto visual máximo</p>
```

**Regla práctica:**
- Cuerpo de texto → `font-normal`
- Labels, categorías → `font-medium`
- Subtítulos de componentes → `font-semibold`
- Headings de página → `font-bold` o `font-extrabold`

---

### 3. Line Height (interlineado)

```html
<!-- line-height afecta la legibilidad del texto corrido -->
<p class="leading-none">leading-none = 1 · Solo para headings cortos</p>
<p class="leading-tight">leading-tight = 1.25 · Headings de varias líneas</p>
<p class="leading-snug">leading-snug = 1.375</p>
<p class="leading-normal">leading-normal = 1.5 · Default del browser</p>
<p class="leading-relaxed">leading-relaxed = 1.625 · Cuerpo de texto ideal</p>
<p class="leading-loose">leading-loose = 2 · Texto muy aireado</p>
```

**Regla práctica:**
- Headings cortos → `leading-tight` o `leading-none`
- Cuerpo de texto largo → `leading-relaxed` o `leading-loose`
- Default → `leading-normal` (1.5)

---

### 4. Letter Spacing (tracking)

```html
<p class="tracking-tighter">tracking-tighter = -0.05em</p>
<p class="tracking-tight">tracking-tight = -0.025em · Headings grandes</p>
<p class="tracking-normal">tracking-normal = 0 · Default</p>
<p class="tracking-wide">tracking-wide = 0.025em</p>
<p class="tracking-wider">tracking-wider = 0.05em</p>
<p class="tracking-widest">tracking-widest = 0.1em · Uppercase labels</p>
```

Patrón común:
```html
<!-- Etiqueta uppercase con tracking amplio -->
<span class="text-xs font-semibold uppercase tracking-widest text-gray-500">
  Categoría
</span>
```

---

### 5. Font Family

Por defecto Tailwind incluye tres stacks:

```html
<!-- Sistema sans-serif (default para UI) -->
<p class="font-sans">Inter, system-ui, -apple-system, sans-serif</p>

<!-- Sistema serif (para contenido editorial) -->
<p class="font-serif">Georgia, Cambria, serif</p>

<!-- Sistema monospace (para código) -->
<p class="font-mono">Menlo, Monaco, monospace</p>
```

Para usar fuentes custom (como Inter de Google Fonts):
```css
/* En src/style.css */
@import "tailwindcss";
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@300..900&display=swap");

@theme {
  --font-sans: 'Inter', system-ui, sans-serif;
}
```

---

### 6. Decoración y Transformación

```html
<!-- Transformación de texto -->
<p class="uppercase">Todo en MAYÚSCULAS</p>
<p class="lowercase">todo en minúsculas</p>
<p class="capitalize">Primera Letra De Cada Palabra</p>
<p class="normal-case">Sin transformación</p>

<!-- Decoración -->
<p class="underline">Subrayado</p>
<p class="line-through">Tachado</p>
<p class="no-underline">Sin subrayado (para links)</p>

<!-- Overflow de texto -->
<p class="truncate">Texto que se trunca con elipsis cuando es muy largo...</p>
<p class="line-clamp-2">Texto que se limita a 2 líneas máximo y luego
  muestra elipsis cuando el contenido es demasiado largo para el contenedor</p>
```

---

### 7. Sistema Tipográfico Completo

Ejemplo de jerarquía coherente para una página de artículo:

```html
<article class="mx-auto max-w-2xl px-4 py-12">
  <!-- Categoría -->
  <span class="text-xs font-semibold uppercase tracking-widest text-sky-600">
    Diseño Web
  </span>

  <!-- Título principal -->
  <h1 class="mt-3 text-4xl font-bold tracking-tight text-gray-900 leading-tight">
    Cómo TailwindCSS cambió mi forma de trabajar
  </h1>

  <!-- Byline -->
  <p class="mt-4 text-sm text-gray-500">
    Por <span class="font-medium text-gray-700">Ana García</span> · 12 min lectura
  </p>

  <!-- Lead paragraph -->
  <p class="mt-6 text-xl text-gray-600 leading-relaxed">
    Después de 5 años usando BEM y CSS Modules, decidí darle una oportunidad real
    a Tailwind. Esta es mi experiencia honesta.
  </p>

  <!-- Cuerpo -->
  <div class="mt-8 space-y-6 text-base text-gray-700 leading-relaxed">
    <p>El primer día fue duro. Las clases interminables en el HTML...</p>
    <p>Pero a la semana, algo cambió. Ya no necesitaba inventar nombres...</p>
  </div>
</article>
```

---

## ✅ Checklist de Verificación

- [ ] Uso `leading-relaxed` o `leading-loose` en texto corrido largo
- [ ] Los headings tienen `tracking-tight` y `leading-tight`
- [ ] Las etiquetas uppercase usan `tracking-widest`
- [ ] Mi jerarquía tipográfica es clara: h1>h2>h3>body claramente distintos
- [ ] Elijo el peso correcto por nivel de la jerarquía
'''

files["1-teoria/03-espaciado.md"] = '''# 📐 Sistema de Espaciado de Tailwind

## 🎯 Objetivos

- Dominar el sistema de espaciado de 4px de Tailwind
- Aplicar padding y margin con precisión por eje y lado
- Usar `space-x` y `space-y` para espaciado entre hijos
- Crear layouts con espaciado consistente

---

## 📋 Contenido

![Escala de espaciado Tailwind: 0 a 24 con valores en px](../0-assets/02-escala-espaciado.svg)

### 1. La Escala de Espaciado

Cada número de la escala = 4px:

| Clase | px | rem |
|-------|----|-----|
| `0` | 0px | 0 |
| `0.5` | 2px | 0.125rem |
| `1` | 4px | 0.25rem |
| `2` | 8px | 0.5rem |
| `3` | 12px | 0.75rem |
| `4` | 16px | 1rem |
| `5` | 20px | 1.25rem |
| `6` | 24px | 1.5rem |
| `8` | 32px | 2rem |
| `10` | 40px | 2.5rem |
| `12` | 48px | 3rem |
| `16` | 64px | 4rem |
| `20` | 80px | 5rem |
| `24` | 96px | 6rem |

---

### 2. Padding

```html
<!-- Todos los lados -->
<div class="p-4">Padding 16px en todos los lados</div>

<!-- Ejes -->
<div class="px-6">Padding horizontal (left + right): 24px</div>
<div class="py-4">Padding vertical (top + bottom): 16px</div>

<!-- Combinado (el más común en UI) -->
<div class="px-4 py-2">Botón: 16px horizontal, 8px vertical</div>
<div class="px-6 py-4">Card: 24px horizontal, 16px vertical</div>

<!-- Por lado individual -->
<div class="pt-8">Padding top: 32px</div>
<div class="pb-4">Padding bottom: 16px</div>
<div class="pl-4">Padding left: 16px</div>
<div class="pr-2">Padding right: 8px</div>
```

---

### 3. Margin

```html
<!-- Todos los lados -->
<div class="m-4">Margin 16px</div>

<!-- Ejes -->
<div class="mx-auto">Centrar horizontalmente</div>
<div class="my-8">Margin vertical 32px</div>

<!-- Por lado -->
<div class="mt-4">Margin top 16px (lo más usado)</div>
<div class="mb-6">Margin bottom 24px</div>

<!-- Margin negativo -->
<div class="mt-4 -mt-2">Margin top negativo (superponer elementos)</div>
```

**Tip importante:** Para espaciado entre elementos de una lista o sección, usa `mt-*` en el elemento hijo, no `mb-*` en el padre.

---

### 4. Space-X y Space-Y

`space-x-*` y `space-y-*` aplican margen entre hijos de un flex container, sin margen en el primer hijo.

```html
<!-- Sin space-x: hay que poner margen manualmente -->
<nav class="flex">
  <a class="ml-6">Link 1</a>  <!-- primero sin margen -->
  <a class="ml-6">Link 2</a>
  <a class="ml-6">Link 3</a>
</nav>

<!-- Con space-x: mucho más limpio -->
<nav class="flex space-x-6">
  <a>Link 1</a>
  <a>Link 2</a>
  <a>Link 3</a>
</nav>

<!-- space-y para listas verticales -->
<ul class="space-y-4">
  <li>Elemento 1</li>
  <li>Elemento 2</li>
  <li>Elemento 3</li>
</ul>
```

**¿Cuándo usar space-* vs gap-*?**
- `space-*` → en flex containers lineales simples
- `gap-*` → en flex o grid con wrap, o en grids, siempre que tengas wrapping

---

### 5. Gap (para Flexbox y Grid)

```html
<!-- Gap uniforme -->
<div class="flex gap-4">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

<!-- Gap por eje -->
<div class="grid grid-cols-3 gap-x-6 gap-y-4">
  <!-- gap horizontal vs vertical diferente -->
</div>
```

---

### 6. Contenedor con Max Width

```html
<!-- Patrón estándar de contenedor centrado -->
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
  <!-- contenido de página -->
</div>

<!-- Contenedor para texto (legibilidad óptima ~65ch) -->
<div class="mx-auto max-w-2xl px-4">
  <!-- artículo o blog post -->
</div>
```

**Referencia de max-width:**
- `max-w-xs` → 320px
- `max-w-sm` → 384px
- `max-w-md` → 448px
- `max-w-lg` → 512px
- `max-w-xl` → 576px
- `max-w-2xl` → 672px (ideal para texto)
- `max-w-4xl` → 896px
- `max-w-7xl` → 1280px (layout de página)

---

## ✅ Checklist de Verificación

- [ ] Puedo convertir cualquier clase de espaciado a px mentalmente (4=16, 6=24, 8=32)
- [ ] Uso `px-*` + `py-*` en componentes en lugar de `p-*` cuando los ejes son diferentes
- [ ] Entiendo cuándo usar `space-y-*` vs `mt-*` vs `gap-*`
- [ ] Mis layouts tienen espaciado consistente: mismos valores para elementos similares
'''

files["1-teoria/04-text-overflow-y-wrapping.md"] = '''# 📄 Text Overflow, Wrapping y Alineación

## 🎯 Objetivos

- Controlar el desbordamiento de texto
- Aplicar truncado y line-clamp
- Gestionar el wrapping y el whitespace
- Dominar la alineación de texto

---

## 📋 Contenido

### 1. Truncado con Elipsis

```html
<!-- truncate: una línea + elipsis al final -->
<p class="w-48 truncate">
  Este texto es muy largo y será truncado con elipsis
</p>
<!-- Resultado: "Este texto es muy lar..." -->

<!-- overflow-hidden: corta sin elipsis -->
<p class="w-48 overflow-hidden">
  Texto cortado abruptamente sin elipsis
</p>
```

Para que `truncate` funcione:
1. El elemento debe tener un ancho definido (`w-*`, `max-w-*`, o estar en un contenedor flex)
2. La clase incluye automáticamente `overflow-hidden` y `text-ellipsis`

---

### 2. Line Clamp (multiline truncate)

```html
<!-- Limitar a 1 línea -->
<p class="line-clamp-1">Texto de una sola línea máximo...</p>

<!-- Limitar a 2 líneas (muy común en cards) -->
<p class="line-clamp-2">
  Descripción de producto que si es muy larga se corta
  a dos líneas exactas con elipsis al final automáticamente
</p>

<!-- Limitar a 3 líneas -->
<p class="line-clamp-3">...</p>

<!-- Eliminar el clamp (útil para toggles) -->
<p class="line-clamp-none">Texto completo sin límite</p>
```

---

### 3. Whitespace

```html
<!-- Colapsa espacios normalmente (default) -->
<p class="whitespace-normal">  Espacios  múltiples    colapsan  </p>

<!-- Preserva saltos de línea y espacios -->
<p class="whitespace-pre">Línea 1
Línea 2
  Indentado</p>

<!-- Preserva pero hace wrap -->
<p class="whitespace-pre-wrap">Preserva formato pero hace wrap cuando llega al borde</p>

<!-- No hace wrap nunca (cuidado con overflow) -->
<p class="whitespace-nowrap">Este texto nunca hará wrap sin importar el ancho</p>
```

---

### 4. Word Break

```html
<!-- Corta palabras largas cuando no hay espacio -->
<p class="break-words">https://una-url-muy-larga-que-no-tiene-espacios/y/sigue/siendo/larga</p>

<!-- No corta palabras nunca -->
<p class="break-normal">Comportamiento normal del navegador</p>

<!-- Corte en cualquier carácter (más agresivo) -->
<p class="break-all">TextoMuyLargoSinEspaciosQueNecesitaCortarse</p>

<!-- Mantiene palabras completas cuando puede -->
<p class="break-keep">For CJK text that should keep words intact</p>
```

---

### 5. Alineación de Texto

```html
<p class="text-left">Alineado a la izquierda (default)</p>
<p class="text-center">Centrado</p>
<p class="text-right">Alineado a la derecha</p>
<p class="text-justify">
  Justificado: el texto se distribuye para ocupar todo el ancho
  de la línea, creando márgenes uniformes en ambos lados.
</p>

<!-- Text-wrap moderno (v3.3+) -->
<h1 class="text-balance">
  Título que balancea el texto para que las líneas sean iguales
</h1>
<p class="text-pretty">
  Párrafo que evita líneas huérfanas al final
</p>
```

---

### 6. Casos de Uso Reales

```html
<!-- Card con título truncado y descripción en 2 líneas -->
<article class="max-w-sm rounded-xl border bg-white p-4">
  <h3 class="truncate font-semibold text-gray-900">
    Nombre de producto muy largo que se trunca
  </h3>
  <p class="mt-1 line-clamp-2 text-sm text-gray-600">
    Descripción detallada del producto que puede ser muy extensa
    y queremos mostrar solo las primeras dos líneas.
  </p>
</article>

<!-- Lista de resultados con text overflow controlado -->
<ul class="space-y-2">
  <li class="flex items-center gap-3">
    <span class="w-32 shrink-0 truncate text-sm font-medium text-gray-900">
      Nombre de archivo largo.pdf
    </span>
    <span class="flex-1 truncate text-sm text-gray-500">
      Ruta: /documentos/importante/muy/profundo/archivo.pdf
    </span>
  </li>
</ul>
```

---

## ✅ Checklist de Verificación

- [ ] Uso `truncate` para títulos en una línea dentro de contenedores con ancho
- [ ] Uso `line-clamp-2` o `line-clamp-3` para descripciones en cards
- [ ] Entiendo cuándo usar `break-words` vs `break-all`
- [ ] Uso `text-balance` en headings para mejor presentación visual
'''

files["1-teoria/05-sistema-diseno-coherencia.md"] = '''# 🎨 Sistema de Diseño y Coherencia Visual

## 🎯 Objetivos

- Entender qué es un sistema de diseño y por qué importa
- Aplicar los tres pilares (color, tipografía, espaciado) de forma coherente
- Crear componentes con jerarquía visual clara
- Conocer los patrones más comunes de UI

---

## 📋 Contenido

### 1. ¿Qué es un Sistema de Diseño?

Un sistema de diseño es un **conjunto de reglas y tokens** que garantizan coherencia visual en toda la interfaz:

- **Tokens de color**: ¿Qué colores usamos y para qué?
- **Escala tipográfica**: ¿Qué tamaños y pesos?
- **Escala de espaciado**: ¿Qué valores de padding y margin?
- **Componentes**: Botones, cards, badges con variantes definidas

Tailwind implementa un sistema de diseño **opinionado pero flexible**.

---

### 2. Los Tres Pilares Juntos

Un error común es usar los pilares por separado. Aquí cómo combinarlos:

```html
<!-- ❌ Sin sistema: valores arbitrarios, sin coherencia -->
<div style="padding: 13px; font-size: 15px; color: #3a4b5c; margin-bottom: 7px;">
  Título sin sistema
</div>

<!-- ✅ Con sistema Tailwind: valores de la escala, coherentes -->
<div class="p-4 text-base text-gray-700 mb-4">
  Contenido con sistema
</div>
```

---

### 3. Jerarquía Visual en la Práctica

```html
<!-- Card de artículo de blog — jerarquía clara -->
<article class="max-w-sm overflow-hidden rounded-2xl bg-white shadow-sm">

  <!-- Imagen -->
  <img
    src="cover.jpg"
    alt="Portada del artículo"
    class="h-40 w-full object-cover"
  />

  <div class="p-5">
    <!-- Categoría: pequeña, colored, uppercase -->
    <span class="text-xs font-semibold uppercase tracking-wider text-sky-600">
      Frontend
    </span>

    <!-- Título: prominente, peso bold -->
    <h2 class="mt-1 text-lg font-bold leading-tight text-gray-900 line-clamp-2">
      Cómo construir un sistema de colores con Tailwind
    </h2>

    <!-- Descripción: secundaria, más pequeña -->
    <p class="mt-2 text-sm text-gray-600 leading-relaxed line-clamp-3">
      Una guía práctica para definir paletas semánticas
      que funcionen en modo claro y oscuro.
    </p>

    <!-- Footer: metadatos, mínimo espacio -->
    <div class="mt-4 flex items-center justify-between">
      <span class="text-xs text-gray-400">12 min lectura</span>
      <time class="text-xs text-gray-400">Mar 2026</time>
    </div>
  </div>
</article>
```

---

### 4. Patrones de Color Comunes

```html
<!-- Patrón 1: Fondo claro con texto oscuro (el default) -->
<div class="bg-white text-gray-900">
  <p class="text-gray-600">Texto secundario</p>
  <p class="text-gray-400">Texto deshabilitado</p>
</div>

<!-- Patrón 2: Sección con fondo de acento suave -->
<section class="bg-sky-50">
  <h2 class="text-sky-900 font-bold">Título</h2>
  <p class="text-sky-700">Texto en la sección de acento</p>
  <button class="bg-sky-500 text-white hover:bg-sky-600">CTA</button>
</section>

<!-- Patrón 3: Header oscuro -->
<header class="bg-slate-900">
  <nav>
    <a class="text-slate-300 hover:text-white">Link</a>
    <a class="text-white font-semibold">Activo</a>
  </nav>
</header>
```

---

### 5. La Regla del "60-30-10"

Una guía clásica de diseño para mantener coherencia:

- **60%** del espacio visual: color neutro (blanco, grays claros)
- **30%** del espacio visual: color secundario (grays medios, backgrounds)
- **10%** del espacio visual: color acento (sky, emerald, violet...)

```html
<!-- 60% neutro, 30% secondary, 10% acento -->
<main class="min-h-screen bg-gray-50">           <!-- 60% neutro -->
  <div class="bg-white rounded-xl shadow-sm p-6"> <!-- 30% blanco -->
    <button class="bg-sky-500 text-white px-4 py-2 rounded-lg"> <!-- 10% acento -->
      Acción principal
    </button>
  </div>
</main>
```

---

## ✅ Checklist de Verificación

- [ ] Mis páginas usan máximo 2-3 colores de acento
- [ ] La jerarquía tipográfica es clara: categoría < subtítulo < título, en ese orden
- [ ] El espaciado es consistente: elementos similares tienen valores iguales
- [ ] Los textos secundarios usan escala 500-600, no 300-400 (bajo contraste)
- [ ] Mis componentes siguen el patrón 60-30-10 intuitivamente
'''

# ─────────────────────────────────────────────────────────────────────────────
# EJERCICIOS
# ─────────────────────────────────────────────────────────────────────────────
files["2-practicas/01-ejercicio-paleta-colores/README.md"] = '''# Ejercicio 01: Construyendo con la Paleta de Colores

## 🎯 Objetivo

Explorar la paleta de Tailwind construyendo componentes de alerta con colores semánticos (éxito, error, advertencia, info).

---

## 🛠️ Configuración

Proyecto Vite + Tailwind corriendo con `pnpm dev`.

---

## 📋 Instrucciones

### Paso 1: Sistema de alertas básico

Descomenta el **bloque 1** para ver los 4 tipos de alerta con colores semánticos.

Observa el patrón: `bg-{color}-50` para fondo suave + `text-{color}-700` para texto + `border-{color}-200` para borde.

---

### Paso 2: Badges por categoría

Descomenta el **bloque 2** para ver un sistema de badges con colores por categoría.

---

### Paso 3: Botones con estados de color

Descomenta el **bloque 3** para ver cómo los colores cambian entre estados: default, hover, active.

---

### Paso 4: Fila de estado con indicadores

Descomenta el **bloque 4** para construir una lista de estados (activo, pendiente, error, inactivo).

---

## ✅ Verificación

El ejercicio está completo cuando:
- Ves todos los componentes con colores correctamente aplicados
- Puedes crear un nuevo tipo de alerta cambiando solo el color
- Entiendes por qué `bg-emerald-50` + `text-emerald-700` tienen buen contraste
'''

files["2-practicas/01-ejercicio-paleta-colores/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 01 — Paleta de Colores</title>
  </head>
  <body class="min-h-screen bg-gray-50 p-8">
    <h1 class="mb-8 text-2xl font-bold text-gray-900">Sistema de Colores Semánticos</h1>

    <!-- ============================================ -->
    <!-- BLOQUE 1: Sistema de alertas                 -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-10 space-y-3">                                                                    -->
    <!--  <h2 class="mb-4 text-lg font-semibold text-gray-700">Alertas semánticas</h2>                      -->
    <!--  <div class="flex items-start gap-3 rounded-xl border border-emerald-200 bg-emerald-50 p-4">       -->
    <!--    <span class="text-lg">✅</span>                                                                   -->
    <!--    <div>                                                                                             -->
    <!--      <p class="font-semibold text-emerald-800">Éxito — Pago procesado</p>                          -->
    <!--      <p class="mt-0.5 text-sm text-emerald-700">Tu orden #1234 fue confirmada exitosamente.</p>    -->
    <!--    </div>                                                                                            -->
    <!--  </div>                                                                                              -->
    <!--  <div class="flex items-start gap-3 rounded-xl border border-red-200 bg-red-50 p-4">              -->
    <!--    <span class="text-lg">❌</span>                                                                   -->
    <!--    <div>                                                                                             -->
    <!--      <p class="font-semibold text-red-800">Error — Pago rechazado</p>                             -->
    <!--      <p class="mt-0.5 text-sm text-red-700">Verifica los datos de tu tarjeta e intenta de nuevo.</p> -->
    <!--    </div>                                                                                            -->
    <!--  </div>                                                                                              -->
    <!--  <div class="flex items-start gap-3 rounded-xl border border-amber-200 bg-amber-50 p-4">          -->
    <!--    <span class="text-lg">⚠️</span>                                                                   -->
    <!--    <div>                                                                                             -->
    <!--      <p class="font-semibold text-amber-800">Advertencia — Stock bajo</p>                         -->
    <!--      <p class="mt-0.5 text-sm text-amber-700">Solo quedan 3 unidades. Compra pronto.</p>          -->
    <!--    </div>                                                                                            -->
    <!--  </div>                                                                                              -->
    <!--  <div class="flex items-start gap-3 rounded-xl border border-sky-200 bg-sky-50 p-4">             -->
    <!--    <span class="text-lg">ℹ️</span>                                                                    -->
    <!--    <div>                                                                                             -->
    <!--      <p class="font-semibold text-sky-800">Info — Nueva versión disponible</p>                    -->
    <!--      <p class="mt-0.5 text-sm text-sky-700">Actualiza para obtener las últimas mejoras.</p>       -->
    <!--    </div>                                                                                            -->
    <!--  </div>                                                                                              -->
    <!-- </section>                                                                                           -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Badges por categoría               -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                    -->
    <!--   <h2 class="mb-4 text-lg font-semibold text-gray-700">Badges por categoría</h2>                        -->
    <!--   <div class="flex flex-wrap gap-2">                                                                       -->
    <!--     <span class="rounded-full bg-sky-100 px-3 py-1 text-xs font-medium text-sky-700">Frontend</span>    -->
    <!--     <span class="rounded-full bg-violet-100 px-3 py-1 text-xs font-medium text-violet-700">Backend</span> -->
    <!--     <span class="rounded-full bg-emerald-100 px-3 py-1 text-xs font-medium text-emerald-700">DevOps</span> -->
    <!--     <span class="rounded-full bg-amber-100 px-3 py-1 text-xs font-medium text-amber-700">Diseño</span>   -->
    <!--     <span class="rounded-full bg-rose-100 px-3 py-1 text-xs font-medium text-rose-700">Mobile</span>    -->
    <!--     <span class="rounded-full bg-gray-100 px-3 py-1 text-xs font-medium text-gray-600">Otro</span>      -->
    <!--   </div>                                                                                                    -->
    <!-- </section>                                                                                                  -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Botones con estados de color       -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                     -->
    <!--   <h2 class="mb-4 text-lg font-semibold text-gray-700">Botones con estados</h2>                          -->
    <!--   <div class="flex flex-wrap gap-3">                                                                        -->
    <!--     <button class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-medium text-white hover:bg-sky-600 active:bg-sky-700 transition-colors">Primario</button> -->
    <!--     <button class="rounded-lg bg-emerald-500 px-4 py-2 text-sm font-medium text-white hover:bg-emerald-600 transition-colors">Éxito</button> -->
    <!--     <button class="rounded-lg bg-red-500 px-4 py-2 text-sm font-medium text-white hover:bg-red-600 transition-colors">Eliminar</button> -->
    <!--     <button class="rounded-lg bg-amber-500 px-4 py-2 text-sm font-medium text-white hover:bg-amber-600 transition-colors">Advertir</button> -->
    <!--     <button class="rounded-lg border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors">Secundario</button> -->
    <!--   </div>                                                                                                     -->
    <!-- </section>                                                                                                   -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Lista de estados                   -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                              -->
    <!--   <h2 class="mb-4 text-lg font-semibold text-gray-700">Estados de servicio</h2>                                   -->
    <!--   <ul class="space-y-2">                                                                                             -->
    <!--     <li class="flex items-center justify-between rounded-lg border border-emerald-200 bg-emerald-50 px-4 py-3">    -->
    <!--       <span class="font-medium text-emerald-800">API de pagos</span>                                               -->
    <!--       <span class="flex items-center gap-1.5 text-xs font-semibold text-emerald-600">                              -->
    <!--         <span class="h-2 w-2 rounded-full bg-emerald-500"></span> Operativo                                        -->
    <!--       </span>                                                                                                        -->
    <!--     </li>                                                                                                            -->
    <!--     <li class="flex items-center justify-between rounded-lg border border-amber-200 bg-amber-50 px-4 py-3">        -->
    <!--       <span class="font-medium text-amber-800">CDN de imágenes</span>                                              -->
    <!--       <span class="flex items-center gap-1.5 text-xs font-semibold text-amber-600">                                -->
    <!--         <span class="h-2 w-2 rounded-full bg-amber-500"></span> Degradado                                          -->
    <!--       </span>                                                                                                        -->
    <!--     </li>                                                                                                            -->
    <!--     <li class="flex items-center justify-between rounded-lg border border-red-200 bg-red-50 px-4 py-3">           -->
    <!--       <span class="font-medium text-red-800">Webhooks</span>                                                       -->
    <!--       <span class="flex items-center gap-1.5 text-xs font-semibold text-red-600">                                  -->
    <!--         <span class="h-2 w-2 rounded-full bg-red-500"></span> Interrumpido                                         -->
    <!--       </span>                                                                                                        -->
    <!--     </li>                                                                                                            -->
    <!--   </ul>                                                                                                              -->
    <!-- </section>                                                                                                           -->

  </body>
</html>
'''

files["2-practicas/02-ejercicio-tipografia/README.md"] = '''# Ejercicio 02: Sistema Tipográfico Jerárquico

## 🎯 Objetivo

Construir un sistema tipográfico coherente con jerarquía visual clara usando las clases de Tailwind para font-size, font-weight, line-height y letter-spacing.

---

## 📋 Instrucciones

### Paso 1: Escala de tamaños

Descomenta el **bloque 1** para ver la escala completa de text-xs a text-5xl aplicada.

---

### Paso 2: Jerarquía de heading + body

Descomenta el **bloque 2** para ver una página de artículo con jerarquía h1, h2, h3, párrafo.

---

### Paso 3: Estilos especiales

Descomenta el **bloque 3** para practicar uppercase+tracking, truncate y line-clamp.

---

### Paso 4: Font families

Descomenta el **bloque 4** para comparar font-sans, font-serif y font-mono.

---

## ✅ Verificación

El ejercicio está completo cuando:
- La jerarquía visual entre niveles es obviamente clara
- Los párrafos tienen `leading-relaxed` y se leen cómodamente
- Puedes crear un nuevo heading de nivel sin consultar documentación
'''

files["2-practicas/02-ejercicio-tipografia/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 02 — Tipografía</title>
  </head>
  <body class="min-h-screen bg-white p-8 text-gray-900">
    <h1 class="mb-10 text-3xl font-bold">Sistema Tipográfico</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Escala de tamaños completa         -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-12 border-b pb-8">                                         -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Escala de tamaños</h2> -->
    <!--   <div class="space-y-3">                                                      -->
    <!--     <p class="text-xs text-gray-500">text-xs — 12px · Badges, notas, meta</p> -->
    <!--     <p class="text-sm text-gray-600">text-sm — 14px · Texto auxiliar y captions</p> -->
    <!--     <p class="text-base font-normal">text-base — 16px · Cuerpo de texto default</p> -->
    <!--     <p class="text-lg">text-lg — 18px · Lead paragraph</p>                    -->
    <!--     <p class="text-xl font-medium">text-xl — 20px · Subtítulo de sección</p> -->
    <!--     <p class="text-2xl font-semibold">text-2xl — 24px · Título de card</p>   -->
    <!--     <p class="text-3xl font-bold">text-3xl — 30px · Heading de sección</p>   -->
    <!--     <p class="text-4xl font-bold">text-4xl — 36px · Título de página</p>     -->
    <!--     <p class="text-5xl font-extrabold">text-5xl — 48px · Hero</p>            -->
    <!--   </div>                                                                       -->
    <!-- </section>                                                                     -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Jerarquía articulo real            -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12 max-w-2xl border-b pb-8">                                              -->
    <!--   <span class="text-xs font-semibold uppercase tracking-widest text-sky-600">Tutorial</span> -->
    <!--   <h1 class="mt-2 text-4xl font-bold leading-tight tracking-tight">                          -->
    <!--     El Sistema de Tipografía de Tailwind                                                      -->
    <!--   </h1>                                                                                       -->
    <!--   <p class="mt-4 text-xl leading-relaxed text-gray-600">                                     -->
    <!--     Aprende a construir jerarquías tipográficas claras que mejoran la legibilidad y guían la  -->
    <!--     atención del usuario de forma intuitiva.                                                  -->
    <!--   </p>                                                                                        -->
    <!--   <h2 class="mt-8 text-2xl font-bold">¿Por qué importa la jerarquía?</h2>                   -->
    <!--   <p class="mt-3 text-base leading-relaxed text-gray-700">                                   -->
    <!--     La jerarquía tipográfica guía la mirada del usuario. Cuando todos los textos tienen el   -->
    <!--     mismo tamaño y peso, el cerebro no sabe por dónde empezar. Una buena jerarquía es como   -->
    <!--     un mapa de navegación visual.                                                             -->
    <!--   </p>                                                                                        -->
    <!--   <h3 class="mt-6 text-xl font-semibold">Los tres niveles básicos</h3>                      -->
    <!--   <p class="mt-2 text-base leading-relaxed text-gray-700">                                   -->
    <!--     Primario (h1), secundario (h2-h3) y cuerpo. Cada nivel debe ser visiblemente distinto.   -->
    <!--   </p>                                                                                        -->
    <!-- </section>                                                                                    -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Estilos especiales                 -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12 border-b pb-8">                                                         -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Estilos especiales</h2> -->
    <!--   <div class="space-y-4">                                                                      -->
    <!--     <div>                                                                                      -->
    <!--       <p class="text-xs text-gray-400">uppercase + tracking-widest</p>                       -->
    <!--       <p class="mt-1 text-sm font-semibold uppercase tracking-widest text-gray-600">Categoría de contenido</p> -->
    <!--     </div>                                                                                     -->
    <!--     <div>                                                                                      -->
    <!--       <p class="text-xs text-gray-400">truncate en contenedor w-64</p>                       -->
    <!--       <p class="w-64 truncate text-sm">Este título muy largo quedará truncado con elipsis automáticamente</p> -->
    <!--     </div>                                                                                     -->
    <!--     <div>                                                                                      -->
    <!--       <p class="text-xs text-gray-400">line-clamp-2</p>                                      -->
    <!--       <p class="mt-1 line-clamp-2 max-w-md text-sm leading-relaxed text-gray-700">           -->
    <!--         Esta descripción es muy larga y queremos que solo muestre dos líneas. El resto quedará -->
    <!--         oculto con una elipsis. Es perfecto para cards de blog o de producto donde el espacio es limitado. -->
    <!--       </p>                                                                                     -->
    <!--     </div>                                                                                     -->
    <!--   </div>                                                                                       -->
    <!-- </section>                                                                                     -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Font families                      -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-12">                                                                 -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Font families</h2> -->
    <!--   <div class="space-y-4">                                                               -->
    <!--     <div>                                                                               -->
    <!--       <p class="text-xs text-gray-400">font-sans (default UI)</p>                     -->
    <!--       <p class="font-sans text-base">Inter / System UI / Sans-serif</p>               -->
    <!--     </div>                                                                             -->
    <!--     <div>                                                                               -->
    <!--       <p class="text-xs text-gray-400">font-serif (editorial)</p>                     -->
    <!--       <p class="font-serif text-base">Georgia / Cambria / Serif</p>                   -->
    <!--     </div>                                                                             -->
    <!--     <div>                                                                               -->
    <!--       <p class="text-xs text-gray-400">font-mono (código)</p>                        -->
    <!--       <p class="font-mono text-sm">Menlo / Monaco / Monospace</p>                    -->
    <!--     </div>                                                                             -->
    <!--   </div>                                                                               -->
    <!-- </section>                                                                             -->

  </body>
</html>
'''

files["2-practicas/03-ejercicio-espaciado/README.md"] = '''# Ejercicio 03: Sistema de Espaciado

## 🎯 Objetivo

Dominar el sistema de espaciado de Tailwind aplicando padding, margin, space-x/y y gap en contextos reales.

---

## 📋 Instrucciones

### Paso 1: Visualización del espaciado

Descomenta el **bloque 1** para ver la escala de padding visualmente con cajas de colores.

---

### Paso 2: Componentes con padding contextual

Descomenta el **bloque 2** para ver cómo diferentes contextos requieren padding diferente (botón vs card vs sección).

---

### Paso 3: space-x y space-y

Descomenta el **bloque 3** para ver `space-x-*` en una navbar y `space-y-*` en una lista.

---

### Paso 4: Contenedor con max-width

Descomenta el **bloque 4** para ver el patrón de contenedor centrado con `max-w-*` + `mx-auto`.

---

## ✅ Verificación

- Ves todos los bloques y el espaciado es claramente visible
- Puedes predecir el valor en px de cualquier clase de espaciado
- Entiendes cuándo usar `space-y-*` vs `gap-*`
'''

files["2-practicas/03-ejercicio-espaciado/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 03 — Espaciado</title>
  </head>
  <body class="min-h-screen bg-slate-100 p-8">
    <h1 class="mb-8 text-2xl font-bold text-gray-900">Sistema de Espaciado</h1>


    <!-- ============================================ -->
    <!-- BLOQUE 1: Escala visual de padding           -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <section class="mb-10">                                                                                           -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Escala de padding</h2>        -->
    <!--   <div class="flex flex-wrap items-end gap-3">                                                                   -->
    <!--     <div class="bg-sky-200 p-1"><span class="block bg-sky-500 text-xs text-white p-0.5">p-1 = 4px</span></div> -->
    <!--     <div class="bg-sky-200 p-2"><span class="block bg-sky-500 text-xs text-white p-0.5">p-2 = 8px</span></div> -->
    <!--     <div class="bg-sky-200 p-3"><span class="block bg-sky-500 text-xs text-white p-0.5">p-3 = 12px</span></div> -->
    <!--     <div class="bg-sky-200 p-4"><span class="block bg-sky-500 text-xs text-white p-0.5">p-4 = 16px</span></div> -->
    <!--     <div class="bg-sky-200 p-6"><span class="block bg-sky-500 text-xs text-white p-0.5">p-6 = 24px</span></div> -->
    <!--     <div class="bg-sky-200 p-8"><span class="block bg-sky-500 text-xs text-white p-0.5">p-8 = 32px</span></div> -->
    <!--     <div class="bg-sky-200 p-12"><span class="block bg-sky-500 text-xs text-white p-0.5">p-12 = 48px</span></div> -->
    <!--   </div>                                                                                                          -->
    <!-- </section>                                                                                                        -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Padding contextual por componente  -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                                                      -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">Padding por contexto</h2> -->
    <!--   <div class="flex flex-wrap items-start gap-4">                                                             -->
    <!--                                                                                                              -->
    <!--     Botones: px horizontal, py vertical pequeño                                                              -->
    <!--     <button class="rounded-md bg-sky-500 px-3 py-1.5 text-sm text-white">px-3 py-1.5 (sm)</button>         -->
    <!--     <button class="rounded-md bg-sky-500 px-4 py-2 text-sm text-white">px-4 py-2 (md)</button>              -->
    <!--     <button class="rounded-md bg-sky-500 px-6 py-3 text-sm text-white">px-6 py-3 (lg)</button>              -->
    <!--                                                                                                              -->
    <!--     Card: padding generoso                                                                                   -->
    <!--     <div class="rounded-xl bg-white p-6 shadow-sm">                                                         -->
    <!--       <p class="text-sm font-semibold text-gray-700">Card — p-6</p>                                         -->
    <!--       <p class="text-xs text-gray-400">24px en todos los lados</p>                                          -->
    <!--     </div>                                                                                                    -->
    <!--                                                                                                              -->
    <!--     Sección: padding grande                                                                                  -->
    <!--     <div class="rounded-xl bg-gray-800 px-8 py-12 text-white">                                             -->
    <!--       <p class="text-sm font-semibold">Sección px-8 py-12</p>                                              -->
    <!--       <p class="text-xs text-gray-400">32px H / 48px V</p>                                                  -->
    <!--     </div>                                                                                                    -->
    <!--   </div>                                                                                                     -->
    <!-- </section>                                                                                                   -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: space-x y space-y                  -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                              -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">space-x y space-y</h2> -->
    <!--                                                                                      -->
    <!--   space-x-6 en navbar                                                                -->
    <!--   <nav class="mb-4 flex items-center space-x-6 rounded-lg bg-white p-4 shadow-sm"> -->
    <!--     <a href="#" class="text-sm font-medium text-gray-900">Inicio</a>                -->
    <!--     <a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Blog</a> -->
    <!--     <a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Proyectos</a> -->
    <!--     <a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Contacto</a> -->
    <!--   </nav>                                                                               -->
    <!--                                                                                      -->
    <!--   space-y-3 en lista de items                                                        -->
    <!--   <ul class="space-y-3">                                                             -->
    <!--     <li class="rounded-lg bg-white p-4 shadow-sm">Item con space-y-3</li>           -->
    <!--     <li class="rounded-lg bg-white p-4 shadow-sm">Separación automática</li>        -->
    <!--     <li class="rounded-lg bg-white p-4 shadow-sm">Entre cada elemento</li>          -->
    <!--   </ul>                                                                              -->
    <!-- </section>                                                                           -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Contenedor centrado con max-width  -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="mb-10">                                                               -->
    <!--   <h2 class="mb-4 text-sm font-semibold uppercase tracking-widest text-gray-400">max-width containers</h2> -->
    <!--                                                                                       -->
    <!--   max-w-sm (384px) — Para cards y formularios                                        -->
    <!--   <div class="mx-auto max-w-sm rounded-lg bg-sky-100 p-4 text-center text-sm">      -->
    <!--     max-w-sm — 384px                                                                  -->
    <!--   </div>                                                                              -->
    <!--                                                                                       -->
    <!--   max-w-2xl (672px) — Para texto de artículo                                        -->
    <!--   <div class="mx-auto mt-4 max-w-2xl rounded-lg bg-emerald-100 p-4 text-center text-sm"> -->
    <!--     max-w-2xl — 672px (ideal para texto)                                             -->
    <!--   </div>                                                                              -->
    <!--                                                                                       -->
    <!--   max-w-7xl (1280px) — Para layout de página                                        -->
    <!--   <div class="mx-auto mt-4 max-w-7xl rounded-lg bg-amber-100 p-4 text-center text-sm"> -->
    <!--     max-w-7xl — 1280px (layout de página)                                            -->
    <!--   </div>                                                                              -->
    <!-- </section>                                                                            -->

  </body>
</html>
'''

files["2-practicas/04-ejercicio-pagina-informacion/README.md"] = '''# Ejercicio 04: Página de Información

## 🎯 Objetivo

Integrar colores, tipografía y espaciado en una página de información completa con múltiples secciones.

---

## 📋 Instrucciones

### Paso 1: Header de página

Descomenta el **bloque 1** para crear el header con fondo de color, título y descripción.

---

### Paso 2: Sección de estadísticas

Descomenta el **bloque 2** para construir una fila de 3 estadísticas numéricas con etiquetas.

---

### Paso 3: Lista de características

Descomenta el **bloque 3** para crear una lista de features con íconos de color y descripciones.

---

### Paso 4: Testimonial

Descomenta el **bloque 4** para construir una cita destacada con tipografía y espaciado correctos.

---

## ✅ Verificación

El ejercicio está completo cuando:
- La página tiene jerarquía visual clara entre secciones
- Los colores son semánticos y consistentes
- El espaciado entre secciones es generoso y coherente
'''

files["2-practicas/04-ejercicio-pagina-informacion/starter/index.html"] = '''<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ejercicio 04 — Página de Información</title>
  </head>
  <body class="min-h-screen bg-gray-50">


    <!-- ============================================ -->
    <!-- BLOQUE 1: Header de página                   -->
    <!-- ============================================ -->
    <!-- Descomenta las siguientes líneas:            -->

    <!-- <header class="bg-slate-900 px-6 py-16 text-center">                                               -->
    <!--   <span class="text-xs font-semibold uppercase tracking-widest text-sky-400">Producto</span>      -->
    <!--   <h1 class="mt-3 text-4xl font-extrabold leading-tight tracking-tight text-white">              -->
    <!--     PixelCraft Studio                                                                              -->
    <!--   </h1>                                                                                             -->
    <!--   <p class="mx-auto mt-4 max-w-xl text-lg leading-relaxed text-slate-400">                       -->
    <!--     Diseño web profesional para startups y emprendedores que quieren destacar.                    -->
    <!--   </p>                                                                                             -->
    <!--   <div class="mt-8 flex justify-center gap-4">                                                    -->
    <!--     <button class="rounded-lg bg-sky-500 px-6 py-3 text-sm font-semibold text-white hover:bg-sky-400 transition-colors">Empezar ahora</button> -->
    <!--     <button class="rounded-lg border border-slate-600 px-6 py-3 text-sm font-semibold text-slate-300 hover:border-slate-400 transition-colors">Ver proyectos</button> -->
    <!--   </div>                                                                                           -->
    <!-- </header>                                                                                         -->


    <!-- ============================================ -->
    <!-- BLOQUE 2: Estadísticas                       -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="bg-white px-6 py-12">                                             -->
    <!--   <div class="mx-auto grid max-w-4xl grid-cols-3 divide-x divide-gray-100 text-center"> -->
    <!--     <div class="px-8">                                                             -->
    <!--       <p class="text-4xl font-extrabold text-gray-900">120+</p>                   -->
    <!--       <p class="mt-1 text-sm text-gray-500">Proyectos entregados</p>              -->
    <!--     </div>                                                                         -->
    <!--     <div class="px-8">                                                             -->
    <!--       <p class="text-4xl font-extrabold text-gray-900">98%</p>                    -->
    <!--       <p class="mt-1 text-sm text-gray-500">Satisfacción del cliente</p>          -->
    <!--     </div>                                                                         -->
    <!--     <div class="px-8">                                                             -->
    <!--       <p class="text-4xl font-extrabold text-gray-900">5 años</p>                 -->
    <!--       <p class="mt-1 text-sm text-gray-500">De experiencia</p>                    -->
    <!--     </div>                                                                         -->
    <!--   </div>                                                                           -->
    <!-- </section>                                                                         -->


    <!-- ============================================ -->
    <!-- BLOQUE 3: Lista de características           -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="px-6 py-16">                                                                  -->
    <!--   <div class="mx-auto max-w-4xl">                                                             -->
    <!--     <h2 class="text-center text-3xl font-bold text-gray-900">¿Qué incluye nuestro servicio?</h2> -->
    <!--     <p class="mx-auto mt-3 max-w-xl text-center text-base text-gray-600">Todo lo que necesitas para lanzar tu proyecto web.</p> -->
    <!--     <ul class="mt-10 grid grid-cols-2 gap-6">                                                 -->
    <!--       <li class="flex items-start gap-4 rounded-xl bg-white p-5 shadow-sm">                  -->
    <!--         <span class="rounded-lg bg-sky-100 p-2 text-xl">🎨</span>                            -->
    <!--         <div>                                                                                  -->
    <!--           <p class="font-semibold text-gray-900">Diseño UI personalizado</p>                  -->
    <!--           <p class="mt-1 text-sm text-gray-600 leading-relaxed">Interfaz única diseñada para tu marca y audiencia.</p> -->
    <!--         </div>                                                                                 -->
    <!--       </li>                                                                                    -->
    <!--       <li class="flex items-start gap-4 rounded-xl bg-white p-5 shadow-sm">                  -->
    <!--         <span class="rounded-lg bg-emerald-100 p-2 text-xl">⚡</span>                         -->
    <!--         <div>                                                                                  -->
    <!--           <p class="font-semibold text-gray-900">Rendimiento optimizado</p>                   -->
    <!--           <p class="mt-1 text-sm text-gray-600 leading-relaxed">Lighthouse 95+ en todas las métricas.</p> -->
    <!--         </div>                                                                                 -->
    <!--       </li>                                                                                    -->
    <!--       <li class="flex items-start gap-4 rounded-xl bg-white p-5 shadow-sm">                  -->
    <!--         <span class="rounded-lg bg-violet-100 p-2 text-xl">📱</span>                         -->
    <!--         <div>                                                                                  -->
    <!--           <p class="font-semibold text-gray-900">Responsive design</p>                        -->
    <!--           <p class="mt-1 text-sm text-gray-600 leading-relaxed">Perfecto en mobile, tablet y desktop.</p> -->
    <!--         </div>                                                                                 -->
    <!--       </li>                                                                                    -->
    <!--       <li class="flex items-start gap-4 rounded-xl bg-white p-5 shadow-sm">                  -->
    <!--         <span class="rounded-lg bg-amber-100 p-2 text-xl">♿</span>                           -->
    <!--         <div>                                                                                  -->
    <!--           <p class="font-semibold text-gray-900">Accesibilidad incluida</p>                   -->
    <!--           <p class="mt-1 text-sm text-gray-600 leading-relaxed">WCAG AA de serie, sin costo adicional.</p> -->
    <!--         </div>                                                                                 -->
    <!--       </li>                                                                                    -->
    <!--     </ul>                                                                                      -->
    <!--   </div>                                                                                       -->
    <!-- </section>                                                                                     -->


    <!-- ============================================ -->
    <!-- BLOQUE 4: Testimonial                        -->
    <!-- ============================================ -->
    <!-- Descomenta:                                  -->

    <!-- <section class="bg-sky-50 px-6 py-16">                                                              -->
    <!--   <div class="mx-auto max-w-2xl text-center">                                                       -->
    <!--     <p class="text-5xl text-sky-300">"</p>                                                          -->
    <!--     <blockquote class="-mt-4 text-xl font-medium leading-relaxed text-gray-700">                   -->
    <!--       PixelCraft nos entregó la web en 2 semanas. El resultado superó todas las expectativas. -->
    <!--       Nuestro bounce rate bajó un 40%.                                                               -->
    <!--     </blockquote>                                                                                    -->
    <!--     <div class="mt-6">                                                                               -->
    <!--       <p class="font-semibold text-gray-900">María González</p>                                    -->
    <!--       <p class="text-sm text-gray-500">CEO, TechStartup MX</p>                                     -->
    <!--     </div>                                                                                           -->
    <!--   </div>                                                                                             -->
    <!-- </section>                                                                                           -->

  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# PROYECTO
# ─────────────────────────────────────────────────────────────────────────────
files["3-proyecto/blog-post-estilizado/README.md"] = '''# Proyecto Semana 3: Blog Post Estilizado

## 📋 Descripción

Construye una **página de artículo de blog** completamente estilizada usando el sistema de colores, tipografía y espaciado de TailwindCSS. Este proyecto es un ejercicio puro de dominio del sistema de diseño de Tailwind.

---

## 🎯 Objetivos

- Aplicar jerarquía tipográfica coherente (h1 → h2 → h3 → body)
- Usar colores semánticos para categorías, meta, código y alertas
- Mantener espaciado consistente a través de toda la página
- Asegurar legibilidad con line-height y max-width correctos

---

## 📐 Estructura esperada

```
┌──────────────────────────────────────────┐
│  HEADER: Nav simple                      │
├──────────────────────────────────────────┤
│  HERO DEL ARTÍCULO                       │
│  Categoría badge + Fecha                 │
│  H1: Título del artículo                 │
│  Lead paragraph (text-xl)                │
│  Autor + tiempo de lectura               │
├──────────────────────────────────────────┤
│  CUERPO DEL ARTÍCULO (max-w-2xl)         │
│  H2 + párrafos + H3 + lista              │
│  Blockquote                              │
│  Snippet de código                       │
│  Alerta/nota                             │
├──────────────────────────────────────────┤
│  FOOTER: Copyright                       │
└──────────────────────────────────────────┘
```

---

## 📁 Estructura

```
3-proyecto/blog-post-estilizado/
├── README.md
└── starter/
    └── index.html
```

---

## 📋 Requisitos

### Tipografía
- [ ] `h1` con `text-4xl font-bold leading-tight tracking-tight`
- [ ] Párrafos con `text-base leading-relaxed`
- [ ] Categoría con `text-xs uppercase tracking-widest`
- [ ] Al menos un `h2` y un `h3` claramente distintos

### Colores
- [ ] Badge de categoría con color semántico
- [ ] Texto principal: `text-gray-900`; secundario: `text-gray-600`
- [ ] Blockquote o alerta con paleta de acento

### Espaciado
- [ ] `max-w-2xl mx-auto` para el contenido del artículo
- [ ] `space-y-6` o `mt-6` entre bloques de texto
- [ ] `py-16` o mayor en secciones principales

### HTML Semántico
- [ ] `<article>` para el cuerpo
- [ ] `<time>` para la fecha
- [ ] `<blockquote>` para citas
- [ ] `<code>` o `<pre>` para código
'''

files["3-proyecto/blog-post-estilizado/starter/index.html"] = '''<!DOCTYPE html>
<!--
  Proyecto Semana 3: Blog Post Estilizado
  Implementa todos los TODO usando SOLO clases TailwindCSS
-->
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Blog Post — Bootcamp TailwindCSS</title>
  </head>
  <body>

    <!-- ============================================ -->
    <!-- TODO: contenedor de página                   -->
    <!-- bg-white o bg-gray-50                        -->
    <!-- font-sans text-gray-900                      -->
    <!-- ============================================ -->
    <div class="???">


      <!-- NAV -->
      <!-- TODO: nav con logo + links usando                 -->
      <!-- flex items-center justify-between                 -->
      <!-- borde inferior border-b border-gray-100           -->
      <!-- padding px-6 py-4, max-w-4xl mx-auto             -->
      <nav class="???">
        <span class="???">📝 Mi Blog</span>
        <!-- TODO: links de nav con space-x-6, text-sm text-gray-600 -->
      </nav>


      <!-- HERO DEL ARTÍCULO -->
      <!-- TODO: sección hero, py-16 px-6, bg-gray-50 -->
      <section class="???">
        <div class="mx-auto max-w-2xl">

          <!-- TODO: badge de categoría -->
          <!-- rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold text-sky-700 -->
          <span class="???">TailwindCSS</span>

          <!-- TODO: título h1 -->
          <!-- mt-4 text-4xl font-bold leading-tight tracking-tight text-gray-900 -->
          <h1 class="???">
            Cómo el Sistema de Diseño de Tailwind Cambió mi Flujo de Trabajo
          </h1>

          <!-- TODO: lead paragraph -->
          <!-- mt-4 text-xl leading-relaxed text-gray-600 -->
          <p class="???">
            Después de años usando CSS arbitrario, descubrí que la consistencia
            no viene de la disciplina, sino del sistema correcto.
          </p>

          <!-- TODO: meta del artículo (autor, fecha, lectura) -->
          <!-- mt-6 flex items-center gap-4 text-sm text-gray-500 -->
          <div class="???">
            <span>Por <strong class="text-gray-700">Ana García</strong></span>
            <!-- TODO: time con datetime -->
            <time datetime="2026-03-29">29 Mar 2026</time>
            <span>8 min lectura</span>
          </div>

        </div>
      </section>


      <!-- CUERPO DEL ARTÍCULO -->
      <!-- TODO: article max-w-2xl mx-auto px-4 py-12 -->
      <article class="???">

        <!-- TODO: espacio entre párrafos con space-y-6 -->
        <div class="???">

          <!-- TODO: primer párrafo -->
          <!-- text-base leading-relaxed text-gray-700 -->
          <p class="???">
            El primer día que instalé Tailwind, quise desinstalarlo. Las clases
            largas en el HTML me parecían un retroceso. Pero le di una semana...
          </p>

          <!-- TODO: h2 del artículo -->
          <!-- text-2xl font-bold text-gray-900 mt-10 -->
          <h2 class="???">El Problema con el CSS Tradicional</h2>

          <p class="???">
            Llevaba 5 años nombrando clases CSS. `.card-header__title--featured`.
            Cada vez que necesitaba un componente nuevo, pasaba 10 minutos solo
            decidiendo el nombre. Era "naming fatigue" en estado puro.
          </p>

          <!-- TODO: blockquote -->
          <!-- border-l-4 border-sky-400 bg-sky-50 pl-4 py-3 -->
          <!-- texto: text-lg font-medium text-sky-900 italic -->
          <blockquote class="???">
            <p class="???">
              "Nombrar cosas es uno de los dos problemas más difíciles en
              computer science. Tailwind elimina ese problema."
            </p>
          </blockquote>

          <!-- TODO: h3 -->
          <!-- text-xl font-semibold text-gray-900 mt-8 -->
          <h3 class="???">La Escala de Espaciado lo Cambia Todo</h3>

          <p class="???">
            Antes usaba valores arbitrarios: `margin: 13px`, `padding: 7px`.
            Ahora todo es múltiplo de 4. El resultado es coherencia automática.
          </p>

          <!-- TODO: lista de items -->
          <!-- ul con space-y-2, cada li con text-base text-gray-700 -->
          <!-- agregar un "·" o "→" antes de cada item -->
          <ul class="???">
            <li class="???">→ p-4 = 16px siempre, en cualquier proyecto</li>
            <li class="???">→ Los layouts se "cuadran" solos</li>
            <li class="???">→ Cero debate sobre valores de spacing</li>
          </ul>

          <!-- TODO: alerta/nota -->
          <!-- rounded-xl border border-amber-200 bg-amber-50 p-4 -->
          <!-- título: font-semibold text-amber-800 -->
          <!-- texto: mt-1 text-sm text-amber-700 -->
          <div class="???">
            <p class="???">⚠ Nota importante</p>
            <p class="???">
              Este patrón solo funciona si usas la escala nativa de Tailwind.
              Agregar valores custom rompe la coherencia.
            </p>
          </div>

          <!-- TODO: snippet de código -->
          <!-- rounded-lg bg-slate-900 p-4 -->
          <!-- code: font-mono text-sm text-sky-300 -->
          <pre class="???"><code class="???"><!-- Antes -->
&lt;div style="margin: 13px; padding: 7px;"&gt;...&lt;/div&gt;

/* Ahora */
&lt;div class="m-3 p-2"&gt;...&lt;/div&gt;</code></pre>

        </div>

      </article>


      <!-- FOOTER -->
      <!-- TODO: footer border-t border-gray-100 py-8 text-center text-sm text-gray-500 -->
      <footer class="???">
        <p>© 2026 Mi Blog · Construido con TailwindCSS</p>
      </footer>

    </div>

    <script type="module" src="/src/main.js"></script>
  </body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# GLOSARIO
# ─────────────────────────────────────────────────────────────────────────────
files["5-glosario/README.md"] = '''# Glosario — Semana 3: Colores, Tipografía y Espaciado

Términos técnicos clave de la semana, ordenados alfabéticamente.

---

## C

### Contraste (WCAG)
Relación de brillo entre el color del texto y el color del fondo. WCAG AA exige ≥4.5:1 para texto normal y ≥3:1 para texto grande. Herramienta: [contrast-ratio.com](https://contrast-ratio.com/).

### `color/{opacidad}`
Sintaxis moderna de Tailwind para aplicar opacidad a colores. Ejemplo: `bg-sky-500/20` aplica sky-500 con 20% de opacidad. Elimina la necesidad de `bg-opacity-*`.

---

## D

### Design Token
Variable que almacena un valor del sistema de diseño: un color, un tamaño de fuente, un valor de espaciado. En Tailwind v4 se definen en `@theme {}` en el CSS.

---

## J

### Jerarquía tipográfica
La organización visual de los textos en niveles de importancia: título (más grande/grueso), subtítulo (mediano), cuerpo (regular), meta/label (pequeño). Una buena jerarquía guía la mirada sin esfuerzo.

---

## L

### `leading-*` (Line Height)
Clases de Tailwind para controlar el interlineado. `leading-tight` (1.25) para headings, `leading-relaxed` (1.625) para cuerpo de texto. El valor correcto mejora significativamente la legibilidad.

### `line-clamp-{n}`
Clase de Tailwind que limita el texto visible a `n` líneas y agrega elipsis. Requiere `overflow-hidden` internamente. Ideal para tarjetas de contenido donde el texto puede variar en longitud.

---

## P

### Paleta de colores (Tailwind)
Conjunto de ~22 colores base con 11 escalas cada uno (50 a 950). Tailwind genera todas las variaciones internamente: no necesitas un plugin de Sass ni variables personalizadas para los colores default.

---

## S

### Escala de espaciado
El sistema numérico de Tailwind donde cada unidad = 4px (0.25rem). Garantiza que todos los valores de spacing sean múltiplos de 4, lo que produce diseños visualmente consistentes y "cuadrados".

### `space-x-{n}` / `space-y-{n}`
Clases que aplican margen entre elementos hijos de un contenedor flex, sin afectar al primer hijo. Equivalente a `> * + * { margin-left/top: ... }`. Alternativa limpia a margin manual en cada hijo.

---

## T

### `tracking-*` (Letter Spacing)
Clase de Tailwind para el espaciado entre caracteres. `tracking-tight` en headings grandes, `tracking-widest` en etiquetas uppercase. Afecta más la legibilidad de lo que parece.

### `truncate`
Clase de Tailwind que aplica `overflow-hidden`, `text-overflow: ellipsis` y `white-space: nowrap` en una sola clase. El elemento debe tener un ancho definido para que funcione.

---

## W

### WCAG (Web Content Accessibility Guidelines)
Estándares internacionales de accesibilidad web. El nivel AA (2.1) es el mínimo estándar profesional. Tailwind facilita cumplirlo porque la paleta fue diseñada con contraste en mente.
'''

# ─────────────────────────────────────────────────────────────────────────────
# RECURSOS
# ─────────────────────────────────────────────────────────────────────────────
files["4-recursos/ebooks-free/README.md"] = '''# Libros y Ebooks Gratuitos — Semana 3

---

## Colores y Diseño

### 📘 Refactoring UI — Color (capítulo preview)
- **Enlace**: [https://www.refactoringui.com/](https://www.refactoringui.com/)
- **Qué encontrarás**: Principios de cómo elegir y usar colores en UI real
- **Nivel**: Intermedio

### 📘 Color Theory for Designers
- **Fuente**: Smashing Magazine (artículos gratuitos)
- **Enlace**: Busca "color theory for designers smashing magazine"
- **Qué encontrarás**: Rueda de colores, contraste, armonías de color

---

## Tipografía

### 📘 The Elements of Typographic Style (extractos)
- **Autor**: Robert Bringhurst
- **Enlace**: Extractos disponibles en Google Scholar
- **Qué encontrarás**: Principios clásicos de tipografía aplicables al diseño web

### 📘 Practical Typography
- **Autor**: Matthew Butterick
- **Enlace**: [https://practicaltypography.com/](https://practicaltypography.com/)
- **Qué encontrarás**: Guía completa de tipografía para la web, muy práctica
- **Nivel**: Principiante - Intermedio

---

## Nota

Todos los enlaces son accesibles sin pago. Los libros físicos completos requieren compra.
'''

files["4-recursos/videografia/README.md"] = '''# Videos y Tutoriales — Semana 3

---

## Colores en Tailwind

### 🎥 Tailwind CSS Color Palette Tutorial
- **Dónde buscar**: YouTube → "tailwind css colors tutorial 2024"
- **Qué aprenderás**: Cómo usar la paleta, personalizar colores, opacidad
- **Duración**: 20-30 min

---

## Tipografía Web

### 🎥 Web Typography Fundamentals
- **Dónde buscar**: YouTube → "web typography fundamentals"
- **Qué aprenderás**: Font pairing, jerarquía, legibilidad
- **Duración**: 30-45 min

### 🎥 Tailwind Typography Plugin
- **Dónde buscar**: YouTube → "tailwindcss typography plugin prose"
- **Qué aprenderás**: Cómo usar @tailwindcss/typography para contenido editorial
- **Duración**: 15-20 min (lo usaremos en semana 11)

---

## Diseño de Sistemas

### 🎥 Design Systems Explained
- **Dónde buscar**: YouTube → "design system explained beginners"
- **Qué aprenderás**: Qué es un DS, tokens, componentes, variantes
- **Duración**: 20-40 min
'''

files["4-recursos/webgrafia/README.md"] = '''# Recursos Web — Semana 3

---

## Colores

- **Tailwind Color Palette**: [https://tailwindcss.com/docs/customizing-colors](https://tailwindcss.com/docs/customizing-colors)
- **Coolors** (generador de paletas): [https://coolors.co/](https://coolors.co/)
- **Color Contrast Checker**: [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)
- **Tailwind Shades** (paletas custom al estilo Tailwind): [https://www.tailwindshades.com/](https://www.tailwindshades.com/)

---

## Tipografía

- **Tailwind Typography**: [https://tailwindcss.com/docs/font-size](https://tailwindcss.com/docs/font-size)
- **Google Fonts**: [https://fonts.google.com/](https://fonts.google.com/)
- **Type Scale** (visualizador de escalas tipográficas): [https://typescale.com/](https://typescale.com/)
- **Font Joy** (parejas de fuentes): [https://fontjoy.com/](https://fontjoy.com/)

---

## Espaciado

- **Tailwind Spacing**: [https://tailwindcss.com/docs/padding](https://tailwindcss.com/docs/padding)
- **Spacing Guide**: Busca "8pt grid system UI design" para el concepto detrás de la escala de 4px

---

## Accesibilidad y Contraste

- **WCAG Contrast Checker**: [https://www.w3.org/WAI/WCAG21/Techniques/general/G18](https://www.w3.org/WAI/WCAG21/Techniques/general/G18)
- **Accessible Colors**: [https://accessible-colors.com/](https://accessible-colors.com/)
'''

# Write all files
for rel_path, content in files.items():
    full_path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {full_path}")

print(f"\n✅ Week 03 complete: {len(files)} files created.")
