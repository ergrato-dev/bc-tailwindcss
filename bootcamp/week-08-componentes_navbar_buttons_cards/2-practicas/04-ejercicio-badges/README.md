# Ejercicio 04: Badges y Tags

## 🎯 Objetivo

Construir un sistema completo de badges con los 5 colores semánticos, pills removibles con botón de cierre, tags de categoría y badge numérico de notificación superpuesto sobre un icono.

---

## 📋 Instrucciones

### Paso 1: Los 5 badges de estado semántico

Descomenta el **bloque 1** para ver los 5 badges usando la fórmula `bg-COLOR-500/15 text-COLOR-400`: emerald (success), red (error), amber (warning), sky (info), gray (neutral). Compara cómo el fondo con `/15` crea el efecto "tint" sutil.

### Paso 2: Pills removibles con botón ×

Descomenta el **bloque 2** para ver los chips/pills de filtros activos, cada uno con un botón SVG de cierre que tiene `aria-label` descriptivo y efecto hover con fondo semitransparente.

### Paso 3: Tags de categoría (estilo GitHub)

Descomenta el **bloque 3** para ver las etiquetas de tecnología con borde, fondo oscuro y hover interactivo. Incluye una fila completa de tags de skills de diferentes colores.

### Paso 4: Badge numérico sobre icono

Descomenta el **bloque 4** para ver el patrón `relative` + `absolute`: el botón tiene `relative` y el badge numérico (3, 99+) tiene `absolute right-1 top-1`. Examina cómo manejar números grandes con "99+".

---

## ✅ Verificación

- El bloque 1: cada badge tiene el color semántico correcto (verde=success, rojo=error, etc.)
- El bloque 2: el botón × es pequeño pero visible y tiene área de clic adecuada
- El bloque 3: los tags con colores diferentes son claramente distinguibles
- El bloque 4: el badge "3" aparece en la esquina superior derecha del icono sin salirse
