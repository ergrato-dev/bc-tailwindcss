# Ejercicio 02: Galería Responsive

## 🎯 Objetivo

Construir una galería de imágenes que sea responsive por defecto usando breakpoints explícitos y la técnica avanzada `auto-fill + minmax()` que elimina la necesidad de breakpoints.

---

## 📋 Instrucciones

### Paso 1: Galería con breakpoints explícitos

Descomenta el **bloque 1** para ver la galería clásica: `grid-cols-1` en mobile, `md:grid-cols-2` en tablet y `lg:grid-cols-3` en desktop. Redimensiona el navegador para ver la transición.

### Paso 2: Galería con `auto-fill` + `minmax()`

Descomenta el **bloque 2** para ver la galería intrínseca: las columnas se crean solas sin ningún breakpoint. Cada columna tiene un mínimo de 200px y se estira hasta `1fr`. Redimensiona el navegador para ver cómo el número de columnas se ajusta automáticamente.

### Paso 3: Diferencia entre `auto-fill` y `auto-fit`

Descomenta el **bloque 3** para comparar lado a lado el comportamiento de `auto-fill` (deja columnas vacías visibles) vs. `auto-fit` (estira los ítems existentes para llenar el espacio).

### Paso 4: Galería con aspect-ratio y hover effect

Descomenta el **bloque 4** para ver la galería final pulida: imágenes con `aspect-square`, `object-cover` para recorte correcto, y hover effect con `scale` usando `group`.

---

## ✅ Verificación

- El bloque 1 cambia de 1 a 2 a 3 columnas al redimensionar
- El bloque 2 cambia automáticamente sin breakpoints explícitos
- El bloque 3 muestra visualmente la diferencia entre `auto-fill` y `auto-fit` con pocos ítems
- El bloque 4 muestra imágenes con ratio consistente y zoom suave al hover
