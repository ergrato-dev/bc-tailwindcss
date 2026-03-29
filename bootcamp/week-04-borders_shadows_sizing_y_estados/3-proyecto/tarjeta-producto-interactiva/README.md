# Proyecto Semana 4: Tarjeta de Producto Interactiva

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
