# Ejercicio 02: Utility-First vs CSS Tradicional

## 🎯 Objetivo

Construir el mismo componente dos veces: una con CSS propio y otra con clases Tailwind. Comparar verbosidad, mantenibilidad y velocidad de desarrollo.

---

## 🛠️ Configuración

Necesitas el proyecto de Vite + Tailwind del ejercicio anterior corriendo con `pnpm dev`.

Copia `starter/index.html` a tu proyecto y ábrelo en el browser.

---

## 📋 Instrucciones

### Paso 1: El diseño objetivo

El componente es una **tarjeta de alerta** con:
- Icono de color (círculo)
- Título en negrita
- Mensaje descriptivo
- Botón de acción

Descomenta el **bloque 1** para ver el diseño objetivo con imagen referencial.

---

### Paso 2: Versión CSS Tradicional

Descomenta el **bloque 2** para ver la versión con CSS propio (`.alert-card`, `.alert-icon`, etc.).

Observa cuántas líneas de CSS requiere.

---

### Paso 3: Versión Tailwind

Descomenta el **bloque 3** para ver la misma tarjeta implementada solo con clases Tailwind.

Observa que **no requiere ningún CSS adicional**.

---

### Paso 4: Comparación

Descomenta el **bloque 4** para ver ambas versiones lado a lado con métricas.

Reflexiona:
- ¿Cuántas líneas de CSS eliminó Tailwind?
- ¿Cuánto tiempo tardaste en entender cada versión?
- ¿Qué es más fácil de modificar?

---

## ✅ Verificación

El ejercicio está completo cuando:
- Ves ambas tarjetas visualmente idénticas en el browser
- Puedes explicar qué clase Tailwind corresponde a cada propiedad CSS
- Modificas el color de una clase en la versión Tailwind sin tocar CSS
