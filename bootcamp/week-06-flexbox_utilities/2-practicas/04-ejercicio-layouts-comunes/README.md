# Ejercicio 04: Layouts Comunes con Flexbox

## 🎯 Objetivo

Construir los tres patrones de layout más importantes del desarrollo web moderno usando exclusivamente Flexbox: navbar con logo + links + CTA, centrado perfecto, y footer multi-columna.

---

## 📋 Instrucciones

### Paso 1: Navbar con `justify-between`

Descomenta el **bloque 1** para construir una navbar completa: logo a la izquierda, links de navegación al centro y botones CTA a la derecha. Todo usando `justify-between` y `items-center`. Sin `float`, sin `position: absolute`.

### Paso 2: Hero section centrada

Descomenta el **bloque 2** para construir una hero section con el contenido centrado vertical y horizontalmente usando `flex flex-col items-center justify-center`. Incluye título, subtítulo y botones.

### Paso 3: Tarjeta de producto horizontal

Descomenta el **bloque 3** para construir una tarjeta con imagen a la izquierda y contenido a la derecha usando `flex` e `items-start`. El contenido interno usa `flex flex-col` para apilar título, descripción y precio.

### Paso 4: Footer multi-columna

Descomenta el **bloque 4** para construir un footer con marca + descripción a la izquierda y tres columnas de links a la derecha. Usa `flex-col md:flex-row` para que sea responsive.

---

## ✅ Verificación

- El bloque 1 muestra logo completamente a la izquierda y CTA completamente a la derecha
- El bloque 2 muestra el hero perfectamente centrado en su contenedor
- El bloque 3 muestra imagen y contenido en fila horizontal sin romper el layout
- El bloque 4 muestra las columnas del footer alineadas en desktop, apiladas en mobile
