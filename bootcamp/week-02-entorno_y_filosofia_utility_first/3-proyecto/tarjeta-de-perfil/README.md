# Proyecto Semana 2: Tarjeta de Perfil

## 📋 Descripción

Construye una **tarjeta de perfil** estilo GitHub/LinkedIn usando exclusivamente clases TailwindCSS v4 en un proyecto Vite. Este es tu primer proyecto real con Tailwind.

---

## 🎯 Objetivos

- Configurar y usar correctamente Vite + TailwindCSS v4
- Aplicar las clases aprendidas para construir un UI completo
- Diseñar un componente responsive que funcione en mobile y desktop
- Usar HTML semántico con Tailwind

---

## 📐 Diseño Esperado

```
┌─────────────────────────────┐
│    [ Avatar circular ]      │  ← bg-color + rounded-full
│                             │
│    Nombre Completo          │  ← text-xl font-bold
│    @usuario · rol           │  ← text-sm text-gray-500
│                             │
│    Bio corta del usuario    │  ← text-sm text-center
│                             │
│  [ Repos ] [ Stars ] [ PRs ]│  ← grid stats
│                             │
│  [ Siguiente →   ]          │  ← botón de acción
└─────────────────────────────┘
```

---

## 📁 Estructura

```
3-proyecto/tarjeta-de-perfil/
├── README.md
└── starter/
    └── index.html
```

> Nota: No hay `solution/` — es acceso solo para instructores.

---

## 🚀 Instrucciones

### 1. Crear el proyecto

```bash
pnpm create vite@latest tarjeta-perfil -- --template vanilla
cd tarjeta-perfil
pnpm install
pnpm add -D tailwindcss @tailwindcss/vite
```

### 2. Configurar

Actualiza `vite.config.js` y `src/style.css` como aprendiste en la teoría y ejercicios.

### 3. Implementar la tarjeta

Abre `starter/index.html` y completa todos los `<!-- TODO -->`.

### 4. Verificar

```bash
pnpm dev
```

---

## 📋 Requisitos del Proyecto

### HTML Semántico

- [ ] La tarjeta usa `<article>` como elemento contenedor
- [ ] La imagen del avatar tiene `alt` descriptivo
- [ ] Las estadísticas usan `<dl>`, `<dt>`, `<dd>` o elementos semánticos equivalentes

### Tailwind

- [ ] `@import "tailwindcss"` en el CSS (no `@tailwind` legacy)
- [ ] 0 líneas de CSS personalizado (todo con clases Tailwind)
- [ ] Clases en orden: layout → sizing → spacing → typography → colors → effects

### Responsive

- [ ] En mobile (< 640px): tarjeta a ancho completo
- [ ] En desktop (≥ 640px): tarjeta centrada con `max-w-sm`

### Diseño

- [ ] Avatar circular con `rounded-full`
- [ ] Nombre con tipografía prominente
- [ ] Al menos 3 estadísticas numéricas
- [ ] Botón de acción con hover visible

---

## 🎨 Recursos de Inspiración

- [GitHub Profile](https://github.com/) — Para el estilo de las estadísticas
- [Tailwind Play](https://play.tailwindcss.com/) — Para experimentar rápido
