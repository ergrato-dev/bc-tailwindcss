# Proyecto Semana 9 — Página de Contacto y Sistema de Notificaciones

## 🎯 Descripción

Construir una página de contacto completa que integra formulario con validación visual, modal de confirmación y un sistema completo de notificaciones (alertas, toasts y banner).

---

## 📋 Requisitos

### Formulario de contacto

- [ ] Nombre completo (`type="text"`, `required`)
- [ ] Email (`type="email"`, `required`)
- [ ] Teléfono (`type="tel"`, opcional)
- [ ] Asunto (`<select>` con ≥4 opciones, `required`)
- [ ] Mensaje (`<textarea rows="5">`, `required`)
- [ ] Checkbox "Acepto los términos" (`required`)
- [ ] Botón submit


### Validación visual por campo

- [ ] Estado error: `border-red-500` + icono ✗ dentro del input + `<p>` con mensaje de error
- [ ] `aria-invalid="true"` + `aria-describedby` en campos con error
- [ ] Al menos 3 campos en estado de error (simulado en el starter)

### Modal de confirmación

- [ ] Se activa con el botón submit
- [ ] Overlay con `fixed inset-0 bg-gray-950/80 backdrop-blur-sm`
- [ ] Contenido centrado con `flex items-center justify-center`
- [ ] Header con título + botón cerrar con `aria-label`
- [ ] Body con mensaje de confirmación
- [ ] Footer con botones "Volver" y "Confirmar"

### Sistema de notificaciones

- [ ] Banner de éxito al tope de la sección (activado cuando el modal confirma)
- [ ] Al menos 3 alertas inline con variantes semánticas (emerald, red, amber o sky)
- [ ] Al menos 1 toast en `fixed bottom-4 right-4 z-50`
- [ ] Todos con `role="alert"`
- [ ] Botón dismiss con `aria-label` en cada uno

### Accesibilidad

- [ ] Todos los `<input>`, `<select>` y `<textarea>` vinculados con `<label for>`
- [ ] `<form>` con estructura semántica
- [ ] `aria-describedby` en campos con error
- [ ] `aria-label` en todos los icon-buttons
- [ ] `aria-live="polite"` en el contenedor de toasts

---

## 📁 Estructura

```
pagina-de-contacto-y-notificaciones/
├── README.md          ← Esta guía
└── starter/
    └── index.html     ← Tu punto de partida
```

---

## 📊 Tabla de evaluación (100 pts)

| Sección | Criterio | Pts |
|---------|----------|-----|
| **Formulario** | 5 tipos de input presentes + checkbox + labels vinculados | 15 |
| **Formulario** | `<fieldset>` y `<legend>` para el checkbox de términos | 5 |
| **Validación** | 3+ campos con estado error (borde + icono + mensaje) | 15 |
| **Validación** | `aria-invalid` + `aria-describedby` correctos | 10 |
| **Modal** | Overlay `fixed inset-0 bg-gray-950/80 backdrop-blur-sm` | 10 |
| **Modal** | Contenido centrado + header/body/footer + botón cerrar aria-label | 10 |
| **Notificaciones** | 3 alertas inline con variantes semánticas diferentes | 10 |
| **Notificaciones** | Toast `fixed bottom-4 right-4 z-50` con dismiss | 10 |
| **Notificaciones** | Banner con botón dismiss accesible | 5 |
| **A11y** | `role="alert"` + `aria-live="polite"` + `aria-label` en icon-buttons | 10 |
| **Total** | | **100** |

---

## 💡 Pistas

```html
<!-- Estructura de un campo con validación -->
<div class="space-y-1.5">
  <label for="campo" class="block text-sm font-medium text-gray-300">
    Campo <span class="text-red-400">*</span>
  </label>
  <div class="relative">
    <input id="campo" ... aria-invalid="true" aria-describedby="campo-error"
      class="... border-red-500 focus:border-red-500 focus:ring-red-500/20 pr-10"/>
    <!-- Icono de error -->
    <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3">
      <svg class="h-5 w-5 text-red-400" .../>
    </div>
  </div>
  <p id="campo-error" class="flex items-center gap-1.5 text-xs text-red-400">
    Mensaje de error.
  </p>
</div>

<!-- Modal con peer -->
<input type="checkbox" id="modal-confirm" class="peer hidden"/>
<label for="modal-confirm" class="...">Enviar</label>
<div class="fixed inset-0 z-50 hidden items-center justify-center p-4
            bg-gray-950/80 backdrop-blur-sm peer-checked:flex">
  ...
</div>
```

---

## 🔗 Recursos útiles

- [Teoría 01: Formularios](../../1-teoria/01-formularios.md)
- [Teoría 02: Validación y estados](../../1-teoria/02-validacion-estados.md)
- [Teoría 03: Modals y drawers](../../1-teoria/03-modals-y-drawers.md)
- [Teoría 04: Alertas, toasts y banners](../../1-teoria/04-alertas-toasts-banners.md)
