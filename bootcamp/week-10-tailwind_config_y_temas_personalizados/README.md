# ⚙️ Semana 10: Tailwind Config y Temas Personalizados

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Entender la estructura de `tailwind.config.js` (o `tailwind.css` en v4)
- ✅ Extender la paleta de colores con colores de marca propios
- ✅ Definir tipografías, espaciados y breakpoints personalizados
- ✅ Usar CSS variables como design tokens interoperables con Tailwind
- ✅ Crear utilidades personalizadas con `@layer utilities`
- ✅ Usar `@apply` de forma moderada para componentes muy repetidos
- ✅ Construir un design system coherente con valores de marca

---

## 📚 Requisitos Previos

- **Semanas 1-9 completadas**
- Dominio completo de las utilidades core de Tailwind

---

## 🗂️ Estructura de la Semana

```
week-10-tailwind_config_y_temas_personalizados/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-tailwind-config-estructura.md
│   ├── 02-extender-paleta-tipografia.md
│   ├── 03-css-variables-y-design-tokens.md
│   └── 04-layer-utilities-y-apply.md
├── 2-practicas/
│   ├── 01-ejercicio-colores-marca/
│   ├── 02-ejercicio-tipografia-custom/
│   ├── 03-ejercicio-design-tokens/
│   └── 04-ejercicio-tema-completo/
├── 3-proyecto/
│   └── landing-con-tema-de-marca/
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
| [Estructura tailwind.config.js](1-teoria/01-tailwind-config-estructura.md) | 30 min | `theme`, `extend`, `content`, `plugins` en v3/v4 |
| [Extender Paleta y Tipografía](1-teoria/02-extender-paleta-tipografia.md) | 35 min | Agregar colores de marca, fuentes custom, escala de spacing |
| [CSS Variables y Design Tokens](1-teoria/03-css-variables-y-design-tokens.md) | 30 min | `--color-brand-*`, integrar variables CSS con Tailwind |
| [`@layer` y `@apply`](1-teoria/04-layer-utilities-y-apply.md) | 25 min | Cuándo y cómo usar `@layer utilities`, `@layer components`, `@apply` |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Colores de Marca | 45 min | Medio | Definir paleta `brand-*` con 9 tonos propios |
| Tipografía Custom | 45 min | Medio | Configurar fuentes de Google Fonts + escala custom |
| Design Tokens | 50 min | Medio | CSS variables que alimentan a Tailwind |
| Tema Completo | 55 min | Avanzado | Config completa: colores + fuentes + spacing + breakpoints |

### 3️⃣ Proyecto (2-2.5 horas)

**Landing con Tema de Marca**

Rediseñar la landing de la Semana 7 con un tema personalizado:
- Paleta de colores de marca definida en config
- Tipografía propia (Google Fonts o system fonts)
- CSS variables para modo claro/oscuro
- Espaciado custom para secciones
- Al menos 2 utilidades personalizadas con `@layer`

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
| **Día 1** | Teoría: Config estructura + Paleta/Tipografía | 1.25h |
| **Día 2** | Teoría: CSS variables + @layer/@apply | 1h |
| **Día 3** | Prácticas: Colores de marca + Tipografía | 1.5h |
| **Día 4** | Prácticas: Design tokens + Tema completo | 1.75h |
| **Día 5-6** | Proyecto: Landing con tema de marca | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Landing con Tema de Marca](3-proyecto/)**

Landing page completamente temática con config personalizada:

- [ ] `tailwind.config.js` (o config en CSS v4) con colores `brand-*` definidos
- [ ] Fuente personalizada cargada y configurada en Tailwind
- [ ] CSS variables (`--color-brand-primary`, etc.) usadas en la configuración
- [ ] Al menos 1 utilidad customizada con `@layer utilities`
- [ ] Diseño visualmente diferenciado del tema por defecto de Tailwind

---

## 🎓 Conceptos Clave

- **`theme.extend`**: Agregar valores nuevos sin reemplazar los existentes de Tailwind
- **`theme.colors`** (sin `extend`): Reemplaza toda la paleta (usa con cuidado)
- **`@layer utilities`**: Agrega utilidades custom que se comportan como las nativas de Tailwind
- **`@layer components`**: Agrega bloques de clases reutilizables (usar con moderación)
- **`@apply`**: Agrupa clases Tailwind en una regla CSS — útil solo para componentes muy repetidos
- **CSS custom properties**: `--color-brand: #3b82f6` es usable como `bg-[var(--color-brand)]`
- **Design tokens**: Valores de diseño centralizados que mantienen la consistencia de marca

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Configuration](https://tailwindcss.com/docs/configuration)
- [TailwindCSS Docs: Adding Custom Styles](https://tailwindcss.com/docs/adding-custom-styles)
- [TailwindCSS v4: CSS-first configuration](https://tailwindcss.com/docs/v4-upgrade)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 11, asegúrate de:

- [ ] Definir colores custom y usarlos con clases `bg-brand-500 text-brand-100`
- [ ] Cargar una fuente externa y configurarla como `font-display` en Tailwind
- [ ] Crear al menos una utilidad con `@layer utilities`
- [ ] Entender la diferencia entre `extend` y reemplazar en el config
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar la landing con tema de marca coherente
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 9: Componentes - Forms, Modals y Alertas](../week-09-componentes_forms_modals_alertas/README.md)  
➡️ **Siguiente**: [Semana 11: Plugins, Animaciones y Dark Mode](../week-11-plugins_animaciones_y_dark_mode/README.md)

---

## 💡 Consejos para Esta Semana

> 🎨 **Usa siempre `extend`**: Salvo que tengas una razón muy concreta, usa `theme.extend` para no perder los valores por defecto de Tailwind (colores, spacing, etc.).

> 🔤 **Google Fonts en CSS, no en HTML**: Carga las fuentes con `@import` en tu CSS, no con `<link>` en el HTML. Luego regístralas en el config de Tailwind.

> ⚠️ **`@apply` es el último recurso**: Si te encuentras escribiendo `@apply flex items-center justify-between` en muchos lugares, extrae un componente HTML, no uses `@apply`. Es una señal de que necesitas un componente.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Tailwind a tu medida! ⚙️</strong><br>
  <em>Con la configuración correcta, Tailwind funciona exactamente como tu design system</em>
</p>

<p align="center">
  <a href="1-teoria/01-tailwind-config-estructura.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
