# 🌙 Semana 11: Plugins, Animaciones y Dark Mode

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Instalar y usar los plugins oficiales: `@tailwindcss/typography`, `@tailwindcss/forms`, `@tailwindcss/aspect-ratio`
- ✅ Aplicar el plugin Typography (`prose`) para contenido editorial enriquecido
- ✅ Crear animaciones con `animate-*` y transiciones suaves con `transition-*`
- ✅ Definir animaciones custom en `tailwind.config.js` con `keyframes`
- ✅ Implementar dark mode con la estrategia `class` y con `media`
- ✅ Usar la variante `dark:` para estilos condicionados al modo oscuro
- ✅ Aplicar principios de accesibilidad: contraste, `prefers-reduced-motion`, focus visible

---

## 📚 Requisitos Previos

- **Semanas 1-10 completadas**
- Dominio de configuración de Tailwind

---

## 🗂️ Estructura de la Semana

```
week-11-plugins_animaciones_y_dark_mode/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-plugins-oficiales.md
│   ├── 02-animaciones-transiciones.md
│   ├── 03-dark-mode.md
│   └── 04-accesibilidad-con-tailwind.md
├── 2-practicas/
│   ├── 01-ejercicio-typography-plugin/
│   ├── 02-ejercicio-animaciones/
│   ├── 03-ejercicio-dark-mode/
│   └── 04-ejercicio-accesibilidad/
├── 3-proyecto/
│   └── blog-con-dark-mode/
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
| [Plugins Oficiales](1-teoria/01-plugins-oficiales.md) | 30 min | Typography (prose), Forms, Aspect Ratio — instalación y uso |
| [Animaciones y Transiciones](1-teoria/02-animaciones-transiciones.md) | 35 min | `animate-*`, `@keyframes` custom, `duration-*`, `motion-safe:` |
| [Dark Mode](1-teoria/03-dark-mode.md) | 30 min | Estrategia `class` vs `media`, toggle con JS, CSS variables |
| [Accesibilidad con Tailwind](1-teoria/04-accesibilidad-con-tailwind.md) | 25 min | Contraste WCAG, `sr-only`, `focus-visible:`, `aria-*` |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Typography Plugin | 45 min | Básico | Estilizar contenido markdown con clases `prose` |
| Animaciones | 50 min | Medio | Loading spinners, fade-in, slide-up, bounce custom |
| Dark Mode Toggle | 55 min | Medio | Implementar toggle de dark mode con clase en `html` |
| Accesibilidad | 45 min | Medio | Auditoría y corrección de contraste y foco en componentes |

### 3️⃣ Proyecto (2-2.5 horas)

**Blog con Dark Mode**

Construir una página de artículo de blog completa:
- Header con toggle dark/light mode
- Contenido del artículo con plugin Typography (prose)
- Sidebar con "artículos relacionados"
- Animación de entrada en el hero
- Todos los elementos correctamente contrastados en ambos modos

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
| **Día 1** | Teoría: Plugins + Animaciones | 1.25h |
| **Día 2** | Teoría: Dark mode + Accesibilidad | 1h |
| **Día 3** | Prácticas: Typography + Animaciones | 1.5h |
| **Día 4** | Prácticas: Dark mode + Accesibilidad | 1.75h |
| **Día 5-6** | Proyecto: Blog con dark mode | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Blog con Dark Mode](3-proyecto/)**

Blog article page con modo oscuro funcional:

- [ ] Toggle dark/light mode funcional (clase `dark` en `<html>`)
- [ ] Todos los textos y fondos con variante `dark:` correcta
- [ ] Contenido del artículo con clases `prose dark:prose-invert`
- [ ] Animación de entrada en al menos un elemento
- [ ] Contraste WCAG AA verificado en ambos modos (herramienta: axe, WAVE)

---

## 🎓 Conceptos Clave

- **`prose`**: Clase del plugin Typography que aplica estilos tipográficos a HTML generado (markdown)
- **`prose-invert`**: Versión dark del plugin Typography
- **`animate-spin`**: Animación de rotación (loading)
- **`animate-pulse`**: Animación de fade in/out (skeleton loading)
- **`motion-safe:`**: Aplica la clase solo si el usuario NO tiene `prefers-reduced-motion: reduce`
- **Dark mode `class`**: Tailwind aplica `dark:` cuando el elemento `html` tiene la clase `dark`
- **Dark mode `media`**: Tailwind aplica `dark:` según `@media (prefers-color-scheme: dark)`
- **`sr-only`**: Visualmente oculto pero legible por lectores de pantalla
- **`focus-visible:`**: Estado de foco solo para interacción por teclado (no mouse/touch)

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Dark Mode](https://tailwindcss.com/docs/dark-mode)
- [TailwindCSS Docs: @tailwindcss/typography](https://tailwindcss.com/docs/typography-plugin)
- [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)
- [axe DevTools](https://www.deque.com/axe/) — Auditoría de accesibilidad

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 12, asegúrate de:

- [ ] Usar `prose` para estilizar contenido HTML dinámico o de markdown
- [ ] Construir un toggle de dark mode funcional con JavaScript que agrega/quita clase `dark`
- [ ] Aplicar `dark:bg-gray-900 dark:text-white` correctamente en el layout principal
- [ ] Usar `motion-safe:animate-*` en lugar de `animate-*` para respetar preferencias
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar el blog con dark mode completo y accesible
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 10: Tailwind Config y Temas Personalizados](../week-10-tailwind_config_y_temas_personalizados/README.md)  
➡️ **Siguiente**: [Semana 12: Integración con Frameworks y Proyecto Final](../week-12-integracion_frameworks_y_proyecto_final/README.md)

---

## 💡 Consejos para Esta Semana

> 🌙 **Dark mode: usa siempre la estrategia `class`**: Es más flexible que `media`. Te permite que el usuario elija, guarda la preferencia en `localStorage` y también respeta `prefers-color-scheme` si implementas bien el JS.

> ♿ **`motion-safe` no es opcional**: Muchos usuarios tienen vestibular disorders y activan `prefers-reduced-motion`. Envuelve tus animaciones en `motion-safe:` para respetarlos.

> 📝 **El plugin Typography es imprescindible para blogs y docs**: Si tu proyecto tiene contenido generado por usuarios (markdown, WYSIWYG), `prose` de `@tailwindcss/typography` es la solución.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Polished UI con dark mode y accesibilidad! 🌙</strong><br>
  <em>Interfaces que brillan de día y de noche, y accesibles para todos</em>
</p>

<p align="center">
  <a href="1-teoria/01-plugins-oficiales.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
