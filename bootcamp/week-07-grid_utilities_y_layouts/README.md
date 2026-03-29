# 🏗️ Semana 7: Grid Utilities y Layouts Complejos

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Activar CSS Grid con `grid` e `inline-grid`
- ✅ Definir columnas con `grid-cols-{n}` y `grid-cols-[template]`
- ✅ Controlar filas con `grid-rows-{n}`
- ✅ Hacer que elementos ocupen múltiples columnas o filas: `col-span-*`, `row-span-*`
- ✅ Usar `gap-*`, `gap-x-*` y `gap-y-*` para separación entre celdas
- ✅ Combinar Grid y Flexbox para layouts complejos reales
- ✅ Construir layouts de tipo masonry, magazine y dashboard

---

## 📚 Requisitos Previos

- **Semanas 1-6 completadas**
- Dominio de Flexbox utilities de Tailwind

---

## 🗂️ Estructura de la Semana

```
week-07-grid_utilities_y_layouts/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-grid-basico.md
│   ├── 02-grid-cols-rows.md
│   ├── 03-col-row-span.md
│   └── 04-grid-vs-flex-cuando-usar.md
├── 2-practicas/
│   ├── 01-ejercicio-grid-basico/
│   ├── 02-ejercicio-galeria/
│   ├── 03-ejercicio-magazine/
│   └── 04-ejercicio-dashboard-grid/
├── 3-proyecto/
│   └── landing-page-completa/
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
| [Grid Básico](1-teoria/01-grid-basico.md) | 30 min | Activar grid, columnas automáticas, colocación |
| [Grid Cols y Rows](1-teoria/02-grid-cols-rows.md) | 35 min | Definir la estructura de la cuadrícula |
| [Col/Row Span](1-teoria/03-col-row-span.md) | 30 min | Extender elementos a múltiples columnas/filas |
| [Grid vs Flex: cuándo usar cada uno](1-teoria/04-grid-vs-flex-cuando-usar.md) | 25 min | Criterios para elegir el sistema correcto |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Grid Básico | 45 min | Básico | Galería de 3 columnas con auto-fill |
| Galería Responsive | 50 min | Medio | Galería que cambia de 1 a 2 a 3 columnas |
| Layout Magazine | 50 min | Medio | Artículo destacado + sidebar con col-span |
| Dashboard Grid | 55 min | Medio | Widgets de stats con diferentes tamaños |

### 3️⃣ Proyecto (2-2.5 horas)

**Landing Page Completa**

Construir una landing page completa de producto que use Grid y Flex en conjunto:
- Hero section (Flex)
- Sección de features en grid de 3 columnas
- Sección de pricing: 3 cards en grid
- Testimonios en grid 2x2
- Footer con grid de links

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
| **Día 1** | Teoría: Grid básico + Cols/Rows | 1.25h |
| **Día 2** | Teoría: Span + Grid vs Flex | 1h |
| **Día 3** | Prácticas: Grid básico + Galería | 1.5h |
| **Día 4** | Prácticas: Magazine + Dashboard | 1.75h |
| **Día 5-6** | Proyecto: Landing page completa | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Landing Page Completa](3-proyecto/)**

Landing page que usa Grid y Flex correctamente:

- [ ] Al menos 3 secciones usando `grid` con columnas definidas
- [ ] Uso de `col-span-*` en al menos una sección
- [ ] Grid responsive: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- [ ] Flex usado donde aplica (navbar, botones, items lineales)
- [ ] Layout coherente y sin elementos desbordados

---

## 🎓 Conceptos Clave

- **`grid`**: Activa CSS Grid en el contenedor
- **`grid-cols-{n}`**: Define `n` columnas de ancho igual
- **`grid-cols-[template]`**: Columnas con template personalizado (ej: `grid-cols-[1fr_2fr]`)
- **`col-span-2`**: El elemento ocupa 2 columnas
- **`col-span-full`**: El elemento ocupa todas las columnas
- **`gap-*`**: Espacio entre filas Y columnas del grid
- **`gap-x-*`** / **`gap-y-*`**: Espacio solo horizontal o solo vertical
- **Grid vs Flex**: Grid para layouts 2D (filas Y columnas), Flex para layouts 1D (una fila o una columna)

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Grid](https://tailwindcss.com/docs/grid-template-columns)
- [CSS-Tricks: A Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Grid Garden](https://cssgridgarden.com/) — Juego para practicar CSS Grid

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 8, asegúrate de:

- [ ] Crear una galería responsive de `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- [ ] Usar `col-span-2` para destacar un elemento en un grid
- [ ] Saber cuándo usar Grid (2D) vs Flex (1D)
- [ ] Completar Grid Garden (niveles 1-14 mínimo)
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar la landing page completa y funcional
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 6: Flexbox Utilities](../week-06-flexbox_utilities/README.md)  
➡️ **Siguiente**: [Semana 8: Componentes - Navbar, Buttons y Cards](../week-08-componentes_navbar_buttons_cards/README.md)

---

## 💡 Consejos para Esta Semana

> 🎯 **Grid para la página, Flex para los componentes**: Grid es ideal para la estructura de página. Flex es ideal para alinear elementos dentro de componentes.

> 📐 **`auto-fill` vs `auto-fit`**: `grid-cols-[repeat(auto-fill,minmax(250px,1fr))]` crea columnas responsivas sin breakpoints. Muy útil para galerías.

> 🌱 **Juega Grid Garden**: Completa los 28 niveles de `cssgridgarden.com`. Es la forma más rápida de dominar mentalmente las propiedades de Grid.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡El layout 2D está en tus manos! 🏗️</strong><br>
  <em>Grid y Flex juntos te permiten construir cualquier layout imaginable</em>
</p>

<p align="center">
  <a href="1-teoria/01-grid-basico.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
