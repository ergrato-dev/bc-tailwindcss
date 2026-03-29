# 📱 Semana 5: Responsive Design y Mobile-First

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Entender y aplicar la filosofía mobile-first de TailwindCSS
- ✅ Usar todos los breakpoints de Tailwind: `sm`, `md`, `lg`, `xl`, `2xl`
- ✅ Mostrar y ocultar elementos por tamaño de pantalla (`hidden`, `block`, `sm:flex`)
- ✅ Aplicar diferente tipografía, espaciado y layout en cada breakpoint
- ✅ Usar el contenedor (`container`) con `mx-auto` y breakpoints
- ✅ Construir interfaces que funcionen en mobile, tablet y desktop
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
├── 0-assets/
├── 1-teoria/
│   ├── 01-filosofia-mobile-first.md
│   ├── 02-breakpoints-tailwind.md
│   ├── 03-container-y-max-width.md
│   └── 04-mostrar-ocultar-responsive.md
├── 2-practicas/
│   ├── 01-ejercicio-mobile-first/
│   ├── 02-ejercicio-breakpoints/
│   ├── 03-ejercicio-container/
│   └── 04-ejercicio-navbar-responsive/
├── 3-proyecto/
│   └── hero-section-responsive/
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
| [Filosofía Mobile-First](1-teoria/01-filosofia-mobile-first.md) | 30 min | Por qué mobile-first, cómo piensa Tailwind |
| [Breakpoints de Tailwind](1-teoria/02-breakpoints-tailwind.md) | 35 min | sm(640px), md(768px), lg(1024px), xl(1280px), 2xl(1536px) |
| [Container y Max-Width](1-teoria/03-container-y-max-width.md) | 25 min | Contenedores centrados, `max-w-7xl mx-auto`, paddings responsivos |
| [Mostrar/Ocultar Responsive](1-teoria/04-mostrar-ocultar-responsive.md) | 20 min | `hidden md:block`, `block md:hidden`, estrategias de visibilidad |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Mobile-First | 45 min | Básico | Partir de mobile y escalar hacia desktop |
| Breakpoints | 50 min | Medio | Cambiar layout completo entre breakpoints |
| Container | 40 min | Básico | Páginas centradas con márgenes correctos |
| Navbar Responsive | 60 min | Medio | Navbar con links para desktop, hamburger para mobile |

### 3️⃣ Proyecto (2-2.5 horas)

**Hero Section Responsive**

Diseñar una sección hero que se adapte a 3 tamaños:
- **Mobile**: texto centrado, imagen debajo del texto, CTA a ancho completo
- **Tablet (md)**: imagen y texto en columnas, CTA más compacto
- **Desktop (lg+)**: layout dividido 60/40, tipografía más grande, padding generoso

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
| **Día 1** | Teoría: Mobile-first + Breakpoints | 1.25h |
| **Día 2** | Teoría: Container + Mostrar/Ocultar | 0.75h |
| **Día 3** | Prácticas: Mobile-first + Breakpoints | 1.5h |
| **Día 4** | Prácticas: Container + Navbar | 1.75h |
| **Día 5-6** | Proyecto: Hero section responsive | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Hero Section Responsive](3-proyecto/)**

Hero section que funciona en 3 breakpoints:

- [ ] Diseño mobile correcto sin clases de breakpoint (base styles)
- [ ] Cambios visuales verificables en `md:` y `lg:`
- [ ] Uso de `container` + `mx-auto` + `px-4` para márgenes consistentes
- [ ] Al menos un elemento con visibilidad condicional (`hidden md:block`)
- [ ] Probado con DevTools en al menos 3 tamaños de pantalla

---

## 🎓 Conceptos Clave

- **Mobile-First**: Sin prefijo = aplica a todos los tamaños; `md:` = aplica desde 768px hacia arriba
- **Breakpoints**: Puntos de quiebre donde el diseño cambia de layout
- **`sm:`**: ≥ 640px | **`md:`**: ≥ 768px | **`lg:`**: ≥ 1024px | **`xl:`**: ≥ 1280px | **`2xl:`**: ≥ 1536px
- **`container`**: Clase que aplica `max-width` según el breakpoint actual
- **`hidden md:block`**: Oculto en mobile, visible como bloque desde tablet
- **`block md:hidden`**: Visible en mobile, oculto desde tablet (e.g., el botón hamburger)

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Responsive Design](https://tailwindcss.com/docs/responsive-design)
- [TailwindCSS Docs: Container](https://tailwindcss.com/docs/container)
- [MDN: Responsive Design](https://developer.mozilla.org/es/docs/Learn/CSS/CSS_layout/Responsive_Design)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 6, asegúrate de:

- [ ] Entender que sin prefijo = mobile, con prefijo = desde ese tamaño hacia arriba
- [ ] Poder cambiar columnas, tamaños de fuente y padding por breakpoint
- [ ] Saber usar `hidden md:flex` para navegación responsive
- [ ] Probar diseños en DevTools con modo responsive
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar el hero section responsive verificado en 3 breakpoints
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 4: Borders, Shadows, Sizing y Estados](../week-04-borders_shadows_sizing_y_estados/README.md)  
➡️ **Siguiente**: [Semana 6: Flexbox Utilities](../week-06-flexbox_utilities/README.md)

---

## 💡 Consejos para Esta Semana

> 📱 **Empieza siempre por mobile**: Abre DevTools, cambia a vista móvil (375px) y diseña desde ahí. Añade breakpoints cuando el diseño lo necesite, no antes.

> 🔍 **DevTools responsive mode**: En Chrome, F12 → ícono de dispositivo. Puedes simular cualquier tamaño de pantalla y ver los breakpoints activos.

> ⚠️ **No abuses de los breakpoints**: Muchos proyectos solo necesitan 2-3 breakpoints. No añadas `sm:` `md:` `lg:` `xl:` a todo si no es necesario.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Un diseño para cada pantalla! 📱💻🖥️</strong><br>
  <em>Desde esta semana, tus interfaces funcionan en todos los dispositivos</em>
</p>

<p align="center">
  <a href="1-teoria/01-filosofia-mobile-first.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
