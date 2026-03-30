# Proyecto Final — Portfolio Personal Completo

## 🎯 Objetivo

Construir un portfolio personal profesional y totalmente funcional que integre **todos los conceptos del bootcamp**: HTML semántico, Tailwind v4, componentes reutilizables, diseño responsive, dark mode, animaciones y al menos una de las herramientas del ecosistema (daisyUI o shadcn/ui).

Este proyecto es tu **carta de presentación como desarrollador frontend**. Debe ser algo que puedas mostrar en entrevistas y publicar en tu GitHub.

---

## 🏗️ Descripción del Proyecto

Un portfolio completo con las siguientes secciones:

| Sección | Descripción |
|---------|-------------|
| **Navbar** | Navegación sticky con links ancla, toggle dark mode y menú responsive |
| **Hero** | Presentación con nombre, rol, descripción y CTAs |
| **About / Skills** | Descripción personal y skills con indicadores de nivel |
| **Projects** | Grid de proyectos con filtros por tecnología |
| **Experience** | Timeline de experiencia laboral o académica |
| **Contact** | Formulario funcional + links a redes sociales |
| **Footer** | Copyright y links secundarios |

---

## 🛠️ Stack Recomendado

### Opción A — Next.js (recomendada para producción)

```bash
# Crear proyecto con App Router
pnpm create next-app@latest portfolio --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
cd portfolio

# Opción: añadir shadcn/ui
npx shadcn@latest init
npx shadcn@latest add button card badge input textarea dialog

# Servidor de desarrollo
pnpm dev
```

### Opción B — React + Vite (más simple para comenzar)

```bash
pnpm create vite@latest portfolio -- --template react
cd portfolio
pnpm add -D tailwindcss @tailwindcss/vite
pnpm add clsx tailwind-merge
# Opcional: daisyUI
pnpm add -D daisyui
pnpm dev
```

> Si usas la carpeta `starter/` de este proyecto, trabaja con HTML/Tailwind CDN en local y luego migrá al framework elegido.

---

## 📁 Estructura de Archivos (Next.js)

```
portfolio/
├── app/
│   ├── layout.jsx          # Root layout + anti-flash + fuente
│   ├── page.jsx            # Home — importa todas las secciones
│   └── globals.css         # @import "tailwindcss" + CSS variables
├── components/
│   ├── Navbar.jsx          # Client Component (menú móvil + toggle)
│   ├── Hero.jsx            # Server Component
│   ├── About.jsx           # Server Component (Skills Client)
│   ├── Projects.jsx        # Client Component (filtros)
│   ├── Experience.jsx      # Server Component
│   ├── Contact.jsx         # Client Component (formulario)
│   ├── Footer.jsx          # Server Component
│   └── ui/                 # shadcn/ui components (si aplica)
├── lib/
│   └── utils.js            # helper cn()
├── public/
│   └── assets/             # imágenes, CV.pdf
├── tailwind.config.js
└── next.config.js
```

---

## ✅ Requisitos Funcionales

### Navbar
- [ ] Logo / nombre a la izquierda
- [ ] Links de navegación: anclas a todas las secciones
- [ ] Toggle dark mode (class strategy + localStorage)
- [ ] Menú hamburger en mobile (`md:hidden`)
- [ ] Sticky + efecto de blur/shadow al hacer scroll

### Hero
- [ ] Nombre completo y rol con tipografía grande y llamativa
- [ ] Descripción breve (2-3 líneas)
- [ ] 2 CTAs: "Ver proyectos" (ancla) + "Descargar CV" (PDF)
- [ ] Indicador de disponibilidad (badge animado)
- [ ] Responsive: texto más pequeño en mobile

### About / Skills
- [ ] Párrafo de descripción personal
- [ ] Grid de skills con nombre e icono (o emoji)
- [ ] Indicadores de nivel (barra de progreso o badge)
- [ ] Al menos 8 skills técnicas listadas

### Projects
- [ ] Mínimo 3 proyectos reales o de práctica del bootcamp
- [ ] Cada card incluye: imagen/preview, nombre, descripción, stack (badges), links (demo + GitHub)
- [ ] Filtros por tecnología (React, Next.js, HTML/CSS, etc.) — Client Component
- [ ] Animación `hover` en cards (scale, shadow)

### Experience / Educación
- [ ] Timeline vertical con al menos 2 items
- [ ] Cada item: título, empresa/institución, fecha, descripción
- [ ] Responsive — columna única en mobile

### Contact
- [ ] Formulario con: nombre, email, asunto, mensaje
- [ ] Validación básica (HTML5 `required`)
- [ ] Feedback de envío (modal de suceso o alerta)
- [ ] Links a redes: GitHub, LinkedIn, Twitter/X (iconos SVG o emoji)

---

## ✅ Requisitos Técnicos

### Tailwind y Diseño
- [ ] Dark mode funcionando con `class` strategy
- [ ] Sin flash en recarga (script anti-flash en `<head>`)
- [ ] Totalmente responsive: mobile → tablet → desktop
- [ ] Paleta de colores consistente (usa CSS variables o design tokens)
- [ ] Al menos 1 animación personalizada (keyframes en config)
- [ ] Transiciones en todos los elementos interactivos

### Accesibilidad
- [ ] `alt` descriptivo en todas las imágenes
- [ ] `aria-label` en botones de icono sin texto
- [ ] Navigation con `<nav>` y `role="navigation"`
- [ ] Links con texto descriptivo (no "click aquí")
- [ ] Contraste mínimo WCAG AA (4.5:1 para texto normal)
- [ ] Navegación completa por teclado (`Tab`, `Enter`, `Escape`)
- [ ] `focus-visible:ring-*` en todos los elementos interactivos

### Código
- [ ] Semántica HTML correcta (`<header>`, `<main>`, `<section>`, `<footer>`, `<article>`)
- [ ] Componentes reutilizables (si usas React/Next.js)
- [ ] Helper `cn()` con `clsx` + `tailwind-merge` para clases condicionales
- [ ] Sin clases de Tailwind generadas dinámicamente (problema de purging)
- [ ] Sin `!important` ni estilos inline innecesarios

### Producción
- [ ] Deploy en Vercel (se conecta directo al repositorio de GitHub)
- [ ] Sin errores de consola en producción
- [ ] Lighthouse score ≥ 90 en Performance, Accessibility y Best Practices
- [ ] `loading="lazy"` en imágenes fuera del viewport inicial

---

## ⏱️ Distribución de Tiempo (2.5 horas)

| Tiempo | Tarea |
|--------|-------|
| 30 min | Setup del proyecto (framework, Tailwind, fuentes, dark mode base) |
| 20 min | Navbar + Hero |
| 20 min | About + Skills |
| 30 min | Projects (con filtros) |
| 20 min | Experience + Contact |
| 20 min | Footer + ajustes responsive |
| 10 min | Deploy en Vercel + revisión final |

---

## 🚀 Deploy en Vercel

```bash
# 1. Push a GitHub
git init && git add -A && git commit -m "feat: portfolio personal completo"
git remote add origin https://github.com/tu-usuario/portfolio.git
git push -u origin main

# 2. Vercel CLI (opcional)
pnpm add -g vercel
vercel

# 3. O conecta el repo en vercel.com (recomendado)
# vercel.com/new → Import Git Repository → tu repo
```

---

## 📌 Entregables

1. **URL del sitio en vivo** (Vercel, Netlify, GitHub Pages)
2. **URL del repositorio en GitHub** (público, con README)
3. **Capturas de pantalla**: modo claro y oscuro, mobile y desktop
4. **README del proyecto** con: descripción, stack, instrucciones de instalación, capturas

---

## 🔗 Recursos Útiles

- [TailwindCSS Docs](https://tailwindcss.com/docs)
- [shadcn/ui Components](https://ui.shadcn.com/docs/components)
- [daisyUI Components](https://daisyui.com/components/)
- [Vercel Deploy Guide](https://vercel.com/docs/deployments/overview)
- [Lighthouse (Chrome DevTools)](https://developer.chrome.com/docs/lighthouse/overview)
- [WCAG Contrast Checker](https://webaim.org/resources/contrastchecker/)
