# Ejercicio 03: Cascade y Especificidad

## 🎯 Objetivo

Observar en acción cómo el navegador resuelve conflictos de CSS: especificidad de selectores, orden de aparición y herencia.

---

## 🛠️ Configuración

1. Abre `starter/index.html` en VS Code y en el browser
2. Abre DevTools → pestaña "Styles" para ver qué reglas aplican y cuáles están tachadas
3. Sigue los pasos descomentando los bloques

---

## 📋 Instrucciones

### Paso 1: Selector de Elemento — Especificidad (0,0,1)

El selector de elemento es el más básico:

```css
p {
  color: #6b7280; /* gris */
  font-size: 1rem;
}
```

Todos los `<p>` de la página heredan este estilo.

**Descomenta el bloque 1** en el starter. Los párrafos aparecen en gris.

---

### Paso 2: Clase — Especificidad (0,1,0)

Una clase tiene mayor especificidad que el selector de elemento:

```css
/* (0,0,1) — elemento */
p { color: gray; }

/* (0,1,0) — clase — GANA sobre el elemento */
.texto-destacado { color: #0ea5e9; }
```

Aunque ambas reglas apuntan al mismo elemento, la clase tiene mayor especificidad y su color prevalece.

**Descomenta el bloque 2**. El párrafo con `.texto-destacado` cambia de color.

---

### Paso 3: ID — Especificidad (1,0,0)

Un ID tiene la mayor especificidad de todas las reglas (excepto estilos inline):

```css
/* (0,1,0) — clase */
.texto-destacado { color: #0ea5e9; }

/* (1,0,0) — ID — GANA sobre la clase */
#parrafo-especial { color: #16a34a; }
```

El ID siempre gana. Por eso en CSS moderno se recomienda evitar IDs y usar solo clases.

**Descomenta el bloque 3**. El párrafo con `#parrafo-especial` cambia a verde.

---

### Paso 4: Orden de Aparición — Desempate

Cuando dos reglas tienen la misma especificidad, gana la que aparece **más tarde** en el CSS:

```css
/* Ambas son (0,1,0) */
.color-azul   { color: blue; }
.color-verde  { color: green; }

/* Si un elemento tiene ambas: class="color-azul color-verde"
   el orden en HTML no importa — lo que importa es el orden en CSS
   → verde gana porque está después */
```

**Descomenta el bloque 4** y observa qué color gana — no el que pusiste primero en el `class`, sino el último en el archivo CSS.

---

### Paso 5: Herencia

Las propiedades de tipografía se heredan del padre al hijo automáticamente:

```html
<div style="color: #7c3aed; font-size: 20px;">
  <p>Este párrafo hereda color y font-size del div padre</p>
  <span>Este span también hereda</span>
</div>
```

Pero propiedades como `border`, `padding`, `background` **no se heredan**.

**Descomenta el bloque 5** y observa qué propiedades heredan los hijos.

---

### Paso 6: Por Qué Evitar `!important`

`!important` rompe la cascada normal. Una vez que lo usas, necesitas más `!important` para sobrescribir:

```css
/* Parece la solución rápida... */
.boton { background: blue !important; }

/* Pero luego necesitas otro !important para sobrescribir */
.boton-rojo { background: red !important; } /* ← gana si está después */

/* El código se vuelve imposible de mantener */
```

**Descomenta el bloque 6** para ver esta "guerra de !important" en acción.

---

## ✅ Resultado Esperado

Al usar DevTools → Styles verás:
- Las reglas con menor especificidad aparecen **tachadas** cuando son sobrescritas
- El selector que gana aparece sin tachado, con el valor aplicado
- Puedes ver el cálculo de especificidad en algunos browsers al pasar el cursor sobre el selector

---

## 💡 Herramientas Útiles

- [Specificity Calculator](https://specificity.keegan.st/) — Visualiza la especificidad de cualquier selector
- DevTools → Styles: Muestra las reglas en orden de aplicación, las descartadas aparecen tachadas
