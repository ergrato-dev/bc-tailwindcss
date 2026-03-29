# Glosario — Semana 4: Borders, Shadows, Sizing y Estados

Términos técnicos clave de la semana, ordenados alfabéticamente.

---

## A

### `active:`
Variante de Tailwind que aplica estilos mientras el elemento está siendo presionado (mousedown o touchstart). Útil para feedback táctil en botones: `active:scale-95`.

### `aria-disabled`
Atributo ARIA para indicar que un elemento está deshabilitado sin usar el atributo `disabled` nativo. Tailwind soporta la variante `aria-disabled:` para estilizarlo.

### `aspect-ratio`
Propiedad CSS que mantiene la relación de aspecto de un elemento independientemente de su ancho. `aspect-video` = 16/9, `aspect-square` = 1/1.

---

## B

### `border-radius`
Propiedad CSS para redondear las esquinas de un elemento. En Tailwind: `rounded-sm` (2px) hasta `rounded-full` (9999px).

### Box Shadow
Sombra exterior aplicada al bounding box del elemento. `shadow-sm` a `shadow-2xl` en Tailwind. No sigue la forma del contenido.

---

## D

### `disabled:`
Variante de Tailwind que aplica estilos cuando el elemento tiene el atributo `disabled`. Combinar con `cursor-not-allowed` y `opacity-50` es el patrón estándar.

### `divide-y`
Clase de Tailwind que aplica `border-top` a todos los hijos de un contenedor excepto el primero. Equivalente más limpio que `mt-*` en cada hijo para listas.

### Drop Shadow
Sombra que sigue la forma real del contenido usando `filter: drop-shadow()`. Útil para SVGs e imágenes PNG transparentes. En Tailwind: `drop-shadow-*`.

---

## F

### `focus-visible:`
Variante de Tailwind que solo aplica estilos cuando el foco viene del teclado (no del mouse). Es la variante correcta para el anillo de focus en botones. Mejora la accesibilidad sin penalizar al usuario de mouse.

### `focus-within:`
Variante que aplica estilos al elemento padre cuando cualquier descendiente tiene el foco. Ideal para wrappers de inputs.

---

## G

### `group`
Clase especial de Tailwind que marca un elemento como referencia padre. Sus descendientes pueden reaccionar a los estados del padre usando `group-hover:`, `group-focus:`, etc.

---

## O

### `object-cover`
Valor de `object-fit` que escala la imagen para cubrir completamente el contenedor, recortando si es necesario. El comportamiento equivalente a `background-size: cover`.

### `overflow-hidden`
En contenedores redondeados con imágenes internas, `overflow-hidden` asegura que la imagen no desborde los bordes redondeados del contenedor.

---

## P

### `peer`
Clase especial de Tailwind que marca un elemento de formulario como referencia. Sus siguientes hermanos (siblings) pueden reaccionar a su estado usando `peer-checked:`, `peer-focus:`, `peer-invalid:`, etc.

---

## R

### `ring`
Utilidad de Tailwind que genera un outline visual usando `box-shadow` sin afectar el layout. `ring-2 ring-sky-500 ring-offset-2` es el patrón de focus accesible.

---

## T

### `transition-*`
Clases de Tailwind para activar transiciones CSS. `transition-colors` anima color/fondo, `transition-shadow` anima sombras, `transition-transform` anima transforms. Más específico = mejor rendimiento que `transition-all`.

### Transform
Transformaciones 2D/3D en CSS. En Tailwind: `scale-*`, `translate-*`, `rotate-*`. Se activan en hover con `hover:scale-105`, etc.

---

## V

### Viewport Units
Unidades relativas al viewport: `vw` (viewport width), `vh` (viewport height). En Tailwind: `w-screen` = 100vw, `h-screen` = 100vh, `h-svh` = 100svh (sin barra del browser en móvil).
