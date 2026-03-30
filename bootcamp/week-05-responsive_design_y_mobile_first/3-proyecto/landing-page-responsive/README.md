# Proyecto Semana 5: Landing Page Responsive

## 📋 Descripción

Construye una **landing page completa** que funcione perfectamente en todos los dispositivos: mobile (375px), tablet (768px) y desktop (1280px+). El proyecto integra todos los conceptos de responsive design de la semana.

---

## 🎯 Objetivos

- Implementar mobile-first desde cero
- Navbar responsive con hamburger funcional
- Hero section que cambia de layout en tablet+
- Grid de features 1→2→3 columnas
- Footer multi-columna responsive

---

## 📐 Estructura de la Landing

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR (logo + links desktop | logo + hamburger mobile) │
├─────────────────────────────────────────────────────┤
│  HERO                                               │
│  Mobile: título centrado + botones + imagen abajo   │
│  Desktop: texto izquierda | imagen derecha          │
├─────────────────────────────────────────────────────┤
│  FEATURES  1 col → 2 col → 3 col                   │
│  [⚡ Speed] [🔒 Security] [📊 Analytics]            │
│  [🎯 Focus] [💡 Smart]   [🚀 Scale]                │
├─────────────────────────────────────────────────────┤
│  TESTIMONIAL  centrado en mobile, max-w-2xl         │
├─────────────────────────────────────────────────────┤
│  FOOTER  1 col → 4 col  con nav links               │
└─────────────────────────────────────────────────────┘
```

---

## 📋 Requisitos

### Navbar
- [ ] Logo a la izquierda
- [ ] Links de navegación ocultos en mobile (`hidden md:flex`)
- [ ] Hamburger visible solo en mobile (`block md:hidden`)
- [ ] Menú mobile funcional (checkbox hack o JS)
- [ ] `sticky top-0 z-50` con glassmorphism (`bg-white/80 backdrop-blur`)

### Hero
- [ ] Mobile: layout columna, texto centrado
- [ ] Desktop: `flex-row`, texto izquierda, imagen derecha
- [ ] Tipografía escala: `text-3xl md:text-5xl lg:text-7xl`
- [ ] Botones: columna en mobile, fila en sm+

### Features
- [ ] `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`
- [ ] Al menos 6 cards con icono, título y descripción
- [ ] Gap responsive: `gap-4 md:gap-6`

### Footer
- [ ] `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4`
- [ ] Logo + descripción, 3 columnas de links
- [ ] Línea de copyright al final, centrada

### Verificación Mobile-First
- [ ] Sin scroll horizontal en 375px
- [ ] Legible sin zoom en 320px
- [ ] Verificado en DevTools (modo responsive)
