# 📊 Rúbrica de Evaluación — Semana 6

**Bootcamp TailwindCSS Zero to Hero** | Semana 6: Flexbox Utilities

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Contenedor vs. Ítem** | Explica la diferencia entre el contenedor flex (donde se aplica `flex`) y los ítems flex (los hijos directos); sabe que propiedades como `justify-content` van al contenedor y `align-self` al ítem | Diferencia correctamente en la mayoría de los casos; confunde alguna propiedad de ítem con la de contenedor | Aplica clases de contenedor a los ítems o viceversa sin entender la distinción |
| **Eje principal vs. eje cruzado** | Explica que en `flex-row` el eje principal es horizontal (justify) y el cruzado es vertical (items); en `flex-col` se invierten; aplica el razonamiento correctamente | Usa `justify-*` e `items-*` correctamente en `flex-row`; se confunde al cambiar a `flex-col` | Confunde `justify-*` e `items-*` en ambas direcciones |
| **flex-1 y flex-none** | Sabe que `flex-1` expande el ítem para ocupar el espacio disponible y que `flex-none` fija su tamaño; entiende `flex-auto` y `flex-initial` | Usa `flex-1` para crear áreas de contenido y `flex-none` para sidebars; no conoce `flex-auto` | No sabe cuándo usar `flex-1`; usa `width: 100%` manual en lugar de `flex-1` |
| **gap vs. margin** | Prefiere `gap-*` sobre `margin` para espaciado entre ítems flex; sabe que `gap` no añade espacio exterior al contenedor | Usa `gap-*` correctamente; a veces añade márgenes redundantes | Usa `space-x-*` o `margin` manual en lugar de `gap` |
| **flex-wrap** | Distingue `flex-wrap` (ítems saltan de línea), `flex-nowrap` (nunca saltan) y `flex-wrap-reverse`; sabe que sin wrap los ítems se comprimen | Usa `flex-wrap` para evitar desbordamiento; desconoce `flex-wrap-reverse` | Los ítems se desbordan y no aplica wrap para solucionarlo |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Flex Básico** | Activa flex, cambia de fila a columna, aplica wrap con gap; el layout se comporta exactamente como los comentarios indican | Completa 3 de los 4 bloques; wrap o gap con pequeños errores | Solo completa el bloque 1; no logra flex-col o wrap |
| **Ejercicio Justify y Align** | Demuestra todas las variantes de `justify-*` e `items-*` correctamente; usa `self-*` para alinear un solo ítem | Demuestra correctamente `justify-between`, `items-center`; falla en `justify-evenly` o `self-*` | Solo demuestra `justify-center` e `items-center`; desconoce el resto |
| **Ejercicio Flex Grow/Shrink** | Crea layout con sidebar fijo (`flex-none`) y contenido expansible (`flex-1`); entiende `grow` y `shrink` de forma aislada | Crea la combinación `flex-none` + `flex-1`; no refuerza grow/shrink individualmente | No logra la distribución sidebar + contenido usando flexbox |
| **Ejercicio Layouts Comunes** | Navbar con logo + links + CTA usando `justify-between`; footer de 3 columnas con separadores; centrado perfecto; todo el código sin posicionamiento absoluto | Navbar y footer funcionan; el centrado perfecto usa algún truco manual | Implementa uno de los tres patrones; los demás usan posicionamiento absoluto o margin manual |

---

## 📦 Producto (30%)

**Proyecto: Dashboard con Sidebar**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Layout principal** | `flex h-screen`: sidebar con `flex-none w-64` y main con `flex-1 overflow-auto`; sin `position: absolute` para el layout base | Sidebar y main en flex; el main no tiene overflow correcto para scroll interno | Layout roto: sidebar encima del main, o se usa `float`, o `position: absolute` |
| **Sidebar navigation** | Links de nav en `flex flex-col gap-1`; ítem activo destacado con `bg-sky-700` o similar; grupo de ítem con icono + label en `flex items-center gap-3` | Nav en columna; ítem activo diferenciado; icono y label no alineados perfectamente | Nav en columna sin estilo de ítem activo |
| **Header interno** | `flex items-center justify-between` para título de página y acciones; acciones en `flex gap-2` | Header con título y al menos un botón de acción | Solo título, sin botón ni separación justify-between |
| **Responsive** | Sidebar `hidden md:flex`; área de main ocupa pantalla completa en mobile; hay indicación visual del menú mobile | Sidebar oculto en mobile; sin menú alternativo mobile | Sidebar siempre visible o siempre oculto sin toggle |
| **Calidad de código** | Clases en orden consistente; sin clases redundantes; comentarios educativos donde aplique | Clases en orden mayormente correcto; alguna clase duplicada | Clases en orden aleatorio; muchas redundancias |
