# 📊 Rúbrica de Evaluación — Semana 5

**Bootcamp TailwindCSS Zero to Hero** | Semana 5: Responsive Design y Mobile-First

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Filosofía Mobile-First** | Explica por qué se diseña desde el viewport más pequeño hacia arriba; entiende que las variantes `sm:`, `md:` etc. son **min-width** | Aplica mobile-first correctamente aunque no articule bien el porqué | Confunde mobile-first con max-width o aplica breakpoints de forma aleatoria |
| **Breakpoints de Tailwind** | Memoriza o puede consultar los 6 breakpoints (`sm` 640, `md` 768, `lg` 1024, `xl` 1280, `2xl` 1536) y elige el adecuado para cada componente | Usa `sm:`, `md:`, `lg:` correctamente; confunde `xl` y `2xl` | Aplica un solo breakpoint para todo o los usa al revés (large-first) |
| **Container y Breakpoints** | Sabe usar `container mx-auto px-4 sm:px-6 lg:px-8` y entiende la diferencia entre `container` y `max-w-7xl mx-auto` | Centra contenedores con `mx-auto`; no domina el padding responsivo | No sabe centrar un contenedor o usa padding fijo que rompe en móvil |
| **Visibilidad Responsive** | Usa `hidden sm:block`, `sm:hidden`, `block md:hidden` con claridad; entiende que son combinaciones de display | Oculta/muestra elementos en 2 breakpoints; se confunde en 3+ | Usa `display: none` en CSS externo en lugar de variantes de Tailwind |
| **Estrategia de imágenes responsive** | Aplica `w-full h-auto`, `aspect-ratio` y `object-cover` para imágenes adaptables; conoce el atributo `srcset` | Usa `w-full` en imágenes correctamente; desconoce aspect-ratio responsive | Las imágenes se deforman o desbordan en mobile |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Breakpoints** | Visualizador de breakpoints completamente funcional; el indicador cambia en los 5 puntos correctos | Funciona en 3-4 breakpoints; falla en el más pequeño o más grande | No cambia o todos los breakpoints muestran lo mismo |
| **Ejercicio Layout Responsive** | Grid de 1→2→3→4 columnas según breakpoints; navegación se transforma correctamente | Grid funciona en 2-3 tamaños; navegación mobile parcial | Layout no cambia entre mobile y desktop |
| **Ejercicio Tipografía Responsive** | Texto escala correctamente: `text-2xl md:text-4xl lg:text-6xl`; espaciado también escala | Tipografía escala en 2 tamaños correctamente | Tipografía fija en todos los tamaños |
| **Ejercicio Navegación Responsive** | Navbar con hamburger en mobile, links horizontales en desktop usando solo Tailwind + checkbox hack | Navbar se transforma; hamburger no es completamente funcional | Navbar no cambia; links siempre visibles o siempre ocultos |

---

## 📦 Producto (30%)

**Proyecto: Landing Page Responsive**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Hero Section** | Texto escala con `text-3xl md:text-5xl lg:text-7xl`; layout cambia de columna a fila en `md:`; imagen se posiciona correctamente | Hero funcional en mobile y desktop; tipografía escala en 2 tamaños | Hero roto en mobile o no se adapta |
| **Grid de Features** | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` correctamente aplicado | Grid de 1 a 2 columnas | Sin grid; columna única siempre |
| **Navegación** | Navbar completamente responsive con hamburger funcional | Navbar con logo y links; sin hamburger | Navbar fixed que no funciona en mobile |
| **Footer** | Columnas de footer: `grid-cols-1 md:grid-cols-3`; links se apilan en mobile | Footer con 2 columnas responsive | Footer sin estructura responsive |
| **Mobile-First verificado** | Se puede verificar en DevTools mobile (iPhone SE, Pixel) sin scroll horizontal ni overflow | Funciona en mobile con mínimos problemas | Scroll horizontal en mobile o layout roto |
