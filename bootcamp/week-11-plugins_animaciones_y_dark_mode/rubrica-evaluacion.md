# 📊 Rúbrica de Evaluación — Semana 11

**Bootcamp TailwindCSS Zero to Hero** | Semana 11: Plugins, Animaciones y Dark Mode

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Plugin Typography (`prose`)** | Explica qué hace el plugin: aplica estilos tipográficos a HTML generado (markdown); sabe usar `prose`, `prose-sm/lg/xl`, `prose-invert` para dark; personaliza con `prose-headings:`, `prose-links:`; entiende por qué existe (HTML dinámico no tiene clases) | Usa `prose` correctamente; sabe que `prose-invert` es para dark mode; no personaliza variantes de prose | Aplica clases prose sin el plugin instalado; confunde prose con fuentes o con tipografía del config |
| **@tailwindcss/forms** | Explica que el plugin normaliza estilos de formularios entre navegadores; sabe que strategy `class` requiere agregar la clase al elemento, `base` la aplica globalmente; customiza inputs con `form-input`, `form-select`; combina con variantes `focus:` | Usa el plugin con la estrategia `base`; los formularios se ven bien en todos los browsers; no conoce la estrategia `class` | Extiende estilos de inputs sin el plugin; los formularios son inconsistentes entre navegadores |
| **Animaciones built-in vs custom** | Diferencia las 4 animaciones built-in (`spin/pulse/bounce/ping`); sabe para qué sirve cada una; define `@keyframes` custom en config con `animation` y `keyframes`; usa la utilidad generada con `animate-{nombre}` | Usa `animate-spin`, `animate-pulse`; define 1 animación custom en config; no combina `duration/delay` correctamente | Solo usa animaciones inline CSS; no sabe que Tailwind genera clases de animación desde los keyframes del config |
| **`motion-safe:` y `motion-reduce:`** | Sabe que `prefers-reduced-motion: reduce` es una media query de accesibilidad; wrap todas las animaciones con `motion-safe:animate-*` para respetarla; entiende la diferencia entre `motion-safe` (aplica SI reduce está off) y `motion-reduce` (aplica SI está on) | Conoce `motion-safe:` y lo aplica en algunas animaciones; no conoce `motion-reduce:` | Aplica todas las animaciones sin considerar preferencias del usuario |
| **Dark Mode: `class` vs `media`** | Diferencia estrategia `class` (programática, usa `dark:` cuando `<html class="dark">`) vs `media` (respeta `prefers-color-scheme` del SO); sabe cuándo usar cada una; implementa toggle JS con `localStorage` para persistir preferencia del usuario | Implementa dark mode con estrategia `class`; toggle funcional; sin persistencia en localStorage | Implementa dark mode solo con CSS `@media (prefers-color-scheme: dark)`; no sabe crear toggle |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Typography Plugin** | Instala/carga el plugin y aplica `prose` a un bloque de HTML; customiza tamaño con `prose-lg`; aplica `prose-invert` en dark mode; personaliza `prose-headings:text-brand-700`, `prose-links:text-brand-500` | Aplica `prose` y `prose-invert`; texto de artículo bien formateado; sin customización de variantes | Aplica `prose` pero sin el plugin (no hay efecto); los headings y párrafos tienen estilos incorrectos |
| **Ejercicio Animaciones** | Loader con `animate-spin`, skeleton con `animate-pulse`, CTA con `animate-bounce`; animación custom `fade-in` definida en keyframes del config; todo wrapped con `motion-safe:` | Usa 3 animaciones built-in correctamente; 1 custom en config; sin `motion-safe:` | Solo usa `animate-spin`; no define animaciones custom; `transition` mal configurado |
| **Ejercicio Dark Mode** | Toggle funcional con `document.documentElement.classList.toggle('dark')`; preferencia persiste en `localStorage`; aplica `dark:bg-*/dark:text-*` en todos los elementos; sistema de color coherente en ambos modos | Toggle funcional; dark mode aplicado correctamente; sin `localStorage`; algún elemento sin dark: | Toggle no funciona; usa `media` en lugar de `class`; menos del 50% de los elementos con variante dark: |
| **Ejercicio Accesibilidad** | `sr-only` en iconos sin texto visible; `focus-visible:ring-*` en todos los elementos interactivos; contraste WCAG AA (≥4.5:1) en todos los textos; atributos `aria-label` donde corresponde; anima solo con `motion-safe:` | `sr-only` y `focus-visible:` aplicados; contraste en la mayoría de elementos; sin `aria-label` en todos los botones | Sin `sr-only`; sin `focus-visible:`; contraste bajo en textos secundarios |

---

## 📦 Producto (30%)

**Proyecto: Blog con Dark Mode**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Toggle dark mode funcional** | Toggle persiste en `localStorage`; detecta preferencia del SO (`prefers-color-scheme`) en primera carga; animación del toggle usando `transition-colors`; botón con `aria-label` y estado `aria-pressed` | Toggle funcional con `localStorage`; sin detectar preferencia del SO | Toggle funciona pero no persiste al recargar; sin `localStorage` |
| **Plugin Typography en artículo** | Contenido del artículo con `prose prose-lg max-w-prose mx-auto`; `dark:prose-invert`; personaliza `prose-headings:font-display prose-a:text-sky-500` con colores del tema | Aplica `prose` y `prose-invert`; texto bien formateado; sin personalización de variantes | Artículo sin plugin Typography; headings y párrafos sin jerarquía visual |
| **Animaciones con accesibilidad** | Animación en hero con `motion-safe:animate-fade-in` (keyframe custom); transiciones en hover con `motion-safe:transition-*`; sin animación en elementos que no requieren atención | 1-2 animaciones con `motion-safe:`; transiciones en botones correctas | Animaciones sin `motion-safe:`; uso de `animate-bounce` en elementos que no requieren llamada de atención |
| **Accesibilidad general** | Todos los botones con `aria-label` o texto visible; contraste verificado con DevTools; `focus-visible:ring-2` en todos los interactivos; headings con jerarquía correcta (h1→h2→h3) | La mayoría de elementos accesibles; algunos iconos sin aria-label; focus visual presente | Sin estrategia de accesibilidad; botones-icono sin label; foco invisible |
| **Coherencia dark/light mode** | Todos los fondos, textos, bordes y sombras tienen variante `dark:`; el blog se ve bien en ambos modos sin elementos "rotos" visualmente | Dark mode funcional con 1-2 elementos sin adaptar | El dark mode deja fondos blancos sobre texto blanco o viceversa |
| **Calidad de código** | HTML semántico (`article`, `aside`, `time`, `mark`); config con animaciones custom nombradas; no CSS inline; responsive mobile-first | HTML mayormente semántico; algunas clases redundantes | Estructura con solo `div`; sin semántica HTML |
