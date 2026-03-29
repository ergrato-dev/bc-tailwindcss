# 📊 Rúbrica de Evaluación — Semana 3

**Bootcamp TailwindCSS Zero to Hero** | Semana 3: Colores, Tipografía y Espaciado

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Paleta de Colores** | Explica la escala 50-950, sabe elegir tonos para texto/fondo/borde según contraste y rol visual | Usa colores correctamente pero no sabe explicar cuándo usar 100 vs 500 | Usa colores al azar sin considerar contraste ni jerarquía |
| **Tipografía** | Domina font-size, font-weight, line-height, letter-spacing y font-family; explica cuándo usar cada uno | Aplica los más comunes (text-*, font-*) con alguna confusión en line-height | No puede aplicar más de 2-3 clases tipográficas sin documentación |
| **Espaciado** | Explica la escala de 4px, diferencia px/py/px-4 sin consultar; elige espaciado apropiado por contexto | Aplica padding y margin básicos pero confunde px/py o mx/my | No puede predecir el valor en px de una clase de espaciado |
| **space-x / space-y** | Explica cuándo space-* es mejor que gap o margin individual; lo usa correctamente | Usa space-* pero confunde cuándo conviene vs gap | Desconoce space-x / space-y |
| **Sistema de Diseño** | Explica cómo la escala consistente de Tailwind elimina decisiones arbitrarias y mejora coherencia | Entiende el concepto pero no puede argumentarlo con ejemplos concretos | No comprende el valor del sistema de diseño vs valores custom |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Paleta** | Crea paleta de colores semántica (texto, fondo, acento, borde) con contrastes WCAG AA | Crea paleta funcional con algunas combinaciones de bajo contraste | Selecciona colores sin considerar contrastes ni roles |
| **Ejercicio Tipografía** | Sistema tipográfico completo: jerarquía clara, pesos y tamaños coherentes, line-height correcto | Sistema funcional con 1-2 inconsistencias menores | Sin jerarquía visual; pesos o tamaños aplicados al azar |
| **Ejercicio Espaciado** | Layout con espaciado perfecto: padding/margin consistentes, space-y para listas, gap para grids | Espaciado mayormente correcto con algún margen faltante o inconsistente | Elementos apilados sin espaciado o con overflow |
| **Ejercicio Página Info** | Combina los tres sistemas (color, tipografía, espaciado) en una página coherente y legible | Combina los sistemas con 1-2 inconsistencias de jerarquía | No logra integrar los tres sistemas de forma coherente |

---

## 📦 Producto (30%)

**Proyecto: Blog Post Estilizado**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Colores** | Paleta semántica: texto principal/secundario, fondo, badges con colores de categoría, alto contraste | Paleta funcional con pocas inconsistencias de contraste | Colores arbitrarios sin sistema ni consideración de contraste |
| **Tipografía** | Jerarquía clara: h1>h2>h3>body; line-height legible en párrafos; peso correcto por nivel | Jerarquía mayormente correcta con algún nivel confuso | Sin jerarquía tipográfica; todos los textos parecen iguales |
| **Espaciado** | Espaciado consistente: márgenes entre secciones, padding de contenedor, gap entre elementos | Espaciado funcional con algún valor inconsistente | Elementos sin respiro o con valores de espaciado aleatorios |
| **HTML Semántico** | `article`, `h1-h3`, `p`, `time`, `address`, `ul/li`, `blockquote` usados correctamente | HTML funcional con algún elemento semántico faltante u omitido | Solo div/span sin semántica |
| **Legibilidad** | max-width en prose (~65ch), line-height 1.6-1.8 en texto corrido, contraste mínimo WCAG AA | Legible con pocas mejoras necesarias | Texto difícil de leer por falta de ancho máximo, line-height o contraste |

---

## 📈 Cálculo de Calificación

```
Nota final = (Conocimiento × 30%) + (Desempeño × 40%) + (Producto × 30%)
```

**Mínimo para aprobar**: 70% en cada tipo de evidencia.
