# ⚙️ Semana 2: Entorno de Desarrollo y Filosofía Utility-First

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Configurar un proyecto TailwindCSS v4 con Vite y pnpm
- ✅ Entender la filosofía utility-first vs. CSS tradicional
- ✅ Aplicar las primeras clases de utilidad de Tailwind
- ✅ Usar el IntelliSense de Tailwind en VS Code
- ✅ Entender cómo Tailwind genera y purga CSS en producción
- ✅ Conocer la estructura de archivos de un proyecto Tailwind+Vite
- ✅ Usar Tailwind Play para experimentar sin instalar nada

---

## 📚 Requisitos Previos

- **Semana 1 completada**: HTML semántico y CSS esencial
- **Node.js 22+** y **pnpm** instalados
- **VS Code** con extensión Tailwind CSS IntelliSense

---

## 🗂️ Estructura de la Semana

```
week-02-entorno_y_filosofia_utility_first/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-filosofia-utility-first.md
│   ├── 02-instalacion-vite-tailwind.md
│   ├── 03-estructura-proyecto.md
│   ├── 04-primeras-clases-utilidad.md
│   └── 05-tailwind-play.md
├── 2-practicas/
│   ├── 01-ejercicio-setup/
│   ├── 02-ejercicio-utility-vs-css/
│   ├── 03-ejercicio-primeras-clases/
│   └── 04-ejercicio-componente-basico/
├── 3-proyecto/
│   └── tarjeta-de-perfil/
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
| [Filosofía Utility-First](1-teoria/01-filosofia-utility-first.md) | 30 min | Por qué utility-first, ventajas vs. BEM/CSS modules |
| [Instalación Vite + Tailwind](1-teoria/02-instalacion-vite-tailwind.md) | 35 min | Setup paso a paso con pnpm |
| [Estructura del Proyecto](1-teoria/03-estructura-proyecto.md) | 20 min | Archivos de configuración y cómo encajan |
| [Primeras Clases de Utilidad](1-teoria/04-primeras-clases-utilidad.md) | 30 min | Colores, texto, fondo, padding, margin básicos |
| [Tailwind Play](1-teoria/05-tailwind-play.md) | 15 min | Sandbox online para experimentar sin instalar |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Setup del Entorno | 45 min | Básico | Crear y levantar proyecto Vite + Tailwind |
| Utility vs CSS | 45 min | Básico | Comparar el mismo diseño con CSS propio vs Tailwind |
| Primeras Clases | 45 min | Básico | Aplicar texto, colores, padding, margin, rounded |
| Componente Básico | 60 min | Básico | Construir un badge/pill con clases Tailwind |

### 3️⃣ Proyecto (2-2.5 horas)

**Tarjeta de Perfil**

Construir una tarjeta de perfil estilo GitHub/LinkedIn usando exclusivamente clases Tailwind:
- Avatar con imagen circular
- Nombre y rol
- Bio corta
- Estadísticas (repos, followers, following)
- Botón de acción

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
| **Día 1** | Teoría: Filosofía utility-first + instalación | 1h |
| **Día 2** | Teoría: Estructura + primeras clases + Play | 1h |
| **Día 3** | Práctica: Setup + Utility vs CSS | 1.5h |
| **Día 4** | Práctica: Primeras clases + Componente | 1.5h |
| **Día 5-6** | Proyecto: Tarjeta de perfil | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Tarjeta de Perfil](3-proyecto/)**

Tarjeta de perfil funcional con Tailwind v4 + Vite:

- [ ] Proyecto inicializado con Vite + pnpm + Tailwind v4
- [ ] `@import "tailwindcss"` en el CSS de entrada (no la API legacy)
- [ ] Diseño responsive: se ve bien en mobile y desktop
- [ ] Clases Tailwind en orden correcto (layout → color → effects)
- [ ] HTML semántico con `alt` en imágenes
- [ ] Sin CSS personalizado innecesario

---

## 🎓 Conceptos Clave

- **Utility-first**: Paradigma donde se componen estilos usando clases de propósito único
- **JIT (Just-in-Time)**: Tailwind genera solo las clases que usas en tu código
- **Purging**: Eliminación automática de clases no usadas en producción
- **`@import "tailwindcss"`**: La forma moderna (v4) de incluir Tailwind (reemplaza las tres directivas `@tailwind`)
- **IntelliSense**: Autocompletado y vista previa de clases en VS Code
- **Tailwind Play**: Sandbox online en `play.tailwindcss.com`

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Installation](https://tailwindcss.com/docs/installation)
- [TailwindCSS Docs: Utility-First Fundamentals](https://tailwindcss.com/docs/utility-first)
- [Tailwind Play](https://play.tailwindcss.com/)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 3, asegúrate de:

- [ ] Poder crear un proyecto Vite + Tailwind desde cero en menos de 5 minutos
- [ ] Entender por qué `utility-first` reduce la fatiga de nombrado de clases
- [ ] Saber usar al menos 20 clases de utilidad básicas
- [ ] Tener IntelliSense de Tailwind funcionando en VS Code
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar la tarjeta de perfil funcional
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 1: HTML Semántico y CSS Esencial](../week-01-html_semantico_y_css_esencial/README.md)  
➡️ **Siguiente**: [Semana 3: Colores, Tipografía y Espaciado](../week-03-colores_tipografia_y_espaciado/README.md)

---

## 💡 Consejos para Esta Semana

> ⚙️ **No uses CDN para aprender**: Configura el entorno real con Vite. El CDN no tiene IntelliSense ni purging, malos hábitos desde el inicio.

> 🎨 **Explora Tailwind Play**: Es perfecto para probar ideas rápido sin configurar nada. Úsalo para experimentar antes de escribir código en tu proyecto.

> 📚 **Lee el output de Vite**: Cuando ejecutas `pnpm dev`, el terminal te dice exactamente qué está pasando. No lo ignores.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Tailwind instalado, a construir interfaces! 🚀</strong><br>
  <em>Desde esta semana, nunca más escribirás CSS aburrido</em>
</p>

<p align="center">
  <a href="1-teoria/01-filosofia-utility-first.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
