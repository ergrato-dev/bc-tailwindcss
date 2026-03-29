# 📦 Semana 6: Flexbox Utilities

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Activar Flexbox con `flex` e `inline-flex`
- ✅ Controlar la dirección con `flex-row` y `flex-col`
- ✅ Alinear elementos en el eje principal: `justify-start`, `justify-center`, `justify-between`, `justify-around`, `justify-evenly`
- ✅ Alinear elementos en el eje cruzado: `items-start`, `items-center`, `items-end`, `items-stretch`
- ✅ Usar `gap-*` para espaciado uniforme entre elementos flex
- ✅ Controlar el crecimiento y encogimiento: `flex-1`, `flex-auto`, `flex-none`, `grow`, `shrink`
- ✅ Manejar el desbordamiento con `flex-wrap` y `flex-nowrap`
- ✅ Construir layouts comunes: navbar, sidebar, centrado perfecto

---

## 📚 Requisitos Previos

- **Semanas 1-5 completadas**
- Dominio del sistema de diseño y responsive de Tailwind

---

## 🗂️ Estructura de la Semana

```
week-06-flexbox_utilities/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-conceptos-flexbox.md
│   ├── 02-justify-y-align.md
│   ├── 03-flex-grow-shrink-basis.md
│   └── 04-patrones-layout-flex.md
├── 2-practicas/
│   ├── 01-ejercicio-flex-basico/
│   ├── 02-ejercicio-justify-align/
│   ├── 03-ejercicio-flex-grow/
│   └── 04-ejercicio-layouts-comunes/
├── 3-proyecto/
│   └── dashboard-sidebar/
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
| [Conceptos Flexbox](1-teoria/01-conceptos-flexbox.md) | 30 min | Eje principal, eje cruzado, contenedor vs. ítems |
| [Justify y Align](1-teoria/02-justify-y-align.md) | 35 min | Distribución y alineación de ítems en ambos ejes |
| [Flex Grow, Shrink, Basis](1-teoria/03-flex-grow-shrink-basis.md) | 30 min | Cómo los ítems crecen y se adaptan al espacio |
| [Patrones de Layout](1-teoria/04-patrones-layout-flex.md) | 25 min | Navbar, sidebar, centrado perfecto, holy grail |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Flex Básico | 45 min | Básico | Activar flex y explorar dirección y wrap |
| Justify y Align | 50 min | Básico | Distribución vertical y horizontal de items |
| Flex Grow/Shrink | 45 min | Medio | Crear columnas que se adaptan al espacio disponible |
| Layouts Comunes | 60 min | Medio | Navbar con logo + links + CTA, footer de 3 columnas |

### 3️⃣ Proyecto (2-2.5 horas)

**Dashboard con Sidebar**

Construir el layout de un dashboard de administración:
- Sidebar fijo a la izquierda con links de navegación
- Área de contenido principal que ocupa el espacio restante
- Header con título de página y acciones
- Responsivo: sidebar se colapsa en mobile

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
| **Día 1** | Teoría: Conceptos + Justify/Align | 1.25h |
| **Día 2** | Teoría: Grow/Shrink + Patrones | 1h |
| **Día 3** | Prácticas: Flex básico + Justify/Align | 1.5h |
| **Día 4** | Prácticas: Grow/Shrink + Layouts | 1.75h |
| **Día 5-6** | Proyecto: Dashboard con sidebar | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Dashboard con Sidebar](3-proyecto/)**

Layout de dashboard funcional:

- [ ] Sidebar + main content usando `flex` (sidebar fijo, main con `flex-1`)
- [ ] Header con `justify-between` para título y acciones
- [ ] Navigation links en sidebar con `flex-col gap-*`
- [ ] Responsive: sidebar `hidden md:flex`, menú en mobile alternativo
- [ ] Sin posicionamiento absoluto para el layout principal

---

## 🎓 Conceptos Clave

- **`flex`**: Activa flexbox en el contenedor
- **`flex-row`** / **`flex-col`**: Dirección horizontal o vertical
- **`justify-{value}`**: Distribuye en el eje principal (horizontal en row)
- **`items-{value}`**: Alinea en el eje cruzado (vertical en row)
- **`gap-*`**: Espacio uniforme entre todos los ítems flex
- **`flex-1`**: El ítem crece para ocupar todo el espacio disponible
- **`flex-none`**: El ítem no crece ni se encoge (tamaño fijo)
- **`flex-wrap`**: Los ítems saltan a la siguiente línea si no caben
- **`self-{value}`**: Alineación individual de un ítem en el eje cruzado

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Flexbox](https://tailwindcss.com/docs/flex)
- [CSS-Tricks: A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Flexbox Froggy](https://flexboxfroggy.com/) — Juego para practicar Flexbox

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 7, asegúrate de:

- [ ] Centrar un div perfectamente con `flex items-center justify-center`
- [ ] Crear una navbar con logo izquierda y links derecha usando `justify-between`
- [ ] Usar `flex-1` para que el contenido principal ocupe el espacio restante
- [ ] Completar Flexbox Froggy (al menos hasta nivel 20)
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar el dashboard con sidebar funcional
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 5: Responsive Design y Mobile-First](../week-05-responsive_design_y_mobile_first/README.md)  
➡️ **Siguiente**: [Semana 7: Grid Utilities y Layouts](../week-07-grid_utilities_y_layouts/README.md)

---

## 💡 Consejos para Esta Semana

> 🎯 **`flex-1` es tu mejor amigo**: Cuando quieres que un elemento "ocupe lo que queda", `flex-1` es la respuesta. Es la clave del layout sidebar + main.

> ↔️ **`justify` vs `items`**: `justify` = eje principal (horizontal si `flex-row`). `items` = eje cruzado (vertical si `flex-row`). Confundirlos es el error más común.

> 🐸 **Juega Flexbox Froggy**: El juego en `flexboxfroggy.com` enseña flexbox de forma interactiva. Completa al menos los primeros 20 niveles.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Flexbox es el superpoder del layout! 📦</strong><br>
  <em>Con flex puedes construir el 80% de los layouts que verás en producción</em>
</p>

<p align="center">
  <a href="1-teoria/01-conceptos-flexbox.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
