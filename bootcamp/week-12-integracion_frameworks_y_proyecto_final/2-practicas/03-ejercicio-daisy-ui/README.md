# Ejercicio 03 — daisyUI: Componentes Semánticos

## 🎯 Objetivo

Aprender a usar daisyUI como capa de componentes sobre Tailwind, construyendo un formulario de contacto completo, una tabla de proyectos y un navbar, usando el sistema de temas con `data-theme`.

---

## 🛠️ Qué vas a construir

Una página con cuatro bloques progresivos usando componentes daisyUI:
1. Sistema de temas: cambiar entre `light` y `dark` con `data-theme`
2. Navbar con `navbar-start/center/end` y badges
3. Formulario de contacto completo: `input`, `select`, `textarea`, `checkbox`, `btn`
4. Tabla de proyectos con `table-zebra` y badges de estado

---

## 📁 Estructura

```
03-ejercicio-daisy-ui/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

---

### 🔵 BLOQUE 1 — Sistema de temas con `data-theme`

**Concepto**: daisyUI maneja temas via el atributo `data-theme` en el `<html>`. Cambiar el atributo cambia automáticamente todos los colores de los componentes daisyUI.

```html
<html data-theme="light">   <!-- tema claro -->
<html data-theme="dark">    <!-- tema oscuro -->
<html data-theme="cupcake"> <!-- tema pastel -->

<!-- Toggle JS básico -->
<script>
  function toggleTheme() {
    const html = document.documentElement
    const current = html.getAttribute('data-theme')
    html.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark')
  }
</script>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — Navbar daisyUI

**Concepto**: La clase `navbar` de daisyUI tiene 3 zonas: `navbar-start`, `navbar-center`, `navbar-end`. Funciona responsive out-of-the-box.

```html
<div class="navbar bg-base-100 shadow-sm">
  <div class="navbar-start">
    <a class="btn btn-ghost text-xl font-bold">Mi Portfolio</a>
  </div>
  <div class="navbar-center hidden lg:flex">
    <ul class="menu menu-horizontal px-1 gap-1">
      <li><a class="rounded-lg">Inicio</a></li>
      <li><a class="rounded-lg">Proyectos</a></li>
    </ul>
  </div>
  <div class="navbar-end gap-2">
    <span class="badge badge-primary">Disponible</span>
    <button class="btn btn-primary btn-sm">Contrátame</button>
  </div>
</div>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — Formulario de contacto

**Concepto**: daisyUI provee clases semánticas para formularios: `form-control`, `label`, `input`, `select`, `textarea`, `checkbox`, `toggle`. Son consistentes entre navegadores sin CSS extra.

```html
<!-- Campo de texto con label -->
<label class="form-control w-full">
  <div class="label">
    <span class="label-text font-medium">Nombre</span>
  </div>
  <input type="text" placeholder="Tu nombre completo"
         class="input input-bordered w-full focus:input-primary" />
</label>

<!-- Select -->
<select class="select select-bordered w-full">
  <option disabled selected>¿En qué puedo ayudarte?</option>
  <option>Desarrollo web</option>
  <option>Consultoría</option>
</select>

<!-- Botón de submit -->
<button class="btn btn-primary w-full">Enviar mensaje</button>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3.

---

### 🔵 BLOQUE 4 — Tabla de proyectos

**Concepto**: `table table-zebra` crea tablas con filas alternadas estilizadas automáticamente. `badge` dentro de las celdas permite mostrar estados visualmente.

```html
<div class="overflow-x-auto rounded-xl border border-base-300">
  <table class="table table-zebra">
    <thead>
      <tr>
        <th>Proyecto</th>
        <th>Stack</th>
        <th>Estado</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="font-medium">Portfolio</td>
        <td>Next.js + Tailwind</td>
        <td><span class="badge badge-success badge-sm">Publicado</span></td>
        <td>
          <button class="btn btn-ghost btn-xs">Ver</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Checklist de Verificación

- [ ] BLOQUE 1: Toggle cambia visualmente todos los colores de daisyUI en la página
- [ ] BLOQUE 2: Navbar se ve completo con logo, links y badge de disponibilidad
- [ ] BLOQUE 3: Formulario con 5+ campos, todos con estilos daisyUI correctos
- [ ] BLOQUE 4: Tabla con filas zebra y badges de estado coloreados
