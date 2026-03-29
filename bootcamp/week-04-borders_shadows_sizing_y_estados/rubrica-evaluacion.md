# 📊 Rúbrica de Evaluación — Semana 4

**Bootcamp TailwindCSS Zero to Hero** | Semana 4: Borders, Shadows, Sizing y Estados

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Borders y Rounded** | Explica `border`, `border-{n}`, `border-{color}`, `rounded-*` y cuándo usar cada uno; entiende la diferencia entre `rounded` y `rounded-full` | Aplica bordes y redondeados básicos sin confundir lados | Confunde `border` (ancho) con `border-color` o aplica mal `rounded` |
| **Shadows** | Domina `shadow-sm` a `shadow-2xl`, `shadow-{color}`, `drop-shadow`; elige la sombra correcta por uso contextual | Aplica sombras comunes (`shadow-sm`, `shadow-md`) sin errores | Aplica sombras al azar sin considerar profundidad visual |
| **Sizing** | Conoce `w-*`, `h-*`, `min/max-w/h`, valores especiales (`full`, `screen`, `fit`, `auto`); opera con el box model | Aplica `w-*` y `h-*` correctamente; confunde `w-full` vs `w-screen` | No puede predecir cómo se verá un elemento con un tamaño dado |
| **Estados interactivos** | Domina `hover:`, `focus:`, `active:`, `disabled:`, `focus-visible:`; explica cuándo usar cada uno con accesibilidad | Usa `hover:` y `focus:` correctamente; confunde `focus` vs `focus-visible` | Solo usa `hover:` sin considerar keyboard nav o disabled states |
| **Group y Peer** | Explica y usa `group`, `group-hover:`, `peer`, `peer-checked:` en componentes reales | Usa `group-hover:` correctamente pero desconoce `peer` | No conoce `group` ni `peer` |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Borders** | Card con bordes, redondeados, dividers y outline de focus completamente correctos | Card con bordes y rounded funcionales, 1-2 detalles menores | Card sin bordes coherentes o con errores de radius |
| **Ejercicio Shadows** | Panel de sombras con escala visible, coloured shadows y hover que eleva la sombra | Sombras básicas aplicadas correctamente | Sombras aplicadas sin escala ni interacción |
| **Ejercicio Sizing** | Grid de componentes con `w-*`, `min-w`, `max-w`, aspect-ratio y viewport units correctos | Sizing básico correcto; 1-2 conflictos de overflow | Overflow no controlado o tamaños inconsistentes |
| **Ejercicio Estados** | Todos los estados (hover, focus, active, disabled, focus-visible) con feedback visual distinto y accesible | Estados hover y focus funcionan; falta disabled o active | Solo hover; sin feedback de focus para teclado |

---

## 📦 Producto (30%)

**Proyecto: Tarjeta de Producto con Interacciones**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Visual Base** | Border correcto, `rounded-xl`, sombra que eleva en hover, imagen con `object-cover` | Card visible con bordes y sombra; hover raro pero funcional | Sin bordes, sin sombra o sin rounded |
| **Sizing** | Ancho controlado `max-w-sm`, altura de imagen fija con `h-48`, texto con `truncate`/`line-clamp` | Tamaños básicos correctos; imagen con overflow visible | Sin control de tamaños; imagen deforma la tarjeta |
| **Estados completos** | Hover eleva (`shadow-lg`, escala), botón con todos los estados (hover/focus/active/disabled) | Hover y focus en botón; falta active o disabled | Solo hover; sin focus visible para teclado |
| **Group hover** | Usa `group` en la card para que la imagen haga zoom y el título cambie de color en hover | Usa `group-hover:` en al menos un elemento | No usa `group` |
| **Accesibilidad** | `focus-visible:ring-*` en botón, `alt` en imagen, contraste WCAG AA en todos los textos | `focus:ring-*` en botón; algún contraste bajo | Sin feedback de foco visible |

---

## 📈 Cálculo de Calificación

```
Nota final = (Conocimiento × 30%) + (Desempeño × 40%) + (Producto × 30%)
```

**Mínimo para aprobar**: 70% en cada tipo de evidencia.
