# 🚀 Proyecto Semana 7: Landing Page Completa

## 📋 Descripción

Construir una **landing page completa de producto** que use Grid y Flexbox de forma combinada y coherente. La landing debe tener al menos 5 secciones, ser completamente responsive y demostrar el criterio de cuándo usar Grid vs. Flexbox.

La landing simula la página principal de un producto SaaS: un servicio de gestión de proyectos llamado **FlowGrid**.

---

## 🎯 Objetivos de Aprendizaje

- Usar `grid` para estructurar secciones multi-columna de la página
- Aplicar `col-span-*` y `col-span-full` en al menos una sección
- Usar Flexbox en navbar, botones y componentes lineales
- Combinar Grid y Flex dentro del mismo diseño sin conflictos
- Hacer toda la landing responsive (mobile-first)

---

## 🏗️ Estructura de la Landing

```
┌──────────────────────────────────────────┐
│  NAVBAR (Flex: justify-between)          │
├──────────────────────────────────────────┤
│  HERO (Flex: flex-col items-center)      │
│  título + subtítulo + CTA buttons        │
├──────────────────────────────────────────┤
│  FEATURES  (Grid: 3 columnas)            │
│  ┌────────┬────────┬────────┐            │
│  │ Card 1 │ Card 2 │ Card 3 │            │
│  └────────┴────────┴────────┘            │
├──────────────────────────────────────────┤
│  STATS (Grid: 4 columnas)                │
│  ┌──────┬──────┬──────┬──────┐           │
│  │ 10K+ │ 99%  │  +48 │  4.9 │           │
│  └──────┴──────┴──────┴──────┘           │
├──────────────────────────────────────────┤
│  PRICING (Grid: 3 columnas)              │
│  ┌────────┬────────┬────────┐            │
│  │  Free  │  Pro ⭐│  Ent.  │            │
│  └────────┴────────┴────────┘            │
├──────────────────────────────────────────┤
│  TESTIMONIOS (Grid: 2 columnas)          │
│  ┌────────────┬────────────┐             │
│  │ Testimonio │ Testimonio │             │
│  ├────────────┴────────────┤             │
│  │ CTA (col-span-full)     │             │
│  └─────────────────────────┘             │
├──────────────────────────────────────────┤
│  FOOTER (Grid: 4 columnas)               │
│  Logo │ Product │ Company │ Connect      │
└──────────────────────────────────────────┘
```

---

## ✅ Requisitos

### Grid (obligatorio)
- [ ] Sección **Features**: `grid-cols-1 md:grid-cols-3` con 3 cards de features
- [ ] Sección **Stats**: `grid-cols-2 md:grid-cols-4` con 4 métricas
- [ ] Sección **Pricing**: `grid-cols-1 md:grid-cols-3` con 3 planes
- [ ] Sección **Testimonios**: `grid-cols-1 md:grid-cols-2` + `col-span-full` en el CTA
- [ ] Sección **Footer**: `grid-cols-2 md:grid-cols-4` con columnas de links

### Flexbox (obligatorio)
- [ ] **Navbar**: `flex justify-between items-center` con logo, links y CTA
- [ ] **Hero**: `flex flex-col items-center` con título, subtítulo y botones
- [ ] **Botones**: `flex items-center gap-2` para iconos + texto
- [ ] **Pricing cards**: internamente `flex flex-col` para empujar el botón al fondo

### Responsive
- [ ] Mobile-first: en 320px toda la landing es una columna, sin overflow
- [ ] En tablet (768px) se activan 2 columnas en Testimonios y Stats
- [ ] En desktop (1024px+) se muestran 3 y 4 columnas según la sección

### Calidad de código
- [ ] HTML semántico: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- [ ] Clases en orden consistente
- [ ] Sin `position: absolute` para el layout

---

## 🎨 Paleta de Colores

| Uso | Clase Tailwind |
|-----|---------------|
| Fondo principal | `bg-gray-950` |
| Secciones alternas | `bg-gray-900` |
| Cards | `bg-gray-800` |
| Bordes | `border-gray-700` / `border-gray-800` |
| Acento principal | `bg-sky-500` / `text-sky-400` |
| Plan Pro (destacado) | `bg-sky-600` |
| Texto primario | `text-white` |
| Texto secundario | `text-gray-400` |

---

## 📊 Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Grid en Features (3 cols responsive) | 15 pts |
| Grid en Pricing (3 cols, plan Pro destacado con ring) | 15 pts |
| Grid en Footer (4 cols responsive) | 10 pts |
| col-span-full en CTA de Testimonios | 10 pts |
| Navbar con Flex justify-between | 10 pts |
| Hero con Flex centrado | 10 pts |
| Pricing cards con flex-col + botón al fondo | 10 pts |
| Responsive completo (mobile → desktop) | 15 pts |
| HTML semántico | 5 pts |
| **Total** | **100 pts** |

**Mínimo aprobatorio: 70/100**

---

## 💡 Pistas

1. **Pricing cards con altura uniforme**: usa `grid` en el contenedor para que las 3 cards tengan la misma altura. Dentro de cada card, usa `flex flex-col` con `flex-1` en el área de features para empujar el botón al fondo.

2. **Plan Pro destacado**: agrega `ring-2 ring-sky-500` y `bg-sky-600` para diferenciar el plan con un anillo brillante.

3. **Stats**: dentro de cada stat, usa `flex flex-col items-center` para centrar el número y el label.

4. **Footer**: en mobile las 4 columnas del footer se convierten en `grid-cols-2` (2 pares de grupos).
