# Ejercicio 01 — Formulario de Login

## 🎯 Objetivo

Aprender a estilizar un formulario de autenticación completo con TailwindCSS, cubriendo todos los estados de un campo: default, focus, error y disabled.

---

## 📋 ¿Qué vas a construir?

Un formulario de login con:
- Campo de **email** con estados: default, focus, error
- Campo de **password** con toggle de visibilidad (visual, sin JS real)
- Checkbox **"Recordarme"**
- Link **"¿Olvidaste tu contraseña?"**
- Botón de **submit** estilizado
- Diseño centrado en pantalla completa

---

## 🗂️ Estructura

```
01-ejercicio-formulario-login/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados** de forma progresiva:

### BLOQUE 1 — Campos básicos (label + input)

Muestra el campo de email y password sin estados especiales. Solo el layout y estilos de reposo.

**Conceptos a observar:**
- Cómo se vincula `label[for]` con `input[id]`
- Clases base de un input: `block w-full rounded-lg border border-gray-700 bg-gray-800 px-4 py-2.5`
- `placeholder:text-gray-500` para el color del placeholder

**Descomenta** las líneas del BLOQUE 1.

---

### BLOQUE 2 — Estados de focus y placeholder

Agrega el ring de enfoque visible al campo activo.

**Conceptos a observar:**
- `focus:border-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-500/20`
- `focus:outline-none` — quitamos el outline nativo del browser (siempre junto a `focus:ring-*`)
- La transparencia `/20` en el ring da un resplandor suave

**Descomenta** las líneas del BLOQUE 2.

---

### BLOQUE 3 — Estado de error en email

El campo de email muestra estado de error con borde rojo + icono + mensaje.

**Conceptos a observar:**
- `border-red-500 focus:border-red-500 focus:ring-red-500/20` sustituye el `border-gray-700`
- Icono `absolute` dentro de un wrapper `relative` en el input
- `aria-invalid="true"` + `aria-describedby` para accesibilidad
- `<p id="email-error" class="text-xs text-red-400">` vinculado con `aria-describedby`

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Formulario completo

El login card completo con: email (error state) + password + checkbox remember-me + forgot link + submit button.

**Conceptos a observar:**
- `space-y-5` para separación entre grupos de campos
- Checkbox con `cursor-pointer` y `text-sky-500` para el check activo
- Botón submit full-width: `w-full rounded-lg bg-sky-500 ...`
- `href="#"` como placeholder de navegación

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Inputs con `label[for]` + `input[id]` vinculados | 20 |
| Estado focus visible con ring sky | 20 |
| Estado error con borde rojo + mensaje accesible | 30 |
| Checkbox "recordarme" estilizado | 15 |
| Botón submit full-width con hover | 15 |
| **Total** | **100** |
