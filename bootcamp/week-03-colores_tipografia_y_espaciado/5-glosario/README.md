# Glosario — Semana 3: Colores, Tipografía y Espaciado

Términos técnicos clave de la semana, ordenados alfabéticamente.

---

## C

### Contraste (WCAG)
Relación de brillo entre el color del texto y el color del fondo. WCAG AA exige ≥4.5:1 para texto normal y ≥3:1 para texto grande. Herramienta: [contrast-ratio.com](https://contrast-ratio.com/).

### `color/{opacidad}`
Sintaxis moderna de Tailwind para aplicar opacidad a colores. Ejemplo: `bg-sky-500/20` aplica sky-500 con 20% de opacidad. Elimina la necesidad de `bg-opacity-*`.

---

## D

### Design Token
Variable que almacena un valor del sistema de diseño: un color, un tamaño de fuente, un valor de espaciado. En Tailwind v4 se definen en `@theme {}` en el CSS.

---

## J

### Jerarquía tipográfica
La organización visual de los textos en niveles de importancia: título (más grande/grueso), subtítulo (mediano), cuerpo (regular), meta/label (pequeño). Una buena jerarquía guía la mirada sin esfuerzo.

---

## L

### `leading-*` (Line Height)
Clases de Tailwind para controlar el interlineado. `leading-tight` (1.25) para headings, `leading-relaxed` (1.625) para cuerpo de texto. El valor correcto mejora significativamente la legibilidad.

### `line-clamp-{n}`
Clase de Tailwind que limita el texto visible a `n` líneas y agrega elipsis. Requiere `overflow-hidden` internamente. Ideal para tarjetas de contenido donde el texto puede variar en longitud.

---

## P

### Paleta de colores (Tailwind)
Conjunto de ~22 colores base con 11 escalas cada uno (50 a 950). Tailwind genera todas las variaciones internamente: no necesitas un plugin de Sass ni variables personalizadas para los colores default.

---

## S

### Escala de espaciado
El sistema numérico de Tailwind donde cada unidad = 4px (0.25rem). Garantiza que todos los valores de spacing sean múltiplos de 4, lo que produce diseños visualmente consistentes y "cuadrados".

### `space-x-{n}` / `space-y-{n}`
Clases que aplican margen entre elementos hijos de un contenedor flex, sin afectar al primer hijo. Equivalente a `> * + * { margin-left/top: ... }`. Alternativa limpia a margin manual en cada hijo.

---

## T

### `tracking-*` (Letter Spacing)
Clase de Tailwind para el espaciado entre caracteres. `tracking-tight` en headings grandes, `tracking-widest` en etiquetas uppercase. Afecta más la legibilidad de lo que parece.

### `truncate`
Clase de Tailwind que aplica `overflow-hidden`, `text-overflow: ellipsis` y `white-space: nowrap` en una sola clase. El elemento debe tener un ancho definido para que funcione.

---

## W

### WCAG (Web Content Accessibility Guidelines)
Estándares internacionales de accesibilidad web. El nivel AA (2.1) es el mínimo estándar profesional. Tailwind facilita cumplirlo porque la paleta fue diseñada con contraste en mente.
