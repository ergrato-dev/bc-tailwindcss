# Proyecto Semana 1: Landing Page Estática

## 📋 Descripción

Construye una **landing page estática** completa usando exclusivamente HTML semántico y CSS puro — sin frameworks, sin JavaScript, sin librerías.

Esta landing representará un servicio ficticio de diseño web llamado **"PixelCraft Studio"**. El objetivo no es el contenido sino la **estructura y técnica**.

---

## 🎯 Objetivos

- Demostrar dominio de HTML5 semántico con landmarks correctos
- Aplicar el box model con `box-sizing: border-box` de forma consistente
- Usar `em` y `rem` apropiadamente para tipografía y espaciado
- Resolver conflictos CSS con especificidad controlada (sin `!important`)
- Construir un layout completo con múltiples secciones

---

## 📐 Diseño Esperado

La landing debe tener las siguientes secciones:

```
┌─────────────────────────────────────────┐
│  HEADER: Logo + Nav (links)             │
├─────────────────────────────────────────┤
│  HERO: Título grande + subtítulo + CTA  │
├─────────────────────────────────────────┤
│  FEATURES: 3 tarjetas de servicios      │
│  [ Card 1 ]  [ Card 2 ]  [ Card 3 ]     │
├─────────────────────────────────────────┤
│  FOOTER: Copyright + links              │
└─────────────────────────────────────────┘
```

---

## 📁 Estructura del Proyecto

```
3-proyecto/landing-estatica/
├── README.md              ← Este archivo
└── starter/
    ├── index.html         ← Tu implementación HTML (con TODOs)
    └── styles.css         ← Tu implementación CSS (con TODOs)
```

---

## 🚀 Instrucciones

### 1. Abrir los archivos

Abre `starter/index.html` y `starter/styles.css` en VS Code.

### 2. Completar los TODOs

Cada `<!-- TODO -->` en el HTML y `/* TODO */` en el CSS indica exactamente qué implementar.

Lee las pistas antes de escribir código — son orientativas, no instrucciones exactas.

### 3. Verificar en el browser

Abre `starter/index.html` en tu browser (arrastra el archivo o usa Live Server).

---

## ✅ Criterios de Evaluación

| Criterio | Descripción | Puntos |
|----------|-------------|--------|
| **Semántica** | Uso correcto de `header`, `nav`, `main`, `section`, `article`, `footer` | 25 |
| **Accesibilidad** | `alt` en imágenes, `aria-label` en nav, contraste adecuado | 20 |
| **Box Model** | `box-sizing: border-box` global, espaciado consistente con las 4 propiedades | 20 |
| **CSS Limpio** | Sin `!important`, selectores de clase (no ID), especificidad controlada | 20 |
| **Unidades** | `rem` para tipografía, unidades apropiadas para cada caso | 15 |

**Total: 100 puntos — Mínimo para aprobar: 70 puntos**

---

## 📌 Entregable

1. Archivo `starter/index.html` completado (sin `<!-- TODO -->` sin resolver)
2. Archivo `starter/styles.css` completado (sin `/* TODO */` sin resolver)
3. Screenshot o grabación de pantalla de la landing terminada

---

## 🔗 Recursos de Referencia

- [MDN — Elementos HTML semánticos](https://developer.mozilla.org/es/docs/Web/HTML/Element)
- [MDN — Box Model](https://developer.mozilla.org/es/docs/Learn/CSS/Building_blocks/The_box_model)
- [CSS Tricks — A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [W3C Validator](https://validator.w3.org/) — Para validar tu HTML
