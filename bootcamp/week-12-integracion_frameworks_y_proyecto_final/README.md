# 🚀 Semana 12: Integración con Frameworks y Proyecto Final

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Configurar TailwindCSS en un proyecto React 19+ con Vite
- ✅ Configurar TailwindCSS en un proyecto Next.js 15+
- ✅ Usar clases Tailwind directamente en JSX
- ✅ Manejar clases condicionales con `clsx`/`cn` helper
- ✅ Instalar y usar daisyUI para componentes con variantes prehechas
- ✅ Integrar shadcn/ui en un proyecto Next.js
- ✅ Optimizar Tailwind para producción: purging, bundle size
- ✅ Construir y presentar un proyecto final integrador completo

---

## 📚 Requisitos Previos

- **Semanas 1-11 completadas**
- Dominio completo del ecosistema Tailwind
- Conocimiento básico de React (componentes, props, estado)

---

## 🗂️ Estructura de la Semana

```
week-12-integracion_frameworks_y_proyecto_final/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-tailwind-en-react.md
│   ├── 02-tailwind-en-nextjs.md
│   ├── 03-daisy-ui.md
│   ├── 04-shadcn-ui.md
│   └── 05-optimizacion-produccion.md
├── 2-practicas/
│   ├── 01-ejercicio-react-tailwind/
│   ├── 02-ejercicio-nextjs-tailwind/
│   ├── 03-ejercicio-daisy-ui/
│   └── 04-ejercicio-shadcn/
├── 3-proyecto/
│   └── proyecto-final-portfolio/
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
| [Tailwind en React](1-teoria/01-tailwind-en-react.md) | 25 min | Setup, JSX, clases condicionales con `clsx` |
| [Tailwind en Next.js](1-teoria/02-tailwind-en-nextjs.md) | 25 min | App Router, Server Components, configuración de purging |
| [daisyUI](1-teoria/03-daisy-ui.md) | 25 min | Instalación, sistema de temas, componentes más usados |
| [shadcn/ui](1-teoria/04-shadcn-ui.md) | 30 min | Qué es, instalación, CLI, cómo se diferencia de daisyUI |
| [Optimización en Producción](1-teoria/05-optimizacion-produccion.md) | 15 min | Purging automático, bundle analysis, lazy loading |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| React + Tailwind | 45 min | Medio | Componente React con clases condicionales y props |
| Next.js + Tailwind | 45 min | Medio | Setup completo y primer componente server-side |
| daisyUI | 45 min | Básico | Construir un formulario y tabla con componentes daisyUI |
| shadcn/ui | 60 min | Medio | Instalar shadcn y componer una página con sus componentes |

### 3️⃣ Proyecto Final (2-2.5 horas)

**Portfolio Personal**

Construir un portfolio profesional completo que sirva como proyecto de presentación:
- **Página de inicio**: Hero, skills, proyectos destacados, contacto
- **Sección de proyectos**: Grid de cards con filtro por categoría
- **Dark mode** con persistencia en localStorage
- **Responsive**: Mobile, tablet y desktop perfectos
- **Animaciones**: Transiciones de entrada en secciones
- **Accesibilidad**: Contraste WCAG AA, navegación por teclado
- Stack: Next.js 15+ o React+Vite, Tailwind v4, shadcn/ui o daisyUI

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
| **Día 1** | Teoría: React + Next.js | 1h |
| **Día 2** | Teoría: daisyUI + shadcn + Producción | 1.25h |
| **Día 3** | Prácticas: React + Next.js | 1.5h |
| **Día 4** | Prácticas: daisyUI + shadcn | 1.75h |
| **Día 5-7** | Proyecto Final: Portfolio | 2-2.5h |

---

## 📌 Entregable Final

**Proyecto: [Portfolio Personal](3-proyecto/)**

Portfolio profesional listo para mostrar en entrevistas:

- [ ] Proyecto en React+Vite o Next.js con Tailwind v4
- [ ] Al menos 4 secciones: Hero, About/Skills, Projects, Contact
- [ ] Dark mode funcional con persistencia
- [ ] Completamente responsive en mobile, tablet y desktop
- [ ] Animaciones de entrada en secciones con `motion-safe:`
- [ ] Accesibilidad: contraste AA, foco por teclado, `alt` en imágenes
- [ ] Código limpio, organizado y en inglés
- [ ] Deployado en Vercel, Netlify o similar (bonus)

---

## 🎓 Conceptos Clave

- **`clsx`**: Librería para construir className strings condicionalmente en React
- **`cn()`**: Helper que combina `clsx` + `tailwind-merge` para evitar conflictos de clases
- **`tailwind-merge`**: Resuelve conflictos cuando se sobreescriben clases Tailwind (e.g., `p-4` + `p-8` → `p-8`)
- **daisyUI**: Plugin de componentes sobre Tailwind con sistema de temas via CSS variables
- **shadcn/ui**: Colección de componentes que se copian al proyecto (no dependencia) — usa Radix UI + Tailwind
- **`content` en tailwind.config**: Lista de archivos que Tailwind escanea para purging
- **Purging**: Eliminar clases no usadas en producción → CSS de <10KB típico

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Framework Guides](https://tailwindcss.com/docs/installation/framework-guides)
- [daisyUI Documentation](https://daisyui.com/)
- [shadcn/ui Documentation](https://ui.shadcn.com/)
- [Vercel Deployment](https://vercel.com/docs)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación Final

¡Has completado el Bootcamp TailwindCSS Zero to Hero! Verifica que puedes:

- [ ] Configurar Tailwind desde cero en React o Next.js
- [ ] Usar `clsx`/`cn` para clases condicionales en componentes
- [ ] Elegir entre daisyUI y shadcn/ui según las necesidades del proyecto
- [ ] Analizar el bundle CSS de producción y verificar el purging
- [ ] Completar todos los ejercicios prácticos de la semana
- [ ] Entregar el portfolio final desplegado o listo para deploy
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia
- [ ] Repasar todos los checklists de las 12 semanas ✅

---

## 🏆 Logros del Bootcamp Completado

Al terminar esta semana, habrás construido:

1. **Semana 1-2**: Fundamentos sólidos de HTML/CSS + primer proyecto Tailwind
2. **Semana 3-5**: Sistema de diseño, responsive y mobile-first
3. **Semana 6-7**: Layouts complejos con Flex y Grid
4. **Semana 8-9**: Biblioteca completa de componentes UI
5. **Semana 10-11**: Tema de marca propio + dark mode
6. **Semana 12**: Portfolio desplegado listo para mostrar en entrevistas

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 11: Plugins, Animaciones y Dark Mode](../week-11-plugins_animaciones_y_dark_mode/README.md)  
🏠 **Inicio**: [Bootcamp TailwindCSS Zero to Hero](../../README.md)

---

## 💡 Consejos para el Proyecto Final

> 🎯 **Calidad sobre cantidad**: Un portfolio con 3-4 proyectos bien presentados es mejor que 10 proyectos mediocres. Invierte en los detalles.

> 🌐 **Despliega siempre**: Un portfolio que no está en línea, no existe. Vercel y Netlify son gratuitos y despliegan en minutos.

> 📱 **Mobile first, siempre**: El reclutador puede revisar tu portfolio desde el móvil. Asegúrate de que se vea impecable en 375px.

> 🌙 **Dark mode es un plus**: No todos los portfolios lo tienen. Implementarlo muestra conocimiento técnico y atención al detalle.

> 🤝 **Comparte tu trabajo**: Sube el link a GitHub, LinkedIn y comunidades de desarrolladores. El feedback de la comunidad es invaluable.

---

<p align="center">
  <strong>🎓 ¡Felicitaciones! Has completado el Bootcamp TailwindCSS Zero to Hero</strong><br>
  <em>De cero a Desarrollador Frontend Junior en 12 semanas</em>
</p>

<p align="center">
  <a href="1-teoria/01-tailwind-en-react.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto Final</a>
</p>

<p align="center">
  Hecho con ❤️ para la comunidad de desarrolladores
</p>
