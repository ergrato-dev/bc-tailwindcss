# 📊 Rúbrica de Evaluación — Semana 8

**Bootcamp TailwindCSS Zero to Hero** | Semana 8: Componentes UI — Navbar, Buttons y Cards

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Navbar con `peer`** | Explica el truco del checkbox oculto + `peer` + `peer-checked:*` para toggle de menú sin JavaScript; sabe agregar `aria-label` al checkbox y al nav | Entiende que `peer` enlaza el estado de un checkbox con otro elemento; no recuerda la sintaxis exacta | No sabe cómo hacer toggle de visibilidad sin JavaScript; usa `display:none` manual o jQuery |
| **Sistema de botones** | Identifica las 5 variantes (primary, secondary, outline, ghost, destructive) y sus diferencias visuales; sabe combinar `focus-visible:ring-2` para accesibilidad de teclado | Conoce 3+ variantes; aplica hover/focus básicos; omite `disabled:opacity-50 disabled:pointer-events-none` | Solo usa un estilo de botón; no diferencia estados ni variantes |
| **group y group-hover** | Sabe poner `group` en el contenedor y `group-hover:translate-y-*` / `group-hover:scale-*` en los hijos; conoce `group/[nombre]` para grupos anidados | Aplica `group-hover:` correctamente en un nivel; no usa grupos nombrados | Confunde `hover:` del propio elemento con `group-hover:` del padre |
| **Cards y truncado** | Aplica `truncate` (1 línea) y `line-clamp-{n}` (n líneas) para texto largo; sabe usar `overflow-hidden` en el contenedor de imágenes para que el `scale` no se salga | Usa `line-clamp-2` en excerpts; no aplica `overflow-hidden` en la card | No controla el desbordamiento de texto ni el overflow de imágenes |
| **Badges semánticos** | Asocia colores correctamente: verde → success, rojo → destructive/error, amarillo → warning, azul → info, gris → neutral; usa fondos con opacidad (`bg-emerald-500/15 text-emerald-400`) | Usa colores semánticos pero sin consistencia; mezcla `bg-red-200 text-red-800` (modo claro) con tema oscuro | Usa colores aleatorios sin significado semántico |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Navbar** | Navbar funcional: logo + links horizontales (ocultos en mobile) + hamburger con `peer` que abre/cierra el menú vertical; sticky con `sticky top-0`; todos los 4 bloques completos | Navbar con hamburger funcional; sin sticky o sin transición de apertura | Solo el nav básico horizontal; sin hamburger ni toggle |
| **Ejercicio Botones** | Los 4 bloques completos: 5 variantes × 3 tamaños; estados `disabled` visibles; botón con spinner animado (`animate-spin`) | 3+ variantes con 2 tamaños; disabled funcional; sin spinner | Solo 1-2 variantes de botón sin controlar tamaños ni estados |
| **Ejercicio Cards** | Las 4 cards con `group-hover:*` funcional; product card con imagen que escala; blog card con `line-clamp-2`; user card con avatar; stat card con incremento de color según tendencia | 3 de las 4 cards; `group-hover` en al menos 2; texto truncado en al menos 1 | Solo 1-2 cards sin efectos hover ni truncado |
| **Ejercicio Badges** | Los 4 bloques: badges de status, pills con `×` de cierre, tags de categorías, badge de notificación numérico con `absolute`; colores semánticos correctos | 3 tipos de badges; colores semánticos en 3+; sin badge numérico | Solo badges de un color; sin distinción semántica |

---

## 📦 Producto (30%)

**Proyecto: Biblioteca de Componentes**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Navbar** | Navbar sticky con hamburger (CSS `peer`) funcional en mobile; links con estado activo marcado; logo + 4+ links + CTA button | Navbar con hamburger funcional pero sin sticky o sin estado activo en links | Navbar solo en desktop; sin menú hamburger |
| **Sección Botones** | Las 5 variantes documentadas visualmente; 3 tamaños; estados hover/focus/disabled; al menos 1 botón con icono | 4 variantes con 2 tamaños; hover funcional; sin icono | 2 variantes de botón sin tamaños ni estados |
| **Grid de cards** | 4+ product cards en `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4`; `group-hover:scale-105` en imágenes; `overflow-hidden` en las cards; `line-clamp-2` en descripciones | 3 cards en grid responsive; hover básico; sin `line-clamp` | 2 cards en fila fija; sin hover ni responsive |
| **Badges y tags** | Al menos 6 badges con los 5 colores semánticos; pills y etiquetas de categoría diferenciadas visualmente | 4 badges con 3+ colores; sin pills | Solo badges de un color |
| **Transiciones** | `transition-*` en todos los elementos interactivos (botones, links, cards, badges con close); `duration-200` o `duration-300` consistente | Transiciones en botones y cards; no en badges ni links | Sin transiciones; los estados cambian abruptamente |
| **Calidad de código** | HTML semántico (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`); clases en orden consistente; ARIA en interactive elements | HTML con `<section>` y `<nav>`; orden de clases mayormente bien | Solo `<div>` y `<span>`; clases en orden aleatorio |
