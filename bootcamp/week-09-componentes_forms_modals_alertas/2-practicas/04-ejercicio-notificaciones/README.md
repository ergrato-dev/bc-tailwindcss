# Ejercicio 04 — Alertas, Toasts y Banners

## 🎯 Objetivo

Implementar el sistema completo de notificaciones con las 4 variantes semánticas (success, error, warning, info) en tres formatos: alerta inline, toast flotante y banner de ancho completo.

---

## 📋 ¿Qué vas a construir?

- 4 **alertas inline** con sus 4 variantes de color semántico
- 1 **banner dismissable** a la parte superior
- 3 **toasts apilados** en posición fija `bottom-4 right-4`
- Una página demo que combina los tres sistemas

---

## 🗂️ Estructura

```
04-ejercicio-notificaciones/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados**:

### BLOQUE 1 — 4 alertas inline con dismiss

Las 4 variantes de alerta: success (emerald), error (red), warning (amber), info (sky).

**Conceptos a observar:**
- Fórmula consistente: `bg-COLOR-500/10 border border-COLOR-500/20`
- `flex items-start gap-3` para iconismo a la izquierda
- `role="alert"` para que los lectores de pantalla anuncien el mensaje
- Botón dismiss con `aria-label="Cerrar alerta"` (icono ×)
- `shrink-0` en el icono para que no se comprima en móvil

**Descomenta** las líneas del BLOQUE 1.

---

### BLOQUE 2 — Banner full-width dismissable

Banner de anuncio que se muestra en la parte superior del contenido.

**Conceptos a observar:**
- `relative` en el banner + `absolute right-3 top-1/2 -translate-y-1/2` para el dismiss
- Sin `fixed` — el banner es parte del flujo normal del documento
- `border-b border-sky-500/20 bg-sky-500/10` para un tono sutil
- Texto centrado con `text-center`; en desktop puede contener más elementos

**Descomenta** las líneas del BLOQUE 2.

---

### BLOQUE 3 — Toasts flotantes

3 toasts apilados en la esquina inferior derecha.

**Conceptos a observar:**
- `fixed bottom-4 right-4 z-50` — flotante encima de todo el contenido
- `flex flex-col gap-3` para apilar múltiples toasts
- `aria-live="polite"` en el contenedor de toasts
- `w-80` ancho fijo del toast
- `shadow-lg shadow-black/20` para profundidad visual
- Fondo `bg-gray-900` (más oscuro que el fondo del cuerpo)

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Sistema completo integrado

Página completa con banner + sección de alertas inline + toasts, todo en una sola vista.

**Conceptos a observar:**
- Jerarquía de z-index: toasts `z-50` > contenido normal
- Los toasts son independientes del scroll de la página
- Combinación de `role="alert"` y `aria-live="polite"` según el contexto
- Espaciado consistente entre alertas con `space-y-4`

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| 4 alertas con colores semánticos correctos (emerald, red, amber, sky) | 30 |
| `role="alert"` en todas las alertas | 10 |
| Banner con botón dismiss `absolute` bien posicionado | 20 |
| Toasts con `fixed bottom-4 right-4 z-50` | 25 |
| `aria-live="polite"` en el contenedor de toasts | 15 |
| **Total** | **100** |
