# Glosario — Semana 6: Flexbox Utilities

---

## A

### `align-content`
Controla cómo se distribuyen **múltiples líneas** en el eje cruzado cuando hay `flex-wrap`. En Tailwind: `content-start`, `content-center`, `content-end`, `content-between`, `content-around`, `content-evenly`. Solo tiene efecto cuando hay más de una línea de ítems.

### `align-items`
Propiedad CSS que alinea todos los ítems flex en el **eje cruzado**. Se aplica al contenedor. En Tailwind: `items-start`, `items-center`, `items-end`, `items-stretch`, `items-baseline`.

### `align-self`
Propiedad CSS que alinea un **ítem individual** en el eje cruzado, sobreescribiendo el `align-items` del contenedor. En Tailwind: `self-start`, `self-center`, `self-end`, `self-stretch`, `self-auto`.

## B

### `basis-*`
Define el **tamaño base** de un ítem flex antes de que el espacio libre se distribuya. Equivalente a `flex-basis` en CSS. Acepta los mismos valores que `width`: `basis-0`, `basis-auto`, `basis-64`, `basis-1/3`, etc.

## C

### Contenedor Flex
El elemento HTML sobre el que se aplica `display: flex` o `display: inline-flex`. Los hijos directos del contenedor se convierten en **ítems flex** automáticamente.

### Contexto Flex
El ambiente de layout creado por un contenedor flex. Los ítems dentro de este contexto se comportan según las reglas de Flexbox, diferentes al flujo normal del documento.

### Eje Cruzado (Cross Axis)
El eje **perpendicular** al eje principal. En `flex-row`: eje cruzado es vertical. En `flex-col`: eje cruzado es horizontal. Las propiedades `align-items`, `align-self` y `align-content` operan sobre este eje.

### Eje Principal (Main Axis)
El eje a lo largo del cual se colocan los ítems flex. En `flex-row`: es horizontal (izquierda → derecha). En `flex-col`: es vertical (arriba → abajo). Las propiedades `justify-content` operan sobre este eje.

## F

### `flex`
Clase de Tailwind que aplica `display: flex` al elemento, creando un contenedor flex. Los hijos se distribuyen en fila por defecto.

### `flex-1`
Atajo de Tailwind equivalente a `flex: 1 1 0%`. El ítem **crece** para ocupar el espacio disponible, puede encogerse y su tamaño base es 0. El "rellena el resto" de los layouts.

### `flex-auto`
Equivalente a `flex: 1 1 auto`. El ítem crece y se encoge, pero respeta su tamaño intrínseco como punto de partida.

### `flex-col`
Cambia la dirección del eje principal a **vertical** (`flex-direction: column`). Los ítems se apilan de arriba hacia abajo.

### `flex-col-reverse`
Los ítems se apilan de **abajo hacia arriba** (`flex-direction: column-reverse`).

### `flex-initial`
Equivalente a `flex: 0 1 auto` (comportamiento por defecto). El ítem NO crece, pero SÍ puede encogerse.

### `flex-none`
Equivalente a `flex: none` (`flex: 0 0 auto`). El ítem tiene **tamaño completamente fijo**, no crece ni se encoge. Ideal para sidebars, logos y avatares de ancho fijo.

### `flex-nowrap`
Los ítems se mantienen en **una sola línea**, comprimiéndose si es necesario (`flex-wrap: nowrap`). Es el comportamiento por defecto.

### `flex-row`
Dirección horizontal (eje principal de izquierda a derecha). Es el **valor por defecto** cuando se aplica `flex`.

### `flex-row-reverse`
Los ítems se colocan de **derecha a izquierda** (`flex-direction: row-reverse`).

### `flex-wrap`
Los ítems saltan a la **siguiente línea** si no caben en el contenedor (`flex-wrap: wrap`).

### `flex-wrap-reverse`
Los ítems saltan de línea pero las líneas se apilan en orden inverso.

## G

### `gap`
Espacio uniforme entre todos los ítems flex (filas y columnas). Preferible sobre `margin` porque no añade espacio exterior al contenedor. En Tailwind: `gap-2`, `gap-4`, etc. También: `gap-x-*` (solo horizontal) y `gap-y-*` (solo vertical).

### `grow`
Hace que un ítem absorba el **espacio libre** disponible en el contenedor (`flex-grow: 1`). Para desactivar: `grow-0`.

## I

### `inline-flex`
Aplica `display: inline-flex`. El contenedor flex se comporta como un elemento en línea (no ocupa el ancho completo). Útil para botones con icono + texto.

### Ítem Flex
Cualquier **hijo directo** de un contenedor flex. Los nietos NO son ítems flex a menos que su padre también sea un contenedor flex.

## J

### `justify-between`
Distribuye los ítems con el primero al inicio y el último al final, y el espacio sobrante se reparte equitativamente **entre** ellos. El patrón más común para navbars (logo izquierda, acciones derecha).

### `justify-content`
Controla la distribución de los ítems en el **eje principal**. En Tailwind se aplica con las clases `justify-*`.

### `justify-evenly`
Espacio completamente uniforme: igual entre ítems y entre ítems y los bordes del contenedor.

### `justify-around`
Espacio igual **alrededor** de cada ítem. El espacio en los bordes es la mitad del espacio entre ítems.

## M

### `min-w-0`
Truco necesario para que el texto pueda truncarse dentro de un ítem flex. Por defecto, un ítem flex tiene `min-width: auto` (no puede ser más pequeño que su contenido), lo que impide que `truncate` funcione correctamente.

## S

### `shrink`
Permite que un ítem se **comprima** cuando el contenedor es más pequeño que el total de sus ítems (`flex-shrink: 1`). Para desactivar: `shrink-0` — útil en imágenes y avatares.

### Espacio Libre
El espacio que queda en el contenedor flex después de colocar todos los ítems en su tamaño base. Las propiedades `flex-grow` determinan cómo se reparte este espacio.
