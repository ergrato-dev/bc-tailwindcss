# Ejercicio 02 — Formulario Complejo (Registro)

## 🎯 Objetivo

Construir un formulario de registro multi-campo que integra todos los tipos de input de HTML con Tailwind, a cuadrícula de 2 columnas en desktop.

---

## 📋 ¿Qué vas a construir?

Un formulario de registro con:
- Grid de 2 columnas para nombre y apellido
- Campo email + select de país
- Textarea de bio (full-width)
- Grupo de **checkboxes** (preferencias)
- Grupo de **radios** (plan)
- Botones cancel/submit

---

## 🗂️ Estructura

```
02-ejercicio-formulario-complejo/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados**:

### BLOQUE 1 — Grid de campos de texto

Nombre y apellido en grid de 2 columnas. Email full-width.

**Conceptos a observar:**
- `grid grid-cols-1 gap-x-6 gap-y-5 sm:grid-cols-2` para el grid responsive
- `sm:col-span-2` hace que email ocupe las 2 columnas en desktop
- Mismo estilo base en todos los inputs (consistencia)

**Descomenta** las líneas del BLOQUE 1.

---

### BLOQUE 2 — Select, textarea y file input

Select de país con flecha personalizada, textarea de bio y campo de foto de perfil.

**Conceptos a observar:**
- `appearance-none` en `<select>` elimina el estilo nativo del browser
- `relative` + SVG `absolute` para reemplazar la flecha del select
- `resize-none rows-4` en textarea
- File input: `file:cursor-pointer file:rounded-lg file:border-0 file:bg-sky-500/15 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-sky-400`

**Descomenta** las líneas del BLOQUE 2.

---

### BLOQUE 3 — Checkboxes y radios

Grupo de checkboxes de notificaciones y grupo de radios de plan con `fieldset` + `legend`.

**Conceptos a observar:**
- `fieldset` agrupa campos relacionados; `legend` es su título
- `h-4 w-4 rounded border-gray-600 bg-gray-800 text-sky-500` para checkbox
- `cursor-pointer` en el label para hacer toda la fila clickeable
- `focus:ring-offset-gray-900` ajusta el ring al fondo oscuro

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Formulario completo

Todo el formulario integrado en una card con header, secciones separadas con `<hr>` y footer de acciones.

**Conceptos a observar:**
- `<h2>` para el título del formulario dentro de la card
- Divider `<div class="border-t border-gray-800">` entre secciones
- Footer con `flex items-center justify-end gap-3` para alignment de botones
- Botón cancel en `text-gray-400 hover:text-white` (sin background)

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Grid 2 columnas responsive en nombre/apellido | 20 |
| Select con `appearance-none` y flecha SVG | 20 |
| Grupo de checkboxes con `fieldset` + `legend` | 20 |
| Grupo de radios con `fieldset` + `legend` | 20 |
| Footer con botones cancel/submit alineados | 20 |
| **Total** | **100** |
