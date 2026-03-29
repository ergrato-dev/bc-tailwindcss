# Glosario — Semana 2: Entorno de Desarrollo y Filosofía Utility-First

Términos técnicos clave de la semana, ordenados alfabéticamente.

---

## B

### Bundle
Archivo(s) final(es) generado(s) por un bundler (como Vite) que combina múltiples módulos de código fuente en uno o pocos archivos optimizados para el navegador. TailwindCSS genera un bundle CSS que solo contiene las clases usadas.

### Bundler
Herramienta que empaqueta módulos JavaScript, CSS y otros assets en archivos optimizados para producción. Vite es el bundler utilizado en este bootcamp.

---

## C

### CDN (Content Delivery Network)
Red de servidores que distribuye archivos estáticos. TailwindCSS tiene un CDN de play (`cdn.tailwindcss.com`), pero **no se recomienda en producción** porque incluye todo Tailwind sin purging.

### CSS-in-JS
Paradigma que escribe CSS usando JavaScript (ej: styled-components). Es una alternativa a utility-first, con pros/contras diferentes.

---

## D

### devDependency
Dependencia de desarrollo listada en `package.json` bajo `devDependencies`. Solo se necesita para el proceso de build, no en el runtime del navegador. `tailwindcss` y `@tailwindcss/vite` son devDependencies porque generan CSS en tiempo de build.

---

## H

### HMR (Hot Module Replacement)
Funcionalidad de Vite que actualiza el navegador automáticamente cuando cambias un archivo, sin recargar la página completa. Mantiene el estado de la aplicación entre cambios.

---

## I

### IntelliSense (Tailwind)
Extensión de VS Code (`Tailwind CSS IntelliSense`) que añade autocompletado, documentación inline y resaltado de errores para clases Tailwind. Esencial para trabajar eficientemente.

---

## J

### JIT (Just-in-Time Compiler)
Motor de Tailwind (activo por defecto desde v3, mejorado en v4) que genera clases CSS bajo demanda mientras detecta qué clases usas en tus archivos. Resultado: CSS final ligerísimo.

---

## P

### pnpm
Gestor de paquetes Node.js alternativo a `npm` y `yarn`. Más rápido y eficiente en espacio de disco gracias al almacenamiento de paquetes como links simbólicos. Es el gestor recomendado en este bootcamp.

### PostCSS
Transformador de CSS usado internamente por TailwindCSS para procesar los imports y directivas. En Tailwind v4 + Vite, el plugin `@tailwindcss/vite` gestiona esto automáticamente.

### Purging
Proceso por el cual Tailwind escanea tus archivos de código y elimina del CSS final todas las clases que no usas. Convierte ~3MB de CSS completo en ~10-50KB. También llamado "tree-shaking" para CSS.

---

## U

### Utility-First
Filosofía de diseño CSS donde se aplican clases de propósito único (utilidades) directamente al HTML en lugar de crear clases de componentes con nombres abstractos. Tailwind es el framework utility-first más usado.

---

## V

### Variante (Tailwind)
Prefijo que condiciona cuándo aplica una clase. Ejemplos: `hover:` (al hacer hover), `md:` (en pantallas ≥ 768px), `dark:` (modo oscuro), `focus:` (al recibir foco). Sintaxis: `variante:clase`.

### Vite
Bundler y servidor de desarrollo extremadamente rápido para proyectos frontend. Usa ES Modules nativos del browser en desarrollo para eliminar el tiempo de bundle, y Rollup para el build de producción.

---

## `@import "tailwindcss"`
La directiva CSS que activa TailwindCSS en tu archivo CSS principal en Tailwind v4. Reemplaza las tres directivas legacy de v3 (`@tailwind base`, `@tailwind components`, `@tailwind utilities`).
