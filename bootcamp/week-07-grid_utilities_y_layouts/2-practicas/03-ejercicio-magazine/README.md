# Ejercicio 03: Layout Magazine

## 🎯 Objetivo

Construir un layout estilo revista/blog que usa `col-span-*` para destacar el artículo principal y combina Grid (para la cuadrícula de artículos) con Flexbox (para el interior de cada card).

---

## 📋 Instrucciones

### Paso 1: Grid básico con artículo destacado

Descomenta el **bloque 1** para ver el grid de 3 columnas donde el artículo principal ocupa las 2 primeras columnas (`col-span-2`) y hay una tarjeta lateral en la 3ª. Esta es la base del layout magazine.

### Paso 2: Fila de artículos secundarios

Descomenta el **bloque 2** para añadir una segunda fila con 3 artículos de igual tamaño. Observa cómo fluyen automáticamente después del artículo destacado.

### Paso 3: Sección con `col-span-full` (newsletter CTA)

Descomenta el **bloque 3** para ver cómo `col-span-full` permite insertar un banner que ocupa las 3 columnas, útil para separadores, CTAs y anuncios entre secciones.

### Paso 4: Layout magazine completo responsive

Descomenta el **bloque 4** para ver el layout final responsive: en mobile todos los artículos se apilan en 1 columna; en tablet el destacado ocupa `col-span-2` de 3; en desktop se mantiene la misma estructura.

---

## ✅ Verificación

- El bloque 1 muestra el artículo destacado ocupando 2/3 del ancho
- El bloque 2 muestra la segunda fila con 3 cards iguales
- El bloque 3 muestra el CTA extendido a las 3 columnas
- El bloque 4 es completamente responsive: 1 col en mobile, magazine en desktop
