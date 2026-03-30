# Glosario — Semana 10: Tailwind Config y Temas Personalizados

Términos clave ordenados alfabéticamente.

---

## @apply

Directiva CSS de Tailwind que permite usar clases de utilidad dentro de reglas CSS en `@layer components` o `@layer base`.

```css
.btn-primary {
  @apply px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600;
}
```

> ⚠️ Usar con moderación. Solo en `@layer components` para estilos que se repiten mucho. En HTML propio, es mejor poner las clases directamente.

---

## @layer base

Capa de cascade de Tailwind para estilos globales de bajo nivel: reset, estilos de elementos HTML, variables CSS.

```css
@layer base {
  *, *::before, *::after { box-sizing: border-box; }
  :focus-visible { @apply outline-2 outline-offset-2 outline-blue-500; }
}
```

---

## @layer components

Capa de cascade de Tailwind para clases de componente reutilizables. Tiene menor especificidad que `@layer utilities`, lo que permite sobreescribirlas con utilidades.

```css
@layer components {
  .card { @apply rounded-xl bg-white shadow-md p-6; }
}
```

---

## @layer utilities

Capa de cascade de Tailwind para utilidades custom. Tiene la mayor especificidad de las tres capas. Se usa para clases que no existen en Tailwind por defecto.

```css
@layer utilities {
  .text-gradient-brand {
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
  }
}
```

---

## @theme (Tailwind v4)

Directiva CSS nueva en Tailwind v4 para definir el design system directamente en CSS, sin necesidad de `tailwind.config.js`.

```css
@import "tailwindcss";

@theme {
  --color-brand-500: #d946ef;
  --font-display: "Plus Jakarta Sans", sans-serif;
  --spacing-section: 6rem;
}
```

---

## breakpoint

Punto de quiebre donde el diseño cambia según el ancho del viewport. En Tailwind son prefijos de responsivo: `sm:`, `md:`, `lg:`, `xl:`, `2xl:`. Se pueden añadir breakpoints custom en `theme.extend.screens`.

```javascript
screens: { xs: '375px' } // → usa xs:grid-cols-2
```

---

## color token

Token de diseño cuyo valor es un color. Puede ser primitivo (`--primitive-sky-500: #0ea5e9`) o semántico (`--color-primary: var(--primitive-sky-500)`).

---

## content (config)

Clave en `tailwind.config.js` que indica dónde están los archivos HTML/JS/JSX que Tailwind debe escanear para encontrar qué clases se usan. En producción, solo se generan las clases encontradas en esos archivos (tree-shaking).

```javascript
content: ['./src/**/*.{html,js,jsx,tsx}']
```

---

## CSS custom property

También llamada "CSS variable". Valor reutilizable definido con `--` que puede usarse en todo el documento.

```css
:root { --color-primary: #0ea5e9; }
.btn { background-color: var(--color-primary); }
```

---

## design system

Conjunto de principios, componentes y reglas que garantizan consistencia visual en un producto. Incluye paleta de colores, tipografía, espaciado, iconografía y componentes de UI.

---

## design token

La unidad mínima de un design system. Un token almacena un valor de diseño (color, tamaño, espaciado) con un nombre semántico en lugar de un valor crudo.

| Tipo | Ejemplo |
|------|---------|
| Primitivo | `--primitive-sky-500: #0ea5e9` |
| Semántico | `--color-primary: var(--primitive-sky-500)` |
| Componente | `--btn-bg: var(--color-primary)` |

---

## font-face

Regla CSS que carga una fuente personalizada en el navegador. Google Fonts genera el `@import` automáticamente; self-hosting requiere `@font-face` manual.

```css
@font-face {
  font-family: 'MiFuente';
  src: url('/fonts/mi-fuente.woff2') format('woff2');
  font-display: swap;
}
```

---

## fontFamily (config)

Clave en `theme.extend.fontFamily` para registrar fuentes custom. El nombre que elijas se convierte en la clase `font-{nombre}`.

```javascript
fontFamily: { display: ['"Plus Jakarta Sans"', 'sans-serif'] }
// → clase: font-display
```

---

## fontSize (config)

Clave en `theme.extend.fontSize` para tamaños de fuente semánticos. Acepta la sintaxis extendida `[size, { lineHeight, fontWeight, letterSpacing }]`.

```javascript
fontSize: { hero: ['3.5rem', { lineHeight: '1.1', fontWeight: '700' }] }
// → clase: text-hero
```

---

## primitivo (token)

Token de nivel más bajo. Contiene un valor crudo sin significado contextual. Nunca se usa directamente en el HTML; solo los tokens semánticos lo referencian.

```css
--primitive-sky-500: #0ea5e9;   /* primitivo */
--color-primary: var(--primitive-sky-500);  /* semántico */
```

---

## purge / tree-shaking

Proceso por el que Tailwind elimina del CSS de producción todas las clases que no se usan en los archivos definidos en `content`. Solo en build de producción. En desarrollo se generan todas las clases.

---

## semántico (token)

Token que describe el propósito de uso, no el valor. Facilita el theming y el dark mode porque cambiar el valor del token actualiza toda la UI.

```css
--color-primary: #0ea5e9;          /* light */
.dark { --color-primary: #38bdf8; } /* dark */
```

---

## spacing (config)

Clave en `theme.extend.spacing` para valores de espaciado custom. Los valores se usan en `p-`, `m-`, `w-`, `h-`, `gap-`, etc.

```javascript
spacing: { section: '6rem', gutter: '1.5rem' }
// → py-section, px-gutter, mt-section, etc.
```

---

## theme (reemplazar)

Cuando defines una clave en `theme` directamente (sin `.extend`), **reemplaza** los valores por defecto de Tailwind. Se pierden todos los tonos de Tailwind para esa clave.

```javascript
// ⚠️ Reemplaza TODOS los colores — ya no existirán gray, red, blue...
theme: { colors: { brand: { 500: '#d946ef' } } }
```

---

## theme.extend

Sub-clave de `theme` que **añade** valores sin reemplazar los de Tailwind. Es la forma correcta en la mayoría de casos: tus custom + todos los defaults de Tailwind.

```javascript
// ✅ Añade brand-* SIN eliminar gray-*, blue-*, etc.
theme: { extend: { colors: { brand: { 500: '#d946ef' } } } }
```
