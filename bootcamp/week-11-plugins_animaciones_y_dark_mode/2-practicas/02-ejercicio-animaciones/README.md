# Ejercicio 02 — Animaciones y Transiciones

## 🎯 Objetivo

Aprender a aplicar transiciones suaves, usar las animaciones built-in de Tailwind (`spin`, `pulse`, `bounce`, `ping`) y crear animaciones custom con `@keyframes` en el config, respetando las preferencias de movimiento reducido del usuario.

---

## 🛠️ Qué vas a construir

Una página de showcase de animaciones con cuatro secciones:
1. Transiciones de hover en botones y cards
2. Animaciones built-in: loader, skeleton, scroll cue, notification badge
3. Animaciones custom con `@keyframes` (`fade-in`, `slide-up`)
4. Accesibilidad en animaciones con `motion-safe:` y `motion-reduce:`

---

## 📁 Estructura

```
02-ejercicio-animaciones/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

Abre `starter/index.html` y descomenta cada bloque en orden.

---

### 🔵 BLOQUE 1 — Transiciones de hover

**Concepto**: Las transiciones hacen que los cambios de estado (hover, focus, active) sean suaves y agradables. La fórmula base es: `transition-{propiedad} duration-{ms} ease-{tipo}`.

```html
<!-- Transición de color en botón -->
<button class="bg-sky-500 hover:bg-sky-600 transition-colors duration-200">
  Hover suave
</button>

<!-- Transición de elevación en card -->
<div class="shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
  Tarjeta elevada
</div>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — Animaciones built-in

**Concepto**: Tailwind incluye 4 animaciones predefinidas para casos de uso comunes en UI.

| Clase | Uso típico |
|-------|-----------|
| `animate-spin` | Indicador de carga (spinner) |
| `animate-pulse` | Skeleton loading (placeholders de contenido) |
| `animate-bounce` | Scroll cue o llamada de atención |
| `animate-ping` | Notification badge con efecto de onda |

```html
<!-- Spinner -->
<div class="animate-spin h-8 w-8 rounded-full border-4 border-gray-200 border-t-sky-500"></div>

<!-- Skeleton card -->
<div class="animate-pulse h-4 bg-gray-200 rounded w-3/4"></div>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — Animaciones custom con `@keyframes`

**Concepto**: Tailwind permite definir `@keyframes` y sus `animation` en el config. Las clases generadas siguen el patrón `animate-{nombre}`.

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        keyframes: {
          'fade-in': {
            '0%':   { opacity: '0', transform: 'translateY(8px)' },
            '100%': { opacity: '1', transform: 'translateY(0)' },
          },
          'slide-up': {
            '0%':   { opacity: '0', transform: 'translateY(24px)' },
            '100%': { opacity: '1', transform: 'translateY(0)' },
          },
        },
        animation: {
          'fade-in':  'fade-in 0.4s ease-out forwards',
          'slide-up': 'slide-up 0.5s ease-out forwards',
        },
      },
    },
  }
</script>

<div class="animate-fade-in">Hero que aparece suavemente</div>
<div class="animate-slide-up delay-100">Card escalonada</div>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3.

---

### 🔵 BLOQUE 4 — `motion-safe:` para accesibilidad

**Concepto**: `motion-safe:` aplica la clase solo cuando el usuario no ha indicado preferencia por movimiento reducido. `motion-reduce:` aplica lo contrario.

```html
<!-- ❌ No considera las preferencias del usuario -->
<div class="animate-slide-up">Animación siempre activa</div>

<!-- ✅ Respeta prefers-reduced-motion -->
<div class="motion-safe:animate-slide-up">
  Animación solo si el usuario acepta movimiento
</div>

<!-- Transición desactivada si se prefiere menos movimiento -->
<button class="motion-reduce:transition-none transition-colors hover:bg-sky-600">
  Botón adaptable
</button>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Criterios de Verificación

- [ ] Los botones tienen transición suave al hacer hover
- [ ] El spinner usa `animate-spin` con un borde coloreado solo en un lado
- [ ] El skeleton loader usa `animate-pulse` con bloques `bg-gray-200`
- [ ] Las animaciones custom `fade-in` y `slide-up` están definidas en `tailwind.config`
- [ ] Las animaciones decorativas usan `motion-safe:animate-*`
- [ ] El `delay-*` scalonado hace que los elementos aparezcan uno tras otro
