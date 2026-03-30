# Ejercicio 03: Flex Grow y Shrink

## 🎯 Objetivo

Entender cómo los ítems flex crecen y se encogen usando `grow`, `shrink`, `flex-1`, `flex-none` y `flex-auto`. Construir el patrón fundamental de sidebar fijo + contenido expansible.

---

## 📋 Instrucciones

### Paso 1: `grow` — Absorber el espacio libre

Descomenta el **bloque 1** para ver tres escenarios: sin `grow` (espacio vacío), un ítem con `grow` (absorbe todo), y varios ítems con `grow` (espacio repartido equitativamente).

### Paso 2: `shrink-0` — No comprimir imágenes

Descomenta el **bloque 2** para ver una lista de usuarios donde el avatar tiene `shrink-0` y no se comprime aunque el texto sea largo. Compara también el efecto de `min-w-0` para habilitar el truncado de texto.

### Paso 3: `flex-1` vs `flex-none` — El patrón fundamental

Descomenta el **bloque 3** para construir el layout sidebar + main usando `flex-none w-48` para el sidebar y `flex-1` para el área de contenido. Este es el patrón más usado en aplicaciones web.

### Paso 4: Barra de progreso con `flex-1`

Descomenta el **bloque 4** para ver cómo `flex-1` y `flex-none` combinados construyen barras de progreso donde la etiqueta y el porcentaje tienen ancho fijo y la barra se expande para ocupar el espacio central.

---

## ✅ Verificación

- El bloque 1 muestra la diferencia visual entre ítems con y sin `grow`
- El bloque 2 muestra el avatar sin deformarse aunque el contenedor sea pequeño
- El bloque 3 muestra el sidebar a ancho fijo y el main ocupando el resto
- El bloque 4 muestra barras de progreso con la barra expandiéndose al centro
