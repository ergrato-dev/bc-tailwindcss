# 📖 Glosario — Semana 7: Grid Utilities y Layouts Complejos

Términos técnicos de CSS Grid y Tailwind ordenados alfabéticamente.

---

## A

**`align-content`** (Tailwind: `content-*`)
Alinea las filas del grid cuando hay espacio extra en el eje cruzado del contenedor. Solo tiene efecto cuando el grid tiene menos altura que el contenedor.
```html
<div class="grid content-center">...</div>
```

**`align-items`** (Tailwind: `items-*`)
Alinea todos los ítems en el eje cruzado dentro de su celda. En Grid, el eje cruzado es vertical (por defecto).
```html
<div class="grid items-start">...</div>
```

**`align-self`** (Tailwind: `self-*`)
Alinea un ítem individual en el eje cruzado de su celda, sobreescribiendo `align-items` del contenedor.
```html
<div class="self-end">...</div>
```

**`auto-fill`**
Valor para `repeat()` que crea el máximo de columnas que quepan según el `minmax()`, incluyendo columnas vacías si no hay suficientes ítems.
```css
grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
```

**`auto-fit`**
Como `auto-fill` pero colapsa las columnas vacías, haciendo que los ítems existentes se estiren para ocupar todo el espacio.
```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```

---

## B

**Bento Box Layout**
Patrón de layout popularizado por Apple en sus keynotes: una cuadrícula con celdas de distintos tamaños combinando `col-span-*` y `row-span-*`. Muy usado en secciones de features modernas.

---

## C

**Celda (Grid Cell)**
La unidad más pequeña del grid: la intersección de una fila y una columna. Un ítem ocupa una celda por defecto; con `col-span-*` puede ocupar varias.

**`col-end-*`** (Tailwind)
Especifica en qué línea vertical termina un ítem del grid (1-based desde la izquierda).
```html
<div class="col-end-4">...</div>  <!-- termina antes de la línea 4 -->
```

**`col-span-*`** (Tailwind)
Hace que un ítem ocupe múltiples columnas. `col-span-2` ocupa 2 columnas, `col-span-full` ocupa todas.
```html
<div class="col-span-2">...</div>
```

**`col-start-*`** (Tailwind)
Especifica en qué línea vertical empieza un ítem del grid (1-based desde la izquierda).
```html
<div class="col-start-2">...</div>  <!-- empieza en la línea 2 -->
```

**Contenedor Grid**
El elemento padre al que se le aplica `display: grid`. Sus hijos directos se convierten automáticamente en ítems del grid.

---

## F

**`fr` (fraction unit)**
Unidad de CSS Grid que representa una fracción del espacio disponible en el contenedor. `1fr 2fr` divide el espacio en 3 partes: 1/3 y 2/3.
```html
<div class="grid grid-cols-[1fr_2fr]">...</div>
```

---

## G

**`gap-*`** (Tailwind)
Espacio entre filas y columnas del grid (o flex). Equivalente a `row-gap` + `column-gap` combinados.

**`gap-x-*`** (Tailwind)
Espacio solo entre columnas (horizontal) del grid.

**`gap-y-*`** (Tailwind)
Espacio solo entre filas (vertical) del grid.

**Grid**
El sistema de layout bidimensional de CSS que permite controlar filas y columnas al mismo tiempo. En Tailwind: `class="grid"`.

**`grid-cols-*`** (Tailwind)
Define el número y tamaño de las columnas del grid.
```html
<div class="grid grid-cols-3">...</div>       <!-- 3 columnas iguales -->
<div class="grid grid-cols-[1fr_2fr]">...</div> <!-- proporcional -->
```

**`grid-flow-col`** (Tailwind)
Hace que los ítems del grid se coloquen columna por columna en lugar de fila por fila.

**`grid-flow-dense`** (Tailwind: `grid-flow-row-dense` / `grid-flow-col-dense`)
Rellena los huecos dejados por ítems de mayor tamaño con ítems más pequeños. Útil para layouts tipo masonry.

**`grid-flow-row`** (Tailwind)
Comportamiento por defecto: los ítems se colocan llenando la cuadrícula fila por fila.

**`grid-rows-*`** (Tailwind)
Define el número y tamaño de las filas del grid.
```html
<div class="grid grid-rows-[auto_1fr_auto]">...</div> <!-- header/main/footer -->
```

---

## I

**`inline-grid`** (Tailwind)
Como `grid` pero el contenedor se comporta como elemento inline (se ajusta al tamaño de su contenido en lugar de ocupar todo el ancho).

**Ítem Grid**
El hijo directo de un contenedor grid. Las propiedades de ítem son: `col-span-*`, `row-span-*`, `col-start-*`, `col-end-*`, `self-*`, `justify-self-*`, `place-self-*`, `order-*`.

---

## J

**`justify-content`** (Tailwind: `justify-*`)
Alinea las columnas del grid cuando hay espacio extra en el eje principal.

**`justify-items`** (Tailwind: `justify-items-*`)
Alinea todos los ítems dentro de sus celdas en el eje principal (horizontal en escritura LTR).

**`justify-self`** (Tailwind: `justify-self-*`)
Alinea un ítem individual en el eje principal de su celda.

---

## L

**Layout Magazine**
Patrón de layout que combina un artículo principal de mayor tamaño (`col-span-2`) con artículos secundarios y un sidebar (`col-span-1`) en un grid de 3 columnas.

**Línea de Grid (Grid Line)**
Las líneas imaginarias que dividen el grid en filas y columnas. La numeración empieza en 1 desde la esquina superior izquierda.

---

## M

**`minmax(min, max)`**
Función CSS que define un rango de tamaño para una columna o fila: mínimo y máximo. Se usa con `auto-fill` o `auto-fit` para grids responsivos.
```html
<!-- Columna de mínimo 200px y máximo 1 fracción del espacio disponible -->
<div style="grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))">
```

---

## P

**`place-content-*`** (Tailwind)
Shorthand para `align-content` + `justify-content`. Posiciona el grid completo dentro del contenedor.

**`place-items-*`** (Tailwind)
Shorthand para `align-items` + `justify-items`. Centra todos los ítems en sus celdas en ambos ejes.
```html
<div class="grid place-items-center h-screen">...</div>
```

**`place-self-*`** (Tailwind)
Shorthand para `align-self` + `justify-self`. Posiciona un ítem individual en su celda en ambos ejes.

---

## R

**`row-span-*`** (Tailwind)
Hace que un ítem ocupe múltiples filas. `row-span-2` ocupa 2 filas, `row-span-full` ocupa todas las filas.
```html
<div class="row-span-2">...</div>
```

**`row-start-*`** / **`row-end-*`** (Tailwind)
Posicionamiento explícito de un ítem en filas específicas del grid.

---

## T

**Template de Grid**
La definición de filas y columnas. Se puede hacer con valores fijos (`240px`), fracciones (`1fr`), contenido (`auto`) o funciones (`minmax()`).
```html
<div class="grid grid-cols-[240px_1fr] grid-rows-[auto_1fr_auto]">...</div>
```

---

## Z

**Z-index en Grid**
Los ítems del grid pueden solaparse cuando se les asigna explícitamente la misma posición. El orden de apilamiento se controla con `z-*` como en cualquier elemento posicionado.
