# Ejercicio 01: Grid Básico

## 🎯 Objetivo

Dominar los fundamentos de CSS Grid: activar el contexto grid, controlar el flujo automático de ítems y usar `place-items` para centrar contenido en ambos ejes.

---

## 📋 Instrucciones

### Paso 1: Activar Grid con `grid`

Descomenta el **bloque 1** para ver la diferencia entre un contenedor sin Grid (ítems en bloque) y uno con `grid grid-cols-3`. Observa cómo los 6 elementos se colocan automáticamente en una cuadrícula de 3 columnas.

### Paso 2: Controlar el flujo con `grid-flow-*`

Descomenta el **bloque 2** para comparar `grid-flow-row` (rellena fila por fila, por defecto) contra `grid-flow-col` (rellena columna por columna). Presta atención al orden en que aparecen los números.

### Paso 3: Centrado perfecto con `place-items-center`

Descomenta el **bloque 3** para ver cómo `place-items-center` centra todos los elementos en sus celdas con una sola clase. Compara el resultado con el equivalente en Flexbox.

### Paso 4: `place-self-*` en ítems individuales

Descomenta el **bloque 4** para ver cómo `place-self-*` posiciona cada ítem de forma independiente dentro de su celda, incluso cuando el contenedor no declara alineación alguna.

---

## ✅ Verificación

- El bloque 1 muestra 6 ítems en una cuadrícula de 3×2 perfectamente formada
- El bloque 2 muestra el mismo contenido pero en orden diferente según el flujo (row vs. col)
- El bloque 3 muestra ítems centrados en celdas de altura fija sin usar Flexbox
- El bloque 4 muestra ítems posicionados en start / center / end dentro de su celda
