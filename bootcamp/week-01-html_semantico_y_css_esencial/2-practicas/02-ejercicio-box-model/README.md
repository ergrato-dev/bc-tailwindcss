# Ejercicio 02: El Box Model en Acción

## 🎯 Objetivo

Observar visualmente las cuatro capas del box model (content, padding, border, margin) y entender `box-sizing: border-box` comparado con el comportamiento por defecto.

---

## 🛠️ Configuración

1. Abre `starter/index.html` en VS Code
2. Abre el archivo en tu browser
3. Sigue los pasos — cada uno revela una capa del box model

---

## 📋 Instrucciones

### Paso 1: Content — El tamaño base

El `content` es el área donde vive el texto o la imagen. Su tamaño se define con `width` y `height`:

```css
.caja {
  width: 200px;
  height: 100px;
  background-color: #0ea5e9;
}
```

El elemento ocupa exactamente 200×100px — solo el contenido, sin nada más.

**Descomenta el bloque 1** en el starter. Observa el tamaño de la caja en DevTools.

---

### Paso 2: Padding — Espacio Interior

El `padding` agrega espacio entre el contenido y el borde. Hereda el `background` del elemento:

```css
.caja {
  width: 200px;
  height: 100px;
  background-color: #0ea5e9;
  padding: 24px;   /* ← Agrega 24px de espacio en todos los lados */
}
```

> ⚠️ Con `box-sizing: content-box` (el default), el `padding` SUMA al tamaño total:  
> Tamaño real = 200 + 24 + 24 = **248px** de ancho

**Descomenta el bloque 2** y observa cómo la caja crece.

---

### Paso 3: Border — El Borde

El `border` envuelve el padding. También SUMA al tamaño total (con `content-box`):

```css
.caja {
  width: 200px;
  height: 100px;
  background-color: #0ea5e9;
  padding: 24px;
  border: 4px solid #0369a1;  /* ← Agrega 4px en cada lado */
}
```

> Tamaño real = 200 + 48(padding) + 8(border) = **256px** de ancho

**Descomenta el bloque 3** y observa el borde.

---

### Paso 4: Margin — Espacio Exterior

El `margin` es transparente — no tiene color. Crea espacio entre el elemento y otros elementos:

```css
.caja {
  /* ... propiedades anteriores ... */
  margin: 32px;   /* ← Espacio exterior, no cambia el tamaño de la caja */
}

/* margin: 0 auto — centra horizontalmente */
.caja-centrada {
  width: 300px;
  margin: 0 auto;
}
```

> El `margin` NO suma al tamaño del elemento en DevTools, solo crea espacio alrededor.

**Descomenta el bloque 4** y observa el espacio exterior.

---

### Paso 5: `box-sizing: border-box`

Con `border-box`, el `width` que defines es el tamaño TOTAL (incluye padding y border):

```css
/* Reset global — siempre al inicio de un proyecto */
*, *::before, *::after {
  box-sizing: border-box;
}

.caja-border-box {
  width: 200px;   /* Este ES el tamaño total en pantalla */
  padding: 24px;  /* Incluido dentro del width */
  border: 4px solid #0369a1;  /* Incluido dentro del width */
  /* Content area = 200 - 48(padding) - 8(border) = 144px */
}
```

**Descomenta el bloque 5** y compara las dos cajas lado a lado.

---

### Paso 6: Margin Collapsing

Cuando dos márgenes verticales se tocan, no se suman — el mayor "gana":

```html
<p style="margin-bottom: 24px">Párrafo 1</p>
<p style="margin-top: 24px">Párrafo 2</p>
<!-- El espacio entre ellos es 24px, NO 48px -->
```

**Descomenta el bloque 6** y abre DevTools para confirmar el comportamiento.

---

## ✅ Resultado Esperado

Al finalizar entenderás:

- Por qué `box-sizing: border-box` es más intuitivo y predecible
- La diferencia visual entre padding (color de fondo) y margin (transparente)
- Que el border añade tamaño extra con `content-box`
- Que dos márgenes verticales entre hermanos no se suman (colapsan)

---

## 💡 Experimentos Adicionales

Una vez completados los pasos, prueba en DevTools:
- Modifica el padding directamente en el panel "Computed"
- Añade `outline: 2px dashed red` para visualizar el espacio del margin
- Compara ambas cajas en el panel "Computed" → Diagrama del box model
