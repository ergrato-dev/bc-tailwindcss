# Ejercicio 01: Flex Básico

## 🎯 Objetivo

Explorar las propiedades fundamentales de Flexbox: activar el contexto flex, cambiar la dirección de los ítems y controlar el desbordamiento con `flex-wrap`.

---

## 📋 Instrucciones

### Paso 1: Activar Flexbox con `flex`

Descomenta el **bloque 1** para ver la diferencia entre un contenedor con `flex` y uno sin él. Observa cómo los elementos pasan de apilarse verticalmente a alinearse en fila.

### Paso 2: Cambiar dirección con `flex-col`

Descomenta el **bloque 2** para ver cómo `flex-col` invierte la dirección: los ítems se apilan verticalmente incluso aunque tengan `flex` activo.

### Paso 3: Controlar el desbordamiento con `flex-wrap`

Descomenta el **bloque 3** para comparar en la misma pantalla un contenedor con `flex-nowrap` (ítems se comprimen) contra uno con `flex-wrap` (ítems saltan de línea).

### Paso 4: Combinación `flex-wrap` + `gap`

Descomenta el **bloque 4** para ver una lista de tags/chips que se ajusta dinámicamente al ancho del contenedor, usando `flex-wrap` y `gap` en lugar de márgenes manuales.

---

## ✅ Verificación

- El bloque 1 muestra los ítems en fila (con `flex`) y en columna (sin `flex`)
- El bloque 2 muestra ítems apilados verticalmente con `flex-col`
- El bloque 3 muestra la diferencia visual entre `nowrap` (compresión) y `wrap` (salto de línea)
- El bloque 4 muestra los tags ajustándose a múltiples líneas al reducir el ancho del navegador
