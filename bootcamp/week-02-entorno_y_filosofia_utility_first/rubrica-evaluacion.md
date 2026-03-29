# 📊 Rúbrica de Evaluación — Semana 2

**Bootcamp TailwindCSS Zero to Hero** | Semana 2: Entorno de Desarrollo y Filosofía Utility-First

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Filosofía Utility-First** | Explica con precisión las ventajas de utility-first vs BEM/CSS modules y cuándo NO usarlo | Entiende el concepto pero no puede argumentar sus ventajas en un contexto real | Confunde utility-first con CSS inline o no comprende su propósito |
| **Instalación Vite + Tailwind** | Explica cada devDependency, el rol de PostCSS y por qué se usa `@import "tailwindcss"` | Sabe los pasos pero no puede explicar qué hace cada uno | No recuerda los comandos de instalación o confunde la configuración |
| **Estructura del Proyecto** | Explica el rol de `vite.config.js`, `postcss.config.js`, `main.css` y cómo Tailwind genera CSS | Conoce los archivos principales pero no sabe cómo interactúan | No sabe dónde va la configuración de Tailwind |
| **JIT y Purging** | Explica qué es JIT, cómo detecta clases usadas y el resultado de `pnpm build` | Sabe que Tailwind elimina clases no usadas pero no sabe cómo | Desconoce el concepto de purging o cree que incluye todo Tailwind |
| **IntelliSense** | Usa IntelliSense correctamente; sabe cómo activarlo y para qué sirve cada sugerencia | Tiene IntelliSense instalado pero no lo usa activamente | No tiene IntelliSense o no lo ha configurado |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Setup del Entorno** | Proyecto Vite + Tailwind v4 creado e iniciado en < 5 min sin errores; HMR funcionando | Proyecto creado pero con algún error menor resuelto con ayuda | No logra levantar el servidor de desarrollo |
| **Utility vs CSS** | Replica el mismo diseño en menos clases Tailwind que propiedades CSS; explica las diferencias | Replica el diseño con Tailwind pero necesita guía para algunas clases | No puede traducir propiedades CSS a clases Tailwind |
| **Primeras Clases** | Usa correctamente: color, bg, padding, margin, text-size, font-weight, rounded, border | Usa la mayoría correctamente; pocos errores de sintaxis (e.g. `p-4` en lugar de `pt-4`) | Más de la mitad de las clases tienen errores o no corresponden |
| **Componente Básico** | Badge/pill con variantes de color usando solo clases Tailwind; código semántico | Badge funcional pero sin variantes o con CSS inline adicional | No logra construir el componente |

---

## 📦 Producto (30%)

**Proyecto: Tarjeta de Perfil**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Setup Correcto** | `@import "tailwindcss"` en main.css; sin `@tailwind base/utilities` legacy | Usa el import correcto pero con archivos de configuración desorganizados | Usa el CDN o la API legacy de Tailwind v3 |
| **Diseño con Tailwind** | Toda la estiización con clases Tailwind; cero CSS personalizado; orden de clases correcto | Principalmente Tailwind; algún estilo inline o CSS externo menor | Mezcla considerable de CSS propio y Tailwind |
| **Responsive** | Se ve bien en mobile y desktop; usa al menos un breakpoint (`md:` o `lg:`) | Funciona en desktop; en mobile hay overflow o elementos rotos | Solo diseñado para un tamaño de pantalla |
| **HTML Semántico** | Usa `article`, `header`, `footer`, `img` con `alt`, `address` o `dl` donde aplica | HTML funcional con algún `div` innecesario | Solo `div`s sin semántica |
| **Calidad Visual** | Diseño equilibrado: espaciado consistente, tipografía legible, jerarquía visual clara | Diseño funcional con alguna inconsistencia de espaciado | Elementos sin espaciado o visualmente desorganizados |

---

## 📈 Cálculo de Calificación

```
Nota final = (Conocimiento × 30%) + (Desempeño × 40%) + (Producto × 30%)
```

**Mínimo para aprobar**: 70% en cada tipo de evidencia.
