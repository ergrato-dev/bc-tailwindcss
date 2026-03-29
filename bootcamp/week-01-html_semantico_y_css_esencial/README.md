# 🌐 Semana 1: HTML Semántico y CSS Esencial

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Estructurar páginas web con HTML5 semántico correcto
- ✅ Entender y aplicar el box model de CSS
- ✅ Comprender la cascada, especificidad y herencia en CSS
- ✅ Usar unidades de medida: px, em, rem, %, vh, vw
- ✅ Aplicar estilos básicos: colores, tipografía, bordes, fondos
- ✅ Escribir HTML accesible con atributos `alt`, `aria-label` y roles
- ✅ Reconocer qué problema resuelve TailwindCSS

---

## 📚 Requisitos Previos

- **Node.js 22+** instalado
- **VS Code** con extensiones recomendadas
- **Git** configurado
- Conocimientos básicos de informática (navegador, archivos, carpetas)

---

## 🗂️ Estructura de la Semana

```
week-01-html_semantico_y_css_esencial/
├── README.md                          # Este archivo
├── rubrica-evaluacion.md              # Criterios de evaluación
├── 0-assets/                          # Diagramas y recursos visuales
├── 1-teoria/
│   ├── 01-html-semantico.md
│   ├── 02-box-model.md
│   ├── 03-cascade-especificidad.md
│   ├── 04-unidades-css.md
│   └── 05-intro-a-tailwind.md
├── 2-practicas/
│   ├── 01-ejercicio-estructura-html/
│   ├── 02-ejercicio-box-model/
│   ├── 03-ejercicio-cascade/
│   └── 04-ejercicio-pagina-personal/
├── 3-proyecto/
│   └── landing-estatica/
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
| [HTML Semántico](1-teoria/01-html-semantico.md) | 30 min | Etiquetas semánticas, accesibilidad, estructura |
| [Box Model](1-teoria/02-box-model.md) | 30 min | margin, padding, border, content, box-sizing |
| [Cascade y Especificidad](1-teoria/03-cascade-especificidad.md) | 25 min | Cómo CSS decide qué regla aplica |
| [Unidades CSS](1-teoria/04-unidades-css.md) | 20 min | px, em, rem, %, vh, vw, fr |
| [Intro a TailwindCSS](1-teoria/05-intro-a-tailwind.md) | 25 min | Filosofía utility-first y por qué existe |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Estructura HTML | 45 min | Básico | Maquetar una página con etiquetas semánticas |
| Box Model | 45 min | Básico | Manipular margin, padding, border con CSS |
| Cascade | 45 min | Básico | Observar cómo la especificidad resuelve conflictos |
| Página Personal | 60 min | Básico | Combinar todo en una página personal estática |

### 3️⃣ Proyecto (2-2.5 horas)

**Landing Page Estática**

Crear una landing page en HTML + CSS puro (sin Tailwind aún) que incluya:
- Header con navegación
- Sección hero con título y descripción
- Sección de características (3 cards)
- Footer con links

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
| **Día 1** | Teoría: HTML semántico + Box model | 1h |
| **Día 2** | Teoría: Cascade + Unidades + Intro Tailwind | 1h |
| **Día 3** | Prácticas: Ejercicios 1-2 | 1.5h |
| **Día 4** | Prácticas: Ejercicios 3-4 | 1.5h |
| **Día 5-6** | Proyecto: Landing estática | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Landing Estática](3-proyecto/)**

Landing page HTML + CSS puro con:

- [ ] HTML semántico correcto (`header`, `nav`, `main`, `section`, `footer`)
- [ ] Imágenes con `alt` descriptivo
- [ ] Box model aplicado correctamente (sin overflow no deseado)
- [ ] Tipografía y colores consistentes
- [ ] Código limpio e indentado

---

## 🎓 Conceptos Clave

- **HTML Semántico**: Usar la etiqueta correcta según el significado del contenido
- **Box Model**: Todo elemento HTML es una caja con content, padding, border y margin
- **Cascade**: El navegador aplica reglas CSS según origen, especificidad y orden
- **Especificidad**: ID > Class > Tag (cómo se "pesan" los selectores)
- **rem**: Unidad relativa al tamaño de fuente del elemento raíz (`html`)
- **Utility-first**: Estilizar con clases pequeñas y reutilizables en lugar de CSS propio

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [MDN: HTML Semántico](https://developer.mozilla.org/es/docs/Glossary/Semantics)
- [MDN: Box Model](https://developer.mozilla.org/es/docs/Web/CSS/CSS_box_model/Introduction_to_the_CSS_box_model)
- [MDN: Cascade](https://developer.mozilla.org/es/docs/Web/CSS/Cascade)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 2, asegúrate de:

- [ ] Conocer al menos 15 etiquetas HTML semánticas y su propósito
- [ ] Entender la diferencia entre margin y padding
- [ ] Saber qué es `box-sizing: border-box` y por qué importa
- [ ] Poder explicar por qué un selector `#id` gana a `.clase`
- [ ] Saber la diferencia entre `em` y `rem`
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar la landing page funcional
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Inicio del Bootcamp](../../README.md)  
➡️ **Siguiente**: [Semana 2: Entorno y Filosofía Utility-First](../week-02-entorno_y_filosofia_utility_first/README.md)

---

## 💡 Consejos para Esta Semana

> 💡 **HTML primero, CSS después**: No intentes estilizar mientras estructuras. Primero escribe HTML semántico correcto, luego agrega estilos.

> 🎯 **box-sizing: border-box siempre**: Aplícalo globalmente con `*, *::before, *::after { box-sizing: border-box; }`. TailwindCSS lo hace automáticamente.

> 🔍 **DevTools es tu amigo**: Abre las herramientas de desarrollo (F12) y explora el panel "Computed" para visualizar el box model de cualquier elemento.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Bienvenido al Bootcamp TailwindCSS! 🎨</strong><br>
  <em>Esta semana construyes los cimientos de todo lo que vendrá</em>
</p>

<p align="center">
  <a href="1-teoria/01-html-semantico.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
