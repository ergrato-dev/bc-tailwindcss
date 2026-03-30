# 📊 Rúbrica de Evaluación — Semana 7

**Bootcamp TailwindCSS Zero to Hero** | Semana 7: Grid Utilities y Layouts Complejos

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Grid 1D vs 2D** | Explica con precisión que Grid es bidimensional (controla filas Y columnas simultáneamente) y Flex es unidimensional; sabe elegir cuál usar y por qué | Diferencia Grid y Flex en términos generales; puede justificar la elección en casos comunes | Confunde Grid y Flex; usa Grid donde Flex bastaría o viceversa sin razonamiento claro |
| **grid-cols y grid-rows** | Sabe definir columnas con `grid-cols-{n}` (iguales), con valores `fr` (proporcionales) y con `[template]` (personalizado); entiende `auto-fill` y `minmax()` | Define columnas con `grid-cols-{n}` y unidades `fr`; no usa `auto-fill` ni `minmax()` | Solo usa `grid-cols-{n}` con valores fijos; no maneja unidades `fr` |
| **col-span y row-span** | Usa `col-span-*` y `row-span-*` para extender celdas; distingue `col-span-full`; combina `col-start-*` / `col-end-*` para posicionamiento explícito | Usa `col-span-2` y `col-span-full` correctamente en layouts reales; desconoce `col-start/end` | No sabe cómo hacer que un elemento ocupe múltiples columnas |
| **gap, gap-x, gap-y** | Distingue `gap-*` (filas y columnas), `gap-x-*` (solo entre columnas) y `gap-y-*` (solo entre filas); los aplica según el diseño | Usa `gap-*` correctamente; olvida que puede diferenciarse entre `gap-x` y `gap-y` | Usa `margin` o `padding` para separar celdas Grid en lugar de `gap-*` |
| **Grid responsive** | Usa `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` con confianza; conoce `grid-cols-[repeat(auto-fill,minmax(250px,1fr))]` para grids intrínsecos | Aplica breakpoints en columnas Grid; no conoce `auto-fill`/`minmax()` | Define columnas fijas sin breakpoints; el grid se rompe en pantallas pequeñas |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Grid Básico** | Activa grid, aplica `auto-flow`, verifica la diferencia entre `grid-cols-3` fijo y `auto-fill`; todos los bloques funcionan tal como se describe en los comentarios | Completa 3 de los 4 bloques; pequeño error en `auto-flow` o en la comparación `auto-fill` vs fijo | Solo completa bloque 1; no logra aplicar `auto-flow` ni variantes responsivas |
| **Ejercicio Galería Responsive** | Galería que transiciona suavemente de 1 a 2 a 3 columnas con breakpoints; aplica `auto-fill + minmax()` para el bloque extra; ratio de imágenes consistente con `aspect-square` | Galería responsive con breakpoints explícitos (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`); sin `auto-fill` | Galería fija de 3 columnas que se rompe en mobile |
| **Ejercicio Magazine** | `col-span-2` en el artículo destacado; grid de 3 columnas con featured + sidebar; hover effects en las cards; el layout no se rompe con texto largo | Artículo destacado con `col-span-2` funcional; sidebar presente; sin hover effects | No logra extender el artículo a múltiples columnas; layout de una sola columna |
| **Ejercicio Dashboard Grid** | Widgets de stat con distintos tamaños (`col-span-1`, `col-span-2`, `col-span-3`); el grid de 6 columnas acomoda todos los widgets correctamente en desktop y mobile | 3 o más widgets con tamaños diferentes; grid de al menos 3 columnas | Todos los widgets del mismo tamaño en una sola columna |

---

## 📦 Producto (30%)

**Proyecto: Landing Page Completa**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Estructura Grid** | Al menos 3 secciones distintas usan `grid` con columnas definidas; `features` en `grid-cols-1 md:grid-cols-3`; `pricing` en `grid-cols-1 md:grid-cols-3`; `testimonios` en `grid-cols-1 md:grid-cols-2`; `footer` con `grid-cols-2 md:grid-cols-4` | Al menos 2 secciones usan grid correctamente; responsive en al menos una sección | Solo el grid de features; el resto usa div con width manual |
| **Uso coherente de col-span** | Al menos una sección usa `col-span-full` (ej: CTA centrado) o `col-span-2` para destacar un elemento de pricing o testimonios | Usa `col-span-full` en el footer o en un CTA | No usa `col-span-*` en ninguna sección |
| **Flex donde aplica** | Navbar, botones, badge de precio y links del footer usan Flex correctamente; no mezcla Grid donde Flex es más apropiado | Navbar usa Flex; botones y badges sin alineación Flex explícita | Usa Grid para la navbar o botones donde Flex es la opción correcta |
| **Responsive completo** | La landing se ve bien en mobile (320px), tablet (768px) y desktop (1280px); no hay overflow horizontal ni elementos cortados | Se ve bien en mobile y desktop; en tablet algún elemento con overflow menor | Se rompe en mobile; columnas fijas sin breakpoints |
| **Calidad de código** | Clases en orden consistente (layout → sizing → spacing → typography → colors → effects); sin clases duplicadas; HTML semántico (`<section>`, `<article>`, `<nav>`, `<footer>`) | Orden de clases mayormente consistente; HTML con algunas etiquetas semánticas | Clases en orden aleatorio; HTML solo con `<div>` |
