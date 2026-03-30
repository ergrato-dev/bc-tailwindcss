# Glosario — Semana 12

## Integración con Frameworks, Producción y Ecosistema Tailwind

---

## A

**App Router**
Sistema de routing de Next.js 13+ basado en carpetas dentro de `/app`. Soporta Server Components, Client Components, layouts anidados y carga en streaming. Reemplaza al antiguo `/pages` directory.

**`@apply`**
Directiva de Tailwind que permite usar clases utilitarias dentro de CSS personalizado. Usar con moderación — puede romper el tree-shaking si se abusa.

---

## C

**Client Component**
En Next.js App Router, un componente que se renderiza en el cliente (browser). Se declara con `'use client'` al inicio del archivo. Necesario para hooks (`useState`, `useEffect`), event listeners y acceso al DOM/localStorage.

**`clsx`**
Librería que construye strings de `className` condicionalmente. Ej: `clsx('base', isActive && 'active', isDark && 'dark')`.

**`cn()`**
Helper estándar que combina `clsx` + `tailwind-merge`. Usado en shadcn/ui y ampliamente en proyectos de React/Next.js para manejar clases condicionales sin conflictos.

**`cva` (class-variance-authority)**
Librería para definir variantes de componentes con TypeScript. Permite declarar todas las variantes de un componente (variant, size, etc.) con tipos seguros. Base del sistema de variantes de shadcn/ui.

---

## D

**`dangerouslySetInnerHTML`**
Prop de React equivalente a `innerHTML` en HTML. Se usa para insertar el script anti-flash en `app/layout.jsx` de Next.js, ya que este script debe ejecutarse antes de la hidratación. El nombre advierte que hay que evitar inyectar HTML de fuentes no confiables.

**`data-theme`**
Atributo HTML usado por daisyUI para aplicar temas. Al cambiar `document.documentElement.setAttribute('data-theme', 'dark')`, daisyUI actualiza todas las variables CSS del tema automáticamente.

**daisyUI**
Plugin de Tailwind que añade clases de componentes semánticas (`btn`, `card`, `badge`, etc.) usando CSS variables internamente. Los estilos cambian de tema con solo modificar `data-theme`.

---

## H

**Hydration**
Proceso por el que React "toma control" del HTML pre-renderizado por el servidor y lo hace interactivo en el cliente. Si el HTML del servidor difiere del cliente, React muestra una advertencia de hidratación.

---

## J

**JIT (Just-In-Time)**
Modo de compilación de Tailwind (activo por defecto desde v3/v4) que genera solo las clases utilizadas en el código, resultando en un CSS mínimo para producción.

---

## N

**`next/font`**
Módulo de Next.js para cargar fuentes (Google Fonts o locales) con zero layout shift. Genera automáticamente variables CSS que se pueden usar en `tailwind.config.js`.

---

## P

**PostCSS**
Herramienta de transformación de CSS. Tailwind funciona como un plugin de PostCSS. En Next.js, el archivo `postcss.config.mjs` configura qué plugins se ejecutan sobre el CSS.

**Purging / Tree-shaking**
Proceso de eliminar clases CSS no utilizadas del bundle final. Tailwind JIT hace esto automáticamente analizando los archivos configurados en `content`. Las clases generadas dinámicamente (ej: `` `bg-${color}-500` ``) NO se detectan y se eliminan.

---

## R

**Radix UI**
Librería de primitivos de UI accesibles y sin estilos. Es la base sobre la que shadcn/ui construye sus componentes. Maneja accesibilidad (ARIA, focus management, keyboard navigation) automáticamente.

---

## S

**Server Component**
En Next.js App Router, componente renderizado en el servidor. Por defecto todos los componentes son Server Components. Pueden ser async, tienen acceso a la base de datos y el sistema de archivos, pero NO pueden usar hooks ni event handlers.

**shadcn/ui**
Colección de componentes que se *copian* al proyecto (en `components/ui/`) en lugar de instalarse como dependencia. Usa Radix UI + Tailwind + `cva`. Totalmente personalizable porque el código es tuyo.

**`suppressHydrationWarning`**
Prop de React que suprime advertencias de hidratación en un elemento específico. Se usa en `<html>` o `<body>` cuando el script anti-flash modifica clases/atributos antes de que React hidrate.

---

## T

**`tailwind-merge`**
Librería que resuelve conflictos entre clases Tailwind en tiempo de ejecución. Por ejemplo: `twMerge('px-4 px-8')` → `'px-8'`. Esencial cuando se combinan clases desde múltiples fuentes o se permite override con `className`.

---

## U

**`use client`**
Directiva de React Server Components. Puesta al inicio de un archivo, marca ese componente y todos sus hijos como Client Components, habilitando el uso de hooks y event handlers.

---

## V

**Variantes de componente**
Patrón de diseño donde un componente acepta una prop `variant` (y a veces `size`) para determinar sus clases. Implementado con un objeto mapa de clases o con la librería `cva`. Ejemplo: `<Button variant="primary" size="lg">`.

**Vercel**
Plataforma de deploy creada por el equipo de Next.js. Detecta automáticamente el framework, ejecuta el build y despliega. Cada merge a `main` genera un nuevo deploy automáticamente.

---

## W

**WCAG (Web Content Accessibility Guidelines)**
Estándar internacional de accesibilidad web. El nivel AA requiere contraste mínimo de 4.5:1 para texto normal. Tailwind incluye utilidades `focus-visible:ring-*` para cumplir los requisitos de navegación por teclado.
