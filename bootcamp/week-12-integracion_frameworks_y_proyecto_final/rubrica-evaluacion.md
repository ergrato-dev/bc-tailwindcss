# 📊 Rúbrica de Evaluación — Semana 12

**Bootcamp TailwindCSS Zero to Hero** | Semana 12: Integración con Frameworks y Proyecto Final

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Tailwind en React** | Explica cómo configurar Tailwind con Vite y `@tailwindcss/vite`; usa `clsx` y `tailwind-merge` para clases condicionales; entiende por qué se necesita `cn()` helper; sabe que JSX requiere `className` en lugar de `class` | Configura Tailwind en React; usa template literals para clases condicionales; sin `clsx` ni `cn` | No sabe configurar Tailwind en React; confunde `class` con `className`; clases condicionales con concatenación manual es propensa a errores |
| **Tailwind en Next.js** | Describe el App Router y sus convenciones de archivos; configura Tailwind correctamente con `@tailwindcss/vite` o PostCSS; entiende cuándo usar Server vs Client Components con Tailwind; sabe que el purging es automático en producción | Configura Tailwind en Next.js; las páginas se renderizan correctamente; sin comprensión de Server vs Client Components | No logra configurar Next.js App Router; confunde Pages Router con App Router; no sabe qué archivo es el entry point del CSS |
| **daisyUI** | Explica que daisyUI es un plugin de Tailwind que agrega componentes semánticos (`btn`, `card`, `badge`); sabe configurar y cambiar temas con `data-theme`; entiende que los temas usan CSS variables internamente; diferencia daisyUI de shadcn/ui | Instala daisyUI y usa 3+ componentes; cambia el tema del sitio; sin personalización avanzada | Usa las clases de daisyUI sin el plugin instalado; no sabe que requiere configuración en tailwind.config |
| **shadcn/ui** | Explica que shadcn/ui NO es una dependencia sino componentes copiados al proyecto; sabe usar la CLI `npx shadcn@latest add button`; entiende que usa Radix UI para accesibilidad y Tailwind para estilos; puede personalizar un componente | Instala shadcn/ui y usa 2+ componentes; CLI funciona; sin personalización de componentes | Confunde shadcn/ui con una librería de npm estándar; no usa la CLI; copia código sin entender la estructura |
| **Optimización en producción** | Sabe que Tailwind elimina clases no usadas en build automáticamente; entiende la diferencia entre dev (JIT) y build de producción; conoce `tailwind-merge` para evitar conflictos; sabe que las clases dinámicas (concatenación de strings) no se purgan | Sabe que Tailwind purga en producción; sin clases dinámicas problemáticas; sin análisis de bundle | No entiende el purging; crea clases con concatenación de strings problemática; el CSS generado en producción es >100KB |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio React + Tailwind** | Crea un componente `Button` reutilizable con variantes de color y tamaño usando `cn()`; props tipadas que controlan las clases; uso correcto de `className` en JSX; dark mode funcional en React | Componente Button funcional con 2+ variantes; `clsx` o ternario para condicionales; sin dark mode | Componente Button con clases hardcoded; sin variantes; usa `class` en lugar de `className` |
| **Ejercicio Next.js + Tailwind** | Setup completo: `app/layout.tsx` importa CSS global, componente Server y Client Component; `cn()` helper en `lib/utils.ts`; metadata configurada; Tailwind funciona en ambos tipos de componentes | Layout y página funcionales; Tailwind activo; sin distinction Server/Client Components | No logra crear el layout base; CSS de Tailwind no aplica; estructura de archivos incorrecta |
| **Ejercicio daisyUI** | Formulario de contacto completo con `input`, `select`, `checkbox`, `btn`; tabla de datos con `table table-zebra`; toggle de tema entre `light` y `dark` con `data-theme`; 3+ componentes daisyUI diferentes correctamente usados | Formulario con 3+ elementos daisyUI; tema cambia; sin tabla de datos | Solo usa `btn` de daisyUI; sin cambio de tema; formulario con clases Tailwind mezcladas sin criterio |
| **Ejercicio shadcn/ui** | Instala shadcn/ui con CLI; agrega `Button`, `Card`, `Input` y `Badge`; compone una página de dashboard o listado; personaliza al menos 1 componente modificando su archivo; dark mode activo | shadcn/ui instalado y 3+ componentes usados; página funcional; sin personalización de componentes | No logra instalar shadcn/ui correctamente; CLI falla; copia componentes manualmente sin estructura |

---

## 📦 Producto (30%)

**Proyecto: Portfolio Personal Completo**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Setup técnico correcto** | Proyecto en Next.js 15+ o React+Vite con Tailwind v4; `cn()` helper configurado; `@tailwindcss/typography` para sección bio/about; shadcn/ui o daisyUI integrado en al menos 1 sección | Proyecto con Tailwind correcto; sin `cn()`; solo Tailwind sin librería de componentes | Proyecto sin configuración de Tailwind; CSS a mano o Bootstrap; sin setup reproducible |
| **Estructura de contenido** | 5+ secciones completas: Hero, About/Skills, Projects (grid de cards), Experience/Timeline, Contact; NAV con scroll suave y active state; footer con links sociales | 4 secciones: Hero, Projects, Skills, Contact; navegación básica | Solo Hero y Projects; sin estructura de portfolio real |
| **Dark mode funcional** | Toggle dark/light con `localStorage`; clase `dark` en `<html>`; todos los textos, fondos, bordes y sombras con variante `dark:`; transición `transition-colors duration-300` en `body` | Toggle funcional; dark mode en secciones principales; 1-2 elementos sin dark: | Sin dark mode; o dark mode con `prefers-color-scheme` solo, sin toggle |
| **Responsive design** | Mobile-first impecable; layout en móvil (columna), tablet (2 cols), desktop (3+ cols) donde aplica; imágenes y cards adaptadas; NAV colapsable con hamburger en mobile | Responsive funcional; algún breakpoint con overflow o texto cortado | Sin diseño responsive; solo pensado para desktop |
| **Animaciones y transiciones** | Animaciones de entrada en secciones con `motion-safe:animate-*`; `hover:` interacciones en cards, botones y links; transiciones suaves `transition-all duration-300`; `group-hover:` en project cards | Hover transitions en botones y cards; sin animaciones de entrada | Sin animaciones ni transiciones; hover states inexistentes |
| **Accesibilidad** | Todos los botones con `aria-label`; imágenes con `alt` descriptivo; headings en jerarquía h1→h2→h3; `focus-visible:ring-2` en interactivos; contraste WCAG AA verificado; skip-link para navegación por teclado | La mayoría de elementos accesibles; skip-link ausente; algunos `alt` vacíos | Sin `alt` en imágenes; foco invisible; headings desordenados; sin `aria-label` |
| **Calidad de código** | Componentes/funciones con responsabilidad única; clases en orden layout→sizing→spacing→typography→color→effects; sin CSS inline; código comentado donde la lógica no es obvia | Código mayormente organizado; algunas clases redundantes o en mal orden; sin comentarios | Clases sin orden, duplicadas; CSS inline mezclado; estructura de archivos caótica |
