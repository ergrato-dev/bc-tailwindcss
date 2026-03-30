# Glosario — Semana 5: Responsive Design y Mobile-First

---

## B

### Breakpoint
Punto de quiebre definido por un valor de ancho de viewport en el que el diseño cambia. En Tailwind: `sm` (640px), `md` (768px), `lg` (1024px), `xl` (1280px), `2xl` (1536px). Todos son **min-width**.

### `backdrop-blur`
Efecto de desenfoque de fondo usando `backdrop-filter: blur()`. Usado en navbars con `bg-white/80 backdrop-blur-md` para el efecto glassmorphism.

## C

### Checkbox Hack
Técnica CSS pura para crear menús toggle sin JavaScript. Un `<input type="checkbox">` actúa como estado; su label activa/desactiva la visibilidad de un elemento usando la variante `peer-checked:` de Tailwind.

### `container`
Clase de Tailwind que aplica `max-width` según el breakpoint activo y centra el elemento. Alternativa a `max-w-7xl mx-auto`.

## G

### Glassmorphism
Efecto visual de "vidrio esmerilado" logrado con `bg-white/80 backdrop-blur-md`. Común en navbars sticky.

## M

### Mobile-First
Estrategia de diseño donde el CSS base aplica a pantallas pequeñas y los breakpoints escalan hacia arriba. Las variantes `sm:`, `md:` son **min-width** en Tailwind.

### `min-width` (breakpoint)
Los breakpoints de Tailwind se activan cuando el viewport es **mayor o igual** al valor del breakpoint. Es lo opuesto a `max-width` (desktop-first).

## P

### Progressive Enhancement
Filosofía de desarrollo donde el contenido base funciona en todos los dispositivos y las mejoras visuales/interactivas se añaden progresivamente para dispositivos más capaces. Mobile-first es una aplicación práctica de esta filosofía.

## R

### Responsive Design
Diseño web que adapta el layout, tipografía y componentes al tamaño del viewport, asegurando una experiencia óptima en todos los dispositivos.

## S

### `srcset`
Atributo HTML de `<img>` que permite especificar múltiples fuentes de imagen para diferentes resoluciones o tamaños de viewport. Complemento a `w-full` de Tailwind para imágenes verdaderamente responsive.

### `sticky`
Posicionamiento CSS donde un elemento se comporta como `relative` en el flujo normal pero se adhiere al viewport al hacer scroll. `sticky top-0` en navbars mantiene la barra siempre visible.

## V

### Viewport
El área visible del navegador donde se renderiza la página web. Sus dimensiones (`vw`, `vh`) son la referencia para los breakpoints y unidades como `w-screen`, `h-screen`.

### Visibilidad Responsive
Control de qué elementos son visibles en qué breakpoints usando `hidden md:block` (oculto en mobile, visible en md+) y `block md:hidden` (visible en mobile, oculto en md+).
