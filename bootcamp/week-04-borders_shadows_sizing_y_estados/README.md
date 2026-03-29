# 🔲 Semana 4: Borders, Shadows, Sizing y Estados Interactivos

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Aplicar bordes con control de ancho, color, estilo y radio
- ✅ Usar `rounded-*` para crear formas redondeadas y círculos
- ✅ Aplicar sombras de caja (`shadow-*`) y de texto (`drop-shadow-*`)
- ✅ Controlar dimensiones con `w-*`, `h-*`, `min-*`, `max-*`
- ✅ Usar unidades viewport (`w-screen`, `h-dvh`) y fraccionarias (`w-1/2`, `w-1/3`)
- ✅ Implementar estados interactivos: `hover:`, `focus:`, `active:`, `disabled:`
- ✅ Usar los modificadores `group` y `peer` para estados en elementos relacionados

---

## 📚 Requisitos Previos

- **Semanas 1-3 completadas**
- Dominio básico de colores, tipografía y espaciado de Tailwind

---

## 🗂️ Estructura de la Semana

```
week-04-borders_shadows_sizing_y_estados/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
├── 1-teoria/
│   ├── 01-borders-y-rounded.md
│   ├── 02-shadows.md
│   ├── 03-sizing.md
│   └── 04-estados-interactivos.md
├── 2-practicas/
│   ├── 01-ejercicio-borders/
│   ├── 02-ejercicio-shadows/
│   ├── 03-ejercicio-sizing/
│   └── 04-ejercicio-estados/
├── 3-proyecto/
│   └── boton-interactivo-y-avatar/
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
| [Borders y Rounded](1-teoria/01-borders-y-rounded.md) | 30 min | border-width, color, style, radius desde `rounded-sm` a `rounded-full` |
| [Shadows](1-teoria/02-shadows.md) | 25 min | box-shadow con `shadow-*`, ring utilities, drop-shadow |
| [Sizing](1-teoria/03-sizing.md) | 30 min | w/h fijos, porcentuales, viewport, fraccionarios, auto, full |
| [Estados Interactivos](1-teoria/04-estados-interactivos.md) | 35 min | hover, focus, active, disabled, group, peer |

### 2️⃣ Prácticas (3-3.5 horas)

| Ejercicio | Duración | Nivel | Objetivo |
|-----------|----------|-------|----------|
| Borders y Formas | 45 min | Básico | Crear badges, avatares y separadores con bordes |
| Shadows | 40 min | Básico | Aplicar profundidad con sombras en cards |
| Sizing | 45 min | Básico | Controlar dimensiones de una galería de imágenes |
| Estados Interactivos | 60 min | Medio | Botones, inputs e items con feedback visual |

### 3️⃣ Proyecto (2-2.5 horas)

**Kit de Botones e Imagen de Avatar**

Construir un kit de componentes atómicos:
- 4 variantes de botón: primario, secundario, outline, destructivo
- Cada botón con estados: default, hover, focus, active, disabled
- Avatar con imagen circular + badge de estado (online/offline)
- Input de formulario con estado focus y error

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
| **Día 1** | Teoría: Borders + Shadows | 1h |
| **Día 2** | Teoría: Sizing + Estados | 1.25h |
| **Día 3** | Prácticas: Borders + Shadows | 1.5h |
| **Día 4** | Prácticas: Sizing + Estados | 1.75h |
| **Día 5-6** | Proyecto: Kit de botones y avatar | 2-2.5h |

---

## 📌 Entregable

**Proyecto: [Kit de Botones e Avatar](3-proyecto/)**

Componentes atómicos funcionales:

- [ ] 4 variantes de botón con todos los estados visibles
- [ ] `focus:ring` correcto en botones para accesibilidad por teclado
- [ ] Avatar circular con badge de estado
- [ ] `disabled:` state con cursor y opacidad correctos
- [ ] `group-hover:` usado en al menos un componente

---

## 🎓 Conceptos Clave

- **`rounded-full`**: Hace el elemento completamente circular/ovalado
- **`ring-*`**: Sombra interna tipo "outline" (ideal para focus accesible)
- **`shadow-{size}`**: De `shadow-sm` (sutil) a `shadow-2xl` (muy pronunciada)
- **`w-full`**: Ocupa el 100% del contenedor padre
- **`max-w-*`**: Limita el ancho máximo (muy usado en contenedores de página)
- **`hover:`**: Prefijo para estilos que se aplican al pasar el cursor
- **`focus:`**: Prefijo para estilos cuando el elemento tiene foco de teclado
- **`group`**: Clase aplicada al padre para que los hijos usen `group-hover:`
- **`peer`**: Clase aplicada a un input para estilar el label hermano con `peer-focus:`

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [TailwindCSS Docs: Border Radius](https://tailwindcss.com/docs/border-radius)
- [TailwindCSS Docs: Box Shadow](https://tailwindcss.com/docs/box-shadow)
- [TailwindCSS Docs: Hover, Focus, and Other States](https://tailwindcss.com/docs/hover-focus-and-other-states)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 5, asegúrate de:

- [ ] Crear avatares circulares con borde de color
- [ ] Aplicar `focus:ring` en todos los elementos interactivos
- [ ] Usar `group` + `group-hover:` en al menos un componente
- [ ] Controlar `max-w-*` para limitar el ancho de un contenedor
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar el kit de botones funcional y accesible
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Semana 3: Colores, Tipografía y Espaciado](../week-03-colores_tipografia_y_espaciado/README.md)  
➡️ **Siguiente**: [Semana 5: Responsive Design y Mobile-First](../week-05-responsive_design_y_mobile_first/README.md)

---

## 💡 Consejos para Esta Semana

> 🎯 **`focus:ring` no es opcional**: La accesibilidad por teclado requiere indicadores de foco visibles. `focus:outline-none focus:ring-2 focus:ring-blue-500` es el patrón estándar.

> 🖱️ **Piensa en todos los estados**: Un botón tiene al menos 5 estados (default, hover, focus, active, disabled). Diseña todos desde el principio.

> 👥 **`group` es muy poderoso**: Permite crear efectos donde el hijo reacciona al hover del padre. Muy usado en cards y menús desplegables.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Los detalles hacen la diferencia! 🔲</strong><br>
  <em>Bordes, sombras y estados son los que hacen una UI sentirse "pulida"</em>
</p>

<p align="center">
  <a href="1-teoria/01-borders-y-rounded.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
