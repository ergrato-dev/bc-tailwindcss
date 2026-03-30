# 📱 Semana 5: Responsive Design y Mobile-First

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Entender y aplicar la filosofía mobile-first de TailwindCSS
- ✅ Usar todos los breakpoints de Tailwind: `sm`, `md`, `lg`, `xl`, `2xl`
- ✅ Mostrar y ocultar elementos por tamaño de pantalla (`hidden`, `block`, `md:flex`)
- ✅ Aplicar diferente tipografía, espaciado y layout en cada breakpoint
- ✅ Construir layouts que cambian de columna a fila según el viewport
- ✅ Implementar un navbar responsive con hamburger menu
- ✅ Depurar problemas de responsive con DevTools

---

## 📚 Requisitos Previos

- **Semanas 1-4 completadas**
- Dominio de colores, tipografía, spacing, borders, shadows y estados

---

## 🗂️ Estructura de la Semana

```
week-05-responsive_design_y_mobile_first/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/                          ← 5 diagramas SVG
├── 1-teoria/
│   ├── 01-filosofia-mobile-first.md
│   ├── 02-breakpoints-sistema.md
│   ├── 03-layout-responsive.md
│   ├── 04-navegacion-responsive.md
│   └── 05-responsive-avanzado.md
├── 2-practicas/
│   ├── 01-ejercicio-breakpoints/
│   ├── 02-ejercicio-layout-responsive/
│   ├── 03-ejercicio-navbar-responsive/
│   └── 04-ejercicio-imagenes-responsive/
├── 3-proyecto/
│   └── landing-page-responsive/
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
| [Filosofía Mobile-First](1-teoria/01-filosofia-mobile-first.md) | 30 min | Por qué mobile-first, cómo piensa Tailwind, min-width |
| [Sistema de Breakpoints](1-teoria/02-breakpoints-sistema.md) | 30 min | sm(640) md(768) lg(1024) xl(1280) 2xl(1536) · contenedor |
| [Layout Responsive](1-teoria/03-layout-responsive.md) | 35 min | flex-col→flex-row, grid 1→2→3 cols, visibilidad responsive |
| [Navegación Responsive](1-teoria/04-navegacion-responsive.md) | 30 min | Navbar con hamburger, checkbox hack, sticky + glassmorphism |
| [Técnicas Avanzadas](1-teoria/05-responsive-avanzado.md) | 25 min | order, line-clamp, text-align, hover solo en desktop |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| [Breakpoints Visualizador](2-practicas/01-ejercicio-breakpoints/) | 40 min | Básico | Ver qué breakpoint está activo en tiempo real |
| [Layout Responsive](2-practicas/02-ejercicio-layout-responsive/) | 55 min | Medio | Hero, features grid, sidebar, footer responsive |
| [Navbar Responsive](2-practicas/03-ejercicio-navbar-responsive/) | 55 min | Medio | Hamburger + checkbox hack + sticky blur |
| [Imágenes Responsive](2-practicas/04-ejercicio-imagenes-responsive/) | 40 min | Básico | aspect-ratio, object-cover, galería grid |

### 3️⃣ Proyecto (2-2.5 horas)

**[Landing Page Responsive](3-proyecto/landing-page-responsive/)**

Landing page completa con navbar hamburger, hero `flex-col md:flex-row`, features `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`, testimonial y footer multi-columna.

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
| **Día 1** | Teoría 01-02: Mobile-first + Breakpoints | 1h |
| **Día 2** | Teoría 03-05: Layout, Navbar, Avanzado | 1.5h |
| **Día 3** | Prácticas 01-02: Breakpoints + Layout | 1.5h |
| **Día 4** | Prácticas 03-04: Navbar + Imágenes | 1.5h |
| **Día 5-6** | Proyecto: Landing Page Responsive | 2.5h |

---

## 📌 Entregable

**Proyecto: [Landing Page Responsive](3-proyecto/landing-page-responsive/)**

Landing page funcional en mobile (375px), tablet (768px) y desktop (1280px):

- [ ] Navbar sticky con hamburger funcional en mobile
- [ ] Hero con layout columna en mobile y fila en desktop
- [ ] Grid de 6 features: 1 → 2 → 3 columnas
- [ ] Footer: 1 → 4 columnas según viewport
- [ ] Sin scroll horizontal en 375px

---

## 🎓 Conceptos Clave

- **Mobile-First**: Sin prefijo = aplica a todos los tamaños; `md:` = aplica desde 768px **hacia arriba**
- **`sm:`** ≥ 640px · **`md:`** ≥ 768px · **`lg:`** ≥ 1024px · **`xl:`** ≥ 1280px · **`2xl:`** ≥ 1536px
- **`hidden md:flex`**: Oculto en mobile, flex desde tablet (links de navbar)
- **`block md:hidden`**: Visible en mobile, oculto en desktop (botón hamburger)
- **`flex-col md:flex-row`**: Columna apilada en mobile, fila lado a lado en tablet+
- **`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`**: Grid responsivo estándar

---

## 📚 Recursos Adicionales

- [TailwindCSS Docs: Responsive Design](https://tailwindcss.com/docs/responsive-design)
- [TailwindCSS Docs: Container](https://tailwindcss.com/docs/container)
- Ver [4-recursos/webgrafia/](4-recursos/webgrafia/) para más enlaces
- Ver [4-recursos/videografia/](4-recursos/videografia/) para videos recomendados

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 6:

- [ ] Entiendo que sin prefijo = mobile, con prefijo = desde ese tamaño hacia arriba
- [ ] Puedo cambiar columnas, fuentes y padding por breakpoint
- [ ] Sé usar `hidden md:flex` para ocultar/mostrar elementos
- [ ] Construí un navbar responsive con hamburger funcional
- [ ] Probé en DevTools: 375px, 768px, 1024px, 1280px
- [ ] Entregué la landing page responsive
- [ ] Alcancé mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 4: Borders, Shadows, Sizing y Estados](../week-04-borders_shadows_sizing_y_estados/README.md)
➡️ **Siguiente**: [Semana 6: Flexbox Utilities](../week-06-flexbox_utilities/README.md)

---

<p align="center">
  <strong>¡Un diseño para cada pantalla! 📱💻🖥️</strong>
</p>

<p align="center">
  <a href="1-teoria/01-filosofia-mobile-first.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Prácticas</a> •
  <a href="3-proyecto/landing-page-responsive/">🚀 Proyecto</a>
</p>
