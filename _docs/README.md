# 📚 Documentación General

Esta carpeta contiene documentación que aplica a todo el bootcamp.

## 📋 Contenido

- [Guía de Inicio Rápido](#guía-de-inicio-rápido)
- [Convenciones del Bootcamp](#convenciones-del-bootcamp)
- [Metodología de Aprendizaje](#metodología-de-aprendizaje)
- [Flujo de Trabajo con Git](#flujo-de-trabajo-con-git)

---

## Guía de Inicio Rápido

### 1. Requisitos del Sistema

| Herramienta | Versión Mínima | Instalación |
|-------------|---------------|-------------|
| Node.js     | 22+           | [nodejs.org](https://nodejs.org/) |
| pnpm        | 9+            | `npm install -g pnpm` |
| Git         | 2.40+         | [git-scm.com](https://git-scm.com/) |
| VS Code     | 1.85+         | [code.visualstudio.com](https://code.visualstudio.com/) |

### 2. Extensiones de VS Code Recomendadas

El repositorio incluye configuración de extensiones recomendadas en `.vscode/extensions.json`:

- **Tailwind CSS IntelliSense** — Autocompletado de clases Tailwind
- **PostCSS Language Support** — Soporte para archivos CSS con PostCSS
- **Prettier** — Formateador de código
- **ESLint** — Linter JavaScript
- **Live Server** — Servidor local para HTML estático
- **Auto Rename Tag** — Renombrado automático de etiquetas HTML

### 3. Configurar un Proyecto de Práctica

```bash
# Crear proyecto con Vite (vanilla JS)
pnpm create vite@latest mi-practica -- --template vanilla
cd mi-practica

# Instalar TailwindCSS v4 con plugin de Vite
pnpm add -D tailwindcss @tailwindcss/vite

# Editar vite.config.js para agregar el plugin de Tailwind
# Editar src/style.css para agregar @import "tailwindcss"

# Iniciar servidor de desarrollo
pnpm dev
```

---

## Convenciones del Bootcamp

### Estructura de Carpetas por Semana

```
bootcamp/week-XX-tema_principal/
├── README.md                 # Descripción, objetivos y navegación
├── rubrica-evaluacion.md     # Criterios de evaluación detallados
├── 0-assets/                 # Imágenes SVG y recursos visuales
├── 1-teoria/                 # Archivos .md con contenido teórico
│   ├── 01-tema-a.md
│   ├── 02-tema-b.md
│   └── 03-tema-c.md
├── 2-practicas/              # Ejercicios guiados (código comentado)
│   ├── 01-ejercicio-nombre/
│   │   ├── README.md
│   │   └── starter/
│   │       └── index.html
│   └── 02-ejercicio-nombre/
├── 3-proyecto/               # Proyecto semanal integrador
│   ├── README.md
│   ├── starter/
│   └── solution/             # ⚠️ OCULTA — solo instructores
├── 4-recursos/
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

### Formato de Ejercicios

Los ejercicios usan **código comentado** para descomentar, no TODOs:

```html
<!-- ✅ FORMATO CORRECTO para ejercicios -->
<!-- Descomenta las siguientes líneas: -->
<!-- <div class="flex items-center justify-center h-screen bg-gray-950"> -->
<!--   <h1 class="text-4xl font-bold text-white">Hola Tailwind</h1>       -->
<!-- </div>                                                                -->
```

### Formato de Proyectos

Los proyectos usan **TODOs** para implementar desde cero:

```html
<!-- ✅ FORMATO CORRECTO para proyectos -->
<!-- TODO: Implementar hero section con fondo oscuro y texto centrado -->
<!-- Pistas:
  - Usa min-h-screen para altura completa
  - flex + items-center + justify-center para centrar
  - bg-gray-950 text-white para colores
-->
<section class="???">
  <!-- TODO: Título principal -->
  <!-- TODO: Subtítulo -->
  <!-- TODO: Botones de acción -->
</section>
```

---

## Metodología de Aprendizaje

### Ciclo Semanal (8 horas)

```
Día 1-2 │ 📖 TEORÍA (2-2.5h)
         │ Leer material en 1-teoria/
         │ Ver diagramas y ejemplos
         │
Día 3-5 │ 💻 PRÁCTICAS (3-3.5h)
         │ Ejecutar ejercicios en 2-practicas/
         │ Descomentar código y verificar resultado
         │
Día 6-7 │ 🚀 PROYECTO (2-2.5h)
         │ Implementar proyecto en 3-proyecto/starter/
         │ Completar TODOs y entregar
```

### Tipos de Evidencias

| Evidencia | Peso | Descripción |
|-----------|------|-------------|
| Conocimiento 🧠 | 30% | Cuestionarios, preguntas teóricas |
| Desempeño 💪 | 40% | Ejercicios completados correctamente |
| Producto 📦 | 30% | Proyecto semanal funcional y accesible |

**Criterio de aprobación**: Mínimo **70%** en cada tipo.

---

## Flujo de Trabajo con Git

### Para Estudiantes

```bash
# 1. Clonar el repo
git clone https://github.com/ergrato-dev/bc-tailwindcss.git
cd bc-tailwindcss

# 2. Navegar a la semana actual
cd bootcamp/week-01-html_semantico_y_css_esencial

# 3. Trabajar en los ejercicios y proyecto
# (los cambios están solo en tu copia local)

# 4. (Opcional) Hacer fork para guardar tu progreso
```

### Convención de Commits (Conventional Commits)

```bash
feat: add new exercise for flexbox utilities
fix: correct wrong Tailwind class in week-03 example
docs: update week-05 README with responsive examples
chore: add missing glosario for week-07
```

---

_Última actualización: Marzo 2026_
