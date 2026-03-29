# Proyecto Semana 3: Blog Post Estilizado

## 📋 Descripción

Construye una **página de artículo de blog** completamente estilizada usando el sistema de colores, tipografía y espaciado de TailwindCSS. Este proyecto es un ejercicio puro de dominio del sistema de diseño de Tailwind.

---

## 🎯 Objetivos

- Aplicar jerarquía tipográfica coherente (h1 → h2 → h3 → body)
- Usar colores semánticos para categorías, meta, código y alertas
- Mantener espaciado consistente a través de toda la página
- Asegurar legibilidad con line-height y max-width correctos

---

## 📐 Estructura esperada

```
┌──────────────────────────────────────────┐
│  HEADER: Nav simple                      │
├──────────────────────────────────────────┤
│  HERO DEL ARTÍCULO                       │
│  Categoría badge + Fecha                 │
│  H1: Título del artículo                 │
│  Lead paragraph (text-xl)                │
│  Autor + tiempo de lectura               │
├──────────────────────────────────────────┤
│  CUERPO DEL ARTÍCULO (max-w-2xl)         │
│  H2 + párrafos + H3 + lista              │
│  Blockquote                              │
│  Snippet de código                       │
│  Alerta/nota                             │
├──────────────────────────────────────────┤
│  FOOTER: Copyright                       │
└──────────────────────────────────────────┘
```

---

## 📁 Estructura

```
3-proyecto/blog-post-estilizado/
├── README.md
└── starter/
    └── index.html
```

---

## 📋 Requisitos

### Tipografía
- [ ] `h1` con `text-4xl font-bold leading-tight tracking-tight`
- [ ] Párrafos con `text-base leading-relaxed`
- [ ] Categoría con `text-xs uppercase tracking-widest`
- [ ] Al menos un `h2` y un `h3` claramente distintos

### Colores
- [ ] Badge de categoría con color semántico
- [ ] Texto principal: `text-gray-900`; secundario: `text-gray-600`
- [ ] Blockquote o alerta con paleta de acento

### Espaciado
- [ ] `max-w-2xl mx-auto` para el contenido del artículo
- [ ] `space-y-6` o `mt-6` entre bloques de texto
- [ ] `py-16` o mayor en secciones principales

### HTML Semántico
- [ ] `<article>` para el cuerpo
- [ ] `<time>` para la fecha
- [ ] `<blockquote>` para citas
- [ ] `<code>` o `<pre>` para código
