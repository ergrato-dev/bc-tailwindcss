# Glosario — Semana 08: Componentes Navbar, Buttons y Cards

Términos clave de la semana ordenados alfabéticamente.

---

## A

**`animate-spin`**
Clase que aplica `animation: spin 1s linear infinite` al elemento. Hace girar continuamente un icono o SVG. Usado típicamente en spinners de carga dentro de botones.
```html
<svg class="h-4 w-4 animate-spin">...</svg>
```

**`aria-current="page"`**
Atributo HTML de accesibilidad que indica que el enlace apunta a la página actual. Los lectores de pantalla (screen readers) lo anuncian como "actual" o "página actual".
```html
<a href="/" aria-current="page">Home</a>
```

**`aria-label`**
Atributo que provee un nombre accesible a elementos interactivos que no tienen texto visible. Indispensable en icon-buttons.
```html
<button aria-label="Abrir menú de navegación">...</button>
```

---

## B

**Badge**
Elemento visual pequeño que comunica un estado, categoría o conteo. Puede ser un pill `rounded-full`, rectángulo `rounded-md` o tag `rounded-lg`. Principio de diseño: color + forma + texto conciso.

**Backdrop blur**
Efecto de desenfoque del fondo a través de un elemento semitransparente. Se logra con `backdrop-blur-sm` combinado con `bg-gray-950/95` (fondo con 95% de opacidad).
```html
<header class="sticky top-0 bg-gray-950/95 backdrop-blur-sm">
```

---

## C

**Card**
Componente de UI que agrupa información relacionada en un contenedor visual delimitado. En Tailwind: `rounded-2xl bg-gray-800 overflow-hidden`. Tipos comunes: product, blog, user, stat.

---

## D

**`disabled:`**
Variante de Tailwind que se aplica cuando un elemento tiene el atributo `disabled`. Se combina con `pointer-events-none` para prevenir interacción y `opacity-50` para indicar inactividad visualmente.
```html
<button disabled class="disabled:opacity-50 disabled:pointer-events-none">
```

---

## F

**`focus-visible:`**
Variante que aplica estilos solo cuando el elemento recibe foco mediante teclado (no con clic del mouse). Es la forma correcta de estilar el estado de foco sin molestar a usuarios de mouse.
```html
<button class="focus-visible:ring-2 focus-visible:ring-sky-500 focus-visible:ring-offset-2">
```

---

## G

**Ghost button**
Variante de botón con el mínimo énfasis visual: sin fondo, sin borde. Solo el texto con color tenue. Hover agrega un fondo sutil. Útil para acciones secundarias o en zonas ya con mucho color.
```html
<button class="px-5 py-2.5 text-gray-400 hover:bg-gray-800 hover:text-white">
```

**`group`**
Clase que marca un elemento como "grupo padre". Permite que los hijos reaccionen al estado del padre usando variantes como `group-hover:`, `group-focus:`, `group-checked:`.
```html
<div class="group">
  <img class="group-hover:scale-110 transition-transform">
</div>
```

**`group-hover:`**
Variante que se activa cuando el elemento con clase `group` recibe hover. El elemento que usa `group-hover:` puede estar a cualquier nivel dentro del grupo.
```html
<article class="group">
  <img class="group-hover:scale-110 transition-transform duration-300">
  <h3 class="group-hover:text-sky-400 transition-colors">Título</h3>
</article>
```

---

## L

**`line-clamp-{n}`**
Utilidad que trunca el texto después de `n` líneas, añadiendo `...` al final. Requiere `overflow-hidden` implícitamente. Valores: `line-clamp-1` hasta `line-clamp-6`.
```html
<p class="line-clamp-2">Texto largo que será recortado después de 2 líneas...</p>
```

---

## O

**`overflow-hidden`**
Oculta todo contenido que sobresale del elemento. Indispensable en cards con imágenes para que el efecto `group-hover:scale-110` de la imagen no se salga del contenedor.
```html
<div class="overflow-hidden rounded-2xl">
  <img class="group-hover:scale-110 transition-transform">
</div>
```

---

## P

**`peer`**
Clase que marca un elemento como "par" o hermano de referencia. Permite que el siguiente hermano en el DOM reaccione a su estado usando variantes como `peer-checked:`, `peer-focus:`.
```html
<!-- El input es el "peer" -->
<input type="checkbox" id="toggle" class="peer hidden">
<!-- El siguiente hermano puede reaccionar a peer-checked -->
<div class="hidden peer-checked:flex">Menú</div>
```

**`peer-checked:`**
Variante que se activa cuando el elemento marcado con `peer` está en estado `checked` (checkboxes, radio buttons). La técnica clásica para menús mobile sin JavaScript.

**Pill**
Badge o botón con bordes completamente redondeados: `rounded-full`. Diferencia visual de un badge rectangular `rounded-md`.

**Primary button**
Variante de botón con el mayor énfasis visual. En el sistema de diseño del bootcamp: `bg-sky-500 hover:bg-sky-400 text-white`.

---

## R

**`ring`**
Sombra/borde exterior implementada con `box-shadow`. Útil para indicadores de foco o bordes de avatar. Clases: `ring-{width}`, `ring-{color}`, `ring-offset-{width}`.
```html
<!-- Avatar con ring que cambia en hover usando group -->
<div class="ring-4 ring-gray-700 group-hover:ring-sky-500 transition-all">
```

---

## S

**`scale-{value}`**
Transforma el tamaño del elemento mediante `transform: scale()`. Con `group-hover:scale-110` se aganda 10% cuando el padre recibe hover. Requiere `overflow-hidden` en el contenedor para no derramarse.

**`sticky`**
Posicionamiento que se comporta como `relative` hasta que el scroll alcanza el offset definido, momento en que se vuelve `fixed`. `sticky top-0` es la base de navbars que siguen el scroll.
```html
<header class="sticky top-0 z-50">
```

---

## T

**`transition-*`**
Familia de clases que activan las transiciones CSS. `transition-colors` anima solo cambios de color. `transition-transform` anima transforms (scale, translate). `transition-all` anima todo (más costoso).

**`truncate`**
Aplica `overflow: hidden`, `text-overflow: ellipsis` y `white-space: nowrap`. Recorta texto de una sola línea con `...`. Para múltiples líneas usar `line-clamp-{n}`.
```html
<h3 class="truncate">Título muy largo que no cabe en el contenedor...</h3>
```

---

## Z

**`z-50`**
Controla el apilamiento (`z-index: 50`). Los navbars sticky necesitan `z-50` para superponerse al contenido de la página al hacer scroll. Escala de Tailwind: `z-0`, `z-10`, `z-20`, `z-30`, `z-40`, `z-50`.

---

> 📖 Consulta la [documentación oficial de TailwindCSS](https://tailwindcss.com/docs) para referencia completa de cada utilidad.
