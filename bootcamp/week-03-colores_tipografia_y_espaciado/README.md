# 🎨 Semana 3: Colores, Tipografía y Espaciado

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Usar la paleta de colores completa de Tailwind (50–950 por color)
- ✅ Aplicar clases de color de texto, fondo y borde
- ✅ Controlar tipografía: `font-size`, `font-weight`, `font-family`, `line-height`, `letter-spacing`
- ✅ Usar la escala de espaciado de Tailwind para `padding` y `margin`
- ✅ Aplicar espaciado unilateral, bilateral y abreviado (e.g., `px-4`, `my-8`)
- ✅ Usar `space-x` y `space-y` para espaciado entre hijos
- ✅ Entender cómo las escalas de Tailwind siguen un sistema de diseño consistente

---

## 📚 Requisitos Previos

- **Semana 1 y 2 completadas**
- Proyecto Vite + Tailwind v4 funcionando
- VS Code con Tailwind IntelliSense

---

## 🗂️ Estructura de la Semana

```
week-03-colores_tipografia_y_espaciado/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-sistema-colores.md
│   ├── 02-tipografia.md
│   ├── 03-escala-espaciado.md
│   └── 04-combinando-colores-tipo-espacio.md
├── 2-practicas/
│   ├── 01-ejercicio-paleta-colores/
│   ├── 02-ejercicio-tipografia/
│   ├── 03-ejercicio-espaciado/
│   └── 04-ejercicio-bloque-texto/
├── 3-proyecto/
│   └── blog-post-card/
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
| [Sistema de Colores](1-teoria/01-sistema-colores.md) | 35 min | Paleta extendida, tonos 50-950, opacidad con `/` |
| [Tipografía](1-teoria/02-tipografia.md) | 35 min | font-size, weight, family, line-height, letter-spacing, text-align |
| [Escala de Espaciado](1-teoria/03-escala-espaciado.md) | 30 min | Padding, margin, gap con la escala 0-96 |
| [Combinando todo](1-teoria/04-combinando-colores-tipo-espacio.md) | 20 min | Cómo aplicar en conjunto para resultados coherentes |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Paleta de Colores | 45 min | Básico | Crear un explorador visual de la paleta Tailwind |
| Tipografía | 50 min | Básico | Escalar jeraquía visual solo con clases de texto |
| Espaciado | 45 min | Básico | Controlar márgenes y paddings con precisión |
| Bloque de Texto | 45 min | Medio | Maquetación editorial con tipografía + espaciado |

### 3️⃣ Proyecto (2-2.5 horas)

**Blog Post Card**

Diseñar una tarjeta de artículo de blog estilo Medium/Dev.to:
- Imagen destacada
- Categoría con color de badge
- Título con tipografía escalada
- Extracto con `line-clamp`
- Metadatos (autor, fecha, tiempo de lectura)
- CTA "Leer más"

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
| **Día 1** | Teoría: Colores + Tipografía | 1.25h |
| **Día 2** | Teoría: Espaciado + Combinando | 1h |
| **Día 3** | Prácticas: Colores + Tipografía | 1.5h |
| **Día 4** | Prácticas: Espaciado + Bloque texto | 1.5h |
| **Día 5-6** | Proyecto: Blog post card | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Blog Post Card](3-proyecto/)**

Tarjeta de artículo con diseño visual sólido:

- [ ] Uso correcto de la paleta de colores (mínimo 3 tonos distintos)
- [ ] Jerarquía tipográfica clara (título > subtítulo > cuerpo > meta)
- [ ] Espaciado consistente en toda la tarjeta
- [ ] `line-clamp` aplicado al extracto
- [ ] Sin CSS personalizado para lo que Tailwind ya resuelve

---

## 🎓 Conceptos Clave

- **Escala de color**: `{color}-{tono}` donde tono va de 50 (más claro) a 950 (más oscuro)
- **Opacidad de color**: `text-blue-500/75` aplica 75% de opacidad al color
- **text-{size}**: Controla `font-size` + `line-height` juntos
- **font-{weight}**: `thin`(100) → `black`(900)
- **tracking-{size}**: Controla `letter-spacing` (wide, wider, widest, tight, etc.)
- **Escala de espaciado**: Basada en múltiplos de 4px (1 unidad = 0.25rem = 4px)
- **`p-4`**: padding de 1rem (16px) en todos los lados
- **`px-4`**: padding horizontal, `py-4`: padding vertical
- **`space-x-4`**: margen izquierdo en hijos excepto el primero

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Customizing Colors](https://tailwindcss.com/docs/customizing-colors)
- [TailwindCSS Docs: Typography](https://tailwindcss.com/docs/font-size)
- [TailwindCSS Docs: Spacing](https://tailwindcss.com/docs/customizing-spacing)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 4, asegúrate de:

- [ ] Poder elegir el tono correcto de un color según el contexto (texto, fondo, borde)
- [ ] Crear jerarquía tipográfica usando solo clases Tailwind
- [ ] Aplicar espaciado consistente sin "adivinar" valores
- [ ] Entender que `4` en Tailwind = 1rem = 16px
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar la blog post card con diseño visual sólido
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 2: Entorno y Filosofía Utility-First](../week-02-entorno_y_filosofia_utility_first/README.md)  
➡️ **Siguiente**: [Semana 4: Borders, Shadows, Sizing y Estados](../week-04-borders_shadows_sizing_y_estados/README.md)

---

## 💡 Consejos para Esta Semana

> 🎨 **El tono -500 es el color "puro"**: Los tonos 100-300 son para fondos sutiles, 400-600 para elementos interactivos, 700-900 para texto sobre fondos claros.

> 📐 **Memoriza la escala de espaciado**: `p-4` = 1rem = 16px. `p-8` = 2rem. `p-2` = 0.5rem. Con esto puedes calcular cualquier valor mentalmente.

> 🔡 **text-base es 1rem**: La escala sigue `xs`, `sm`, `base`, `lg`, `xl`, `2xl`... `9xl`. Base = tamaño de fuente por defecto (16px).

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡El sistema de diseño de Tailwind es tu nueva paleta! 🎨</strong><br>
  <em>Colores, tipo y espaciado consistentes sin tomar decisiones arbitrarias</em>
</p>

<p align="center">
  <a href="1-teoria/01-sistema-colores.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
