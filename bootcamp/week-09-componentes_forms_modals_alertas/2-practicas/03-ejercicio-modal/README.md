# Ejercicio 03 — Modal y Drawer

## 🎯 Objetivo

Construir un modal centrado con overlay blur y un drawer lateral usando la técnica `peer` de Tailwind, sin ninguna línea de JavaScript.

---

## 📋 ¿Qué vas a construir?

- Un **overlay** que cubre toda la pantalla con `fixed inset-0`
- Un **modal centrado** con header, body y footer
- Un **modal con scroll** para contenido largo
- Un **drawer lateral** que se desliza desde la derecha

---

## 🗂️ Estructura

```
03-ejercicio-modal/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados**:

### BLOQUE 1 — Overlay básico

Muestra solo el overlay negro semitransparente que cubre toda la pantalla.

**Conceptos a observar:**
- `fixed inset-0` — el overlay cubre 100vw × 100vh independientemente del scroll
- `z-50` — por encima de todo el contenido de la página
- `bg-gray-950/80` — color + opacidad del overlay

**Descomenta** las líneas del BLOQUE 1.

---

### BLOQUE 2 — Panel centrado

Dentro del overlay aparece el contenido del modal centrado.

**Conceptos a observar:**
- `flex items-center justify-center` en el overlay centra el contenido
- `w-full max-w-md` limita el ancho del modal
- `rounded-2xl bg-gray-900 shadow-2xl` para la card del modal
- `relative z-10` para que el contenido esté encima del label-overlay

**Descomenta** las líneas del BLOQUE 2.

---

### BLOQUE 3 — Modal con backdrop-blur y botón cerrar

Agrega el efecto de desenfoque al overlay y el botón × funcional.

**Conceptos a observar:**
- `backdrop-blur-sm` — difumina el contenido detrás del overlay (requiere bg con opacidad)
- Técnica `peer`: `<input type="checkbox" class="peer hidden">` + `peer-checked:flex`
- `<label for="modal-toggle">` como botón que activa/desactiva el checkbox
- El overlay también tiene un `<label for="modal-toggle">` para cerrar al hacer clic fuera

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Drawer lateral

Panel que se desliza desde la derecha con transición CSS.

**Conceptos a observar:**
- `fixed inset-y-0 right-0` — ocupa todo el alto, pegado al lado derecho
- `translate-x-full` — oculto fuera de pantalla por defecto
- `peer-checked:-translate-x-0 transition-transform duration-300` — animación de entrada
- `w-80` de ancho fijo del drawer
- Overlay por separado del drawer (dos efectos independientes)

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Overlay con `fixed inset-0 z-50` funcional | 20 |
| `backdrop-blur-sm` + `bg-gray-950/80` correctos | 20 |
| Modal abre/cierra con técnica `peer` | 25 |
| Cierre al clic en overlay (label en overlay) | 15 |
| Drawer lateral con transición CSS | 20 |
| **Total** | **100** |
