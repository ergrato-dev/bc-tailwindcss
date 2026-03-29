# 🧩 Semana 8: Componentes UI — Navbar, Buttons y Cards

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Construir un navbar responsive completo con logo, links y menú hamburger (sin JS)
- ✅ Diseñar un sistema de botones con variantes: primario, secundario, outline, ghost, destructivo
- ✅ Crear cards polivalentes: de producto, de blog, de usuario, de estadística
- ✅ Usar `group` para efectos hover que involucran múltiples elementos
- ✅ Aplicar transiciones suaves con `transition-*` y `duration-*`
- ✅ Construir badges, pills y tags con variantes de color
- ✅ Combinar todos los conocimientos previos en componentes reutilizables

---

## 📚 Requisitos Previos

- **Semanas 1-7 completadas**
- Dominio de Flex, Grid, responsive, estados interactivos y sistema de diseño

---

## 🗂️ Estructura de la Semana

```
week-08-componentes_navbar_buttons_cards/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-navbar-responsive.md
│   ├── 02-sistema-de-botones.md
│   ├── 03-cards-variantes.md
│   └── 04-badges-y-tags.md
├── 2-practicas/
│   ├── 01-ejercicio-navbar/
│   ├── 02-ejercicio-botones/
│   ├── 03-ejercicio-cards/
│   └── 04-ejercicio-badges/
├── 3-proyecto/
│   └── biblioteca-de-componentes/
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
| [Navbar Responsive](1-teoria/01-navbar-responsive.md) | 35 min | Estructura, logo, links, hamburger con CSS `peer` |
| [Sistema de Botones](1-teoria/02-sistema-de-botones.md) | 30 min | Variantes, tamaños, estados, accesibilidad |
| [Cards y Variantes](1-teoria/03-cards-variantes.md) | 30 min | Product card, blog card, user card, stat card |
| [Badges y Tags](1-teoria/04-badges-y-tags.md) | 15 min | Pills, badges, labels con colores semánticos |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Navbar Responsive | 60 min | Medio | Navbar con hamburger toggle (CSS puro, `peer`) |
| Sistema de Botones | 50 min | Medio | 5 variantes × 3 tamaños = 15 botones con todos los estados |
| Cards | 55 min | Medio | 4 tipos de cards con efectos hover usando `group` |
| Badges y Tags | 30 min | Básico | Set de badges de colores para categorías y estados |

### 3️⃣ Proyecto (2-2.5 horas)

**Biblioteca de Componentes**

Crear una página de referencia visual con todos los componentes:
- Header con el navbar completo
- Sección de botones documentados
- Grid de cards de producto (4+ items)
- Set de badges y tags de color

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
| **Día 1** | Teoría: Navbar + Botones | 1.25h |
| **Día 2** | Teoría: Cards + Badges | 0.75h |
| **Día 3** | Prácticas: Navbar + Botones | 1.75h |
| **Día 4** | Prácticas: Cards + Badges | 1.5h |
| **Día 5-6** | Proyecto: Biblioteca de componentes | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Biblioteca de Componentes](3-proyecto/)**

Página de referencia visual con componentes:

- [ ] Navbar funcional con menú hamburger (solo CSS, usando `peer`)
- [ ] Mínimo 4 variantes de botón con estados visibles
- [ ] Mínimo 3 tipos de cards con hover effects
- [ ] Set de badges con colores semánticos (éxito, error, advertencia, info)
- [ ] Transiciones suaves en todos los elementos interactivos

---

## 🎓 Conceptos Clave

- **`transition-all duration-300`**: Transición suave en todas las propiedades en 300ms
- **`group-hover:translate-y-1`**: Mover hijo cuando el padre tiene hover
- **`peer` + `peer-checked:`**: Controlar visibilidad con el estado de un checkbox (hamburger menu)
- **`focus-visible:`**: Estado de foco solo para navegación por teclado (no mouse)
- **`truncate`**: Corta texto con `...` cuando desborda
- **`line-clamp-{n}`**: Limita el texto visible a `n` líneas
- **Variantes de botón**: Primary (filled), Secondary (light bg), Outline (border), Ghost (transparent), Destructive (red)

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Transitions & Animation](https://tailwindcss.com/docs/transition-property)
- [Headless UI](https://headlessui.com/) — Componentes accesibles sin estilos
- [TailwindUI Components](https://tailwindui.com/components) — Referencia de componentes oficiales

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 9, asegúrate de:

- [ ] Construir el menú hamburger con `peer` y CSS puro (sin JavaScript)
- [ ] Tener todos los estados de botón documentados visualmente
- [ ] Usar `group-hover:` en al menos una card
- [ ] Aplicar `transition-*` en todos los elementos interactivos
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar la biblioteca de componentes
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 7: Grid Utilities y Layouts](../week-07-grid_utilities_y_layouts/README.md)  
➡️ **Siguiente**: [Semana 9: Componentes - Forms, Modals y Alertas](../week-09-componentes_forms_modals_alertas/README.md)

---

## 💡 Consejos para Esta Semana

> ✨ **Transiciones son obligatorias**: Cualquier elemento interactivo sin `transition` se siente "brusco". Siempre agrega `transition-colors duration-200` como mínimo.

> 🍔 **El hamburger con `peer` es magia**: `<input type="checkbox" class="peer hidden">` + `<nav class="hidden peer-checked:flex">` = menú funcional sin una línea de JavaScript.

> 📦 **Estudia Tailwind UI**: La galería de componentes en `tailwindui.com` (los free) es la mejor referencia de cómo Tailwind recomienda construir componentes.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Los componentes son los ladrillos de tus UIs! 🧩</strong><br>
  <em>Dominar navbar, botones y cards te prepara para construir cualquier interfaz</em>
</p>

<p align="center">
  <a href="1-teoria/01-navbar-responsive.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
