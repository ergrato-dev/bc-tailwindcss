# 🚀 Proyecto Semana 6: Dashboard con Sidebar

## 📋 Descripción

Construir el layout completo de una aplicación de gestión de tareas usando **exclusivamente Flexbox** de TailwindCSS. El objetivo es demostrar dominio de `flex`, `flex-1`, `flex-none`, `justify-between`, `items-center`, `gap`, `flex-col` y `flex-wrap` en un contexto real.

**No se permite usar `position: absolute/fixed` para el layout principal, ni `float`, ni `grid`** (aunque sí se puede usar para overlays o badges).

---

## 🎯 Lo que vas a construir

Un dashboard de gestión de tareas con:
- **Sidebar** de navegación lateral fijo (oculto en mobile)
- **Header** del área de contenido con título y acciones
- **Sección de estadísticas** con cards en fila (`flex-wrap`)
- **Lista de tareas recientes** con layout avatar + texto + badge + acción
- **Responsive**: sidebar se oculta en mobile, layout de stack vertical

---

## 📁 Estructura

```
dashboard-sidebar/
├── README.md        ← este archivo
└── starter/
    └── index.html   ← código inicial con TODOs
```

---

## 📝 Instrucciones

### Requisitos del Sidebar

- [ ] Debe estar **oculto en mobile** (`hidden`) y **visible en desktop** (`md:flex`)
- [ ] Ancho fijo de 256px (`w-64`) usando `flex-none`
- [ ] Contiene: logo arriba, links de navegación (con `flex-col gap-1`), perfil de usuario abajo
- [ ] Ítem de navegación activo con color diferente
- [ ] Cada ítem de nav: icono SVG + texto en `flex items-center gap-3`

### Requisitos del Área Principal (main)

- [ ] Usa `flex-1` para ocupar todo el espacio que el sidebar no toma
- [ ] Tiene `flex flex-col` internamente (header fijo + área de scroll)
- [ ] El **header interno** usa `justify-between` para título ↔ botones

### Requisitos de las Stat Cards

- [ ] Mínimo 4 tarjetas de estadísticas
- [ ] Deben estar en `flex flex-wrap gap-4`
- [ ] Cada tarjeta: icono + número + etiqueta en `flex flex-col`
- [ ] Las tarjetas deben tener un ancho base (`basis-40` o similar) para que hagan wrap

### Requisitos de la Lista de Tareas

- [ ] Al menos 4 ítems de tarea
- [ ] Cada ítem usa el patrón: `flex items-center gap-3`
- [ ] Avatar/ícono: `shrink-0`
- [ ] Texto (título + descripción): `flex-1 min-w-0` con `truncate`
- [ ] Badge de estado: `flex-none`
- [ ] Botón de acción: `flex-none`

### Bonus

- [ ] Indicador de breakpoint activo (como en el ejercicio 01)
- [ ] Un botón de hamburger visible en mobile (`md:hidden`)

---

## 🎨 Paleta sugerida

Usa el **tema dark** del bootcamp:
- Fondo general: `bg-gray-950`
- Sidebar: `bg-gray-900`
- Cards y paneles: `bg-gray-900` con `border border-gray-800`
- Acento principal: `sky-500`
- Texto primario: `text-white`
- Texto secundario: `text-gray-400`

---

## ✅ Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Sidebar con `flex-none w-64`, oculto en mobile | 20 |
| Main con `flex-1`, header con `justify-between` | 20 |
| Stat cards con `flex-wrap gap-*` | 20 |
| Lista con patrón `shrink-0` + `flex-1 min-w-0` | 20 |
| Sin `position: absolute/fixed` en el layout principal | 10 |
| Responsive funcional en mobile | 10 |
| **Total** | **100** |

---

## 📚 Referencias

- [Teoría: Patrones de Layout con Flexbox](../../1-teoria/04-patrones-layout-flex.md)
- [Teoría: Flex Grow, Shrink y Basis](../../1-teoria/03-flex-grow-shrink-basis.md)
- [TailwindCSS Docs: Flexbox](https://tailwindcss.com/docs/flex)
