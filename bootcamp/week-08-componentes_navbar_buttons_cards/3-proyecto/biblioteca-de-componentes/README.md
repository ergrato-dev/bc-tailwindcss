# Proyecto Semana 08 — Biblioteca de Componentes UI

## 🎯 Descripción

Construye una **página de showcase completa** que documente y exhiba todos los componentes UI construidos durante la semana: navbar responsive, sistema de botones, cards en sus variantes y badges/tags semánticos.

Imagina que eres el autor de una librería de componentes y estás creando la página de **documentación visual** para otros desarrolladores.

---

## 📋 Requisitos

### Estructura de la página

La página debe tener **5 secciones bien diferenciadas**:

1. **`<header>`** — Navbar sticky funcional con tu propia marca o nombre
2. **Sección Héroes / Intro** — Título de la librería + descripción breve
3. **Sección Botones** — Showcase de las 5 variantes, 3 tamaños, estados y button groups
4. **Sección Cards** — Grid con mínimo 6 cards (combina 2 o más tipos)
5. **Sección Badges** — Paleta completa de colores + pills removibles + tags

### Especificaciones técnicas

| Requisito | Detalle |
|-----------|---------|
| Navbar | `sticky top-0 z-50`, hamburger mobile con `peer`, links activos |
| Responsive | Funciona en 320px–1440px (mobile-first) |
| Botones | Todos los tipos teorizados, con focus-visible accesible |
| Cards | `group` + `group-hover` en al menos 4 cards |
| Badges | Los 5 colores semánticos presentes + al menos 1 badge numérico |
| Dark theme | `bg-gray-950` base, coherente con el sistema de diseño del bootcamp |
| Accesibilidad | `aria-label` en icon-buttons, `alt` en imágenes, `aria-current` en nav activo |

---

## 📁 Estructura

```
3-proyecto/biblioteca-de-componentes/
├── README.md          ← Este archivo
└── starter/
    └── index.html     ← Tu implementación
```

---

## 🏁 Punto de partida

Abre `starter/index.html`. Encontrarás la estructura HTML esqueleto con secciones, comentarios `<!-- TODO -->` y pistas para implementar cada componente.

Completa cada sección hasta tener la página de biblioteca funcional.

---

## ✅ Criterios de evaluación (100 pts)

| Categoría | Criterio | Puntos |
|-----------|----------|--------|
| **Navbar** | Sticky funcional + hamburger peer + link activo | 15 |
| **Botones** | 5 variantes presentes + tamaños + disabled | 15 |
| **Button group** | Al menos 1 button group implementado | 5 |
| **Product/Blog cards** | group-hover:scale en imagen, line-clamp, truncate | 20 |
| **User o Stat cards** | ring en hover o stat con tendencia | 10 |
| **Badges semánticos** | Los 5 colores semánticos presentes | 10 |
| **Pills removibles** | Al menos 3 pills con botón × y aria-label | 5 |
| **Badge numérico** | Al menos 1 icono con badge absolute | 5 |
| **Responsive** | Grid responsive mobile → desktop | 10 |
| **Accesibilidad** | aria-label, alt, aria-current, focus-visible | 5 |

**Total: 100 puntos — Mínimo aprobatorio: 70 puntos**

---

## 💡 Sugerencias

- Usa imágenes de [Unsplash](https://unsplash.com/) con `?w=400&h=240&fit=crop`
- Mantén el orden de clases: layout → sizing → spacing → typography → colors → effects
- Revisa la teoría de la semana si necesitas recordar alguna clase específica
- Prueba el navbar en mobile reduciendo el ancho del navegador a < 768px

---

## 🔗 Recursos de apoyo

- [TailwindCSS Docs — group](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-parent-state)
- [TailwindCSS Docs — peer](https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-sibling-state)
- [TailwindCSS Docs — line-clamp](https://tailwindcss.com/docs/line-clamp)
