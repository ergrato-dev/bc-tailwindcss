# Guía de Contribución

¡Gracias por tu interés en contribuir al Bootcamp TailwindCSS Zero to Hero! 🎉

Este proyecto es mantenido por [ergrato-dev](https://github.com/ergrato-dev) y toda contribución es bienvenida, ya sea una corrección de typo, mejora de contenido o nuevo material.

---

## 📋 Tipos de contribuciones aceptadas

- **Correcciones**: typos, errores de código, links rotos
- **Mejoras de contenido**: ejemplos más claros, explicaciones más precisas
- **Traducción**: mejorar o corregir la documentación en inglés
- **Nuevos recursos**: añadir recursos (webgrafia, videografía, ebooks) relevantes y gratuitos
- **Reportar errores**: crear Issues descriptivos con pasos para reproducir
- **Sugerencias**: proponer nuevos temas, ejercicios o mejoras de estructura

---

## 🔧 Cómo contribuir

### 1. Reportar un problema

Abre un [Issue](https://github.com/ergrato-dev/bc-tailwindcss/issues/new/choose) usando la plantilla adecuada:

- **Bug report**: para errores en código, links rotos, contenido incorrecto
- **Feature request**: para sugerir nuevo contenido o mejoras

### 2. Proponer un cambio de código o contenido

1. **Fork** del repositorio
2. **Crea una rama** descriptiva:
   ```bash
   git checkout -b fix/week-03-typo-flexbox
   git checkout -b feat/week-06-add-example-grid
   ```
3. **Realiza los cambios** siguiendo las convenciones del proyecto
4. **Commit** con mensaje descriptivo en español:
   ```bash
   git commit -m "fix(week-03): corregir ejemplo de flexbox gap"
   git commit -m "feat(week-06): añadir ejemplo de grid auto-fill"
   ```
5. **Push** y abre un **Pull Request** describiendo los cambios

---

## 📐 Convenciones del proyecto

### Idioma
- **Documentación y explicaciones**: español
- **Código y comentarios técnicos**: inglés (clases, IDs, variables)

### Código HTML/Tailwind
- Orden de clases: layout → sizing → spacing → typography → colors → effects
- HTML semántico siempre (`<nav>`, `<main>`, `<article>`, `<section>`, etc.)
- `alt` en imágenes, `aria-label` en botones de icono

### Archivos Markdown
- Títulos con emoji descriptivo según la sección
- Ejemplos de código con syntax highlighting (```html, ```js, etc.)
- Links a documentación oficial cuando aplique

### Assets SVG
- Tema oscuro (fondo `#030712`)
- Sin degradados (gradients)
- Paleta: sky-400 (`#38BDF8`), violet (`#818CF8`), green (`#34D399`), red (`#F87171`)

---

## ✅ Checklist antes de abrir un PR

- [ ] Los cambios siguen las convenciones del proyecto
- [ ] El código HTML se puede abrir en el browser y funciona correctamente
- [ ] No hay errores de consola
- [ ] Los links internos son relativos y funcionan
- [ ] El contenido está en español (documentación) o inglés (código)

---

## 🚫 Qué NO incluir

- Soluciones completas de los proyectos semanales (van en `solution/`, que está en `.gitignore`)
- Dependencias externas no aprobadas
- Contenido con copyright sin permiso explícito
- Código generado por IA sin revisión humana

---

## 💬 ¿Preguntas?

Abre un [Issue](https://github.com/ergrato-dev/bc-tailwindcss/issues) con la etiqueta `question` o contacta directamente en GitHub: [@ergrato-dev](https://github.com/ergrato-dev).

---

_Este proyecto sigue el [Código de Conducta](CODE_OF_CONDUCT.md). Al contribuir, aceptas cumplirlo._
