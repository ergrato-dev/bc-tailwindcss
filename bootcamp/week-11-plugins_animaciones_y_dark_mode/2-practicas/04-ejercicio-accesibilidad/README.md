# Ejercicio 04 — Accesibilidad con Tailwind

## 🎯 Objetivo

Aplicar las principales técnicas de accesibilidad web disponibles en Tailwind: ocultar visualmente elementos para lectores de pantalla, crear foco visible solo para teclado, verificar y corregir contraste de color, y agregar atributos ARIA correctamente.

---

## 🛠️ Qué vas a construir

Una UI con cuatro secciones de accesibilidad progresiva:
1. Botones con íconos y texto accesible (`sr-only`)
2. Navegación por teclado con `focus-visible:` y skip link
3. Auditoría y corrección de contraste de color (WCAG AA)
4. Animaciones accesibles con `motion-safe:` y atributos `aria-*`

---

## 📁 Estructura

```
04-ejercicio-accesibilidad/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

Abre `starter/index.html` y descomenta cada bloque en orden.

---

### 🔵 BLOQUE 1 — `sr-only` y íconos accesibles

**Concepto**: Los botones que solo muestran un ícono deben tener texto alternativo para lectores de pantalla. `sr-only` oculta el texto visualmente pero lo mantiene accesible.

```html
<!-- ❌ Botón inaccesible: sin texto, lector lee "button" sin contexto -->
<button class="p-2 rounded">
  <svg aria-hidden="false"><!-- ícono de búsqueda --></svg>
</button>

<!-- ✅ Accesible: texto sr-only + aria-hidden en ícono -->
<button class="p-2 rounded" aria-label="Buscar">
  <svg aria-hidden="true"><!-- ícono de búsqueda --></svg>
</button>

<!-- O con span sr-only: -->
<button class="p-2 rounded">
  <svg aria-hidden="true"><!-- ícono --></svg>
  <span class="sr-only">Buscar</span>
</button>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — `focus-visible:` y skip link

**Concepto**: Los usuarios de teclado necesitan ver claramente dónde está el foco. `focus-visible:` muestra el ring de foco solo cuando se navega con teclado, sin mostrarlo al hacer click.

```html
<!-- Skip link: primer elemento de la página, permite saltar al contenido -->
<a href="#main"
   class="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4
          focus:z-50 focus:px-4 focus:py-2 focus:bg-sky-500 focus:text-white
          focus:rounded-lg">
  Saltar al contenido principal
</a>

<!-- Botón con focus-visible: ring visible solo con teclado -->
<button class="px-4 py-2 rounded-xl bg-sky-500 text-white
               outline-none
               focus-visible:ring-2 focus-visible:ring-sky-500
               focus-visible:ring-offset-2">
  Accesible con teclado (Tab para probar)
</button>
```

**Instrucción**: Usa `Tab` en el browser para navegar el BLOQUE 2 y verificar que el foco es visible.

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — Contraste y WCAG AA

**Concepto**: WCAG AA requiere relación de contraste ≥4.5:1 para texto normal. Varias combinaciones de colores de Tailwind que se ven "bien" en realidad no pasan este umbral.

| Color texto | Fondo | Contraste | WCAG |
|-------------|-------|-----------|------|
| `gray-400` | `white` | 2.5:1 | ❌ Falla |
| `gray-500` | `white` | 4.6:1 | ✅ Aprueba |
| `gray-600` | `white` | 7.0:1 | ✅ Excelente |
| `sky-400`  | `gray-950` | 7.8:1 | ✅ Excelente |

```html
<!-- Antes (❌ Falla): texto demasiado claro -->
<p class="text-gray-400">Texto de ayuda — difícil de leer</p>

<!-- Después (✅ Aprueba): mínimo para WCAG AA -->
<p class="text-gray-600">Texto de ayuda — legible</p>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3 (que muestra las versiones antes/después).

---

### 🔵 BLOQUE 4 — `motion-safe:` y atributos ARIA

**Concepto**: Las animaciones deben respetar la preferencia del usuario por movimiento reducido. Los atributos ARIA complementan el HTML semántico para comunicar estados.

```html
<!-- Animación que respeta prefers-reduced-motion -->
<div class="motion-safe:animate-fade-in motion-safe:animate-slide-up">
  Aparece animado solo si el usuario acepta movimiento
</div>

<!-- Botón toggle con aria-pressed -->
<button aria-pressed="false"
        onclick="this.setAttribute('aria-pressed',
                 this.getAttribute('aria-pressed') === 'true' ? 'false' : 'true')">
  Favorito
</button>

<!-- Nav con aria-current -->
<nav>
  <a href="/" aria-current="page" class="text-sky-600 font-semibold">Inicio</a>
  <a href="/blog" class="text-gray-600">Blog</a>
</nav>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Criterios de Verificación

- [ ] Los botones-ícono tienen `aria-label` o `<span class="sr-only">`
- [ ] Los íconos decorativos tienen `aria-hidden="true"`
- [ ] El skip link aparece al presionar Tab por primera vez
- [ ] El ring de foco es visible al navegar con teclado (Tab), invisible al hacer click
- [ ] Los textos secundarios usan `text-gray-600` o superior sobre fondos blancos
- [ ] Las animaciones decorativas usan `motion-safe:animate-*`
- [ ] Los botones de toggle tienen `aria-pressed` que se actualiza al hacer click
- [ ] Los links de nav activos tienen `aria-current="page"`
