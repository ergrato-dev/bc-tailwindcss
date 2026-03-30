# 📖 Glosario — Semana 9: Forms, Modals y Alertas

Términos clave de la semana ordenados alfabéticamente.

---

## A

**`appearance-none`**
Clase de Tailwind que elimina los estilos visuales nativos del browser en elementos de formulario como `<select>`, `<input type="checkbox">` y `<input type="radio">`. Permite reemplazarlos con estilos CSS personalizados.
```html
<select class="appearance-none ...">...</select>
```

**`aria-describedby`**
Atributo ARIA que vincula un elemento con otro que lo describe. Se usa en campos de formulario para asociar el mensaje de error con el input. El valor es el `id` del elemento que contiene la descripción.
```html
<input aria-describedby="email-error" aria-invalid="true" />
<p id="email-error">Email inválido.</p>
```

**`aria-invalid`**
Atributo ARIA que indica que el valor de un campo de formulario es inválido. Se usa junto con `aria-describedby` para hacer la validación accesible a lectores de pantalla. Valor: `"true"` cuando hay error.

**`aria-label`**
Atributo ARIA que proporciona un nombre accesible a elementos sin texto visible (como icon-buttons o botones dismiss con solo un ícono SVG).
```html
<button aria-label="Cerrar modal">
  <svg .../>
</button>
```

**`aria-live`**
Atributo ARIA que indica a los lectores de pantalla que deben anunciar cambios en el contenido de un elemento. Valores: `"polite"` (espera a que el usuario termine) o `"assertive"` (interrumpe inmediatamente). Se usa en contenedores de notificaciones dinámicas.

---

## B

**`backdrop-blur`**
Utilidad de Tailwind que aplica un desenfoque gaussiano al contenido **detrás** de un elemento. Requiere que el elemento tenga un color de fondo con opacidad (ej. `bg-gray-950/80`). Variantes: `backdrop-blur-sm`, `backdrop-blur`, `backdrop-blur-md`, etc.
```html
<div class="bg-gray-950/80 backdrop-blur-sm">...</div>
```

**Banner**
Componente de notificación de ancho completo que se muestra en la parte superior de la página o sección. Tipicamente usado para anuncios, alertas de mantenimiento o novedades. No confundir con toast.

---

## D

**`disabled:cursor-not-allowed`**
Modificador de estado condicional de Tailwind que aplica `cursor: not-allowed` cuando el elemento tiene el atributo `disabled`. Se combina con `disabled:opacity-50` para indicar visualmente que el campo está inactivo.

**Drawer**
Variante de modal que se presenta como un panel que se desliza desde uno de los lados de la pantalla (normalmente derecha o izquierda). Se usa para navegación secundaria, filtros o configuraciones.

---

## F

**`fieldset`**
Elemento HTML semántico que agrupa campos de formulario relacionados. Se usa principalmente con grupos de `<input type="checkbox">` y `<input type="radio">`. Siempre se acompaña de `<legend>` como su título.

**`fixed inset-0`**
Combinación de clases de Tailwind que posiciona un elemento como `fixed` y lo expande para cubrir todo el viewport (`top: 0; right: 0; bottom: 0; left: 0`). Es la base de los overlays de modal.

**`focus:ring-2`**
Clase de Tailwind que aplica un anillo visual de 2px de ancho cuando el elemento recibe el foco del teclado. Se usa siempre junto con `focus:outline-none` para reemplazar el contorno nativo del browser. Nunca elimines el foco visible sin reemplazarlo.

**Form group**
Patrón de composición HTML que agrupa `<label>`, `<input>` y mensaje de hint/error en un `<div>`. Permite aplicar espacio entre grupos con `space-y-5` en el formulario padre.

---

## M

**Modal**
Componente overlay que aparece encima del contenido de la página bloqueando la interacción con el fondo hasta que se cierra. Requiere `fixed inset-0` para el overlay + z-index alto + contenido centrado. Siempre debe tener un botón de cierre accesible.

---

## O

**Overlay**
Capa semitransparente que cubre el contenido de la página detrás de un modal o drawer. Se implementa con `fixed inset-0 z-50 bg-gray-950/80 backdrop-blur-sm`. Su propósito es enfocar la atención del usuario en el modal.

---

## P

**`peer`**
Clase especial de Tailwind que marca un elemento como "par" (peer). Los elementos hermanos **posteriores** en el DOM pueden usar modificadores `peer-*` para aplicar estilos basados en el estado del peer. Útil para validación CSS sin JavaScript y para toggles con `<input type="checkbox">`.

**`peer-invalid:`**
Modificador de Tailwind que aplica estilos cuando el elemento marcado como `peer` tiene el estado CSS `:invalid`. Se usa junto con `required` en el input para mostrar mensajes de error sin JavaScript.

**`peer-placeholder-shown:`**
Modificador de Tailwind que aplica estilos cuando el placeholder del elemento `peer` está visible (el campo está vacío). Se combina con `peer-invalid:block` y `peer-placeholder-shown:hidden` para ocultar mensajes de error prematuros.

**`placeholder:text-gray-500`**
Sintaxis de Tailwind para estilizar el pseudo-elemento `::placeholder` de un input. Se escribe con el prefijo `placeholder:` seguido de la clase de color/tipografía.

---

## R

**`resize-none`**
Clase de Tailwind que desactiva el handle de redimensionado nativo de los `<textarea>`. Asegura que el textarea mantenga la altura definida por `rows`.
```html
<textarea class="resize-none rows-4 ..."></textarea>
```

**`role="alert"`**
Atributo HTML que indica a los lectores de pantalla que el contenido del elemento es una alerta importante. Es equivalente a `aria-live="assertive"`. Se usa en alertas inline de error o confirmación.

---

## T

**Toast**
Notificación pequeña y temporal que aparece en una esquina de la pantalla (generalmente `bottom-4 right-4`) con posicionamiento `fixed`. Se usa para confirmar acciones recientes (guardado, éxito, error de red). Generalmente se auto-cierra después de unos segundos.

---

## V

**Validación inline**
Técnica de mostrar mensajes de error directamente junto al campo que los generó, en lugar de en una lista al final del formulario. Mejora la UX al dar retroalimentación inmediata y contextual.

---

## Z

**`z-50`**
Clase de Tailwind que aplica `z-index: 50`. Se usa en overlays y modals para asegurar que estén por encima del contenido de la página. La escala completa de Tailwind: `z-0`, `z-10`, `z-20`, `z-30`, `z-40`, `z-50`.
