# Ejercicio 01 — Colores de Marca

## 🎯 Objetivo

Aprender a extender la paleta de colores de Tailwind con una escala de colores de marca completa (9-11 tonos), y usarla en componentes UI reales.

---

## 📋 ¿Qué vas a construir?

Una paleta de colores de marca con la escala completa y una tarjeta de producto que usa exclusivamente esos colores:
- Escala `brand-*` con tonos del 50 al 950
- Botón CTA con estados hover/active/focus usando la paleta
- Badge con fondo suave (`brand-100 text-brand-700`)
- Card con borde de color (`border-brand-200`)
- Sección de swatches que muestra toda la paleta visual

---

## 🗂️ Estructura

```
01-ejercicio-colores-marca/
├── README.md         ← Esta guía
└── starter/
    └── index.html    ← Abre este archivo en tu browser
```

---

## 📝 Instrucciones

Abre `starter/index.html` y trabaja con los **4 bloques comentados** de forma progresiva:

### BLOQUE 1 — Definir la paleta brand en tailwind.config

Configura el objeto `tailwind.config` del CDN con los 11 tonos de la paleta brand.

**Conceptos a observar:**
- `tailwind.config = { theme: { extend: { colors: { brand: { ... } } } } }`
- La escala de valores: 50 (más claro) → 950 (más oscuro)
- El tono 500 es el "color base" y los demás son variaciones de luminosidad
- Sin `extend`: desaparecen los colores default de Tailwind

**Descomenta** el bloque `<script>tailwind.config = {...}</script>`.

---

### BLOQUE 2 — Swatches de la paleta

Muestra los 11 tonos de la paleta brand como cuadros de color con sus nombres de clase.

**Conceptos a observar:**
- Cada div usa `bg-brand-X` donde X es el tono
- Los tonos oscuros del 600+ muestran texto claro (`text-white`)
- Los tonos claros del 100- muestran texto oscuro (`text-brand-900`)
- Esto es exactamente cómo la documentación de Tailwind presenta sus paletas

**Descomenta** las líneas del BLOQUE 2.

---

### BLOQUE 3 — Badge y botón de marca

Construye los elementos interactivos que usan la paleta de forma semántica.

**Conceptos a observar:**
- Badge: `bg-brand-100 text-brand-700` — fondo muy suave + texto legible
- Botón: `bg-brand-500 hover:bg-brand-600 active:bg-brand-700`
- Botón outline: `border-brand-300 text-brand-600 hover:bg-brand-50`
- Focus ring: `focus:ring-2 focus:ring-brand-500/40`

**Descomenta** las líneas del BLOQUE 3.

---

### BLOQUE 4 — Card completa con paleta de marca

Construye una card de producto que use la paleta en todos sus elementos: header, imagen placeholder, contenido y footer.

**Conceptos a observar:**
- Header con gradiente suave usando la paleta: `from-brand-50 to-brand-100`
- Borde de la card: `border-brand-200`
- Texto de precio: `text-brand-600 font-bold`
- Tag/etiqueta: `bg-brand-500 text-white`
- Toda la card evita usar colores que no sean de la paleta brand o neutros

**Descomenta** las líneas del BLOQUE 4.

---

## ✅ Criterios de Éxito

Al terminar deberías poder:
- [ ] Ver los 11 swatches de la paleta brand del 50 al 950
- [ ] El botón cambia de tono en hover y active
- [ ] El focus ring del botón es visible y usa el color de marca
- [ ] La card usa solo colores de la paleta brand y gris neutro
- [ ] Sin usar ningún color default de Tailwind (sky, blue, indigo, etc.)

---

## 💡 Ayuda

Si un color no funciona: verifica que el `tailwind.config` CDN esté escrito correctamente antes del cierre del `</head>`. En CDN, la configuración de Tailwind debe estar en una etiqueta `<script>` con `tailwind.config = {...}` (no como módulo ES).
