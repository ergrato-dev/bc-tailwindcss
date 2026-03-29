# 📋 Semana 9: Componentes UI — Forms, Modals y Alertas

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Estilizar formularios completos: inputs, selects, checkboxes, radios, textareas
- ✅ Usar el plugin `@tailwindcss/forms` para estilos base de inputs
- ✅ Mostrar estados de validación: error, éxito, advertencia en campos de formulario
- ✅ Construir modals y drawers con `fixed`, `inset-0`, capas y `backdrop`
- ✅ Diseñar alertas, toasts y banners de notificación
- ✅ Usar `z-index` (`z-*`) para gestión de capas en overlays
- ✅ Aplicar `backdrop-blur-*` y `bg-opacity` para fondos de overlay

---

## 📚 Requisitos Previos

- **Semanas 1-8 completadas**
- Dominio de componentes navbar, botones y cards

---

## 🗂️ Estructura de la Semana

```
week-09-componentes_forms_modals_alertas/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-formularios.md
│   ├── 02-validacion-estados.md
│   ├── 03-modals-y-drawers.md
│   └── 04-alertas-toasts-banners.md
├── 2-practicas/
│   ├── 01-ejercicio-formulario-login/
│   ├── 02-ejercicio-formulario-complejo/
│   ├── 03-ejercicio-modal/
│   └── 04-ejercicio-notificaciones/
├── 3-proyecto/
│   └── pagina-de-contacto-y-notificaciones/
├── 4-recursos/
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 📝 Contenidos

### 1️⃣ Teoría (2-2.5 horas)

| Tema | Duración | Descripción |
|------|----------|-------------|
| [Formularios](1-teoria/01-formularios.md) | 35 min | Input, select, textarea, checkbox, radio con clases Tailwind |
| [Estados de Validación](1-teoria/02-validacion-estados.md) | 30 min | Error/success/warning con `peer` y clases condicionales |
| [Modals y Drawers](1-teoria/03-modals-y-drawers.md) | 30 min | Overlay con `fixed inset-0`, backdrop blur, z-index |
| [Alertas, Toasts y Banners](1-teoria/04-alertas-toasts-banners.md) | 25 min | Notificaciones con variantes de color semántico |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Formulario de Login | 45 min | Básico | Email + password con estados de error |
| Formulario Complejo | 55 min | Medio | Formulario de registro multi-campo con validación visual |
| Modal Responsive | 55 min | Medio | Modal con overlay, cerrar al hacer click, accesible |
| Set de Notificaciones | 40 min | Básico | Alertas y toasts con 4 variantes de color |

### 3️⃣ Proyecto (2-2.5 horas)

**Página de Contacto y Sistema de Notificaciones**

Construir una página de contacto completa:
- Formulario con todos los tipos de input (texto, email, teléfono, select, textarea)
- Validación visual (estados de error por campo)
- Modal de confirmación al enviar
- Banner de éxito con descarte
- Alertas de error inline

---

## ⏱️ Distribución del Tiempo (8 horas)

```
📖 Teoría:     2-2.5h  (25-31%)
💻 Prácticas:  3-3.5h  (37-44%)
🚀 Proyecto:   2-2.5h  (25-31%)
```

### Cronograma Sugerido

| Día | Actividad | Tiempo |
|-----|-----------|--------|
| **Día 1** | Teoría: Formularios + Validación | 1.25h |
| **Día 2** | Teoría: Modals + Alertas | 1h |
| **Día 3** | Prácticas: Login + Formulario complejo | 1.75h |
| **Día 4** | Prácticas: Modal + Notificaciones | 1.5h |
| **Día 5-6** | Proyecto: Página de contacto | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Página de Contacto](3-proyecto/)**

Página funcional con formulario y notificaciones:

- [ ] Todos los tipos de input correctamente estilizados con Tailwind
- [ ] Estados de error visibles por campo (borde rojo + mensaje)
- [ ] Modal de confirmación con overlay y backdrop
- [ ] Mínimo 3 variantes de alerta (éxito, error, advertencia)
- [ ] Formulario accesible: `label` vinculado a `input`, `aria-describedby` en errores

---

## 🎓 Conceptos Clave

- **`@tailwindcss/forms`**: Plugin que reinicia los estilos de los inputs del browser
- **`focus:ring`**: Indicador visual de foco obligatorio para accesibilidad
- **`peer` + `peer-invalid:`**: Estilizar label/mensaje cuando el input es inválido
- **`fixed inset-0`**: Posición fija que cubre toda la pantalla (base para overlays)
- **`z-50`**: Capa de índice alto para modals (siempre encima del contenido)
- **`backdrop-blur-sm`**: Desenfoque del fondo detrás del modal
- **`overflow-hidden`**: Aplica al `body` para prevenir scroll cuando hay modal abierto
- **`aria-live="polite"`**: Anuncia cambios dinámicos (toasts) a lectores de pantalla

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: @tailwindcss/forms](https://github.com/tailwindlabs/tailwindcss-forms)
- [WCAG: Forms](https://www.w3.org/WAI/tutorials/forms/)
- [Headless UI: Dialog (Modal)](https://headlessui.com/react/dialog)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 10, asegúrate de:

- [ ] Estilizar un input con estados: default, focus, error, disabled
- [ ] Construir un modal con overlay usando `fixed inset-0` y `z-50`
- [ ] Crear alertas con las 4 variantes semánticas (success, error, warning, info)
- [ ] Asegurar que todos los `input` tienen `label` vinculado correctamente
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar la página de contacto funcional y accesible
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 8: Componentes - Navbar, Buttons y Cards](../week-08-componentes_navbar_buttons_cards/README.md)  
➡️ **Siguiente**: [Semana 10: Tailwind Config y Temas Personalizados](../week-10-tailwind_config_y_temas_personalizados/README.md)

---

## 💡 Consejos para Esta Semana

> ♿ **Accesibilidad en formularios no es opcional**: Cada `input` necesita su `label` (no solo placeholder). Cada error necesita `aria-describedby`. Los lectores de pantalla dependen de esto.

> 🪟 **Modals y `overflow-hidden`**: Cuando abres un modal, agrega `overflow-hidden` al `body` con JavaScript para prevenir que el fondo sea scrolleable.

> 🎨 **Los colores de alertas son semánticos**: Verde = éxito, Rojo = error, Amarillo = advertencia, Azul = información. No uses otros colores para estos propósitos.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Los formularios son la puerta de entrada del usuario! 📋</strong><br>
  <em>Un buen formulario puede ser la diferencia entre conversión y rebote</em>
</p>

<p align="center">
  <a href="1-teoria/01-formularios.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
