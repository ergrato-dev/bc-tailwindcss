# Glosario — Semana 1: HTML Semántico y CSS Esencial

Términos técnicos clave de la semana, ordenados alfabéticamente.

---

## A

### `alt` (texto alternativo)
Atributo obligatorio en `<img>` que proporciona una descripción textual de la imagen. Usado por lectores de pantalla, motores de búsqueda y mostrado cuando la imagen no carga. Si la imagen es decorativa, usar `alt=""`.

```html
<img src="logo.png" alt="Logo de PixelCraft Studio" />
<img src="divider.svg" alt="" />  <!-- decorativa: alt vacío -->
```

### `aria-current`
Atributo ARIA que indica el elemento "actual" dentro de un conjunto. `aria-current="page"` en el enlace activo del nav le indica al lector de pantalla en qué página está el usuario.

### `aria-label`
Atributo ARIA que provee un nombre accesible cuando no hay texto visible. Esencial en `<nav>` cuando hay múltiples navegaciones en la misma página.

```html
<nav aria-label="Navegación principal">...</nav>
<nav aria-label="Navegación del pie de página">...</nav>
```

### `aria-labelledby`
Atributo ARIA que asocia un elemento a un heading visible como su etiqueta. Ayuda a lectores de pantalla a comprender la sección.

```html
<section aria-labelledby="titulo-servicios">
  <h2 id="titulo-servicios">Nuestros Servicios</h2>
</section>
```

---

## B

### Block vs Inline
Comportamiento de visualización de los elementos HTML. Los elementos **block** (`div`, `p`, `h1-h6`, `section`, etc.) ocupan toda la anchura disponible y generan salto de línea. Los elementos **inline** (`span`, `a`, `strong`, `em`) fluyen dentro del texto.

### Box Model
El modelo de caja CSS que describe cómo se calcula el tamaño y espacio de cada elemento HTML. Tiene cuatro capas: **content → padding → border → margin**.

### `box-sizing: border-box`
Propiedad CSS que hace que `width` y `height` incluyan el `padding` y el `border`. Es el comportamiento más predecible y es el reset moderno estándar.

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

---

## C

### Cascade (Cascada)
El algoritmo de CSS que determina qué reglas aplican cuando múltiples reglas apuntan al mismo elemento. Considera: origen de la hoja, especificidad del selector, y orden de aparición.

### `charset`
Atributo de `<meta>` que define la codificación de caracteres del documento. `UTF-8` soporta casi todos los idiomas y caracteres especiales del mundo.

### Content Area
La capa más interna del box model. Es el área donde vive el texto o la imagen del elemento. Se controla con `width` y `height`.

---

## D

### DOCTYPE
Declaración al inicio de todo documento HTML5 que indica al browser el tipo de documento y activa el "modo estándar" de renderizado. Siempre debe ser la primera línea del archivo.

```html
<!DOCTYPE html>
```

---

## E

### `em`
Unidad relativa CSS basada en el `font-size` del **elemento padre**. `1em` = tamaño de fuente del padre. Se usa para espaciado proporcional al texto, pero puede ser impredecible por el efecto de composición (cada nivel hereda y multiplica).

### Especificidad (Specificity)
Peso o "autoridad" de un selector CSS, expresado como tres números (A, B, C):
- **A**: Selectores de ID → `#mi-id` (A=1)
- **B**: Clases, pseudo-clases, atributos → `.mi-clase`, `:hover`, `[type]` (B=1)
- **C**: Elementos y pseudo-elementos → `p`, `::before` (C=1)

Mayor especificidad = mayor prioridad.

---

## H

### HTML Semántico
Uso de elementos HTML por su **significado** en lugar de su apariencia visual. `<nav>` para navegación, `<article>` para contenido autónomo, `<footer>` para pie de página — en vez de usar siempre `<div>`.

### Herencia (CSS Inheritance)
Propiedad técnica que hace que ciertos estilos CSS (principalmente tipográficos) fluyan automáticamente de padre a hijo. `color`, `font-family`, `line-height` se heredan. `border`, `padding`, `background` NO se heredan.

---

## I

### `id`
Atributo HTML que identifica un elemento de forma **única** en el documento. Se usa para anclas (`href="#seccion"`), asociación con labels, y como selector CSS `#id` (aunque este último se desaconseja por especificidad alta).

---

## L

### `lang`
Atributo del elemento `<html>` que declara el idioma principal del documento. Fundamental para lectores de pantalla y correcta pronunciación. También ayuda al SEO local.

```html
<html lang="es">
<html lang="en">
```

### Landmark (HTML5)
Elementos HTML semánticos que sirven como puntos de navegación para tecnologías asistivas: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`.

---

## M

### Margin
La capa exterior del box model. Espacio transparente que separa el elemento de sus vecinos. Los márgenes verticales entre hermanos **colapsan** (el mayor gana).

### Margin Collapsing
Comportamiento CSS donde dos márgenes verticales adyacentes se fusionan tomando el valor del mayor de los dos en lugar de sumarse.

---

## P

### Padding
La capa interna del box model entre el contenido y el borde. Hereda el color de fondo del elemento. El padding NO colapsa.

### `px` (pixel)
Unidad CSS absoluta. 1px = 1 pixel de pantalla (en dispositivos con 1:1 device pixel ratio). Predecible pero no se escala con las preferencias de fuente del usuario. Se recomienda evitar en tamaños de fuente.

---

## R

### `rem`
Unidad relativa CSS basada en el `font-size` del **elemento raíz** (`<html>`). Por defecto `1rem = 16px`. Escala respetando la configuración de fuente del usuario, lo que lo hace accesible. Recomendada para tipografía y espaciado.

### Reset CSS
Conjunto de reglas CSS que elimina o normaliza los estilos por defecto del browser antes de comenzar a estilizar. El más moderno es simplemente `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }`.

---

## S

### Selector (CSS)
Patrón que identifica qué elementos HTML reciben un estilo. Tipos principales: de elemento (`p`), de clase (`.nombre`), de ID (`#nombre`), de pseudo-clase (`:hover`), combinadores (`div > p`).

### Semántica (HTML)
Ver **HTML Semántico**.

### Specificity
Ver **Especificidad**.

---

## U

### Unidades CSS
Sistema de medida en CSS. Absolutas: `px`. Relativas: `rem` (al root), `em` (al padre), `%` (al padre), `vh`/`vw` (al viewport). Para UI accesible se prefieren unidades relativas para textos.

---

## V

### Viewport
El área visible del browser donde se renderiza la página web. Las unidades `vh` (viewport height) y `vw` (viewport width) son relativas a este espacio.

### `viewport` (meta tag)
Etiqueta `<meta>` que controla cómo el browser escala la página en dispositivos móviles. Sin ella, los móviles renderizan páginas como si fueran desktop y luego hacen zoom out.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

---

## W

### WCAG
_Web Content Accessibility Guidelines_. Estándar internacional de accesibilidad web. El nivel **AA** es el mínimo recomendado: incluye contraste de color mínimo de 4.5:1 para texto normal.
