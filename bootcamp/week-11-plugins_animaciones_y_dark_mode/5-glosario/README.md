# 📖 Glosario — Semana 11

**Plugins, Animaciones y Dark Mode**

---

## A

**`@keyframes`**
Regla CSS que define los puntos clave de una animación. Cada punto se especifica como un porcentaje (`0%`, `50%`, `100%`) o con las palabras clave `from`/`to`. En Tailwind, se definen en `theme.extend.keyframes` del config para generar clases `animate-{nombre}`.

**`aria-current`**
Atributo ARIA que indica el elemento activo o actual dentro de un set. Valores comunes: `page` (link de nav activo), `step` (paso activo en wizard), `true` (elemento activo genérico). Permite a lectores de pantalla anunciar "actual" o "página actual".

**`aria-expanded`**
Atributo ARIA que indica si un elemento colapsable (acordeón, dropdown, menú) está expandido (`true`) o colapsado (`false`). Debe actualizarse con JavaScript cuando el estado cambia.

**`aria-hidden`**
Atributo que oculta un elemento y todos sus hijos para las tecnologías de asistencia. Usar `aria-hidden="true"` en íconos decorativos para que los lectores de pantalla los ignoren.

**`aria-label`**
Atributo que proporciona un nombre accesible a un elemento cuando no hay texto visible. Esencial en botones que solo contienen íconos: `<button aria-label="Buscar">`.

**`aria-live`**
Atributo que indica a los lectores de pantalla que deben anunciar los cambios en el contenido del elemento automáticamente. Valores: `off` (silencio), `polite` (espera turno), `assertive` (interrumpe).

**`aria-pressed`**
Atributo ARIA para botones de tipo toggle. Valores: `true` (presionado/activo) o `false` (no presionado). Debe actualizarse con JavaScript cuando el estado cambia.

---

## C

**contrast ratio (relación de contraste)**
Medida de la diferencia de luminosidad entre dos colores. Se expresa como `X:1`. WCAG AA requiere ≥4.5:1 para texto normal y ≥3:1 para texto grande e íconos. Se calcula con la fórmula de luminancia relativa.

---

## D

**dark mode**
Modo de visualización con fondos oscuros y texto claro. Reduce la fatiga ocular en condiciones de poca luz. En Tailwind se implementa con la variante `dark:` y la estrategia `class` (controlada por JS) o `media` (automática según el SO).

**`delay-*`**
Familia de utilidades de Tailwind que establece `transition-delay`. Define cuánto tiempo espera antes de que inicie la transición o animación. Valores: `delay-75`, `delay-100`, `delay-150`, `delay-200`, `delay-300`, `delay-500`, `delay-700`, `delay-1000`.

**`duration-*`**
Familia de utilidades de Tailwind que establece `transition-duration` (o `animation-duration`). Define cuánto dura la transición. Valores en milisegundos: 75, 100, 150, 200, 300, 500, 700, 1000.

---

## E

**`ease-*`**
Familia de utilidades de Tailwind para `transition-timing-function`. Controla la curva de aceleración: `ease-linear` (constante), `ease-in` (lento al inicio), `ease-out` (lento al final), `ease-in-out` (lento en ambos extremos).

---

## F

**`focus-visible:`**
Variante de Tailwind equivalente a la pseudo-clase CSS `:focus-visible`. Aplica estilos de foco solo cuando el usuario navega con teclado o un método de entrada que requiere indicador de foco (no con mouse o touch). Esencial para accesibilidad sin afectar la experiencia mouse.

**FOUC (Flash of Unstyled Content)**
Destello de contenido sin estilo que puede ocurrir al cargar una página con dark mode gestionado por JS. Se previene ejecutando un script inline en el `<head>` antes del renderizado, que aplica la clase `dark` inmediatamente.

---

## K

**keyframe**
Punto clave en una animación CSS que define los valores de las propiedades en ese momento específico. Junto con `@keyframes`, los keyframes crean la trayectoria completa de una animación entre su estado inicial y final.

---

## L

**`localStorage`**
API del browser para almacenar pares clave-valor que persisten entre sesiones (no se borran al cerrar la pestaña). Se usa para recordar la preferencia de tema del usuario: `localStorage.setItem('theme', 'dark')`.

---

## M

**`motion-reduce:`**
Variante de Tailwind que aplica una clase solo cuando el usuario tiene activado `prefers-reduced-motion: reduce` en su sistema operativo. Se usa para proporcionar alternativas a las animaciones.

**`motion-safe:`**
Variante de Tailwind que aplica una clase solo cuando el usuario NO tiene activado `prefers-reduced-motion: reduce`. Permite que las animaciones se ejecuten por defecto pero se desactiven automáticamente para los usuarios que lo necesiten.

---

## P

**`prefers-color-scheme`**
Media query CSS que detecta si el sistema operativo del usuario tiene activado el modo oscuro (`dark`) o claro (`light`). En Tailwind, es la base de la estrategia `media` de dark mode.

**`prefers-reduced-motion`**
Media query CSS que detecta si el usuario ha solicitado reducir el movimiento/animaciones en su interfaz. Se activa en el SO (Accessibility → Reduce Motion en macOS/iOS, Similar en Windows/Android). Las variantes `motion-safe:` y `motion-reduce:` de Tailwind responden a esta preferencia.

**`prose`**
Clase principal del plugin `@tailwindcss/typography`. Aplica estilos tipográficos completos a todos los elementos HTML hijos: headings, párrafos, listas, blockquotes, código, imágenes. Especialmente útil para HTMLgenerado desde Markdown.

**`prose-invert`**
Modificador del plugin Typography que adapta los colores de `prose` para fondos oscuros. Invierte la paleta principal para que los textos sean claros. Se usa con `dark:prose-invert` para activarse solo en dark mode.

---

## S

**skip link**
Enlace de accesibilidad que permite a usuarios de teclado y lectores de pantalla saltar bloques de navegación repetitivos e ir directamente al contenido principal. Se implementa con `<a href="#main" class="sr-only focus:not-sr-only">`.

**`sr-only`**
Clase de Tailwind que oculta un elemento visualmente pero lo mantiene accesible para tecnologías de asistencia (lectores de pantalla). Aplica: `position: absolute; width: 1px; height: 1px; clip: rect(0,0,0,0)...`.

---

## T

**`transition`**
Propiedad CSS que define qué propiedades animará el navegador cuando cambien. En Tailwind, `transition` activa cambios suaves en las propiedades más comunes (colors, shadow, transform, opacity). Se combina con `duration-*` y `ease-*`.

---

## W

**WCAG (Web Content Accessibility Guidelines)**
Estándar internacional de accesibilidad web desarrollado por el W3C. WCAG 2.1 nivel AA es el estándar mínimo recomendado para la mayoría de sitios. Define criterios como contraste de color (4.5:1), navegación por teclado, y textos alternativos.

**`will-change-*`**
Utilidades de Tailwind para la propiedad CSS `will-change`. Avisan al browser sobre propiedades que cambiarán próximamente, permitiéndole optimizar el rendering. Usar con moderación: `will-change-transform`, `will-change-opacity`.
