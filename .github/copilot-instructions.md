# 🤖 Instrucciones para GitHub Copilot

## 📋 Contexto del Bootcamp

Este es un **Bootcamp de TailwindCSS Zero to Hero** estructurado para llevar a estudiantes de cero a héroe en diseño UI moderno con TailwindCSS y su ecosistema.

### 📊 Datos del Bootcamp

- **Duración**: 12 semanas (~3 meses)
- **Dedicación semanal**: 8 horas
- **Total de horas**: ~96 horas
- **Nivel de salida**: Desarrollador Frontend Junior (UI/TailwindCSS)
- **Enfoque**: TailwindCSS moderno con Tailwind v4+, integración con React/Next.js
- **Stack**: TailwindCSS 4+, Node.js 22+, PostCSS, Vite, React 19+, Next.js 15+

---

## 🎯 Objetivos de Aprendizaje

Al finalizar el bootcamp, los estudiantes serán capaces de:

- ✅ Dominar los fundamentos de HTML semántico y CSS necesarios para usar Tailwind
- ✅ Usar la filosofía utility-first para construir interfaces modernas
- ✅ Aplicar el sistema de diseño de Tailwind (colores, tipografía, espaciado)
- ✅ Construir layouts complejos con Flexbox y Grid utilities de Tailwind
- ✅ Implementar diseño responsive con el enfoque mobile-first
- ✅ Diseñar componentes UI reutilizables (navbar, cards, forms, modals)
- ✅ Personalizar Tailwind con `tailwind.config.js` y temas custom
- ✅ Usar plugins oficiales (Typography, Forms, Aspect Ratio, etc.)
- ✅ Implementar dark mode, animaciones y transiciones
- ✅ Integrar TailwindCSS con React, Next.js y bibliotecas de componentes

---

## 📚 Estructura del Bootcamp

### Distribución por Etapas

#### **Fundamentos Web (Semanas 1-2)** - 16 horas

- HTML semántico: etiquetas, accesibilidad, estructura
- CSS esencial: box model, cascade, specificity, unidades
- Entorno de desarrollo: Node.js, npm/pnpm, Vite
- Introducción a TailwindCSS v4: filosofía utility-first
- Instalación y configuración básica
- Primeras clases de utilidad

#### **Core Tailwind (Semanas 3-5)** - 24 horas

- Sistema de diseño: paleta de colores, escala de espaciado
- Tipografía: font-family, font-size, font-weight, line-height, etc.
- Borders y shadows: border-radius, border-width, box-shadow
- Sizing: width, height, min/max, viewport units
- Estados interactivos: hover, focus, active, disabled
- Grupos y pares: `group`, `peer`

#### **Layout (Semanas 6-7)** - 16 horas

- Flexbox utilities: flex, justify, align, wrap, gap
- Grid utilities: grid-cols, grid-rows, col-span, row-span
- Contenedores y breakpoints
- Composición de layouts reales
- Position, z-index y overflow

#### **Componentes & UI (Semanas 8-9)** - 16 horas

- Navbar y header responsive
- Cards y list items
- Buttons y badges
- Forms: inputs, selects, checkboxes, radio
- Modals, drawers y overlays
- Alertas, toasts y notificaciones

#### **Tailwind Avanzado (Semanas 10-11)** - 16 horas

- `tailwind.config.js`/`tailwind.css` y temas personalizados
- CSS variables y design tokens
- Plugins oficiales: Typography, Forms, Aspect Ratio, Line Clamp
- Animaciones y transiciones
- Dark mode: class y media strategy
- Accesibilidad con Tailwind

#### **Ecosistema & Producción (Semana 12)** - 8 horas

- Integración con React y Next.js 15+
- daisyUI y shadcn/ui
- Optimización y purging en producción
- Proyecto final integrador

---

## 🗂️ Estructura de Carpetas

Cada semana sigue esta estructura estándar:

```
bootcamp/week-XX-tema_principal/
├── README.md                 # Descripción y objetivos de la semana
├── rubrica-evaluacion.md     # Criterios de evaluación detallados
├── 0-assets/                 # Imágenes, diagramas y recursos visuales
├── 1-teoria/                 # Material teórico (archivos .md)
├── 2-practicas/              # Ejercicios guiados paso a paso
├── 3-proyecto/               # Proyecto semanal integrador con carpeta solution (oculta)
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/          # Libros electrónicos gratuitos
│   ├── videografia/          # Videos y tutoriales recomendados
│   └── webgrafia/            # Enlaces y documentación
└── 5-glosario/               # Términos clave de la semana (A-Z)
    └── README.md
```

### 📁 Carpetas Raíz

- **`_assets/`**: Recursos visuales globales (logos, headers, etc.)
- **`_docs/`**: Documentación general que aplica a todo el bootcamp
- **`_scripts/`**: Scripts de automatización y utilidades
- **`bootcamp/`**: Contenido semanal del bootcamp

---

## 🎓 Componentes de Cada Semana

### 1. **Teoría** (1-teoria/)

- Archivos markdown con explicaciones conceptuales
- Ejemplos de código HTML/CSS/Tailwind con comentarios claros
- Diagramas y visualizaciones cuando sea necesario
- Referencias a documentación oficial de TailwindCSS

### 2. **Prácticas** (2-practicas/)

- Ejercicios guiados paso a paso
- Incremento progresivo de dificultad
- Soluciones comentadas
- Casos de uso del mundo real

#### 📋 Formato de Ejercicios

Los ejercicios son **tutoriales guiados**, NO tareas con TODOs. El estudiante aprende descomentando código:

**README.md del ejercicio:**

```markdown
### Paso 1: Centrar un div con Flexbox

Explicación del concepto con ejemplo:

\`\`\`html

<!-- Ejemplo explicativo -->
<div class="flex items-center justify-center h-screen">
  <p class="text-xl font-bold">Centrado perfecto</p>
</div>
\`\`\`

**Abre `starter/index.html`** y descomenta la sección correspondiente.
```

**starter/index.html:**

```html
<!-- ============================================ -->
<!-- PASO 1: Centrar un div con Flexbox           -->
<!-- ============================================ -->

<!-- Descomenta las siguientes líneas: -->
<!-- <div class="flex items-center justify-center h-screen"> -->
<!--   <p class="text-xl font-bold">Centrado perfecto</p>  -->
<!-- </div>                                                  -->
```

> ⚠️ **IMPORTANTE**: Los ejercicios NO tienen carpeta `solution/`. El estudiante aprende descomentando el código y verificando que funcione correctamente.

#### ❌ NO usar este formato en ejercicios:

```html
<!-- ❌ INCORRECTO - Este formato es para PROYECTOS, no ejercicios -->
<div class="???">
  <!-- TODO: añadir clases de flexbox -->
  <p>Contenido</p>
</div>
```

#### ✅ Usar este formato en ejercicios:

```html
<!-- ✅ CORRECTO - Código comentado para descomentar -->
<!-- Descomenta las siguientes líneas: -->
<!-- <div class="flex items-center justify-center h-screen"> -->
<!--   <p class="text-xl font-bold">Centrado perfecto</p>     -->
<!-- </div>                                                    -->
```

### 3. **Proyecto** (3-proyecto/)

- Proyecto integrador que consolida lo aprendido
- README.md con instrucciones claras
- Código inicial en `starter/`
- Carpeta `solution/` oculta (en `.gitignore`) solo para instructores
- Criterios de evaluación específicos

#### 📋 Formato de Proyecto (con TODOs)

A diferencia de los ejercicios, el proyecto SÍ usa TODOs para que el estudiante implemente desde cero:

**starter/index.html:**

```html
<!-- ============================================ -->
<!-- COMPONENTE: Navbar responsive                -->
<!-- Crea un navbar con logo, links y hamburger   -->
<!-- ============================================ -->

<!-- TODO: Implementar navbar container con clases Tailwind -->
<!-- Pistas:
  - Usa flex para el layout principal
  - Aplica bg-white shadow-md para el estilo
  - El hamburger debe ser visible solo en mobile (md:hidden)
-->
<nav class="???">
  <!-- TODO: Logo -->
  <!-- TODO: Nav links (ocultos en mobile) -->
  <!-- TODO: Hamburger button (visible solo en mobile) -->
</nav>
```

> 📁 **Estructura del proyecto:**
>
> ```
> 3-proyecto/
> ├── README.md          # Instrucciones del proyecto
> ├── starter/           # Código inicial para el estudiante
> └── solution/          # ⚠️ OCULTA - Solo para instructores
> ```
>
> La carpeta `solution/` está en `.gitignore` y NO se sube al repositorio público.

### 4. **Recursos** (4-recursos/)

- **ebooks-free/**: Libros gratuitos relevantes
- **videografia/**: Videos tutoriales complementarios
- **webgrafia/**: Enlaces a documentación y artículos

### 5. **Glosario** (5-glosario/)

- Términos técnicos ordenados alfabéticamente
- Definiciones claras y concisas
- Ejemplos de código cuando aplique

---

## 📝 Convenciones de Código

### HTML Semántico y Tailwind

```html
<!-- ✅ BIEN - HTML semántico con clases Tailwind descriptivas -->
<nav class="flex items-center justify-between px-6 py-4 bg-white shadow-sm">
  <a href="/" class="text-xl font-bold text-gray-900">Logo</a>
  <ul class="hidden md:flex gap-8">
    <li>
      <a
        href="/about"
        class="text-gray-600 hover:text-gray-900 transition-colors"
        >About</a
      >
    </li>
  </ul>
</nav>

<!-- ✅ BIEN - Componente card con variantes de estado -->
<article
  class="group rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300"
>
  <img
    class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
    src="..."
    alt="..."
  />
  <div class="p-6">
    <h2 class="text-lg font-semibold text-gray-900">Título</h2>
    <p class="mt-2 text-sm text-gray-600 line-clamp-2">Descripción...</p>
  </div>
</article>

<!-- ❌ MAL - clases en orden inconsistente y sin semántica -->
<div
  class="p-6 font-semibold overflow-hidden text-lg rounded-2xl shadow-md text-gray-900"
>
  Título
</div>
```

### Nomenclatura

- **Clases Tailwind**: respetar orden utilitario: layout → sizing → spacing → typography → colors → effects
- **IDs y data-attributes**: kebab-case (`hero-section`, `data-modal-target`)
- **Archivos HTML/CSS**: kebab-case (`hero-section.html`, `custom-theme.css`)
- **Variables CSS**: kebab-case con prefijo (`--color-brand-primary`, `--spacing-section`)
- **Idioma**: inglés para código, español para documentación

### Estructura de Proyecto Tailwind con Vite

```
proyecto/
├── index.html             # Punto de entrada
├── package.json
├── vite.config.js         # Configuración Vite
├── tailwind.config.js     # Configuración Tailwind
├── postcss.config.js
├── src/
│   ├── main.css           # Entry CSS con @import "tailwindcss"
│   ├── components/        # Componentes HTML/JS reutilizables
│   └── assets/            # Imágenes y recursos estáticos
└── public/                # Archivos estáticos públicos
```

---

## 📖 Documentación

### README.md de Semana

Debe incluir:

1. **Título y descripción**
2. **🎯 Objetivos de aprendizaje**
3. **📚 Requisitos previos**
4. **🗂️ Estructura de la semana**
5. **📝 Contenidos** (con enlaces a teoría/prácticas)
6. **⏱️ Distribución del tiempo** (8 horas)
7. **📌 Entregables**
8. **🔗 Navegación** (anterior/siguiente semana)

### Archivos de Teoría

```markdown
# Título del Tema

## 🎯 Objetivos

- Objetivo 1
- Objetivo 2

## 📋 Contenido

### 1. Introducción

### 2. Conceptos Clave

### 3. Ejemplos Prácticos

### 4. Ejercicios

## 📚 Recursos Adicionales

## ✅ Checklist de Verificación
```

---

## 🎨 Recursos Visuales y Estándares de Diseño

### Formato de Assets

- ✅ **Preferir SVG** para todos los diagramas, iconos y gráficos
- ❌ **NO usar ASCII art** para diagramas o visualizaciones
- ✅ Usar PNG/JPG solo para screenshots o fotografías
- ✅ Optimizar imágenes antes de incluirlas

### Criterio para Assets SVG por Semana

Los assets SVG en `0-assets/` de cada semana tienen un propósito educativo específico:

- ✅ **Apoyo visual para comprensión de conceptos teóricos**
- ✅ **Diagramas de arquitectura** (flujo CSS cascade, box model, etc.)
- ✅ **Visualización de procesos** (responsive breakpoints, flex/grid, etc.)
- ✅ **Headers de semana** para identificación visual

**Reglas de vinculación:**

1. Todo SVG debe estar **vinculado en al menos un archivo** de teoría o práctica
2. Usar sintaxis markdown: `![Descripción](../0-assets/nombre.svg)`
3. Incluir texto alternativo descriptivo para accesibilidad
4. Nombrar archivos descriptivamente: `flexbox-model.svg`, `breakpoints.svg`

```markdown
<!-- Ejemplo de vinculación correcta en teoría -->

## Box Model en Tailwind

![Diagrama del box model con clases Tailwind](../0-assets/box-model.svg)

Como se observa en el diagrama, el padding...
```

### Tema Visual

- 🌙 **Tema dark** para todos los assets visuales
- ❌ **Sin degradés** (gradients) en diseños
- ✅ Colores sólidos y contrastes claros
- ✅ Paleta consistente basada en azul cyan TailwindCSS (`#38BDF8` / `sky-400`)

### Tipografía

- ✅ **Fuentes sans-serif** exclusivamente
- ✅ Recomendadas: Inter, Roboto, Open Sans, System UI
- ❌ **NO usar fuentes serif** (Times, Georgia, etc.)
- ✅ Mantener jerarquía visual clara

---

## 🌐 Idioma y Nomenclatura

### Código y Comentarios Técnicos

- ✅ **Nomenclatura en inglés** (clases, variables, IDs, data-attributes)
- ✅ **Comentarios de código en inglés**
- ✅ Usar términos técnicos estándar de la industria

```html
<!-- ✅ CORRECTO - inglés -->
<section
  id="hero-section"
  class="relative flex items-center min-h-screen bg-gray-950"
>
  <!-- Hero content -->
</section>

<!-- ❌ INCORRECTO - español en código -->
<section
  id="seccion-hero"
  class="relative flex items-center min-h-screen bg-gray-950"
>
  <!-- Contenido del hero -->
</section>
```

### Documentación

- ✅ **Documentación en español** (READMEs, teoría, guías)
- ✅ Explicaciones y tutoriales en español
- ✅ Comentarios educativos en español cuando expliquen conceptos

```html
<!-- ✅ CORRECTO - código en inglés, explicación en español -->
<!-- La clase "group" permite que los hijos reaccionen al hover del padre -->
<div class="group cursor-pointer">
  <span class="text-gray-400 group-hover:text-white transition-colors">
    Texto interactivo
  </span>
</div>
```

---

## 🔐 Mejores Prácticas

### HTML Accesible

- Usar elementos semánticos correctos (`<nav>`, `<main>`, `<article>`, `<section>`, etc.)
- Incluir `alt` descriptivo en todas las imágenes
- Usar `aria-label` y `aria-describedby` cuando sea necesario
- Garantizar contraste mínimo WCAG AA (4.5:1 para texto normal)
- Asegurar navegabilidad por teclado

### CSS / Tailwind Limpio

- Mantener el orden de clases: layout → sizing → spacing → typography → colors → effects
- Usar `@apply` con moderación (solo para componentes muy repetidos)
- Preferir composición de clases sobre `@apply` masivo
- Extraer componentes cuando el bloque de clases supera ~10 utilidades repetidas

### Rendimiento

- Siempre usar Tailwind con PostCSS/Vite para purging automático en producción
- Evitar generar clases dinámicas con concatenación de strings (no purgeables)
- Usar `content` en `tailwind.config.js` correctamente para incluir todos los archivos
- Lazy load de imágenes con `loading="lazy"`

---

## 📊 Evaluación

Cada semana incluye **tres tipos de evidencias**:

1. **Conocimiento 🧠** (30%): Evaluaciones teóricas, cuestionarios
2. **Desempeño 💪** (40%): Ejercicios prácticos en clase
3. **Producto 📦** (30%): Proyecto entregable funcional

### Criterios de Aprobación

- Mínimo **70%** en cada tipo de evidencia
- Entrega puntual de proyectos
- Código funcional y bien documentado
- Accesibilidad básica verificada

---

## 🚀 Metodología de Aprendizaje

### Estrategias Didácticas

- **Aprendizaje Basado en Proyectos (ABP)**: Proyectos semanales integradores
- **Práctica Deliberada**: Ejercicios incrementales
- **UI Challenges**: Réplicas de interfaces reales
- **Code Review**: Revisión de código entre estudiantes
- **Live Coding**: Sesiones en vivo de maquetación

### Distribución del Tiempo (8h/semana)

- **Teoría**: 2-2.5 horas
- **Prácticas**: 3-3.5 horas
- **Proyecto**: 2-2.5 horas

---

## 🤖 Instrucciones para Copilot

Cuando trabajes en este proyecto:

### Límites de Respuesta

1. **Divide respuestas largas**
   - ❌ **NUNCA generar respuestas que superen los límites de tokens**
   - ✅ **SIEMPRE dividir contenido extenso en múltiples entregas**
   - ✅ Crear contenido por secciones, esperar confirmación del usuario
   - ✅ Priorizar calidad sobre cantidad en cada entrega
   - Razón: Evitar pérdida de contenido y garantizar completitud

2. **Estrategia de División**
   - Para semanas completas: dividir por carpetas (teoria → practicas → proyecto)
   - Para archivos grandes: dividir por secciones lógicas
   - Siempre indicar claramente qué parte se entrega y qué falta
   - Esperar confirmación del usuario antes de continuar

### Generación de Código

1. **Usa siempre TailwindCSS moderno (v4+)**
   - Usar `@import "tailwindcss"` en lugar del antiguo `@tailwind base/components/utilities`
   - Preferir CSS variables nativas para personalización
   - Usar variantes modernas: `group-hover`, `peer-focus`, `has-*`, `in-*`
   - Responsive: siempre mobile-first (`sm:`, `md:`, `lg:`, `xl:`, `2xl:`)
   - Dark mode: siempre con la variante `dark:`

2. **Entorno de Desarrollo con Node.js + Vite**
   - ✅ **USAR Vite** como bundler para HMR y builds optimizados
   - ✅ **pnpm** como gestor de paquetes (rápido y eficiente en disco)
   - ✅ Crear archivos `.env` para variables de entorno si aplica
   - Razón: Entorno consistente, reproducible y moderno

   Estructura recomendada:

   ```
   proyecto/
   ├── package.json
   ├── vite.config.js
   ├── tailwind.config.js
   ├── postcss.config.js
   ├── index.html
   └── src/
       └── main.css
   ```

   Comandos esenciales:

   ```bash
   # Crear proyecto
   pnpm create vite@latest mi-proyecto -- --template vanilla

   # Instalar Tailwind
   pnpm add -D tailwindcss @tailwindcss/vite

   # Desarrollo
   pnpm dev

   # Build producción
   pnpm build
   ```

3. **Clases Tailwind: orden consistente**
   Layout primero, luego sizing, spacing, typography, colors, borders, effects:

   ```html
   <!-- ✅ Orden correcto -->
   <div
     class="flex items-center justify-between w-full max-w-7xl mx-auto px-6 py-4 text-sm font-medium text-gray-700 bg-white border-b border-gray-200 shadow-sm hover:bg-gray-50 transition-colors"
   ></div>
   ```

4. **Accesibilidad siempre presente**
   - `alt` en imágenes
   - `aria-label` en botones sin texto
   - Roles semánticos correctos
   - Contraste WCAG AA mínimo

5. **Comenta el código de manera educativa**
   - Explica el propósito de grupos de clases para principiantes
   - Incluye referencias a la documentación oficial cuando sea útil
   - Usa comentarios que enseñen, no solo describan

6. **Proporciona ejemplos completos y funcionales**
   - Código HTML que se pueda copiar, abrir en browser y ver resultados
   - Incluye casos de uso realistas (landing pages, dashboards, forms)
   - Muestra tanto lo que se debe hacer como lo que se debe evitar

### Creación de Contenido

1. **Estructura clara y progresiva**
   - De lo simple a lo complejo
   - Conceptos construidos sobre conocimientos previos
   - Repetición espaciada de conceptos clave

2. **Ejemplos del mundo real**
   - Casos de uso prácticos y relevantes
   - Proyectos que los estudiantes puedan mostrar en portfolios
   - Interfaces que reconozcan de sitios reales (Stripe, Vercel, Linear)

3. **Enfoque moderno**
   - No mencionar características obsoletas (PostCSS `@tailwind` old API)
   - Enfocarse en Tailwind v4 y sus mejoras
   - Usar herramientas y patrones modernos

### Respuestas y Ayuda

1. **Explicaciones claras**
   - Lenguaje simple y directo
   - Evitar jerga innecesaria
   - Proporcionar analogías cuando sea útil

2. **Código comentado**
   - Explicar cada grupo de clases importante
   - Destacar conceptos clave de Tailwind
   - Señalar posibles errores comunes (clases que no existen, typos)

3. **Recursos adicionales**
   - Referencias a documentación oficial de TailwindCSS
   - Enlace a Tailwind Play para demos interactivos
   - Artículos relevantes de calidad

---

## 📚 Referencias Oficiales

- **TailwindCSS Documentation**: https://tailwindcss.com/docs
- **Tailwind Play (sandbox)**: https://play.tailwindcss.com/
- **Tailwind UI**: https://tailwindui.com/
- **Headless UI**: https://headlessui.com/
- **daisyUI**: https://daisyui.com/
- **shadcn/ui**: https://ui.shadcn.com/
- **Vite Documentation**: https://vitejs.dev/
- **MDN Web Docs**: https://developer.mozilla.org/

---

## 🔗 Enlaces Importantes

- **Repositorio**: https://github.com/ergrato-dev/bc-tailwindcss
- **Documentación general**: [\_docs/README.md](_docs/README.md)
- **Primera semana**: [bootcamp/week-01-html_semantico_y_css_esencial/README.md](bootcamp/week-01-html_semantico_y_css_esencial/README.md)

---

## ✅ Checklist para Nuevas Semanas

Cuando crees contenido para una nueva semana:

- [ ] Crear estructura de carpetas completa
- [ ] README.md con objetivos y estructura
- [ ] Material teórico en 1-teoria/
- [ ] Ejercicios prácticos en 2-practicas/
- [ ] Proyecto integrador en 3-proyecto/
- [ ] Recursos adicionales en 4-recursos/
- [ ] Glosario de términos en 5-glosario/
- [ ] Rúbrica de evaluación
- [ ] Verificar coherencia con semanas anteriores
- [ ] Revisar progresión de dificultad
- [ ] Probar código de ejemplos en browser

---

## 💡 Notas Finales

- **Prioridad**: Claridad sobre brevedad
- **Enfoque**: Aprendizaje práctico sobre teoría abstracta
- **Objetivo**: Preparar desarrolladores frontend listos para trabajar
- **Filosofía**: TailwindCSS moderno desde el día 1

---

_Última actualización: Marzo 2026_
_Versión: 1.0_
