# Ejercicio 01 — Plugin Typography (prose)

## 🎯 Objetivo

Aprender a usar el plugin `@tailwindcss/typography` para aplicar estilos tipográficos completos a contenido HTML generado dinámicamente (artículos, documentación, contenido de CMS).

---

## 🛠️ Qué vas a construir

Una página de artículo de blog con cuatro etapas de estilizado:
1. Artículo con clase `prose` base
2. Variantes de tamaño: `prose-sm`, `prose-lg`, `prose-xl`
3. Personalización con modificadores de elemento (`prose-headings:`, `prose-a:`)
4. Dark mode con `prose-invert` y toggle

---

## 📁 Estructura

```
01-ejercicio-typography-plugin/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

Abre `starter/index.html` y sigue los pasos descomentando cada bloque.

> 💡 Cada bloque tiene comentarios que explican qué hace cada clase.

---

### 🔵 BLOQUE 1 — Plugin y clase `prose` base

**Concepto**: El plugin Typography aplica estilos tipográficos a todo el HTML hijos de la clase `prose`, sin necesitar clases individuales en cada elemento.

```html
<!-- Ejemplo: CDN con typography plugin -->
<script src="https://cdn.tailwindcss.com?plugins=typography"></script>

<!-- Aplicar prose a un artículo -->
<article class="prose max-w-prose mx-auto">
  <h1>Titulo</h1>
  <p>Párrafo con estilos automáticos...</p>
  <code>código inline</code>
  <blockquote>Cita...</blockquote>
  <ul><li>Item 1</li></ul>
</article>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — Modificadores de tamaño

**Concepto**: `prose-sm/lg/xl/2xl` controlan el tamaño base de todos los elementos del artículo de forma proporcional.

```html
<!-- Combinar prose con modificador de tamaño -->
<article class="prose prose-lg max-w-prose mx-auto">...</article>
<article class="prose prose-xl max-w-prose mx-auto">...</article>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — Modificadores de elemento

**Concepto**: Se puede personalizar cualquier elemento HTML dentro de `prose` usando sus modificadores específicos: `prose-headings:`, `prose-a:`, `prose-code:`, `prose-blockquote:`.

```html
<article class="prose prose-lg
  prose-headings:text-sky-700
  prose-a:text-sky-600
  prose-a:no-underline hover:prose-a:underline
  prose-code:bg-sky-50 prose-code:text-sky-700 prose-code:rounded
  prose-blockquote:border-sky-400
  max-w-prose mx-auto">
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3.

---

### 🔵 BLOQUE 4 — `prose-invert` y dark mode

**Concepto**: `prose-invert` adapta todos los colores del plugin para fondos oscuros. Se usa junto con la variante `dark:`.

```html
<script>
  tailwind.config = { darkMode: 'class' }
</script>

<article class="prose prose-lg dark:prose-invert max-w-prose mx-auto">
  <!-- Mismo HTML — los colores se invierten con dark mode activo -->
</article>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Criterios de Verificación

- [ ] El artículo tiene estilos tipográficos completos sin ninguna clase en los elementos hijos
- [ ] La clase `prose-lg` hace los textos visiblemente más grandes que `prose` sin modificador
- [ ] Al personalizar con `prose-headings:text-sky-700`, los h2 y h3 también cambian de color
- [ ] En dark mode, el texto pasa a ser claro y los headings se adaptan automáticamente
- [ ] El ancho del artículo está limitado con `max-w-prose` para legibilidad óptima
