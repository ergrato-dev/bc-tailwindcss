# Blog con Dark Mode — Proyecto Semana 11

## 🎯 Objetivo

Construir una página de artículo de blog completa que integre los cuatro temas de la semana:
- Plugin Typography para el contenido del artículo (`prose`)
- Animaciones y transiciones accesibles (`motion-safe:`)
- Dark mode con toggle persistente en `localStorage`
- Accesibilidad completa: contraste WCAG AA, `sr-only`, `focus-visible:`, `aria-*`

---

## 🛠️ Qué vas a construir

Una página de blog con:

1. **Header sticky** con logo, navegación y toggle dark/light (`localStorage`)
2. **Hero del artículo** con imagen de cover, título, metadata y animación `fade-in`
3. **Contenido editorial** con plugin Typography (`prose prose-lg dark:prose-invert`)
4. **Sidebar** con artículos relacionados y newsletter
5. **Footer** con branding y links

---

## 📁 Estructura

```
blog-con-dark-mode/
├── README.md
└── starter/
    └── index.html       ← Edita este archivo
```

---

## 📋 Instrucciones

Abre `starter/index.html`. El archivo tiene la estructura base con secciones marcadas como `TODO`.

Lee las instrucciones en cada TODO antes de implementar. Los hints indican las clases específicas que debes usar.

---

## ✏️ Áreas a Completar

### 1. Header sticky con dark mode toggle

```html
<!-- TODO: Header sticky con nav responsive -->
<!-- Pistas:
  - sticky top-0 z-10 para que quede sobre el contenido
  - bg-white dark:bg-gray-900 con border-b dark:border-gray-700
  - Logo con text-gray-900 dark:text-gray-100
  - Toggle button con aria-pressed y aria-label
  - Íconos del sun/moon con dark:hidden y hidden dark:block
-->
```

### 2. Hero section con animación

```html
<!-- TODO: Hero section del artículo -->
<!-- Pistas:
  - Imagen de cover con aspect-[21/9] object-cover
  - Título con motion-safe:animate-fade-in
  - Meta info (autor, fecha, tiempo de lectura) con time datetime="..."
  - Badges de categorías con rounded-full
  - Todo con variantes dark: correspondientes
-->
```

### 3. Contenido con prose

```html
<!-- TODO: Artículo con plugin Typography -->
<!-- Pistas:
  - prose prose-lg dark:prose-invert max-w-prose mx-auto
  - Personaliza con prose-headings:, prose-a:, prose-code:
  - Incluye: h2, p, ul, blockquote, pre>code, img
  - Los elementos hijos NO necesitan clases Tailwind
-->
```

### 4. Sidebar con contenido relacionado

```html
<!-- TODO: Sidebar con artículos relacionados y newsletter -->
<!-- Pistas:
  - aside con bg-white dark:bg-gray-900 rounded-2xl
  - Cards de artículos relacionados con hover:shadow y transition
  - Input de newsletter con focus-visible:ring-2
  - Todos los textos con variantes dark: correctas
-->
```

### 5. Script de dark mode

```javascript
// TODO: Script de inicialización del tema
// Pistas:
//   - Leer localStorage.getItem('theme')
//   - Detectar window.matchMedia('(prefers-color-scheme: dark)').matches
//   - Aplicar document.documentElement.classList.add/remove('dark')
//   - Función toggleTheme() que guarda en localStorage
//   - Actualizar aria-pressed del botón y cambiar ícono
```

---

## ✅ Criterios de Evaluación

### Funcionalidad

| Requisito | Verificado |
|-----------|-----------|
| Toggle funciona correctamente (claro ↔ oscuro) | ☐ |
| Preferencia persiste al recargar | ☐ |
| Primera carga detecta preferencia del sistema operativo | ☐ |
| Artículo formateado correctamente con `prose prose-lg dark:prose-invert` | ☐ |
| Animación del hero con `motion-safe:animate-fade-in` | ☐ |

### Accesibilidad

| Requisito | Verificado |
|-----------|-----------|
| Botón toggle con `aria-pressed` y `aria-label` | ☐ |
| Íconos decorativos con `aria-hidden="true"` | ☐ |
| Todos los elementos interactivos con `focus-visible:ring-*` | ☐ |
| Contraste de textos ≥4.5:1 en ambos modos | ☐ |
| Jerarquía de headings correcta (h1→h2→h3) | ☐ |

### Calidad de Código

| Requisito | Verificado |
|-----------|-----------|
| HTML semántico: `header`, `main`, `article`, `aside`, `footer`, `time` | ☐ |
| Clases en orden: layout → sizing → spacing → colors → effects | ☐ |
| Sin elementos "rotos" en dark mode | ☐ |
| Responsive: funciona en mobile y desktop | ☐ |

---

## 🔗 Recursos

- [Tailwind Typography Plugin](https://tailwindcss.com/docs/typography-plugin)
- [Tailwind Dark Mode](https://tailwindcss.com/docs/dark-mode)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [MDN: prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
