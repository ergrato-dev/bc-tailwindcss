# Ejercicio 02: Sistema de Botones

## 🎯 Objetivo

Construir un sistema completo de botones con 5 variantes, 3 tamaños, todos los estados interactivos (hover, focus, active, disabled, loading) y botones con iconos.

---

## 📋 Instrucciones

### Paso 1: Las 5 variantes de botón

Descomenta el **bloque 1** para ver las 5 variantes en tamaño base: Primary (sky), Secondary (gris), Outline (border), Ghost (transparente) y Destructive (rojo). Presta atención a cómo cada una usa `transition-colors` y `focus-visible:ring-2`.

### Paso 2: Tamaños sm / base / lg + estado disabled

Descomenta el **bloque 2** para ver la matriz de tamaños. Observa que el único cambio entre tamaños son `px-*`, `py-*`, `text-*` y `rounded-*`. Los botones `disabled` muestran `opacity-50 pointer-events-none`.

### Paso 3: Botones con iconos y estado loading

Descomenta el **bloque 3** para ver botones con SVG a la izquierda, a la derecha, icono-only con `aria-label`, y el botón con spinner `animate-spin` para estados de carga.

### Paso 4: Button Group y variantes pill

Descomenta el **bloque 4** para ver un botón-grupo con bordes compartidos (para toggle día/semana/mes) y botones tipo "pill" completamente redondos.

---

## ✅ Verificación

- El bloque 1 muestra las 5 variantes con colores correctos y sin borde visible en Primary/Secondary/Ghost
- El bloque 2: los 3 tamaños son claramente diferentes en altura y padding
- Los disabled tienen opacidad reducida y no reaccionan al hover
- El bloque 3: el spinner del botón loading rota continuamente con `animate-spin`
- El bloque 4: el botón-grupo tiene bordes internos pero redondeados en los extremos
