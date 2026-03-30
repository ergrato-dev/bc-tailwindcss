# 📊 Rúbrica de Evaluación — Semana 10

**Bootcamp TailwindCSS Zero to Hero** | Semana 10: Tailwind Config y Temas Personalizados

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **theme.extend vs theme** | Explica claramente la diferencia: `theme.extend` agrega sin reemplazar los defaults; `theme.colors` (sin extend) elimina todos los colores de Tailwind; elige cuándo usar cada uno | Sabe que `extend` conserva los defaults; no explica las consecuencias de reemplazar | Confunde ambos; no sabe por qué su paleta default desapareció al usar `theme.colors` |
| **Escalas de color (50→950)** | Define 9 tonos de una paleta brand: 50 (casi blanco) → 500 (color sólido) → 950 (casi negro); entiende que el shade 500 es el color base y los demás son variaciones de luminosidad | Define 3-5 tonos; entiende la numeración pero no la relación luminosidad/número | Define 1-2 colores sueltos sin escala; no entiende la convención de tonos de Tailwind |
| **CSS variables como design tokens** | Declara `--color-brand-primary: #...` en `:root`; úsala con `bg-[var(--color-brand-primary)]` en v3, o con `@theme` en v4; entiende la ventaja: cambiar un token actualiza toda la UI | Declara variables CSS; las usa solo en CSS nativo, no en clases de Tailwind; no sabe `@theme` | Confunde variables CSS con variables JS; no las usa en Tailwind |
| **@layer base/components/utilities** | Diferencía los 3 layers: `base` para reset y estilos globales, `components` para bloques reutilizables, `utilities` para utilidades custom de un solo propósito; sabe que el orden determina la especificidad | Conoce `@layer utilities` y `@apply`; no diferencia cuándo usar `components` vs `utilities` | Escribe CSS sin `@layer`; sus estilos custom no respetan la cascada de Tailwind |
| **@apply: cuándo y cuándo no** | Sabe que `@apply` es útil solo para componentes muy repetidos (`.btn-primary`) que se reutilizan en HTML; rechaza usarlo para one-offs; conoce su limitación: genera CSS estático sin las variantes dinámicas | Usa `@apply` para extraer patrones; lo usa en exceso para estilos de un solo uso | Usa `@apply` para todo porque "es más limpio"; no entiende que hace el CSS más pesado |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Colores de Marca** | Paleta `brand-*` con 9 shades (50/100/200/300/400/500/600/700/800/900/950) correctamente definida en config; usa `bg-brand-500 text-brand-50 border-brand-700` y variantes `hover:bg-brand-600`; incluye escala `dark:` | Paleta con 5+ shades; usa `bg-brand-*` en el HTML; sin variantes hover/dark | Define 2-3 colores brand sin escala; usa valores hardcoded en lugar de la paleta config |
| **Ejercicio Tipografía Custom** | Fuente de Google Fonts importada con `@import` en CSS; registrada como `fontFamily.display` y `fontFamily.body` en el config; usada con `font-display font-body`; escala de `fontSize` custom con `text-hero` y `text-caption` | Fuente importada y registrada; usa `font-display`; sin escala de fontSize extra | Solo cambia el `fontFamily.sans` global; no crea valores nombrados custom |
| **Ejercicio Design Tokens** | CSS variables declaradas en `:root` para colores, spacing y radii; integradas en Tailwind v4 con `@theme` o en v3 con `theme.extend` + `var()`; switch de tema claro/oscuro actualizando solo las variables | Variables CSS declaradas y usadas; theme switch parcial; sin integración completa con config | CSS variables declaradas pero nunca usadas en clases Tailwind; todo hardcoded |
| **Ejercicio Tema Completo** | Config con: paleta brand (9 shades), 2 fuentes custom, 3 valores de spacing extra (`section-sm/md/lg`), breakpoint `xs: 375px`, 2 utilidades `@layer utilities`; toda la UI usa solo clases del tema | Config con colores + fuentes; sin spacing custom ni breakpoints; 1 @layer utility | Config solo con colores; sin fuentes, spacing o utilities custom |

---

## 📦 Producto (30%)

**Proyecto: Landing con Tema de Marca**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Paleta de marca en config** | Paleta `brand-*` con ≥7 shades usada en toda la landing: hero, navbar, botones, secciones; sin usar colores default de Tailwind (sky, indigo, etc.) para elementos de marca | Paleta `brand-*` definida con 4+ shades; usada en 60%+ de los elementos visuales | Paleta definida pero la landing mezcla `brand-*` con colores default Tailwind; inconsistente |
| **Tipografía personalizada** | 2 fuentes custom registradas y usadas: `font-display` para headings, `font-body` para texto; escala de tamaños extendida con al menos `text-hero` | 1 fuente custom registrada y usada de forma consistente en headings | Fuente cargada con `<link>` en HTML pero no registrada en el config de Tailwind |
| **CSS variables y design tokens** | ≥6 tokens declarados en `:root`: colores primarios/secundarios, spacing de sección, radio de borde; integrados con Tailwind; cambiar un token visible afecta toda la landing | 3+ tokens declarados; integrados con `bg-[var(--)]`; no todos los elementos los usan | Tokens declarados en CSS pero no integrados con clases Tailwind |
| **@layer utilities** | ≥2 utilidades custom: ej. `.text-gradient-brand`, `.section-padding`, `.card-hover`; usadas en el HTML como clases normales; respetan el sistema de capas | 1 utilidad custom en `@layer utilities` usada correctamente | `@apply` usado en `@layer components` pero sin utilidades de un solo propósito |
| **Coherencia visual del tema** | La landing tiene una identidad visual clara y diferenciada del tema default de Tailwind; colores, tipografía y espaciado son consistentes en todas las secciones | Tema visualmente diferenciado; 1-2 secciones con inconsistencias de color o tipografía | La landing parece un template genérico de Tailwind; no hay identidad de marca |
| **Calidad de código** | Archivo HTML bien estructurado; config comentada explicando decisiones de diseño; sin hardcoding de valores que deberían estar en el theme; responsive (mobile-first) | Config presente y funcional; responsive parcial; algún valor hardcoded | Sin archivo de config separado; todo con clases arbitrarias `bg-[#...]` inline |
