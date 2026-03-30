# Ejercicio 03: Cards y Variantes

## 🎯 Objetivo

Construir los 4 tipos de card más comunes en UI modernas: product card, blog card, user card y stat card. Aplicar `group`/`group-hover:*` para efectos coordinados y `line-clamp-*` para texto controlado.

---

## 📋 Instrucciones

### Paso 1: Product Card con group-hover en imagen

Descomenta el **bloque 1** para ver la product card con efecto zoom en la imagen al hacer hover. La clave: `group` en el `<article>`, `group-hover:scale-110` en el `<img>`, y `overflow-hidden` en el contenedor de la imagen para evitar desbordamiento.

### Paso 2: Blog Card con badge y line-clamp

Descomenta el **bloque 2** para ver la blog card con badge de categoría, título que cambia a `text-sky-400` en hover (gracias a `group-hover:text-sky-400`) y excerpt con `line-clamp-3`. Nota el `flex flex-col` con `flex-1` que empuja el autor al fondo.

### Paso 3: User Card con avatar y stats grid

Descomenta el **bloque 3** para ver la user card con avatar redondeado que obtiene `ring-sky-500` al hacer hover, badge de online con `absolute`, mini grid de estadísticas con `grid-cols-3` y botón de seguir.

### Paso 4: Stat Card con indicador de tendencia

Descomenta el **bloque 4** para ver las stat cards de dashboard: icono con fondo de color semitransparente, métrica grande, y el indicador de tendencia en verde (positivo) o rojo (negativo).

---

## ✅ Verificación

- El bloque 1: al pasar el ratón sobre la card, la imagen hace zoom suave sin desbordar
- El bloque 2: el título cambia a azul en hover; el excerpt corta en 3 líneas con `...`
- El bloque 3: el anillo del avatar cambia de gris a sky en hover
- El bloque 4: la flecha ▲ está en emerald y ▼ en rojo según la tendencia
